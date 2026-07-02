# Review Batch 013: Accelerated Medium-Risk Sweep

Status: completed
Created: 2026-06-30

## Scope

Accelerated terminology cleanup for the current top medium-risk pages after Batch 012. `TRA/22184352-Release Notes.html` remains a watch item from Batch 011 and is skipped unless a later scan shows new actionable issues. This batch should favor grouped text-node-only normalization and audit-rule calibration for true identifiers, UI labels, enum values, and code-adjacent literals.

## Pages

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 1 | `REN27/542221476-Visibility.html` | 150/medium -> 0/low | Completed; normalized visibility/ray/attribute prose while preserving UI paths and shader parameter labels. |
| 2 | `RU/657162271-Stirling Compositing.html` | 149/medium -> 0/low | Completed; normalized compositing/tutorial prose while preserving Nuke, ACES, OCIO, file-format, shortcut, and curve/tool identifiers. |
| 3 | `RFM27/544541369-Lighting in Maya.html` | 149/medium -> 0/low | Completed; normalized Maya lighting, light type, visibility, and material prose while preserving Pxr light nodes and Maya UI labels. |
| 4 | `RFK27/546177488-Volumes in Katana.html` | 147/medium -> 0/low | Completed; normalized Katana volume/OpenVDB workflow prose while preserving PrmanVolume, PxrVolume, VDB, primvar, enum, and parameter identifiers. |
| 5 | `RFK27/546178855-PrmanObjectStatements.html` | 143/medium -> 0/low | Completed; normalized Katana object statement, dicing, traversal, and Geolib prose while preserving RenderMan attributes, RIB fragments, enum values, and parameter paths. |
| 6 | `REN27/542238759-542238759.html` | 143/medium -> 28/low | Completed; normalized ordinary release-note prose while preserving RenderMan/XPU feature names, UI labels, enum values, file names, and API identifiers. |
| 7 | `RFB27/544639651-Render Holdouts in Blender.html` | 141/medium -> 0/low | Completed; normalized Blender holdout/compositing prose while preserving Blender UI options, AOV/LPE labels, filter node names, and `__illumholdout`. |
| 8 | `TRA/22184326-Initial Configuration.html` | 140/medium -> 14/low | Completed; normalized Tractor initial-configuration prose while preserving config keys, paths, environment variables, command-line parameters, service names, and component labels. |
| 9 | `TRA/22184264-JSON Job Scripting.html` | 140/medium -> 4/low | Completed; normalized JSON job scripting prose while preserving `tractor-spool`, command-line flags, JSON example names, RIB file names, field names, and `RemoteCmd` literals. |
| 10 | `RU/563478530-The Hunted Story.html` | 140/medium -> 9/low | Completed; normalized RenderMan University narrative/tutorial prose while preserving UFO, Google Maps/Street View, ShotDeck, Panavision/Panaflex, and film-title proper names. |
| 11 | `TRA/22184232-Data Filtering.html` | 139/medium -> 26/low | Completed; normalized Dashboard filtering prose while preserving joblist/bladelist query types, Dashboard UI labels, filter dialog names, and command/path examples. |
| 12 | `TRA/22184226-Task Graph Pane.html` | 138/medium -> 4/low | Completed; normalized Task Graph pane prose while preserving Task Graph/Task Info UI labels, Control-click interaction label, chaser command term, and joblist query type. |
| 13 | `REN27/542221096-PxrDisplace.html` | 138/medium -> 8/low | Completed; normalized displacement/plugin, object/world space, scalar/vector displacement, shading-rate, and bounding-box prose while preserving PxrDisplace/PxrDispTransform nodes, parameter labels, `micropolygonlength`, `sqrt`, Mudbox/ZBrush, and result identifiers. |
| 14 | `RU/392265765-Procedural Ground Dirt.html` | 134/medium -> 9/low | Completed; normalized procedural ground-dirt tutorial prose while preserving RenderMan node names, Blender/Maya UI labels, coordinate-system labels, ramp/ink-mode labels, media names, and DCC/tool proper names. |
| 15 | `RFM27/544540989-Using Material Layers.html` | 134/medium -> 26/low | Completed; normalized Maya material-layer workflow prose while preserving PxrLayerSurface/PxrLayerMixer/PxrLayer nodes, Input Material connections, layer labels, shader parameter labels, Maya pattern names, and downloadable/resource names. |
| 16 | `TRA/22184274-tractor-blade.html` | 133/medium -> 15/low | Completed; normalized tractor-blade command-help prose while preserving command options, host/port placeholders, environment variables, config keys, signal names, logging identifiers, and command examples. |
| 17 | `TRA/22184230-Query Pane.html` | 132/medium -> 21/low | Completed; normalized Query Pane UI prose while preserving query entity type values, `jid`/`tid`, `shift-select`, `Enter`, Dashboard labels, and linked search-clause syntax. |
| 18 | `RFH27/544642975-Preset Browser.html` | 132/medium -> 32/low | Completed; normalized Houdini Preset Browser prose while preserving Preset Browser, UI labels, node names, file formats, environment variables, library paths, and asset/package identifiers. |
| 19 | `TRA/22184298-Creating a custom Environment Handler.html` | 131/medium -> 8/low | Completed; normalized Tractor environment-handler scripting prose while preserving class/function names, envkeys, command literals, environment variables, path fragments, and component names. |
| 20 | `RFK27/546178051-PrmanSignalVisualizer.html` | 131/medium -> 49/low | Completed; normalized Katana signal-visualizer prose while preserving PrmanSignalVisualizer, Katana UI labels, parameter names, node names, mode labels, `signal`, and `vstruct`. |

