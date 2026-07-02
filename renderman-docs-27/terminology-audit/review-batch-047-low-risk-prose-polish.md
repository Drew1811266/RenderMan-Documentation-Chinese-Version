# Review Batch 047: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 046. This batch targets Blender integration pages, RenderMan node-reference pages, geometry reference prose, MaterialX overview prose, and RenderMan University asset prose where ordinary English remains embedded in Chinese sentences.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, attribute names, file formats, shader names, project names, artist names, and acronyms. Translate ordinary prose terms such as integrator, camera rays, renderer, light transport, production integrators, path tracer, dome lights, specular caustics, mesh, locker, collection, base color, edge mask, shader, roughness, placement, area light, exposure, pattern node, filter/gel, specular/diffuse light, shading/surface, light group, pattern, layer, background/base layer, blend mode, alpha channel, Physically Based Shading Nodes, pattern nodes, networks, material intent, linear curves, presence/opacity, samples-per-pixel, project, skin rendering, 3D artist, and character artist when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFB27/544639892-Integrators in Blender.html` | 30/low | Translate integrator/path-tracing/light-transport prose while preserving RenderMan integrator names and Blender UI labels. |
| 2 | `RFB27/544638080-Instances.html` | 30/low | Translate mesh/locker/collection/shading/material variation prose while preserving Blender and node names. |
| 3 | `REN27/542227805-PxrMeshLight.html` | 30/low | Translate mesh-light, exposure, pattern-node, temperature, specular/diffuse, near-distance, thin-shadow, and light-group prose while preserving parameter names. |
| 4 | `REN27/542224038-PxrLayeredBlend.html` | 30/low | Translate pattern/layer/background/base/blend-mode/alpha-channel prose while preserving node and parameter names. |
| 5 | `REN27/542220715-MaterialX.html` | 30/low | Translate MaterialX overview prose, physically-based shading nodes, pattern nodes, networks, material intent, ShaderGen, and limitation prose while preserving MaterialX/USD/Hydra names. |
| 6 | `REN27/542212854-Curves.html` | 30/low | Translate remaining linear/presence/opacity/samples-per-pixel/minwidth prose while preserving basis and attribute names. |
| 7 | `RU/611680348-Taraji.html` | 29/low | Translate project-resource labels, artist bio, skin-rendering prose, and license wording while preserving asset/artist/product names. |

## Results

Edited 56 visible article text-node update operations across 7 pages. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFB27/544639892-Integrators in Blender.html` | 11/low | Translated integrator/path-tracing/light-transport, camera-ray, renderer, production-quality, dome-light, and caustic prose while preserving RenderMan integrator names and Blender UI labels. |
| 2 | `RFB27/544638080-Instances.html` | 20/low | Translated mesh/locker/collection/base-color/edge-mask/shader/roughness/placement prose while preserving Blender and node names. |
| 3 | `REN27/542227805-PxrMeshLight.html` | 6/low | Translated area-light, pattern-node, high-dynamic-range, filter/gel/tint, specular/diffuse light, camera, thin-shadow, and light-group prose while preserving parameter names. |
| 4 | `REN27/542224038-PxrLayeredBlend.html` | 7/low | Translated pattern/layer/background/base/blend-mode/alpha-channel/mask prose while preserving node and parameter names. |
| 5 | `REN27/542220715-MaterialX.html` | 8/low | Translated MaterialX overview prose, physically-based shading nodes, pattern nodes, networks, material intent, ShaderGen, and limitation prose while preserving MaterialX/USD/Hydra names. |
| 6 | `REN27/542212854-Curves.html` | 28/low | Translated remaining linear and aliasing prose while preserving curve basis, attribute names, presence/opacity literals, and samples-per-pixel terminology. |
| 7 | `RU/611680348-Taraji.html` | 16/low | Translated project-resource labels, artist bio, skin-rendering prose, and license wording while preserving asset/artist/product names. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 37 flagged terms, and 3043 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
