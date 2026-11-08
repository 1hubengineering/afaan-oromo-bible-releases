# Delivery validation

Prepared on 8 November 2026 for `1hubengineering/afaan-oromo-bible-releases`.

## Completed checks

| Area | Evidence and result |
| --- | --- |
| Public release content | The GitHub connector verified the published `v0.1.0-beta.8` prerelease, all four installer asset URLs and byte sizes, SHA256SUMS, and the linked public guides/notices. No installer was downloaded or executed. |
| Static deployment | The publication allowlist includes only the two language pages, their CSS/JavaScript, favicon and authorized image assets. The workflow uploads `_site/`, not the repository. Existing repository documentation, releases and issue templates are not part of the additions or deployment. |
| Local paths | Both languages pass local asset, `srcset`, anchor, ARIA-reference and language-link validation. The actual page was inspected under `/afaan-oromo-bible-releases/` and `/afaan-oromo-bible-releases/om/`. |
| Domain metadata | Staging with a custom-domain URL correctly rewrites both locale canonicals, the en/om/x-default alternates and social-image URLs. Installer URLs remain unchanged. |
| Bilingual content | All 112 keyed content entries are translated. Full paragraphs, screenshot descriptions, accessibility labels and page metadata are also covered. The committed Oromo page matches the catalog-generated result. Remaining English text in that page consists of intentional names, technical terms and the English language-link label. |
| Desktop appearance | Light and dark appearances inspected in the browser. The main desktop preview was approximately 1363 pixels wide; a 1200-pixel content frame also covered Oromo download columns and navigation. |
| Responsive layout | Browser frames at 320, 390, 820 and 1200 pixels were inspected. Document width equaled available viewport width at those checks, with no horizontal overflow. Longer Oromo labels and the developer section were reviewed. These are responsive browser checks, not physical-device qualification. |
| Mobile navigation | Opening the menu by keyboard moves focus into navigation. Escape closes it and restores focus; following a section link closes it and moves focus to that section. Navigation wraps on narrow screens. |
| Gallery and modal | Arrow-key tab navigation changes the selected screenshot and visible panel. Keyboard activation opens the image dialog with focus on Close. Escape closes it and restores focus to the triggering image link. |
| JavaScript disabled | Both complete static language pages remain navigable. All gallery figures, downloads and native FAQ disclosures remain available; language links continue working. A FAQ was opened with the keyboard while scripts were disabled. |
| Appearance preference | Manual appearance persists between locale pages. The initial theme follows the system unless a saved choice exists. Unavailable browser storage is handled without blocking the page. |
| Accessibility review | Semantic headings, meaningful image descriptions, visible focus, roving gallery-tab focus and modal focus behavior were inspected. A dark Windows-panel contrast issue and the original mobile focus order were corrected. Reduced-motion CSS disables animation, transitions and smooth scrolling. This is not a full assistive-technology certification. |
| Assets and dependencies | Five supplied app captures were converted to responsive WebP assets; the full-resolution versions are lossless. The original first screenshot is used for social sharing. No stock photographs, fabricated screenshots, external font service, framework, analytics or live release-API request is required. |

## Remaining publishing actions

The active GitHub connection reported `pull: true` and `push: false`; repository metadata reported Pages was not yet enabled. No branch, commit, pull request, release, repository setting or DNS record was changed. The ZIP is an additive package for the existing checkout.

Someone with the appropriate repository access must add the files, select **Settings → Pages → GitHub Actions**, and merge/run the workflow on `main`. The actual hosted deployment and certificate provisioning cannot be verified until those actions occur. Custom-domain setup instructions are in `website-docs/README.md`.

No required visual assets are missing. The Oromo translation is complete and integrated, but has not received an independent fluent-speaker editorial review; a wording review is recommended before a broad public launch. The application’s own beta qualification and signing limitations remain as stated in its existing public documentation.

## Reproduce the static checks

```bash
python3 scripts/localize_site.py --check
python3 scripts/prepare_site.py
python3 scripts/check_site.py _site
```

Optional JavaScript syntax checks during development:

```bash
node --check website/theme.js
node --check website/app.js
```

Node.js is not needed to host or use the site.

## Deployment preparation — 8 November 2026

The owner-supplied ZIP was integrated into the public release repository without replacing existing releases, issue templates or user guides. The developer section now uses official compact light/dark AndHub artwork, the shortened company name, and company website, general email, two telephone links and office location from the published brand context. Logo geometry, proportions and colors are preserved; the accessible SVG title uses the requested company name.

The localization consistency check and prepared-site validator pass for both languages. Nineteen allowlisted files are staged; runtime assets and language links work below the repository path. The reviewed beta.8 Windows, two Mac and Ubuntu installer names match the current release inventory. JavaScript syntax and secret scans pass.

