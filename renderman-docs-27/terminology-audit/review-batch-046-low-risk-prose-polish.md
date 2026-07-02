# Review Batch 046: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 045. This batch targets RenderMan University project/compositing/lighting prose, TangentField node-reference prose, Maya denoiser prose, Katana configuration prose, and Houdini camera-projection prose.

Preserve exact product names, node names, macro names, menu paths, UI labels, parameter names, enum values, attribute names, file formats, shader names, project names, and acronyms. Translate ordinary prose terms such as project-based learning, hero image, tractor beam, vector method, texture filter, mip-mapping, shading tangent, vector map, sample textures, rotation/vector map, render, compositing, background, gradient, light/shadow contrast, brightness, post-processing, color grading, image realism, lighting rig, dragon features, rim/key/fill light, scene, option, preference, lookdev, PRMan-specific, integrator, custom integrator, shading network, volume box, camera projection, projection plugin, view tab, and spare parameters when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/600145995-Projects.html` | 32/low | Translate project-learning labels, hero-image label, tractor-beam wording, and generic project descriptors while preserving project names. |
| 2 | `REN27/542224996-PxrTangentField.html` | 32/low | Translate vector-method, texture-filter, mip-mapping, shading-tangent, vector-map, sample-texture, wrap-mode, and pattern-map prose while preserving parameter and enum names. |
| 3 | `RU/657621227-Dragon Compositing.html` | 31/low | Translate render/compositing/background/gradient/lighting/post-processing/color-grading/image-realism prose while preserving Dragon and Photoshop/Nuke-style terms where needed. |
| 4 | `RU/656834669-Dragon Lighting.html` | 31/low | Translate lighting-rig, dragon-feature, rim/key/fill-light, cinematic look, shadow, area, material, studio-photography, placement, and setting prose. |
| 5 | `RFM27/544542924-Interactive Denoiser in Maya.html` | 31/low | Translate viewport-render, first-pass, heuristic, quality, render convergence, denoised-result, sample, preference, interval, lookdev, and interactivity prose while preserving UI labels. |
| 6 | `RFK27/546177143-Configuring Katana.html` | 31/low | Translate PRMan-specific, integrator/custom-integrator, denoiser/holdout, sample-filter, shading-network, volume-box, Ops, and pattern-output prose while preserving node/macro names. |
| 7 | `RFH27/544644832-Camera Projections.html` | 31/low | Translate camera-projection, custom projection-plugin, projection, camera/View/RenderMan-tab, spare-parameter, shelf, and connection prose while preserving node and UI labels. |

## Results

Edited 63 visible article text-node update operations across 7 pages, including a focused follow-up pass to translate `Tip`, `Note`, `wrap mode`, ordinary `dragon` references, and generic camera/projection headings. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RU/600145995-Projects.html` | 23/low | Translated project-learning labels, hero-image label, and tractor-beam wording while preserving project names. |
| 2 | `REN27/542224996-PxrTangentField.html` | 2/low | Translated vector-method, texture-filter, MIP-mapping, shading-tangent, vector-map, sample-texture, wrap-mode, and pattern-map prose while preserving parameter and enum names. |
| 3 | `RU/657621227-Dragon Compositing.html` | 2/low | Translated render/compositing/background/gradient/lighting/post-processing/color-grading/image-realism prose and localized Tip labels. |
| 4 | `RU/656834669-Dragon Lighting.html` | 0/low | Translated lighting-rig, dragon-feature, rim/key/fill-light, cinematic look, shadow, area, material, studio-photography, placement, and setting prose. |
| 5 | `RFM27/544542924-Interactive Denoiser in Maya.html` | 5/low | Translated viewport-render, first-pass, heuristic, quality, render convergence, denoised-result, sample, preference, interval, lookdev, and interactivity prose while preserving UI labels. |
| 6 | `RFK27/546177143-Configuring Katana.html` | 9/low | Translated PRMan-specific, integrator/custom-integrator, denoiser/holdout, sample-filter, shading-network, volume-box, Ops, and pattern-output prose while preserving node/macro names. |
| 7 | `RFH27/544644832-Camera Projections.html` | 15/low | Translated camera-projection, custom projection-plugin, projection, camera/View/RenderMan-tab, spare-parameter, shelf, and connection prose while preserving node and UI labels. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 38 flagged terms, and 3050 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
