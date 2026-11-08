# Installation and updates

## Windows beta

1. Download the recommended x64 setup executable and its SHA256SUMS file from the same [release](https://github.com/1hubengineering/afaan-oromo-bible-releases/releases/tag/v0.1.0-beta.8).
2. Verify its checksum in PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath .\Afaan-Oromo-Bible-0.1.0-beta.8-x64-setup.exe
```

Compare the complete hash with the row for that exact filename in SHA256SUMS. If it differs, do not run the file; download it again from the official release page.

3. Review the [beta notice](BETA_NOTICE.md). These installers are unsigned; Windows may warn about an unrecognized publisher. Check the repository and checksum and proceed only if you trust this distribution. Do not disable system-wide security controls.
4. Run the installer and follow its prompts. Microsoft Edge WebView2 is required; the installer may download it when absent, so first installation may need internet access.
5. Start **Afaan Oromo Bible Beta**. No source checkout, WSL, Node, Rust or Python is required.

The beta has installed-app evidence on Windows 11 x64. Other Windows versions and architectures have not been qualified here. A clean computer without WebView2 and fully disconnected installation remain unqualified scenarios.

## Updating

Export a personal-data JSON backup from the app's backup controls and keep an extra copy outside its data directory. Close the application before running the newer installer. Current beta installers use the same separate beta identity and normally update the existing beta installation; this is not a guarantee of compatibility between development versions.

Use the highest numbered beta unless you are deliberately investigating a historical build. Older installers are archived prereleases. Switching to an older version can leave newer data unreadable; do not downgrade your only working profile.

## Uninstalling

Use Windows Settings > Apps to uninstall Afaan Oromo Bible Beta. Back up records you want to retain first. Uninstalling must not be treated as a guaranteed personal-data erasure procedure; see [privacy](PRIVACY.md).

## Other platforms

macOS and Linux are development targets. There are no qualified public packages for them in these beta releases.
