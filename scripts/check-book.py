#!/usr/bin/env python3
"""Check a populated mdBook 0.5.4 build without third-party packages or network I/O."""

import argparse
import ast
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.text = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == "id":
                self.ids.add(value)
            if key in ("href", "src") and value:
                self.links.append(value)

    def handle_data(self, data):
        self.text.append(data)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_target(origin, link, boundary):
    url = urlsplit(link)
    if url.scheme or url.netloc:
        return None
    if url.path.startswith("/"):
        target = (boundary / unquote(url.path).lstrip("/")).resolve()
    else:
        target = (origin.parent / unquote(url.path)).resolve() if url.path else origin
    require(target.is_relative_to(boundary), f"Link escapes {boundary}: {link}")
    if target.is_dir():
        target /= "index.html"
    require(target.is_file(), f"Missing local target in {origin}: {link}")
    return target, unquote(url.fragment)


def check(root, output):
    source = root / "src"
    summary = (source / "SUMMARY.md").read_text()
    # SUMMARY contains plain inline chapter links; reject missing/duplicate chapters.
    members = re.findall(r"\[[^\]]+\]\(([^)]+)\)", summary)
    chapters = {p.relative_to(source).as_posix() for p in source.rglob("*.md")}
    chapters.remove("SUMMARY.md")
    require(set(members) == chapters, f"SUMMARY mismatch: {set(members) ^ chapters}")
    require(all(n == 1 for n in Counter(members).values()), "Duplicate SUMMARY chapter")
    for member in members:
        text = (source / member).read_text().strip()
        require(len(text.splitlines()) > 1, f"Empty chapter: {member}")
        require(text.startswith("# "), f"Missing chapter heading: {member}")
        require((output / Path(member).with_suffix(".html")).is_file(),
                f"Chapter not rendered: {member}")

    pages = {p.resolve(): Page(p.read_text()) for p in output.rglob("*.html")}
    require(pages, "No HTML output; run mdbook build first")
    count = 0
    for origin, page in pages.items():
        for link in page.links:
            result = local_target(origin, link, output)
            if result is None:
                continue
            target, fragment = result
            if fragment and target in pages:
                require(fragment in pages[target].ids,
                        f"Missing anchor in {origin}: {link}")
            count += 1

    readme = root / "README.md"
    for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme.read_text()):
        result = local_target(readme, link, root)
        if result:
            # README currently links files, without Markdown heading fragments.
            require(not result[1], f"README fragment needs validation: {link}")

    indexes = list(output.glob("searchindex-*.js"))
    require(len(indexes) == 1, "Expected one mdBook 0.5.4 search index; clean/rebuild output")
    script = indexes[0].read_text()
    # mdBook 0.5.4 wraps its JSON in JSON.parse('...'). literal_eval decodes the
    # quoted string only; it does not execute JavaScript or Python expressions.
    literal = script.split("JSON.parse(", 1)[1].rsplit(")", 2)[0]
    search = json.loads(ast.literal_eval(literal))
    urls = search["doc_urls"]
    indexed = {urlsplit(url).path for url in urls}
    for member in members:
        require(Path(member).with_suffix(".html").as_posix() in indexed,
                f"Chapter absent from search: {member}")
    for url in urls:
        result = local_target(output / "index.html", url, output)
        require(result is not None, f"Nonlocal search entry: {url}")
        target, fragment = result
        require(target in pages and (not fragment or fragment in pages[target].ids),
                f"Broken search entry: {url}")

    coverage = " ".join(pages[output / "coverage.html"].text)
    docs = search["index"]["documentStore"]["docs"]
    search_coverage = " ".join(
        docs[str(i)]["body"] for i, url in enumerate(urls)
        if urlsplit(url).path == "coverage.html"
    )
    # Distinctive text from the inherited map and the current qualification:
    # having just a coverage title or sidebar link is insufficient.
    markers = ("Chapter 10 UDP streaming", "historical local evidence inherited",
               "Resolved in this book", "Rust 1.85")
    for marker in markers:
        for label, text in (("rendered coverage", coverage), ("search coverage", search_coverage)):
            require(marker in " ".join(text.split()), f"Missing {marker!r} in {label}")
    print(f"PASS: {len(members)} populated chapters, {len(pages)} HTML pages, "
          f"{count} local references, {len(urls)} search entries; current coverage rendered/indexed")


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book-dir", type=Path, default=root / "book")
    args = parser.parse_args()
    try:
        check(root, args.book_dir.resolve())
    except (ValueError, KeyError, IndexError, SyntaxError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