## Current Progress

- Reviewed pages: 20 / 20.
- Batch completion: 100.00%.
- Overall page review progress: 112 / 816 = 13.73%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 0 high / 221 medium / 594 low pages after Batch 013 completion.
- Structure validation for `REN27/542221476-Visibility.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/657162271-Stirling Compositing.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544541369-Lighting in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFK27/546177488-Volumes in Katana.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFK27/546178855-PrmanObjectStatements.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542238759-542238759.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFB27/544639651-Render Holdouts in Blender.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184326-Initial Configuration.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184264-JSON Job Scripting.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/563478530-The Hunted Story.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184232-Data Filtering.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184226-Task Graph Pane.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542221096-PxrDisplace.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/392265765-Procedural Ground Dirt.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544540989-Using Material Layers.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184274-tractor-blade.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184230-Query Pane.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFH27/544642975-Preset Browser.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184298-Creating a custom Environment Handler.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFK27/546178051-PrmanSignalVisualizer.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Audit calibration added for RenderMan for DCC product labels, visibility UI paths, and PxrSurface translucency parameter labels.
- Audit calibration added for Nuke UI labels, `.png`, keyboard shortcut, Bezier/B-spline, and roto paint identifiers.
- Audit calibration added for RenderMan Shelf/Menu, Hypershade, Light Data, Gobo/Cookie, constant Bxdf, glow, and emission identifiers.
- Audit calibration added for Katana volume/OpenVDB parameter labels, `box`/`vdb`/`uniform` enum values, mipmap terms, and density-bias/incandescence identifiers.
- Audit calibration added for Katana object-statement labels, `Display Format`, `identifier:name`, `dice:minlength`, `polygon:smoothnormals`, `Geolib`, `Ndsp`, `Reves`, `Op Chain`, and `Instance Attributes` contexts.
- Audit calibration added for RenderMan 27 release-note feature names, XPU/OpenEXR/Stylized Looks identifiers, Blender/Solaris UI labels, texture enums, LPE/AOV prefixes, and release-note file/API literals.
- Audit calibration added for Blender holdout UI labels, `traceholdout`, `adapt all`, `__illumholdout`, holdout LPE prefix, and compositing operation labels.
- Tractor initial-configuration prose reviewed using the existing Tractor component/configuration protection rules; no new audit calibration was required.
- Tractor JSON job scripting prose reviewed using the existing Tractor command/API/example-literal protection rules; no new audit calibration was required.
- RenderMan University narrative prose reviewed; no new audit calibration was required.
- Audit calibration added for Dashboard filter UI labels (`Filter Lister`, `Filter Editor`, `Filter Name`, pulldown labels, time-rule labels) and JavaScript as a protected programming-language name.
- Audit calibration added for Task Graph/Task Info UI labels, `Control-click`, `RenderMan format`, `Alfred format`, and `chaser` command terminology.
- Audit calibration added for PxrDisplace section/parameter labels including `Displacement Space`, `Displacement Types`, `Input Parameters`, `Displacement Bounds`, `Scalar Displacement`, `Vector Displacement`, `Model Displacement`, and `Micropolygon Length`.
- Audit calibration added for procedural shading UI/tool labels including `RenderMan Geometry`, `Export as CoordSys`, `Plain Axis`, `3D Placement`, `Coordinate System`, `Ramp Type`, `T Ramp`, `EmitColor`, `Multiply ink mode`, Mari, and Substance Painter.
- Audit calibration added for material-layer UI/API labels including `PxrLayerMixer`, `PxrLayerSurface`, `Layer 1`, `Input Material`, `Copper/Bronze`, `Diffuse`, `Primary Specular`, `Bias Normal`, `Red result`, `pxrMaterialOut`, and `inputMaterial`.
- Tractor command-help prose reviewed using the existing Tractor command/configuration protection rules; no new audit calibration was required.
- Query Pane prose reviewed using the existing Tractor query/entity protection rules; no new audit calibration was required.
- Houdini Preset Browser prose reviewed using the existing DCC UI/node/file-format/path/environment-variable protection rules; no new audit calibration was required.
- Tractor environment-handler prose reviewed using the existing Tractor class/function/envkey/environment-variable protection rules; no new audit calibration was required.
- Katana signal-visualizer prose reviewed using the existing Katana UI/node/parameter protection rules; no new audit calibration was required.
- Final layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser-sampled pages after Batch 013 completion.

## Acceleration Rules

- For pages with repeated UI/parameter tables, first restore/protect exact identifiers, then translate surrounding prose.
- For tutorial/story pages, prioritize removing unnecessary English in narrative sentences while preserving product names, node names, file names, UI labels, and shader identifiers.
- After each edited page, run `python3 tools/audit_terminology.py scan-pages` and page tag-count validation.
- Run `python3 tools/audit_official_layout_alignment.py` before closing a page group or batch.
