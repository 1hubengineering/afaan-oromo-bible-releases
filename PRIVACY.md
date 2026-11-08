# Privacy

## Current beta.8 application

Core reading, search, notes, bookmarks, highlights and preferences operate locally. No account or hosted application backend is required for these features. Personal records are stored separately from the bundled read-only Scripture libraries.

JSON backups and note exports are files you choose to save. They can contain private writing and quotations. You control where they are stored and with whom they are shared. Restoring data creates a recovery snapshot that may retain earlier personal records.

The current beta uses the beta application identity `org.afaanoromobible.reader.beta`. Its Windows production-profile data is normally under `%APPDATA%\org.afaanoromobible.reader.beta\production`. On macOS the production profile is normally under ~/Library/Application Support/org.afaanoromobible.reader.beta/production; on Linux under ~/.local/share/org.afaanoromobible.reader.beta/production, or the configured XDG_DATA_HOME. Uninstalling the app should not be assumed to remove all records, recovery copies, exports or backups.

The installer may contact Microsoft to obtain WebView2 when it is absent. Opening external links, downloading releases and using GitHub issues involves those external services and their policies. This document is not a guarantee about operating-system or WebView2 vendor behavior.

## Historical builds and reports

Beta.4 contains experimental online integration and has different network behavior from beta.8. Prefer the current beta.

GitHub issues are public. Remove personal notes, backup content, access tokens, local usernames and other sensitive information before posting logs or screenshots. See [security reporting](SECURITY.md) for vulnerabilities.
