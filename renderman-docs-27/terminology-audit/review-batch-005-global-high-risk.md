# Review Batch 005: Highest-Risk Tools, Lights, CheatSheet, Configuration, and Katana Cleanup

Status: complete
Created: 2026-06-30

## Scope

Fifth manual terminology cleanup batch. This batch continues the speed-oriented pass by selecting the current highest-risk pages from `page-risk-report.json` after Batch 004.

## Term Rules For This Batch

| English | Preferred Chinese / Rule |
|---|---|
| txmake / command options / file extensions | Preserve command names, option flags, arguments, file paths, and literal extensions; translate surrounding prose. |
| wrap mode / minmax shadow map / pyramid shadow map | 包裹模式 / minmax 阴影贴图 / pyramid 阴影贴图 in prose; preserve exact option values and command tokens. |
| dome light / portal light / environment light | 穹顶灯 / 门户灯 / 环境光 in prose; preserve Houdini/RenderMan UI labels when used as labels. |
| CheatSheet / quick reference / syntax examples | Preserve syntax and code examples; translate explanatory prose, headings where they are not literal commands, and ordinary workflow text. |
| Tractor configuration / profile / crews / service keys | Translate prose around configuration concepts; preserve config keys, service keys, example values, and UI/status literals. |
| Katana instancing / user attributes / instance sources | 实例化 / 用户属性 / 实例源 in prose; preserve Katana node names, CEL paths, parameter names, and renderer tokens. |

## Pages

| Order | Page | Risk score | Notes |
|---:|---|---:|---|
| 1 | `REN27/542236544-txmake.html` | 360 -> 114 | Reviewed and corrected. Localized txmake prose for texture files, wrap modes, resize operations, filters, mipmap/ripmap levels, pyramid wording, environment maps, data compression, channel handling, bump-to-roughness, shadow maps, command output, and directory/thread/help text while preserving command options, file extensions, option values, examples, format names, and literal arguments. |
| 2 | `RFH27/544645263-Dome And Portal Lights.html` | 342 -> 101 | Reviewed and corrected. Localized dome/portal light prose for portal orientation, parent dome lights, portal names, intensity, color tint, gamma/saturation inheritance, color temperature, visibility, specular/diffuse amount, shadows, trace subsets, light paths, caustics, samples, light groups, importance, and bridge application wording while preserving Houdini/RenderMan labels, node names, paper title, LPE tokens, and parameter names. |
| 3 | `RU/384368745-RenderMan CheatSheet.html` | 341 -> 70 | Reviewed and corrected. Localized quick-reference table prose for shaders, material models, layering, texture loading/placement, texture correction, blending, bump/displacement, generators, randomization, edge detection, lights, and light filters while preserving node names, category labels, feature labels, AOV/LPE terminology, and RenderMan product names. |
| 4 | `TRA/22184210-Configuration.html` | 327 -> 76 | Reviewed and corrected. Localized Tractor configuration prose for configuration settings, install/config directories, permissions, policy settings, comments, services, parser behavior, merge overlays, profiles, network service ports, listener ports, connections, multicast advertisements, firewalls, machine exceptions, database wording, and license-server notes while preserving config keys, service names, command options, literal values, paths, and example snippets. |
| 5 | `RFK27/546177906-Instancing in Katana.html` | 326 -> 11 | Reviewed and corrected. Localized Katana instancing prose for geometry reuse, instancing methods, leaf-level and hierarchical instancing, object prototypes, scene graph locations, instance sources, instance arrays, attributes, transforms, material overrides, user attributes, point clouds, Bxdf variation, displacement constraints, light instancing, light shader parameters, and light filters while preserving Katana node names, parameter names, attribute identifiers, file names, literal type values, and renderer tokens. |

## Exit Criteria

- Each page is reviewed against the English source page and the current batch term rules.
- Prose is natural Chinese and avoids unnecessary English fragments.
- Product names, UI labels, node names, API identifiers, parameter names, renderer tokens, code examples, command options, paths, and literal values remain exact.
- Only visible text nodes are changed; HTML structure and official layout remain intact.
- Re-run `python3 tools/audit_terminology.py scan-pages` after each page.
- Re-run `python3 tools/audit_official_layout_alignment.py` before marking the batch complete.

## Current Progress

- Reviewed pages: 5 / 5.
- Batch completion: 100.00%.
- Overall page review progress: 28 / 816 = 3.43%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 48 high / 295 medium / 472 low pages. `RFK27/546177906-Instancing in Katana.html` moved from 326/high to 11/low with no flagged terms; quick article tag-count check shows no HTML structure delta against the English source except the expected local `script`/`link` assets.
- Batch layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816 / 816 static pages and 816 / 816 browser-sampled pages.
