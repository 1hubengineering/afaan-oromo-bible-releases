"""Metadata integrity checks without a browser or external services."""

import json
import unittest

from site_metadata import inject_structured_data, structured_data


def page(language: str, description: str = "Offline reader") -> str:
    return (f'<html lang="{language}"><head><title>Afaan Oromo Bible</title>'
            f'<meta name="description" content="{description}"></head><body></body></html>')


class MetadataTests(unittest.TestCase):
    def test_language_and_domain_references_agree(self) -> None:
        for base in ("https://bible.1hubengineering.com/", "https://example.com/project/"):
            for language in ("en", "om"):
                graph = structured_data(page(language), base, language)["@graph"]
                web_page = next(item for item in graph if item["@type"] == "WebPage")
                self.assertEqual(web_page["url"], base + ("om/" if language == "om" else ""))
                self.assertEqual(web_page["inLanguage"], language)
                self.assertEqual(web_page["workTranslation"]["url"], base if language == "om" else base + "om/")
                identifiers = {item["@id"] for item in graph}
                for key in ("isPartOf", "about", "publisher"):
                    self.assertIn(web_page[key]["@id"], identifiers)

    def test_script_termination_is_escaped_without_changing_description(self) -> None:
        description = "Reader </script> &amp; notes"
        output = inject_structured_data(page("en", description), "https://example.com/", "en")
        serialized = output.split('type="application/ld+json">\n', 1)[1].split("\n</script>", 1)[0]
        self.assertNotIn("</script>", serialized)
        self.assertIn("\\u003c/script>", serialized)
        graph = json.loads(serialized)["@graph"]
        self.assertEqual(graph[-1]["description"], "Reader </script> & notes")

    def test_rejects_wrong_locale_missing_copy_and_duplicate_injection(self) -> None:
        for content, language in ((page("en"), "om"), (page("fr"), "fr"), (page("en", ""), "en")):
            with self.assertRaises(ValueError):
                inject_structured_data(content, "https://example.com/", language)
        output = inject_structured_data(page("en"), "https://example.com/", "en")
        with self.assertRaises(ValueError):
            inject_structured_data(output, "https://example.com/", "en")

    def test_app_metadata_preserves_beta_scope_without_invented_claims(self) -> None:
        graph = structured_data(page("en"), "https://example.com/", "en")["@graph"]
        application = next(item for item in graph if item["@type"] == "SoftwareApplication")
        self.assertIn("beta", application["softwareVersion"])
        self.assertTrue(all("beta" in system for system in application["operatingSystem"]))
        self.assertNotIn("offers", application)
        self.assertNotIn("aggregateRating", application)
        self.assertNotIn("review", application)
        self.assertNotIn("accessibilityConformance", application)


if __name__ == "__main__":
    unittest.main()
