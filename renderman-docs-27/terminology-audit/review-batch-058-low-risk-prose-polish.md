# Review Batch 058: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 057. This batch targets example/gallery pages, support/help prose, Blender workspace settings, Katana debug workflow, Solaris render settings, and Cryptomatte reference prose where residual English appears in reader-facing explanations.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, file formats, shader names, project names, acronyms, code identifiers, AOV/LPE terms, artist names, and official scene/asset titles. Translate ordinary prose terms such as toolset, download, digital double, micro displacement, shading/lighting, concept, render/pass/beauty, context/parameter/tooltip, shelf tool, commercial support/forum, output path, pointcloud, token, render options, attribute opinion, display view, user attribute, outliner, sidecar, and metadata when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFM27/544543762-Examples in Maya.html` | 26/low | Translate example-gallery labels and credits such as Download, digital double, micro displacement, shading/lighting, concept, and Coming Soon while preserving scene names and artist names. |
| 2 | `RFB27/544640190-Examples in Blender.html` | 24/low | Align Blender example-gallery terminology with the Maya examples page while preserving scene names, ACES, shader names, and credits. |
| 3 | `RFK27/546177401-PrmanOpDebug.html` | 24/low | Translate Katana debug workflow prose around ops, terminal ops, parameter/attribute tabs, and node usage while preserving Katana/RfK labels. |
| 4 | `RFH27/544642900-Getting Help.html` | 24/low | Translate help/context/parameter/tooltip/shelf-tool/commercial-support/forum prose while preserving support link labels. |
| 5 | `RFB27/544637132-Workspace in Blender.html` | 24/low | Translate workspace/output path/token/pointcloud/version/take/user-token prose while preserving UI labels and path tokens. |
| 6 | `RFH27/544641753-Solaris Render Settings.html` | 23/low | Translate renderer options, attribute opinions, Attribute Block, Display view, and render settings prose while preserving UI labels. |
| 7 | `REN27/542235274-PxrCryptomatte.html` | 23/low | Translate Cryptomatte manifest/sidecar/layer/outliner/user-attribute/levels/accuracy prose while preserving parameter names and format terms. |

## Results

| Order | Page | Result | Notes |
|---:|---|---:|---|
| 1 | `RFM27/544543762-Examples in Maya.html` | 26/low -> 1/low | Completed; aligned example-gallery wording with the Houdini examples page, translating toolset, download labels, digital double, micro displacement, animation, shading/lighting, concept credits, model credits, and coming-soon text while preserving project titles, artist names, studio names, URLs, shader/material labels, ACES, and Stylized Looks. |
| 2 | `RFB27/544640190-Examples in Blender.html` | 24/low -> 6/low | Completed; matched Maya/Houdini example-gallery terminology, normalized displacement, download labels, digital double, micro displacement, animation, shading/lighting, concept credits, model credits, and coming-soon text while preserving project titles, artist names, shader/material labels, and feature labels. |
| 3 | `RFK27/546177401-PrmanOpDebug.html` | 24/low -> 15/low | Completed; reduced ordinary English around node usage and Op wording while preserving Katana concepts and UI labels such as Interactive Render Filters, Implicit Resolvers, Terminal Ops, Parameters Tab, Attributes Tab, and View at Location. |
| 4 | `RFH27/544642900-Getting Help.html` | 24/low -> 0/low | Completed; translated help/context/parameter/tooltip/shelf-tool/commercial-support/forum prose while preserving RenderMan and RenderMan Menu link labels. |
| 5 | `RFB27/544637132-Workspace in Blender.html` | 24/low -> 5/low | Completed; translated workspace/output path/pointcloud/token/user-token prose and avoided over-preserving full English section labels, while retaining necessary UI/path tokens such as Open Workspace, RIB, Beauty, AOV, Take, `<version>`, and `<take>`. |
| 6 | `RFH27/544641753-Solaris Render Settings.html` | 23/low -> 12/low | Completed; translated renderer-option and USD opinion prose while preserving enum/UI values such as Set or Create, Set if Exists, Block, Do Nothing, Display view, RenderMan persp, and Render Settings. |
| 7 | `REN27/542235274-PxrCryptomatte.html` | 23/low -> 11/low | Completed; translated Cryptomatte metadata, user-attribute, level/accuracy, and outliner explanatory prose while preserving parameter names, enum values, format terms, and official names. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 25 flagged terms, and 2885 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` passes 816/816 static pages and 816/816 browser-sampled pages.
