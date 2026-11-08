#!/usr/bin/env python3
"""Validate both static language pages, assets and the verified beta.8 downloads.

This check needs no third-party dependencies or network requests. Installer
URLs were checked against the published release asset inventory; new releases
should be verified before updating the website and this inventory together.
"""

from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from prepare_site import PROJECT_ROOT, is_public_file, normalize_site_url


REPOSITORY = "https://github.com/1hubengineering/afaan-oromo-bible-releases"
RELEASE = f"{REPOSITORY}/releases/tag/v0.1.0-beta.8"
DOWNLOAD_BASE = f"{REPOSITORY}/releases/download/v0.1.0-beta.8/"
INSTALLERS = {
    "Afaan-Oromo-Bible-0.1.0-beta.8-x64-setup.exe",
    "Afaan-Oromo-Bible-0.1.0-beta.8-macos-arm64.dmg",
    "Afaan-Oromo-Bible-0.1.0-beta.8-macos-x86_64.dmg",
    "Afaan-Oromo-Bible-0.1.0-beta.8-linux-amd64.deb",
}
REQUIRED_DOWNLOADS = {DOWNLOAD_BASE + name for name in INSTALLERS}


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.references: list[tuple[str, str, int]] = []
        self.fragments: list[tuple[str, int]] = []
        self.metadata: dict[str, str] = {}
        self.alternates: dict[str, str] = {}
        self.canonical: str | None = None
        self.lang: str | None = None
        self.h1_count = 0
        self.has_title = False
        self.images = 0
        self.errors: list[str] = []
        self.json_ld: list[str] = []
        self._in_json_ld = False
        self._json_buffer = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        line = self.getpos()[0]
        if attributes.get("id"):
            self.ids.append(attributes["id"] or "")
        if tag == "html":
            self.lang = attributes.get("lang")
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "title":
            self.has_title = True
        elif tag == "meta":
            key = attributes.get("property") or attributes.get("name")
            if key:
                self.metadata[key] = attributes.get("content") or ""
        elif tag == "link" and "canonical" in (attributes.get("rel") or "").split():
            self.canonical = attributes.get("href")
        elif tag == "link" and "alternate" in (attributes.get("rel") or "").split():
            if attributes.get("hreflang"):
                self.alternates[attributes["hreflang"] or ""] = attributes.get("href") or ""
        elif tag == "img":
            self.images += 1
            if "alt" not in attributes:
                self.errors.append(f"Line {line}: image is missing alternative text")
            if not attributes.get("width") or not attributes.get("height"):
                self.errors.append(f"Line {line}: image needs width and height to reserve its layout space")
        elif tag == "script" and attributes.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_buffer = ""

        for name in ("aria-labelledby", "aria-describedby", "aria-controls"):
            for identifier in (attributes.get(name) or "").split():
                self.fragments.append((identifier, line))

        href = attributes.get("href")
        if href:
            if tag == "a":
                self.links.append(href)
            if href.startswith("#"):
                if len(href) > 1:
                    self.fragments.append((unquote(href[1:]), line))
            elif tag == "a":
                self.references.append((href, "link", line))
            elif tag == "link" and not ({"canonical", "alternate"} & set((attributes.get("rel") or "").split())):
                self.references.append((href, "asset", line))

        for name in ("src", "poster", "data-full-src", "data-full", "data-src", "data-image"):
            if attributes.get(name):
                self.references.append((attributes[name] or "", "asset", line))
        if attributes.get("srcset"):
            for candidate in (attributes["srcset"] or "").split(","):
                if candidate.strip():
                    self.references.append((candidate.strip().split()[0], "asset", line))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_json_ld:
            self.json_ld.append(self._json_buffer)
            self._in_json_ld = False

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self._json_buffer += data


def check_local_url(url: str, directory: Path, *, context: str,
                    errors: list[str], relative_to: Path | None = None,
                    allow_directory_index: bool = False) -> None:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        errors.append(f"{context}: loaded assets must be local, not {url}")
        return
    if parsed.path.startswith("/"):
        errors.append(f"{context}: root-relative path breaks repository-subpath hosting: {url}")
        return
    if not parsed.path:
        return
    local = ((relative_to or directory) / unquote(parsed.path)).resolve()
    try:
        local.relative_to(directory)
    except ValueError:
        errors.append(f"{context}: asset path escapes the website directory: {url}")
        return
    if allow_directory_index and local.is_dir():
        local = local / "index.html"
    if not local.is_file():
        errors.append(f"{context}: file does not exist: {url}")


