#!/usr/bin/env python3
"""
Download the public RenderMan 27 documentation from rmanwiki-27.pixar.com.

The source site is a JavaScript app backed by Confluence REST APIs. This script
uses the public sitemap to enumerate pages, downloads rendered page bodies via
the official API, rewrites common page and attachment links for offline use, and
stores the raw API responses alongside generated HTML.
"""

from __future__ import annotations

import argparse
import html
import http.client
import json
import os
import posixpath
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SOURCE = "https://rmanwiki-27.pixar.com"
SITEMAP = f"{SOURCE}/sitemap.xml"
USER_AGENT = "RenderManDocsDownloader/1.0 (+local archival use)"
CHUNK_SIZE = 1024 * 1024


@dataclass(frozen=True)
class PageRef:
    source_url: str
    space_key: str
    page_id: str
    slug: str


def request_bytes(url: str, *, tries: int = 5, sleep: float = 0.4) -> bytes:
    last_error: Exception | None = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=90) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 429:
                delay = int(exc.headers.get("Retry-After", "20"))
            elif 500 <= exc.code <= 599:
                delay = sleep * (2**attempt)
            else:
                raise
        except (urllib.error.URLError, TimeoutError, http.client.IncompleteRead, ConnectionResetError) as exc:
            last_error = exc
            delay = sleep * (2**attempt)
        time.sleep(delay)
    raise RuntimeError(f"failed to download {url}: {last_error}")


def expected_download_size(response: http.client.HTTPResponse, offset: int) -> int | None:
    content_range = response.headers.get("Content-Range")
    if content_range:
        match = re.search(r"/(\d+)$", content_range)
        if match:
            return int(match.group(1))
    content_length = response.headers.get("Content-Length")
    if content_length and content_length.isdigit():
        return offset + int(content_length)
    return None


def download_file(url: str, target: Path, *, tries: int = 8, sleep: float = 0.6) -> dict:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 0:
        return {"bytes": target.stat().st_size, "cached": True}

    partial = target.with_name(f"{target.name}.part")
    last_error: Exception | None = None
    for attempt in range(tries):
        offset = partial.stat().st_size if partial.exists() else 0
        headers = {"User-Agent": USER_AGENT, "Accept-Encoding": "identity"}
        if offset:
            headers["Range"] = f"bytes={offset}-"

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=120) as response:
                status = response.getcode()
                if offset and status != 206:
                    offset = 0
                    mode = "wb"
                else:
                    mode = "ab" if offset else "wb"
                expected_size = expected_download_size(response, offset)

                with partial.open(mode + "") as handle:
                    while True:
                        chunk = response.read(CHUNK_SIZE)
                        if not chunk:
                            break
                        handle.write(chunk)

                actual_size = partial.stat().st_size
                if expected_size is not None and actual_size < expected_size:
                    raise http.client.IncompleteRead(b"", expected_size - actual_size)

            partial.replace(target)
            return {"bytes": target.stat().st_size, "cached": False}
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 416 and partial.exists() and partial.stat().st_size > 0:
                partial.replace(target)
                return {"bytes": target.stat().st_size, "cached": False}
            if exc.code == 429:
                delay = int(exc.headers.get("Retry-After", "20"))
            elif 500 <= exc.code <= 599:
                delay = sleep * (2**attempt)
            else:
                raise
        except (urllib.error.URLError, TimeoutError, http.client.IncompleteRead, ConnectionResetError) as exc:
            last_error = exc
            delay = sleep * (2**attempt)
        time.sleep(delay)

    raise RuntimeError(f"failed to download {url}: {last_error}")


