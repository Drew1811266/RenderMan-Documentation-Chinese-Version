# Review Batch 038: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 037. This batch targets Katana barn light filter prose, Houdini texture-manager prose, LamaTricolorSSS layer/radius explanations, and RenderMan University tutorial prose about look development, path tracing, and value maps.

Preserve exact product names, node names, UI labels, parameter names, enum values, file/tool names, artist/source names, and acronyms. Translate ordinary prose terms such as shadows, physical shadows, scene units, subsurface, pattern, lookdev scene, neutral lighting, light rig, shader adjustment, digital image, virtual scene, ray, bounce, surface, value, rendering, material, metallic workflow, bump map, displacement map, and opacity when they are not exact UI labels.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFK27/546178609-PxrBarnLightFilter in Katana.html` | 41/low | Translate barn-light explanatory prose, shadows, physical shadows, start/effect/cone descriptions while preserving PxrBarnLightFilter and parameter/enum labels. |
| 2 | `RFH27/544644341-Texture Manager.html` | 41/low | Translate texture-manager user-interface and batch-rendering prose while preserving UI labels, OpenImageIO, txmake, and config names. |
| 3 | `REN27/542220410-LamaTricolorSSS.html` | 41/low | Translate subsurface, scene-units, pattern, layer, scattering, and continuation-ray prose while preserving Lama/MaterialX parameter labels. |
| 4 | `RU/657228220-RazorBack Shading Pt.1.html` | 40/low | Translate look-development, lighting, studio/client, shader-adjustment, HDRI, and Hypershade prose. |
| 5 | `RU/629932059-What is Path Tracing-.html` | 40/low | Translate path-tracing explanation terms such as digital image, virtual world, scene, rays, line segments, bounce, surface, source, and image. |
| 6 | `RU/625672304-Black & White.html` | 40/low | Translate value-map tutorial terms such as black/white colors, rendering, roughness, metallic workflow, bump maps, displacement maps, and opacity. |

## Results

Edited 90 visible article text nodes. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFK27/546178609-PxrBarnLightFilter in Katana.html` | 38/low | Translated shadows, barn-light explanatory prose, start/effect/cone descriptions, and guide text while preserving PxrBarnLightFilter, Physical/Analytic Barn, edge, preBarn, enum labels, Viewer, and Guide Size. |
| 2 | `RFH27/544644341-Texture Manager.html` | 36/low | Translated texture-manager prose around user interface, queue behavior, batch rendering, backend, workers, and OCIO config while preserving UI labels and tools. |
| 3 | `REN27/542220410-LamaTricolorSSS.html` | 6/low | Translated subsurface, scene-units, Pattern-node, layer, scattering, and Radius prose while preserving Lama, MaterialX, parameter labels, and mode names. |
| 4 | `RU/657228220-RazorBack Shading Pt.1.html` | 4/low | Translated look-development, neutral-lighting, light-rig, asset-shading, studio/client, shot, shader-adjustment, HDRI-environment, and Hypershade prose. |
| 5 | `RU/629932059-What is Path Tracing-.html` | 4/low | Translated path-tracing explanation prose for digital images, light, virtual worlds, scene, rays, line segments, bounce, surface, source, and final image. |
| 6 | `RU/625672304-Black & White.html` | 1/low | Translated black/white value-map tutorial prose while preserving the official source's original roughness/metallic values and the Presence/Opacity label. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 48 flagged terms, and 3212 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
