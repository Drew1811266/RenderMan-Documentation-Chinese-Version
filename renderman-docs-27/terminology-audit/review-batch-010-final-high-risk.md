# Review Batch 010: Final High-Risk Terminology Cleanup

Status: completed
Created: 2026-06-30

## Scope

Tenth terminology cleanup batch. This batch targets all 15 pages that remain in the high-risk tier after Batch 009. The goal is to drive the page-risk report to zero high-risk pages while keeping the official RenderMan documentation layout and HTML structure unchanged.

## Acceleration Rules

- Group pages by product/domain and reuse the same terminology decisions across related pages.
- Preserve product names, shader/node names, API identifiers, parameter names, command options, paths, environment variables, config keys, enum values, UI labels, and literal examples.
- Translate ordinary explanatory prose that currently over-preserves English, especially job/task/engine/blade, file/frame/directory, viewport/window/screen/aspect ratio, light/lighting/material, attribute/object/archive, and render/batch/export wording.
- Keep UI/menu paths readable by translating surrounding prose while preserving literal menu labels when they are documented UI strings.
- Do not modify code/pre/script/style content or HTML attributes.
- After each completed page, run `python3 tools/audit_terminology.py scan-pages`, run page tag-count validation, and report the updated overall page percentage.
- Before closing the batch, run `python3 tools/audit_official_layout_alignment.py`.

## Page Groups

### DCC Workflow And Look Development

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 1 | `RFK27/546179471-PxrMatteID in Katana.html` | 233 -> 17 / low | Reviewed PxrMatteID matte/AOV workflow prose; translated object/material/output/compositing/tutorial/example/color-channel/user-attribute/value/pass/render/texture/result wording while preserving Katana attribute paths, shader/node names, parameter labels, file names, and MatteID identifiers. |
| 2 | `RFM27/544542955-Batch Rendering in Maya.html` | 231 -> 41 / low | Reviewed batch-rendering prose; translated batch render, render job, local queue, settings, preview render, file/frame/directory, command line, warning, installation, environment variable, RIB job structure, cache, processing command, and diagnostic information wording while preserving Maya/RenderMan UI labels, command examples, paths, flags, XML/RLF/RIB identifiers, and literal warning text. |
| 3 | `RFK27/546177025-RenderMan 27 for Katana.html` | 210 -> 29 / low | Reviewed Katana overview prose; translated plugin/nodes/macros, live rendering, lights/light filters, shaders, material workflow, framebuffer/render view, global illumination, ray tracing, area light, volume, curved surface, subsurface scattering, secondary output, pipeline, renderfarm, and standalone implementation wording while preserving RfK/PRMan product names, links, `renderSettings`, ROI/cropWindow/resolution, `it`, API, and official feature labels where needed. |
| 4 | `RFM27/544543053-Baking illumination.html` | 205 -> 26 / low | Reviewed illumination-baking prose; translated bake/output/settings/scene/render globals/menu/validation/object/image/file pattern/point cloud/world space/resolution/integrator/samples/noise/AOV/display channel/denoiser/batch render wording while preserving UI labels, `Max Samples`, `Dicing Strategy`, `Dicing Distance Length`, `Bake Render: Illumination`, Hider names, and parameter names. |
| 5 | `RFM27/544540223-Alembic Workflows.html` | 201 -> 49 / low | Reviewed Alembic workflow prose; translated archive/node/cache/geometry/material/shader/list/filter/annotation/debugging/export workflow wording while preserving Alembic, gpuCache, RLF, RenderMan Look File, menu paths, UI labels, model/author names, and literal options. Also calibrated the audit protection list for Alembic/gpuCache/RLF as protected technical identifiers. |
| 6 | `RFB27/544638905-Mesh Lights in Blender.html` | 201 -> 41 / low | Reviewed Blender mesh-light prose; translated geometry/emissive/material/shading group/area light/render visibility/deformation motion blur/color/intensity/temperature/sampling/near distance/light group/compositing/sample-balancing wording while preserving PxrMeshLight/PxrBlack/PxrTexture, UI labels, parameter labels, HDRI/sRGB/Rec 709/D65, and integrator names. |

