# Review Batch 036: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 035. This batch focuses on pages with ordinary English still embedded in prose across RenderMan University resources, Katana portal-light workflow, RenderMan ocean/volume reference material, and modeling/texturing best-practice pages.

Preserve exact node names, shader names, parameter labels, file names, attribute values, license names, and project/place names when they function as identifiers. Translate explanatory prose terms such as map, nightclub, light filter, parent dome, volume, sampling, high/low poly, texture resolution, displacement maps, texturing, roughness map, pattern network, bake, render farm, and node graph when they are not exact labels.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/608469073-Berns Red Room.html` | 42/low | Translate resource prose around HDRI use, location, map attachment, venue description, and license wording. |
| 2 | `RFK27/546178489-Portal Lights in Katana.html` | 42/low | Translate portal/dome light setup prose, light-filter inheritance, parent dome behavior, and live-rendering update mode wording. |
| 3 | `REN27/542222405-aaOceanPrmanShader.html` | 42/low | Review ocean-shader prose and translate ordinary diffuse/displacement wording while preserving parameter and node labels. |
| 4 | `REN27/542220781-PxrVolume.html` | 42/low | Translate volume/smoke/cloud/sampling/performance/motion-blur/meshlight prose while preserving parameter labels and attribute names. |
| 5 | `RU/657555575-Dragon Modeling.html` | 41/low | Translate modeling, high/low poly, texture-resolution, displacement-map, subdivision, projection, mirroring, and UV patch prose. |
| 6 | `RU/608927745-Best Practices - The Tray.html` | 41/low | Translate texturing, roughness, normal map, look development, pattern-network, baking, Ptex, texture-map, and node-graph prose. |

## Results

Edited 86 visible article text nodes. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RU/608469073-Berns Red Room.html` | 26/low | Translated HDRI use, location, nightclub description, map attachment, and license prose while preserving place, author, and license names. |
| 2 | `RFK27/546178489-Portal Lights in Katana.html` | 2/low | Translated explanatory portal/dome-light prose to `门户灯光` and `穹顶灯`, while preserving exact node names such as `PxrPortalLight` and `PxrDomeLight`. |
| 3 | `REN27/542222405-aaOceanPrmanShader.html` | 40/low | Reviewed ocean-shader prose, corrected ordinary diffuse wording, and preserved parameter labels, node names, and author/reference names. |
| 4 | `REN27/542220781-PxrVolume.html` | 37/low | Translated smoke/cloud/volume, OpenVDB, sampling, performance, motion-blur, meshlight, Pattern, and light-filter prose while preserving parameter and attribute labels. |
| 5 | `RU/657555575-Dragon Modeling.html` | 6/low | Translated high/low poly, texture-resolution, map, parallelization, creative workflow, subdivision, projection, displacement-map, and UV patch prose. |
| 6 | `RU/608927745-Best Practices - The Tray.html` | 8/low | Translated texturing, roughness, normal-map, utility-node, look-development, Pattern-network, baking, render-farm, Ptex, texture-map, and node-graph prose. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 50 flagged terms, and 3244 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
