# Review Batch 014: Accelerated Medium-Risk Sweep

Status: completed
Created: 2026-07-01

## Scope

Accelerated terminology cleanup for the next highest medium-risk pages after Batch 013. `TRA/22184352-Release Notes.html` remains a watch item already rechecked in earlier batches and is skipped unless a later scan shows new actionable issues beyond protected release-note identifiers. This batch should continue reducing ordinary English fragments in Chinese prose while preserving true product names, DCC UI labels, RenderMan node names, parameter names, code literals, file formats, and command/API identifiers.

## Pages

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 1 | `TRA/22184236-Engine Metrics.html` | 127/medium -> 21/low | Completed; normalized Tractor engine metrics prose while preserving `Engine Metrics`, `tractor-engine`, `blade`, `slot`, `loadavg`, `service key`, socket/I/O terms, and command literals. |
| 2 | `RU/630915278-Interactive Rendering Tips.html` | 127/medium -> 34/low | Completed; normalized interactive rendering tutorial prose while preserving RenderMan XPU, DCC/product labels, UI/parameter labels, integrator names, and technical terms with useful bilingual glosses. |
| 3 | `RU/393805842-Creating a Wooden Floor.html` | 126/medium -> 24/low | Completed; normalized procedural wood-floor material tutorial prose while preserving RenderMan node names, shader parameter labels, texture provider/product names, UV/geometry identifiers, and useful bilingual technical terms. |
| 4 | `RFM27/544542501-AOVs.html` | 124/medium -> 18/low | Completed; calibrated Maya AOV UI labels and validated existing prose while preserving Display Channel/Driver, Pass, OpenEXR/Tiff format labels, precision/compression labels, remap labels, and AOV/channel settings. |
| 5 | `RFM27/544542444-Features.html` | 123/medium -> 37/low | Completed; normalized Maya Features, renderer, motion blur, shutter, OCIO, interactive denoiser, and Stylized Looks prose while preserving UI labels and parameter names. |
| 6 | `RFM27/544540118-Aggregate Volumes in Maya.html` | 123/medium -> 35/low | Completed; normalized Maya aggregate-volume, visibility override, joint sampling, OpenVDB parameter, and PxrSurface interior aggregate prose while preserving `rmanVolumeAggregateSet`, `globalVolumeAggregate`, `PxrPathTracer`, parameter labels, and camera/transmission/indirect enum values. |
| 7 | `RFM27/544540066-OpenVDB Volumes in Maya.html` | 123/medium -> 22/low | Completed; normalized OpenVDB volume workflow, Attribute Editor visibility note, VDB grid/voxel prose, visualizer options, and shading-network wording while preserving OpenVDB/VDB identifiers, RiVolume/RiBlobby, PxrVolume, UI labels, node names, and code node types. |
| 8 | `RFH27/544645977-AOV Setup and Viewing.html` | 123/medium -> 42/low | Completed; normalized Houdini AOV display/output, built-in AOV, custom LPE, filter, denoise, and compositing prose while preserving AOV/LPE terms, Houdini UI labels, RenderMan identifiers, OpenEXR, Beauty/Ci Display Channel, Gaussian, and literal LPE expressions. |
| 9 | `RU/656998602-Bakery Texturing.html` | 122/medium -> 9/low | Completed; normalized RenderMan University texturing tutorial prose for UVs, UDIMs, Substance fills/materials, variations, denoising, texture maps, and shading while preserving Substance, Pixar/Luca, UDIM, UV Shells, Unfold, RenderMan Denoiser, map type labels, and button text. |
| 10 | `RFH27/567279625-EnvDayLight in Solaris.html` | 122/medium -> 8/low | Completed; normalized Solaris EnvDayLight daylight, direction, shadow, tracing, integrator, manifold-walk, light-sample, and light-group prose while preserving EnvDayLight parameter labels, `use direction`, Pxr integrator names, On/Off enum values, and cited author/title names. |
| 11 | `RFH27/544645130-Adding Lights.html` | 122/medium -> 22/low | Completed; normalized Houdini light creation, light transformation, dome/portal light, mesh light, and visibility prose while preserving Pxr light node names, `RenderMan Shelf`, `Render TAB Menu`, `Dome Light`, visibility UI labels, and light parameter names. |
| 12 | `RFM27/544541201-Texture Manager.html` | 121/medium -> 22/low | Completed; normalized Maya Texture Manager conversion queue, image/texture processing, interactive/batch rendering, backend/process, fallback path, extension, and configuration-rule prose while preserving Texture Manager, OpenImageIO, txmake, rmanoiiotool, UI buttons, queue names, Tractor job, and format/tool identifiers. |
| 13 | `TRA/22184254-Job Scripting.html` | 119/medium -> 43/low | Completed; normalized Tractor job scripting prose around service keys, service-key expressions, substitutions, environment variables, shared server check-outs, shell/tokenization notes, progress reporting, and exit status while preserving Tractor operators, command syntax, example host names, shell commands, and literal variables. |
| 14 | `REN27/542222017-Stylized AOVs.html` | 118/medium -> 42/low | Completed; normalized Stylized AOV bridge-tool, display-filter, shader-result, line, edge-detection, surface-normal, projection, coordinate-space, and workflow prose while preserving AOV names, shader labels, `Line Type` values, `PxrStylizedControl`, `beauty`, and `Primary`. |
| 15 | `TRA/22184272-Directory Mapping.html` | 117/medium -> 17/low | Completed; normalized Tractor directory-mapping, file-system path, operating-system, asset-path, job-script, directory-map, zone, mapped-drive, Windows service, credential, persistence, and account prose while preserving `-dirmaps`, `%D()`, `DirMapZone`, UNC/NFS markers, path examples, and Windows credential values. |
| 16 | `REN27/542222552-PxrAttribute.html` | 116/medium -> 14/low | Completed; normalized PxrAttribute prose around attributes, color attributes, user attributes, attribute namespaces, shader-ball wording, transform nodes, and DCC usage while preserving node names, parameter labels, type values, `trace:maxdiffusedepth`, `user:Ball`, OpScript code, and Katana attribute paths. |
| 17 | `RU/592019497-Light Randomization.html` | 113/medium -> 20/low | Completed; normalized RenderMan University light-randomization tutorial prose around Solaris scene graph, lights, randomization, Attribute Wrangle nodes, neon tubes, frames, parameters, intensity, bulb color/value, animation, fairground bulbs, mesh lights, USD lights, and code snippets while preserving `attributewrangle`, VEX, `Bulb_COL`, `Bulb_INT`, `$FF`, `Glow`, and RenderMan node/product labels. |
| 18 | `RU/567509003-The Hunted Texturing.html` | 115/medium -> 3/low | Completed; normalized RenderMan University texturing/story tutorial prose around texturing, art style, vehicle/truck/van wording, paint wear, stains, patina, color references, past-life story cues, decals/stickers, presets, materials, channels, texture files, and shading networks while preserving Substance Painter, Mari, RenderMan Preset Browser, DCC names, `.exr`, `.tex`, and turntable filenames. |
| 19 | `REN27/542223359-PxrDispTransform.html` | 114/medium -> 21/low | Completed; normalized PxrDispTransform scalar/vector displacement, float/vector data, displacement value, object-space/world-space, displacement direction, and output prose while preserving PxrDispTransform parameter labels, enum labels, Mudbox/ZBrush names, `spline("catmullrom", ...)`, `resultXYZ`, and code literals. |
| 20 | `RFK27/546177673-Subdivision Surfaces in Katana.html` | 113/medium -> 9/low | Completed; normalized Katana subdivision-surface, geometry, texture-coordinate, normal, faceting, tessellation, displacement, mesh, and developer-prose wording while preserving `polymesh`, `subdmesh`, `AttributeSet`, `PrmanObjectStatements`, Catmull-Clark/Loop values, `micropolygonlength`, `type`, code literals, and geometry attribute paths. |

