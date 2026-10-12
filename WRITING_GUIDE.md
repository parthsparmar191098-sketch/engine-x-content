# Engine-X Blog – Writing Guide

Instructions for the daily run that writes one blog post.

## Voice
- English, clear, written as **Parth Parmar, a mechanical engineer** (mechanical design and drafting in AutoCAD and SolidWorks, plus dry dock / marine / piping / valves background) explaining machines to students, engineers and clients.
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
- `keywords`: 3–6 comma-separated search phrases people would actually type (e.g. "how does a jack-up vessel work")
- `takeaways`: 3–5 short bullet points (one line each) — shown in the "In short" box at the top
- `tldr`: one sentence that sums up the whole post — shown at the bottom
- `faq`: 2–4 real questions a reader would search, written `Question | Answer`; each answer 1–2 sentences, fully supported by the post and its sources
- `updated`: only when a published post is genuinely revised (new facts or corrections), never just to look fresh
- `video`: only a relevant YouTube video from an official source (company, agency, university); leave out if none

The template adds the rest automatically: contents list, breadcrumbs, reading time, author link and bio, dates, share buttons, related and latest posts, the 3D machines box, the services box and all schema.org data. Do not write these by hand in the body.

## Length & structure
- News: 450–800 words. Case study: 900–1500 words. Guide: 800–1300 words.
- Open with what happened (2–3 sentences), then `##` sections explaining the engineering. Use at least 3 `##` sections with clear, descriptive headings (they become the contents list).
- Use numbered steps when explaining a process or how-to, and a short Markdown comparison table when comparing options, specs or old vs new. Only when they genuinely help.
- Include a real-world example (a named project, vessel, plant or test from the sources) to ground the explanation.
- A short quote (under 15 words) from an official source is welcome when the exact words matter; one per source at most.
- Link 1–3 earlier Engine-X posts inside the text where they are genuinely related, using their full URL `https://engx3d.com/blog/posts/<slug>.html`.
- Link key facts to their source inline the first time they appear, in addition to the Sources list.
- End with a short "The engineering takeaway" section.

## Images
- Prefer an original SVG diagram saved in `assets/` (dark background `#0a1120`, accents `#5ea7ff` / `#8a6cff`, white text, readable at phone width).
- Or a public-domain / properly licensed image (e.g. NASA) with `image_credit`.
- Never use photos from news articles.

## Publishing
Run `python3 build.py` to check it builds, then commit on a new branch `post/YYYY-MM-DD` and open a pull request to `main` for review. Merging publishes it.
