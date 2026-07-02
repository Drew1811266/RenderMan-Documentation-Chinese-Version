# Review Batch 057: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02
Completed: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 056. This batch targets content-heavy RenderMan/Houdini workflow and node-reference pages where residual English appears in explanatory prose, not only in command/API/UI literal lists.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, attribute names, file formats, shader names, project names, acronyms, code identifiers, AOV/LPE terms, and artist names. Translate ordinary prose terms such as user attribute, attribute, label, tag, parameter, shading rate, primitive variables, custom data, variation, attributes, shading, dicing, motion blur, velocity/acceleration blur, transform motion blur, pattern/index/input/transform/user attribute, aggregate-volume memberships/subsets, procedural, mipmapping, texel, pyro/volume/lookdev, shading network, and browser video text when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFH27/544643715-User Attributes.html` | 28/low | Translate user-attribute, label, tag, attribute, Tag Value, and parameter prose while preserving Houdini UI labels and `ri_user_` prefix. |
| 2 | `REN27/542212781-Geometry.html` | 28/low | Add Chinese explanations for Micropolygonlength and shading-rate prose while preserving `dice`, `micropolygonlength`, and PrimVars identifiers. |
| 3 | `RFH27/544643750-Using Primvars and Attributes.html` | 27/low | Translate primitive-variable/custom-data/variation/attribute/shading/dicing prose while preserving `primvars`, SOP/OBJ, and `user`/`rman` labels. |
| 4 | `RFH27/544641996-Motion Blur in Solaris.html` | 27/low | Translate motion-blur, velocity/acceleration/transform blur, setting, and attribute prose while preserving Solaris UI labels. |
| 5 | `REN27/542224974-PxrSwitch.html` | 27/low | Translate pattern/index/input/attribute/user-attribute/data-type prose while preserving parameter names and color/input labels. |
| 6 | `REN27/542213347-Aggregate Volumes.html` | 24/low | Translate procedural/membership/subset/mipmapping/texel/filterwidth prose while preserving tool, plugin, and parameter identifiers. |
| 7 | `RFH27/544646763-Kaboom Box HDA.html` | 22/low | Translate pyro/volume/lookdev/shading-network/video prose while preserving Kaboom Box HDA, PxrVolume, and artist credit. |

## Results

- Updated visible article text nodes/fragments across 7 pages; HTML tag fingerprints were preserved during every write.
- `RFH27/544643715-User Attributes.html`: 28/low -> 15/low. Cleaned user-attribute, Tag Value, label, tags, RenderMan attribute, and parameter prose while preserving Houdini UI labels and `ri_user_` prefix.
- `REN27/542212781-Geometry.html`: 28/low -> 7/low. Cleaned repeated micropolygonlength and shading-rate prose, translated formula examples and explanatory paragraphs, and preserved code/attribute identifiers where needed.
- `RFH27/544643750-Using Primvars and Attributes.html`: 27/low -> 9/low. Cleaned primitive-variable, custom-data, variation, Houdini attribute, shading/dicing/displacement, detail-attribute, and instance-attribute prose while preserving `primvars`, SOP/OBJ, and table labels.
- `RFH27/544641996-Motion Blur in Solaris.html`: 27/low -> 20/low. Cleaned motion-blur, Velocity Blur setting, velocities/accelerations attribute prose while preserving Solaris UI labels and LOP node names.
- `REN27/542224974-PxrSwitch.html`: 27/low -> 4/low. Cleaned Pattern/index/input/attribute/user-attribute/data-type prose while preserving PxrSwitch parameter names and color/input labels.
- `REN27/542213347-Aggregate Volumes.html`: 24/low -> 23/low. Cleaned procedural, trace memberships/ray subsets, mipmapping, texel, filterWidth/filterwidth, mipmapped-grid, and vdbmake prose while preserving exact identifiers and Luca credits.
- `RFH27/544646763-Kaboom Box HDA.html`: 22/low -> 6/low. Cleaned pyro, volume, lookdev, PxrVolume shading-network, and HTML5 video prose while preserving Kaboom Box HDA and artist credit.

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` passed: 0 high / 1 medium / 814 low pages, 26 flagged terms, 2891 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` passed: 816/816 static pages and 816/816 browser-sampled pages.
