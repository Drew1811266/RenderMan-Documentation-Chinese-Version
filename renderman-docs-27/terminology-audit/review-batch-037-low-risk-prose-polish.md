# Review Batch 037: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 036. This batch targets material fundamentals, Maya baking/camera/volume workflows, Katana XPU configuration, and Houdini holdout/compositing prose.

Preserve exact node names, UI labels, menu names, parameter labels, command snippets, file names, and product names. Translate ordinary prose terms such as renderer, material, lobe, shader, texture map, linearize, pattern network, bake render, image plane, sample filter, volume, mesh light, settings, override, holdout, live-action plate, display, and filter when they are not exact UI labels.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/599523329-R.F. - Materials - PxrSurface.html` | 41/low | Translate material/lobe/shader/texture-map/linearization and lesson-summary prose while preserving RenderMan/PxrSurface names. |
| 2 | `RFM27/544543018-Baking in Maya.html` | 41/low | Translate pattern-network, bake, texture, point-cloud, disk, hider, and batch-render prose while preserving node/menu labels. |
| 3 | `RFM27/544541707-Cameras in Maya.html` | 41/low | Translate camera/effect/projection/image-plane/sample-filter prose while preserving PxrCamera, txmake, and option labels. |
| 4 | `RFM27/544541121-PxrVolume in Maya.html` | 41/low | Translate volume, meshlight, smoke/cloud, sampling, motion-blur, and light-filter prose while preserving parameter names and attribute literals. |
| 5 | `RFK27/546178939-XPU in Katana.html` | 41/low | Translate XPU setting/override/machine/interactive/batch render prose while preserving command-line examples and option names. |
| 6 | `RFH27/544645461-Holdouts.html` | 41/low | Translate holdout/live-action plate/display/filter/compositing prose while preserving Houdini/RenderMan UI and AOV labels. |

## Results

Edited 74 visible article text nodes. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RU/599523329-R.F. - Materials - PxrSurface.html` | 15/low | Translated renderer, material, lobe, shader, texture-map, linearization, fabric, asset, scene, and MaterialX Lama shading-system prose while preserving lesson/product names. |
| 2 | `RFM27/544543018-Baking in Maya.html` | 8/low | Translated Pattern-network, bake, texture, point-cloud, disk, hider, and batch-render prose while preserving node and menu labels. |
| 3 | `RFM27/544541707-Cameras in Maya.html` | 15/low | Translated camera/effect/projection/image-plane/sample-filter prose while preserving PxrCamera, txmake, and option labels. |
| 4 | `RFM27/544541121-PxrVolume in Maya.html` | 38/low | Translated volume, meshlight, smoke/cloud, sampling, motion-blur, density, BxDF, Pattern, and light-filter prose while preserving parameter labels. |
| 5 | `RFK27/546178939-XPU in Katana.html` | 22/low | Translated XPU setting/override/machine/interactive/batch-render prose while preserving command-line examples and option names. |
| 6 | `RFH27/544645461-Holdouts.html` | 12/low | Translated holdout/live-action plate/display/filter/compositing prose while preserving RenderMan/Houdini UI labels and AOV names. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 49 flagged terms, and 3232 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
