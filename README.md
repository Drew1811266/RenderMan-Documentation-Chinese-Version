# RenderMan 27 中文文档本地化项目

这是一个 RenderMan 27 官方文档的本地中文化与版式复刻项目。项目从 Pixar RenderMan 27 官方文档站点下载 HTML 页面、附件资源和页面元数据，并通过自定义 HTML 翻译管线生成简体中文静态文档。

项目目标不是只翻译正文，而是让中文文档在内容结构、页面层级、导航、版式、资源引用和核心阅读/搜索体验上尽量与官方文档一致；简体中文文本是唯一有意差异。

当前版本：`0.02`

## 当前状态

- 源 HTML 页面：816
- 中文 HTML 页面：816
- 翻译进度：816 / 816 = 100%
- 静态结构审计：816 / 816 通过
- 浏览器视觉抽样：816 / 816 通过
- 待视觉校对页面：0
- 最终版式完成审计：11 / 11 项通过
- 专业术语审查：816 / 816 完成

关键审计结果记录在：

- `renderman-docs-27/final-layout-completion-audit.md`
- `renderman-docs-27/official-layout-page-audit.md`
- `renderman-docs-27/official-layout-alignment.md`
- `renderman-docs-27/translation-progress.md`
- `renderman-docs-27/terminology-audit/completion-audit-summary.md`

## 版本记录

### 0.02

- 完成全量专业术语审查，覆盖 816 个中文页面。
- 根据术语审查结果优化中文表达，减少误译、过度翻译和不必要的英文夹杂。
- 保持官方风格版式、入口页、章节面板、导航、搜索和本地附件路径不变。
- 明确本地 HTTP 预览入口为 `http://127.0.0.1:8765/html-zh/index.html`，避免附件路径断链。

### 0.01

- 完成 RenderMan 27 官方文档的中文静态文档初版。
- 完成官方风格版式复刻、链接重写、离线搜索和初轮版式审计。

## 如何查看

直接打开中文入口页：

```bash
open "renderman-docs-27/html-zh/index.html"
```

也可以启动本地 HTTP 服务查看，推荐用于浏览器验证和资源路径排查：

```bash
python3 -m http.server 8765 --directory renderman-docs-27
```

然后访问：

```text
http://127.0.0.1:8765/html-zh/index.html
```

## 目录结构

```text
.
├── README.md
├── TRANSLATION_PIPELINE.md
├── tools/
│   ├── download_renderman_docs.py
│   ├── translate_html_docs.py
│   ├── precheck_html_translation_phase.py
│   ├── audit_html_translation_phase.py
│   ├── apply_renderman_official_theme.py
│   ├── rewrite_local_confluence_links.py
│   ├── audit_official_layout_alignment.py
│   └── audit_terminology.py
└── renderman-docs-27/
    ├── html/                         # 英文源 HTML
    ├── html-zh/                      # 中文静态文档
    ├── attachments/                  # 图片、GIF、下载附件等资源
    ├── api/                          # 原始页面 API 响应
    ├── source/                       # sitemap 和源 URL 列表
    ├── glossary/                     # RenderMan 术语库
    ├── terminology-audit/            # 专业术语审查计划、批次记录和完成报告
    ├── codex-translations/           # Codex 逐页翻译 JSONL
    ├── codex-translation-packs/      # 翻译批次包
    ├── phases/                       # 阶段应用与审计报告
    ├── manifest.json                 # 页面清单和源站元数据
    ├── final-layout-completion-audit.md
    ├── official-layout-page-audit.md
    ├── official-layout-alignment.md
    └── translation-progress.md
```

## 翻译管线

翻译管线的核心设计是保留 HTML 结构，只替换可见文本节点：

- 不把完整 HTML 交给 AI 直接改写。
- 脚本只提取可见文本节点。
- 标签、属性、图片路径、表格结构、链接、脚本和样式保持原结构。
- `script`、`style`、`pre`、`code`、`kbd`、`samp`、`var`、`svg`、`math` 等区域默认跳过。
- 应用翻译后会比对源文档和目标文档的标签指纹，结构变化会被视为失败。
- 专业术语由 `renderman-docs-27/glossary/renderman_terminology.json` 约束。

更多细节见：

```text
TRANSLATION_PIPELINE.md
```

## 重要命令

查看翻译工具帮助：

```bash
python3 tools/translate_html_docs.py --help
```

运行官方版式对齐审计：

```bash
python3 tools/audit_official_layout_alignment.py
```

检查本地中文页面中是否仍有未重写的 Confluence `/wiki/` 链接：

```bash
rg -n 'src="/wiki/|href="/wiki/' renderman-docs-27/html-zh
```

重新生成或维护官方风格静态外壳时，相关工具包括：

```bash
python3 tools/apply_renderman_official_theme.py
python3 tools/rewrite_local_confluence_links.py
```

## 版式与交互

中文文档已经实现以下官方风格能力：

- RenderMan 27 Docs 顶栏和产品导航。
- 官方风格入口页、章节首页面板和普通文章面包屑。
- 静态左侧章节导航，包含筛选框和当前页高亮。
- 中文离线搜索，覆盖标题、路径和正文索引。
- 桌面与 390px 移动端响应式布局检查。
- 本地附件路径和已下载页面链接重写。
- 下载器元数据在 HTML 中保留，但在阅读版式中隐藏。

## 已知静态差异

本项目是静态 HTML 文档，不运行官方私有的 Refined/Confluence 前端。当前记录的可接受差异包括：

- 官方站点使用动态 Refined/Confluence 页面树；本地文档使用静态清单顺序生成导航。
- 官方搜索是动态站内搜索；本地搜索是离线标题、路径和正文索引搜索。
- 官方首页视频是真实播放器；本地首页视频区使用静态预览复刻。
- `Source:` / `Downloaded:` 元数据保留在 HTML 源码中用于审计，但读者视图中隐藏。

## 版权与使用说明

RenderMan、Pixar 以及官方文档内容归其各自权利方所有。本项目用于本地学习、翻译、审计和阅读体验复刻，不是 Pixar 官方发布物，也不代表 Pixar。

如果官方文档更新，应重新下载源文档、更新术语库，并重新运行翻译和版式审计流程。
