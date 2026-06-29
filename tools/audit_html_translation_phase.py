#!/usr/bin/env python3
"""Audit one translated HTML documentation page.

This is intentionally conservative: it proves the HTML tag stream is unchanged,
the target can be reproduced by replaying the item-level JSONL translations, and
terminology/layout-critical text was preserved. It also reports source/ASCII
residuals with lightweight heuristics so page-specific audits only need to add
required phrases or explicit allowed IDs.
"""

from __future__ import annotations

import argparse
import html
import importlib.util
import json
import re
import sys
from pathlib import Path


def load_pipeline(root: Path):
    script = root / "tools" / "translate_html_docs.py"
    spec = importlib.util.spec_from_file_location("translate_html_docs", script)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Unable to load {script}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def html_variants(text: str) -> set[str]:
    escaped = html.escape(text, quote=False)
    return {
        text,
        html.escape(text, quote=True),
        escaped,
        text.replace(" ", "&nbsp;"),
        escaped.replace(" ", "&nbsp;"),
    }


def contains_variant(markup: str, text: str) -> bool:
    return any(variant in markup for variant in html_variants(text))


def cjk_count(text: str) -> int:
    return sum(1 for char in text if "\u4e00" <= char <= "\u9fff")


def ascii_letter_count(text: str) -> int:
    return sum(1 for char in text if ("A" <= char <= "Z") or ("a" <= char <= "z"))


def looks_like_ui_or_identifier(text: str, preserve_terms: set[str]) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    if stripped in preserve_terms:
        return True
    if any(term and term in stripped for term in preserve_terms):
        return True
    if any(token in stripped for token in [">", "=", "::", "/", "_", "@", "#"]):
        return True
    if re.search(r"\b(?:Pxr|Rix|Ri|USD|OSL|AOV|LPE|XPU|RIS|RfM|Maya|RenderMan)\w*\b", stripped):
        return True
    if re.fullmatch(r"[A-Za-z0-9_.:+ ：-]+", stripped) and len(stripped) <= 80:
        words = [word for word in re.split(r"\s+", stripped) if word]
        if len(words) <= 8:
            return True
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", stripped):
        return True
    return False


