# Search discovery and sharing

The canonical website is https://bible.1hubengineering.com/, with Afaan Oromoo at https://bible.1hubengineering.com/om/. This public repository distributes beta releases and website source; application source remains private.

## Search phrases and repository topics

Use the product name and relevant phrases naturally: **Afaan Oromo Bible**, **Afaan Oromoo**, **Oromo Bible**, **Kitaaba Qulqulluu**, **offline Bible reader**, **Bible study**, **Bible comparison**, and **personal study notes**. Descriptions retain the Windows beta and experimental Mac/Ubuntu distinction. Do not add unverified publisher affiliations, fake testimonials, download counts or open-source licensing claims.

The public repository About description, website link and topics identify its purpose. Topics cover Afaan Oromo, Bible reading/study, offline use, comparison, notes, languages, desktop platforms and beta status. GitHub issue labels and the accessibility form organize feedback; they are separate from repository discovery topics.

Google ignores the old meta-keywords tag. Search phrases are placed in relevant titles/descriptions, readable repository copy and structured website metadata. No hidden keyword lists or duplicate language doorway pages are used.

## Crawlable pages and metadata

- `/robots.txt` allows crawling and advertises the canonical `/sitemap.xml`.
- The sitemap contains the English and Oromo URLs with reciprocal `en`, `om` and `x-default` language annotations. No invented modification dates or frequency promises are included.
- Both HTML pages have distinct localized titles/descriptions, canonical URLs, language alternates, a crawlable robots policy, Open Graph and large-image Twitter/X card metadata.
- The preparation script adds static JSON-LD for `Organization`, `WebSite`, `WebPage` and `SoftwareApplication`. It uses current developer details, the actual beta release and localized page copy. It contains no invented prices, ratings, endorsements, reviews or application accessibility certifications.
- The shared 1280×640 PNG combines original website typography with an authorized screenshot of the actual reader. Source screenshots and publisher notices retain their original provenance.

Search engines decide indexing, ranking and rich-result eligibility. Application metadata without invented reviews/pricing is useful descriptive data; this setup does not promise a software rich result. The existing HTTPS redirects consolidate the original GitHub Pages address onto the custom domain.

## Search Console and Bing Webmaster Tools

The files are ready for account-owner verification, but no search-engine account was connected or submitted to during implementation.

1. Add `https://bible.1hubengineering.com/` to Google Search Console using the account that should own the property. Choose URL-prefix verification if you want verification limited to this website; a domain property uses a DNS TXT record in Porkbun.
2. Use Google's actual verification value. For an HTML meta verification method, add the supplied public tag to `website/index.html`, regenerate the Oromo page and deploy. A supplied verification HTML file needs an explicit publication-allowlist decision. Never invent a token or publish a private API credential.
3. Submit `https://bible.1hubengineering.com/sitemap.xml` in Search Console and inspect both language URLs. Use its indexing reports to diagnose actual crawl problems.
4. If desired, import the verified property into Bing Webmaster Tools or use Bing's supplied verification method, then submit the same sitemap.

These account actions need owner access and are separate from publishing robots/sitemap files. No tracking code, analytics account or paid SEO service is required by the website.

## GitHub repository social preview

The website's sharing image and the README preview are already part of this repository at `website/assets/images/social-preview.png`. To use the same image as GitHub's own repository social-preview setting, an administrator can upload it under **Settings → General → Social preview → Edit → Upload an image**. GitHub's supported repository metadata API does not expose this image setting; the automated changes do not claim to have set it. The prepared image is 1280×640 and under 1 MB.

## Maintaining this setup

Update page copy, the translation catalog and generated Oromo HTML together. Update beta release references in `scripts/site_metadata.py` and the reviewed download inventory in `scripts/check_site.py` when publishing another version. Source canonical placeholders remain the default GitHub project URL; `prepare_site.py` replaces them with the actual HTTPS URL supplied by `configure-pages` and then creates the static structured-data graph. This supports a custom-domain root and the repository-path preview without mixed canonical URLs.

Run localization consistency, metadata unit checks, staging and static validation before deployment. Review all gallery states and keyboard behavior after interface changes. The [accessibility statement](../ACCESSIBILITY.md) explains reporting and current verification scope.

## Primary references

- [Google-supported meta tags](https://developers.google.com/search/docs/crawling-indexing/special-tags)
- [Localized pages and hreflang sitemaps](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Software application structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- [GitHub repository topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [GitHub social previews](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [WAI-ARIA tabs pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)
