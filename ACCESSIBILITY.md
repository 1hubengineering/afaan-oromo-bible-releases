# Website accessibility

The Afaan Oromo Bible product website is available in [English](https://bible.1hubengineering.com/) and [Afaan Oromoo](https://bible.1hubengineering.com/om/). It is maintained by AndHub Engineering.

## Using the website

- Press Tab to reach **Skip to content**, then Enter to move focus to the main page.
- All navigation, theme controls, screenshot tabs, download links and FAQs support the keyboard. Screenshot tabs use Left/Right Arrow, Home and End; Escape closes an enlarged screenshot and returns focus to its link.
- Browser zoom and text enlargement remain available. Layouts reflow on small screens, and light/dark appearance follows the system unless you choose a preference.
- Reduced-motion preferences are respected. Images have text alternatives; decorative artwork is hidden from assistive technology when equivalent text is present.
- With JavaScript disabled, both language pages, ordinary navigation, downloads, FAQs and the full screenshot gallery remain available. Interactive theme switching and the screenshot overlay require JavaScript.

The website uses static HTML and local assets without third-party font, tracking or analytics scripts. The English and Afaan Oromoo pages are separate URLs with language navigation; language is not forced by location or browser settings.

## Reporting a barrier

Use the [accessibility issue form](https://github.com/1hubengineering/afaan-oromo-bible-releases/issues/new?template=accessibility.yml), or email [info@1hubengineering.com](mailto:info@1hubengineering.com) if GitHub is difficult to use. Include the affected URL, browser/device, assistive technology if applicable, steps to reproduce and what prevented you from completing your task. You may report website or desktop-reader barriers; identify which one is affected.

GitHub issues are public. Use synthetic examples and redact screenshots. Do not attach personal notes, backups, credentials or private publisher correspondence. See [SECURITY.md](SECURITY.md) for sensitive security reports.

## Verification scope

Website checks include semantic HTML, image text alternatives, focus navigation, screenshot tabs/dialogs, reflow, light/dark contrast and automated axe checks. The [website validation record](website-docs/VALIDATION.md) records the actual environments and results. Manual assistive-technology testing and independent fluent Afaan Oromo review remain ongoing needs.

The desktop reader is a development beta with its own platform, signing, accessibility and content qualification requirements. Website checks do not establish desktop-reader screen-reader compatibility. See [BETA_NOTICE.md](BETA_NOTICE.md) and [TESTING_GUIDE.md](TESTING_GUIDE.md).
