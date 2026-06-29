#!/usr/bin/env python3
"""Precheck a Codex-authored HTML translation JSONL before applying it."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


def load_pipeline_module(root: Path):
    module_path = root / "tools" / "translate_html_docs.py"
    spec = importlib.util.spec_from_file_location("translate_html_docs", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate JSONL item coverage, order, duplicates, and glossary terms."
    )
    parser.add_argument("--phase", type=int, required=True)
    parser.add_argument("--file", required=True, help="Source-relative HTML path.")
    parser.add_argument("--translation", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--input", default="renderman-docs-27/html")
    parser.add_argument("--glossary", default="renderman-docs-27/glossary/renderman_terminology.json")
    parser.add_argument("--scope", default="article")
    parser.add_argument("--no-fail", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path.cwd()
    pipeline = load_pipeline_module(root)

    input_root = root / args.input
    source = input_root / args.file
    translation_path = root / args.translation
    report_path = root / args.report
    glossary_path = root / args.glossary

    file_id = pipeline.make_file_id(source.resolve(), input_root)
    items, _ = pipeline.extract_text_items(
        source.read_text(encoding="utf-8"),
        file_id,
        scope=args.scope,
    )

    rows: list[dict[str, str]] = []
    translations: dict[str, str] = {}
    duplicate_item_ids: list[str] = []
    seen: set[str] = set()

    for line_number, line in enumerate(translation_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        item_id = row.get("item_id")
        text = row.get("text")
        if not isinstance(item_id, str) or not isinstance(text, str):
            raise ValueError(f"Invalid row at line {line_number}: expected string item_id and text")
        rows.append({"item_id": item_id, "text": text})
        if item_id in seen:
            duplicate_item_ids.append(item_id)
        seen.add(item_id)
        translations[item_id] = text

    source_ids = [item.item_id for item in items]
    row_ids = [row["item_id"] for row in rows]
    source_id_set = set(source_ids)
    missing_item_ids = [item_id for item_id in source_ids if item_id not in translations]
    extra_item_ids = [item_id for item_id in row_ids if item_id not in source_id_set]

    glossary = pipeline.load_glossary(glossary_path)
    glossary_violations = pipeline.validate_glossary(items, {}, glossary, translations)

    serialized_violations = [
        violation if isinstance(violation, dict) else violation.__dict__
        for violation in glossary_violations
    ]

    report = {
        "phase": args.phase,
        "source": str(source),
        "translation": str(translation_path),
        "source_item_count": len(items),
        "translation_row_count": len(rows),
        "source_items_match_translation_rows": source_ids == row_ids,
        "missing_item_ids": missing_item_ids,
        "extra_item_ids": extra_item_ids,
        "duplicate_item_ids": duplicate_item_ids,
        "glossary_violations": serialized_violations,
    }

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    failed = (
        missing_item_ids
        or extra_item_ids
        or duplicate_item_ids
        or glossary_violations
        or source_ids != row_ids
    )
    return 1 if failed and not args.no_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
