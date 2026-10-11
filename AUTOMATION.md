# Parth's automation — how it all fits together

Read this first in any new chat about Tech Pulse Daily, the Engine-X blog or engx3d.com.

## Repos (GitHub: parthsparmar191098-sketch)
| Repo | What it is |
|---|---|
| `techpulse-bot` (public) | Telegram channel **Tech Pulse Daily** (@technical369). Posts are queued in `queue/` and sent by a GitHub Action every 15 min (`.github/workflows/send.yml`, `scripts/send_due.py`). Bot token is the repo secret `TELEGRAM_BOT_TOKEN`. Rules: `POSTING_GUIDE.md`. |
| `engine-x-content` (public, this repo) | The Engine-X blog. Posts in `posts/*.md`, diagrams in `assets/`. `build.py` builds the site; GitHub Actions publishes it to GitHub Pages. Rules: `WRITING_GUIDE.md`. |
| `Engine-x` (private) | The main site **engx3d.com** on Cloudflare Pages. `blog.html` is the cinematic Journal page (reads `/blog/feed.json`). `functions/blog/[[path]].js` serves this repo's blog at **engx3d.com/blog/**. |

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
