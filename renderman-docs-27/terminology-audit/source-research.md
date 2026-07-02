# Terminology Source Research Notes

Status: initial research pass
Date: 2026-06-30

This file records sources used to recalibrate the RenderMan 27 Chinese terminology review. It is not the final termbase; it is the evidence map for later term decisions.

## Primary RenderMan Sources

| Source | Use in Review |
|---|---|
| https://rmanwiki-27.pixar.com/ | Primary source for RenderMan 27 page titles, product areas, node names, parameter labels, workflows, and official terminology. |
| https://rmanwiki-27.pixar.com/space/REN27/542213836/PxrSurface | Material and shading terminology, especially PxrSurface, lobes, diffuse/specular/glass/SSS/fuzz/clearcoat concepts. |
| https://renderman.pixar.com/tech-specs | Product-level terminology, version/platform names, renderer support terms, XPU/RIS context. |
| https://renderman.pixar.com/fundamentals-materials | Beginner-facing material terminology and readable wording for material/shading concepts. |
| https://renderman.pixar.com/fundamentals-patterns | Beginner-facing pattern terminology and readable wording for pattern/texture/procedural terms. |

## Upstream Standards and Ecosystem Sources

| Source | Use in Review |
|---|---|
| https://open-shading-language.readthedocs.io/en/latest/ | OSL, shader, closure, pattern, attribute, and code-related wording. |
| https://materialx.org/ | MaterialX node/network/graph terms and whether to preserve MaterialX-specific names. |
| https://openusd.org/release/glossary.html | USD, stage, layer, prim, attribute, composition, Hydra, and scene description terms. |
| https://openexr.com/en/latest/ | EXR, OpenEXR, deep image/data/compositing terminology. |
| https://opencolorio.org/ | OCIO/OpenColorIO, color space, config, display/view transform terminology. |
| https://github.com/Psyop/Cryptomatte | Cryptomatte naming, matte/ID/channel terminology, and exact product/project spelling. |

## Domain Decision Notes

### Product and Renderer Names

Preserve exact names:

- RenderMan, Pixar RenderMan, RenderMan 27.
- PRMan, RenderMan RIS, RenderMan XPU, RIS, XPU.
- RenderMan for Maya, RenderMan for Houdini, RenderMan for Katana, RenderMan for Blender.
- RfM, RfH, RfK, RfB.

Preferred prose:

- `XPU` can be explained as `CPU/GPU 混合渲染器`.
- `RIS` normally stays as `RIS`; if needed, explain as RenderMan Integrator System.

### Node, API, and Identifier Names

Preserve exact spellings:

- `Pxr*` nodes such as `PxrSurface`, `PxrDisplace`, `PxrPathTracer`.
- `Rix*`, `Ri*`, RIB syntax, command names, environment variables, attribute names, JSON keys.
- File extensions, path fragments, command-line examples, and code identifiers.

Review risk:

- Page titles and parameter names can remain exact, but their surrounding prose should be Chinese.
- A phrase like `Shadow Mode` is a UI/parameter label when naming a control, but `shadow mode` in prose should not automatically remain English.

### Materials and Shading

Preferred Chinese terms:

- material -> 材质
- shading -> 着色
- shader -> 着色器
- surface -> 表面
- displacement -> 置换
- bump -> 凹凸
- subsurface scattering -> 次表面散射
- lobe -> 波瓣
- diffuse -> 漫反射
- specular -> 镜面反射 / 高光, depending on context
- clearcoat -> 清漆层 / clearcoat, depending on whether it is a UI lobe label or prose concept
- sheen/fuzz -> 绒毛感 / 绒毛, depending on page context

Review risk:

- Existing glossary has many `preserve: true` entries for phrases like `pattern nodes`, `texture nodes`, `procedural noise`, and `User lobe`; these should not be blindly preserved.
- Lobe names in LPE contexts may need exact English labels, but explanatory prose should use `波瓣`.

### Rendering, Outputs, and Sampling

Preferred Chinese terms:

- rendering -> 渲染
- renderer -> 渲染器
- integrator -> 积分器
- path tracer -> 路径追踪器
- path tracing -> 路径追踪
- light transport -> 光传输
- sample -> 采样 / 样本, depending on context
- sample filter -> 采样滤镜
- display filter -> 显示滤镜
- denoiser -> 降噪器
- checkpointing -> 检查点 / 检查点续渲, depending on context

Preferred bilingual/acronym terms:

- AOV -> 任意输出变量（AOV）
- LPE -> 光路表达式（LPE）
- BSDF/BRDF/BxDF -> usually preserve acronym, optionally explain on first use.

### Geometry and Scene Data

Preferred Chinese terms:

- geometry -> 几何体 / 几何
- subdivision surface -> 细分曲面
- curves -> 曲线
- normals -> 法线
- primitive variable / primvar -> 基元变量（primvar）
- instance -> 实例
- prototype -> 原型
- visibility -> 可见性
- trace sets -> 追踪集

Review risk:

- USD-specific terms such as stage, layer, prim, and composition must be checked against OpenUSD usage. Some should be bilingual on first use.

### Color, Images, and Textures

Preferred Chinese terms:

- texture -> 纹理
- pattern -> Pattern 节点 / 图案, depending on RenderMan node-category context.
- procedural -> 程序化
- noise -> 噪声
- color space -> 色彩空间
- color management -> 色彩管理
- OpenColorIO / OCIO -> preserve exact name/acronym.
- OpenEXR / EXR -> preserve exact name/acronym.
- deep data -> 深度数据
- deep compositing -> 深度合成

Review risk:

- `pattern` is context-dependent in RenderMan. When it means the RenderMan node category, `Pattern 节点` may be preferable; when it is ordinary prose, use `图案` or `模式`.

### Stylized Looks and NPR

Preferred Chinese terms:

- stylized -> 风格化
- stylized looks -> 风格化外观
- toon -> 卡通 / Toon, depending on node or effect name.
- hatching -> 排线 / hatching, depending on exact feature name.
- lines -> 线条
- control -> 控制

Review risk:

- Official feature/node names should remain exact, but prose headings like `Stylized Looks in Maya` may need Chinese title plus original English for search.

### DCC Bridge Terms

Preserve:

- Maya, Houdini, Katana, Blender, Solaris.
- Exact menu names, shelf names, node names, panes, and UI labels.

Translate:

- Generic workflow prose: setup, lighting, rendering, material assignment, preferences, examples, release notes, shortcuts.

Review risk:

- Bridge pages often mix UI labels and prose in the same sentence. These pages need context-aware review, not pure dictionary replacement.

### Tractor and Developer Pages

Preserve:

- Tractor, Blade, Engine, Dashboard when used as product/component names.
- API names, Python identifiers, command names, config keys, query examples.

Translate:

- Generic prose such as administration, query, service, scheduling, job, task, command, logging, troubleshooting when not exact labels.

Review risk:

- Developer pages contain legitimate English code-heavy text. The scanner must exempt code/pre/API contexts before flagging under-translation.

## Immediate Next Research Work

- Extract top 200 glossary preserve candidates from `overpreserve-candidates.tsv`.
- For each candidate, assign one of: preserve, translate, bilingual-first-use, context-ui-label, context-title, review-required.
- Build `term-decision-overrides.json` as a non-destructive overlay before editing the original glossary.
- Then run a page-level mixed-language scanner using the overlay.
