# Review Batch 048: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 047. This batch targets RenderMan node-reference prose, RenderMan University overview/course prose, Blender material-layering prose, and PxrSurface material-layering prose.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, attribute names, file formats, shader names, project names, artist names, and acronyms. Translate ordinary prose terms such as ambient, knock back, deepen, mult, diffuse/specular, scene units, primitive variable, random source, tiling mode, seed, attribute, primitive variable, shapes, pattern, randomization parameters, web archive, Pixar tutors, community, shading network, pattern node, base/upper layer, material layering, props, sets, environments, materials, layering, dirt, Shading lead, shot, sequence, workflow, textures, render, Presence parameter, production integrators, depth, cached/non-cached, micropolygon length, and shading sample when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `REN27/542232193-PxrOcclusion.html` | 29/low | Translate ambient/knock-back/deepen/mult, diffuse/specular, scene-unit, and diffuse-color prose while preserving parameter names. |
| 2 | `REN27/542224582-PxrRandomTextureManifold.html` | 29/low | Translate primitive-variable, random-source, tiling-mode, frequency, blend, seed, attribute, shape, pattern, and randomization prose while preserving parameter names. |
| 3 | `RU/608600070-About RenderMan University.html` | 28/low | Translate web-archive, tutor/community, CG generalist, and RenderMan University overview prose while preserving names. |
| 4 | `RU/599163195-Procedural.html` | 28/low | Translate shading-network and RenderMan pattern-node prose while preserving lesson titles. |
| 5 | `RFB27/544638559-Material Layering with PxrLayerSurface in Blender.html` | 28/low | Translate base/upper layer, pattern, shader-editor, solo-node, and layer/global-bump prose while preserving node/UI labels. |
| 6 | `REN27/542221558-Presence and Opacity.html` | 27/low | Translate Presence/cutout/pattern/integrator/depth/cached/micropolygon/shading-sample prose while preserving parameter names. |
| 7 | `RU/619806721-PxrSurface - Material Layering.html` | 26/low | Translate Pixar material-layering prose, props/sets/environments, dirt, Shading lead, shot/sequence, workflow, textures, render, and look prose while preserving product names. |

## Results

Edited 46 visible article text-node update operations across 7 pages, including a focused follow-up pass on PxrOcclusion to translate remaining ordinary diffuse/specular prose. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `REN27/542232193-PxrOcclusion.html` | 13/low | Translated ambient/knock-back/deepen/mult, diffuse/specular, scene-unit, and diffuse-color prose while preserving parameter names. |
| 2 | `REN27/542224582-PxrRandomTextureManifold.html` | 14/low | Translated primitive-variable, tiling-mode, frequency, blend, seed, attribute, shape, pattern, and randomization prose while preserving random-source and parameter labels. |
| 3 | `RU/608600070-About RenderMan University.html` | 23/low | Translated web-archive, tutor/community, CG generalist, and RenderMan University overview prose while preserving names. |
| 4 | `RU/599163195-Procedural.html` | 15/low | Translated shading-network and RenderMan pattern-node prose while preserving lesson titles. |
| 5 | `RFB27/544638559-Material Layering with PxrLayerSurface in Blender.html` | 18/low | Translated base/upper layer, pattern, shader-editor, solo-node, and layer/global-bump prose while preserving node/UI labels. |
| 6 | `REN27/542221558-Presence and Opacity.html` | 16/low | Translated Presence/cutout/pattern/integrator/depth/cached/micropolygon/shading-sample prose while preserving parameter names and cache mode labels. |
| 7 | `RU/619806721-PxrSurface - Material Layering.html` | 3/low | Translated Pixar material-layering prose, props/sets/environments, dirt, Shading Lead, shot/sequence, workflow, textures, render, and look prose while preserving product names. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 35 flagged terms, and 3030 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
