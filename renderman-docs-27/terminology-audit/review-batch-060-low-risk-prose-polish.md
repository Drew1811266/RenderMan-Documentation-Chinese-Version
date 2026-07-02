# Review Batch 060: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 059. This batch targets the next highest remaining residual-English pages across Katana release notes, Tractor dashboard links, Linux installation, Solaris Tractor spool settings, RenderMan University HDRI listings, Blender string tokens, and the Houdini RenderMan Shelf page.

Preserve exact product names, DCC names, node names, command/path literals, package names, UI labels where users must match an application, enum/status/button values, token syntax, file names, page titles where they function as linked titles, project/place/resource names, and RenderMan feature names. Translate ordinary prose terms such as live render, node graph, updates, motion blur, installer, server, download, farm, job, panel, key, dispatching tier, metadata, token, current date/time, shelf, shortcuts, render session, parameters, objects, holdout, and setup when they are explanatory rather than exact labels.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFK27/546179753-RenderMan for Katana Release Notes.html` | 30/low | Translate release-note prose around live render, node graph, filters, transforms, edits, updates, interactive motion blur, and rendering while preserving Katana/RfK labels and literal node names. |
| 2 | `TRA/22184282-Dashboard App.html` | 30/low | Translate dashboard navigation link labels where they are reader-facing page titles while preserving Tractor component names. |
| 3 | `REN27/542212252-Installing on Linux.html` | 28/low | Translate Linux installer/license-server/download/support prose while preserving package names, command/path literals, `.rpm`, compiler/library names, and button labels. |
| 4 | `RFH27/544642287-Tractor Spool Panel.html` | 26/low | Translate Tractor Spool Panel explanatory prose around farm/job/pane/panel/threads/user/service keys/env keys/dispatching tier/metadata/commands while preserving true UI labels and command key literals. |
| 5 | `RU/600178689-HDRIs.html` | 26/low | Translate HDRI map/listing labels where they are descriptive while preserving HDRI, project/place/resource names, and library names. |
| 6 | `RFB27/544637295-String Tokens in Blender.html` | 24/low | Translate Blender string-token table prose around tokens, current blend, workspace editor, version/take, date/time, job identifiers, and custom user tokens while preserving token syntax and literal values. |
| 7 | `RFH27/544643009-RenderMan Shelf.html` | 24/low | Translate RenderMan Shelf prose around shelf shortcuts, IPR render sessions, parameters, objects, holdouts, and setup while preserving UI labels, node names, OBJ/VOP, and feature names. |

## Results

| Order | Page | Result | Notes |
|---:|---|---:|---|
| 1 | `RFK27/546179753-RenderMan for Katana Release Notes.html` | 30/low -> 10/low | Completed; translated release-note prose around live render, node graph, filters, transforms, edits, updates, interactive motion blur, and rendering while preserving Katana/RfK labels, `Render node`, `no-op node`, `Merge`, `coordsys`, and `light filter reference`. |
| 2 | `TRA/22184282-Dashboard App.html` | 30/low -> 1/low | Completed; translated dashboard navigation link labels while preserving Tractor component names where useful. |
| 3 | `REN27/542212252-Installing on Linux.html` | 28/low -> 18/low | Completed; translated Linux installer/license-server/download/support prose while preserving package names, command/path literals, `.rpm`, compiler/library names, and button labels. |
| 4 | `RFH27/544642287-Tractor Spool Panel.html` | 26/low -> 18/low | Completed; translated Tractor Spool Panel explanatory prose around farm/job/service keys/env keys/dispatching tier/metadata and commands while preserving true UI labels and command key literals. |
| 5 | `RU/600178689-HDRIs.html` | 26/low -> 24/low | Completed; translated HDRI map/listing descriptors while preserving project/place/resource/library names. |
| 6 | `RFB27/544637295-String Tokens in Blender.html` | 24/low -> 14/low | Completed; translated Blender string-token prose around tokens, current blend file, workspace editor, version/take, date/time, job identifiers, and custom user tokens while preserving token syntax and literal values. |
| 7 | `RFH27/544643009-RenderMan Shelf.html` | 24/low -> 5/low | Completed; translated RenderMan Shelf prose around shelf shortcuts, IPR render sessions, parameters, objects, holdouts, and setup while preserving UI labels, node names, OBJ/VOP, and feature names. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 25 flagged terms, and 2844 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser-sampled pages.
