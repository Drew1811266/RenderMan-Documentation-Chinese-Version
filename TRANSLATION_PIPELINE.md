# HTML Translation Pipeline

This project includes a layout-preserving translation pipeline:

```bash
python3 tools/translate_html_docs.py --help
```

## Safety Model

- The AI never receives full HTML.
- The script extracts only visible text nodes from the selected scope.
- Tags, attributes, image paths, table markup, links, and scripts are written back exactly as they were.
- `script`, `style`, `pre`, `code`, `kbd`, `samp`, `var`, `svg`, `math`, `textarea`, `noscript`, `translate="no"`, and `notranslate` sections are skipped.
- After rendering, the script compares the original and translated HTML tag fingerprints. If any tag changes, the file is treated as a layout failure.
- Repeated text is cached by hash, so reruns do not retranslate unchanged strings.

## Codex Translation Workflow

Do not use external machine translation tools for this project.

Codex translates pages by producing JSONL translation rows, then the script
applies those rows back into the original HTML. The script is only responsible
for extraction, validation, caching, and layout-preserving HTML reconstruction.

The default output path is `renderman-docs-27/html-zh`. This keeps relative
paths like `../../attachments/...` valid without copying the downloaded
attachments.

## Offline / Manual JSONL Workflow

Export untranslated text:

```bash
python3 tools/translate_html_docs.py \
  --provider jsonl-export \
  --input renderman-docs-27/html \
  --export-path renderman-docs-27/translation-items.jsonl
```

Codex translates each JSONL row and saves rows as:

```json
{"id":"same_hash_id","text":"translated text"}
```

Rows may also include an `item_id` for context-specific overrides when the same
short English text appears in multiple places but needs different Chinese
wording in one HTML node:

```json
{"id":"same_hash_id","item_id":"filehash:index","text":"context-specific translated text"}
```

Hash-only rows update the translation cache. `item_id` rows are applied only to
that extracted text node during rendering, which keeps repeated parameter names
safe while still allowing awkward split sentences to be repaired.

Apply translated rows:

```bash
python3 tools/translate_html_docs.py \
  --provider jsonl-apply \
  --input renderman-docs-27/html \
  --output renderman-docs-27/html-zh \
  --apply-path renderman-docs-27/translation-items.translated.jsonl
```

## Smoke Test

Run this to verify extraction and layout validation without using AI:

```bash
python3 tools/translate_html_docs.py \
  --provider copy \
  --limit-files 3 \
  --output renderman-docs-27/html-zh-smoke
```

In `copy` mode, translated output should be byte-identical to source HTML.

## Terminology

Use these files before translating any page:

- `renderman-docs-27/glossary/renderman_terminology.json`
- `renderman-docs-27/glossary/renderman_terminology.md`

The glossary is also used during `jsonl-apply` to report missing protected
terms such as `XPU`, `RIS`, `AOV`, `LPE`, `MaterialX`, `PxrSurface`, and
environment variables.
