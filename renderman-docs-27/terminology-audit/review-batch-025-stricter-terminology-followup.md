# Review Batch 025: Stricter Terminology Follow-Up

Status: completed
Created: 2026-07-01

## Scope

Follow-up cleanup after T1 terminology calibration reduced `review-required` decisions from 65 to 22. This batch targets the new medium-risk pages surfaced by stricter decisions for terms such as `Light Filter(s)`, `object space`, `Prototype Attributes`, and `user attributes`.

`TRA/22184352-Release Notes.html` remains medium in the global report but is excluded from this batch because it was conservatively reviewed and accepted as a special release-note page. Its residual English is dominated by release-note feature names, command/config/status literals, and Tractor component names.

## Pages

| Order | Page | Starting Risk | Primary Terms | Notes |
|---:|---|---:|---|---|
| 1 | `RU/628752397-Light Filters.html` | 94/medium -> 2/low | `Light Filter`, `Light Filters` | Completed; normalized page title and explanatory prose around light filters, lights, lighting, gobos/gels/blockers/reflectors, barn/window/bounce lights, physical/analytic modes, rods, blockers, controls, intensity/exposure, assets, linking, ramp/color/intensity, and combined filters while preserving exact `Pxr...LightFilter` node names and useful English filter-type labels. |
| 2 | `RFB27/544638842-Light Filters in Blender.html` | 86/medium -> 2/low | `Light Filter`, `Light Filters` | Completed; normalized Blender page title, intro, creation instructions, object properties panel wording, shortcut/menu prose, filter object/list wording, and filter-type heading while preserving exact `Pxr...LightFilter` node names and useful UI labels such as `Add`. |
| 3 | `RFH27/544641289-Light Filters in Solaris.html` | 73/medium -> 14/low | `Light Filters` | Completed; normalized Solaris page title, intro, light-filter primitive wording, PxrAssign assignment prose, Light Filters parameter text, light primitive/filter primitive descriptions, and child-primitive path instructions while preserving `Light Edit LOP`, `PxrAssign`, `Scene Graph`, `light:filters`, `Base Properties`, and `Primitive Path` labels. |
| 4 | `RFH27/544645033-Light Filters.html` | 66/medium -> 0/low | `Light Filter`, `Light Filters` | Completed; normalized Houdini page title, RenderMan-doc reference, add/set headings, OBJ/TAB menu instructions, transform/parenting prose, translation/scale guidance, and VOP shader assignment wording while preserving `OBJ`, `TAB`, and `VOP` identifiers. |
| 5 | `RFM27/544539452-Prefs - Viewport.html` | 59/medium -> 45/low | `Light Filters` | Completed; normalized the `Light Filters Wire Color` preference text to `灯光滤镜线框颜色` and corrected `Show Command Output` gloss to `显示命令输出`, while leaving broader Viewport/Playblast UI labels intact. |
| 6 | `REN27/542232400-PxrVisualizer.html` | 59/medium -> 26/low | `object space`, `Object space` | Completed; normalized the `["normals"]` style description from object-space prose to `对象空间中渲染法线` while preserving enum names, parameter names, and UI labels. |
| 7 | `RU/384368745-RenderMan CheatSheet.html` | 58/medium -> 46/low | `Light Filters` | Completed; normalized the cheat-sheet table heading from `Light Filters（灯光过滤器）` to `灯光滤镜`, leaving existing node names and table content intact. |
| 8 | `RFM27/544541661-PxrAOVLight in Maya.html` | 56/medium -> 39/low | `Light Filters` | Completed; normalized the `Light Filters and PxrAOVLight` heading and output-AOV sentence to `灯光滤镜`, while preserving `PxrAOVLight`, AOV, and existing light-linking terminology. |
| 9 | `RFK27/546177835-Geometric Settings.html` | 54/medium -> 23/low | `Prototype Attributes`, `user attributes` | Completed; normalized instance/prototype attribute-category prose and the user-attributes reference to `实例属性`, `原型属性`, and `用户属性` while preserving `prmanStatements...` paths and Katana/RfK identifiers. |
| 10 | `REN27/542221833-Stylized Hatching.html` | 51/medium -> 19/low | `object space`, `Object space` | Completed; normalized the remaining NPRPtriplanar object-space sentence to `对象空间中的 P`, while preserving AOV names, enum labels, and stylized-look identifiers. |

## Current Progress

- Updated: 2026-07-01 20:03 CST after completing page 10.
- Reviewed pages: 10 / 10.
- Batch completion: 100.00%.
- Overall unique page review progress is 334 / 816 = 40.93%.
- T1 term-decision progress: 598 / 620 = 96.45%.
- Current risk baseline after Batch 025 completion: 0 high / 1 medium / 814 low pages, excluding the homepage.
- Latest validation baseline: `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages and 67 flagged terms after Batch 025 completion.
- Latest layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser-sampled pages after Batch 025 completion.
- Latest page tag-count validation: `REN27/542221833-Stylized Hatching.html` shows only expected offline theme injection differences (`link` +1, `script` +2).
- Resume from: T1 remaining 22 review-required term decisions or a stricter prose-polish batch for low-risk residual English.

## Acceleration Rules

- Treat `Light Filter(s)` as `灯光滤镜` in prose; preserve exact node names such as `PxrBarnLightFilter`, `PxrCookieLightFilter`, and exact UI labels when directly quoted.
- Treat `object space` as `对象空间` in prose; preserve exact parameter labels only when the page is clearly naming a UI/control value.
- Treat `Prototype Attributes` as `原型属性` and `user attributes` as `用户属性` in prose.
- Continue text-node-only edits and abort if HTML tag fingerprints change.
- After each edited page, run terminology scan, page tag-count validation, and official layout audit.
