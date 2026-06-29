#!/usr/bin/env python3
"""Apply an offline documentation shell to the translated RenderMan HTML.

The downloaded pages are Confluence API `body.view` fragments wrapped in a very
small static document. This script keeps the translated article markup intact
and adds a local navigation/search shell around it.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCROOT = ROOT / "renderman-docs-27"
HTML_ZH = DOCROOT / "html-zh"
MANIFEST = DOCROOT / "manifest.json"
ASSETS = HTML_ZH / "assets"


CSS = r"""
:root {
  color-scheme: light;
  --rm-bg: #f4f5f7;
  --rm-panel: #ffffff;
  --rm-border: #d9dde5;
  --rm-text: #172033;
  --rm-muted: #5d6676;
  --rm-link: #0756a5;
  --rm-link-hover: #003e78;
  --rm-sidebar: #f8f9fb;
  --rm-accent: #e62429;
  --rm-code: #f2f4f7;
}

html,
body {
  margin: 0;
  min-height: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", "Microsoft YaHei", sans-serif;
  color: var(--rm-text);
  background: var(--rm-bg);
  line-height: 1.58;
}

body.rm-docs-shell {
  overflow-x: hidden;
}

.rm-topbar {
  position: sticky;
  top: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: 56px;
  padding: 0 20px;
  border-bottom: 1px solid var(--rm-border);
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(12px);
}

.rm-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 220px;
  color: var(--rm-text);
  font-weight: 700;
  text-decoration: none;
}

.rm-brand-mark {
  width: 28px;
  height: 28px;
  display: inline-grid;
  place-items: center;
  border-radius: 6px;
  background: var(--rm-accent);
  color: #fff;
  font-size: 13px;
  letter-spacing: 0;
}

.rm-search {
  position: relative;
  flex: 1;
  max-width: 620px;
}

.rm-search input {
  width: 100%;
  height: 34px;
  box-sizing: border-box;
  padding: 0 12px;
  border: 1px solid var(--rm-border);
  border-radius: 6px;
  color: var(--rm-text);
  background: #fff;
  font: inherit;
}

.rm-search input:focus {
  outline: 2px solid rgba(7, 86, 165, 0.18);
  border-color: var(--rm-link);
}

.rm-top-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-left: auto;
}

.rm-top-actions a,
.rm-mobile-toggle {
  border: 1px solid var(--rm-border);
  border-radius: 6px;
  background: #fff;
  color: var(--rm-text);
  text-decoration: none;
  font: inherit;
  font-size: 13px;
  padding: 6px 10px;
}

.rm-mobile-toggle {
  display: none;
}

.rm-shell-layout {
  display: grid;
  grid-template-columns: 300px minmax(0, 1fr);
  min-height: calc(100vh - 57px);
}

.rm-sidebar {
  position: sticky;
  top: 57px;
  height: calc(100vh - 57px);
  overflow: auto;
  border-right: 1px solid var(--rm-border);
  background: var(--rm-sidebar);
}

.rm-sidebar-inner {
  padding: 16px 12px 28px;
}

.rm-sidebar-title {
  margin: 0 8px 10px;
  color: var(--rm-muted);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.rm-sidebar details {
  border-top: 1px solid #e7eaf0;
  padding: 8px 0;
}

.rm-sidebar summary {
  cursor: pointer;
  padding: 4px 8px;
  color: #253149;
  font-weight: 700;
  list-style-position: outside;
}

.rm-sidebar ul {
  columns: auto;
  margin: 6px 0 0;
  padding: 0;
  list-style: none;
}

.rm-sidebar li {
  margin: 0;
  break-inside: auto;
}

.rm-sidebar a {
  display: block;
  padding: 5px 8px 5px 18px;
  border-radius: 5px;
  color: #334057;
  font-size: 13px;
  line-height: 1.35;
  text-decoration: none;
}

.rm-sidebar a:hover {
  color: var(--rm-link-hover);
  background: #edf3fb;
}

.rm-sidebar a[aria-current="page"] {
  color: var(--rm-link-hover);
  background: #dfeeff;
  font-weight: 700;
}

.rm-content {
  min-width: 0;
  background: var(--rm-bg);
}

.rm-content main {
  max-width: 1120px;
  min-height: calc(100vh - 57px);
  margin: 0 auto;
  padding: 30px 42px 72px;
  box-sizing: border-box;
  background: var(--rm-panel);
  box-shadow: 0 0 0 1px rgba(23, 32, 51, 0.04);
}

.rm-content header {
  margin: 0 0 28px;
  padding: 0 0 18px;
  border-bottom: 1px solid var(--rm-border);
}

.rm-content h1 {
  margin: 0 0 8px;
  font-size: 32px;
  line-height: 1.2;
  letter-spacing: 0;
}

.rm-content h2 {
  margin-top: 34px;
  padding-top: 8px;
  font-size: 24px;
  border-top: 1px solid #edf0f4;
}

.rm-content h3 {
  margin-top: 28px;
  font-size: 20px;
}

.rm-content h4 {
  margin-top: 22px;
  font-size: 16px;
}

.rm-content a {
  color: var(--rm-link);
}

.rm-content a:hover {
  color: var(--rm-link-hover);
}

.rm-content .source,
.rm-content .meta {
  color: var(--rm-muted);
  font-size: 13px;
  word-break: break-all;
}

.rm-content article img {
  max-width: 100%;
  height: auto;
}

.rm-content article table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  overflow-wrap: anywhere;
  font-size: 14px;
}

