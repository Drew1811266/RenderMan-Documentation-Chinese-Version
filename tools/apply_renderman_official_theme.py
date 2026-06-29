#!/usr/bin/env python3
"""Apply an official-like RenderMan documentation theme to html-zh.

This does not claim to be Pixar's private Confluence frontend. It recreates the
public RenderMan docs visual shell shown by the official site while preserving
the translated article HTML already generated in html-zh.
"""

from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCROOT = ROOT / "renderman-docs-27"
HTML_ZH = DOCROOT / "html-zh"
ASSETS = HTML_ZH / "assets"
MANIFEST = DOCROOT / "manifest.json"


class ArticleTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_article = False
        self.skip_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "article":
            self.in_article = True
        if self.in_article and tag in {"script", "style"}:
            self.skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if self.in_article and tag in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1
        if tag == "article":
            self.in_article = False

    def handle_data(self, data: str) -> None:
        if self.in_article and not self.skip_depth:
            text = data.strip()
            if text:
                self.parts.append(text)


def article_text(path: Path) -> str:
    if not path.exists():
        return ""
    parser = ArticleTextExtractor()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return re.sub(r"\s+", " ", " ".join(parser.parts)).strip()


CSS = r"""
@import url("https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap");

:root {
  color-scheme: light;
  --25-release-color: #ffff33;
  --26-release-color: #66cdff;
  --current-release-color: var(--26-release-color);
  --rm-white: #fff;
  --rm-blue-default: #0099ff;
  --rm-black: #2f2f2f;
  --rm-grey-900: #2f2f2f;
  --rm-grey-default: #f5f5f5;
  --rm-grey-300: #fafafa;
  --rm-grey-500: #eaeaea;
  --rm-orange: #ff6600;
  --rm-text: #202124;
  --rm-muted: #4f5359;
  --rm-soft: var(--rm-grey-default);
  --rm-border: #dedede;
  --rm-link: var(--rm-blue-default);
  --rm-border-radius: 8px;
  --rm-border-radius-sm: 4px;
  --rm-container: 1182px;
  --rm-content-container: 1214px;
}

* {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  min-height: 100%;
}

body {
  color: var(--rm-text);
  background: #fff;
  font-family: "Open Sans", "Noto Sans SC", "Microsoft YaHei", Arial, sans-serif;
  font-optical-sizing: auto;
  line-height: 1.55;
}

body h1,
body h2,
body h3,
body h4,
body h5,
body h6 {
  font-family: "Open Sans", "Noto Sans SC", "Microsoft YaHei", Arial, sans-serif;
}

body.rm-themed {
  overflow-x: hidden;
}

.rm-site-header {
  background: var(--rm-black);
  color: #fff;
  margin: 0;
  padding: 0;
  border: 0;
}

.rm-header-inner,
.rm-nav-inner,
.rm-home-inner,
.rm-section-inner,
.rm-doc-main {
  width: min(var(--rm-container), calc(100vw - 48px));
  margin: 0 auto;
}

.rm-header-inner {
  min-height: 80px;
  padding: 24px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.rm-logo {
  display: inline-flex;
  align-items: center;
  gap: 0;
  color: #fff;
  text-decoration: none;
  font-family: "Gotham Narrow", "Arial Narrow", "Open Sans", Arial, sans-serif;
  font-weight: 900;
  letter-spacing: 0;
  line-height: 1;
  text-transform: uppercase;
  white-space: nowrap;
}

.rm-logo-mark {
  width: 34px;
  height: 34px;
  display: block;
  flex: 0 0 auto;
  margin-right: 16px;
  color: #fff;
}

.rm-logo-word {
  font-size: 24px;
  font-weight: 900;
}

.rm-logo-word strong {
  color: var(--rm-orange);
  font-weight: 1000;
}

.rm-logo-word span {
  color: #f1f1f1;
  font-weight: 500;
}

.rm-logo-caret {
  width: 0;
  height: 0;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-top: 6px solid #8e8e8e;
  margin-left: -4px;
}

.rm-main-site {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 32px;
  min-width: 96px;
  padding: 6px 20px;
  border: 1px solid #fff;
  border-radius: 4px;
  color: #fff;
  text-decoration: none;
  font-size: 12px;
  font-weight: 600;
  box-shadow: 0 3px 0 0 #fff;
  transition: box-shadow 0.2s, transform 0.2s, color 0.2s, border-color 0.2s;
}

.rm-main-site:hover {
  color: var(--rm-orange);
  border-color: var(--rm-orange);
  box-shadow: 0 6px 0 0 var(--rm-orange);
  transform: translateY(-3px);
}

.rm-product-nav {
  background: #fff;
  border-bottom: 1px solid #ececec;
}

.rm-nav-inner {
  height: 82px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(20px, 3vw, 44px);
  position: relative;
}

.rm-nav-link {
  align-self: stretch;
  display: inline-flex;
  align-items: center;
  color: #4f5359;
  text-decoration: none;
  font-size: 15px;
  border-bottom: 4px solid transparent;
  white-space: nowrap;
  transition: color 0.2s, border-color 0.2s;
}

.rm-nav-link:hover,
.rm-nav-link[aria-current="page"] {
  color: #111;
}

.rm-nav-link[aria-current="page"] {
  border-bottom-color: var(--rm-blue-default);
  font-weight: 700;
}

.rm-nav-search {
  position: absolute;
  right: 0;
  width: 32px;
  height: 32px;
  border: 1px solid var(--rm-grey-900);
  border-radius: 50%;
  background: #fff;
  color: #333;
  display: inline-grid;
  place-items: center;
  cursor: pointer;
  box-shadow: 0 1px 0 0 var(--rm-grey-900);
  transition: box-shadow 0.2s, transform 0.2s, color 0.2s, border-color 0.2s;
}

.rm-nav-search:hover {
  color: var(--rm-blue-default);
  border-color: var(--rm-blue-default);
  box-shadow: 0 3px 0 0 var(--rm-blue-default);
  transform: translateY(-2px);
}

.rm-nav-search::before {
  content: "";
  width: 11px;
  height: 11px;
  border: 1.8px solid currentColor;
  border-radius: 50%;
  transform: translate(-1px, -1px);
}

.rm-nav-search::after {
  content: "";
  width: 8px;
  height: 2px;
  background: currentColor;
  transform: translate(7px, 7px) rotate(-45deg);
  position: absolute;
}

.rm-home main,
.rm-home-page {
  margin: 0;
  padding: 0;
  max-width: none;
  min-height: 0;
  background: #fff;
}

.rm-hero {
  background: var(--rm-soft);
  padding: 86px 0 80px;
}

.rm-home-inner {
  display: grid;
  grid-template-columns: minmax(320px, 0.93fr) minmax(420px, 1fr);
  gap: 58px;
  align-items: center;
}

.rm-hero h1 {
  margin: 0 0 20px;
  font-size: clamp(36px, 3.6vw, 50px);
  line-height: 1.16;
  font-weight: 500;
  letter-spacing: 0;
}

.rm-hero h1 strong {
  color: var(--rm-orange);
  font-weight: 800;
}

.rm-hero p {
  max-width: 610px;
  margin: 0 0 42px;
  color: #333;
  font-size: 22px;
  line-height: 1.42;
}

.rm-home-search {
  position: relative;
  max-width: 590px;
}

.rm-home-search input,
.rm-search-panel input {
  width: 100%;
  height: 46px;
  padding: 0 18px 0 48px;
  border: 1px solid #797979;
  border-radius: 6px;
  background: #fff;
  color: #333;
  font: inherit;
  font-size: 16px;
  box-shadow: 0 4px 0 #2f3033;
}

.rm-home-search::before,
.rm-search-panel .rm-search-field::before {
  content: "";
  position: absolute;
  left: 18px;
  top: 15px;
  width: 12px;
  height: 12px;
  border: 1.6px solid #8d8f94;
  border-radius: 50%;
}

.rm-home-search::after,
.rm-search-panel .rm-search-field::after {
  content: "";
  position: absolute;
  left: 29px;
  top: 28px;
  width: 7px;
  height: 1.6px;
  background: #8d8f94;
  transform: rotate(45deg);
}

.rm-video-card {
  height: 330px;
  border-radius: var(--rm-border-radius-sm);
  overflow: hidden;
  background:
    radial-gradient(circle at 74% 22%, rgba(255, 91, 16, 0.35), transparent 15%),
    radial-gradient(circle at 24% 72%, rgba(0, 164, 255, 0.28), transparent 18%),
    linear-gradient(145deg, #030303, #171717 54%, #050505);
  position: relative;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.35);
}

.rm-video-card::before {
  content: "RENDERMAN";
  position: absolute;
  left: 50%;
  top: 34%;
  transform: translate(-50%, -50%);
  color: #fff;
  font-size: clamp(44px, 5vw, 64px);
  font-weight: 900;
  text-shadow: 3px 2px 0 #00a4ff, -3px -2px 0 #ff5b10;
  letter-spacing: 0;
}

.rm-video-card::after {
  content: "v.27";
  position: absolute;
  left: 50%;
  top: 55%;
  transform: translate(-50%, -50%);
  color: #fff;
  font-size: clamp(42px, 5vw, 58px);
  font-weight: 900;
  text-shadow: 3px 2px 0 #00a4ff, -3px -2px 0 #ff5b10;
}

.rm-video-dots {
  position: absolute;
  right: 22px;
  top: 18px;
  width: 4px;
  height: 24px;
  background: radial-gradient(circle, #fff 2px, transparent 3px) 0 0 / 4px 8px repeat-y;
}

.rm-video-controls {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 42px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 18px;
  background: rgba(0, 0, 0, 0.72);
  color: #fff;
}

.rm-play {
  width: 0;
  height: 0;
  border-top: 9px solid transparent;
  border-bottom: 9px solid transparent;
  border-left: 15px solid #fff;
}

.rm-time {
  font-size: 12px;
  background: #fff;
  color: #111;
  padding: 2px 5px;
  border-radius: 3px;
}

.rm-bar {
  flex: 1;
  height: 5px;
  border-radius: 5px;
  background: linear-gradient(90deg, #fff 0 20%, #333 20%);
}

.rm-started {
  padding: 76px 0 88px;
  background: #fff;
}

.rm-started h2 {
  margin: 0 0 12px;
  font-size: clamp(34px, 3.2vw, 48px);
  font-weight: 500;
  letter-spacing: 0;
}

.rm-started p {
  margin: 0 0 56px;
  font-size: 17px;
  color: #222;
}

.rm-card-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
}

.rm-doc-card {
  min-height: 230px;
  border-radius: var(--rm-border-radius-sm);
  overflow: hidden;
  position: relative;
  color: #fff;
  text-decoration: none;
  background: #111;
  isolation: isolate;
}

.rm-doc-card img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.24s ease;
  z-index: -2;
}

.rm-doc-card::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0.08), rgba(0,0,0,0.62));
  z-index: -1;
}

.rm-doc-card:hover img {
  transform: scale(1.04);
}

.rm-card-title {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 16px;
  font-size: 22px;
  font-weight: 700;
  text-shadow: 0 2px 8px rgba(0,0,0,0.45);
}

.rm-browse {
  padding: 0 0 80px;
  background: #fff;
}

.rm-browse h2 {
  margin: 0 0 22px;
  font-size: 34px;
  font-weight: 500;
}

.rm-browse-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

.rm-browse-card {
  min-height: 118px;
  padding: 20px 22px;
  border: 1px solid #d7d7d7;
  border-radius: var(--rm-border-radius-sm);
  color: #222;
  text-decoration: none;
  background: #fafafa;
}

.rm-browse-card:hover {
  border-color: #a8a8a8;
  background: #fff;
}

.rm-browse-card strong {
  display: block;
  margin-bottom: 8px;
  font-size: 20px;
}

.rm-browse-card span {
  color: #5b5f66;
}

.rm-doc-section-panel {
  background: var(--rm-soft);
  border-bottom: 1px solid #e4e4e4;
  padding: 42px 0;
}

.rm-section-panel-inner {
  width: min(var(--rm-container), calc(100vw - 48px));
  margin: 0 auto;
}

.rm-section-eyebrow {
  margin: 0 0 8px;
  color: #60646b;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.rm-doc-section-panel h1 {
  margin: 0 0 10px;
  font-size: clamp(34px, 3.4vw, 48px);
  line-height: 1.14;
  font-weight: 500;
}

.rm-doc-section-panel p {
  max-width: 780px;
  margin: 0;
  color: #333;
  font-size: 18px;
  line-height: 1.5;
}

.rm-section-cards {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  margin-top: 28px;
}

.rm-section-card {
  min-height: 112px;
  padding: 17px 18px;
  border: 1px solid #d8d8d8;
  border-radius: var(--rm-border-radius-sm);
  color: #24272c;
  background: #fff;
  text-decoration: none;
}

.rm-section-card:hover {
  border-color: #a8a8a8;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
}

.rm-section-card strong {
  display: block;
  margin-bottom: 8px;
  font-size: 17px;
  line-height: 1.25;
}

.rm-section-card span {
  color: #62666d;
  font-size: 13px;
}

.rm-doc-breadcrumb-strip {
  background: #f5f5f5;
  border-bottom: 1px solid #e3e3e3;
}

.rm-doc-breadcrumb-inner {
  width: min(var(--rm-content-container), calc(100vw - 48px));
  margin: 0 auto;
  padding: 16px 24px;
  color: #60646b;
  font-size: 14px;
}

.rm-doc-breadcrumb-inner a {
  color: #333;
  text-decoration: none;
  font-weight: 600;
}

.rm-doc-breadcrumb-inner a:hover {
  text-decoration: underline;
}

.rm-doc-breadcrumb-inner span {
  color: #858a92;
  margin: 0 8px;
}

.rm-doc-layout {
  width: min(var(--rm-content-container), calc(100vw - 48px));
  margin: 0 auto;
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  gap: 24px;
  align-items: start;
}

.rm-doc-page main {
  max-width: var(--rm-content-container);
  margin: 0 auto;
  padding: 32px 24px 84px;
  background: #fff;
  min-height: 70vh;
}

.rm-doc-page .rm-doc-layout main {
  max-width: none;
  width: 100%;
  margin: 0;
  padding-left: 0;
  padding-right: 0;
  min-width: 0;
}

.rm-space-navigation {
  min-width: 0;
  padding-top: 32px;
}

.rm-space-navigation-inner {
  position: sticky;
  top: 18px;
  max-height: calc(100vh - 36px);
  overflow: auto;
  padding: 0 20px 28px 0;
}

.rm-sidebar-kicker {
  margin: 0 0 6px;
  color: #6a6e75;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}

.rm-sidebar-title {
  margin: 0 0 14px;
  color: var(--rm-grey-900);
  font-size: 18px;
  line-height: 1.25;
  font-weight: 700;
}

.rm-sidebar-search {
  display: block;
  position: relative;
  margin-bottom: 14px;
}

.rm-sidebar-search input {
  width: 100%;
  height: 34px;
  padding: 0 11px;
  border: 1px solid #d1d5db;
  border-radius: var(--rm-border-radius-sm);
  background: #fff;
  color: #222;
  font: inherit;
  font-size: 13px;
}

.rm-page-tree {
  margin: 0;
  padding: 0;
  list-style: none;
}

.rm-page-tree li {
  margin: 0 0 2px;
}

.rm-page-node {
  display: block;
  padding: 6px 8px;
  border: 2px solid transparent;
  border-radius: var(--rm-border-radius-sm);
  color: #3f434a;
  text-decoration: none;
  font-size: 13px;
  line-height: 1.35;
}

.rm-page-node:hover,
.rm-page-node:focus {
  color: var(--rm-blue-default);
  outline: none;
}

.rm-page-node[aria-current="page"] {
  border-color: var(--rm-blue-default);
  color: #111;
  font-weight: 700;
}

.rm-page-node.is-hidden {
  display: none;
}

.rm-doc-page main header {
  margin: 0 0 28px;
  padding: 0;
  border-bottom: 0;
}

.rm-doc-page main h1 {
  margin: 0 0 12px;
  font-size: 44px;
  line-height: 1.1;
  font-weight: 700;
  overflow-wrap: anywhere;
  word-break: break-word;
}

.rm-doc-page main h2 {
  margin-top: 34px;
  font-size: 28px;
  font-weight: 500;
}

.rm-doc-page main h3 {
  margin-top: 28px;
  font-size: 22px;
}

.rm-doc-page .source,
.rm-doc-page .meta {
  color: #686d73;
  font-size: 13px;
  word-break: break-word;
}

.rm-doc-page main header .source {
  display: none;
}

.rm-doc-page article img {
  max-width: 100%;
  height: auto;
  border-radius: var(--rm-border-radius-sm);
}

.rm-doc-page article {
  min-width: 0;
  overflow-wrap: anywhere;
}

.rm-doc-page article iframe,
.rm-doc-page article video,
.rm-doc-page article .conf-macro.output-block {
  max-width: 100%;
}

.rm-doc-page article iframe,
.rm-doc-page article video {
  width: 100%;
}

.rm-doc-page article video {
  height: auto;
}

.rm-doc-page article .confluence-embedded-file-wrapper {
  display: block;
  margin: 18px 0;
}

.rm-doc-page article .image-center-wrapper,
.rm-doc-page article img.image-center {
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}

.rm-doc-page article .image-left-wrapper,
.rm-doc-page article img.image-left {
  text-align: left;
  margin-right: auto;
}

.rm-doc-page article .image-right-wrapper,
.rm-doc-page article img.image-right {
  text-align: right;
  margin-left: auto;
}

.rm-doc-page article table {
  width: 100%;
  border-collapse: collapse;
  margin: 18px 0;
  font-size: 14px;
}

.rm-doc-page article th,
.rm-doc-page article td {
  border: 1px solid #d7d7d7;
  padding: 9px 11px;
  vertical-align: top;
}

.rm-doc-page article th {
  background: #f3f3f3;
}

.rm-doc-page pre,
.rm-doc-page code,
.rm-doc-page kbd,
.rm-doc-page samp {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}

.rm-doc-page pre {
  overflow-x: auto;
  max-width: 100%;
  padding: 13px 15px;
  border: 1px solid #d7d7d7;
  border-radius: 4px;
  background: #f5f5f5;
}

.rm-doc-page code {
  border-radius: 3px;
  background: #f1f1f1;
  padding: 0.08em 0.28em;
}

.rm-doc-page .confluence-information-macro,
.rm-doc-page .confluence-information-macro-note,
.rm-doc-page .confluence-information-macro-warning,
.rm-doc-page .confluence-information-macro-tip,
.rm-doc-page .confluence-information-macro-information {
  margin: 18px 0;
  padding: 14px 18px;
  border-left: 4px solid #ffb000;
  background: #fff8e6;
}

.rm-doc-page article > ul.childpages-macro,
.rm-doc-page article ul.childpages-macro,
.rm-doc-page article .content-by-label ul {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin: 24px 0;
  padding: 0;
  list-style: none;
  columns: auto;
}

.rm-doc-page article > ul.childpages-macro li,
.rm-doc-page article ul.childpages-macro li,
.rm-doc-page article .content-by-label li {
  margin: 0;
  break-inside: auto;
}

.rm-doc-page article > ul.childpages-macro a,
.rm-doc-page article ul.childpages-macro a,
.rm-doc-page article .content-by-label a {
  display: block;
  min-height: 72px;
  padding: 15px 16px;
  border: 1px solid #d8d8d8;
  border-radius: 5px;
  background: #fafafa;
  color: #202124;
  text-decoration: none;
  font-weight: 600;
}

.rm-doc-page article > ul.childpages-macro a:hover,
.rm-doc-page article ul.childpages-macro a:hover,
.rm-doc-page article .content-by-label a:hover {
  background: #fff;
  border-color: #aaa;
}

.rm-doc-page article .expand-container {
  margin: 18px 0;
  border: 1px solid #d9d9d9;
  border-radius: 5px;
  background: #fafafa;
}

.rm-doc-page article .expand-control {
  padding: 12px 15px;
  border-bottom: 1px solid #e4e4e4;
  font-weight: 700;
}

.rm-doc-page article .expand-content {
  padding: 14px 15px;
}

.rm-search-panel {
  position: fixed;
  inset: 0;
  z-index: 100;
  display: none;
  background: rgba(0, 0, 0, 0.44);
}

body.rm-search-open .rm-search-panel {
  display: block;
}

.rm-search-box {
  width: min(760px, calc(100vw - 36px));
  max-height: min(720px, calc(100vh - 80px));
  margin: 70px auto;
  padding: 24px;
  border-radius: 6px;
  background: #fff;
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.32);
  overflow: auto;
}

.rm-search-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  margin-bottom: 18px;
}

.rm-search-head strong {
  font-size: 22px;
  font-weight: 600;
}

.rm-search-close {
  width: 34px;
  height: 34px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background: #fff;
  cursor: pointer;
  font-size: 22px;
  line-height: 1;
}

.rm-search-field {
  position: relative;
  margin-bottom: 18px;
}

.rm-search-results {
  display: grid;
  gap: 8px;
}

.rm-search-results a {
  display: block;
  padding: 11px 12px;
  border: 1px solid #e1e1e1;
  border-radius: 4px;
  color: #222;
  text-decoration: none;
}

.rm-search-results a:hover {
  border-color: #bdbdbd;
  background: #f7f7f7;
}

.rm-search-results span {
  display: block;
  color: #70757d;
  font-size: 12px;
  margin-top: 2px;
}

@media (max-width: 980px) {
  .rm-header-inner,
  .rm-nav-inner,
  .rm-home-inner,
  .rm-section-inner,
  .rm-doc-main {
    width: min(100% - 32px, var(--rm-container));
  }

  .rm-home-inner {
    grid-template-columns: 1fr;
  }

  .rm-doc-layout {
    width: min(100% - 32px, var(--rm-content-container));
    grid-template-columns: 1fr;
    gap: 0;
  }

  .rm-space-navigation {
    padding-top: 22px;
  }

  .rm-space-navigation-inner {
    position: static;
    max-height: 360px;
    overflow: auto;
    padding: 0 0 16px;
    border-bottom: 1px solid #e4e4e4;
  }

  .rm-page-tree {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2px 8px;
  }

  .rm-product-nav {
    overflow: hidden;
    contain: paint;
  }

  .rm-nav-inner {
    justify-content: flex-start;
    overflow-x: auto;
    contain: paint;
    gap: 26px;
    padding-right: 54px;
  }

  .rm-nav-search {
    right: 0;
  }

  .rm-card-grid,
  .rm-browse-grid,
  .rm-section-cards {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .rm-header-inner {
    height: 68px;
  }

  .rm-logo-word {
    font-size: 18px;
  }

  .rm-nav-inner {
    height: auto;
    min-height: 72px;
    flex-wrap: wrap;
    align-content: center;
    overflow-x: hidden;
    overflow-y: visible;
    gap: 0 18px;
    padding: 10px 48px 10px 0;
  }

  .rm-nav-link {
    align-self: auto;
    min-height: 32px;
    border-bottom-width: 3px;
    font-size: 13px;
  }

  .rm-nav-search {
    top: 20px;
  }

  .rm-main-site {
    display: none;
  }

  .rm-hero {
    padding: 52px 0 58px;
  }

  .rm-started {
    padding: 52px 0 64px;
  }

  .rm-video-card {
    height: 230px;
  }

  .rm-card-grid,
  .rm-browse-grid,
  .rm-section-cards,
  .rm-page-tree,
  .rm-doc-page article > ul.childpages-macro,
  .rm-doc-page article ul.childpages-macro,
  .rm-doc-page article .content-by-label ul {
    grid-template-columns: 1fr;
  }

  .rm-doc-page main {
    padding: 34px 18px 64px;
  }

  .rm-doc-page article table {
    display: block;
    max-width: 100%;
    overflow-x: auto;
  }

  .rm-doc-page main h1 {
    font-size: 34px;
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

  function currentSpace(rel) {
    if (rel.indexOf("/") === -1) return "";
    return rel.split("/")[0];
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (char) {
      return {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
      }[char];
    });
  }

  function queryTerms(query) {
    var q = query.toLowerCase();
    var terms = [q];
    var hints = [
      ["许可", ["license", "licensing"]],
      ["许可证", ["license", "licensing"]],
      ["安装", ["install", "installation"]],
      ["材质", ["material", "materials"]],
      ["着色", ["shading", "shader"]],
      ["灯光", ["light", "lighting"]],
      ["体积", ["volume", "volumes"]],
      ["几何", ["geometry"]],
      ["渲染", ["render", "rendering"]],
      ["纹理", ["texture", "texturing"]],
      ["相机", ["camera", "cameras"]]
    ];
    hints.forEach(function (hint) {
      if (q.indexOf(hint[0]) !== -1) {
        hint[1].forEach(function (term) {
          if (terms.indexOf(term) === -1) terms.push(term);
        });
      }
    });
    return terms;
  }

  function navItems(prefix) {
    return [
      ["RenderMan", "REN27/542212097-RenderMan 27 Documentation.html", "REN27"],
      ["Maya", "RFM27/544538625-RenderMan 27 for Maya.html", "RFM27"],
      ["Katana", "RFK27/546177025-RenderMan 27 for Katana.html", "RFK27"],
      ["Houdini", "RFH27/544640331-RenderMan 27 for Houdini.html", "RFH27"],
      ["Blender", "RFB27/544636929-RenderMan 27 for Blender.html", "RFB27"],
      ["Tractor", "TRA/22183944-Tractor 2.html", "TRA"],
      ["FAQs", "https://renderman.pixar.com/general-faq", "FAQ"],
      ["RenderMan University", "RU/476283147-RenderMan University Home.html", "RU"]
    ].map(function (item) {
      var href = /^https?:/.test(item[1]) ? item[1] : prefix + item[1];
      return { label: item[0], href: href, space: item[2] };
    });
  }

  function sectionMeta(space) {
    var data = {
      REN27: {
        title: "RenderMan 27",
        desc: "核心渲染器文档，包括安装、几何、材质、灯光、渲染设置、XPU、RIS、工具和发行说明。",
        home: "REN27/542212097-RenderMan 27 Documentation.html"
      },
      RFM27: {
        title: "RenderMan for Maya",
        desc: "面向 Maya 的 RenderMan 工作流，包括安装、场景设置、材质、灯光、AOV、渲染和开发者指南。",
        home: "RFM27/544538625-RenderMan 27 for Maya.html"
      },
      RFK27: {
        title: "RenderMan for Katana",
        desc: "面向 Katana 的 RenderMan 工作流，包括环境配置、场景设置、几何、材质、灯光和渲染。",
        home: "RFK27/546177025-RenderMan 27 for Katana.html"
      },
      RFH27: {
        title: "RenderMan for Houdini",
        desc: "面向 Houdini 与 Solaris 的 RenderMan 工作流，包括 LOP、材质、灯光、AOV、渲染和 Tractor。",
        home: "RFH27/544640331-RenderMan 27 for Houdini.html"
      },
      RFB27: {
        title: "RenderMan for Blender",
        desc: "面向 Blender 的 RenderMan 文档，包括安装、材质、灯光、渲染、AOV、示例和高级配置。",
        home: "RFB27/544636929-RenderMan 27 for Blender.html"
      },
      TRA: {
        title: "Tractor",
        desc: "Tractor 分布式队列系统文档，包括 engine、blade、spool、Dashboard、API、配置和升级。",
        home: "TRA/22183944-Tractor 2.html"
      },
      RU: {
        title: "RenderMan University",
        desc: "RenderMan University 教程与项目资源，包括基础课程、示例场景、项目路径和学习材料。",
        home: "RU/476283147-RenderMan University Home.html"
      }
    };
    return data[space] || null;
  }

  function sectionPages(space) {
    var pages = (window.RM_DOCS_PAGES || []).filter(function (page) {
      return page.space === space;
    });
    var preferred = /(home|documentation|getting started|installation|licensing|scene setup|geometry|materials?|shading|lighting|rendering|examples|release notes|dashboard|configuration)/i;
    var scored = pages.map(function (page) {
      var score = preferred.test(page.title) ? 0 : 1;
      if (/home|documentation/i.test(page.title)) score = -1;
      return { page: page, score: score };
    });
    scored.sort(function (a, b) {
      if (a.score !== b.score) return a.score - b.score;
      return a.page.title.localeCompare(b.page.title, "zh-Hans-u-co-pinyin");
    });
    return scored.slice(0, 8).map(function (item) { return item.page; });
  }

  function injectSectionPanel(prefix, rel) {
    var main = document.querySelector("main");
    if (!main || rel === "index.html" || rel === "") return;
    var space = currentSpace(rel);
    var meta = sectionMeta(space);
    if (!meta) return;
    var isLanding = rel === meta.home || / Home\.html$/.test(rel);
    if (isLanding) {
      var panel = document.createElement("section");
      panel.className = "rm-doc-section-panel";
      var cards = sectionPages(space).map(function (page) {
        return '<a class="rm-section-card" href="' + escapeHtml(prefix + page.path) + '"><strong>' + escapeHtml(page.title) + '</strong><span>' + escapeHtml(page.space) + '</span></a>';
      }).join("");
      panel.innerHTML =
        '<div class="rm-section-panel-inner">' +
        '<p class="rm-section-eyebrow">RenderMan Docs</p>' +
        '<h1>' + escapeHtml(meta.title) + '</h1>' +
        '<p>' + escapeHtml(meta.desc) + '</p>' +
        '<div class="rm-section-cards">' + cards + '</div>' +
        '</div>';
      main.parentNode.insertBefore(panel, main);
      return;
    }
    var strip = document.createElement("div");
    strip.className = "rm-doc-breadcrumb-strip";
    strip.innerHTML =
      '<div class="rm-doc-breadcrumb-inner">' +
      '<a href="' + escapeHtml(prefix + 'index.html') + '">RenderMan 27 Docs</a>' +
      '<span>/</span>' +
      '<a href="' + escapeHtml(prefix + meta.home) + '">' + escapeHtml(meta.title) + '</a>' +
      '</div>';
    main.parentNode.insertBefore(strip, main);
  }

  function buildHeader(prefix, rel) {
    var active = currentSpace(rel);
    var header = document.createElement("div");
    header.innerHTML =
      '<header class="rm-site-header">' +
      '  <div class="rm-header-inner">' +
      '    <a class="rm-logo" href="' + prefix + 'index.html" aria-label="RenderMan 27 Docs">' +
      '      <svg class="rm-logo-mark" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M32 0H0v32h32V0ZM2.284 2.286v27.428h9.812v-7.993h1.598l4.974 7.993h11.045l-6.39-9.717c3.286-1.529 5.477-4.076 5.477-8.033v-.235c0-2.86-1.004-4.937-2.875-6.544-2.145-1.842-5.568-2.9-10.497-2.9H2.284ZM15.291 15.49h-3.195V9.417h3.24c2.146 0 3.56.98 3.56 2.939v.196c0 1.92-1.414 2.938-3.605 2.938Z" clip-rule="evenodd"/></svg>' +
      '      <span class="rm-logo-word">RENDERMAN <strong>27</strong> <span>DOCS</span></span>' +
      '      <span class="rm-logo-caret" aria-hidden="true"></span>' +
      '    </a>' +
      '    <a class="rm-main-site" href="https://renderman.pixar.com/" target="_blank" rel="noreferrer">主站</a>' +
      '  </div>' +
      '</header>' +
      '<nav class="rm-product-nav" aria-label="产品导航">' +
      '  <div class="rm-nav-inner"></div>' +
      '</nav>';
    var nav = header.querySelector(".rm-nav-inner");
    navItems(prefix).forEach(function (item) {
      var a = document.createElement("a");
      a.className = "rm-nav-link";
      a.href = item.href;
      a.textContent = item.label;
      if (active && item.space === active) a.setAttribute("aria-current", "page");
      nav.appendChild(a);
    });
    var button = document.createElement("button");
    button.className = "rm-nav-search";
    button.type = "button";
    button.setAttribute("aria-label", "搜索");
    nav.appendChild(button);
    return header;
  }

  function searchHref(prefix, page) {
    return prefix + page.path;
  }

  function renderResults(container, query, prefix) {
    var pages = window.RM_DOCS_PAGES || [];
    var q = query.trim().toLowerCase();
    var terms = queryTerms(q);
    container.innerHTML = "";
    if (!q) {
      pages.slice(0, 12).forEach(function (page) {
        addResult(container, page, prefix);
      });
      return;
    }
    var matches = [];
    pages.forEach(function (page) {
      var haystack = (page.title + " " + page.space + " " + page.path + " " + (page.search || "")).toLowerCase();
      var matchedTerm = "";
      var firstIndex = -1;
      terms.some(function (term) {
        var index = haystack.indexOf(term);
        if (index !== -1) {
          matchedTerm = term;
          firstIndex = index;
          return true;
        }
        return false;
      });
      if (matchedTerm) {
        var title = page.title.toLowerCase();
        var path = page.path.toLowerCase();
        var score = 10000 + firstIndex;
        terms.forEach(function (term) {
          if (title.indexOf(term) !== -1) score = Math.min(score, 0 + title.indexOf(term));
          if (path.indexOf(term) !== -1) score = Math.min(score, 100 + path.indexOf(term));
        });
        if ((page.excerpt || "").toLowerCase().indexOf(q) !== -1) score = Math.min(score, 500);
        matches.push({ page: page, score: score });
      }
    });
    matches.sort(function (a, b) {
      if (a.score !== b.score) return a.score - b.score;
      return a.page.title.localeCompare(b.page.title, "zh-Hans-u-co-pinyin");
    });
    matches.slice(0, 40).forEach(function (item) {
      addResult(container, item.page, prefix, q);
    });
    if (!matches.length) {
      var empty = document.createElement("div");
      empty.className = "rm-empty-search";
      empty.textContent = "没有匹配的页面";
      container.appendChild(empty);
    }
  }

  function addResult(container, page, prefix, query) {
    var a = document.createElement("a");
    a.href = searchHref(prefix, page);
    var detail = page.space + " / " + page.path;
    if (query && page.excerpt) detail += " · " + page.excerpt;
    a.innerHTML = escapeHtml(page.title) + "<span>" + escapeHtml(detail) + "</span>";
    container.appendChild(a);
  }

  function pagesForSpace(space) {
    return (window.RM_DOCS_PAGES || []).filter(function (page) {
      return page.space === space;
    });
  }

  function buildSpaceNavigation(prefix, rel) {
    var space = currentSpace(rel);
    var meta = sectionMeta(space);
    var pages = pagesForSpace(space);
    if (!space || !meta || !pages.length) return null;
    var aside = document.createElement("aside");
    aside.className = "rm-space-navigation";
    var items = pages.map(function (page) {
      var current = page.path === rel;
      return '<li><a class="rm-page-node" href="' + escapeHtml(prefix + page.path) + '"' +
        (current ? ' aria-current="page"' : '') +
        ' data-title="' + escapeHtml(page.title.toLowerCase()) + '">' +
        escapeHtml(page.title) +
        '</a></li>';
    }).join("");
    aside.innerHTML =
      '<div class="rm-space-navigation-inner">' +
      '<p class="rm-sidebar-kicker">章节导航</p>' +
      '<h2 class="rm-sidebar-title">' + escapeHtml(meta.title) + '</h2>' +
      '<label class="rm-sidebar-search"><input type="search" placeholder="筛选页面" autocomplete="off"></label>' +
      '<ul class="rm-page-tree">' + items + '</ul>' +
      '</div>';
    var filter = aside.querySelector("input");
    filter.addEventListener("input", function () {
      var q = filter.value.trim().toLowerCase();
      aside.querySelectorAll(".rm-page-node").forEach(function (node) {
        node.classList.toggle("is-hidden", q && node.dataset.title.indexOf(q) === -1);
      });
    });
    return aside;
  }

  function sizeSpaceNavigationScroller(scroller) {
    if (!scroller) return;
    var rect = scroller.getBoundingClientRect();
    var available = Math.max(360, window.innerHeight - rect.top - 24);
    scroller.style.maxHeight = Math.round(available) + "px";
  }

  function enhanceDocLayout(prefix, rel) {
    if (rel === "index.html" || rel === "") return;
    var main = document.querySelector("main");
    if (!main || main.closest(".rm-doc-layout")) return;
    var aside = buildSpaceNavigation(prefix, rel);
    if (!aside) return;
    var layout = document.createElement("div");
    layout.className = "rm-doc-layout";
    main.parentNode.insertBefore(layout, main);
    layout.appendChild(aside);
    layout.appendChild(main);
    document.body.classList.add("rm-has-space-navigation");
    var current = aside.querySelector('.rm-page-node[aria-current="page"]');
    var scroller = aside.querySelector(".rm-space-navigation-inner");
    if (current && scroller) {
      window.requestAnimationFrame(function () {
        sizeSpaceNavigationScroller(scroller);
        var scrollerRect = scroller.getBoundingClientRect();
        var currentRect = current.getBoundingClientRect();
        var delta = currentRect.top - scrollerRect.top;
        scroller.scrollTop = Math.max(0, scroller.scrollTop + delta - Math.round(scroller.clientHeight * 0.35));
      });
      window.addEventListener("resize", function () {
        sizeSpaceNavigationScroller(scroller);
      });
    }
  }

  function buildSearchPanel(prefix) {
    var panel = document.createElement("div");
    panel.className = "rm-search-panel";
    panel.innerHTML =
      '<div class="rm-search-box" role="dialog" aria-modal="true" aria-label="搜索文档">' +
      '  <div class="rm-search-head"><strong>搜索 RenderMan 27 文档</strong><button class="rm-search-close" type="button" aria-label="关闭">×</button></div>' +
      '  <label class="rm-search-field"><input type="search" placeholder="搜索..." autocomplete="off"></label>' +
      '  <div class="rm-search-results"></div>' +
      '</div>';
    var input = panel.querySelector("input");
    var results = panel.querySelector(".rm-search-results");
    input.addEventListener("input", function () {
      renderResults(results, input.value, prefix);
    });
    panel.querySelector(".rm-search-close").addEventListener("click", function () {
      document.body.classList.remove("rm-search-open");
    });
    panel.addEventListener("click", function (event) {
      if (event.target === panel) document.body.classList.remove("rm-search-open");
    });
    renderResults(results, "", prefix);
    return panel;
  }

  function wireHomeSearch(prefix) {
    var input = document.querySelector("[data-rm-home-search]");
    if (!input) return;
    input.addEventListener("focus", function () {
      document.body.classList.add("rm-search-open");
      var panelInput = document.querySelector(".rm-search-panel input");
      if (panelInput) {
        panelInput.value = input.value;
        panelInput.dispatchEvent(new Event("input"));
        setTimeout(function () { panelInput.focus(); }, 0);
      }
    });
  }

  function init() {
    if (document.querySelector(".rm-site-header")) return;
    var prefix = rootPrefix();
    var rel = currentRel();
    var isHome = rel === "index.html" || rel === "";
    document.body.classList.add("rm-themed");
    document.body.classList.add(isHome ? "rm-home" : "rm-doc-page");

    var first = document.body.firstChild;
    document.body.insertBefore(buildHeader(prefix, rel), first);
    injectSectionPanel(prefix, rel);
    enhanceDocLayout(prefix, rel);
    document.body.appendChild(buildSearchPanel(prefix));

    var searchButton = document.querySelector(".rm-nav-search");
    searchButton.addEventListener("click", function () {
      document.body.classList.add("rm-search-open");
      var input = document.querySelector(".rm-search-panel input");
      if (input) setTimeout(function () { input.focus(); }, 0);
    });

    wireHomeSearch(prefix);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
""".strip()


