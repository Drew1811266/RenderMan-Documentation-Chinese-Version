# RenderMan 27 中文文档官方版式对齐记录

## 目标

翻译后的 RenderMan 27 文档应与官方 RenderMan 文档在内容结构、页面层级、视觉样式、导航面板、入口页、章节面板、资源引用和核心阅读/搜索体验上保持一致；简体中文文本是唯一有意差异。

## 当前阶段

最终审计：版式对齐长期目标的逐项完成审计，已通过。

- 官方取证：`https://rmanwiki-27.pixar.com/` 和 `https://rmanwiki-27.pixar.com/space/REN27/542212097/RenderMan+27+Documentation` 均返回 `renderman-app-bar`、`/gen/css/site.C8T2LfI6.css`、`/gen/js/site-bundle.C0xn_Q5P.js` 和 Pixar 的公开组件包 `pixar-renderman.umd.cjs`。
- 已对齐公开组件参数：Open Sans 字体栈、官方 `#2F2F2F` 深灰、`#0099FF` 蓝色、`#ff6600` 版本号橙色、1182px 顶栏容器、1214px 文章内容容器、官方 R 标志 SVG、顶部 `Main site` 按钮样式、产品导航蓝色活动下划线、搜索按钮阴影/悬浮样式。
- 已对齐静态入口页：深色 RenderMan 27 Docs 顶栏、白色产品导航、灰色 hero、搜索框、RenderMan v.27 视频预览、Get started 卡片区和 Browse documentation 卡片区。
- 已对齐章节首页面板：产品/章节首页会插入官方风格灰色章节面板和章节卡片；普通文章页保留面包屑条。
- 已对齐文章页导航面板：普通文章页会插入按当前 space 生成的静态左侧导航，包含空间标题、过滤框、当前页高亮和 page-node 风格的蓝色活动边框。
- 已降低旧下载器样式闪烁：`html-zh` 页面现在预置 `rm-themed rm-home` 或 `rm-themed rm-doc-page` body class。
- 已修正文章页顶栏污染：旧下载器的全局 `header` 样式不再影响官方深色顶栏，桌面实测顶栏与产品导航之间无空隙。
- 已增强离线搜索：`offline-docs-data.js` 现在包含中文正文索引和摘要；搜索会同时匹配标题、路径和正文，并对常见中英术语（许可/license、材质/material、体积/volume 等）做轻量扩展和相关性排序。
- 已修正移动端阅读问题：文章页媒体嵌入不会撑出横向滚动；移动端左侧导航改为固定高度可滚动面板，并自动把当前页滚入可见区域。
- 已修正长空间侧栏定位：当前页自动滚动改为基于浏览器实际渲染矩形计算，避免 `RenderMan University` 等长列表页面当前项不可见。
- 已中文化官方外壳 UI：入口页标题、快速开始/浏览文档、搜索占位符、主站按钮、产品导航 aria、章节导航、页面筛选框、搜索弹窗和关闭按钮均为中文；品牌 Logo 中的 `DOCS` 按官方视觉保留。
- 已修正抽样发现的正文残留：`RenderMan University Home` 与 `Official Example Scenes` 中的 “Welcome to” 类残留改为中文，同时保持正文标签结构一致。
- 已建立逐页版式审计：`tools/audit_official_layout_alignment.py` 会输出 `official-layout-page-audit.json` 和 `official-layout-page-audit.md`，记录每页静态结构、主题资源、链接状态、页面类别和浏览器视觉抽样状态。
- 已修正正文内部链接：`tools/rewrite_local_confluence_links.py` 将已下载的 RenderMan 27 页面链接改成本地相对链接，将本地附件下载链接改成本地附件路径，将旧版本文档链接改为官方绝对 URL。当前 `/wiki/` 本地坏链为 0。
- 已修正顶部导航：`FAQs` 不再错误指向 Release Notes，改为 Pixar RenderMan General FAQ；搜索按钮 aria label 改为中文。
- 已隐藏下载器元数据：文章顶部 `Source:` / `Downloaded:` 元数据仍保留在 HTML 中用于审计，但在读者版式中隐藏，不再干扰官方阅读体验。
- 已修正 390px 移动端新增溢出：窄屏产品导航改为紧凑换行；长技术标题（如 `PrmanObjectStatements`）可安全断行。
- 已保留正文结构：中文页只加载共享主题，不改写文章正文 DOM。
- 已扩展 Stage 3d 浏览器抽样：覆盖 `txmake`、Color Management、OpenVDB、Projection Plugins、Integrators、`PxrPathTracer`、Sample and Display Filters、Blender Release Notes、RenderMan University Fundamentals、USD Models 和 Tutorials 等高风险页面；桌面 16 页和 390px 移动端 8 页均通过。
- 已扩展 Stage 3e 浏览器抽样：覆盖 Volumes、Aggregate Volumes、`PxrVolume`、Houdini/Maya 体积页、`PxrRectLight`、`PxrPortalLight`、`PxrRodLightFilter`、Blender Mesh Lights、Blender/Katana/Maya denoiser、Houdini/Katana release notes、Lama Fundamentals、USD Workflows 和 Treasure Denoising；桌面 18 页和 390px 移动端 10 页均通过。
- 已修正深层侧栏可见性：桌面侧栏滚动容器会按当前首屏位置动态收紧高度，再把当前页滚入可见区域，避免 Katana Release Notes、Treasure Denoising 等长列表页面当前项落在首屏下方。
- 已扩展 Stage 3f 浏览器抽样：覆盖 Windows/macOS 安装、许可证服务器、Large Sites、`PxrIntMultLightFilter`、`PxrRampLightFilter`、`PxrGoboLightFilter`、Solaris/Maya Light Filters、`PxrSurface`、`PxrMarschnerHair`、OSL Patterns、`PxrBlend`、Assign materials 和 RenderMan University shading 教程；桌面 20 页和 390px 移动端 10 页均通过。
- 已修正 Confluence 资源源地址：`tools/rewrite_local_confluence_links.py` 现在处理非脚本 `src="/wiki/..."` 资源、附件 `src` 和 Confluence emoticon 图标；OSL Patterns 中的旧 `/wiki/s/.../2705.png` 勾选图标已改为内联 SVG，避免断图。
- 已增强审计覆盖：`tools/audit_official_layout_alignment.py` 现在会捕获非脚本资源 `src` 中残留的 `/wiki/` 地址，并把这类问题列为静态失败。
- 已扩展 Stage 3g 浏览器抽样：覆盖 Diffuse/Specular/Glass/Subsurface 参数页、LamaConductor/LamaDielectric/LamaSheen/LamaSSS、`PxrDisplace`、Nested Dielectrics、Stylized Hatching/Lines、Solaris/Katana/Maya workflow、Maya 安装/OSL/Alembic/Material Layers，以及 RenderMan University 多 iframe 教程页面；桌面 24 页和 390px 移动端 12 页均通过。
- 已扩展 Stage 3h 浏览器抽样：覆盖更新/许可续期、`PxrHairColor`、`PxrTileManifold`、Blender/Houdini/Katana/Maya Preset Browser 和 Examples、Blender/Houdini/Katana DCC workflow、RenderMan University Lama/Patterns/mentor/tutorial 页面，以及 Tractor Dashboard/Job Scripting/spool/Limit/Engine/API 页面；桌面 28 页和 390px 移动端 14 页均通过。
- 已扩展 Stage 3i 浏览器抽样：覆盖 Clear Coat/Iridescence/Single Scatter 参数、LamaLayer、`PxrDirt`、`PxrFlakes`、`PxrWorley`、多种 light reference、Blender/Solaris/Katana/Maya workflow、RenderMan University project/best-practice 页面，以及 Tractor logging/API/engine 页面；桌面 30 页和 390px 移动端 15 页均通过。
- 已扩展 Stage 3j 浏览器抽样：覆盖 `PxrDiskLight`、`PxrEnvDayLight`、`PxrMeshLight`、`PxrDistantLight`、Fuzz/Glow 参数、LamaDiffuse、`PxrMultiTexture`、`PxrUnified`、Blender Render Holdouts、Houdini/Maya shelf 与灯光工作流、Katana Volumes/PrmanGlobalStatements/Stats、University iframe 教程页面，以及 Tractor Directory Mapping/NIMBY/Custom Menu Items/tq Cookbook；桌面 30 页和 390px 移动端 15 页均通过。
- 已扩展 Stage 3k 浏览器抽样：覆盖 Geometry、Curves、`PxrAttribute`、`PxrRandomTextureManifold`、`PxrCamera`、Custom OCIO Config、Blender Trace Sets/Light Linking/Aggregate Volumes/Interactive Rendering、Solaris Mesh Lights/Checkpoint/Cryptomatte/Smoke、Katana Configuring/Custom Ops/XGen/`PxrMatteID`、Maya Geometric Settings/Tilt-Shift/Holdouts/Procedurals、University French Bakery/Dragon Treasure/Best Practices/Texture Randomization/Toy Car/Character Lighting，以及 Tractor RenderMan for Maya/PostgreSQL；桌面 30 页和 390px 移动端 15 页均通过。
- 已扩展 Stage 3l 浏览器抽样：覆盖 RenderMan Home、Subdivision/Implicit/Modeling、LamaEmission/LamaIridescence/Lama Metals、Visibility、`PxrBakeTexture`、`PxrCurvature`、`PxrMatteID`、`PxrTexture`、Blender string tokens/material layering/AOV light、Houdini Solaris/User Attributes/Implicit Surfaces、Katana error/instancing/iframe/checkpoint、Maya image-heavy/iframe/custom nodes/best-practices、University CheatSheet/Studio Lights，以及 Tractor JSON/Checkpoint 代码页面；桌面 33 页和 390px 移动端 18 页均通过。
- 已扩展 Stage 3m 浏览器抽样：覆盖 LamaTranslucent、Presence and Opacity、Stylized AOVs/Gallery、`PxrBlackBody`、`PxrMix`、`PxrRamp`、`PxrRemap`、`PxrRoundCube`、`PxrTee`、Blender Getting Started/Instances/UDIMs/Lighting/Light Linking、Houdini Bokeh/Adding Lights/Checkpoints/Rendering to a Device/Stylized iframe/Examples、Katana Subdivision/User Attributes/`PxrAovLight`/Thread Control/Copper Patina、Maya Instances/Geometric edits/Stylized iframe/Mesh Lights/Baking illumination、University Procedural Ground Dirt/Wooden Floor/What Light When/Lighting Path/Textures，以及 Tractor Configuration/Glossary/Site Status/custom Environment Handler；桌面 40 页和 390px 移动端 21 页均通过。
- 已扩展 Stage 3n 浏览器抽样：覆盖 NURBS/Polygons/Instancing、LamaMix/Lama Glass、`PxrLayeredTexture`、`PxrManifold3D`、`PxrTangentField`、Bokeh、`PxrOcclusion`、Blender Archives/Curves/Subdivision/Displacement/AOV、Houdini LOP/Volumes/OSL/Camera/PDG/Stylized、Katana hdPrman/Procedurals/Signal/Light Arrays/Rendering、Maya string tokens/Archives/ZBrush displacement/Lighting/AOV、University Hunted/Sorindar/Hippie/Path Tracing/Toy Car，以及 Tractor Troubleshooting/Environment Handler/Crews/Login；桌面 42 页和 390px 移动端 22 页均通过。
- 已扩展 Stage 3o 浏览器抽样：覆盖 RenderMan/Particles/Aggregate Volumes/Shading/Pixar Surface Materials、`PxrLayerMixer`、MaterialX Lama/Layering、LamaAdd/Schlick/HairChiang/Surface/Tricolor/LPE/Stylized Looks、Blender Home/UI/Workspace/Light Mixer/Geometry/Quadrics/Procedural/OpenVDB、Houdini Home/Solaris/Geometry/Displacement/Subdivision/Render Geometry/Shading/SOP Volumes/Textures、Katana Home/Installation/Upgrade/PrmanOpDebug/Geometry、Maya Home/UI/Menu/Preferences/Prefs Render、University Textures/Neons/Denoising/Look 2，以及 Tractor Connections/Job List/Job Info/UI Tour；桌面 52 页和 390px 移动端 26 页均通过。
- 已扩展 Stage 3p 浏览器抽样：覆盖 MaterialX、`PxrDisneyBsdf`、Stylized Canvas/Toon/Control/Patterns、`aaOceanPrmanShader`、`PxrAdjustNormal`、`PxrArithmetic`、`PxrBakePointCloud`、`PxrBlenderPrincipledInputs`、`PxrBump` 系列、Blender Particles/Shading/Stylized/Light Filters/Cameras/Rendering/Baking/Integrators/Advanced、Houdini Solaris Preset/Solo/Cameras/Rendering/Denoiser/LPE/Cryptomatte、Katana Aggregate/Polygons/Curves/Primitive Variables、Maya Preferences、University Look/Stylization，以及 Tractor About/Blade List 面板；桌面 56 页和 390px 移动端 28 页均通过。
- 已扩展 Stage 3q 浏览器抽样：覆盖 `PxrColorCorrect`/`PxrColorGrade`/`PxrColorSpace` 等 pattern/reference 尾部页、Houdini Solaris Studio/RfH Classic、Katana displacement/stylized/lighting、Maya geometry/curves/particles/subdivision/OpenVDB/Aggregate Volume、University Look/Samples/Stylization/Procedural Edge/External Learning，以及 Tractor Dashboard Blade/Task/Query/Data Filtering/Engine Metrics/Admin 面板；桌面 62 页和 390px 移动端 31 页均通过。
- 已扩展 Stage 3r 浏览器抽样：覆盖 RenderMan Core 剩余 projection/pattern/camera/rendering/reference 页、Katana Portal/Mesh/Light Filters/Camera/Integrator/XPU/Holdout/Baking/Denoiser/Examples/Export 页，以及 Tractor Limit/Preferences/Admin/RMS/Auth/Search/tractor-blade/Dashboard/Blades 等表格和命令页；桌面 71 页和 390px 移动端 71 页均通过。
- 已扩展 Stage 3s 浏览器抽样：覆盖 Houdini 剩余 geometry/shading/lighting/rendering/workflow/how-to 页面、Maya 剩余 shading/displacement/render settings/rendering/AOV/Cryptomatte/Trace Sets 页面，以及 Tractor 剩余 command/admin/upgrading/system/mobile 页面；桌面 117 页和 390px 移动端 117 页均通过。
- 已扩展 Stage 3t 浏览器抽样：覆盖剩余 121 个 RenderMan University project/tutorial/resource 页面，包括 Hunted、Neon、Learning Paths、HDRI、Lama、Best Practices、Toy Car、Bakery、Dragon、Treasure、RazorBack、Hippie Dragon 等图片密集页面；桌面 121 页和 390px 移动端 121 页均通过。

