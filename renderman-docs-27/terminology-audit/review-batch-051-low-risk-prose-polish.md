# Review Batch 051: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02
Completed: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 050. This batch targets Houdini export/curves/volume/shading workflow prose and Blender subdivision/light-linking workflow prose.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, attribute names, file formats, shader names, project names, acronyms, and code identifiers. Translate ordinary prose terms such as viewport, look-development, shading calculation data, attributes, volumes, OpenVDB sequence export, diffuse/emission color fields, DCCs, shader, string name, width attribute, shelf button, curve basis, opacity samples, stochastic samples, minimum width, volume SOP, simulation, material network, grids, vector grid, aggregate volumes, menu/shelf tool prose, primitive attribute, custom tool, visibility attributes, Materials, custom integrator prose, Subdivision Surface modifier, viewport, normals, mesh/data properties/polygon prose, light linking editor, link/unlink, RenderMan light, result, and rect light when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFH27/544646833-Export.html` | 29/low | Translate export, viewport/look-development, shading-data, attributes, volume fields, DCC/shader/string-name prose while preserving HDA, DCC, VDB/OpenVDB, preset, and UI labels. |
| 2 | `RFH27/544643849-Curves.html` | 27/low | Translate curve, width-attribute, shelf-button, curve-basis, opacity/stochastic samples, ROP/minimum-width prose while preserving node/menu labels. |
| 3 | `RFH27/544640830-Rendering SOP Volumes.html` | 24/low | Translate volume SOP, VDB simulation, volume-material-network, grid/fireball, motion-blur/vector-grid, path prose while preserving LOP/SOP/node names. |
| 4 | `RFH27/544644033-Aggregate Volumes.html` | 24/low | Translate aggregate-volume, shelf/menu tool, primitive-attribute, custom-tool, visibility-attribute prose while preserving parameter names and UI labels. |
| 5 | `RFH27/544644296-Shading in Houdini.html` | 24/low | Translate material/Bxdf/integrator/custom/gold and category-heading prose while preserving shader/material node names. |
| 6 | `RFB27/544638001-Subdivision Surfaces in Blender.html` | 23/low | Translate Subdivision Surface modifier, viewport, normals, mesh, data properties, polygon, edge-creasing prose while preserving product names and UI labels. |
| 7 | `RFB27/544637371-Light Linking Editor.html` | 23/low | Translate light-linking editor/link/unlink/result/rect-light prose while preserving UI labels and menu names. |

## Results

- Updated 54 visible article text nodes across 7 pages; HTML tag fingerprints were preserved during every page write.
- `RFH27/544646833-Export.html`: 29/low -> 8/low. Cleaned SOP-network, viewport/look-development, shading calculation data, volume-shader, attribute/volume/export, diffuse/emission color-field, DCC/preset-shader, volume-field, shader, and string-name prose while preserving HDA, VEX/VDB, DCC, OpenVDB, UI labels, and option names.
- `RFH27/544643849-Curves.html`: 27/low -> 10/low. Cleaned Curves, camera-facing/billboard, width-attribute, shelf-button, tab/property, curve-basis, integrator/opacity/stochastic-sample, ROP, and min-sample prose while preserving SOP names, parameter labels, and menu paths.
- `RFH27/544640830-Rendering SOP Volumes.html`: 24/low -> 7/low. Cleaned SOP Path wording, volume SOP, VDB simulation, volume-material network, grid/fireball, volume-motion-blur, vector/float-grid, and path prose while preserving LOP/SOP/node names and field identifiers.
- `RFH27/544644033-Aggregate Volumes.html`: 24/low -> 4/low. Cleaned aggregate-volume, shelf/menu tool, volume-aggregate, primitive-attribute, custom-tool, and visibility-attribute prose while preserving parameter names, UI labels, and visibility type names.
- `RFH27/544644296-Shading in Houdini.html`: 24/low -> 0/low. Cleaned material/Bxdf/integrator/custom/gold prose and ordinary category headings while preserving shader/material node names and Pattern-node terminology.
- `RFB27/544638001-Subdivision Surfaces in Blender.html`: 23/low -> 8/low. Cleaned Subdivision Surface modifier, viewport, normal, mesh, data-property, polygon, edge-creasing, and crease-weight prose while preserving OpenSubdiv, RfB, SubD, UI labels, and modifier names.
- `RFB27/544637371-Light Linking Editor.html`: 23/low -> 10/low. Cleaned light-linking editor, link/unlink, RenderMan-light, result, light-link list, and rect-light prose while preserving Light Linking Editor, Object Context Menu, enum labels, Invert Light Linking, and Workflow UI labels.

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` passed: 0 high / 1 medium / 814 low pages, 31 flagged terms, 2962 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` passed: 816/816 static pages and 816/816 browser-sampled pages.
