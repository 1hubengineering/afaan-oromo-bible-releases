# Afaan Oromo Bible website

A small, static product and download page for the desktop reader. It uses HTML, CSS and a little JavaScript; it has no framework, package installation, database or build-service dependency. Python 3 is used only for previewing, maintaining the translated page, validating and preparing the deployment artifact.

The feedback update adds a native dialog and lazy Tally iframe, with CTAs in navigation, downloads, Help and the existing developer/feedback areas. The connected plugins created and configured real forms: English is published, and an imported setup test plus a fresh embedded submission verify private Google Sheets synchronization. Afaan Oromoo remains a draft pending fluent review, publication and connection. Their IDs are in `website/feedback-config.js`, with Oromo embedding gated off. Google Drive created the private workbook, field map and review structure; the owner saved Tally's English authorization. Follow the [setup guide](FEEDBACK.md) for the remaining steps. The form requires JavaScript and internet; other static content remains available without JavaScript. [Current validation](VALIDATION.md#tally-and-google-drive-plugin-follow-up--8-november-2026) distinguishes real checks from transport fixtures. The website is not deployed. The current brief identifies the developer and maintainer as AndHub Engineering PLC, superseding the earlier shortened company-name preference described in the historical delivery notes below.

The website includes **English and Afaan Oromo pages**, with ordinary language links between them. It introduces the current **0.1.0-beta.8** release, with the Windows beta distinguished from the experimental macOS and Linux packages. An About section identifies the developer and maintainer as AndHub Engineering PLC and includes official compact light/dark logo artwork, the company website, general email, telephone numbers and office location.

## Add it to the release repository

Copy these additions into the root of the existing `1hubengineering/afaan-oromo-bible-releases` checkout:

| Path | Purpose |
| --- | --- |
| `website/index.html` | The complete English page. |
| `website/om/index.html` | The complete, committed Afaan Oromo page. |
| `website/styles.css`, `website/theme.js`, `website/app.js` | Shared appearance and small interactive enhancements for both languages. |
| `website/feedback-config.js`, `website/feedback.js` | Public form configuration and accessible lazy feedback embedding; no credentials or backend. |
| `website/assets/` | Shared authorized screenshots, favicon and social-sharing image. |
| `.github/workflows/deploy-website.yml` | Validation and GitHub Pages deployment. |
| `scripts/prepare_site.py` | Copies only allowed website files into a publication directory. |
| `scripts/check_site.py` | Checks local assets, anchor targets, metadata and the beta.8 download inventory. |
| `scripts/site_metadata.py`, `scripts/test_site_metadata.py` | Static localized search/schema metadata and integrity tests. |
| `website/robots.txt`, `website/sitemap.xml` | Crawl policy and reciprocal English/Oromo discovery URLs. |
| `scripts/localize_site.py` | Maintains the committed static Afaan Oromo page from the English page and translation catalog. |
| `website-docs/` | Website documentation and `oromo-translations.json`; not deployed. |

Merge directories when copying; do not replace the repository's `.github` directory. The existing issue templates, README, licensing, guides and releases remain in place. Make sure the hidden `.github` directory is included when extracting or copying the package. Do not upload the ZIP itself as the website.

Review and commit only the additions. For example, from the existing checkout:

```bash
git switch -c website/download-page
git add website .github/workflows/deploy-website.yml scripts/prepare_site.py scripts/check_site.py scripts/localize_site.py website-docs
git diff --cached --stat
git commit -m "Add the Afaan Oromo Bible download website"
git push -u origin website/download-page
```

Open a pull request, review its checks, and merge it into `main` when ready to publish. Generated `_site/`, `_preview/`, Python caches and local QA captures do not need to be committed. The private application repository and proprietary UI packages are not part of this package or workflow.

## Local preview