def validate_page(parser: SiteParser, page: Path, directory: Path,
                  expected_language: str, site_url: str) -> list[str]:
    errors: list[str] = []
    errors.extend(parser.errors)

    if parser.lang != expected_language:
        errors.append(f"The page must declare html lang=\"{expected_language}\"")
    if parser.h1_count != 1:
        errors.append(f"Expected one primary heading; found {parser.h1_count}")
    if not parser.has_title:
        errors.append("The page title is missing")
    for name in ("description", "viewport", "og:title", "og:description", "og:type",
                 "og:url", "og:image", "og:locale", "twitter:card", "twitter:image"):
        if not parser.metadata.get(name):
            errors.append(f"Required metadata is missing or empty: {name}")
    canonical = parser.canonical or ""
    try:
        if normalize_site_url(canonical) != canonical:
            errors.append("Canonical URL must end in a slash")
    except ValueError:
        errors.append("The canonical URL must be an absolute HTTPS site URL")
    expected_canonical = site_url + ("om/" if expected_language == "om" else "")
    if canonical != expected_canonical:
        errors.append(f"Unexpected locale canonical URL; expected {expected_canonical}")
    expected_locale = "om_ET" if expected_language == "om" else "en_US"
    if parser.metadata.get("og:locale") != expected_locale:
        errors.append(f"og:locale must identify this page as {expected_locale}")
    expected_alternates = {"en": site_url, "om": site_url + "om/", "x-default": site_url}
    for language, url in expected_alternates.items():
        if parser.alternates.get(language) != url:
            errors.append(f"Missing or incorrect hreflang={language}: expected {url}")
    if parser.metadata.get("og:url") != canonical:
        errors.append("og:url and the canonical URL disagree")
    for name in ("og:image", "twitter:image"):
        value = parser.metadata.get(name, "")
        if site_url and value.startswith(site_url):
            check_local_url(value[len(site_url):], directory, context=name, errors=errors)
        else:
            errors.append(f"{name} must use an absolute image URL under the root site URL")
    for content in parser.json_ld:
        try:
            json.loads(content)
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid structured-data JSON: {exc}")

    ids = set(parser.ids)
    for identifier, count in Counter(parser.ids).items():
        if count > 1:
            errors.append(f"Duplicate element id: {identifier}")
    for fragment, line in parser.fragments:
        if fragment not in ids:
            errors.append(f"Line {line}: target id does not exist: {fragment}")

    for url, kind, line in parser.references:
        parsed = urlsplit(url)
        if kind == "link" and parsed.scheme == "https":
            continue
        if kind == "link" and parsed.scheme in {"mailto", "tel"}:
            continue
        check_local_url(url, directory, context=f"Line {line}", errors=errors,
                        relative_to=page.parent, allow_directory_index=kind == "link")

    links = set(parser.links)
    other_page = directory / ("index.html" if expected_language == "om" else "om/index.html")
    has_language_link = False
    for url in links:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (page.parent / unquote(parsed.path)).resolve()
        if target.is_dir():
            target = target / "index.html"
        if target == other_page:
            has_language_link = True
            break
    if not has_language_link:
        errors.append("Missing ordinary HTML link to the other language page")
    for url in sorted(REQUIRED_DOWNLOADS - links):
        errors.append(f"Missing verified beta.8 installer link: {url}")
    installer_suffixes = (".exe", ".dmg", ".deb", ".msi", ".appimage", ".rpm")
    for url in links:
        if urlsplit(url).path.lower().endswith(installer_suffixes) and url not in REQUIRED_DOWNLOADS:
            errors.append(f"Installer link is not in the verified beta.8 inventory: {url}")
    for document in ("INSTALLATION.md", "TESTING_GUIDE.md", "LICENSING.md", "PRIVACY.md", "SECURITY.md"):
        expected = f"{REPOSITORY}/blob/main/{document}"
        if expected not in links:
            errors.append(f"Missing public documentation link: {document}")
    if DOWNLOAD_BASE + "SHA256SUMS" not in links:
        errors.append("Missing beta.8 SHA256SUMS link")
    if not ({RELEASE, DOWNLOAD_BASE + "RELEASE_NOTES.md"} & links):
        errors.append("Missing beta.8 release-notes link")
    if not any(url.startswith(REPOSITORY + "/issues") for url in links):
        errors.append("Missing issue-reporting link")

    return [f"{page.relative_to(directory)}: {error}" for error in errors]


def validate(directory: Path) -> list[str]:
    errors: list[str] = []
    pages: dict[str, SiteParser] = {}
    for name in ("index.html", "om/index.html"):
        page = directory / name
        if not page.is_file():
            errors.append(f"Missing {page}")
            continue
        parser = SiteParser()
        parser.feed(page.read_text(encoding="utf-8"))
        pages[name] = parser
    site_url = (pages["index.html"].canonical or "") if "index.html" in pages else ""
    for name, parser in pages.items():
        language = "om" if name.startswith("om/") else "en"
        errors.extend(validate_page(parser, directory / name, directory, language, site_url))

    for item in sorted(directory.rglob("*")):
        relative = item.relative_to(directory)
        if item.is_symlink():
            errors.append(f"Symbolic links must not be deployed: {relative}")
        elif item.is_file() and not is_public_file(relative):
            errors.append(f"Unexpected file in the public output: {relative}")
        if item.is_file() and item.suffix == ".css":
            content = item.read_text(encoding="utf-8")
            for match in re.finditer(r"url\(\s*['\"]?([^'\")\s]+)['\"]?\s*\)", content):
                url = match.group(1)
                if url.startswith("#"):
                    continue
                check_local_url(url, directory, context=str(relative), errors=errors, relative_to=item.parent)
            if re.search(r"@import\s", content):
                errors.append(f"Unexpected CSS import; keep styles self-contained: {relative}")

    if not errors:
        for name, parser in pages.items():
            print(f"PASS: {name} — {parser.images} images, {len(set(parser.ids))} unique ids, "
                  f"{len(parser.references)} asset/link references and all 4 verified beta.8 installers")
        print("PASS: root/subpath-safe assets, native language links, locale metadata and public documentation links")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", default="_site",
                        help="Website directory relative to the project (default: _site)")
    args = parser.parse_args()
    directory = Path(args.directory)
    if not directory.is_absolute():
        directory = PROJECT_ROOT / directory
    directory = directory.resolve()
    try:
        errors = validate(directory)
    except (OSError, UnicodeError, ValueError) as exc:
        errors = [str(exc)]
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
