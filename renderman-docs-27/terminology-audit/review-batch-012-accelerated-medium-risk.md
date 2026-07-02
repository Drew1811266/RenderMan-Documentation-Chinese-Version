# Review Batch 012: Accelerated Medium-Risk Sweep

Status: completed; `TRA/22184352-Release Notes.html` remains a watch item already rechecked in Batch 011.
Created: 2026-06-30

## Scope

Accelerated terminology cleanup for the current top medium-risk pages. The goal is to reduce unnecessary English in Chinese prose while preserving RenderMan, DCC, UI, shader, API, command, file, and parameter identifiers. Related pages should be handled together where terminology repeats.

## Pages

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 1 | `RFK27/546179237-Preset Browser in Katana.html` | 199/medium -> 20/low | Completed; normalized asset/library/preset/prose headings while preserving UI/product identifiers. |
| 2 | `REN27/542232083-PxrUnified.html` | 199/medium -> 48/low | Completed; normalized integrator/path-guiding/manifold/photon prose while preserving parameter labels and paper titles. |
| 3 | `TRA/22184352-Release Notes.html` | 198/medium | Rechecked in Batch 011; keep as watch item, not counted again unless edited. |
| 4 | `RFM27/544540950-PxrSurface in Maya.html` | 191/medium -> 39/low | Completed; normalized shader/material/lobe prose while preserving parameter labels and lobe identifiers. |
| 5 | `RFM27/544538718-Getting Started in Maya.html` | 185/medium -> 25/low | Completed; normalized plug-in/shelf/light/material/rendering prose while preserving Maya UI labels. |
| 6 | `RFM27/544538696-Installation of RenderMan for Maya.html` | 178/medium -> 48/low | Completed; normalized installation/module/path prose while preserving paths, commands, env vars, and module file names. |
| 7 | `RFM27/544543095-Holdouts in Maya.html` | 177/medium -> 32/low | Completed; normalized Holdout/shadow/plate/compositing prose while preserving channel and feature names. |
| 8 | `RFM27/544541742-Motion Blur in Maya.html` | 173/medium -> 21/low | Completed; normalized frame/shutter/motion-sample prose while preserving UI enum labels. |
| 9 | `REN27/542221154-PxrMarschnerHair.html` | 172/medium -> 24/low | Completed; normalized hair/specular/gain/lobe prose while preserving R/TT/TRT and named lobe identifiers. |
| 10 | `RFM27/544543137-Image Tool or -it- in Maya.html` | 170/medium -> 34/low | Completed; normalized Image Tool prose and calibrated protected UI/brand/shortcut identifiers. |
| 11 | `RFK27/546178913-PrmanGlobalStatements.html` | 165/medium -> 0/low | Completed; restored over-translated RenderMan option names and normalized Katana/global statement descriptions. |
| 12 | `REN27/542221833-Stylized Hatching.html` | 162/medium -> 46/low | Completed; normalized hatching/triplanar/signal prose and protected true parameter labels. |
| 13 | `RFM27/544541301-Stylized Looks in Maya Overview.html` | 161/medium -> 11/low | Completed; normalized Stylized Looks setup prose while preserving workflow button, step, and node labels. |
| 14 | `RFH27/544646941-Fire.html` | 161/medium -> 2/low | Completed; normalized fire-volume prose while preserving Houdini parameter labels. |
| 15 | `REN27/542236770-Custom OCIO Config.html` | 161/medium -> 34/low | Completed; normalized OCIO/JSON configuration prose while preserving role names, JSON keys, and txmake values. |
| 16 | `RFH27/544646437-The ROP Node.html` | 156/medium -> 42/low | Completed; normalized Houdini ROP prose while preserving ROP parameter labels and enum values. |
| 17 | `RFM27/544540203-About Primitive Variables.html` | 155/medium -> 29/low | Completed; corrected primitive variables to 图元变量/primvars and normalized table prose while preserving primvar declarations. |
| 18 | `REN27/542221920-Stylized Lines.html` | 155/medium -> 39/low | Completed; normalized linework/signal/depth/color prose and protected true Stylized Lines UI labels. |
| 19 | `RFM27/544539564-Preset Browser in Maya.html` | 154/medium -> 19/low | Completed; paired with Katana Preset Browser terminology cleanup. |
| 20 | `RFM27/544539792-Instances in Maya.html` | 153/medium -> 20/low | Completed; normalized instancing/archive/geometry prose while preserving Maya/XGen UI labels and node/tool identifiers. |

## Current Progress

- Reviewed pages: 19 / 20.
- Batch completion: 95.00%; actionable cleanup pages are complete, with page 3 retained as a watch item.
- Overall page review progress: 92 / 816 = 11.27%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 0 high / 251 medium / 564 low pages after Batch 012 pages 1, 2, 4 through 20.
- Structure validation for `RFK27/546179237-Preset Browser in Katana.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544539564-Preset Browser in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544541742-Motion Blur in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544543095-Holdouts in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544538718-Getting Started in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544538696-Installation of RenderMan for Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544540950-PxrSurface in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542221154-PxrMarschnerHair.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544543137-Image Tool or -it- in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542232083-PxrUnified.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542221833-Stylized Hatching.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542221920-Stylized Lines.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544541301-Stylized Looks in Maya Overview.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFH27/544646941-Fire.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542236770-Custom OCIO Config.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544540203-About Primitive Variables.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFH27/544646437-The ROP Node.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544539792-Instances in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFK27/546178913-PrmanGlobalStatements.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Audit calibration added for Image Tool UI labels, shortcuts, Nvidia/Optix hardware identifiers, and beauty channel names.
- Audit calibration added for PxrUnified path-guiding/manifold/photon identifiers, Stylized Hatching labels, Stylized Lines labels/modes, Stylized Looks overview workflow labels, Houdini Fire parameter labels, OCIO JSON/configuration identifiers, and Houdini ROP parameter labels.
- Audit calibration added for Maya/XGen instancing page headings, menu commands, buttons, tabs, and tool/node identifiers.
- Audit calibration added for Katana PrmanGlobalStatements literal values, bracket range markers, RenderMan option names, and RfK plugin traversal identifiers.
- Interim layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser-sampled pages.

## Acceleration Rules

- Prefer grouped text-node-only normalization for repeated prose terms across related pages.
- Use audit-rule calibration only for true identifiers, not ordinary English nouns that should read as Chinese.
- After each edited page, run `python3 tools/audit_terminology.py scan-pages` and page tag-count validation.
- Before closing the batch, run `python3 tools/audit_official_layout_alignment.py`.
