# Review Batch 004: High-Risk Volume, Image Tool, OSL, and Lama Cleanup

Status: complete
Created: 2026-06-30

## Scope

Fourth manual terminology cleanup batch. This batch continues the speed-oriented pass over the current highest-risk pages after Batch 003.

## Term Rules For This Batch

| English | Preferred Chinese / Rule |
|---|---|
| PxrVolume / LamaLayer / OSL / Image Tool / `it` | Preserve product, node, shader, and tool names; translate surrounding prose. |
| volume / density / scattering / anisotropy | 体积 / 密度 / 散射 / 各向异性 in prose; preserve shader parameter names and UI labels. |
| Bxdf / Shading Group / Material Connection / Attribute Editor | Preserve exact Maya/RenderMan UI or node labels when they identify UI elements; add Chinese explanation where helpful. |
| indirect visibility / dicing projection / scene units | 间接可见性 / 切分投影 / 场景单位 in prose; preserve exact parameter labels when used as UI text. |
| catalog / framebuffer / render view / image processing | 目录 / 帧缓冲 / 渲染视图 / 图像处理 in prose; preserve `it` command/tool identifiers. |
| shader / pattern / closure / shading network | 着色器 / 图案 / 闭包 / 着色网络 in prose; preserve OSL code identifiers, file extensions, and shader type tokens. |
| rough coating / smooth coating / Fresnel blend | 粗糙涂层 / 平滑涂层 / 菲涅耳混合 in prose; preserve Lama lobe names and parameter identifiers. |

## Pages

| Order | Page | Risk score | Notes |
|---:|---|---:|---|
| 1 | `RFM27/544541121-PxrVolume in Maya.html` | 510 -> 95 | Reviewed and corrected. Localized volume, density, scattering, velocity/motion blur, light-filter, mesh-light, OpenVDB, dicing, scene-unit, anisotropy, sampling, and user-lobe prose while preserving PxrVolume, Maya/RenderMan UI labels, parameter names, enum values, shader/node names, and examples. |
| 2 | `RFM27/544543137-Image Tool or -it- in Maya.html` | 487 -> 170 | Reviewed and corrected. Localized Image Tool prose for catalog, framebuffer/render view, image window, sequence controls, monitor controls, remapping, view mapping, background images, denoise, snapshots, sequences, color charts, heat maps, metadata, and analysis tools while preserving menu paths, UI labels, shortcuts, file names, and official feature names. |
| 3 | `REN27/542222454-OSL Patterns.html` | 479 -> 144 | Reviewed and corrected. Localized OSL prose for shader/pattern wording, material closures, shading networks, shader globals, output parameters, object files, implicit derivatives, custom LPE matching, and throughput while preserving OSL code identifiers, file extensions, log levels, renderer tokens, node names, and UI labels. |
| 4 | `RFM27/544542672-Advanced.html` | 452 -> 100 | Reviewed and corrected. Localized advanced RenderMan for Maya prose for export, objects, procedural rendering, buckets, opacity/depth, sampling metrics, dicing, trace bias, scene units, crop windows, cache/memory, statistics, and LPE lobe mappings while preserving UI labels, parameter names, renderer tokens, enum values, and examples. |
| 5 | `REN27/542219129-LamaLayer.html` | 451 -> 19 | Reviewed and corrected. Localized LamaLayer prose for top/base layers, material layering, Fresnel blend, smooth/rough coating, attenuation, refraction, scattering, roughness, absorption, Relative IOR, bump maps, and comparison captions while preserving Lama node names, parameter names, mode labels, lobe names, and material examples. |

## Exit Criteria

- Each page is reviewed against the English source page and the current batch term rules.
- Prose is natural Chinese and avoids unnecessary English fragments.
- Product names, UI labels, node names, API identifiers, parameter names, renderer tokens, code examples, and path literals remain exact.
- Only visible text nodes are changed; HTML structure and official layout remain intact.
- Re-run `python3 tools/audit_terminology.py scan-pages` after each page.
- Re-run `python3 tools/audit_official_layout_alignment.py` before marking the batch complete.

## Current Progress

- Reviewed pages: 5 / 5.
- Batch completion: 100.00%.
- Overall page review progress: 23 / 816 = 2.82%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 54 high / 290 medium / 471 low pages. `REN27/542219129-LamaLayer.html` moved from 451/high to 19/low with no flagged terms. Full layout audit `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser samples; batch article tag-count checks show no HTML structure delta against the English source except the expected local `script`/`link` assets.
