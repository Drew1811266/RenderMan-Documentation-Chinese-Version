# Review Batch 034: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 033. This batch targets pages with clear ordinary English remnants in Houdini implicit surfaces and motion blur, RenderMan University lighting, Maya interactive rendering and tilt-shift workflows, and the Solaris Studio sample scene.

Preserve exact RenderMan/DCC UI labels, menu paths, node names, file names, USD layer paths, project names, and established acronyms. Translate generic prose terms such as implicit surface, field, blending, lighting, setup, scene, workflow, motion blur, transformation blur, assets, variants, and rendering when they are not exact labels.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFH27/544644133-Implicit Surfaces.html` | 44/low | Translate implicit-surface, built-in primitive, blending, field-plugin, cache-file, volume, and primitive prose. |
| 2 | `RU/655065134-Toy Car Lighting.html` | 43/low | Translate lighting/setup/scene/shadow/reference/pipeline prose while preserving project and software names. |
| 3 | `RFM27/544542819-Interactive Rendering in Maya.html` | 43/low | Translate IPR/playblast/render-view prose while preserving Maya/RenderMan UI labels and commands. |
| 4 | `RFM27/544542112-Tilt-Shift in Maya.html` | 43/low | Translate tilt/roll/focus/camera-projection workflow prose while preserving parameter and menu labels. |
| 5 | `RFH27/544644938-Using Motion Blur.html` | 43/low | Translate motion-blur, micropolygon, transformation/deformation blur, AOV, particle, and object-node prose. |
| 6 | `RFH27/544642517-Solaris Studio.html` | 43/low | Translate studio asset/setup/layout/lighting prose while preserving USD, file names, asset names, and layer paths. |

## Results

Edited 57 visible article text nodes. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFH27/544644133-Implicit Surfaces.html` | 14/low | Translated implicit-surface, primitive, blending, field-plugin, cache-file, volume, and primitive prose while preserving `RiBlobby`, OpenVDB, Maya Fluids, and Bifrost names. |
| 2 | `RU/655065134-Toy Car Lighting.html` | 4/low | Translated lighting/setup/scene/shadow/reference/pipeline prose while preserving project/software names. |
| 3 | `RFM27/544542819-Interactive Rendering in Maya.html` | 40/low | Polished IPR, refinement, render-image, visibility, and playblast prose; remaining English is mainly Maya/RenderMan UI labels and command names. |
| 4 | `RFM27/544542112-Tilt-Shift in Maya.html` | 43/low | Reviewed and polished camera-projection, tilt, focus, and locator workflow prose; remaining English is dominated by parameter and menu labels. |
| 5 | `RFH27/544644938-Using Motion Blur.html` | 13/low | Translated motion-blur, micropolygon, transformation/deformation blur, AOV, particle, and object-node prose while preserving parameter labels. |
| 6 | `RFH27/544642517-Solaris Studio.html` | 21/low | Translated studio asset/setup/layout/lighting prose while preserving asset names, USD paths, file names, and release labels. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 54 flagged terms, and 3281 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
