# docs.page Guide

docs.page is a "docs as code" platform. Source your docs from a GitHub repo
and get a beautiful, searchable documentation site instantly.

## How it works

1. In your GitHub repo, add a `docs/` folder (or a single `README.md`).
2. Write Markdown (`.md`) or MDX (`.mdx`) files.
3. Visit `https://docs.page/<owner>/<repo>` — your site is live.

## Configuration (`docs.json`)

Place a `docs.json` in your repo root or `docs/` directory:

```json
{
  "header": {
    "showName": true,
    "showGitHubCard": true,
    "links": [
      { "title": "GitHub", "href": "https://github.com/..." }
    ]
  },
  "social": {
    "github": "owner/repo",
    "x": "@handle"
  }
}
```

## Features

- **Markdown / MDX** — write in the format you already know.
- **Live preview** — PR previews via the GitHub App.
- **Custom domains** — point your own domain at docs.page.
- **Pre-built components** — alerts, tabs, code blocks, videos.
- **Search** — built-in full-text search.
- **Analytics** — Google Analytics or Plausible.

## Local preview

```bash
npx docs.page
```

This starts a local preview server with hot reload so you can see changes
before pushing.

## Links

- Website: https://docs.page
- Docs: https://use.docs.page
- GitHub: https://github.com/invertase/docs.page
- GitHub App: https://github.com/apps/docs-page
