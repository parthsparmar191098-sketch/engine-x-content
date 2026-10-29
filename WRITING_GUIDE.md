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
| Fri | Comparison, Field Notes or Learn Engineering (link an Engine-X model when relevant) |
| Sat | News · the week's biggest machine story (any tag) |
| Sun | Case Study on the 1st and 3rd Sunday of the month, otherwise News |

## Research
- News: stories from the last 7 days, from reputable or original sources. Verify key numbers in at least two sources when possible.
- Case studies: well-documented events (official reports, reputable outlets). Stick to established facts.
- Don't repeat a topic covered in the last 30 days (check `posts/`).
- No investment, medical or unverified defence claims. Remove any detail you can't source.

## Post file
`posts/YYYY-MM-DD-short-slug.md`, header as documented in `build.py`:
- `category`: news | comparison | case-study | field-notes | learn
  - `comparison`: any post that compares machines, parts, materials, methods or tools ("A vs B", "A, B or C?")
  - `field-notes`: practical how-it-works and troubleshooting from ship repair, dry dock, piping, testing and workshop work
  - `case-study`: a well-documented real event (official reports, reputable outlets)
  - `learn`: engineering basics and skills (drawings, CAD, standards)
  - The Journal's "Machine Guides" filter is only for the Engine-X 3D machine pages on the main site; don't use `guide` for new posts
- `tag` (news only): machines | automation | space | design
- `summary`: 1–2 sentences, under 220 characters
- `seo_title`: the title Google shows, **max 60 characters**, main search phrase first (e.g. "Pump Cavitation and NPSH Explained, With an Example"). The on-page headline (`title`) can stay longer. " | Engine-X Blog" is added automatically only if it still fits.
- `seo_description`: the Google snippet, **120–155 characters**, says what the reader will learn; only facts that are in the post. If left out, the summary is cut to 155 automatically.
- `model`: turbo | pulleybelt | pump | gearbox | diesel855 — only when genuinely related (also adds the "Free 3D model · download" box for that machine; posts without it show all models in a strip)
- `sources`: every source used, `Name | URL`
- `keywords`: 3–6 comma-separated search phrases people would actually type (e.g. "how does a jack-up vessel work")
- `takeaways`: 3–5 short bullet points (one line each) — shown in the "In short" box at the top
- `tldr`: one sentence that sums up the whole post — shown at the bottom
- `faq`: 2–4 real questions a reader would search, written `Question | Answer`; each answer 1–2 sentences, fully supported by the post and its sources
- `updated`: only when a published post is genuinely revised (new facts or corrections), never just to look fresh
- `video`: only a relevant YouTube video from an official source (company, agency, university); leave out if none

The template adds the rest automatically: contents list, breadcrumbs, reading time, author link and bio, dates, share buttons, related and latest posts, the 3D machines box, the services box and all schema.org data. Do not write these by hand in the body.

## Length & structure
- News: 450–800 words. Case study: 900–1500 words. Comparison, field notes and learn: 800–1300 words.
- Open with what happened (2–3 sentences), then `##` sections explaining the engineering. Use at least 3 `##` sections with clear, descriptive headings (they become the contents list).
- Use numbered steps when explaining a process or how-to, and a short Markdown comparison table when comparing options, specs or old vs new. Only when they genuinely help.
- Include a real-world example (a named project, vessel, plant or test from the sources) to ground the explanation.
- A short quote (under 15 words) from an official source is welcome when the exact words matter; one per source at most.
- Link 1–3 earlier Engine-X posts inside the text where they are genuinely related, using their full URL `https://engx3d.com/blog/posts/<slug>.html`.
- Link key facts to their source inline the first time they appear, in addition to the Sources list.
- End with a short "The engineering takeaway" section.

## Answer engines (AEO)
Write every post so ChatGPT, Perplexity, Google AI Overviews and similar tools can lift a clean answer and cite Engine-X.
- **Answer first.** The first paragraph answers the post's main question in 40–60 words, as a standalone statement that makes sense out of context. Name the thing directly; never start with "In this article" or "This post".
- **Question headings.** At least 2 of the `##` headings are phrased the way people ask, e.g. "How does a jack-up vessel stay stable?" or "Why do ships use slow-speed diesels?". Answer each one in the first 1–2 sentences under it, then explain.
- **Self-contained sections.** Each section repeats the subject by name instead of opening with "it" or "this", so a single section still reads correctly when quoted alone.
- **Define once, plainly.** The first time a technical term appears, give a one-sentence definition (e.g. "A wastegate is a valve that lets exhaust bypass the turbine.").
- **Concrete facts.** Prefer specific numbers with units, dates and named examples over vague words like "huge" or "very fast", each traceable to a source.
- **`faq` questions** are written exactly as someone would type or say them, and the answers are complete on their own.
- **Link the guides.** When the topic touches them, link the matching Engine-X guide or comparison inside the text:
  - https://engx3d.com/turbocharger · https://engx3d.com/turbocharger-vs-supercharger
  - https://engx3d.com/centrifugal-pump · https://engx3d.com/centrifugal-vs-positive-displacement-pump
  - https://engx3d.com/v-belt-drive · https://engx3d.com/belt-vs-chain-vs-gear-drive
  - https://engx3d.com/gear-reducer (gearboxes, gears, reducers)
  - https://engx3d.com/marine-diesel-engine (diesel engines, marine engines, cooling, fuel injection)
- **Consistent names.** Always "Engine-X" (with the hyphen) and "Parth Parmar".

### AEO v2 — what gets a post cited first
- **Pick questions we can win.** Prefer the exact questions people type in Parth's niche — ship repair, dry docking, marine engines, pumps, valves, piping, inspection, CAD for mechanical work — where today's top answers are thin or generic. One main question per post; put it in the title or the first `##`.
- **First-hand experience.** If Parth has told us something real about the topic (dry dock, workshop, testing, design work), add it as `field_note` (1–2 sentences, his voice). Never invent experiences, places, clients or numbers; leave `field_note` out if there is nothing real to say.
- **One table when the topic allows.** A comparison table or a key-values table with units (pressures, temperatures, ratios). Answer engines lift tables directly.
- **Numbers with dates.** For anything that changes (prices, records, fleets, standards editions), say when: "as of October 2026", "ASME B31.3-2022".
- **Link two related posts** from the blog inside the text, plus the matching engx3d.com guide, so the topic cluster stays connected.

## Images
- Prefer an original SVG diagram saved in `assets/` (dark background `#0a1120`, accents `#5ea7ff` / `#8a6cff`, white text, readable at phone width).
- Or a public-domain / properly licensed image (e.g. NASA) with `image_credit`.
- Never use photos from news articles.

## Publishing
Run `python3 build.py` to check it builds, then commit on a new branch `post/YYYY-MM-DD` and open a pull request to `main` for review. Merging publishes it.
