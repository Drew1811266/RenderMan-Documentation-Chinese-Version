# Review Batch 062: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 061. This batch targets the next highest remaining residual-English pages across Solaris/MaterialX workflow notes, Katana environment and upgrade guidance, RenderMan node references, Blender quadric primitives, and Blender bug-reporting workflow.

Preserve exact product names, bridge names, node names, parameter names, enum values, file extensions, environment variables, command/path literals, UI labels that users must match in DCC applications, and official feature names. Translate ordinary prose terms such as artists, studios, workflows, shading nodes, materials, shading network, geometry, limitations, output port, naming convention, upgrading materials, patterns, placement, bump mapping, derivatives, ramp, knot, contribution, multiplier, primitive, viewport, debug logging, render properties, and file packaging when they are explanatory wording rather than exact UI/identifier text.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFH27/544640862-Solaris & MaterialX.html` | 21/low | Translate Solaris/MaterialX explanatory prose around artists/studios, workflows, shading nodes, materials, networks, geometry, and limitations while preserving MaterialX, Solaris, XPU, node names, and MaterialX Subnets. |
| 2 | `RFK27/546177126-Environment Variables in Katana.html` | 21/low | Translate Katana environment variable prose and table headings while preserving env vars, Args, shader paths, plugin labels, and configuration names. |
| 3 | `RFK27/546177369-Upgrading scenes from RenderMan 24 to 27.html` | 21/low | Translate upgrade prose around output-port conventions, DCCs, parameters, shelf update workflow, materials, and op behavior while preserving code identifiers, option strings, and UI command names. |
| 4 | `REN27/542222866-PxrBumpManifold2D.html` | 20/low | Translate PxrBumpManifold2D prose around patterns, placement, bump mapping, derivatives, rotation angle, frequency, offset, manifold, and float result while preserving parameter labels and primvar names. |
| 5 | `REN27/542229544-PxrRampLightFilter.html` | 20/low | Translate PxrRampLightFilter explanatory prose around ramp behavior, knots, interpolation type, diffuse/specular contribution, multiplier, and combine mode while preserving parameter labels and enum values. |
| 6 | `RFB27/544637617-Quadrics in Blender.html` | 20/low | Translate Blender quadric primitive prose while preserving the Add menu label and object names when they are UI labels. |
| 7 | `RFB27/544640138-Reporting Bugs.html` | 20/low | Translate bug-reporting prose around support, reproduction, debug logs, render properties, viewport, utilities, and packaging while preserving UI labels and file extensions. |

## Results

- `RFH27/544640862-Solaris & MaterialX.html`: 21/low -> 1/low. Translated Solaris/MaterialX explanatory prose around artists, studios, workflows, shading nodes, materials, geometry assignment, and limitations while preserving product/node names and MaterialX Subnets.
- `RFK27/546177126-Environment Variables in Katana.html`: 21/low -> 6/low. Translated environment-variable headings and shader-discovery prose while preserving env vars, Args, OSL, C++ plugin labeling, and configuration paths.
- `RFK27/546177369-Upgrading scenes from RenderMan 24 to 27.html`: 21/low -> 3/low. Translated output-port, DCC, parameter-default, shelf, material-upgrade, and op prose while preserving exact code identifiers and the shelf command label.
- `REN27/542222866-PxrBumpManifold2D.html`: 20/low -> 6/low. Translated pattern/placement/bump/derivative/manifold prose while preserving parameter labels, primvar names, and float/result identifiers.
- `REN27/542229544-PxrRampLightFilter.html`: 20/low -> 3/low. Translated ramp, knot, interpolation, diffuse/specular contribution, multiplier, and combine-mode prose while preserving parameter labels and enum values.
- `RFB27/544637617-Quadrics in Blender.html`: 20/low -> 12/low. Translated quadric primitive prose while preserving Add menu and object/UI labels.
- `RFB27/544640138-Reporting Bugs.html`: 20/low -> 11/low. Translated support/debug/package-scene prose while preserving UI labels, file extensions, and RenderMan texture naming.

Batch 062 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 580 / 816 = 71.08%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 22 flagged terms, 2819 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
