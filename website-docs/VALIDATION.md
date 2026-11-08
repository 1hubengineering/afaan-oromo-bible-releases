# Delivery validation

Prepared on 8 November 2026 for `1hubengineering/afaan-oromo-bible-releases`.

## Compact website refinement — 9 November 2026

Published at [bible.1hubengineering.com](https://bible.1hubengineering.com/) and [/om/](https://bible.1hubengineering.com/om/) from website commit `1239e23d2733acab8c40ab5116c1e3916a567208`. [Pages run 42524469516](https://github.com/1hubengineering/afaan-oromo-bible-releases/actions/runs/42524469516) passed validation/package and publication. Nine live text assets match the prepared output. Eight live layouts (English/Oromo × light/dark × 375/1440px) pass with no horizontal overflow, page error or checked axe violation. Both real localized Tally forms load and reveal a conditional question; closing returns focus to the CTA. No additional submission was sent during these live deployment checks. Private evidence: `refinement-deployment-verification.json` and companion captures, excluded from publication.

The simplified source uses outlined EN/OR language controls, four navigation links with one Download button, and three separate feedback CTA buttons (hero, downloads, Help). A proportionate desktop monitor sits beside the hero on desktop and below the text on mobile. The gallery shows four thumbnails in one desktop row, two columns on smaller screens, and uses the existing native image dialog for enlargement. Screenshot tabs and their controller were removed. The warm cream, cedar and amber palette includes dark and CSS-only system variants. No runtime dependency, backend, analytics or external asset service was added.

Repeated benefits, decorative feature footnotes, verbose gallery headings and the standalone feedback section were consolidated. Edition credits and licensing remain in an expandable native section under the features; the beta, platform qualification, installation, privacy and edition notices remain intact. Compared with the previous committed site, default collapsed pages at 1440px are 48% shorter in English (7391 → 3848px) and 46% shorter in Oromo (7508 → 4057px). At 375px the reductions are 23% and 25%. These are rendered document heights, not claims about reading speed.

Local checks completed:

- `python3 scripts/localize_site.py --check`, four metadata unit checks, JavaScript syntax and `git diff --check` pass.
- `prepare_site.py` and `check_site.py` pass for the custom-domain root and GitHub project subpath. Each artifact contains 23 allowlisted public files, both complete static pages, and the unchanged four verified beta.8 installer links.
- Chromium passes 24 root layouts: English/Oromo × light/dark × 320, 375, 768, 844 landscape, 1280 and 1440 CSS pixels. Each exercises all three feedback CTAs with the unavailable-state fixture, modal background inertness, focus return, Escape, mobile navigation, all four screenshot dialogs and theme persistence. All screenshots remain visible together; the desktop row and responsive hero geometry are asserted. Expanded FAQs and modal states report zero axe violations for the checked WCAG 2 A/AA, 2.1 AA, 2.2 AA and best-practice rules. This is automated evidence, not an accessibility certification.
- Two transport-only journeys test delayed/blocked Tally requests, retry, late-ready recovery, trusted lifecycle messages, confirmation focus and exclusion of host query parameters. They do not submit a real form. Two script-disabled journeys verify language navigation, all four visible gallery images and the email fallback. CSS-only dark appearance and keyboard opening of edition details also pass. Header controls retain 44px targets, including the narrow-screen follow-up after the final size adjustment.
- The real English and Oromo Tally embeds each load on mobile/dark (375px) and desktop/light (1440px). All five conditional categories reveal their own questions and hide the other branches without horizontal overflow. A single clearly labeled Oromo setup test, with no contact details, was submitted through the actual embed. Tally accepted it; the parent showed the Oromo confirmation and focused its heading. Connector read-back confirms one completed Oromo submission and no partial submissions. No English submission was added during this refinement.

Oromo was published at the owner's request, independently of fluent approval. Questions, category options, editable instructions, submit text and confirmation are translated. Fluent review remains outstanding. [Tally's supported system-language list](https://tally.so/help/supported-languages), rechecked on 9 November, still lacks Oromo; some validation/upload controls remain English, as disclosed in the dialog and form. The embed has a fixed warm light palette inside either website theme. English Google Sheets delivery was verified previously. Oromo's separate account authorization and Sheet delivery remain outstanding; Tally acceptance alone does not establish synchronization. Attachment delivery and manual assistive-technology checks are not certified.

The repository-subpath rerun passes eight additional layouts (both languages and themes at 375/1440px), the transport failure/confirmation checks and both script-disabled language journeys. No horizontal overflow or checked axe violation was reported. The final narrow-screen follow-up verifies all header controls are at least 44px and that edition details open by keyboard without overflow. Website secret scanning reports no leaks; a separate source search finds no private spreadsheet URL, Google API key or private-key marker in website assets, website documentation or scripts.

Local evidence is stored outside publication in `.tooling/website-feedback-20261108/`, with root/subpath matrices in the public checkout's ignored `_preview/refinement-full-qa/results.json` and `_preview/refinement-subpath-qa/results.json`. A preview-server race during a staging rebuild interrupted the first subpath run; the private harness was corrected to read bytes before sending headers and the successful rerun used the completed artifact. Deployment results are recorded below after verification.

## Feedback website deployment — 8 November 2026

Published at [bible.1hubengineering.com](https://bible.1hubengineering.com/), with [Afaan Oromoo at `/om/`](https://bible.1hubengineering.com/om/), from website commit `777fb503da62911d01b9d2e4729461c91c919357`. [Pages run 42495675061](https://github.com/1hubengineering/afaan-oromo-bible-releases/actions/runs/42495675061) passed both validation/package and publication jobs. The existing custom domain, HTTPS enforcement, deployment workflow and release downloads are preserved.

Nine live text assets match the locally prepared output after line-ending normalization: both HTML pages, CSS, theme/app/feedback/config scripts, robots and sitemap. Live Chromium checks passed eight layouts (English/Oromo, light/dark, 375/1440px). They verify localized canonicals, all six CTAs, real English Tally loading and conditional questions, Oromo's translated email fallback, modal focus return, decoded reader artwork, no horizontal overflow and no page errors. All eight closed-page axe audits reported zero violations for the checked WCAG/best-practice tags. TLS verification remained enabled, and the workstation's normal DNS resolved the domain.

English's previously verified private Google Sheets connection is configured in the published embed. No additional submissions were sent during deployment checks. Oromo stays gated until fluent review, publication and its separate Sheets connection; deployment does not certify those outstanding steps. The earlier “not deployed” statements below describe their historical checkpoints. Local live-deployment evidence is `.tooling/website-feedback-20261108/deployment-verification.json` and its companion captures, excluded from publication.

## Tally and Google Drive plugin follow-up — 8 November 2026

The owner connected Tally and requested Google Drive use after the local implementation. This supersedes earlier notes about empty IDs and no account access; the website itself remains undeployed.

- Created real English (`vXrgVQ`) and Afaan Oromoo (`KpeOA7`) forms in the sole connected Tally workspace. Each form's read-back confirms 19 questions, five category SHOW rules, five optional fields (correction, reproduction steps, screenshot, name and email), matching edition/OS options, privacy/review notices and a custom thank-you page. No unnecessary branch, calculated-field system, respondent login, password, payment or email notification was added.
- Applied the website's ivory, forest text and green button colors through Tally's supported appearance settings. English system messages are used because the plugin has no Oromo system-language option. Oromo editable content is translated but remains unreviewed.
- Published English at https://tally.so/r/vXrgVQ. Oromo remains an unpublished draft at https://tally.so/forms/KpeOA7/edit, with its website review gate false. Both real IDs are in `website/feedback-config.js`.
- Verified the actual English iframe on a locally served prepared website at desktop/light (1280px) and mobile/dark (375px). All five categories reveal their own questions and hide other branches, the real `Tally.FormLoaded` message clears the loading status, and neither the frame nor website overflows horizontally in these checks.
- Sent two clearly labeled setup tests through the actual English embed, with name/email blank: general feedback before connection and a website issue after connection. In each case the actual `Tally.FormSubmitted` message triggered the website confirmation and focused its heading. Tally read-back and the response Sheet identify the accepted submissions; no optional contacts were entered.
- Created **Afaan Oromo Bible — Private Feedback Review** using Google Drive. Initial and final read-back confirm `shared: false`, with only owner permission. Tally writes to its generated `Afaan Oromo Bible — Share Feedback (English)` tab. `Feedback EN` is a native formula view of those real rows with readable UTC timestamps. `Feedback OM` is reserved for the reviewed form's future connection. `Setup`, bilingual `Field Map` and the empty `Review` tab explain the workflow. Review has canonical headers and status/priority dropdowns; these are reviewer-owned, not automatically populated by Tally. The private workbook URL is shared only in the owner's chat, not public source or the source ZIP.
- The owner saved the English Google Sheets authorization in Tally's dashboard because neither plugin can save that connection. **Actual synchronization is verified:** the existing setup test was imported, and a new test submitted after connection arrived automatically. Read-back matched submission IDs, UTC timestamps, categories, affected page and description, with optional contacts empty. No response row was manually inserted to stand in for synchronization. Both tests remain clearly labeled in the actual service and Sheet. Oromo still needs review, publication and connection.

The unavailable-state browser matrix now overrides configuration in its test browser so it remains reproducible after real IDs are configured. An additional eight-layout regression plus transport/no-JavaScript checks passed after this configuration change, with no checked axe violations. Fixture tests still prove only mechanics. The separate real-English checks above use the actual service and no intercepted form. Local evidence is retained under the ignored `.tooling/website-feedback-20261108` directory, including the live event/submission reports and desktop/mobile captures. Real screenshot uploads, completed submissions in all categories, Oromo rendering/submission, manual assistive-technology checks and website publication remain open.

## Feedback and UI refinement — 8 November 2026

This checkpoint supersedes the historical copy, file counts and company-name preferences below. Changes are local to the public website checkout; **no deployment, real Tally submission or Google Sheets connection was performed**.

The site retains its existing ivory/forest/gold palette, serif headings, authorized screenshots, edition attributions, installer links and beta disclosures. Review using the humanizer and ui-ux-pro-max skills led to these changes:

| Finding | Change |
| --- | --- |
| Feedback required a public GitHub issue/account | Six feedback entry points open one native modal; each locale uses its own public Tally configuration. Empty/unreviewed configuration displays an email alternative. |
| Small mobile body text and dense feature columns | Key mobile prose and FAQs now use 16px text, with a single feature column, readable line spacing and wrapping for long Oromo labels. |
| Crowded navigation and small links | Collapsed-menu breakpoint accommodates longer text; important controls/links have 44px targets. Feedback is emphasized in navigation and downloads without replacing the primary Download action. |
| Vague or repetitive marketing copy | Shorter hero, feature, download, Help and feedback wording. Gallery copy now accurately identifies English beta controls and pending Oromo interface review. |
| Developer role needed clarification | About identifies AndHub Engineering PLC as the developer and maintainer, explains its software/systems/consultancy work, and preserves independence and contact details. |
| Embedded form failures and privacy needed clear handling | On-demand iframe, status messages, a direct-form link above the embed, delayed/blocked-load recovery, retry and a trusted-event confirmation. Optional contacts, privacy and edition-review notices are bilingual. No answer storage, query-string forwarding, analytics or backend was added. |

Completed checks on Windows with Node 24.19.0, Python 3.14 and the existing Playwright/axe installation:

- Localization generation and `--check` pass. JavaScript syntax checks and `git diff --check` pass.
- Four existing metadata unit tests pass. Both custom-domain and project-subpath artifacts pass the static validator: 23 allowlisted files, valid assets/anchors/ARIA/localized metadata and all four unchanged beta.8 installer links.
- Chromium passes 24 root-hosted layouts: English/Oromo, light/dark, at 320, 375, 768, 844 (390px-high landscape), 1280 and 1440 CSS pixels. Eight additional project-subpath layouts pass at 375 and 1440 in both languages/themes. These cover all six CTAs, modal background inertness, focus return, shell Escape, menu focus, gallery keyboard behavior, appearance persistence, no horizontal overflow, and whole-page/modal axe checks with FAQs expanded. No checked axe violations or page errors were reported. The layout runs use reduced-motion emulation.
- In both hosting modes, separate configured-transport checks pass for both locales: lazy iframe creation, correct locale routing, loading, 15-second delayed state, late readiness, retry, blocked network requests, direct fallback URL, malicious-origin/wrong-window/wrong-form message rejection, confirmation focus and iframe cleanup. After moving the direct fallback above the embed, the affected configured checks were rerun successfully. These use intercepted **test-only message fixtures**, never a fake production form; they do not demonstrate a real successful Tally submission or a Sheet row.
- Four no-JavaScript journeys pass across the two hosting modes: email fallback, all four screenshots visible and ordinary static language links.
- Desktop/light and Oromo/mobile/dark captures were visually inspected. Configured captures contain an unmistakable transport-test page, not a representation of a real form.

Chromium does not propagate Escape from within a cross-origin iframe to the parent dialog. The fixture checks demonstrate leaving it with Shift+Tab, reaching Close and closing with Escape. The sticky Close button stays available, the dialog includes the alternative keyboard instruction, and backdrop clicks do not discard work. Repeat keyboard/screen-reader checks in the actual Tally forms because their fields and validation can change behavior. Native dialogs may also let keyboard focus visit browser chrome at a boundary; background page controls remain inert.

Still required: real form creation/publishing, fluent Oromo review, acceptance of English Tally system/validation messages, private Google Sheets connection and row/attachment verification, live conditional-question and submission tests, real mobile/file-upload checks, browser zoom/manual assistive-technology checks and Pages publication verification. Tally’s cross-origin form retains a neutral light surface within the themed shell. The website cannot independently guarantee the form’s internal dark-mode appearance. See [the setup and launch checklist](FEEDBACK.md).

QA JSON and PNG captures are retained only in local `_preview/feedback-qa`, `_preview/feedback-subpath-qa` and `_preview/feedback-transport-qa` directories, excluded from the website publication allowlist.

### Reproduce feedback browser checks

The optional `scripts/test_feedback.mjs` uses Playwright and axe for development only. This workspace reuses the already installed packages; nothing was added to the website’s runtime or Pages workflow. In a separate QA directory, install `@playwright/test` and `@axe-core/playwright` and the matching Chromium if they are not already available. Set `AOB_QA_DIR` to that directory so the script resolves its packages there. Without it, normal Node module resolution is used. Host the prepared artifact first:

```sh
python3 scripts/prepare_site.py --site-url https://bible.1hubengineering.com/
python3 -m http.server 8770 --bind 127.0.0.1 --directory _site
```

In another terminal, from the website repository:

```sh
node scripts/test_feedback.mjs
```

For project-path checks, prepare `_preview/afaan-oromo-bible-releases`, serve `_preview` on port 8771, set `AOB_SITE_URL=http://127.0.0.1:8771/afaan-oromo-bible-releases/` and `AOB_QA_OUTPUT=_preview/feedback-subpath-qa`, then run `node scripts/test_feedback.mjs --subpath-smoke`. In PowerShell set these with `$env:AOB_SITE_URL='…'` and `$env:AOB_QA_OUTPUT='…'`. The `--transport-only` flag reruns affected configured mechanics without repeating the layout matrix. Test routing overrides configuration in the browser only; it never writes fixture IDs to website source.

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

Published at website commit `37786138cabfe1d588cd12e0364b4d7c26b96fa5`; [deployment 42486719568](https://github.com/1hubengineering/afaan-oromo-bible-releases/actions/runs/42486719568) passes validation, the four metadata checks, packaging and Pages publication. Live verification matches ten public files to prepared output (both pages, crawl files, sharing image, CSS/JavaScript and developer logos); each returns HTTP 200. Both live mobile language pages pass the checked axe rules, expose the new schema and preserve skip/tab navigation. The public About description/homepage and all 19 topics match the reviewed metadata. Public DNS resolves the correct GitHub origin; this environment's default resolver still failed to resolve the custom hostname, so live requests used that independently verified origin with full TLS hostname/certificate validation.

Added reciprocal language sitemap entries, an allow-crawl robots file, localized search/share titles, explicit image-preview policy and static organization/website/page/application schema. The app metadata preserves beta/experimental-platform scope and contains no invented prices, ratings or accessibility certifications. A shared 1280×640 image uses the existing authorized reader screenshot and website typography; its PNG is 120,989 bytes, compared with the previous 229,317-byte screenshot. Search verification and GitHub's separate UI-only repository social-preview setting are documented honestly in [SEO.md](SEO.md).

The baseline whole-page axe audit found `aria-allowed-role` violations because JavaScript assigned `tabpanel` to a figure. The gallery now gives the role to a generic container and preserves a nested semantic figure/caption. A focusable main target makes native skip navigation explicit. A linked accessibility statement and public issue template explain keyboard use, fallback behavior and private-data precautions.

Four metadata unit checks pass: locale/domain reference integrity, safe JSON/script escaping, rejection of missing/wrong-language/duplicate metadata, and preservation of beta scope without invented claims. Custom-root and GitHub-project staging both pass page, asset, release-link, crawl-file, reciprocal sitemap and structured-data checks. The validator checks the real PNG dimensions and size. Twenty-one allowlisted files are staged. JavaScript syntax, diff and secret checks pass.

Chromium passes 16 rendered layouts: English/Oromo, light/dark, at 320, 375, 844 landscape and 1440 CSS pixels. Each verifies skip-link focus, all screenshot tab states and Home/End navigation, modal Escape/focus return, static localized schema, no horizontal overflow and a full-page axe check with FAQs expanded. At mobile/desktop widths, 32 additional visible gallery-state axe checks pass. No violations were reported across these 48 runs (WCAG 2 A/AA, 2.1 AA, 2.2 AA and axe best-practice tags). Two separate no-JavaScript journeys verify main focus, all four visible screenshots, static metadata and ordinary language links. The no-JavaScript journeys use functional/DOM checks; the injected axe engine requires script execution. The sharing card and mobile gallery were visually reviewed. Manual screen-reader testing and independent fluent review remain open.

Prepared custom-domain output passes both-language asset/link/metadata/download checks. Both live HTML pages, the two logo SVGs, CSS and JavaScript return HTTP 200 and match the newly prepared files after line-ending normalization. HTTP and the original GitHub Pages URL redirect to the custom HTTPS root. Live mobile Chromium checks in both languages confirm the canonical/social URL, language navigation, four contact links and decoded logo. This workstation temporarily cached an earlier nonexistent DNS answer, so live checks used GitHub's publicly resolved origin address with the real hostname and full TLS verification; certificate checks were not bypassed. No website UI, application code, download artifacts or DNS records changed during this activation.