.rm-content article th,
.rm-content article td {
  border: 1px solid var(--rm-border);
  padding: 8px 10px;
  vertical-align: top;
}

.rm-content article th {
  background: #f3f5f8;
  font-weight: 700;
}

.rm-content pre,
.rm-content code,
.rm-content kbd,
.rm-content samp {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}

.rm-content pre {
  overflow-x: auto;
  padding: 12px 14px;
  border: 1px solid var(--rm-border);
  border-radius: 6px;
  background: var(--rm-code);
}

.rm-content code {
  border-radius: 4px;
  background: var(--rm-code);
  padding: 0.1em 0.3em;
}

.rm-content .confluence-information-macro,
.rm-content .confluence-information-macro-note,
.rm-content .confluence-information-macro-warning,
.rm-content .confluence-information-macro-tip,
.rm-content .confluence-information-macro-information {
  border: 1px solid #f0d9a8;
  border-left: 4px solid #e09b25;
  border-radius: 6px;
  background: #fff8ea;
  padding: 12px 16px;
  margin: 16px 0;
}

.rm-content .childpages-macro,
.rm-content .content-by-label,
.rm-content .expand-container {
  border: 1px solid var(--rm-border);
  border-radius: 6px;
  background: #fbfcfe;
  padding: 12px 14px;
}

.rm-content iframe {
  max-width: 100%;
}

.rm-no-results {
  padding: 12px 8px;
  color: var(--rm-muted);
  font-size: 13px;
}