def load_rows(path: Path) -> tuple[list[dict], dict[str, str], list[dict]]:
    rows: list[dict] = []
    translations: dict[str, str] = {}
    duplicates: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        rows.append(row)
        item_id = row.get("item_id")
        if item_id in translations:
            duplicates.append({"line": line_number, "item_id": item_id})
        translations[item_id] = row.get("text", "")
    return rows, translations, duplicates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", type=int, required=True)
    parser.add_argument("--file", required=True, help="Relative HTML path under --input")
    parser.add_argument("--translation", required=True, help="Item-level JSONL translation")
    parser.add_argument("--input", default="renderman-docs-27/html")
    parser.add_argument("--output", default="renderman-docs-27/html-zh")
    parser.add_argument("--glossary", default="renderman-docs-27/glossary/renderman_terminology.json")
    parser.add_argument("--scope", default="article", choices=["article", "body", "all"])
    parser.add_argument("--report")
    parser.add_argument("--allow-source-id", action="append", default=[])
    parser.add_argument("--allow-ascii-id", action="append", default=[])
    parser.add_argument("--required-phrase", action="append", default=[])
    parser.add_argument("--order-phrase", action="append", default=[])
    parser.add_argument("--long-source-len", type=int, default=18)
    parser.add_argument("--ascii-letters", type=int, default=8)
    parser.add_argument("--ascii-ratio", type=float, default=1.4)
    parser.add_argument("--no-fail", action="store_true")
    args = parser.parse_args()

    root = Path.cwd()
    pipeline = load_pipeline(root)
    input_root = (root / args.input).resolve()
    source = input_root / args.file
    target = (root / args.output).resolve() / args.file
    translation_path = (root / args.translation).resolve()
    glossary = pipeline.load_glossary((root / args.glossary).resolve())
    preserve_terms = {term.get("zh") or term.get("en", "") for term in glossary.get("terms", []) if term.get("preserve")}
    preserve_terms |= {term.get("en", "") for term in glossary.get("terms", []) if term.get("preserve")}

    source_markup = source.read_text(encoding="utf-8")
    target_markup = target.read_text(encoding="utf-8")
    file_id = pipeline.make_file_id(source.resolve(), input_root)
    items, tokens = pipeline.extract_text_items(source_markup, file_id, args.scope)
    rows, translations, duplicate_rows = load_rows(translation_path)

    source_ids = [item.item_id for item in items]
    row_ids = [row.get("item_id") for row in rows]
    missing_item_ids = [item_id for item_id in source_ids if item_id not in translations]
    extra_item_ids = [item_id for item_id in row_ids if item_id not in source_ids]
    rendered_markup = pipeline.render_tokens(tokens, {}, translations)

    direct_placement_missing = []
    for item in items:
        translated = translations.get(item.item_id, "")
        if translated and translated != item.source and not contains_variant(target_markup, translated):
            direct_placement_missing.append({"item_id": item.item_id, "text": translated})

    allowed_source_ids = set(args.allow_source_id)
    actionable_long_source_residuals = []
    accepted_long_source_residuals = []
    for item in items:
        source_text = item.source.strip()
        translated = translations.get(item.item_id, "")
        if len(source_text) < args.long_source_len:
            continue
        if source_text not in target_markup and html.escape(source_text, quote=False) not in target_markup:
            continue
        record = {"item_id": item.item_id, "source": source_text}
        if (
            item.item_id in allowed_source_ids
            or (translated != item.source and cjk_count(translated) > 0)
            or looks_like_ui_or_identifier(source_text, preserve_terms)
        ):
            accepted_long_source_residuals.append(record)
        else:
            actionable_long_source_residuals.append(record)

    allowed_ascii_ids = set(args.allow_ascii_id)
    actionable_ascii_heavy_residuals = []
    accepted_ascii_heavy_residuals = []
    for item in items:
        translated = translations.get(item.item_id, "")
        letters = ascii_letter_count(translated)
        cjk = cjk_count(translated)
        if letters < args.ascii_letters or (cjk and letters / max(cjk, 1) < args.ascii_ratio):
            continue
        record = {
            "item_id": item.item_id,
            "text": translated,
            "ascii_letters": letters,
            "cjk_chars": cjk,
        }
        if (
            item.item_id in allowed_ascii_ids
            or looks_like_ui_or_identifier(translated, preserve_terms)
            or (cjk >= 5 and translated != item.source)
        ):
            accepted_ascii_heavy_residuals.append(record)
        else:
            actionable_ascii_heavy_residuals.append(record)

    required_phrase_missing = [phrase for phrase in args.required_phrase if not contains_variant(target_markup, phrase)]
    order_patterns = args.order_phrase or args.required_phrase
    positions = []
    last = -1
    section_order_ok = True
    for phrase in order_patterns:
        position = -1
        for variant in html_variants(phrase):
            found = target_markup.find(variant)
            if found != -1:
                position = found
                break
        positions.append({"pattern": phrase, "position": position})
        if position == -1 or position <= last:
            section_order_ok = False
        if position != -1:
            last = position

    report = {
        "phase": args.phase,
        "file": args.file,
        "file_id": file_id,
        "source_items": len(items),
        "translation_rows": len(rows),
        "source_items_match_translation_rows": source_ids == row_ids,
        "duplicate_rows": duplicate_rows,
        "missing_item_ids": missing_item_ids,
        "extra_item_ids": extra_item_ids,
        "tag_fingerprint_identical": pipeline.tag_fingerprint(source_markup) == pipeline.tag_fingerprint(target_markup),
        "rendered_markup_matches_target_markup": rendered_markup == target_markup,
        "glossary_violations": pipeline.validate_glossary(items, {}, glossary, translations),
        "direct_placement_missing": direct_placement_missing,
        "actionable_long_source_residuals": actionable_long_source_residuals,
        "accepted_long_source_residuals": accepted_long_source_residuals,
        "actionable_ascii_heavy_residuals": actionable_ascii_heavy_residuals,
        "accepted_ascii_heavy_residuals": accepted_ascii_heavy_residuals,
        "required_phrase_missing": required_phrase_missing,
        "section_order_positions": positions,
        "section_order_ok": section_order_ok,
    }
    report["passed"] = all(
        [
            report["source_items"] == report["translation_rows"],
            report["source_items_match_translation_rows"],
            not duplicate_rows,
            not missing_item_ids,
            not extra_item_ids,
            report["tag_fingerprint_identical"],
            report["rendered_markup_matches_target_markup"],
            not report["glossary_violations"],
            not direct_placement_missing,
            not actionable_long_source_residuals,
            not actionable_ascii_heavy_residuals,
            not required_phrase_missing,
            section_order_ok,
        ]
    )

    report_path = Path(args.report) if args.report else root / "renderman-docs-27" / "phases" / f"phase-{args.phase}-independent-audit.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = {
        "phase": report["phase"],
        "passed": report["passed"],
        "source_items": report["source_items"],
        "translation_rows": report["translation_rows"],
        "layout_tag_ok": report["tag_fingerprint_identical"],
        "rendered_ok": report["rendered_markup_matches_target_markup"],
        "glossary_violations": len(report["glossary_violations"]),
        "direct_placement_missing": len(report["direct_placement_missing"]),
        "actionable_long_source_residuals": len(report["actionable_long_source_residuals"]),
        "actionable_ascii_heavy_residuals": len(report["actionable_ascii_heavy_residuals"]),
        "required_phrase_missing": len(report["required_phrase_missing"]),
        "report": str(report_path),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if report["passed"] or args.no_fail else 1


if __name__ == "__main__":
    raise SystemExit(main())
