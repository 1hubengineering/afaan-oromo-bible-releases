#!/usr/bin/env python3
"""Generate the committed Afaan Oromoo page from explicit copy mappings.

This is maintenance tooling, not a browser dependency. Both languages remain
complete static HTML and work with JavaScript disabled. Python standard library only.
"""
from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "website/index.html"
DESTINATION = ROOT / "website/om/index.html"
TRANSLATIONS = ROOT / "website-docs/oromo-translations.json"
BASE_URL = "https://1hubengineering.github.io/afaan-oromo-bible-releases/"


class ExactTranslator(HTMLParser):
    """Translate whole text nodes and whole text attributes, never substrings."""
    def __init__(self, replacements: dict[str, str]) -> None:
        super().__init__(convert_charrefs=False)
        self.replacements = replacements
        self.output: list[str] = []
        self.pending: list[str] = []

    def flush(self) -> None:
        raw = ''.join(self.pending)
        self.pending.clear()
        decoded = html.unescape(raw)
        stripped = decoded.strip()
        if stripped in self.replacements:
            leading = re.match(r'\s*', decoded).group(0)
            trailing = re.search(r'\s*$', decoded).group(0)
            self.output.append(leading + html.escape(self.replacements[stripped], quote=False) + trailing)
        else:
            self.output.append(raw)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.flush()
        def translate_attribute(match: re.Match) -> str:
            name, quote, raw_value = match.group('name', 'quote', 'value')
            value = html.unescape(raw_value)
            if name in {'alt', 'aria-label', 'title', 'data-caption', 'content'} and value in self.replacements:
                return name + '=' + quote + html.escape(self.replacements[value], quote=True) + quote
            return match.group(0)
        text = re.sub(r'(?P<name>[\w:-]+)=(?P<quote>["\'])(?P<value>.*?)(?P=quote)',
                      translate_attribute, self.get_starttag_text(), flags=re.DOTALL)
        self.output.append(text)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        self.flush()
        self.output.append('</' + tag + '>')

    def handle_data(self, data: str) -> None:
        self.pending.append(data)

    def handle_entityref(self, name: str) -> None:
        self.pending.append('&' + name + ';')

    def handle_charref(self, name: str) -> None:
        self.pending.append('&#' + name + ';')

    def handle_decl(self, decl: str) -> None:
        self.flush()
        self.output.append('<!' + decl + '>')

    def handle_comment(self, data: str) -> None:
        self.flush()
        self.output.append('<!--' + data + '-->')


def localized_html() -> str:
    source = SOURCE.read_text(encoding="utf-8")
    translation = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))
    keys = set(re.findall(r'data-i18n="([^"]+)"', source))
    keyed = translation["i18n"]
    missing = sorted(keys - keyed.keys())
    if missing:
        raise ValueError("Missing Afaan Oromoo content keys: " + ", ".join(missing))

    for key in sorted(keys):
        pattern = re.compile(
            r'(<(?P<tag>[a-z][a-z0-9]*)\b[^>]*\bdata-i18n="'
            + re.escape(key) + r'"[^>]*>)(?P<body>.*?)</(?P=tag)>', re.DOTALL)
        source, count = pattern.subn(lambda match: match.group(1) + keyed[key]
                                     + "</" + match.group("tag") + ">", source)
        if count != 1:
            raise ValueError(f"Translation key must occur exactly once: {key} ({count})")

    # Full paragraphs with inline links are translated together for natural word order.
    exact = translation.get("exact", {})
    for english, oromo in sorted(exact.items(), key=lambda item: len(item[0]), reverse=True):
        if '<' in english:
            source = source.replace(english, oromo)
    parser = ExactTranslator({key: value for key, value in exact.items() if '<' not in key})
    parser.feed(source)
    parser.close()
    parser.flush()
    source = ''.join(parser.output)

    source = source.replace('<html lang="en"', '<html lang="om"')
    source = source.replace('property="og:locale:alternate" content="om_ET"',
                            'property="og:locale:alternate" content="en_US"')
    source = source.replace('property="og:locale" content="en_US"',
                            'property="og:locale" content="om_ET"')
    source = source.replace(f'rel="canonical" href="{BASE_URL}"',
                            f'rel="canonical" href="{BASE_URL}om/"')
    source = source.replace(f'property="og:url" content="{BASE_URL}"',
                            f'property="og:url" content="{BASE_URL}om/"')
    # srcset candidates after commas need the same prefix adjustment as src/href.
    source = source.replace('./assets/', '../assets/')
    source = re.sub(r'(["\'])\./(styles\.css|theme\.js|app\.js|feedback-config\.js|feedback\.js)',
                    r'\1../\2', source)

    language_group = ('<div class="language-switcher" role="group" aria-label="Afaan fuula kanaa">'
                      '<a class="language-option language-switch" href="../" lang="en" hreflang="en" aria-label="English">EN</a>'
                      '<a class="language-option" href="./" lang="om" hreflang="om" aria-current="page" aria-label="Afaan Oromoo">OR</a></div>')
    source, count = re.subn(r'<div class="language-switcher"[^>]*>.*?</div>',
                            language_group, source, flags=re.DOTALL)
    if count != 1:
        raise ValueError("Expected exactly one language switcher")
    return source


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Fail if the committed Oromo page is missing or stale")
    args = parser.parse_args()
    try:
        output = localized_html()
        if args.check:
            if not DESTINATION.is_file() or DESTINATION.read_text(encoding="utf-8") != output:
                raise ValueError("Afaan Oromoo page is stale; run python3 scripts/localize_site.py")
            print("PASS: the complete Afaan Oromoo page matches the translation source")
        else:
            DESTINATION.parent.mkdir(parents=True, exist_ok=True)
            DESTINATION.write_text(output, encoding="utf-8")
            print("Generated website/om/index.html")
    except (OSError, ValueError, KeyError) as exc:
        print(f"Localization failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