NAV_TARGETS = {
    "RenderMan": "REN27/542212097-RenderMan 27 Documentation.html",
    "Maya": "RFM27/544538625-RenderMan 27 for Maya.html",
    "Katana": "RFK27/546177025-RenderMan 27 for Katana.html",
    "Houdini": "RFH27/544640331-RenderMan 27 for Houdini.html",
    "Blender": "RFB27/544636929-RenderMan 27 for Blender.html",
    "Tractor": "TRA/22183944-Tractor 2.html",
    "RenderMan University": "RU/476283147-RenderMan University Home.html",
}

HOME_CARDS = [
    {
        "title": "RenderMan",
        "href": "REN27/542212097-RenderMan 27 Documentation.html",
        "image": "../attachments/544638905/TeapotSign.jpg",
    },
    {
        "title": "Maya",
        "href": "RFM27/544538625-RenderMan 27 for Maya.html",
        "image": "../attachments/544540950/teapot2.jpg",
    },
    {
        "title": "Houdini",
        "href": "RFH27/544640331-RenderMan 27 for Houdini.html",
        "image": "../attachments/600145995/thehunted_header.jpg",
    },
    {
        "title": "Blender",
        "href": "RFB27/544636929-RenderMan 27 for Blender.html",
        "image": "../attachments/544640862/RenderMan_MaterialX_Solaris_chessSet.jpg",
    },
]

