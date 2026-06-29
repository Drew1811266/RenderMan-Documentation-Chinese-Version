#!/usr/bin/env python3
"""Rewrite Confluence-internal links in html-zh for local offline reading."""

from __future__ import annotations

import html
import json
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCROOT = ROOT / "renderman-docs-27"
HTML_ZH = DOCROOT / "html-zh"
MANIFEST = DOCROOT / "manifest.json"
ATTACHMENTS = DOCROOT / "attachments"

SPACE_HOME = {
    "REN27": "REN27/542212097-RenderMan 27 Documentation.html",
    "RFM27": "RFM27/544538625-RenderMan 27 for Maya.html",
    "RFK27": "RFK27/546177025-RenderMan 27 for Katana.html",
    "RFH27": "RFH27/544640331-RenderMan 27 for Houdini.html",
    "RFB27": "RFB27/544636929-RenderMan 27 for Blender.html",
    "TRA": "TRA/22183944-Tractor 2.html",
    "RU": "RU/476283147-RenderMan University Home.html",
}

HREF_RE = re.compile(r"""href=(["'])(/wiki/[^"']+)\1""")
SRC_RE = re.compile(r"""src=(["'])(/wiki/[^"']+)\1""")


def svg_data_uri(mark: str, color: str) -> str:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" '
        'viewBox="0 0 16 16">'
        f'<text x="8" y="12.8" text-anchor="middle" font-size="14" '
        f'font-family="Arial, sans-serif" fill="{color}">{mark}</text>'
        '</svg>'
    )
    return "data:image/svg+xml," + quote(svg, safe="/:;,=%")


EMOTICON_SRC = {
    "check.png": svg_data_uri("✓", "#14853d"),
    "2705.png": svg_data_uri("✓", "#14853d"),
    "error.png": svg_data_uri("×", "#bf1f2f"),
    "cross.png": svg_data_uri("×", "#bf1f2f"),
    "smile.png": svg_data_uri("☺", "#6a6e75"),
}


def load_page_id_map() -> dict[str, str]:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for page in data.get("pages", []):
        rel = str(Path(page["html_path"]).relative_to("html"))
        out[str(page["page_id"])] = rel
    return out


def rel_url(from_file: Path, target: Path) -> str:
    return os.path.relpath(target, start=from_file.parent).replace(os.sep, "/")


def versioned_wiki_url(path: str, query: str, fragment: str) -> str:
    parts = path.split("/")
    space = parts[3] if len(parts) > 3 else ""
    match = re.search(r"(\d+)$", space)
    if match:
        version = match.group(1)
        if len(parts) >= 6 and parts[4] == "pages":
            page_id = parts[5]
            slug = "/".join(parts[6:])
            public_path = f"/space/{space}/{page_id}"
            if slug:
                public_path += "/" + slug
            base = f"https://rmanwiki-{version}.pixar.com{public_path}"
        else:
            base = f"https://rmanwiki-{version}.pixar.com/space/{space}"
    else:
        base = "https://renderman.atlassian.net" + path
    if query:
        base += "?" + query
    if fragment:
        base += "#" + fragment
    return base


def rewrite_href(page_file: Path, href: str, page_id_map: dict[str, str]) -> tuple[str, str]:
    parsed = urlparse(html.unescape(href))
    path = unquote(parsed.path)
    fragment = f"#{parsed.fragment}" if parsed.fragment else ""

    if path.startswith("/wiki/download/attachments/"):
        parts = path.split("/")
        if len(parts) >= 6:
            attachment_id = parts[4]
            filename = unquote("/".join(parts[5:]))
            target = ATTACHMENTS / attachment_id / filename
            if target.exists():
                return rel_url(page_file, target) + fragment, "local_attachment"
        external = "https://renderman.atlassian.net" + parsed.path
        if parsed.query:
            external += "?" + parsed.query
        if parsed.fragment:
            external += "#" + parsed.fragment
        return external, "external_attachment"

    if not path.startswith("/wiki/spaces/"):
        return href, "unchanged"

    parts = path.split("/")
    space = parts[3] if len(parts) > 3 else ""
    if len(parts) >= 6 and parts[4] == "pages":
        page_id = parts[5]
        target_rel = page_id_map.get(page_id)
        if target_rel:
            return rel_url(page_file, HTML_ZH / target_rel) + fragment, "local_page"

    if len(parts) <= 4 or (len(parts) >= 5 and parts[4] == "overview"):
        target_rel = SPACE_HOME.get(space)
        if target_rel:
            return rel_url(page_file, HTML_ZH / target_rel) + fragment, "local_space"

    return versioned_wiki_url(path, parsed.query, parsed.fragment), "external_page"