## 本轮验证

- 中文 HTML 总数：816。
- 正文页与英文源页结构计数比对：815/815 通过；首页按官方入口视觉重建，作为预期差异单独记录。
- 缺少共享主题资源的页面：0。
- 缺少主题 body class 的页面：0。
- 入口页本地链接检查：通过。
- 主题检查：Open Sans、官方色值、官方 R SVG、顶部导航活动态、文章标题规则、入口 hero、静态左侧导航 CSS/JS 均通过。
- 浏览器渲染检查：通过本地 HTTP 预览验证首页、Katana、Houdini、Blender、Tractor、RenderMan University、安装/许可、`PxrLayer`、`Job Author Python API`、`PxrProjector`、`PxrSurface`、`PxrCookieLightFilter`、`Official Example Scenes`；控制台错误 0。
- 搜索交互检查：`许可证`、`材质`、`体积` 查询能命中正文并返回相关官方标题页面；搜索弹窗 display 状态、中文占位符和关闭按钮 aria 均通过。
- 响应式检查：390px 移动视口下首页、Katana、RenderMan University、`PxrLayer`、`Job Author Python API`、`PxrSurface` 均无横向溢出，当前页在移动端导航面板内可见。
- 壳层英文残留检查：针对 `Welcome to`、`Let's get`、`Browse documentation`、`Search...`、`Main site`、`Filter pages`、`Space navigation`、`Product navigation`、`Search documentation`、`aria-label="Close"` 的静态扫描为 0。
- 逐页审计：`official-layout-page-audit.json` 当前记录 816/816 静态通过、816 页浏览器视觉抽样通过、0 页待浏览器/人工视觉校对、0 个未重写 `/wiki/` 本地链接。
- 阶段 3c 浏览器渲染检查：新增验证 Maya Release Notes、Lighting、Rendering、RenderMan for Maya API、Tractor Release Notes、Installing on Linux、`PxrBarnLightFilter`、`PxrLayerSurface`、`PrmanObjectStatements`、Lighting in Solaris；桌面控制台错误 0。
- 阶段 3c 移动端检查：390px 下 Lighting、Rendering、Tractor Release Notes、Installing on Linux、`PxrBarnLightFilter`、`PxrLayerSurface`、`PrmanObjectStatements` 通过；期间发现并修复 `PrmanObjectStatements` 页面由窄屏导航/长标题引起的横向溢出。
- 阶段 3d 浏览器渲染检查：新增验证 `txmake`、Color Management、OpenVDB、Projection Plugins、Integrators、`PxrPathTracer`、Sample and Display Filters、Blender Release Notes、RenderMan Fundamentals、`PxrSurface` Fundamentals、Lighting Fundamentals、USD Models、Tutorials；桌面控制台错误 0，可见下载器元数据 0，未重写 `/wiki/` 链接 0。
- 阶段 3d 移动端检查：390px 下 `txmake`、OpenVDB Implicit Field Plugin、`PxrPathTracer`、Blender/Houdini Sample and Display Filters、`PxrSurface` Fundamentals、Lighting Fundamentals、USD Models 均无横向溢出，当前页在移动端导航面板内可见。
- 阶段 3e 官网对照抽样：官方 `PxrVolume`、`PxrRectLight`、Lama Fundamentals 源 URL 返回 200，并暴露官方 RenderMan 文档外壳信号、Pixar 组件脚本和官方 CSS。
- 阶段 3e 浏览器渲染检查：新增验证 18 个体积/灯光/denoiser/release notes/University 页面；桌面和 390px 移动端均无横向溢出、无可见下载器元数据、无未重写 `/wiki/` 链接、无本地 4xx 资源、无已加载破图，顶部产品导航活动态和当前页侧栏定位通过。
- 阶段 3f 官网对照抽样：官方 Installing on Windows、`PxrMarschnerHair`、OSL Patterns 源 URL 返回 200，并暴露官方产品导航、搜索入口、官方 Refined/Confluence CSS 和页面标题信号。
- 阶段 3f 浏览器渲染检查：新增验证 20 个安装/许可、Light Filter、Shader/Pattern、Maya/Houdini workflow 和 University iframe 教程页面；桌面 20 页和 390px 移动端 10 页均无横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态和当前页侧栏定位通过。Vimeo/Cloudflare iframe 401 属外部服务响应，未影响本地文档壳层和正文布局。
- 阶段 3g 官网对照抽样：官方 Specular Parameters、LamaConductor、Alembic Workflows、R.F. - Getting Started 源 URL 返回 200，并暴露官方产品导航、搜索入口、官方 Refined/Confluence CSS 和页面标题信号。
- 阶段 3g 浏览器渲染检查：新增验证 24 个材质参数、Lama/Stylized、DCC workflow 和 University 多 iframe 页面；桌面 24 页和 390px 移动端 12 页均无横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe 尺寸和 expand 容器布局通过。Vimeo/Cloudflare iframe 401 属外部服务响应，未影响本地文档壳层和正文布局。
- 阶段 3h 官网对照抽样：官方 `PxrHairColor`、Preset Browser in Maya、R.F. - Materials - Lama、Job Scripting 源 URL 返回 200，并暴露官方产品导航、搜索入口、官方 Refined/Confluence CSS 和页面标题信号。
- 阶段 3h 浏览器渲染检查：新增验证 28 个 Preset/Examples、Tractor 管理/API、深层 University 和图片密集 shader 页面；桌面 28 页和 390px 移动端 14 页均无横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe 尺寸和 expand 容器布局通过。Vimeo/Cloudflare iframe 401 属外部服务响应，未影响本地文档壳层和正文布局。
- 阶段 3i 官网对照抽样：官方 `PxrCylinderLight`、Motion Blur in Blender、Best Practices - Milk Bottle、Query Python API 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS、Pixar RenderMan 组件和页面标题信号。
- 阶段 3i 浏览器渲染检查：新增验证 30 个灯光/材质 reference、DCC workflow、深层 University project/best-practice 和 Tractor API/命令页面；桌面 30 页和 390px 移动端 15 页均无横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe 尺寸和 expand 容器布局通过。
- 阶段 3j 官网对照抽样：官方 `PxrDiskLight`、Render Holdouts in Blender、PxrMarschnerHair in Maya、Custom Menu Items 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS、Pixar RenderMan 组件和页面标题信号。
- 阶段 3j 浏览器渲染检查：新增验证 30 个高图量 light reference、shader/texture reference、DCC shelf/workflow、University iframe 教程和 Tractor 代码页面；桌面 30 页和 390px 移动端 15 页均无页面级横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe/expand 容器布局通过。`PxrMultiTexture` 移动端表格内部代码列保留可横向滚动表格行为，页面本身不横向溢出。
- 阶段 3k 官网对照抽样：官方 Curves、Trace Sets Editor、XGen in Katana、PostgreSQL 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS、Pixar RenderMan 组件和页面标题信号。
- 阶段 3k 浏览器渲染检查：新增验证 30 个 Core 几何/曲线/相机/OCIO、DCC 高级 workflow、University 深层 project 和 Tractor 代码页面；桌面 30 页和 390px 移动端 15 页均无页面级横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe/expand 容器布局通过。
- 阶段 3l 官网对照抽样：官方 Subdivision Surfaces、LamaEmission、PxrAOVLight in Blender、PxrSurface in Maya、Checkpoint-Resume and Incremental Processing 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3l 浏览器渲染检查：新增验证 33 个 Core modeling/Lama/pattern reference、DCC workflow、University 表格/代码和 Tractor 代码页面；桌面 33 页和 390px 移动端 18 页均无页面级横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe/expand 容器布局通过。
- 阶段 3m 官网对照抽样：官方 PxrRamp、Lighting in Blender、Bokeh、Copper Patina with Layered Materials、Mesh Lights in Maya、Creating a custom Environment Handler 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3m 浏览器渲染检查：新增验证 40 个 Core pattern/Lama/Stylized reference、DCC workflow、University 图片密集页和 Tractor 表格/代码页面；桌面 40 页和 390px 移动端 21 页均无页面级横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe/expand 容器布局通过。
- 阶段 3n 官网对照抽样：官方 `PxrOcclusion`、Curves in Blender、Stylized Looks in Solaris、Rendering in Katana、Lighting in Maya、Login Management 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3n 浏览器渲染检查：新增验证 42 个 Core geometry/pattern/reference、DCC 高风险页、University 深层项目页和 Tractor 残余页；桌面 42 页和 390px 移动端 22 页均无页面级横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe/expand 容器布局通过。`Toy Car Modeling` 中外部 Vimeo/Cloudflare 401 属外部服务响应，未影响本地文档壳层和正文布局。
- 阶段 3o 官网对照抽样：官方 RenderMan、Pixar Surface Materials、Blender 27 Home、Solaris、Katana 27 Home、Maya 27 Home、Connections 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3o 浏览器渲染检查：新增验证 52 个 Core/MaterialX/Lama/Stylized、Blender/Houdini/Katana/Maya 章节首页与设置页、University 和 Tractor 面板页；桌面 52 页和 390px 移动端 26 页均无页面级横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态通过。普通文章页要求当前页侧栏项在移动端视口内可见；章节首页因官方风格章节面板优先，要求章节面板可见且当前页在导航面板内部可见。
- 阶段 3p 官网对照抽样：官方 MaterialX、`PxrBumpRoughness`、Stylized Looks in Blender、Cryptomatte in Solaris、Primitive Variables in Katana、Prefs - OpenColorIO、About Tractor Pane 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3p 浏览器渲染检查：新增验证 56 个 Core MaterialX/Stylized/Pattern、Blender 尾部页、Houdini Solaris/RfH、Katana 几何表格、Maya 偏好、University 和 Tractor 面板页；桌面 56 页和 390px 移动端 28 页均无页面级横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx 资源、无已加载破图，顶部产品导航活动态和当前页侧栏定位通过。
- 阶段 3q 官网对照抽样：官方 `PxrColorSpace`、`PxrMetallicWorkflow`、Assembly Stage、Shortcuts in Katana、OpenVDB Volumes in Maya、Samples made Simple、Blade Activity Pane 源 URL 返回 200，并在渲染 DOM 中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3q 浏览器渲染检查：新增验证 62 个 RenderMan pattern/reference、Houdini Solaris Studio/RfH、Katana lighting/stylized、Maya geometry/volume、University learning/project 和 Tractor dashboard/admin 面板页；桌面 62 页和 390px 移动端 31 页均无页面级横向溢出、无可见下载器元数据、无未重写相对 `/wiki/` 链接或资源、无本地 4xx/5xx 资源、无已加载破图，顶部产品导航活动态、当前页侧栏定位、iframe/video/expand 容器布局通过。
- 阶段 3r 官网对照抽样：官方 `PxrProjectionLayer`、Shadows、`PxrVCM`、`PxrCryptomatte`、Light Filters in Katana、Interactive Denoiser、`tractor-blade` 源 URL 返回 200，并在渲染 DOM 与资源列表中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3r 浏览器渲染检查：新增验证 71 个 RenderMan Core pattern/camera/rendering/reference、Katana lighting/rendering/output 和 Tractor dashboard/command/admin table 页面；桌面 71 页和 390px 移动端 71 页均无页面级横向溢出、无可见下载器元数据、无未重写本地 `/wiki/` 链接或资源、无本地 4xx/5xx 资源、无已加载破图，顶部产品导航活动态、搜索按钮、当前页侧栏定位、iframe/video/expand 容器布局通过。
- 阶段 3s 官网对照抽样：官方 RenderMan Menu、Fur and Hair in Houdini、Denoiser in Houdini、Export to RIB、RenderMan Render Settings、Using Displacement in Maya、Interactive Rendering in Maya、Cryptomatte in Maya、`tq: Tractor Query tool`、System Requirements 源 URL 返回 200，并在渲染 DOM 与资源列表中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3s 浏览器渲染检查：新增验证 117 个 Houdini/Maya/Tractor 剩余视觉待校对页面；桌面 117 页和 390px 移动端 117 页均无页面级横向溢出、无可见下载器元数据、无未重写本地 `/wiki/` 链接或资源、无本地 4xx/5xx 资源、无已加载破图，顶部产品导航活动态、搜索按钮、当前页侧栏定位、iframe/video/expand 容器布局通过。
- 阶段 3t 官网对照抽样：官方 The Hunted、Start with Words、RenderMan Art Challenge、Resources、Lama Metals、HDR Vault、Texture Basics、Best Practices - PxrSurface、Kaboom Box、PxrSurface - Metallic Workflow、Light Filters、Toy Car Lighting、Bakery Shading、RazorBack Whiptail 源 URL 返回 200，并在渲染 DOM 与资源列表中暴露官方产品导航、搜索控件、官方 Refined/Confluence CSS/JS 和 Pixar RenderMan 组件信号。
- 阶段 3t 浏览器渲染检查：新增验证剩余 121 个 RenderMan University project/tutorial/resource 页面；桌面 121 页和 390px 移动端 121 页均无页面级横向溢出、无可见下载器元数据、无未重写本地 `/wiki/` 链接或资源、无本地 4xx/5xx 资源、无已加载破图，顶部产品导航活动态、搜索按钮、当前页侧栏定位、iframe/video/expand 容器布局通过。检查脚本会先滚动完整页面以触发 lazy-loaded 图片，避免把未触发加载的合法图片误判为破图。
- 最终完成审计：`final-layout-completion-audit.json` 记录 11/11 项要求通过，覆盖源/目标页面、唯一完成路径、JSONL 翻译产物、外部机翻工具引用扫描、逐页静态结构和主题、816 页浏览器视觉证据、本地链接/资源重写、搜索/阅读交互、Stage 3t 剩余 RU 桌面/移动端检查、官方实时渲染抽样和已知离线差异记录。

