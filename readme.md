# docs.page — Docs for Humans + Agents

- **Repo**: https://github.com/invertase/docs.page
- **License**: Open source (owned by Invertase)
- **Language**: TypeScript / Node.js
- **Status**: Set up — ready for content

## setup

No local install needed — it's a hosted platform.

1. Write Markdown files in `docs/`.
2. Push to GitHub — your docs appear at:
   `https://docs.page/<user>/<repo>`

Optionally install the [GitHub App](https://github.com/apps/docs-page) for
live preview on pull requests.

## what was done

- [x] created a `docs.json` config
- [x] wrote first Markdown doc pages
- [ ] pushed to GitHub and verified the site is live
- [ ] installed the GitHub App for PR previews (optional)

## adding articles

Drop any `.md` or `.mdx` file into `docs/`. The filename becomes the URL
slug and sidebar label. Use frontmatter for per-page title/description.
