# Review Batch 009: Accelerated High-Risk Terminology Cleanup

Status: completed
Created: 2026-06-30

## Scope

Ninth terminology cleanup batch. This batch expands the stage size from 5 pages to 15 pages in response to the observed slow page-by-page throughput. The workflow remains conservative: apply high-confidence text-node-only normalization across related pages first, then manually review each page's remaining ambiguous UI labels, code-adjacent prose, product names, shader/node names, file paths, commands, and examples.

## Acceleration Rules

- Use grouped terminology normalization for repeated prose-level terms instead of rediscovering the same decisions page by page.
- Preserve product names, shader/node names, UI labels, API identifiers, parameter names, command options, paths, environment variables, config keys, enum values, and literal examples.
- Translate ordinary explanatory prose that currently over-preserves English, especially operational words like host, queue, task, job, service, command line, file, output, response, node, material, volume, projection, sampling, and visibility.
- Do not modify code/pre/script/style content or HTML attributes.
- After each completed page, run `python3 tools/audit_terminology.py scan-pages`, run page tag-count validation, and report the updated overall page percentage.
- Before closing the batch, run `python3 tools/audit_official_layout_alignment.py`.

## Page Groups

### Tractor Operations

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 1 | `TRA/22184318-tq Cookbook.html` | 268 -> 44 / low | Reviewed tq usage and farm-management prose; translated command-line tool, search clause, job/task/queue, result set, database, resource utilization, Blade/rack/farm, command history, retry, and maintenance descriptions while preserving flags, command syntax, state expressions, field names, shell snippets, and example values. |
| 2 | `TRA/22184328-Setting Up Services.html` | 265 -> 37 / low | Reviewed service setup prose across systemd, sysVinit, Windows service, macOS launchd, and firewall sections; translated system service, boot/start, settings files, command line, override, owner, logging, user account, registry, .plist, permissions, network access, and port descriptions while preserving service names, paths, unit keys, UI labels, commands, and links. |
| 3 | `TRA/22184214-Job List Pane.html` | 243 -> 48 / low | Reviewed Dashboard job-list prose; translated job/task/queue/archive/pane/graph/engine/notes/progress/filter wording, keyboard and menu explanations, archive behavior, task graph navigation, and reload timer descriptions while preserving literal UI labels, status values, keyboard names, menu commands, and query-page references. |
| 4 | `TRA/22184332-Image Preview.html` | 241 -> 14 / low | Reviewed image-preview prose; translated browser/Web server, desktop, image file, output image, preview handler, display program, plugin, central fileserver, network path, document root, URI handler, and device/workstation descriptions while preserving `Preview Output Image`, JavaScript callback names, `SiteURLMap`, URI examples, paths, and `mailto` literals. |
| 5 | `TRA/22184262-Search Clauses.html` | 238 -> 42 / low | Reviewed search-clause syntax prose; translated search clause, query page/API/tool, Boolean expression, comparison operator, attribute/value, quote, list matching, alias, affiliated entity, time comparison, and unit descriptions while preserving literal field names, status values, operators, usernames, examples, and command syntax. |
| 6 | `TRA/22184356-Implementation.html` | 235 -> 20 / low | Reviewed Tractor implementation and bundle prose; translated Engine/Blade/database/job queue, spooling, Dashboard layout, release contents, component list, PostgreSQL/Python/Tcl bundle, backend data store, scripted access, and throughput descriptions while preserving component names, module/package names, API/tool names, schema terms, config values, and command literals. |

