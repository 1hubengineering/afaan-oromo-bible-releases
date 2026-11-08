"""Static, factual search metadata for the two public website languages."""

from __future__ import annotations

from html.parser import HTMLParser
import json


REPOSITORY = "https://github.com/1hubengineering/afaan-oromo-bible-releases"
RELEASE = REPOSITORY + "/releases/tag/v0.1.0-beta.8"
KEYWORDS = [
    "Afaan Oromo Bible", "Afaan Oromoo", "Oromo Bible", "Kitaaba Qulqulluu",
    "offline Bible reader", "Bible study", "Bible comparison", "personal study notes",
]


class PageMetadata(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.language = ""
        self.title = ""
        self.meta: dict[str, str] = {}
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.language = attributes.get("lang") or ""
        elif tag == "title":
            self.in_title = True
        elif tag == "meta":
            key = attributes.get("name") or attributes.get("property")
            if key:
                self.meta[key] = attributes.get("content") or ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def structured_data(content: str, site_url: str, language: str) -> dict:
    page = PageMetadata()
    page.feed(content)
    if language not in {"en", "om"} or page.language != language:
        raise ValueError("Structured metadata requires the correct en/om page language")
    if not page.title.strip() or not page.meta.get("description"):
        raise ValueError("Structured metadata requires the localized title and description")
    canonical = site_url + ("om/" if language == "om" else "")
    organization = site_url + "#organization"
    website = site_url + "#website"
    application = site_url + "#application"
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization", "@id": organization,
                "name": "AndHub Engineering", "url": "https://1hubengineering.com/",
                "logo": site_url + "assets/images/andhub-logo-light.svg",
                "email": "info@1hubengineering.com",
            },
            {
                "@type": "WebSite", "@id": website,
                "name": "Afaan Oromo Bible", "url": site_url,
                "inLanguage": ["en", "om"], "keywords": KEYWORDS,
                "publisher": {"@id": organization},
            },
            {
                "@type": "SoftwareApplication", "@id": application,
                "name": "Afaan Oromo Bible", "alternateName": "Oromo Bible Reader",
                "description": page.meta["description"], "url": site_url,
                "applicationCategory": "ReferenceApplication",
                "operatingSystem": ["Windows x64 (beta)", "macOS (experimental beta)",
                                    "Ubuntu 24.04 x64 (experimental beta)"],
                "softwareVersion": "0.1.0-beta.8", "inLanguage": ["en", "om"],
                "downloadUrl": RELEASE, "installUrl": site_url + "#downloads",
                "releaseNotes": RELEASE, "license": REPOSITORY + "/blob/main/LICENSING.md",
                "screenshot": site_url + "assets/images/reader-classic.webp",
                "publisher": {"@id": organization},
            },
            {
                "@type": "WebPage", "@id": canonical + "#webpage",
                "name": page.title.strip(), "description": page.meta["description"],
                "url": canonical, "inLanguage": language,
                "isPartOf": {"@id": website}, "about": {"@id": application},
                "publisher": {"@id": organization},
                "workTranslation": {"@type": "WebPage", "inLanguage": "en" if language == "om" else "om",
                                    "url": site_url if language == "om" else site_url + "om/"},
                "primaryImageOfPage": {
                    "@type": "ImageObject", "url": site_url + "assets/images/social-preview.png",
                    "width": 1280, "height": 640,
                },
            },
        ],
    }


def inject_structured_data(content: str, site_url: str, language: str) -> str:
    if content.count("</head>") != 1 or 'id="structured-data"' in content:
        raise ValueError("Expected one clean HTML head before metadata injection")
    data = json.dumps(structured_data(content, site_url, language), ensure_ascii=False, indent=2)
    # Metadata is static HTML; a localized title must never terminate its script.
    data = data.replace("<", "\\u003c")
    return content.replace("</head>", '<script id="structured-data" type="application/ld+json">\n'
                           + data + "\n</script>\n</head>")
