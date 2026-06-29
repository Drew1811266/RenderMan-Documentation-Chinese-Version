#!/usr/bin/env python3
"""Create one page translation packet for Codex-authored translation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from translate_html_docs import extract_text_items, load_glossary, make_file_id  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html_file", help="HTML file to translate")
    parser.add_argument("--input-root", default="renderman-docs-27/html")
    parser.add_argument("--output-root", default="renderman-docs-27/html-zh")
    parser.add_argument("--scope", choices=["article", "body", "all"], default="article")
    parser.add_argument("--glossary", default="renderman-docs-27/glossary/renderman_terminology.json")
    parser.add_argument("--pack-dir", default="renderman-docs-27/codex-translation-packs")
    args = parser.parse_args()

    input_root = Path(args.input_root).resolve()
    source_path = Path(args.html_file).resolve()
    output_root = Path(args.output_root).resolve()
    relative = source_path.relative_to(input_root)
    target_path = output_root / relative
    glossary = load_glossary(Path(args.glossary).resolve())

    markup = source_path.read_text(encoding="utf-8", errors="ignore")
    file_id = make_file_id(source_path, input_root)
    items, _ = extract_text_items(markup, file_id, args.scope)
    pack = {
        "source_html": str(source_path),
        "target_html": str(target_path),
        "relative_path": str(relative),
        "scope": args.scope,
        "translation_jsonl": str(
            Path("renderman-docs-27/codex-translations") / f"{relative.as_posix().replace('/', '__')}.jsonl"
        ),
        "glossary": {
            "rules": glossary.get("rules", []),
            "protected_terms": [
                {"en": term["en"], "required": term.get("zh") or term["en"], "note": term.get("note", "")}
                for term in glossary.get("terms", [])
                if term.get("preserve")
            ],
        },
        "items": [{"id": item.key, "item_id": item.item_id, "text": item.source} for item in items],
    }

    pack_dir = Path(args.pack_dir)
    pack_path = pack_dir / f"{relative.as_posix().replace('/', '__')}.json"
    pack_path.parent.mkdir(parents=True, exist_ok=True)
    pack_path.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(pack_path)
    print(f"items={len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
