# Review Batch 040: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 039. This batch targets Maya custom-node installation and displacement prose, Katana render-settings and displacement prose, Houdini fur/hair prose, and Blender display/sample-filter and projection-plugin prose.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, environment variables, file names, code identifiers, and acronyms. Translate ordinary prose terms such as patterns, plugins, nodes, artists, session, config files, environment variables, displacement workflow, tessellation, hard normals, mesh, cracks, render input/output, framebuffer, scene graph, fur, hair, curve attributes, sample/display filters, adaptive sampler, projection plugin, lens, camera, viewport, bounds, network, and surface shading when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFM27/544541146-Installing Custom Nodes.html` | 39/low | Translate custom node/plugin/config prose while preserving environment variables, JSON files, and node IDs. |
| 2 | `RFM27/544540663-Using Displacement.html` | 39/low | Translate displacement workflow, tessellation, hard-normal, mesh, crack, smoothed-normal, and interpolation prose while preserving parameter names. |
| 3 | `RFK27/546178764-Render Settings in Katana.html` | 39/low | Translate render input/output, framebuffer, scene graph, visibility, transmission rays, error-handler and attribute-function prose while preserving Katana/RenderMan attribute names. |
| 4 | `RFH27/544643901-Fur and Hair in Houdini.html` | 39/low | Translate fur/hair, curve-attribute, width, hair-width, sample, aliasing, shader-path, tube/ribbon, and display prose while preserving node and UI labels. |
| 5 | `RFB27/544639822-Sample and Display Filters in Blender.html` | 39/low | Translate sample/display-filter, camera-ray sample, framebuffer, adaptive-sampler, deep-image, World-node, and filter-slot prose while preserving plugin/node names. |
| 6 | `RFK27/546178105-Using Displacement.html` | 38/low | Translate geometric-detail, maps, vector/scalar displacement, bounds, renderer, surface, network, surface-shading and material-location prose while preserving node names and CEL paths. |
| 7 | `RFB27/544639119-Projection Plugins in Blender.html` | 38/low | Translate projection-plugin, lens, camera type, projection, parameter, field-of-view, and viewport prose while preserving plugin names and UI labels. |

## Results

Edited 62 visible article text nodes. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFM27/544541146-Installing Custom Nodes.html` | 6/low | Translated Pattern/plugin/node/config/environment-variable prose while preserving environment variables, JSON names, node IDs, metadata, `.args`, tags, and `light`. |
| 2 | `RFM27/544540663-Using Displacement.html` | 11/low | Translated displacement workflow, tessellation, hard-normal, mesh, crack, smoothed-normal, cube, displacement-pattern, sharp-edge, and normal-interpolation prose while preserving parameter names. |
| 3 | `RFK27/546178764-Render Settings in Katana.html` | 22/low | Translated render input/output, camera/framebuffer, scene-graph, transmission-ray, custom-preset, and attribute-function prose while preserving Katana/RenderMan attribute names. |
| 4 | `RFH27/544643901-Fur and Hair in Houdini.html` | 24/low | Translated fur/hair, curve-attribute, width, hair-width, sample, aliasing, shader-path, tube/ribbon, normal, and display prose while preserving Houdini node/UI labels. |
| 5 | `RFB27/544639822-Sample and Display Filters in Blender.html` | 25/low | Translated sample/display-filter, camera-ray sample, framebuffer, deep-image, adaptive-sampler, World-node, filter-slot, and shader-node prose while preserving plugin/node labels. |
| 6 | `RFK27/546178105-Using Displacement.html` | 9/low | Translated geometric-detail, maps, vector/scalar displacement, bounds, renderer, surface, object, network, surface-shading, Pattern output, and material-location prose while preserving node names and CEL paths. |
| 7 | `RFB27/544639119-Projection Plugins in Blender.html` | 19/low | Translated projection-plugin, lens, camera type, projection, parameter, field-of-view, and viewport prose while preserving plugin names and UI labels. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 46 flagged terms, and 3190 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
