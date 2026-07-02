# Review Batch 041: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 040. This batch targets Katana camera settings and polygon geometry prose, Houdini AOV Light prose, RenderMan University lighting/resource prose, and core RenderMan light-filter/single-scatter parameter prose.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, attribute names, file paths, shader names, artist/source names, license names, and acronyms. Translate ordinary prose terms such as projection plugin, custom plugin, material attribute, field of view, motion blur, utility light, lighting artist, shot-specific AOV mask, linking setup, geometry, light filter, outdoor scene, distant light, environment, dynamic range, map, polygonal geometry, subdivision surface, normal, displacement, light contribution, alpha channel, combine mode, single scatter, mean free path, directionality, roughness, scattering, and scene scale when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFK27/546178709-Camera Settings in Katana.html` | 38/low | Translate projection-plugin/FOV/camera-motion-blur prose while preserving Katana/RenderMan attribute names. |
| 2 | `RFH27/544645211-AOV Light.html` | 38/low | Translate AOV light, utility-light, artist, mask, geometry, linking, and light-filter prose while preserving node and LPE labels. |
| 3 | `RU/656998424-Stirling Lighting.html` | 37/low | Translate lighting/HDRI capture prose around outdoor scene, distant lights, parallel shadows, exposure levels, and dynamic range. |
| 4 | `RU/608468993-Slussen.html` | 37/low | Translate resource metadata and HDRI map/location/license prose while preserving place and license names. |
| 5 | `RFK27/546177753-Polygons in Katana.html` | 37/low | Translate polygonal geometry, look-development, primitive-variable, subdivision-surface, normal, topology, and shading prose. |
| 6 | `REN27/542230807-PxrGoboLightFilter.html` | 37/low | Translate light-filter, alpha-channel, tile-mode, diffuse/specular contribution, offset, combine-mode, and filter-group prose while preserving parameter/enum labels. |
| 7 | `REN27/542216422-Single Scatter Parameters.html` | 37/low | Translate single-scatter, mean-free-path, directionality, blur, direct-illumination, trace-control, roughness, unit-length, and scene-scale prose while preserving parameter labels. |

## Results

Edited 65 visible article text-node update operations across 7 pages, including a focused follow-up pass on resource prose, light-filter prose, and single-scatter prose. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFK27/546178709-Camera Settings in Katana.html` | 20/low | Translated projection-plugin, custom-plugin, FOV, and motion-blur prose while preserving Katana/RenderMan attribute names and shader labels. |
| 2 | `RFH27/544645211-AOV Light.html` | 24/low | Translated utility-light, lighting-artist, shot-specific AOV mask, geometry, linking-setup, and light-filter prose while preserving Light Linking, Light Filter labels, and node names. |
| 3 | `RU/656998424-Stirling Lighting.html` | 2/low | Translated outdoor-scene, distant-light, environment, parallel-shadow, HDRI capture, exposure-level, dynamic-range, final-image, and 32-bit-format prose. |
| 4 | `RU/608468993-Slussen.html` | 14/low | Translated resource metadata, HDRI map attachment, location, transit-hub, rebuild, and credit/license prose while preserving place and license names. |
| 5 | `RFK27/546177753-Polygons in Katana.html` | 7/low | Translated polygonal-geometry, look-development, texture-coordinate, primitive-variable, subdivision-surface, normal, topology, and shading prose while preserving exact attribute/menu labels. |
| 6 | `REN27/542230807-PxrGoboLightFilter.html` | 13/low | Translated light-filter, alpha-channel, tile-mode, diffuse/specular contribution, offset, multiplier, combine-mode, and filter-group prose while preserving parameter/enum labels. |
| 7 | `REN27/542216422-Single Scatter Parameters.html` | 6/low | Translated single-scatter, mean-free-path, directionality, blur, direct-illumination, trace-subset, roughness, shading-model, unit-length, and scene-scale prose while preserving parameter labels. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 46 flagged terms, and 3169 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
