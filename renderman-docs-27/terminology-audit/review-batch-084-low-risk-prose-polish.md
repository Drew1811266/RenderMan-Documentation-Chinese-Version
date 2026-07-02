# Review Batch 084: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 083. This batch targets Blender nightly/install prose, RenderMan camera and displacement reference prose, selected parameter-reference prose, RenderMan University resource prose, Katana shortcut prose, and Houdini stylized/light-linking prose.

Preserve exact product names, page titles, node names, parameter names, enum names, menu paths, file names, URLs, acronyms, artist names, and project titles. Translate ordinary prose terms such as releases, Start, zoom, dicing, deep EXR, shallow EXR, pattern, Input/Output Parameters, Values, Add, Average, Bold Face, Italicized, Specular, Fuzz, bump normal, downloads, computer desktop, Kickstarter, Fundamentals, Cheatsheet, lights, light filters, example scenes, concept, Models, light linking, shadow linking, and SideFX documentation when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFB27/544640079-GitHub Nightlies.html` | 7/low | Translate GitHub nightly prose around releases and Start while preserving URLs and menu paths. |
| 2 | `REN27/542231837-PxrCamera Advanced.html` | 7/low | Translate camera advanced prose around dicing, zoom, deep EXR, shallow EXR, and masks while preserving RIS/XPU and EXR terms. |
| 3 | `REN27/542223392-PxrDispVectorLayer.html` | 7/low | Translate displacement-layer prose around pattern, Values, operations, and output parameters while preserving exact node/parameter labels. |
| 4 | `REN27/542223338-PxrDispScalarLayer.html` | 7/low | Translate scalar-layer prose around pattern, Value, operations, and output parameters while preserving exact node/parameter labels. |
| 5 | `REN27/542216066-Fuzz Parameters.html` | 7/low | Translate Fuzz parameter prose around Bold Face, Italicized, Specular, cone angle, bump normal, and Fundamentals while preserving parameter labels. |
| 6 | `RU/606339097-Fun Stuff.html` | 6/low | Translate RenderMan University fun-resource prose around downloads and computer desktop while preserving wallpaper title. |
| 7 | `RU/599261185-New to RenderMan-.html` | 6/low | Translate new-user prose around Kickstarters, Fundamentals, Cookies 'n Milk, and Cheatsheet while preserving course titles. |
| 8 | `RFK27/546178425-Shortcuts in Katana.html` | 6/low | Translate Katana shortcut prose around RenderMan lights and light filters while preserving node names. |
| 9 | `RFH27/544646600-Stylized Looks Overview Videos in Houdini.html` | 6/low | Translate Houdini Stylized Looks overview prose around example scenes, concept art, and model credits while preserving artist and project names. |
| 10 | `RFH27/544641475-Light Linking in Solaris.html` | 6/low | Translate Solaris light-linking prose while preserving lightlinker node name and SideFX reference. |

## Results

- `RFB27/544640079-GitHub Nightlies.html`: 7/low -> 5/low. Translated GitHub nightly prose around releases and Start while preserving URLs and menu paths.
- `REN27/542231837-PxrCamera Advanced.html`: 7/low -> 1/low. Translated camera advanced prose around dicing, zoom, deep EXR, shallow EXR, and masks while preserving RIS/XPU and EXR terms.
- `REN27/542223392-PxrDispVectorLayer.html`: 7/low -> 4/low. Translated displacement-layer prose around pattern, Values, operations, and output parameters while preserving exact node/parameter labels.
- `REN27/542223338-PxrDispScalarLayer.html`: 7/low -> 4/low. Translated scalar-layer prose around pattern, Value, operations, and output parameters while preserving exact node/parameter labels.
- `REN27/542216066-Fuzz Parameters.html`: 7/low -> 1/low. Translated Fuzz parameter prose around Bold Face, Italicized, Specular, cone angle, bump normal, and Fundamentals while preserving parameter labels.
- `RU/606339097-Fun Stuff.html`: 6/low -> 0/low. Translated RenderMan University fun-resource prose around downloads and computer desktop while preserving wallpaper title.
- `RU/599261185-New to RenderMan-.html`: 6/low -> 3/low. Translated new-user prose around Kickstarters, Fundamentals, and Cheatsheet while preserving course titles.
- `RFK27/546178425-Shortcuts in Katana.html`: 6/low -> 2/low. Translated Katana shortcut prose around RenderMan lights and light filters while preserving node names.
- `RFH27/544646600-Stylized Looks Overview Videos in Houdini.html`: 6/low -> 3/low. Translated Houdini Stylized Looks overview prose around example scenes, concept art, and model credits while preserving artist and project names.
- `RFH27/544641475-Light Linking in Solaris.html`: 6/low -> 2/low. Translated Solaris light-linking prose while preserving lightlinker node name and SideFX reference.

Batch 084 total progress contribution: 10 / 10 pages complete. Overall terminology review progress is now 743 / 816 = 91.05%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2585 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
