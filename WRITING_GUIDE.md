# Engine-X Blog – Writing Guide

Instructions for the daily run that writes one blog post.

## Voice
- English, clear, written as **Parth Parmar, a mechanical engineer** (dry dock / marine / piping / valves background) explaining machines to students, engineers and clients.
- Always explain **how the machine works** — the mechanism is the point, not just the headline.
- Own words only. Never copy sentences from sources; any quote under 15 words.

## Daily rotation (IST)
| Day | Post |
|---|---|
| Mon | News · machines |
| Tue | News · automation |
| Wed | News · space |
| Thu | News · design |
| Fri | Machine Guide or Learn Engineering (link an Engine-X model when relevant) |
| Sat | News · the week's biggest machine story (any tag) |
| Sun | Case Study on the 1st and 3rd Sunday of the month, otherwise News |

## Research
- News: stories from the last 7 days, from reputable or original sources. Verify key numbers in at least two sources when possible.
- Case studies: well-documented events (official reports, reputable outlets). Stick to established facts.
- Don't repeat a topic covered in the last 30 days (check `posts/`).
- No investment, medical or unverified defence claims. Remove any detail you can't source.

## Post file
`posts/YYYY-MM-DD-short-slug.md`, header as documented in `build.py`:
- `category`: news | guide | case-study | field-notes | learn
- `tag` (news only): machines | automation | space | design
- `summary`: 1–2 sentences, under 220 characters
- `model`: turbo | pulleybelt | pump — only when genuinely related
- `sources`: every source used, `Name | URL`

## Length & structure
- News: 450–800 words. Case study: 900–1500 words. Guide: 800–1300 words.
- Open with what happened (2–3 sentences), then `##` sections explaining the engineering.
- End with a short "engineering takeaway".

## Images
- Prefer an original SVG diagram saved in `assets/` (dark background `#0a1120`, accents `#5ea7ff` / `#8a6cff`, white text, readable at phone width).
- Or a public-domain / properly licensed image (e.g. NASA) with `image_credit`.
- Never use photos from news articles.

## Publishing
Run `python3 build.py` to check it builds, then commit on a new branch `post/YYYY-MM-DD` and open a pull request to `main` for review. Merging publishes it.
