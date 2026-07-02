# Review Batch 039: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 038. This batch targets Blender batch-rendering settings, Katana scene-setup prose, Maya feature and tilt-shift descriptions, RenderMan University asset/tutorial prose, and Houdini PxrMatteID attribute wording.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, file/tool names, event names, artist/source names, and acronyms. Translate ordinary prose terms such as batch rendering, external rendering, frame chunking, compositor, recovery, scene setup, renderer, object, material, pattern node, motion blur, scene linear, focus plane, cluster handle, look development, bridge product, animation, modeling, shading, texturing, setup techniques, user attribute, RenderMan attribute, texture mask, and matte AOV when they are not exact UI labels.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFB27/544639612-Batch Rendering in Blender.html` | 46/low | Translate batch-rendering, frame-chunking, compositor, recovery, RIB format/compression prose while preserving UI labels and renderer/tool names. |
| 2 | `RFK27/546177260-Scene Setup.html` | 44/low | Translate scene setup, object, renderer, material, pattern-node, shader-adjustment, render-configuration prose while preserving Katana node/UI labels. |
| 3 | `RFM27/544542444-Features.html` | 43/low | Translate feature-tab, motion-blur, shutter, scene-linear, denoiser, stylized-looks, and filter prose while preserving settings labels. |
| 4 | `RFM27/544542112-Tilt-Shift in Maya.html` | 43/low | Translate tilt-shift, focus-plane, cluster-handle, locator, connection-editor, and viewport prose while preserving Maya menu paths and labels. |
| 5 | `RU/608469325-Official Swatch.html` | 40/low | Translate shader-lookdev, look-development, bridge-product, swatch asset-section, hair-type, and license prose while preserving asset and license names. |
| 6 | `RU/562757686-RenderMan Demo Sign.html` | 40/low | Translate animation, demo-pod, neon-sign, modeling/shading/texturing, VEX setup, bulb, and randomization prose while preserving project/event names. |
| 7 | `RFH27/544646676-Using PxrMatteID.html` | 40/low | Translate matte AOV, user attribute, RenderMan attribute, Pattern node, texture-mask, and output-tab prose while preserving PxrMatteID and node names. |

## Results

Edited 64 distinct visible article text nodes, with 72 total text-node update operations including follow-up corrections. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFB27/544639612-Batch Rendering in Blender.html` | 37/low | Translated batch-rendering, Blender batch-process, frame-chunking, compositor, recovery, and RIB output prose while preserving UI labels and tool names. |
| 2 | `RFK27/546177260-Scene Setup.html` | 44/low | Reviewed scene-setup/material/Pattern-node/render-configuration prose; translated ordinary prose and corrected a split Pattern-link sentence while preserving Katana node names, UI labels, and renderer properties. |
| 3 | `RFM27/544542444-Features.html` | 31/low | Translated feature-tab, motion-blur, shutter, scene-linear, denoiser, stylized-looks, and filter prose while preserving setting labels. |
| 4 | `RFM27/544542112-Tilt-Shift in Maya.html` | 43/low | Reviewed tilt/roll/focus/locator/connection-editor prose and translated ordinary explanatory terms while preserving Maya menu paths and UI labels. |
| 5 | `RU/608469325-Official Swatch.html` | 21/low | Translated shader-lookdev, look-development, bridge-product, swatch asset-section, and hair-type prose while preserving asset names and license names. |
| 6 | `RU/562757686-RenderMan Demo Sign.html` | 16/low | Translated animation, demo-pod, neon-sign, modeling/shading/texturing, VEX setup, bulb setup, and randomization prose while preserving project/event names. |
| 7 | `RFH27/544646676-Using PxrMatteID.html` | 9/low | Translated matte AOV, user attribute, RenderMan attribute, Pattern node, texture-mask, and output-tab prose while preserving node names and attribute literals. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 46 flagged terms, and 3202 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