BROWSE_CARDS = [
    ("安装与授权", "REN27/542212198-Installation and Licensing.html", "安装 RenderMan、配置许可证和更新现有安装。"),
    ("RenderMan 核心", "REN27/542212097-RenderMan 27 Documentation.html", "浏览 RenderMan 27 的核心功能、材质、灯光和渲染设置。"),
    ("Maya", "RFM27/544538625-RenderMan 27 for Maya.html", "RenderMan for Maya 的安装、场景设置、材质和渲染流程。"),
    ("Houdini", "RFH27/544640331-RenderMan 27 for Houdini.html", "Solaris、LOP、材质、灯光和 Houdini 渲染工作流。"),
    ("Blender", "RFB27/544636929-RenderMan 27 for Blender.html", "RenderMan for Blender 的配置、材质、灯光和示例。"),
    ("Tractor", "TRA/22183944-Tractor 2.html", "Tractor 队列、blade、engine、spool 和管理文档。"),
]


def load_pages() -> list[dict[str, str]]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pages = []
    for page in manifest["pages"]:
        path = page["html_path"]
        if path.startswith("html/"):
            path = path[len("html/") :]
        text = article_text(HTML_ZH / path)
        pages.append({
            "space": page["space_key"],
            "title": page["title"],
            "path": path,
            "search": text,
            "excerpt": text[:220],
        })
    extra = HTML_ZH / "REN27" / "542238759-542238759.html"
    if extra.exists() and not any(page["path"] == "REN27/542238759-542238759.html" for page in pages):
        text = article_text(extra)
        pages.append({
            "space": "REN27",
            "title": "RenderMan 27.0",
            "path": "REN27/542238759-542238759.html",
            "search": text,
            "excerpt": text[:220],
        })
    return pages