From the repository root, with Python 3 installed:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory website
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for English or [http://127.0.0.1:8000/om/](http://127.0.0.1:8000/om/) for Afaan Oromo. On Windows, use `py -3` in place of `python3` if that is your installed launcher. Stop the server with **Ctrl+C**.

No Node.js installation is required. Both language pages are committed HTML and can be served immediately; translation does not depend on JavaScript or a runtime translation service. Downloads remain ordinary links to the public GitHub release. The website does not fetch a release API at runtime, so a GitHub API rate limit cannot hide the download buttons.

### Validate the deployment output

```bash
python3 scripts/localize_site.py --check
python3 scripts/prepare_site.py
python3 scripts/check_site.py _site
```

The localization check verifies that the committed Oromo page matches the current English source and translation catalog. The preparer rejects symbolic links and unexpected files, recreates `_site/` from `website/`, and injects static localized JSON-LD into the prepared HTML. Crawl files and all metadata use the configured HTTPS site URL. Only explicit website file types, `om/index.html` and approved asset paths are published. It does not copy the repository root, app source, guides, translation catalog, installers or personal data. If a new type of public asset is needed, deliberately update the allowlist in `prepare_site.py`. See [SEO.md](SEO.md) for topics, metadata, sharing artwork and search-engine verification, and [the accessibility statement](../ACCESSIBILITY.md) for user guidance.

### Preview at the GitHub project path

To reproduce hosting below a repository name, stop any existing preview server and run:

```bash
python3 scripts/prepare_site.py --output _preview/afaan-oromo-bible-releases
python3 scripts/check_site.py _preview/afaan-oromo-bible-releases
python3 -m http.server 8000 --bind 127.0.0.1 --directory _preview
```

Open [http://127.0.0.1:8000/afaan-oromo-bible-releases/](http://127.0.0.1:8000/afaan-oromo-bible-releases/) and switch to Afaan Oromo, or open its `/om/` child path directly. All runtime asset and language links are relative, so the same website works at the repository path and at the root of a custom domain.

## Enable GitHub Pages

1. In the public release repository, open **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Merge the website additions into `main`. If they are already merged, open **Actions → Deploy website to GitHub Pages → Run workflow**, selecting `main`.
4. Wait for both the validation/package job and the deployment job to succeed. The deployment's `github-pages` environment shows the published URL.

The website is live at [https://bible.1hubengineering.com/](https://bible.1hubengineering.com/), with [Afaan Oromoo at `/om/`](https://bible.1hubengineering.com/om/). Initial deployment [42482600224](https://github.com/1hubengineering/afaan-oromo-bible-releases/actions/runs/42482600224) passed on 8 November 2026 at website commit `05677a4f85fd671eb8476b35a18ec970ff041d85`. GitHub approved the custom-domain certificate and HTTPS enforcement is enabled. [Custom-domain deployment 42484165828](https://github.com/1hubengineering/afaan-oromo-bible-releases/actions/runs/42484165828) passed; the original GitHub Pages URL redirects to the custom domain.

The workflow runs when website-related files, the localization script or the translation catalog change on `main`. It checks the committed Oromo page before staging both languages. Pull requests receive validation only; they cannot deploy. A manual run on a branch other than `main` also validates without deploying. The build job has read-only repository/Pages permissions; only the deployment job has `pages: write` and `id-token: write`. No personal access token or other manually supplied secret is required. Official GitHub actions are pinned to the commit SHAs resolved from their current major-version tags on 8 November 2026.

The workflow intentionally does not enable Pages or change repository settings. That first setting must be made by someone with permission to manage the repository. If the configuration step reports that Pages is unavailable, verify the source setting above, then rerun it. Repository or organization policies may also require approving the deployment environment or allowing the pinned official actions.

## Custom domain configuration

The current custom domain is `bible.1hubengineering.com`. The owner configured it in GitHub Pages and added the `bible` CNAME in Porkbun; GitHub's certificate is approved and HTTPS is enforced. These steps document the configuration for maintenance.

1. Verify the domain in GitHub if appropriate for your account, then enter the exact chosen subdomain in **repository Settings → Pages → Custom domain** and save it.
2. At your DNS provider, create the corresponding CNAME record. For the example above:

   | Type | Name | Target |
   | --- | --- | --- |
   | CNAME | `bible` | `1hubengineering.github.io` |

3. After GitHub validates DNS and provisions the certificate, enable **Enforce HTTPS**.
4. Run **Deploy website to GitHub Pages** again on `main` after the custom domain is configured.

The CNAME target contains **no repository path**. With this custom Actions workflow, GitHub reads the domain from Pages settings; a repository `CNAME` file is not required. At deployment, `configure-pages` supplies the actual site URL and `prepare_site.py` updates both pages' canonical URLs, alternate-language URLs and social-image URLs in the generated output. Source files remain unchanged. English remains at the site root and Afaan Oromo at `/om/`.

To inspect this metadata change locally without changing DNS:

```bash
python3 scripts/prepare_site.py --site-url https://bible.1hubengineering.com/
python3 scripts/check_site.py _site
```

## Content and assets

The five screenshots came from the supplied beta.8 capture package. They show the installed application using an isolated demo profile. Note titles, text and bookmark labels are illustrative demo material, not personal records. Website assets are optimized versions of these genuine captures; they should not be described as screenshots of future features.

The site uses a small book symbol and system fonts. No publisher or Bible Society logo, stock religious photograph, fabricated app screen or proprietary component library is required. The existing [licensing notice](https://github.com/1hubengineering/afaan-oromo-bible-releases/blob/main/LICENSING.md) remains authoritative for application and Scripture content; adding website files does not relicense the application or the Bible editions.

The initial copy identifies **gaz 2022 (Western Oromo), OOCS 2024 and King James Version**. Keep licensing and independence language intact. NIV and the planned 1997 edition are not advertised as available. Windows is an unsigned beta; Mac and Linux packages are experimental, with ad-hoc, unnotarized Mac builds and unsigned Linux packages.

### Updating a release

1. Verify the new release and its exact published asset names on GitHub.
2. Update the version, links, platform notes and any sizes shown in `website/index.html`, then update the translation catalog and regenerate the Oromo page.
3. Update the explicit release/download inventory in `scripts/check_site.py`.
4. Review the public installation, licensing, privacy, security and testing documents for changed claims.
5. Run the checks and repeat the relevant browser checks before merging.

Do not switch to unverified `latest` download URLs: they could silently mismatch the version or qualification level described on this page. The automated script checks the reviewed URL inventory and local files without making network requests; it does not download or execute installers.

### Maintaining the Afaan Oromo page

English copy is ordinary semantic HTML, with stable `data-i18n` markers for translation. `website-docs/oromo-translations.json` stores the Oromo copy and attribute replacements; `scripts/localize_site.py` produces the committed `website/om/index.html` page. The generated page uses `lang="om"`, its own canonical URL and alternate-language metadata. Both pages share the same CSS, images and JavaScript, whose small label dictionary follows the document language.

After editing English copy, update the corresponding catalog entries, regenerate the Oromo page, then check it:

```bash
python3 scripts/localize_site.py
python3 scripts/localize_site.py --check
python3 scripts/prepare_site.py
python3 scripts/check_site.py _site
```

Commit the source, catalog and generated page together. Direct edits to the generated Oromo HTML will be overwritten the next time it is generated. Review translations for navigation, FAQs, download notices, screenshot descriptions, accessibility labels, metadata and interactive labels together so neither language falls behind.

The Afaan Oromo copy is included, but independent review by a fluent Oromo editor has not been completed. A language review should confirm natural wording, edition terminology and the important beta/installation disclosures before broad promotion. The site's language selection is independent of the application's existing interface-language setting.

## Validation and operational limits

The automated checks cover both languages: missing local assets, repository-path-safe URLs, native language navigation, duplicate IDs, broken anchor/ARIA references, image dimensions/alternative-text attributes, locale/social metadata, required public document links and the four reviewed installer URLs. They also reject unexpected files in the staged publication directory.

After design or interaction changes, check both languages at mobile, tablet and desktop widths; light and dark appearance; menu and screenshot-dialog keyboard operation; visible focus; reduced motion; a browser with JavaScript disabled; and root plus repository-subpath hosting. These checks complement one another: the static script does not certify linguistic accuracy, visual accessibility or operating-system installers.

The website adds no analytics or tracking scripts. Its appearance preference is stored locally in the browser when storage is available. Hosting and download requests are handled by GitHub and remain subject to GitHub's policies.

## Source references

- [Beta.8 release and asset inventory](https://github.com/1hubengineering/afaan-oromo-bible-releases/releases/tag/v0.1.0-beta.8)
- [Installation instructions](https://github.com/1hubengineering/afaan-oromo-bible-releases/blob/main/INSTALLATION.md)
- [Testing guide](https://github.com/1hubengineering/afaan-oromo-bible-releases/blob/main/TESTING_GUIDE.md)
- [User guide](https://github.com/1hubengineering/afaan-oromo-bible-releases/blob/main/USER_GUIDE.md)
- [Licensing](https://github.com/1hubengineering/afaan-oromo-bible-releases/blob/main/LICENSING.md), [privacy](https://github.com/1hubengineering/afaan-oromo-bible-releases/blob/main/PRIVACY.md), and [security](https://github.com/1hubengineering/afaan-oromo-bible-releases/blob/main/SECURITY.md)
- [GitHub: custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [GitHub: custom-domain setup](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

## Brand and contact source

The About section uses the current compact logo artwork and company contact details from [AndHub brand resources](https://brand.1hubengineering.com/) and its [machine-readable brand context](https://brand.1hubengineering.com/assets/ai/brand-context.json), inspected on 8 November 2026. The initial delivery shortened the company name. The subsequent refinement brief restores **AndHub Engineering PLC** in the About copy; the official logo artwork stays intact. Only the SVG accessible title was shortened; logo paths, colors and proportions are unchanged. Separate official light/dark variants follow the website appearance, including the no-JavaScript system-theme fallback. The company website is https://1hubengineering.com/, email is info@1hubengineering.com, telephone numbers are +251913231123 and +251922964576, and the published office location is Lebu, Addis Ababa, Ethiopia. Both static language pages share these contact links. The initial deployment used GitHub’s default address; the subsequent custom-domain setup is documented above.