def request_json(url: str) -> dict:
    return json.loads(request_bytes(url).decode("utf-8"))


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def safe_name(value: str, fallback: str = "untitled") -> str:
    value = urllib.parse.unquote_plus(value).strip()
    value = re.sub(r"[\\/:*?\"<>|]+", "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    return value or fallback


def page_filename(page: PageRef | dict) -> str:
    if isinstance(page, PageRef):
        return f"{page.page_id}-{safe_name(page.slug)}.html"
    return f"{page['page_id']}-{safe_name(page.get('title') or page.get('slug') or 'untitled')}.html"


def parse_sitemap(xml_data: bytes) -> list[PageRef]:
    root = ET.fromstring(xml_data)
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    pages: list[PageRef] = []
    seen: set[str] = set()
    pattern = re.compile(r"^/space/([^/]+)/(\d+)(?:/(.*))?$")

    for node in root.findall("s:url", namespace):
        loc = node.findtext("s:loc", namespaces=namespace)
        if not loc:
            continue
        parsed = urllib.parse.urlparse(loc)
        match = pattern.match(parsed.path)
        if not match:
            continue
        space_key, page_id, slug = match.groups()
        if page_id in seen:
            continue
        seen.add(page_id)
        pages.append(PageRef(loc, space_key, page_id, slug or page_id))
    return pages


def relative_path(from_file: Path, to_file: Path) -> str:
    return posixpath.join(*Path(os.path.relpath(to_file, from_file.parent)).parts)


def rewrite_page_links(body: str, page_lookup: dict[str, Path], html_file: Path) -> str:
    def replace_atlassian(match: re.Match[str]) -> str:
        quote, page_id = match.group(1), match.group(2)
        target = page_lookup.get(page_id)
        if not target:
            return match.group(0)
        return f'href={quote}{html.escape(relative_path(html_file, target), quote=True)}{quote}'

    def replace_rmanwiki(match: re.Match[str]) -> str:
        quote, page_id = match.group(1), match.group(2)
        target = page_lookup.get(page_id)
        if not target:
            return match.group(0)
        return f'href={quote}{html.escape(relative_path(html_file, target), quote=True)}{quote}'

    body = re.sub(
        r'href=(["\'])https://renderman\.atlassian\.net/wiki/spaces/[^/"\']+/pages/(\d+)(?:/[^"\']*)?\1',
        replace_atlassian,
        body,
    )
    body = re.sub(
        r'href=(["\'])https://rmanwiki-27\.pixar\.com/space/[^/"\']+/(\d+)(?:/[^"\']*)?\1',
        replace_rmanwiki,
        body,
    )
    body = re.sub(
        r'href=(["\'])/space/[^/"\']+/(\d+)(?:/[^"\']*)?\1',
        replace_rmanwiki,
        body,
    )
    return body


def attachment_relative_path(page_id: str, raw_url: str, attachment_root: Path) -> Path | None:
    parsed = urllib.parse.urlparse(html.unescape(raw_url))
    match = re.search(r"/download/(?:thumbnails|attachments)/(\d+)/([^/?#]+)", parsed.path)
    if not match:
        return None
    source_page_id, filename = match.groups()
    filename = safe_name(filename)
    if source_page_id != page_id:
        page_id = source_page_id
    return attachment_root / page_id / filename


def rewrite_attachment_links(body: str, page_id: str, html_file: Path, attachment_root: Path) -> tuple[str, list[str]]:
    downloads: set[str] = set()

    def replace_attr(match: re.Match[str]) -> str:
        attr, quote, url = match.group(1), match.group(2), match.group(3)
        decoded_url = html.unescape(url)
        target = attachment_relative_path(page_id, decoded_url, attachment_root)
        if not target:
            return match.group(0)
        downloads.add(decoded_url)
        rel = html.escape(relative_path(html_file, target), quote=True)
        return f"{attr}={quote}{rel}{quote}"

    body = re.sub(
        r'\b(src|href|data-image-src)=(["\'])(https://renderman\.atlassian\.net/wiki/download/[^"\']+|https://rmanwiki-27\.pixar\.com/download/[^"\']+|/download/[^"\']+)\2',
        replace_attr,
        body,
    )
    body = re.sub(r'\s+srcset=(["\']).*?\1', "", body)
    return body, sorted(downloads)


def make_html_document(title: str, source_url: str, body: str, generated_at: str) -> str:
    escaped_title = html.escape(title)
    escaped_source = html.escape(source_url, quote=True)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escaped_title}</title>
  <style>
    :root {{ color-scheme: light; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.55;
      color: #202124;
      background: #f6f7f8;
    }}
    main {{
      max-width: 1040px;
      margin: 0 auto;
      padding: 32px 24px 64px;
      background: #fff;
      min-height: 100vh;
      box-sizing: border-box;
    }}
    header {{
      border-bottom: 1px solid #d8dde4;
      margin-bottom: 28px;
      padding-bottom: 18px;
    }}
    .source {{
      color: #5f6368;
      font-size: 13px;
      word-break: break-all;
    }}
    img {{
      max-width: 100%;
      height: auto;
    }}
    pre, code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }}
    pre {{
      overflow-x: auto;
      background: #f1f3f4;
      padding: 12px;
      border-radius: 6px;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      overflow-wrap: anywhere;
    }}
    th, td {{
      border: 1px solid #d8dde4;
      padding: 8px;
      vertical-align: top;
    }}
    .confluence-information-macro,
    .confluence-information-macro-note,
    .confluence-information-macro-warning,
    .confluence-information-macro-tip {{
      border-left: 4px solid #ff8a00;
      background: #fff7e6;
      padding: 12px 16px;
      margin: 16px 0;
    }}
  </style>
</head>
<body>
<main>
  <header>
    <h1>{escaped_title}</h1>
    <div class="source">Source: <a href="{escaped_source}">{html.escape(source_url)}</a></div>
    <div class="source">Downloaded: {html.escape(generated_at)}</div>
  </header>
  <article>
{body}
  </article>
