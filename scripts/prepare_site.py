#!/usr/bin/env python3
"""Stage a deliberate, static-only GitHub Pages artifact using the Python stdlib."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import urlsplit


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT_ROOT / "website"
DEFAULT_SITE_URL = "https://1hubengineering.github.io/afaan-oromo-bible-releases/"

# This is an allowlist, not a copy of the repository root. Extend it deliberately
# when adding a new public asset type. Documentation and app data do not belong
# in the deployment artifact.
ROOT_FILES = {
    "index.html", "404.html", "styles.css", "app.js", "theme.js", ".nojekyll",
    "robots.txt", "sitemap.xml", "site.webmanifest", "favicon.ico",
}
IMAGE_SUFFIXES = {".webp", ".png", ".jpg", ".jpeg", ".avif", ".svg", ".ico"}


def is_public_file(relative_path: Path) -> bool:
    """Return whether a website-relative path is explicitly publishable."""
    name = relative_path.as_posix()
    if name in ROOT_FILES or name in {"assets/favicon.svg", "om/index.html"}:
        return True
    return (
        len(relative_path.parts) >= 3
        and relative_path.parts[:2] == ("assets", "images")
        and not any(part.startswith(".") for part in relative_path.parts)
        and relative_path.suffix.lower() in IMAGE_SUFFIXES
    )


def normalize_site_url(value: str) -> str:
    """Accept a public HTTPS base URL, with no credentials or injected markup."""
    value = value.strip()
    parsed = urlsplit(value)
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or not re.fullmatch(r"[A-Za-z0-9.-]+", parsed.netloc)
        or not re.fullmatch(r"/[A-Za-z0-9._~%/-]*|", parsed.path)
        or any(part in {".", ".."} for part in parsed.path.split("/"))
    ):
        raise ValueError("--site-url must be an absolute HTTPS site URL without a query or fragment")
    return value.rstrip("/") + "/"


def safe_output_path(value: str) -> Path:
    """Limit replaceable output to this project's generated output directories."""
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = PROJECT_ROOT / candidate
    if candidate.is_symlink():
        raise ValueError("The output directory must not be a symbolic link")
    resolved = candidate.resolve()
    try:
        relative = resolved.relative_to(PROJECT_ROOT)
    except ValueError as exc:
        raise ValueError("Output must be inside the project, under _site or _preview") from exc
    if not relative.parts or relative.parts[0] not in {"_site", "_preview"}:
        raise ValueError("Output must be inside the project, under _site or _preview")
    if resolved.exists() and not resolved.is_dir():
        raise ValueError("The output path already exists and is not a directory")
    return resolved


def stage_site(site_url: str, output: Path) -> int:
    if SOURCE.is_symlink() or not SOURCE.is_dir():
        raise ValueError("website/ must be an ordinary directory")
    if not (SOURCE / "index.html").is_file():
        raise ValueError("website/index.html is missing")

    files: list[Path] = []
    for item in sorted(SOURCE.rglob("*")):
        relative = item.relative_to(SOURCE)
        if item.is_symlink():
            raise ValueError(f"Refusing to publish symbolic link: {relative}")
        if item.is_dir():
            continue
        if not item.is_file() or not is_public_file(relative):
            raise ValueError(f"Unexpected website file (not in the publication allowlist): {relative}")
        files.append(relative)

    # Validate the entire source before replacing a previous generated artifact.
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    for relative in files:
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SOURCE / relative, destination)
        if destination.suffix in {".html", ".xml", ".txt", ".webmanifest"}:
            content = destination.read_text(encoding="utf-8")
            destination.write_text(content.replace(DEFAULT_SITE_URL, site_url), encoding="utf-8")
    (output / ".nojekyll").touch()
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-url", default=DEFAULT_SITE_URL,
                        help="Canonical HTTPS base URL (defaults to the project GitHub Pages URL)")
    parser.add_argument("--output", default="_site",
                        help="Generated directory below _site/ or _preview/ (default: _site)")
    args = parser.parse_args()
    try:
        site_url = normalize_site_url(args.site_url)
        output = safe_output_path(args.output)
        count = stage_site(site_url, output)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Website staging failed: {exc}", file=sys.stderr)
        return 1
    print(f"Staged {count} public files in {output.relative_to(PROJECT_ROOT)}/")
    print(f"Canonical site URL: {site_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
