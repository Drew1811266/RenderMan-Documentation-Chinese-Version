# Review Batch 035: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 034. This batch focuses on Houdini release-note prose, Kaboom Box lookdev setup, Solaris LPE workflow, Blender baking, and two RenderMan pattern/reference pages where ordinary English remains embedded in Chinese prose.

Preserve exact node names, HDA/tool names, UI labels, file extensions, USD/RenderMan identifiers, AOV/LPE acronyms, command names, and literal attribute names. Translate explanatory prose terms such as production builds, shading network, lookdev, light paths, baking workflow, pass-through node, procedural noise, channels, outputs, layers, and downstream nodes when they are not exact UI labels.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFH27/544647320-RenderMan for Houdini Release Notes.html` | 43/low | Translate release-note prose around production builds, Apprentice editions, shading networks, visualizer nodes, CUDA device, and subnet inputs while preserving product/UI names. |
| 2 | `RFH27/544647115-Kaboom Box Kickstarter.html` | 43/low | Translate pyro lookdev, node-network, VDB sequence, preset, properties panel, lights/camera, and explosion prose. |
| 3 | `RFH27/544641953-Setting up LPEs in Solaris.html` | 43/low | Translate LPE workflow prose around light paths, light bounces, additive compositing, AOV channels, light groups, and source names. |
| 4 | `RFB27/544639698-Baking in Blender.html` | 43/low | Translate baking, hider, texture manifold, point cloud, panel, filename pattern, primvar, and UV-set prose while preserving UI labels. |
| 5 | `REN27/542224392-PxrProjectionStack.html` | 43/low | Translate channel/layer/output routing prose while preserving parameter names and AOV/channel identifiers. |
| 6 | `REN27/542222579-PxrBakePointCloud.html` | 43/low | Translate pass-through, pattern-network, baking workflow, scalar/procedural-noise, display-driver, world-space, point, and primvar prose. |

## Results

Edited 66 visible article text nodes. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFH27/544647320-RenderMan for Houdini Release Notes.html` | 12/low | Translated release-note prose around production builds, Apprentice editions, shading networks, visualizer nodes, CUDA device, shader nodes, undo, and subnet inputs while preserving product/UI names. |
| 2 | `RFH27/544647115-Kaboom Box Kickstarter.html` | 21/low | Translated pyro lookdev, RenderMan artist, node-network, VDB sequence, fireball preset, properties panel, lights/camera, and explosion prose while preserving HDA/node labels. |
| 3 | `RFH27/544641953-Setting up LPEs in Solaris.html` | 9/low | Translated LPE workflow prose around production, art direction, light paths, additive compositing, AOV channels, light groups, and source names. |
| 4 | `RFB27/544639698-Baking in Blender.html` | 33/low | Translated baking, hider, texture manifold, point cloud, filename pattern, primvar, and UV-set prose while preserving Blender UI labels and RenderMan control names. |
| 5 | `REN27/542224392-PxrProjectionStack.html` | 8/low | Translated channel/layer/output routing prose while preserving exact parameter, AOV, channel, and result names. |
| 6 | `REN27/542222579-PxrBakePointCloud.html` | 8/low | Translated pass-through, Pattern network, baking workflow, scalar/procedural-noise, display-driver, world-space, point, and primvar prose. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 51 flagged terms, and 3262 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
