# docs.page: Zero-Config Documentation Sites from GitHub

**Source:** `08-docs-page.md` · **Phase 1** · Cleaned & annotated

## Overview

docs.page is a free, open-source tool that turns a GitHub repo's `docs/` folder into a polished documentation website — no build step, no hosting config, no framework knowledge required. Write `.mdx` files, push to GitHub, and your site is live at `docs.page/yourname/repo`.

## Core Content

### 1. The Elevator Pitch

Write markdown in a `docs/` folder, push to GitHub, get a beautiful docs site with search, navigation, dark mode, and live PR previews. No builds, no hosting, no config headaches. It's like Notion publishing for developers who want version control and zero infrastructure.

### 2. Why This Matters

- **Unfair advantage:** Skip the entire "setup a docs site" rabbit hole — no Docusaurus configs, no Vercel, no broken builds. Docs ship 10× faster.
- **Hidden leverage:** Live PR previews via GitHub bot. Every pull request auto-generates a preview URL — documentation stays in sync with code because the friction is near-zero.
- **"Aha!" moment:** You don't need to `npm run dev` anything. Open `docs.page/preview` in your browser, point it at your local `docs/` folder, and edits auto-reload in real time.

### 3. Reality Check

- **Overrated when:** You need custom interactive components, heavy API auto-generation, or i18n support. docs.page is opinionated and simple — not a replacement for Docusaurus/Nextra.
- **Opportunity cost:** You learn one tool's conventions (docs.json, MDX component syntax) rather than transferable skills like Next.js or CI/CD pipelines.
- **Not for:** Teams outside GitHub (GitLab/Bitbucket unsupported), anyone needing private documentation (public-repo only), or dedicated docs engineers who want full design control.

### 4. Core Concepts

| Feature | What It Does | Analogy |
|---------|-------------|---------|
| **docs.json** | One config file — logo, theme, sidebar, search, social links | TV remote that controls every device |
| **MDX** | Markdown with embedded React components (tabs, cards, callouts) | Texting, but you can embed a spreadsheet mid-conversation |
| **PR Previews** | Every pull request auto-generates a live preview URL | Sending a photo of your outfit before leaving the house |
| **Live Reload** | Edit locally, see changes in a browser tab — no server needed | Google Docs for developer docs |
| **Instant Deploy** | Push to GitHub → live site in seconds | Teleporting a letter to its recipient |

### 5. AI Leverage

**Use AI for:** Drafting `docs.json` config, converting existing READMEs/docs to `.mdx` with proper frontmatter, brainstorming sidebar structures.

**Don't outsource:** Your actual content — AI doesn't know your user's pain points. Component design decisions (when to use `<Callout>` vs `<Steps>` vs plain text).

**One AI workflow:** *"I have a GitHub repo called [user/repo]. Turn these 3 README sections into a docs.page structure: docs.json with [brand details], index.mdx homepage using <Info> and <Steps> components, and a sidebar grouping Installation, API Reference, and FAQ."*

### 6. Learning Map

| Phase | Time | Goal |
|-------|------|------|
| **Hook** | 15 min | Run `pnpm dlx @docs.page/cli init docs.page`, open `docs.page/preview`, edit `index.mdx` — watch it live-reload |
| **Foundation** | 1 hr | 3 principles: `docs.json` is your control panel; frontmatter drives SEO/Meta; MDX components work out of the box |
| **Application** | 1–2 hr | Migrate an existing project's README into a 3-page docs site with sidebar, dark theme, and PR preview |
| **Deep Dive** | Optional | Custom MDX components, Algolia DocSearch, advanced theming, multi-tab navigation |

### 7. Go/No-Go

| Situation | Verdict |
|-----------|---------|
| Docs live in <10 min with zero infra | 🟢 **Learn this NOW** |
| Custom design/interactive demos needed | ⏳ Use Docusaurus or Nextra |
| Private repos or non-GitHub VCS | 🔴 Skip — GitHub-public only |
| API auto-generation from code | ⏳ Use Swagger/ReadMe instead |
| Solo dev who hates maintaining docs sites | 🟢 **Learn this NOW** |
| Existing Markdown docs to publish | 🟢 **Learn this NOW** — trivial migration |

## Key Takeaways

1. **docs.page is the "just ship it" documentation tool** — ideal for developers who've wasted weekends configuring docs sites instead of writing actual docs.
2. The **one-file config** (`docs.json`) pattern is elegant but means you're locked into docs.page's opinionated model.
3. **PR previews are the killer feature** — they solve the "documentation drifts from code" problem by putting docs review in the same workflow as code review.
4. GitHub-only + public-only constraints are real hard limits — evaluate these before investing.