Chromium verification covers English and Afaan Oromo at 375×900, 844×390 landscape and 1440×1000, in light and dark appearance (12 layouts). Each checks the four company contact links, one correctly loaded theme-specific logo, preserved logo proportions, no horizontal overflow and no About-section axe violations. Actual keyboard navigation shows the logo link's focus outline. No page errors or failed requests occurred. Two additional mobile journeys disable JavaScript, verify the dark system-theme logo and contact links, and navigate to the other language. Desktop/light and mobile/dark About screenshots were visually reviewed; private QA captures are not included in the deployed artifact.

The initial deployment uses GitHub Pages' default HTTPS project address. No custom domain or DNS record is configured by this change. Independent fluent review and existing application/platform qualification limits remain open.

Published result: [deployment 42482600224](https://github.com/1hubengineering/afaan-oromo-bible-releases/actions/runs/42482600224) passed at website commit `05677a4f85fd671eb8476b35a18ec970ff041d85`. Anonymous requests to both language pages, the two logo SVGs, CSS and both JavaScript files return HTTP 200 and match the prepared content after line-ending normalization. A live Chromium mobile check in each language verifies contact links, absence of the removed company suffix, decoded logo assets and light-to-dark switching. Public website: https://1hubengineering.github.io/afaan-oromo-bible-releases/; Afaan Oromoo: https://1hubengineering.github.io/afaan-oromo-bible-releases/om/.

## Custom domain activation — 8 November 2026

The owner configured `bible.1hubengineering.com` in GitHub and its Porkbun CNAME. Public DNS confirms the target `1hubengineering.github.io`. After GitHub approved the certificate, HTTPS enforcement was enabled and [deployment 42484165828](https://github.com/1hubengineering/afaan-oromo-bible-releases/actions/runs/42484165828) succeeded. The repository homepage and current documentation use https://bible.1hubengineering.com/ and its `/om/` language page.

## Search discovery and accessibility — 8 November 2026

Added reciprocal language sitemap entries, an allow-crawl robots file, localized search/share titles, explicit image-preview policy and static organization/website/page/application schema. The app metadata preserves beta/experimental-platform scope and contains no invented prices, ratings or accessibility certifications. A shared 1280×640 image uses the existing authorized reader screenshot and website typography; its PNG is 120,989 bytes, compared with the previous 229,317-byte screenshot. Search verification and GitHub's separate UI-only repository social-preview setting are documented honestly in [SEO.md](SEO.md).

The baseline whole-page axe audit found `aria-allowed-role` violations because JavaScript assigned `tabpanel` to a figure. The gallery now gives the role to a generic container and preserves a nested semantic figure/caption. A focusable main target makes native skip navigation explicit. A linked accessibility statement and public issue template explain keyboard use, fallback behavior and private-data precautions.

Four metadata unit checks pass: locale/domain reference integrity, safe JSON/script escaping, rejection of missing/wrong-language/duplicate metadata, and preservation of beta scope without invented claims. Custom-root and GitHub-project staging both pass page, asset, release-link, crawl-file, reciprocal sitemap and structured-data checks. The validator checks the real PNG dimensions and size. Twenty-one allowlisted files are staged. JavaScript syntax, diff and secret checks pass.

Chromium passes 16 rendered layouts: English/Oromo, light/dark, at 320, 375, 844 landscape and 1440 CSS pixels. Each verifies skip-link focus, all screenshot tab states and Home/End navigation, modal Escape/focus return, static localized schema, no horizontal overflow and a full-page axe check with FAQs expanded. At mobile/desktop widths, 32 additional visible gallery-state axe checks pass. No violations were reported across these 48 runs (WCAG 2 A/AA, 2.1 AA, 2.2 AA and axe best-practice tags). Two separate no-JavaScript journeys verify main focus, all four visible screenshots, static metadata and ordinary language links. The no-JavaScript journeys use functional/DOM checks; the injected axe engine requires script execution. The sharing card and mobile gallery were visually reviewed. Manual screen-reader testing and independent fluent review remain open.

Prepared custom-domain output passes both-language asset/link/metadata/download checks. Both live HTML pages, the two logo SVGs, CSS and JavaScript return HTTP 200 and match the newly prepared files after line-ending normalization. HTTP and the original GitHub Pages URL redirect to the custom HTTPS root. Live mobile Chromium checks in both languages confirm the canonical/social URL, language navigation, four contact links and decoded logo. This workstation temporarily cached an earlier nonexistent DNS answer, so live checks used GitHub's publicly resolved origin address with the real hostname and full TLS verification; certificate checks were not bypassed. No website UI, application code, download artifacts or DNS records changed during this activation.
