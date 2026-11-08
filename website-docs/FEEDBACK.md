# Feedback setup: Tally and private Google Sheets

Two real forms have now been created through the connected Tally plugin. The [English form](https://tally.so/r/vXrgVQ) is published, and the [Afaan Oromoo form](https://tally.so/forms/KpeOA7/edit) is a draft pending fluent review. Both have 19 questions, five conditional category rules, optional name/email, optional correction/reproduction/screenshot fields, privacy notices and a custom thank-you page. The public form IDs are configured locally; Oromo embedding remains gated by `copyReviewed: false`.

Google Drive was used to create **Afaan Oromo Bible — Private Feedback Review**. The owner then authorized Tally's English Google Sheets connection. **English synchronization is verified:** the earlier setup test was imported, and a fresh test submitted after connection arrived automatically with matching fields. Tally created the raw tab `Afaan Oromo Bible — Share Feedback (English)`. `Feedback EN` is a live formula view of that raw tab, with UTC timestamp formatting; `Feedback OM` is reserved for the future Oromo connection. `Setup`, `Field Map` and the empty reviewer-owned `Review` tab explain the structure. Drive metadata still confirms `shared: false` and owner-only permission. The private spreadsheet URL is deliberately absent from website files and this public guide; it was shared only in the owner's chat.

Two real, clearly labeled English setup tests were accepted through the website embed, covering general feedback and a website issue with no name/email. The first was imported from Tally; the second demonstrated new automatic delivery. All five English branches were exercised on desktop/light and mobile/dark. No user report was fabricated, and no response row was inserted to simulate integration success. The website has not been deployed. Oromo fluent review, publication and its own Sheets connection remain open.

## Activate the integration

1. Use the existing [published English form](https://tally.so/r/vXrgVQ), editing it at `https://tally.so/forms/vXrgVQ/edit`. It has no password, respondent login, payment or submission limit. Partial submissions, save-for-later and completion redirects are off. Do not create a duplicate.
2. Use the existing [Afaan Oromoo draft](https://tally.so/forms/KpeOA7/edit). Its editable questions, answer options, help text, submit label and thank-you copy are translated, with equivalent types and conditions. Do not create a duplicate.
3. Have a fluent Afaan Oromoo editor review the website catalog, feedback dialog and the actual form, including error recovery and translation terminology. The supplied Oromo wording has been checked for completeness and consistency, **not certified by a fluent reviewer**.
4. The English connection is complete and verified. After Oromo review and publication, connect its form to the same private workbook as described below. Keep restricted sharing and check attachment accessibility before relying on screenshot delivery.
5. The real IDs are already in `website/feedback-config.js`: English `vXrgVQ`, Oromo `KpeOA7`. If replacing a form later, paste only its real ID, with no URL, spaces or query parameters. These IDs are intentionally public; never put Google credentials or spreadsheet URLs in this file.
6. Publish the Oromo form after fluent review, then set `om.copyReviewed` to `true` only after that review and acceptance of the system-message limitation below. `en.copyReviewed` is already `true`. An invalid/empty ID, missing config or false review flag keeps that language’s embed unavailable; it never silently substitutes the other language.
7. Complete the live tests at the end, then deploy through the existing Pages workflow. Activate both languages together for a complete bilingual launch. Public IDs are the only account-specific values needed in website source.

Current configuration (real IDs):

```js
window.AOB_FEEDBACK = Object.freeze({
  en: { formId: 'vXrgVQ', copyReviewed: true },
  om: { formId: 'KpeOA7', copyReviewed: false } // Draft; publish and review before enabling.
});
```

## Form structure and copy

Use one form per language, with a single required category choice, conditional detail questions and a short optional contact section. Keep it on one page if practical. Ask for details only after a category is chosen. Name and email remain optional in every branch. Turn off partial-submission collection, third-party analytics, tracking pixels and respondent email collection by default. Do not enable a redirect after submission.

| Element | English | Afaan Oromoo draft |
| --- | --- | --- |
| Form heading | Share Feedback | Yaada kee nuuf qoodi |
| Introduction | Tell us what happened or what would help. Choose a topic to see the relevant questions. Your name and email are optional. | Waan mudate yookaan waan si gargaaru nutti himi. Gaaffilee si ilaallatan arguuf mata duree filadhu. Maqaa fi imeelii galchuun dirqama miti. |
| Category question | What would you like to share? | Yaada akkamii nuuf qooduu barbaadda? |
| Translation category | Bible translation or wording correction | Hiika yookaan jechoota Kitaaba Qulqulluu sirreessuu |
| Bug category | Application bug or technical issue | Rakkoo sagantichaa yookaan rakkoo teeknikaa |
| Feature category | Feature request or improvement | Gaaffii amala haaraa yookaan fooyyaʼiinsaa |
| Website category | Website or download issue | Rakkoo marsariitii yookaan buufannaa |
| General category | General feedback | Yaada waliigalaa |
| Optional contact heading | May we contact you? (optional) | Si qunnamuu dandeenyaa? (filannoo) |
| Name | Name (optional) | Maqaa (filannoo) |
| Email | Email (optional, if you’d like a reply) | Imeelii (yoo deebii barbaadde; filannoo) |
| Submit button | Send feedback | Yaada ergi |
| Thank-you heading | Thank you for your feedback. | Yaada keetiif galatoomi. |
| Thank-you description | Your feedback was sent to the team for review. Wording suggestions will be checked in the context of the edition you selected. | Yaadni kee garee keenyaaf akka ilaalamuuf ergameera. Yaadni jechoota sirreessuu maxxansa ati filatte irratti hundaaʼee ilaalama. |

Copy the dialog’s privacy and wording-review notices into each form too, so visitors following the direct fallback link see the same disclosures. They live in `website/index.html` under `dialog.privacy` and `dialog.review`, and in `website-docs/oromo-translations.json` under those same keys. The website’s success message means Tally accepted the submission; it does not assert that a reviewer has read it or that Sheets delivery succeeded.

### Conditional questions

All fields below are required **only while their branch is selected**, except those explicitly marked optional. The plugin's supported setup uses one SHOW rule per category, targeting the entire relevant questions. SHOW establishes the hidden default; hidden questions are not required. Essential questions retain their required setting when shown, and the five optional fields are explicitly optional. Do not add reverse HIDE rules as an else: Tally evaluates SHOW rules without an if/else pair. When reviewing exports, use the selected category to identify relevant columns; do not treat retained answers from an abandoned branch as part of the active report.

| Show when | Question / field type | English | Afaan Oromoo draft |
| --- | --- | --- | --- |
| Translation | Edition / dropdown | Which Bible edition? | Maxxansa Kitaaba Qulqulluu kam? |
| Translation | Book / short text | Book | Kitaaba |
| Translation | Chapter / short text | Chapter | Boqonnaa |
| Translation | Verse / short text | Verse or verse range | Caqasa yookaan caqasoota |
| Translation | Concern / long text | What concerns you about the wording? | Jechoota kana ilaalchisee maaltu si yaaddesse? |
| Translation | Correction / optional long text | What wording would you suggest? (optional) | Jechoota akkamii akka taʼan yaadda? (filannoo) |
| Bug | OS / dropdown | Which operating system are you using? | Sirna kompiitaraa kam fayyadamta? |
| Bug | Version / short text | Which app version? You can find it in About. “Not sure” is fine. | Maxxansa sagantichaa kam? Waaʼee sagantichaa (About) keessaa ilaali. Yoo hin beekne, “Hin beeku” barreessi. |
| Bug | Problem / long text | What went wrong? | Rakkoon maal ture? |
| Bug | Reproduction / optional long text | How can we reproduce it? (optional) | Rakkoo kana irra deebiʼanii arguuf maal gochuu qabna? (filannoo) |
| Bug | Screenshot / optional file upload | Add a screenshot (optional). Remove names, private notes and other personal details first. | Suuraa iskiriinii dabali (filannoo). Dura maqaa, yaadannoo dhuunfaa fi odeeffannoo dhuunfaa biroo keessaa haqi. |
| Feature | Suggestion / long text | What would you like to add or improve? | Maal dabaluun yookaan fooyyessuun siif wayya? |
| Feature | Benefit / long text | How would it help you? | Akkamitti si gargaara? |
| Website | Affected area / short text | Which page or download platform? | Fuula yookaan sirna buufannaa kam? |
| Website | Issue / long text | What happened? | Maaltu mudate? |
| General | Comments / long text | What would you like us to know? | Maal akka beeknu barbaadda? |

Edition options must remain **gaz 2022**, **OOCS 2024**, **KJV** in both forms. Add **Not sure / Hin beeku** to avoid forcing inaccurate reports. Use text for chapter and verse to preserve ranges, source labels and subverses. Do not assume matching verse numbering across editions. No report changes Scripture automatically. Review source fidelity separately from a translation difference, preserve edition identity, and refer editorial suggestions to the appropriate rights holder when needed. AndHub Engineering PLC does not claim permission to revise third-party editions.

OS options: Windows, macOS, Linux, Other / Kan biraa, Not sure / Hin beeku. The optional screenshot field currently uses Tally's upload defaults; no custom image-type/count/size restriction has been verified. An owner may set one JPG/PNG/WebP up to 5 MB in the editor and test it if desired. The form does not claim an unverified size limit. Do not ask for backups, databases, complete app logs, personal notes or reading history. Require only what helps someone explain their issue.

## Bilingual and visual limitations

Use separate forms so questions and confirmations remain coherent in the selected website language. Tally’s current [system-message language list](https://tally.so/help/supported-languages) does not include Afaan Oromoo. Editable content can be Oromo, but validation, closed-form text and some upload controls may remain English. Select English for those built-in messages and retain the Oromo dialog notice explaining this. If English system messages are unacceptable, leave Oromo activation gated and request Oromo support from Tally; do not describe the service as fully localized.

Use Tally’s supported editor customization for forest-green buttons, readable body type and restrained headings. The website dialog follows the site’s appearance. Its cross-origin form uses a deliberately neutral white surface in both themes to keep Tally’s own text legible. The site cannot recolor Tally’s internal controls with CSS. A matching dark form depends on Tally’s available customization and must be checked in the actual account; do not add unverified theme parameters, custom-domain services or paid features as hidden prerequisites. Tally branding may remain. No additional font, widget script, translation service or backend is needed.

## Google Sheets: private reporting

Use Tally’s native [Google Sheets integration](https://tally.so/help/google-sheets-integration). English is already connected: **preserve the existing connection and its Tally-managed response tab**. For Oromo after publication, open **Integrations → Google Sheets → Connect**, authorize the company Google account and select the existing **Afaan Oromo Bible — Private Feedback Review** workbook. Tally may create a new response tab named after the form, as it did for English. Read back the actual destination; do not assume it is the prepared `Feedback OM` tab. A live view can be added there after verifying the real raw columns. Neither available plugin can save this authorization on the owner's behalf. Give each connection a clear name. Never publish the spreadsheet to the web or use link-wide access. Limit access to people reviewing feedback.

The prepared `Field Map` contains equivalent bilingual question labels and editor UUIDs. Submission API/export identifiers differ from these editor UUIDs; match the real output by question labels and Tally's generated schema. English currently exports three metadata columns plus the 19 question columns. `Feedback EN` uses a native FILTER formula to display nonempty rows from the real raw tab; it does not create or submit responses. Do not type over its formula. `Review` has canonical headers plus status/priority dropdowns and no response rows. A reviewer must populate it or build a review view; those tracking fields are not automatically supplied by Tally.

Separate raw tabs prevent independently translated column headers from being mistaken for identical field identifiers. Keep the same field order/types in the duplicated forms. Verify actual generated headers and then maintain this reporting map in a private review tab:

| Reporting field | Source / handling |
| --- | --- |
| Submission ID; date/time | Tally submission metadata; retain UTC. Add a separate local display column for Africa/Nairobi (UTC+3) if useful. |
| Language | Destination tab identifies `en` or `om`; optionally add a fixed hidden locale field in each form. |
| Category | Selected category; map its two labels to internal codes `translation`, `bug`, `feature`, `website`, `general`. |
| Bible edition; book; chapter; verse | Translation branch only. Preserve entered labels; do not infer another edition. |
| OS; app version | Bug branch only. “Not sure” is allowed. |
| Feedback description | Active branch’s concern, problem, feature suggestion, website issue or general comments. The integration exports separate question columns; combine in a private review view if desired. |
| Suggested correction | Translation branch, optional. |
| Steps to reproduce; why helpful; affected page/platform | Respective branch fields. |
| Name; email | Optional contact fields; empty is valid. |
| Attachment links | Bug upload field; verify who can open downloaded/exported links before enabling uploads. Treat the URLs as sensitive. |
| Review status; priority; assigned reviewer; resolution notes | Internal reviewer-owned columns or a review tab keyed by submission ID. These are **not automatically populated by Tally**. |

A single merged reporting view is optional: build it privately after inspecting the real export columns, normalizing category labels and selecting only the active branch’s description. Do not assume translated labels or duplicated forms share internal IDs. No Apps Script, public API credentials, custom backend or public spreadsheet is required.

Send one unmistakably labeled test report per category and language. Match submission IDs and timestamps between Tally and each raw tab; confirm optional blanks, edition references, multiline descriptions and attachment links. Remove test reports from Tally and the Sheet when finished. For missing rows, check Tally’s delivery logs, authorization and retry/resend controls. Keep formulas and tracking rows in a separate review tab so they do not interfere with raw response insertion. Tally acceptance and Sheets delivery are separate checks.

Decide a retention period and reviewer access within the company before launch; add the chosen policy to both forms. Do not promise a response deadline or specific retention duration until agreed. For a deletion request, the existing company email is the contact; remove relevant records from Tally, Sheets and downloaded copies, following the company’s process. The page itself never reads or logs answer payloads, stores contacts, or accesses Google Sheets. Tally/Google still process their own service-request metadata under their privacy policies.

## Implementation and maintenance

- `website/feedback-config.js`: public IDs and review gate only.
- `website/feedback.js`: native modal, lazy direct iframe embed, 15-second slow state, retry, direct link and trusted Tally lifecycle events. An iframe load alone never means successful submission or even a working form. A late `Tally.FormLoaded` recovers from the slow state.
- `website/index.html` and catalog: static bilingual shell, privacy, confirmation and unconfigured fallback. Regenerate `website/om/index.html` with `scripts/localize_site.py` after copy changes.
- Direct Tally iframe URLs use documented embed options `hideTitle=1` and `alignLeft=1`. The widget script is unnecessary for the fixed-height embed; omitting it also avoids its automatic forwarding of host query parameters. Tally itself sends the documented postMessage lifecycle events. Check these against the real forms before launch.
- The browser’s native dialog provides modality and background inertness. Opening focuses Close, closing restores the trigger (the menu toggle for mobile navigation). Escape closes from the website shell. Chromium does not forward Escape from inside a cross-origin iframe to the parent dialog; the transport check verifies Shift+Tab can return to Close, then Escape works. The dialog explains the keyboard alternative, and Close remains visible in the sticky header. Repeat this check inside both real forms, whose own controls may consume keys. Clicking the backdrop does not discard a report. Closing warns that unfinished work may be lost; the website does not autosave drafts.
- JavaScript-disabled/unsupported-dialog visitors reach the static feedback section and company email. Direct form fallback opens a new tab and keeps the website open.
- Relative local script/assets/language paths and the explicit preparation allowlist preserve repository-subpath hosting. No release asset, binary or application code is changed.

The locally inspected licensed `dialog-dialog-standard-1` uses React/shadcn components and is unsuitable for this dependency-free public HTML site. Its header/description/action structure informed the dialog. No proprietary source was copied into the public repository. The existing semantic native image dialog pattern is reused. The official [embed guide](https://tally.so/help/embed-your-form), [event contract](https://developers.tally.so/widgets/events) and [conditional logic guide](https://tally.so/help/conditional-form-logic) were consulted on 8 November 2026.

## Launch checklist

- [ ] Real English and Oromo forms published; all five conditional paths tested, including switching categories and optional contacts.
- [ ] Fluent review completed and `om.copyReviewed` enabled; English Tally system-message limitation accepted and disclosed.
- [ ] Actual public form IDs entered; no spreadsheet URL, key or credential in source.
- [ ] Both private Google Sheets connections saved; response rows and attachment access verified.
- [ ] Company reviewer access and retention process agreed; privacy and translation-review notices present in both forms.
- [ ] On real forms, test successful submission, thank-you content, parent confirmation and exactly one Sheet row per submission. Do not treat local transport fixtures as this evidence.
- [ ] Live iframe keyboard entry/exit, Escape, tab order, screen reader, mobile uploads, zoom, light/dark contrast and conditional validation checked.
- [ ] Block Tally or disconnect internet: loading state, delayed state, retry and direct link remain understandable; closing restores focus.
- [ ] Run localization, metadata and artifact checks from README; inspect root and repository-path previews.
- [ ] Review website diff; merge/deploy with the existing Pages workflow and verify the returned deployment plus both live language URLs. No deployment was performed by this local change.

Local browser checks and outstanding integration evidence are recorded in [VALIDATION.md](VALIDATION.md).
