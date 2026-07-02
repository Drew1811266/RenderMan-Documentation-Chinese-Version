# Review Batch 003: Global Highest-Risk RenderMan/RfK/RfM Cleanup

Status: complete
Created: 2026-06-30

## Scope

Third manual terminology cleanup batch. This batch switches from Tractor-local cleanup to the current highest-risk pages across RenderMan core, RenderMan for Katana, and RenderMan for Maya.

## Term Rules For This Batch

| English | Preferred Chinese / Rule |
|---|---|
| RIS / XPU / PRMan / RfK / RfM | Preserve product/renderer abbreviations; translate surrounding prose. |
| Denoiser / Stylized Looks | 降噪器 / 风格化外观, unless used as exact product or node labels. |
| statement / global statement / object statement | 语句 / 全局语句 / 对象语句 in prose; preserve node/page identifiers such as `PrmanGlobalStatements`. |
| attribute / parameter / option / setting | 属性 / 参数 / 选项 / 设置; preserve exact UI, node, and code identifiers. |
| instance / object / geometry | 实例 / 对象 / 几何体, unless part of a literal parameter name. |
| displacement / subdivision / dicing / presence | 置换 / 细分 / 切分 / 存在度, with original identifier preserved when needed. |
| AOV / LPE / channel | Preserve `AOV` and `LPE`; translate prose as arbitrary output variable / light path expression contextually when explanatory. |
| sample / filter / variance / denoise | 采样 / 滤波器 / 方差 / 降噪 in prose; preserve renderer tokens. |

## Pages

| Order | Page | Risk score | Notes |
|---:|---|---:|---|
| 1 | `REN27/542238759-542238759.html` | 1567 -> 166 | Reviewed and corrected. Localized release-note prose across XPU/RIS, Denoiser, Stylized Looks, RfB/RfM/RfK/RfH sections, reduced excessive English parentheticals, fixed repeated/awkward mixed terms, and calibrated protection for renderer syntax, UI labels, enum values, function names, texture tools, and feature names. |
| 2 | `RFK27/546178913-PrmanGlobalStatements.html` | 985 -> 175 | Reviewed and corrected. Localized global option/parameter descriptions, adaptive sampling, baking, shading, dicing, display, checkpoint, statistics, search path, OSL, and volume prose while preserving RfK node names, parameter identifiers, defaults, enum values, renderer tokens, and examples. |
| 3 | `RFK27/546178855-PrmanObjectStatements.html` | 821 -> 149 | Reviewed and corrected. Localized object/location, instance, primitive attributes, grouping, visibility, trace, dicing, displacement, volume, and traversal prose while preserving statement identifiers, parameter names, defaults, enum values, renderer tokens, and examples. |
| 4 | `RFM27/544540160-Geometric Settings.html` | 647 -> 85 | Reviewed and corrected. Localized Maya geometric setting prose for instance attributes, grouping, shading, visibility, dicing, displacement, volume, polygon, and procedural settings while preserving Maya/RenderMan UI labels, type/default values, attribute identifiers, node names, and examples. |
| 5 | `RFM27/544542501-AOVs.html` | 566 -> 144 | Reviewed and corrected. Localized Maya AOV, Display, OpenEXR/DeepEXR, texture, TIFF, remap, display-channel, light-group, filter, and statistics prose while preserving AOV/LPE names, UI labels, token names, file formats, parameter names, enum values, and examples. |

## Exit Criteria

- Each page is reviewed against the English source page and the current RenderMan/RfK/RfM term rules.
- Prose is natural Chinese and avoids unnecessary English fragments.
- Product names, UI labels, node names, API identifiers, parameter names, renderer tokens, code examples, and path literals remain exact.
- Only visible text nodes are changed; HTML structure and official layout remain intact.
- Re-run `python3 tools/audit_terminology.py scan-pages` after each page.
- Re-run `python3 tools/audit_official_layout_alignment.py` before marking the batch complete.

## Current Progress

- Reviewed pages: 5 / 5.
- Batch completion: 100.00%.
- Overall page review progress: 18 / 816 = 2.21%.
- Latest terminology validation: `python3 tools/audit_terminology.py scan-pages` reports 63 high / 299 medium / 453 low pages. `RFM27/544542501-AOVs.html` moved from 566/high to 144/medium with no flagged terms.
- Latest layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816 / 816 pages; quick article tag-count check for the AOVs page shows no HTML structure delta against the English source except the expected local `script`/`link` assets.
