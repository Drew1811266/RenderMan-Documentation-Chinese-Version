# Review Batch 028: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish on the next highest-ranked pages. This batch focuses on RenderMan University resource/tutorial prose and DCC/reference pages where ordinary English words remain in Chinese sentences, while preserving project/resource titles, node names, UI labels, parameter names, and technical abbreviations.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/608469242-HDR Vault.html` | 48/low -> 15/low | Completed; translated folder/library/category/preset-browser resource prose while preserving artist names, HDR Vault title, and asset-library path labels. |
| 2 | `RU/599883858-Textures.html` | 48/low -> 9/low | Completed; translated resource-card prose around textures, manifolds, maps, randomization, and Mari texturing workflow while preserving project/product names. |
| 3 | `RFM27/544539731-Curves in Maya.html` | 48/low -> 18/low | Completed; normalized curve/fur/hair prose while preserving XGen/IGS, primvar names, Maya UI labels, and sample files. |
| 4 | `RFK27/546179420-Using PxrVary.html` | 48/low -> 8/low | Completed; translated PxrVary explanatory prose around variation, visual effects, shader attributes, examples, and scene setup logic while preserving ID/source names. |
| 5 | `RFK27/546178051-PrmanSignalVisualizer.html` | 48/low -> 42/low | Completed conservatively; normalized ordinary wording while preserving UI parameter labels such as Scene Graph, Material Location, Shading Node, Output Port, and Set from Scenegraph Selection. |
| 6 | `REN27/542222258-Patterns.html` | 48/low -> 4/low | Completed; translated ordinary pattern-category prose while preserving official node names and Pattern/OSL terminology where it functions as a technical category. |

## Validation

- Edited 88 visible article text nodes through the HTML text-node replay pipeline.
- Per-page edit pass preserved each page's pre-edit tag fingerprint.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 64 flagged terms, and 3360 residual term candidates after this batch.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pass and 816/816 browser-sampled pass after this batch.
