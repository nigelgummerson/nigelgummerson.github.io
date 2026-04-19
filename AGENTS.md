# AGENTS.md — skeletalsurgery-landing

## Project Overview

Static landing site served at `plan.skeletalsurgery.com` — the public entry page for Nigel's open-source skeletal-surgery planning tools. Currently links to the Spinal Instrumentation Plan & Record (hosted at `plan.skeletalsurgery.com/spine/`) and can be extended with other planning tools as they mature.

Deployed via GitHub Pages from `nigelgummerson/nigelgummerson.github.io`; custom domain configured via `CNAME`.

## Structure

```
spine-surgery/planning/skeletalsurgery-landing/
├── index.html          # Landing page (hand-authored HTML + embedded CSS)
├── CNAME               # plan.skeletalsurgery.com
├── robots.txt
├── sitemap.xml
├── linkedin-post.md    # Launch post draft for LinkedIn
├── AGENTS.md           # This file
├── CLAUDE.md           # Session history
└── .git/
```

## Read First

`index.html` is the whole site. It is a single hand-authored HTML file with embedded CSS — no build step, no framework, no JavaScript.

## Deployment

- **Repository:** `nigelgummerson/nigelgummerson.github.io` (GitHub user/organisation Pages repo)
- **Live URL:** https://plan.skeletalsurgery.com/
- **Custom domain:** configured via `CNAME`; DNS managed separately
- **Deployment model:** push to `main` → GitHub Pages publishes automatically. No CI.

## Adding a Tool

1. Add a new `<div class="tool">` block to `index.html` linking to the tool's path (e.g. `/spine/`, `/<newtool>/`).
2. Add the tool's URL to `sitemap.xml` with an appropriate priority.
3. If the tool is a separate repo deployed to the same domain, its build must land in the correct subpath (handled in that tool's own deploy workflow).

## Code Style

- Hand-authored HTML + embedded CSS. No JS. Keep it that way.
- UK English where prose matters; technical terms follow the linked tool's conventions.
- Accessibility: semantic headings, WCAG-AA contrast (the existing palette is compliant).

## SEO

- Descriptive `<title>`, `<meta name="description">`, Open Graph tags, and JSON-LD schema for `WebApplication`/`Person` already in place.
- `sitemap.xml` lists the landing page, the planner app, and the quick reference.

## AI Collaboration

- **AGENTS.md** — this file; static project description for any AI.
- **CLAUDE.md** — session history and next steps.
- Read `CLAUDE.md` for current state before making changes.
