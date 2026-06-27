# AGENTS.md — docspage

This is a **local reference note** about the [docs.page](https://docs.page) hosted platform — not the platform's source code.

## Structure

- `readme.md` — setup checklist
- `guide.md` — docs.page usage reference (config, features, commands)
- `docs/` — markdown articles published to docs.page
- `docs.json` — docs.page platform config

## What not to do

- **Do not run builds, install deps, or look for tests** — no code, no manifest, no lockfile.
- **Do not try `npx docs.page` or `@docs.page/cli` preview** — the CLI has no dev server; this is a hosted-only platform.
- **Do not edit the docs.page platform** — its source lives at `https://github.com/invertase/docs.page`.
- **Do not touch `serve.py` or the systemd service unless the user asks** — they are setup once and left running.

## Scope

Add new `.md` / `.mdx` files to `docs/` — they become articles on the hosted site. Tick checkboxes in `readme.md` as setup progresses. The `guide.md` is reference; only update if the platform itself changes.
