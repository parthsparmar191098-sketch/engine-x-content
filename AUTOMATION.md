# Parth's automation — how it all fits together

Read this first in any new chat about Tech Pulse Daily, the Engine-X blog or engx3d.com.

## Repos (GitHub: parthsparmar191098-sketch)
| Repo | What it is |
|---|---|
| `techpulse-bot` (public) | Telegram channel **Tech Pulse Daily** (@technical369). Posts are queued in `queue/` and sent by a GitHub Action every 15 min (`.github/workflows/send.yml`, `scripts/send_due.py`). Bot token is the repo secret `TELEGRAM_BOT_TOKEN`. Rules: `POSTING_GUIDE.md`. |
| `engine-x-content` (public, this repo) | The Engine-X blog. Posts in `posts/*.md`, diagrams in `assets/`. `build.py` builds the site; GitHub Actions publishes it to GitHub Pages. Rules: `WRITING_GUIDE.md`. |
| `Engine-x` (private) | The main site **engx3d.com** on Cloudflare Pages. `blog.html` is the cinematic Journal page (reads `/blog/feed.json`). `functions/blog/[[path]].js` serves this repo's blog at **engx3d.com/blog/**. |

## Claude connectors
| Connector | Use |
|---|---|
| GitHub | Reads/writes the three repos above. |
| Gmail | Outreach drafts and reply summaries; Claude sends only after Parth says so. |
| Cloudflare Developer Platform (added 11 Oct 2026) | Workers, KV, R2, D1 on Parth's Cloudflare account. No Workers yet; the site itself runs on Cloudflare Pages. |

Google Search Console is set up for engx3d.com (no connector; check it at search.google.com/search-console).

## Scheduled tasks (claude.ai → Scheduled tasks), all on Sonnet, IST
| Time | Task | What it does |
|---|---|---|
| 06:25 | Tech Pulse Daily digest | Researches the last 24 h and queues ONE Daily Digest → sent to Telegram at 08:00. |
| 06:50 | Engine-X daily blog post | Writes one post (uses the `engine-x-blog` skill) and opens a PR in this repo. |
| 07:45 | Morning check: digest + blog | Confirms both happened; fills any gap. |

## Parth's daily job
Open the blog PR notification → read → **Merge**. The post appears on engx3d.com/blog within ~5 min.

## Decisions so far
- Telegram: English, worldwide tech news, one Daily Digest at 08:00 IST.
- Blog: one post a day by weekday rotation; reviewed via PR before publishing.
- No investment tips, no copied text or photos; every fact sourced.
- Blog SEO (12 Oct 2026): `build.py` adds contents list, breadcrumbs, reading time, author link + bio, dates, "In short" box, TL;DR, expandable FAQ, share buttons, related + latest posts, 3D machines box, free 3D model download box (29 Oct 2026: links to engx3d.com/3d-models/, parts count in `MODEL_PAGES`), services offer and schema.org data (Article/BlogPosting, Person, Organization, BreadcrumbList, FAQPage) to every post. Optional header fields `keywords`, `takeaways`, `tldr`, `faq`, `updated`, `video` are filled by the daily post per `WRITING_GUIDE.md`.
- engx3d.com (12 Oct 2026): `engine-x-98a.pages.dev` 301-redirects to engx3d.com; site-wide schema.org data added (Organization, services, FAQ on /about, machine list on /atlas).
- Blog AEO (17 Oct 2026): `WRITING_GUIDE.md` now has an "Answer engines (AEO)" section: 40–60 word answer-first opening, question-style `##` headings, self-contained sections, one-line definitions, concrete sourced numbers, and links to the engx3d.com machine guides and comparison pages (/turbocharger, /centrifugal-pump, /v-belt-drive and their "vs" pages). Site side (Engine-x repo): those 6 pages, robots.txt allowing AI crawlers, llms.txt + llms-full.txt; sitemaps submitted to Google Search Console and Bing Webmaster Tools.
- Blog AEO fixes (26 Oct 2026): `build.py` now also writes `llms.txt` (every post with its one-line answer) and `llms-full.txt` (answer, key facts and FAQ for every post), served at engx3d.com/blog/llms.txt and linked from the main site's llms.txt, so they update by themselves with each new post. Posts get SpeakableSpecification schema, and the build prints a warning when a post's opening answer is over 60 words. The 5 older news posts got question-style headings and 14 long openings were trimmed to 40–60 words (marked `updated: 2026-10-26`).
- AEO v2 (26 Oct 2026): IndexNow — after every publish, the `indexnow` job in `deploy.yml` runs `indexnow.py` to ping new/changed post URLs to IndexNow (Bing, Yandex; ChatGPT search uses Bing). Key `indexnow_key` in `site.json`, key file at engx3d.com/<key>.txt (Engine-x repo). Run the workflow by hand with `ping_all` to ping every page. Posts can carry a `field_note` (first-hand note from Parth, shown as a "From the field" box and in llms-full.txt); WRITING_GUIDE has an "AEO v2" section. Schema links Engine-X to linkedin.com/company/engx3d and Parth to LinkedIn + Reddit.

## Fixes log
- **12 Oct 2026** – Digest didn't reach Telegram though the tasks said "success": a tracked `.pyc` file in `techpulse-bot` changed during validation, so `git pull --rebase` failed and nothing was pushed. Fixed by untracking `__pycache__` (+ `.gitignore`). The digest and morning-check prompts now validate with `python3 -B`, commit only the queue file, and confirm the file is on GitHub before reporting OK. If a digest is missing, check `queue/` and `sent/` on GitHub first.