@media (max-width: 920px) {
  .rm-mobile-toggle {
    display: inline-flex;
  }

  .rm-brand {
    min-width: 0;
  }

  .rm-top-actions a {
    display: none;
  }

  .rm-shell-layout {
    grid-template-columns: 1fr;
  }

  .rm-sidebar {
    position: fixed;
    top: 57px;
    left: 0;
    z-index: 40;
    width: min(86vw, 320px);
    transform: translateX(-100%);
    transition: transform 0.18s ease;
    box-shadow: 6px 0 18px rgba(23, 32, 51, 0.18);
  }

  body.rm-sidebar-open .rm-sidebar {
    transform: translateX(0);
  }

  .rm-content main {
    padding: 24px 18px 56px;
  }
}
""".strip()


JS = r"""
(function () {
  function rootPrefix() {
    var path = decodeURIComponent(window.location.pathname);
    var marker = "/html-zh/";
    var index = path.lastIndexOf(marker);
    if (index === -1) return "";
    var rel = path.slice(index + marker.length);
    var depth = rel.split("/").length - 1;
    return depth > 0 ? "../".repeat(depth) : "";
  }

  function currentRel() {
    var path = decodeURIComponent(window.location.pathname);
    var marker = "/html-zh/";
    var index = path.lastIndexOf(marker);
    return index === -1 ? "index.html" : path.slice(index + marker.length);
  }

  function groupedPages() {
    var groups = {};
    (window.RM_DOCS_PAGES || []).forEach(function (page) {
      if (!groups[page.space]) groups[page.space] = [];
      groups[page.space].push(page);
    });
    Object.keys(groups).forEach(function (space) {
      groups[space].sort(function (a, b) {
        return a.title.localeCompare(b.title, "zh-Hans-u-co-pinyin");
      });
    });
    return groups;
  }

  function buildSidebar(prefix, current) {
    var nav = document.createElement("nav");
    nav.className = "rm-sidebar";
    nav.setAttribute("aria-label", "文档目录");
    var inner = document.createElement("div");
    inner.className = "rm-sidebar-inner";
    var title = document.createElement("p");
    title.className = "rm-sidebar-title";
    title.textContent = "文档目录";
    inner.appendChild(title);

    var groups = groupedPages();
    Object.keys(groups).sort().forEach(function (space) {
      var details = document.createElement("details");
      var shouldOpen = current.indexOf(space + "/") === 0 || current === "index.html";
      if (shouldOpen) details.open = true;
      var summary = document.createElement("summary");
      summary.textContent = space;
      details.appendChild(summary);
      var list = document.createElement("ul");
      groups[space].forEach(function (page) {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = prefix + page.path;
        a.textContent = page.title;
        a.dataset.title = page.title.toLowerCase();
        a.dataset.space = page.space.toLowerCase();
        if (page.path === current) a.setAttribute("aria-current", "page");
        li.appendChild(a);
        list.appendChild(li);
      });
      details.appendChild(list);
      inner.appendChild(details);
    });
    nav.appendChild(inner);
    return nav;
  }

  function filterSidebar(sidebar, query) {
    var q = query.trim().toLowerCase();
    var any = false;
    sidebar.querySelectorAll("details").forEach(function (details) {
      var groupHas = false;
      details.querySelectorAll("li").forEach(function (li) {
        var a = li.querySelector("a");
        var match = !q || a.dataset.title.indexOf(q) !== -1 || a.dataset.space.indexOf(q) !== -1;
        li.hidden = !match;
        groupHas = groupHas || match;
        any = any || match;
      });
      details.hidden = !groupHas;
      if (q && groupHas) details.open = true;
    });
    var empty = sidebar.querySelector(".rm-no-results");
    if (!empty) {
      empty = document.createElement("div");
      empty.className = "rm-no-results";
      empty.textContent = "没有匹配的页面";
      sidebar.querySelector(".rm-sidebar-inner").appendChild(empty);
    }
    empty.hidden = any || !q;
  }

  function init() {
    var main = document.querySelector("main");
    if (!main || document.querySelector(".rm-shell-layout")) return;
    var prefix = rootPrefix();
    var current = currentRel();
    document.body.classList.add("rm-docs-shell");

    var topbar = document.createElement("div");
    topbar.className = "rm-topbar";
    topbar.innerHTML =
      '<button class="rm-mobile-toggle" type="button" aria-label="打开目录">目录</button>' +
      '<a class="rm-brand" href="' + prefix + 'index.html"><span class="rm-brand-mark">RM</span><span>RenderMan 27 中文文档</span></a>' +
      '<label class="rm-search"><input type="search" placeholder="搜索页面" autocomplete="off"></label>' +
      '<div class="rm-top-actions"><a href="https://rmanwiki-27.pixar.com/" target="_blank" rel="noreferrer">官方站点</a></div>';

    var layout = document.createElement("div");
    layout.className = "rm-shell-layout";
    var sidebar = buildSidebar(prefix, current);
    var content = document.createElement("div");
    content.className = "rm-content";

    main.parentNode.insertBefore(topbar, main);
    main.parentNode.insertBefore(layout, main);
    content.appendChild(main);
    layout.appendChild(sidebar);
    layout.appendChild(content);

    var search = topbar.querySelector("input[type='search']");
    search.addEventListener("input", function () {
      filterSidebar(sidebar, search.value);
    });
    topbar.querySelector(".rm-mobile-toggle").addEventListener("click", function () {
      document.body.classList.toggle("rm-sidebar-open");
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
""".strip()


def page_data() -> list[dict[str, str]]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pages = []
    for page in manifest["pages"]:
        html_path = page["html_path"]
        if html_path.startswith("html/"):
            html_path = html_path[len("html/") :]
        pages.append(
            {
                "space": page["space_key"],
                "title": page["title"],
                "path": html_path,
            }
        )
    extra = HTML_ZH / "REN27" / "542238759-542238759.html"
    if extra.exists() and not any(page["path"] == "REN27/542238759-542238759.html" for page in pages):
        pages.append({"space": "REN27", "title": "RenderMan 27.0", "path": "REN27/542238759-542238759.html"})
    return pages


def relative_asset_prefix(html_file: Path) -> str:
    rel_parent = html_file.parent.relative_to(HTML_ZH)
    if str(rel_parent) == ".":
        return "assets"
    return "/".join([".."] * len(rel_parent.parts) + ["assets"])


def ensure_shell_assets() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "offline-docs.css").write_text(CSS + "\n", encoding="utf-8")
    (ASSETS / "offline-docs.js").write_text(JS + "\n", encoding="utf-8")
    data = "window.RM_DOCS_PAGES = " + json.dumps(page_data(), ensure_ascii=False, indent=2) + ";\n"
    (ASSETS / "offline-docs-data.js").write_text(data, encoding="utf-8")


def patch_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = re.sub(r"<html lang=\"[^\"]*\">", '<html lang="zh-CN">', text, count=1)
    if path.name == "index.html":
        text = text.replace('href="html/', 'href="')

    prefix = relative_asset_prefix(path)
    inject = (
        f'  <link rel="stylesheet" href="{prefix}/offline-docs.css">\n'
        f'  <script src="{prefix}/offline-docs-data.js" defer></script>\n'
        f'  <script src="{prefix}/offline-docs.js" defer></script>\n'
    )
    text = re.sub(
        r"\n\s*<link rel=\"stylesheet\" href=\"[^\"]*/offline-docs\.css\">\n"
        r"\s*<script src=\"[^\"]*/offline-docs-data\.js\" defer></script>\n"
        r"\s*<script src=\"[^\"]*/offline-docs\.js\" defer></script>\n",
        "\n",
        text,
        count=1,
    )
    text = text.replace("</head>", inject + "</head>", 1)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> int:
    ensure_shell_assets()
    changed = 0
    for path in sorted(HTML_ZH.rglob("*.html")):
        if patch_html(path):
            changed += 1
    print(json.dumps({"html_files_changed": changed, "assets": str(ASSETS.relative_to(ROOT))}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