</main>
</body>
</html>
"""


def make_index(page_records: list[dict], generated_at: str) -> str:
    groups: dict[str, list[dict]] = {}
    for record in page_records:
        groups.setdefault(record["space_key"], []).append(record)

    sections = []
    for space_key in sorted(groups):
        items = []
        for record in sorted(groups[space_key], key=lambda r: (r.get("title") or "", r["page_id"])):
            rel = html.escape(record["html_path"], quote=True)
            title = html.escape(record.get("title") or record.get("slug") or record["page_id"])
            items.append(f'<li><a href="{rel}">{title}</a> <span>{record["page_id"]}</span></li>')
        sections.append(f"<section><h2>{html.escape(space_key)}</h2><ul>{''.join(items)}</ul></section>")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RenderMan 27 Documentation</title>
  <style>
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #202124;
      background: #f6f7f8;
      line-height: 1.5;
    }}
    main {{
      max-width: 1040px;
      margin: 0 auto;
      padding: 32px 24px 64px;
      background: white;
      min-height: 100vh;
      box-sizing: border-box;
    }}
    h1 {{ margin-bottom: 0; }}
    .meta {{ color: #5f6368; margin: 8px 0 28px; }}
    section {{ border-top: 1px solid #d8dde4; padding-top: 18px; margin-top: 22px; }}
    ul {{ columns: 2 320px; padding-left: 20px; }}
    li {{ break-inside: avoid; margin: 0 0 8px; }}
    span {{ color: #7a7f85; font-size: 12px; }}
  </style>
</head>
<body>
<main>
  <h1>RenderMan 27 Documentation</h1>
  <div class="meta">Source: <a href="{SOURCE}/">{SOURCE}/</a> · Downloaded: {html.escape(generated_at)} · Pages: {len(page_records)}</div>
  {''.join(sections)}
</main>
</body>
</html>
"""


def page_api_url(page_id: str) -> str:
    params = urllib.parse.urlencode({"body-format": "view"})
    return f"{SOURCE}/api/v2/pages/{page_id}?{params}"


def collect_page_refs(output: Path) -> list[PageRef]:
    sitemap_data = request_bytes(SITEMAP)
    write_bytes(output / "source" / "sitemap.xml", sitemap_data)
    pages = parse_sitemap(sitemap_data)
    write_text(output / "source" / "urls.txt", "\n".join(page.source_url for page in pages) + "\n")
    return pages


def build_page_lookup(output: Path, pages: list[PageRef]) -> dict[str, Path]:
    return {
        page.page_id: output / "html" / page.space_key / page_filename(page)
        for page in pages
    }


def discover_referenced_pages(output: Path, page_records: list[dict], known_page_ids: set[str]) -> list[PageRef]:
    discovered: list[PageRef] = []
    seen = set(known_page_ids)
    pattern = re.compile(
        r'href=["\'](https://rmanwiki-27\.pixar\.com/space/([^/"\']+)/(\d+)(?:/([^"\']*))?)["\']'
    )

    for record in page_records:
        html_path = output / record["html_path"]
        if not html_path.exists():
            continue
        article = html_path.read_text(encoding="utf-8", errors="ignore").split("<article>", 1)[-1]
        for match in pattern.finditer(article):
            source_url, space_key, page_id, slug = match.groups()
            if page_id in seen:
                continue
            seen.add(page_id)
            discovered.append(PageRef(source_url, space_key, page_id, slug or page_id))
    return discovered


def download_page(page: PageRef, output: Path, page_lookup: dict[str, Path], generated_at: str) -> dict:
    filename = page_filename(page)
    html_path = output / "html" / page.space_key / filename
    raw_path = output / "api" / "pages" / page.space_key / f"{page.page_id}.json"
    attachment_root = output / "attachments"
    if raw_path.exists():
        api_data = json.loads(raw_path.read_text(encoding="utf-8"))
    else:
        api_data = request_json(page_api_url(page.page_id))
    title = api_data.get("title") or safe_name(page.slug)
    body = api_data.get("body", {}).get("view", {}).get("value", "")

    body = rewrite_page_links(body, page_lookup, html_path)
    body, attachment_urls = rewrite_attachment_links(body, page.page_id, html_path, attachment_root)

    write_text(raw_path, json.dumps(api_data, ensure_ascii=False, indent=2))
    write_text(html_path, make_html_document(title, page.source_url, body, generated_at))

    return {
        "source_url": page.source_url,
        "space_key": page.space_key,
        "page_id": page.page_id,
        "slug": page.slug,
        "title": title,
        "api_url": page_api_url(page.page_id),
        "api_path": str(raw_path.relative_to(output)),
        "html_path": str(html_path.relative_to(output)),
        "attachment_urls": attachment_urls,
    }