### RenderMan Core And RenderMan University

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 7 | `RU/568787000-Start with Words.html` | 232 -> 10 / low | Reviewed creative-planning prose; translated artist/theme/brief/guidelines/message/story/emotion/viewer/synopsis/assets/van/tractor beam/character/backstory/clothing/props/weather/lighting/color palette/value/hue/shading/rendering/process wording while preserving author names, Art Challenge, UFO, and the work title `The Hunted`. |
| 8 | `REN27/542231325-The Viewing Transformation.html` | 219 -> 15 / low | Reviewed viewing-transformation prose; translated viewing transformation, camera-to-screen, screen-to-raster, screen/window/raster, pixel aspect ratio, frame aspect ratio, crop window, screen coordinate system, viewing pyramid/box, field of view, and anamorphic-view wording while preserving Ri* APIs, projection enum values, Panavision, and formula text. |
| 9 | `RU/656999009-Character Lighting Tips.html` | 204 -> 17 / low | Reviewed character-lighting prose; translated community/contributor/scenes/lighting tips, fill/key/rim lights, rig/setup, diffuser/blocker/ground plane, bounce/softening/sampling, lookdev scenarios, light-rig switcher, HDR maps, three-point lighting, color temperature, isolate lights, intensity, and contribution wording while preserving artist/work names, PxrDomeLight, UI labels, and scenario names. |

### Tractor Operations And APIs

| Order | Page | Starting Risk | Notes |
|---:|---|---:|---|
| 10 | `TRA/22184258-Idle Job or Task.html` | 220 -> 29 / low | Reviewed Tractor idle-job/task troubleshooting prose; translated job/task/work/scheduling/network/failure/command/log/file/ready/blocked/Blade/Engine/Dashboard/priority/requirements/limit-counter wording while preserving command expressions, state values, `afterJids`, `RecentErrorThrottle`, ports, trace labels, and service-key/limit identifiers. |
| 11 | `TRA/22184314-Job Author Python API.html` | 214 -> 20 / low | Reviewed Job Author Python API prose; translated module/interpreter/configuration/examples/classes/methods/spooling/blocking/owner/attributes/tasks/commands/serial subtask/exception/directory mapping/Engine connectivity/session/API-usage wording while preserving class names, methods, attributes, environment variables, file paths, and code identifiers. |
| 12 | `TRA/22184348-Upgrading.html` | 208 -> 15 / low | Reviewed Tractor upgrade/downgrade prose; translated Engine/Blade compatibility, active tasks, backup/upgrade/downgrade, job database, database schema, log files, job ID reuse, dispatching, multiple Engine deployment, configuration/data/database directories, shared volumes, and version-specific upgrade information while preserving `tractor-dbctl` commands, options, config keys, and state values. |
| 13 | `TRA/22184334-Getting Started.html` | 208 -> 20 / low | Reviewed Tractor getting-started prose; translated system services, studios/hosts, installation location, Engine/Blade process checks, licensing, route/firewall/connectivity tests, DNS aliases, ports, service-key matching, Blade capabilities, keywords, queue, Trace Job diagnostics, and dispatching issues while preserving commands, URLs, executable names, labels, and config entries. |
| 14 | `TRA/22184260-Tractor URL API.html` | 208 -> 34 / low | Reviewed URL API prose and calibrated URL/query-token audit protection; translated JSON response formatting, authentication/session ID, job actions, dispatch/pause text, stored filters/preferences/sessions, Engine/Blade query and control descriptions, NIMBY proxy/direct control, health statistics, metric samples, backlog/queue descriptions, and statslog ring-buffer wording while preserving literal URLs, query parameters, metric keys, HTTP headers, and API values. |
| 15 | `TRA/22184290-Blade Environment Configuration- Keys and Handlers.html` | 207 -> 42 / low | Reviewed Blade environment configuration prose; translated command/render/subprocess/environment variables, custom environment configuration, dictionaries, inherited environment, EnvKey definitions, handlers, launch environment, version/platform/install-location/path wording while preserving handler names, EnvKey, file names, environment variables, paths, profile/config keys, and examples. |

## Current Progress

- Reviewed pages: 15 / 15.
- Batch completion: 100.00%.
- Overall page review progress: 73 / 816 = 8.95%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 1 high / 278 medium / 536 low pages after `TRA/22184290-Blade Environment Configuration- Keys and Handlers.html`.
- Final layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser-sampled pages after Batch 010.
- Structure validation for `RFK27/546179471-PxrMatteID in Katana.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544542955-Batch Rendering in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFK27/546177025-RenderMan 27 for Katana.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544543053-Baking illumination.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544540223-Alembic Workflows.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFB27/544638905-Mesh Lights in Blender.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/568787000-Start with Words.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542231325-The Viewing Transformation.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RU/656999009-Character Lighting Tips.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184258-Idle Job or Task.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184314-Job Author Python API.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184348-Upgrading.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184334-Getting Started.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184260-Tractor URL API.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184290-Blade Environment Configuration- Keys and Handlers.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