## Current Progress

- Completed and updated: 2026-07-01 10:58 CST.
- Reviewed pages: 20 / 20.
- Batch completion: 100.00%.
- Overall page review progress: 132 / 816 = 16.18%.
- Resume from: define Batch 015 from the updated medium-risk report.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 0 high / 196 medium / 619 low pages after Batch 014 page 20.
- Structure validation for `TRA/22184236-Engine Metrics.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/630915278-Interactive Rendering Tips.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/393805842-Creating a Wooden Floor.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544542501-AOVs.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544542444-Features.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544540118-Aggregate Volumes in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544540066-OpenVDB Volumes in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFH27/544645977-AOV Setup and Viewing.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/656998602-Bakery Texturing.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFH27/567279625-EnvDayLight in Solaris.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFH27/544645130-Adding Lights.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544541201-Texture Manager.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184254-Job Scripting.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542222017-Stylized AOVs.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184272-Directory Mapping.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542222552-PxrAttribute.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/592019497-Light Randomization.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/567509003-The Hunted Texturing.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542223359-PxrDispTransform.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFK27/546177673-Subdivision Surfaces in Katana.html`: tag-count diff shows no source tags removed; the translated page has the expected offline stylesheet and two offline script elements (`link`: 0 -> 1, `script` tag count: 0 -> 4 including opening and closing script tags).
- Tractor engine metrics prose reviewed using the existing Tractor component/metric/command-literal protection rules; no new audit calibration was required.
- RenderMan University interactive-rendering tutorial prose reviewed using the existing DCC/product/UI/parameter protection rules; no new audit calibration was required.
- RenderMan University wood-floor material tutorial prose reviewed using the existing RenderMan node/material/texture-provider protection rules; no new audit calibration was required.
- Audit calibration added for Maya AOV UI labels including Display Channel/Driver, Pass, precision/compression labels, remap labels, and common file-format/enum values.
- Maya Features prose reviewed using the existing Maya UI/renderer/parameter protection rules; no new audit calibration was required.
- Maya aggregate-volume prose reviewed using the existing Maya volume, visibility, OpenVDB, and protected-parameter rules; no new audit calibration was required.
- Maya OpenVDB volume prose reviewed using the existing OpenVDB, VDB grid, Maya UI, RIB, and protected-parameter rules; no new audit calibration was required.
- Houdini AOV setup prose reviewed using the existing AOV/LPE, display driver/channel, filtering, denoising, OpenEXR, and Houdini UI protection rules; no new audit calibration was required.
- RenderMan University texturing prose reviewed using the existing texture/material/shading/Substance/UDIM/tutorial-prose rules; no new audit calibration was required.
- Audit calibration added for EnvDayLight/Solaris parameter labels and enum values including `use direction`, Specular/Diffuse Amount, shadow controls, Trace Light Paths, Manifold Walk controls, Light Samples, Light Group, and Importance Multiplier.
- Audit calibration added for capitalized light visibility UI labels including Camera Visibility, Transmission Visibility, and Indirect Visibility while leaving lowercase prose phrases reviewable.
- Maya Texture Manager prose reviewed using the existing texture, txmake/OpenImageIO, file-format, queue, settings, and protected UI/button label rules; no new audit calibration was required.
- Tractor job scripting prose reviewed using the existing Tractor operator, shell-command, service-key, environment-variable, and syntax-placeholder protection rules; no new audit calibration was required.
- Stylized AOV prose reviewed using the existing Stylized Looks, AOV, shader-label, `Line Type`, and `PxrStylizedControl` protection rules; no new audit calibration was required.
- Tractor directory-mapping prose reviewed using the existing Tractor path, UNC/NFS, `DirMapZone`, `%D()`, Windows service, and credential-value protection rules; no new audit calibration was required.
- PxrAttribute prose reviewed using the existing RenderMan node, parameter-label, type-value, attribute-name, and DCC/code-literal protection rules; no new audit calibration was required.
- RenderMan University light-randomization tutorial prose reviewed using the existing RenderMan/Houdini/Solaris, VEX, wrangle, primvar, meshlight, and USD protection rules; no new audit calibration was required.
- RenderMan University texturing/story prose reviewed using the existing Substance Painter, Mari, RenderMan Preset Browser, DCC, file-extension, and turntable-filename protection rules; no new audit calibration was required.
- Audit calibration added for PxrDispTransform parameter and enum labels including Displacement Type, Vector Space, Displacement Height/Depth/Center/Scale Space, Use Displacement Direction, Displacement Direction Space, Generic Vector, Mudbox Vector, ZBrush Vector, Absolute Tangent, Relative Tangent, and Interpolate Depth and Height.
- PxrDispTransform prose reviewed using the calibrated parameter/enum protection rules; no additional calibration was required after page validation.
- Katana subdivision-surface prose reviewed using the existing geometry, normal, tessellation, crease, Catmull-Clark, primvar, and code-literal protection rules; no new audit calibration was required.
- Final layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser-sampled pages after Batch 014 page 20.

## Acceleration Rules

- Keep UI labels, parameter labels, enum values, node names, code/API identifiers, and literal file/command syntax in English where that is how the software presents them.
- Translate ordinary explanatory nouns such as task, request, host, material, map, node, scene, object, directory, and value when they are prose rather than UI labels.
- For tutorial/story pages, keep proper names and source titles, but avoid unnecessary English inside normal Chinese sentences.
- After each edited page, run `python3 tools/audit_terminology.py scan-pages` and page tag-count validation.
- Run `python3 tools/audit_official_layout_alignment.py` before closing a page group or batch.