def iter_unique_downloads(page_records: Iterable[dict]) -> Iterable[tuple[str, Path]]:
    seen: set[Path] = set()
    attachment_root = Path("attachments")
    for record in page_records:
        for url in record.get("attachment_urls", []):
            target = attachment_relative_path(record["page_id"], url, attachment_root)
            if target is None or target in seen:
                continue
            seen.add(target)
            if url.startswith("/"):
                url = f"{SOURCE}{url}"
            yield url, target


def download_attachments(output: Path, page_records: list[dict], workers: int = 6) -> list[dict]:
    records: list[dict] = []
    downloads = list(iter_unique_downloads(page_records))
    workers = max(1, workers)

    def download_one(index: int, url: str, relative_target: Path) -> dict:
        target = output / relative_target
        try:
            result = download_file(url, target)
            return {"index": index, "url": url, "path": str(relative_target), **result}
        except Exception as exc:
            return {"index": index, "url": url, "path": str(relative_target), "error": str(exc), "cached": False}

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(download_one, index, url, relative_target)
            for index, (url, relative_target) in enumerate(downloads, 1)
        ]
        for completed, future in enumerate(as_completed(futures), 1):
            records.append(future.result())
            if completed % 100 == 0 or completed == len(downloads):
                print(f"Processed {completed}/{len(downloads)} attachments", flush=True)

    return sorted(records, key=lambda record: record["index"])


def write_readme(
    output: Path,
    page_count: int,
    page_failure_count: int,
    attachment_count: int,
    total_bytes: int,
    generated_at: str,
) -> None:
    readme = f"""# RenderMan 27 Documentation

Downloaded from `{SOURCE}/` on {generated_at}.

- Local entry point: `html/index.html`
- Pages: {page_count}
- Page API failures: {page_failure_count}
- Downloaded referenced attachments/images: {attachment_count}
- Attachment bytes: {total_bytes}
- Raw page API responses: `api/pages/`
- Sitemap and source URL list: `source/`

The source site is a JavaScript application. These files are a local static copy
generated from its public sitemap and public Confluence API responses.
"""
    write_text(output / "README.md", readme)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="renderman-docs-27", help="output directory")
    parser.add_argument("--skip-attachments", action="store_true", help="download page HTML/JSON only")
    parser.add_argument("--attachment-workers", type=int, default=6, help="parallel attachment downloads")
    args = parser.parse_args()

    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    print(f"Fetching sitemap: {SITEMAP}", flush=True)
    pages = collect_page_refs(output)
    print(f"Found {len(pages)} page URLs", flush=True)

    failures: list[dict] = []
    known_page_ids = {page.page_id for page in pages}
    page_records: list[dict] = []
    for discovery_round in range(1, 5):
        page_lookup = build_page_lookup(output, pages)
        page_records = []
        failures = []
        for index, page in enumerate(pages, 1):
            try:
                record = download_page(page, output, page_lookup, generated_at)
                page_records.append(record)
            except Exception as exc:
                failures.append({"page_id": page.page_id, "url": page.source_url, "error": str(exc)})
            if index % 50 == 0 or index == len(pages):
                print(f"Downloaded {index}/{len(pages)} page API responses", flush=True)

        extra_pages = discover_referenced_pages(output, page_records, known_page_ids)
        if not extra_pages:
            break
        pages.extend(extra_pages)
        known_page_ids.update(page.page_id for page in extra_pages)
        print(
            f"Discovered {len(extra_pages)} additional current-site referenced pages "
            f"(round {discovery_round})",
            flush=True,
        )

    write_text(output / "source" / "urls.txt", "\n".join(page.source_url for page in pages) + "\n")

    attachment_records: list[dict] = []
    if not args.skip_attachments:
        print("Downloading referenced attachments/images", flush=True)
        attachment_records = download_attachments(output, page_records, workers=args.attachment_workers)

    write_text(output / "html" / "index.html", make_index(page_records, generated_at))
    total_attachment_bytes = sum(item.get("bytes", 0) for item in attachment_records)
    manifest = {
        "source": SOURCE,
        "generated_at": generated_at,
        "page_count": len(page_records),
        "failed_page_count": len(failures),
        "attachment_count": len(attachment_records),
        "attachment_bytes": total_attachment_bytes,
        "pages": page_records,
        "attachments": attachment_records,
        "failures": failures,
    }
    write_text(output / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    write_readme(
        output,
        len(page_records),
        len(failures),
        len(attachment_records),
        total_attachment_bytes,
        generated_at,
    )

    if failures:
        print(f"Completed with {len(failures)} page failures. See manifest.json.", flush=True)
        return 2
    print("Completed successfully", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