def rewrite_src(page_file: Path, src: str) -> tuple[str, str]:
    parsed = urlparse(html.unescape(src))
    path = unquote(parsed.path)
    fragment = f"#{parsed.fragment}" if parsed.fragment else ""
    filename = path.rsplit("/", 1)[-1]
    if path.startswith("/wiki/download/attachments/"):
        parts = path.split("/")
        if len(parts) >= 6:
            attachment_id = parts[4]
            attachment_name = unquote("/".join(parts[5:]))
            target = ATTACHMENTS / attachment_id / attachment_name
            if target.exists():
                return rel_url(page_file, target) + fragment, "local_src_attachment"
        external = "https://renderman.atlassian.net" + parsed.path
        if parsed.query:
            external += "?" + parsed.query
        if parsed.fragment:
            external += "#" + parsed.fragment
        return external, "external_src_attachment"
    if "/images/icons/emoticons/" in path and filename in EMOTICON_SRC:
        return EMOTICON_SRC[filename], "local_emoticon"
    return src, "unchanged_src"


def rewrite_file(path: Path, page_id_map: dict[str, str]) -> dict[str, int]:
    text = path.read_text(encoding="utf-8", errors="replace")
    counts = {
        "local_page": 0,
        "local_space": 0,
        "local_attachment": 0,
        "local_src_attachment": 0,
        "local_emoticon": 0,
        "external_page": 0,
        "external_attachment": 0,
        "external_src_attachment": 0,
        "unchanged": 0,
        "unchanged_src": 0,
    }

    def repl(match: re.Match[str]) -> str:
        quote = match.group(1)
        href = match.group(2)
        new_href, kind = rewrite_href(path, href, page_id_map)
        counts[kind] = counts.get(kind, 0) + 1
        if new_href == href:
            return match.group(0)
        return f"href={quote}{html.escape(new_href, quote=True)}{quote}"

    def repl_src(match: re.Match[str]) -> str:
        quote_char = match.group(1)
        src = match.group(2)
        new_src, kind = rewrite_src(path, src)
        counts[kind] = counts.get(kind, 0) + 1
        if new_src == src:
            return match.group(0)
        return f"src={quote_char}{html.escape(new_src, quote=True)}{quote_char}"

    new_text = HREF_RE.sub(repl, text)
    new_text = SRC_RE.sub(repl_src, new_text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return counts


def main() -> None:
    page_id_map = load_page_id_map()
    totals = {
        "files_changed": 0,
        "local_page": 0,
        "local_space": 0,
        "local_attachment": 0,
        "local_src_attachment": 0,
        "local_emoticon": 0,
        "external_page": 0,
        "external_attachment": 0,
        "external_src_attachment": 0,
        "unchanged": 0,
        "unchanged_src": 0,
    }
    for path in sorted(HTML_ZH.rglob("*.html")):
        rel = path.relative_to(HTML_ZH)
        if rel.parts and rel.parts[0] == "assets":
            continue
        before = path.read_text(encoding="utf-8", errors="replace")
        counts = rewrite_file(path, page_id_map)
        after = path.read_text(encoding="utf-8", errors="replace")
        if before != after:
            totals["files_changed"] += 1
        for key, value in counts.items():
            totals[key] += value
    print(json.dumps(totals, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