def write_assets() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "offline-docs.css").write_text(CSS + "\n", encoding="utf-8")
    (ASSETS / "offline-docs.js").write_text(JS + "\n", encoding="utf-8")
    data = "window.RM_DOCS_PAGES = " + json.dumps(load_pages(), ensure_ascii=False, indent=2) + ";\n"
    (ASSETS / "offline-docs-data.js").write_text(data, encoding="utf-8")


def asset_prefix(path: Path) -> str:
    rel_parent = path.parent.relative_to(HTML_ZH)
    if str(rel_parent) == ".":
        return "assets"
    return "/".join([".."] * len(rel_parent.parts) + ["assets"])


def inject_assets(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = re.sub(r"<html lang=\"[^\"]*\">", '<html lang="zh-CN">', text, count=1)
    text = re.sub(r"<body(?:\s+class=\"[^\"]*\")?>", '<body class="rm-themed rm-doc-page">', text, count=1)
    text = re.sub(
        r"\n\s*<link rel=\"stylesheet\" href=\"[^\"]*/?assets/offline-docs\.css\">\n"
        r"\s*<script src=\"[^\"]*/?assets/offline-docs-data\.js\" defer></script>\n"
        r"\s*<script src=\"[^\"]*/?assets/offline-docs\.js\" defer></script>\n",
        "\n",
        text,
        count=1,
    )
    prefix = asset_prefix(path)
    injection = (
        f'  <link rel="stylesheet" href="{prefix}/offline-docs.css">\n'
        f'  <script src="{prefix}/offline-docs-data.js" defer></script>\n'
        f'  <script src="{prefix}/offline-docs.js" defer></script>\n'
    )
    text = text.replace("</head>", injection + "</head>", 1)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def make_homepage() -> str:
    card_html = []
    for card in HOME_CARDS:
        card_html.append(
            '<a class="rm-doc-card" href="{href}">'
            '<img src="{image}" alt="">'
            '<span class="rm-card-title">{title}</span>'
            "</a>".format(
                href=html.escape(card["href"], quote=True),
                image=html.escape(card["image"], quote=True),
                title=html.escape(card["title"]),
            )
        )
    browse_html = []
    for title, href, desc in BROWSE_CARDS:
        browse_html.append(
            '<a class="rm-browse-card" href="{href}"><strong>{title}</strong><span>{desc}</span></a>'.format(
                href=html.escape(href, quote=True),
                title=html.escape(title),
                desc=html.escape(desc),
            )
        )

    return """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RenderMan 27 中文文档</title>
  <link rel="stylesheet" href="assets/offline-docs.css">
  <script src="assets/offline-docs-data.js" defer></script>
  <script src="assets/offline-docs.js" defer></script>
</head>
<body class="rm-themed rm-home">
<main class="rm-home-page">
  <section class="rm-hero">
    <div class="rm-home-inner">
      <div>
        <h1>欢迎使用 <strong>RenderMan 27</strong><br>文档。</h1>
        <p>搜索 RenderMan 27 文档，查找你正在处理的问题、主题，或者浏览最常用的页面。</p>
        <label class="rm-home-search">
          <input data-rm-home-search type="search" placeholder="搜索..." autocomplete="off">
        </label>
      </div>
      <div class="rm-video-card" aria-label="RenderMan 27 feature reel preview">
        <span class="rm-video-dots"></span>
        <div class="rm-video-controls">
          <span class="rm-play"></span>
          <span class="rm-time">02:29</span>
          <span class="rm-bar"></span>
        </div>
      </div>
    </div>
  </section>
  <section class="rm-started">
    <div class="rm-section-inner">
      <h2>快速开始</h2>
      <p>这里可以找到如何安装、授权以及使用 RenderMan 和 Maya、Houdini、Blender、Katana 等桥接产品的信息。</p>
      <div class="rm-card-grid">
        {cards}
      </div>
    </div>
  </section>
  <section class="rm-browse">
    <div class="rm-section-inner">
      <h2>浏览文档</h2>
      <div class="rm-browse-grid">
        {browse}
      </div>
    </div>
  </section>
</main>
</body>
</html>
""".format(cards="\n        ".join(card_html), browse="\n        ".join(browse_html))


def main() -> int:
    write_assets()
    (HTML_ZH / "index.html").write_text(make_homepage(), encoding="utf-8")
    changed = 0
    for path in sorted(HTML_ZH.rglob("*.html")):
        if path.name == "index.html":
            continue
        if inject_assets(path):
            changed += 1
    print(json.dumps({"article_files_updated": changed, "homepage": str((HTML_ZH / "index.html").relative_to(ROOT))}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
