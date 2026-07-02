# Review Batch 083: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 082. This batch targets installation/licensing prose, RenderMan core reference pages, RenderMan University glass/mentoring prose, and Houdini workflow pages where ordinary English remains in Chinese explanatory text.

Preserve exact product names, command names, file names, environment variables, parameter names, UI labels, node names, page titles, acronyms, and proper nouns. Translate ordinary prose terms such as Installer, Get License, hostname, hostid, Third Party Rendering, RenderMan Software, material, mixed value, map, Points, width, varying float, mentoring sessions, liquid mesh, shader, material, lobe, gain, half, portal lights, domelight, Attributes File, Class, Detail, Value, Bridge, rest, patterns, and Rest node when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `REN27/542212671-Installing for Large Sites.html` | 9/low | Translate installation prose around Installer, Get License, hostname/hostid, and license-server lookup while preserving files, paths, and environment variables. |
| 2 | `REN27/542212198-Installation and Licensing.html` | 9/low | Translate installation/licensing prose around Third Party Rendering, RenderMan Software, and license-server wording while preserving platform/product names. |
| 3 | `REN27/542219300-LamaAdd.html` | 8/low | Translate LamaAdd parameter prose around material, mixed value, and map while preserving parameter labels. |
| 4 | `REN27/542213120-Particles.html` | 8/low | Translate particle prose around Points, width, constant/varying variables, and star-field examples while preserving exact primitive/parameter names. |
| 5 | `RU/622592143-Mentoring Session Archive.html` | 7/low | Translate mentoring-session prose while preserving organization names and session titles. |
| 6 | `RU/612401313-PxrSurface - Glass.html` | 7/low | Translate glass material prose around liquid mesh, shader, material, lobe, gain, and half while preserving PxrSurface parameter names. |
| 7 | `RFH27/567050268-Portal Lights in Solaris.html` | 7/low | Translate Portal Light prose around portal lights, domelight, and setup instructions while preserving LOP/node labels. |
| 8 | `RFH27/544646645-Exporting Ri Attributes.html` | 7/low | Translate Ri attribute export prose around Alembic File, Class, Detail, Value, and Round Curve while preserving exact attribute names. |
| 9 | `RFH27/544645351-Workflows.html` | 7/low | Translate Houdini Bridge/workflow section prose and labels while preserving feature/page titles. |
| 10 | `RFH27/544643704-Setting Pref.html` | 7/low | Translate Pref setup prose around swimming, rest, patterns, and Rest node while preserving Pref/Nref/rnml attribute names. |

## Results

- `REN27/542212671-Installing for Large Sites.html`: 9/low -> 9/low. Translated installation prose around Installer, Get License, hostname, hostid, and localhost while preserving files, paths, and environment variables.
- `REN27/542212198-Installation and Licensing.html`: 9/low -> 9/low. Translated installation/licensing prose around Third Party Rendering, Pixar License Server, and RenderMan Software while preserving platform/product names.
- `REN27/542219300-LamaAdd.html`: 8/low -> 8/low. Translated LamaAdd parameter prose around material, mixed value, and map while preserving parameter labels.
- `REN27/542213120-Particles.html`: 8/low -> 8/low. Translated particle prose around Points, width, constant/varying variables, and star-field examples while preserving exact primitive/parameter names.
- `RU/622592143-Mentoring Session Archive.html`: 7/low -> 7/low. Translated mentoring-session prose while preserving organization names and session titles.
- `RU/612401313-PxrSurface - Glass.html`: 7/low -> 7/low. Translated glass material prose around liquid mesh, shader, material, lobe, and gain while preserving PxrSurface parameter names. The final `half` token is retained because the official source HTML itself ends that sentence at `half`.
- `RFH27/567050268-Portal Lights in Solaris.html`: 7/low -> 7/low. Translated Portal Light prose around portal lights, domelight, and setup instructions while preserving LOP/node labels.
- `RFH27/544646645-Exporting Ri Attributes.html`: 7/low -> 7/low. Translated Ri attribute export prose around Alembic File, Class, Detail, Value, and Round Curve while preserving exact attribute names.
- `RFH27/544645351-Workflows.html`: 7/low -> 7/low. Translated Houdini Bridge/workflow section prose and labels while preserving feature/page titles.
- `RFH27/544643704-Setting Pref.html`: 7/low -> 7/low. Translated Pref setup prose around swimming, patterns, and Rest node while preserving Pref/Nref/rnml/rest attribute names.

Batch 083 total progress contribution: 10 / 10 pages complete. Overall terminology review progress is now 733 / 816 = 89.83%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2595 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
