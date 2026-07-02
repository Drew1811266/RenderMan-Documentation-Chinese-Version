# Review Batch 063: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 062. This batch targets the next highest remaining residual-English pages across Katana RIB export, RenderMan University tutorial/resource listings, Tractor contents/navigation labels, macOS license-server instructions, and Tractor administration-pane prose.

Preserve exact product/component names, command names, node names, UI command labels, paths, environment-style identifiers, file extensions, app names, and official project/person names. Translate ordinary prose and navigational labels such as scene, node, context menu, debug menu, disk render, live render, option, neon sign maker, blast into pieces, texel density, contents titles, license server, installer, support/resource titles, wallpaper descriptions, toolbar, icon, pane, tab, configuration control, and connected users when they are not exact UI strings.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFK27/628719654-Export to RIB.html` | 20/low | Translate Katana RIB export prose around scene, node, context/debug menus, disk renders, live renders, and options while preserving the exact external-editor command and debug path. |
| 2 | `RU/592216069-Neon Modelling.html` | 20/low | Translate Neon tutorial prose around sign maker, Blast usage, SideFX naming, UV/texel density, and workflow wording while preserving Houdini node names and tool names. |
| 3 | `TRA/22191842-Contents.html` | 20/low | Translate Tractor contents/navigation labels where they are ordinary page titles while preserving component/command names such as tractor-engine and tq. |
| 4 | `REN27/542212592-macOS License Server.html` | 19/low | Translate macOS license-server prose while preserving LicenseApp, paths, button labels, package version placeholders, and script names. |
| 5 | `RU/599654499-MaterialX Lama.html` | 19/low | Translate MaterialX/Lama resource titles and descriptions while preserving Lama, MaterialX, personal names, and official scene/topic names. |
| 6 | `RU/606240829-RenderMan Wallpapers.html` | 19/low | Translate wallpaper resource copy and titles while preserving RenderMan/Pixar and deliberate theme names where needed. |
| 7 | `TRA/22184244-Administration Pane.html` | 19/low | Translate Tractor administration-pane prose around toolbar, icon, pane, tab, configuration control, limit activity, and connected users while preserving UI section labels. |

## Results

- `RFK27/628719654-Export to RIB.html`: 20/low -> 5/low. Translated scene/node/context/debug-menu/disk-render/live-render/option prose while preserving the exact external-editor command and debug option path.
- `RU/592216069-Neon Modelling.html`: 20/low -> 15/low. Translated neon sign maker, Blast splitting, SideFX capitalization, UV/texel-density, and workflow prose while preserving Houdini node/tool names.
- `TRA/22191842-Contents.html`: 20/low -> 6/low. Translated ordinary Tractor contents labels while preserving component names, command names, and recognizable UI/page labels.
- `REN27/542212592-macOS License Server.html`: 19/low -> 4/low. Translated license-server prose while preserving LicenseApp, paths, button labels, placeholders, and script names.
- `RU/599654499-MaterialX Lama.html`: 19/low -> 3/low. Translated Lama/MaterialX resource titles and descriptions while preserving Lama, MaterialX, Rassoul Edji, and Samurai.
- `RU/606240829-RenderMan Wallpapers.html`: 19/low -> 0/low. Translated wallpaper copy and resource titles while preserving Pixar and 3D where appropriate.
- `TRA/22184244-Administration Pane.html`: 19/low -> 5/low. Translated toolbar/icon/pane/tab/configuration/limit/user prose while preserving Administration, Admin, Limit Counters, and User Connections UI labels.

Batch 063 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 587 / 816 = 71.94%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 22 flagged terms, 2798 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