## 已知差异

- 官方站点是 Refined/Confluence + Pixar Web Components 的动态应用；本地文档是静态 HTML。当前实现复刻公开可观察的视觉外壳和阅读交互，不运行官方私有 Confluence 前端。
- 本地搜索是离线标题/路径/正文索引搜索；官方搜索是动态站内搜索。
- 本地左侧导航来自 sitemap/manifest 的 flat page order；官方站点的左侧导航来自 Confluence/Refined 运行时 page tree。当前静态导航保留空间级浏览、过滤和当前页高亮，但不能保证完全相同的树状折叠层级。
- 首页视频区是静态预览复刻；官方站点使用真实视频播放器。
- 下载器的 `Source:` / `Downloaded:` 元数据仍在 HTML 源码中，但已在渲染版式中隐藏；这是为了保留审计可追溯性。
- 部分 University/Shader 页面保留官方内容中的外部 Vimeo iframe；浏览器自动化环境可能收到 Vimeo/Cloudflare 401，但本地 HTML 保留 iframe 布局，外部服务响应不计为本地版式差异。
- 当前已完成 816 页逐页静态审计、816 页浏览器视觉抽样和最终逐项完成审计。

## 下一阶段

无剩余版式对齐阶段；后续只在官方源站变化或用户复查反馈指出具体不一致时继续维护。

- 入口页：首页 hero、导航、卡片区继续与官方截图做人工视觉比对。
- 产品首页：已抽样 Maya、Katana、Houdini、Blender、Tractor、RenderMan University；FAQ 顶部链接已修正为官方外链。
- 普通文章页：816 页已完成静态审计和浏览器视觉抽样；最终审计已确认这些证据覆盖长期目标的显式要求。
- 左侧导航：长空间列表、当前页高亮、过滤框、移动端滚动布局已抽样，仍需跨 space 复查。
- 针对人工反馈继续修正静态主题。