### RenderMan Volumes And Projection

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 7 | `REN27/542220781-PxrVolume.html` | 261 -> 45 / low | Reviewed PxrVolume volume-rendering prose; translated volume shader, OpenVDB file, plugin, motion blur, velocity, scattering, sampling, equiangular sampling, density, anisotropy, light filter, mesh light, and input connection wording while preserving shader names, parameter labels, primvar names, attributes, method names, and literal examples. |
| 8 | `RFH27/544643998-Volumes.html` | 260 -> 32 / low | Applied volume terminology decisions in Houdini context; translated Houdini pipeline, exported volumes, OpenVDB file, motion blur, velocity, scattering, sampling, density, anisotropy, light filter, mesh light, and shadow prose while preserving Houdini/RenderMan UI labels, shader names, parameter names, primvars, attributes, and literal examples. |
| 9 | `RFH27/544644370-Volume Material.html` | 257 -> 31 / low | Reviewed Houdini volume-material setup and inherited PxrVolume prose; translated material assignment, pure volume, OpenVDB file, motion blur, velocity, scattering, sampling, density, anisotropy, light filter, mesh light, shadow, and connection wording while preserving VOP/OBJ/MAT labels, shader names, node names, parameter labels, primvars, attributes, and literal examples. |
| 10 | `REN27/542224403-PxrProjector.html` | 255 -> 28 / low | Reviewed projection/manifold prose; translated projection manifold, coordinate system, projected texture, geometry, transform, projection direction, underlying surface material, scene units, authoring package, camera film back, mask output, frustum, planar clamp, viewport representation, 2D manifold, output mask, and underlying texture wording while preserving shader names, parameter labels, enum labels, primvars, Maya menu labels, and trace-set identifiers. |

### DCC Workflow And Look Development

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 11 | `RU/631308308-Modeling Guidelines.html` | 260 -> 38 / low | Reviewed modeling guidelines prose; translated subdivision surface, polygon mesh, crease/corner, sharp/semi-sharp features, displacement cracks, topology constraints, heavy geometry, micropolygons, dicing, micropolygon length, memory, ray tracing, displacement/bump mapping, and performance wording while preserving Catmull-Clark, Loop, Bilinear, TTFP, RAM, PxrVisualizer, ZBrush, and formal parameter labels. |
| 12 | `RFK27/546179303-XGen in Katana.html` | 257 -> 45 / low | Reviewed XGen/Katana workflow prose; translated hair/fur, render workflow, procedural process, arguments, node graph, scene graph, screen snapshot, file/path, render scene, camera matching, shading network, primitive variables, material, texture, and wire wording while preserving XGen, Katana/Maya labels, node names, flags, file paths, collection/description values, RenderMan DSO references, and shader names. |
| 13 | `RFM27/544540421-Assign materials.html` | 246 -> 32 / low | Reviewed material assignment and Dynamic Rules workflow prose; translated shape, material, attribute, rule, editor, node list, matching engine, glob matching, Alembic node list, instance, archive, hierarchy, expression field, shading node, asset, RLF assignment, and rule-order wording while preserving gpuCache, RLF, Alembic, UI labels where literal, exact/glob/re labels, code examples, path expressions, and literal `rivet`/`ring` examples. |
| 14 | `RU/657555758-Lama Skin Shading.html` | 244 -> 46 / low | Reviewed Lama skin-shading prose; translated skin shader, texture transfer, scan cleanup, maps, surfacing channels, roughness channel, pores, clear coat, values, references, SSS layer, skin material, masks, scale/unit length, anisotropy, meniscus handling, primary specular, displacement setup, Bump to Roughness, bump details, filter scale, and accuracy wording while preserving artist/title credits, Lama shader names, TexturingXYZ/Mari/ZBrush names, BTR/Pxr node names, and formal parameter labels. |
| 15 | `RFM27/544542819-Interactive Rendering in Maya.html` | 241 -> 46 / low | Reviewed interactive-rendering workflow prose; translated IPR button, shelf, menu, preview, pixels, session, viewport rendering, monitor resolution, progress bar, crop window/region, render/export, objects/material picking, hidden/templated nodes, playblast controls, image/quality, and batch rendering wording while preserving RenderMan/Maya UI labels, menu paths, command examples, option names, and It/Image Tool references. |

## Current Progress

- Reviewed pages: 15 / 15.
- Batch completion: 100.00%.
- Overall page review progress: 58 / 816 = 7.11%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 15 high / 287 medium / 513 low pages after `RFM27/544542819-Interactive Rendering in Maya.html`.
- Final layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser-sampled pages after Batch 009.
- Structure validation for `TRA/22184318-tq Cookbook.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184328-Setting Up Services.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184214-Job List Pane.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184332-Image Preview.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184262-Search Clauses.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184356-Implementation.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542220781-PxrVolume.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFH27/544643998-Volumes.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFH27/544644370-Volume Material.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542224403-PxrProjector.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/631308308-Modeling Guidelines.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFK27/546179303-XGen in Katana.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544540421-Assign materials.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/657555758-Lama Skin Shading.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544542819-Interactive Rendering in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
