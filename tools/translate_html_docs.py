#!/usr/bin/env python3
"""
Translate static HTML documentation while keeping layout-critical markup intact.

The core safety rule is simple: the translator never receives complete HTML.
This script tokenizes HTML, extracts only eligible visible text nodes, translates
those text nodes, and writes the original tags/attributes back byte-for-byte.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable


TAG_RE = re.compile(r"(?is)<!--.*?-->|<!\[CDATA\[.*?\]\]>|<!DOCTYPE[^>]*>|<[^>]*>")
TAG_NAME_RE = re.compile(r"^<\s*/?\s*([a-zA-Z][\w:-]*)")
END_TAG_RE = re.compile(r"^<\s*/")
TRANSLATE_NO_RE = re.compile(r"""\btranslate\s*=\s*(['"]?)no\1""", re.IGNORECASE)
CLASS_NO_TRANSLATE_RE = re.compile(
    r"""\bclass\s*=\s*(['"])(?:(?!\1).)*(?:notranslate|no-translate)(?:(?!\1).)*\1""",
    re.IGNORECASE,
)
EDGE_WS_RE = re.compile(r"^((?:\s|&nbsp;|&#160;|&#x[aA]0;)*)(.*?)((?:\s|&nbsp;|&#160;|&#x[aA]0;)*)$", re.DOTALL)
ZH_LEADING_PUNCT_RE = re.compile(r"^[，。！？；：、（）【】《》「」『』]")

SKIP_TAGS = {
    "script",
    "style",
    "pre",
    "code",
    "kbd",
    "samp",
    "var",
    "svg",
    "math",
    "textarea",
    "noscript",
}
VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


@dataclass
class TextItem:
    file_id: str
    index: int
    source: str
    leading: str
    trailing: str

    @property
    def key(self) -> str:
        return hashlib.sha256(self.source.encode("utf-8")).hexdigest()

    @property
    def item_id(self) -> str:
        return f"{self.file_id}:{self.index}"


def read_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def tag_name(tag: str) -> str | None:
    match = TAG_NAME_RE.match(tag)
    return match.group(1).lower() if match else None


def is_end_tag(tag: str) -> bool:
    return bool(END_TAG_RE.match(tag))


def is_self_closing(tag: str, name: str | None) -> bool:
    return not name or name in VOID_TAGS or tag.rstrip().endswith("/>")


def element_disables_translation(tag: str, name: str | None) -> bool:
    if not name:
        return False
    return name in SKIP_TAGS or bool(TRANSLATE_NO_RE.search(tag) or CLASS_NO_TRANSLATE_RE.search(tag))


def scope_ranges(markup: str, scope: str) -> list[tuple[int, int]]:
    if scope == "all":
        return [(0, len(markup))]

    tag = "article" if scope == "article" else "body"
    start_match = re.search(rf"(?is)<{tag}\b[^>]*>", markup)
    end_match = re.search(rf"(?is)</{tag}\s*>", markup)
    if start_match and end_match and start_match.end() <= end_match.start():
        return [(start_match.end(), end_match.start())]

    if scope == "article":
        return scope_ranges(markup, "body")
    return [(0, len(markup))]


def in_ranges(position: int, ranges: list[tuple[int, int]]) -> bool:
    return any(start <= position < end for start, end in ranges)


def split_edge_whitespace(raw: str) -> tuple[str, str, str]:
    match = EDGE_WS_RE.match(raw)
    if not match:
        return "", raw, ""
    leading = match.group(1) or ""
    trailing = match.group(3) or ""
    core = raw[len(leading) : len(raw) - len(trailing) if trailing else len(raw)]
    return leading, core, trailing


def looks_translatable(text: str) -> bool:
    decoded = html.unescape(text).strip()
    if decoded in {".", "!", "?", ":", ";"}:
        return True
    if len(decoded) < 2:
        return False
    if not re.search(r"[A-Za-z]", decoded):
        return False
    if re.fullmatch(r"[\W\d_]+", decoded):
        return False
    return True


def extract_text_items(markup: str, file_id: str, scope: str) -> tuple[list[TextItem], list[tuple[str, TextItem | None]]]:
    ranges = scope_ranges(markup, scope)
    tokens: list[tuple[str, TextItem | None]] = []
    items: list[TextItem] = []
    stack: list[tuple[str, bool]] = []
    cursor = 0

    def add_text(raw: str, start: int) -> None:
        nonlocal items
        if not raw:
            return
        if not in_ranges(start, ranges) or any(skip for _, skip in stack):
            tokens.append((raw, None))
            return
        leading, core_raw, trailing = split_edge_whitespace(raw)
        if not looks_translatable(core_raw):
            tokens.append((raw, None))
            return
        item = TextItem(
            file_id=file_id,
            index=len(items),
            source=html.unescape(core_raw),
            leading=leading,
            trailing=trailing,
        )
        items.append(item)
        tokens.append((raw, item))

    for match in TAG_RE.finditer(markup):
        add_text(markup[cursor : match.start()], cursor)
        tag = match.group(0)
        tokens.append((tag, None))

        name = tag_name(tag)
        if name:
            if is_end_tag(tag):
                for pos in range(len(stack) - 1, -1, -1):
                    if stack[pos][0] == name:
                        del stack[pos:]
                        break
            elif not is_self_closing(tag, name):
                stack.append((name, element_disables_translation(tag, name)))
        cursor = match.end()

    add_text(markup[cursor:], cursor)
    return items, tokens


def tag_fingerprint(markup: str) -> list[str]:
    return TAG_RE.findall(markup)


def translation_for_item(item: TextItem, translations: dict[str, str], item_translations: dict[str, str] | None = None) -> str:
    if item_translations and item.item_id in item_translations:
        return item_translations[item.item_id]
    return translations.get(item.key, item.source)


def render_tokens(
    tokens: list[tuple[str, TextItem | None]],
    translations: dict[str, str],
    item_translations: dict[str, str] | None = None,
) -> str:
    rendered: list[str] = []
    for raw, item in tokens:
        if item is None:
            rendered.append(raw)
            continue
        translated = translation_for_item(item, translations, item_translations)
        if translated == item.source:
            rendered.append(raw)
            continue
        leading = "" if ZH_LEADING_PUNCT_RE.match(translated) else item.leading
        rendered.append(leading + html.escape(translated, quote=False) + item.trailing)
    return "".join(rendered)


def make_file_id(path: Path, root: Path) -> str:
    return hashlib.sha1(str(path.relative_to(root)).encode("utf-8")).hexdigest()[:10]


class Translator:
    def translate_many(self, items: list[TextItem]) -> dict[str, str]:
        raise NotImplementedError


class CopyTranslator(Translator):
    def translate_many(self, items: list[TextItem]) -> dict[str, str]:
        return {item.key: item.source for item in items}


def parse_model_json(content: str) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        start = content.find("{")
        end = content.rfind("}")
        if start >= 0 and end > start:
            return json.loads(content[start : end + 1])
        raise


def batched(items: list[TextItem], batch_size: int) -> Iterable[list[TextItem]]:
    for index in range(0, len(items), batch_size):
        yield items[index : index + batch_size]


def load_export_translations(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    translations: dict[str, str] = {}
    item_translations: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("item_id"):
            item_translations[row["item_id"]] = row["text"]
        else:
            translations[row["id"]] = row["text"]
    return translations, item_translations


def export_items(path: Path, items: list[TextItem]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for item in items:
            handle.write(json.dumps({"id": item.key, "item_id": item.item_id, "text": item.source}, ensure_ascii=False) + "\n")


def html_files(root: Path, limit: int | None, only: list[str] | None = None, only_file: str | None = None) -> list[Path]:
    if only_file:
        entries = [line.strip() for line in Path(only_file).read_text(encoding="utf-8").splitlines()]
        only = [*(only or []), *[entry for entry in entries if entry and not entry.startswith("#")]]
    if only:
        files = []
        for entry in only:
            path = (root / entry).resolve()
            if not path.exists():
                raise SystemExit(f"Requested HTML file does not exist: {entry}")
            if root not in path.parents and path != root:
                raise SystemExit(f"Requested HTML file is outside input root: {entry}")
            files.append(path)
    else:
        files = sorted(root.rglob("*.html"))
    return files[:limit] if limit else files


def build_translator(args: argparse.Namespace) -> Translator:
    if args.provider == "copy":
        return CopyTranslator()
    raise SystemExit(f"Provider {args.provider} does not translate directly")


def load_glossary(path: Path) -> dict:
    if not path.exists():
        return {"terms": [], "identifier_prefixes_to_preserve": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    data["terms"] = sorted(data.get("terms", []), key=lambda term: len(term.get("en", "")), reverse=True)
    return data


def contains_term(text: str, term: str) -> bool:
    if not term:
        return False
    if re.match(r"^[A-Za-z0-9_]+$", term):
        return bool(re.search(rf"(?<![A-Za-z0-9_]){re.escape(term)}(?![A-Za-z0-9_])", text))
    return term in text


def validate_glossary(
    items: Iterable[TextItem],
    translations: dict[str, str],
    glossary: dict,
    item_translations: dict[str, str] | None = None,
) -> list[dict]:
    violations = []
    preserve_terms = [term for term in glossary.get("terms", []) if term.get("preserve")]
    prefixes = glossary.get("identifier_prefixes_to_preserve", [])
    identifier_re = re.compile(
        r"\b(?:" + "|".join(re.escape(prefix) for prefix in prefixes if prefix.isalnum()) + r")[A-Za-z0-9_]*\b"
    ) if prefixes else None

    seen: set[tuple[str, str]] = set()
    for item in items:
        translated = translation_for_item(item, translations, item_translations)
        for term in preserve_terms:
            source_term = term.get("en", "")
            required = term.get("zh") or source_term
            if contains_term(item.source, source_term) and required not in translated:
                key = (item.item_id, required)
                if key not in seen:
                    seen.add(key)
                    violations.append(
                        {
                            "item_id": item.item_id,
                            "missing": required,
                            "source_term": source_term,
                            "source": item.source,
                            "translation": translated,
                        }
                    )
        if identifier_re:
            for identifier in sorted(set(identifier_re.findall(item.source))):
                if identifier not in translated:
                    key = (item.item_id, identifier)
                    if key not in seen:
                        seen.add(key)
                        violations.append(
                            {
                                "item_id": item.item_id,
                                "missing": identifier,
                                "source_term": identifier,
                                "source": item.source,
                                "translation": translated,
                            }
                        )
    return violations


def process_files(args: argparse.Namespace) -> dict:
    input_root = Path(args.input).resolve()
    output_root = Path(args.output).resolve()
    cache_path = Path(args.cache).resolve()
    cache = read_json(cache_path, {})
    item_translations: dict[str, str] = {}
    glossary = load_glossary(Path(args.glossary).resolve()) if args.glossary else {"terms": []}

    file_records = []
    all_missing: dict[str, TextItem] = {}
    extracted: list[tuple[Path, Path, str, list[tuple[str, TextItem | None]], list[TextItem]]] = []

    for source_path in html_files(input_root, args.limit_files, args.only, args.only_file):
        relative = source_path.relative_to(input_root)
        target_path = output_root / relative
        markup = source_path.read_text(encoding="utf-8", errors="ignore")
        file_id = make_file_id(source_path, input_root)
        items, tokens = extract_text_items(markup, file_id, args.scope)
        extracted.append((source_path, target_path, markup, tokens, items))
        for item in items:
            if item.key not in cache:
                all_missing[item.key] = item

    missing_items = list(all_missing.values())
    if args.provider == "jsonl-export":
        export_items(Path(args.export_path), missing_items)
        return {
            "mode": "jsonl-export",
            "files": len(extracted),
            "items_exported": len(missing_items),
            "export_path": args.export_path,
        }

    if args.provider == "jsonl-apply":
        export_translations, item_translations = load_export_translations(Path(args.apply_path))
        cache.update(export_translations)
    else:
        translator = build_translator(args)
        for batch_index, batch in enumerate(batched(missing_items, args.batch_size), 1):
            translated = translator.translate_many(batch)
            cache.update(translated)
            if batch_index % 10 == 0:
                write_json(cache_path, cache)
                print(f"Translated {min(batch_index * args.batch_size, len(missing_items))}/{len(missing_items)} unique text nodes", flush=True)

    write_json(cache_path, cache)

    layout_errors = []
    glossary_violations = []
    all_items_for_validation = []
    for source_path, target_path, original_markup, tokens, items in extracted:
        all_items_for_validation.extend(items)
        translated_markup = render_tokens(tokens, cache, item_translations)
        if tag_fingerprint(original_markup) != tag_fingerprint(translated_markup):
            layout_errors.append(str(source_path))
            if args.fail_on_layout_change:
                continue
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(translated_markup, encoding="utf-8")
        file_records.append(
            {
                "source": str(source_path),
                "target": str(target_path),
                "text_nodes": len(items),
                "changed": translated_markup != original_markup,
            }
        )

    report = {
        "input": str(input_root),
        "output": str(output_root),
        "provider": args.provider,
        "scope": args.scope,
        "target_language": args.target_lang,
        "files": len(extracted),
        "written_files": len(file_records),
        "unique_text_nodes": len({item.key for _, _, _, _, items in extracted for item in items}),
        "new_unique_text_nodes": len(missing_items),
        "layout_errors": layout_errors,
        "glossary_violations": validate_glossary(all_items_for_validation, cache, glossary, item_translations),
        "records": file_records,
    }
    write_json(Path(args.report), report)
    if layout_errors and args.fail_on_layout_change:
        raise SystemExit(f"Layout validation failed for {len(layout_errors)} files")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="renderman-docs-27/html", help="source HTML root")
    parser.add_argument("--output", default="renderman-docs-27/html-zh", help="translated HTML root")
    parser.add_argument("--scope", choices=["article", "body", "all"], default="article")
    parser.add_argument("--provider", choices=["copy", "jsonl-export", "jsonl-apply"], default="copy")
    parser.add_argument("--source-lang", default="English")
    parser.add_argument("--target-lang", default="Simplified Chinese")
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--cache", default="renderman-docs-27/translation-cache.json")
    parser.add_argument("--report", default="renderman-docs-27/translation-report.json")
    parser.add_argument("--glossary", default="renderman-docs-27/glossary/renderman_terminology.json")
    parser.add_argument("--export-path", default="renderman-docs-27/translation-items.jsonl")
    parser.add_argument("--apply-path", default="renderman-docs-27/translation-items.translated.jsonl")
    parser.add_argument("--only", action="append", help="relative HTML path under --input to process; may be repeated")
    parser.add_argument("--only-file", help="file containing relative HTML paths under --input")
    parser.add_argument("--limit-files", type=int)
    parser.add_argument("--fail-on-layout-change", action="store_true", default=True)
    parser.add_argument("--allow-layout-change", dest="fail_on_layout_change", action="store_false")
    args = parser.parse_args()

    report = process_files(args)
    print(json.dumps({k: v for k, v in report.items() if k != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
