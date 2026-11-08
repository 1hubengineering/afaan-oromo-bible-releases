# Experimental macOS and Linux testing — beta.8

These builds are available for colleagues and partners to evaluate on real devices. They are development prereleases with limited automated startup evidence, not qualified production releases. Use test notes and export any useful records before changing installations.

## Choose your download

| Device | File | Testing status |
| --- | --- | --- |
| Apple silicon Mac (M1 or later) | [Apple silicon DMG](https://github.com/1hubengineering/afaan-oromo-bible-releases/releases/download/v0.1.0-beta.8/Afaan-Oromo-Bible-0.1.0-beta.8-macos-arm64.dmg) | Native startup/package checks on macOS 15; built with a macOS 14.0 deployment minimum |
| Intel Mac | [Intel DMG](https://github.com/1hubengineering/afaan-oromo-bible-releases/releases/download/v0.1.0-beta.8/Afaan-Oromo-Bible-0.1.0-beta.8-macos-x86_64.dmg) | Native startup/package checks on macOS 15; built with a macOS 14.0 deployment minimum |
| Ubuntu 24.04 LTS x86_64 / amd64 | [Ubuntu Debian package](https://github.com/1hubengineering/afaan-oromo-bible-releases/releases/download/v0.1.0-beta.8/Afaan-Oromo-Bible-0.1.0-beta.8-linux-amd64.deb) | Native reading and package lifecycle checks under Xvfb/Openbox; GNOME/X11/Wayland still need real-device feedback |

Use About This Mac to identify Apple silicon or Intel. macOS 14 itself, older macOS, other Linux distributions and Linux ARM are not qualified by these tests. [Release files and checksums](https://github.com/1hubengineering/afaan-oromo-bible-releases/releases/tag/v0.1.0-beta.8) identify the exact builds; the new platform packages include gaz, OOCS and KJV, with required notices. NIV/1997 text is not installed.

## Verify and install

Download SHA256SUMS from the same release and compare the complete hash for your exact filename. Checksums detect file changes; they do not authenticate the publisher.

On macOS, run `shasum -a 256 ./Afaan-Oromo-Bible-0.1.0-beta.8-macos-arm64.dmg`, substituting the Intel filename when appropriate. Open the DMG and drag **Afaan Oromo Bible Beta** into Applications.

The Mac builds have an ad-hoc signature only: no Apple Developer ID or notarization. Gatekeeper may block a downloaded copy. Follow [Apple’s instructions for opening an app you trust](https://support.apple.com/en-us/102445), using the per-app Privacy & Security > Open Anyway option if available. This does not authenticate the publisher. Do not disable Gatekeeper globally. If the system reports malware/damage or organizational policy prevents opening it, stop and report the exact message rather than forcing installation.

On Ubuntu 24.04 x64, run:

```sh
sha256sum ./Afaan-Oromo-Bible-0.1.0-beta.8-linux-amd64.deb
sudo apt install ./Afaan-Oromo-Bible-0.1.0-beta.8-linux-amd64.deb
```

The Linux package has no release-key signature. APT may need internet to obtain declared GTK3/WebKitGTK 4.1 system dependencies. The package does not contain a complete operating-system web runtime. Start **Afaan Oromo Bible Beta** from the application launcher. After prerequisites are installed, Scripture and personal study tools use local content.

## Test on your device

1. Record the app version, complete installer SHA-256, OS version and CPU architecture. On Linux also record GNOME/other desktop and X11/Wayland session. Report whether installation or first launch required an extra step.
2. Read, navigate, change versions and open comparison. Check Afaan Oromo book names, source text, headings and wrapped lines. Compare a familiar passage against its source where possible.
3. Search an Afaan Oromo word/phrase, change case or apostrophe style, use book/testament filters and result pages, and open a reference. Repeat in another installed edition.
4. Highlight verses in each pane. Check that the color follows wrapped text, More removes the highlight, and the other edition keeps its own annotations. Check copy and Add note without inserting long source metadata into the note.
5. Create synthetic notes, bookmarks and highlights, close the app and reopen it. Confirm the exact records, reading location, language, palette and light/dark preference persist. On Mac test the window close button and Command-Q with a draft; on Linux test normal window-manager close. Report failed-save/close behavior if it occurs.
6. Test both English and Afaan Oromo, light/dark modes, enlarged text, narrow windows and keyboard focus. Where available, test VoiceOver on Mac or Orca on Ubuntu and describe the exact inaccessible control.
7. Export a synthetic note as Markdown, DOCX and PDF. Export a personal-record JSON backup. Test restore only with a disposable test profile, because restoring replaces its current records; preserve an independent backup first.
8. Disconnect the network after installation and repeat reading, search, annotation and restart. Report any action that unexpectedly requires internet. On Ubuntu, a remove/reinstall test may use `sudo apt remove afaan-oromo-bible-beta`; back up first and confirm whether records remain after reinstalling. Do not delete application-data folders as part of ordinary testing.

## Known limits and feedback

Native Mac evidence currently covers package architecture/resources, ad-hoc signature verification and two process startups with SQLite initialization/integrity, not a complete reading or VoiceOver journey. Ubuntu evidence covers initial Scripture through AT-SPI and actual install/remove/reinstall with preserved isolated profile bytes, not clean-host GNOME/Wayland/Orca qualification. Downloaded/quarantined Mac installation still needs your feedback. Independent fluent Oromo/editorial review remains open.

Two browser checks are still unresolved: palette-dialog color contrast and intermittent local Scripture quote suggestions in notes. Report their actual behavior on your device; successful package builds do not mean all application tests passed.

Submit a [bug report](https://github.com/1hubengineering/afaan-oromo-bible-releases/issues/new?template=bug_report.yml) with your environment, edition/reference, steps, expected/actual result and the relevant test number above. Synthetic text and redacted screenshots are sufficient. Never attach personal notes, a complete backup, credentials or unredacted personal data. Use [private security reporting](SECURITY.md) for a vulnerability. No source checkout, Node, Rust, Python or developer account is needed to run the installed app.
