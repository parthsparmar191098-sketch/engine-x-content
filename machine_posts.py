#!/usr/bin/env python3
"""Write a blog post for every Engine-X machine that doesn't have one yet.

Reads the machine list the main site publishes (engx3d.com/models/index.json, built by the
Engine-x repo whenever a machine is added). A machine "has a post" when any post's header says
`model: <its id>`. For each machine without one, this writes posts/<date>-<page>-3d-model.md
(with the machine's picture in assets/) from the machine's own data: what it is, its systems,
key facts, how to explore it, download it and see it in AR.

Run by .github/workflows/new-machine-posts.yml every day, or by hand:
    python machine_posts.py            # writes new posts, prints their URLs
    python machine_posts.py --dry-run  # only lists what it would write
"""
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = json.loads((ROOT / "site.json").read_text())
MAIN = SITE["main_site"].rstrip("/")
BLOG = f"{MAIN}/blog"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "engine-x-blog-bot (+https://engx3d.com/blog/)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def has_post(mid):
    pat = re.compile(rf"^model:\s*{re.escape(mid)}\s*$", re.M)
    return any(pat.search(p.read_text(encoding="utf-8")) for p in (ROOT / "posts").glob("*.md"))


def sentences(text, n):
    parts = re.split(r"(?<=[.!?])\s+", (text or "").strip())
    return " ".join(p for p in parts[:n] if p)


def clip(text, limit):
    return text if len(text) <= limit else text[: limit - 1].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def post_for(m, today):
    name, low, page = m["name"], m["name"].lower(), m["page"]
    title_name = " ".join(w[:1].upper() + w[1:] for w in name.split())
    w, h, d = m["size_mm"]
    intro = sentences(m["about"], 2) or f"{name}: {m['sub']}."
    systems = m["systems"]
    sys_names = ", ".join(s["name"].lower() for s in systems)
    guide = f" For the theory step by step, read the [{low} guide]({m['guide']})." if m.get("guide") else ""
    title = f"New Free 3D Model: The {title_name}, Part by Part"
    seo_title = clip(f"{title_name} 3D Model: Every Part, Free STL & GLB", 60)
    seo_desc = clip(f"A free, real-scale {low} 3D model with {m['pieces']} named parts. See how it works, "
                    f"take it apart in 3D, download GLB or STL, or view it in AR.", 155)
    summary = clip(f"Engine-X now has a free {low} 3D model: {m['pieces']} named parts you can explode, "
                   f"cut open, download as STL or GLB, or place in your room in AR.", 220)
    sys_lines = "\n".join(f"- **{s['name']}**: {s['blurb'] or 'see it in the 3D atlas.'}" for s in systems)
    faq = [
        f"Is the Engine-X {low} 3D model free? | Yes. It is free for personal and educational use under CC BY-NC 4.0, with credit to Engine-X. Selling the files or prints is not allowed.",
        f"What file formats can I download the {low} in? | The whole machine comes as GLB (with colours and named parts) or STL in millimetres, and each of its {m['parts']} different parts can be downloaded as its own STL or all together as a ZIP.",
        f"Can I see the {low} in AR on my phone? | Yes. On Android or iPhone, tap the View in AR button on the model page or the cube button in the atlas to place it in your room at real size, with no app to install.",
    ]
    takeaways = [
        f"Engine-X has a free, real-scale {low} 3D model with {m['pieces']} named parts.",
        f"It is organised into {len(systems)} systems: {sys_names}.",
        "You can explode it, cut it open and X-ray it in the browser.",
        f"Download it as GLB or STL, or any of its {m['parts']} parts as separate STL files.",
        "On a phone it opens in AR at real size, with no app.",
    ]
    keywords = f"{low} 3d model, {low} parts, how does a {low} work, {low} stl download, {low} 3d model free"
    header = "\n".join([
        "---",
        f"title: {title}",
        f"date: {today}",
        "category: guide",
        f"summary: {summary}",
        f"seo_title: {seo_title}",
        f"seo_description: {seo_desc}",
        f"image: assets/{today}-{page}-3d-model.jpg",
        f"image_alt: The Engine-X {low} 3D model, assembled",
        "image_credit: 3D model: Engine-X",
        f"model: {m['id']}",
        f"keywords: {keywords}",
        f"tldr: The {low} is now a free Engine-X 3D model you can take apart in the browser, download part by part, or see in AR.",
        "takeaways:",
        *[f"- {t}" for t in takeaways],
        "faq:",
        *[f"- {q}" for q in faq],
        "sources:",
        f"- Engine-X — {name} 3D model | {m['url']}",
        f"- Engine-X — Interactive 3D atlas | {m['atlas']}",
        "---",
    ])
    body = f"""{intro}

Engine-X now has this machine as a free, real-scale 3D model. All {m['pieces']} parts are modeled one by one and named, so you can see how the {low} is built and how it works, then download any part you need.{guide}

## What is inside a {low}?

The model is split into {len(systems)} systems. Each one is a group of parts that do one job together:

{sys_lines}

## Key facts about the 3D model

| | |
|---|---|
| Parts modeled | {m['pieces']} named parts ({m['parts']} different ones) |
| Systems | {len(systems)} |
| Size | {w} × {h} × {d} mm, real scale |
| Formats | GLB, STL, USDZ (iPhone AR) |
| License | CC BY-NC 4.0, free with credit |

## How do you explore the {low} in 3D?

1. Open the [{low} in the Engine-X atlas]({m['atlas']}). It runs in any browser, on a phone too.
2. Press play to watch it run, and change the speed with the slider.
3. Drag the **Explode** slider to pull the parts apart.
4. Use **section** to cut it in half and **X-ray** to see through the housings.
5. Tap any part to read what it does, then isolate it or zoom to it.

## How do you download the model and its parts?

On the [{low} model page]({m['url']}) you can download:

- the whole machine as **GLB** (colours and part names, for Blender and 3D viewers) or **STL** (millimetres, for CAD and slicers),
- every part as its **own STL**, one by one, with a picture and size for each,
- or all {m['parts']} parts in one **ZIP**.

These are learning models, not a print kit: some parts touch or overlap and there are no fit tolerances, so scale them up and print them as a display piece.

## Can you see it in AR?

Yes. On Android or iPhone, tap **View in AR** on the model page, or the cube button in the atlas, and place the {low} on your table or floor at real size. No app is needed.
"""
    return header + "\n" + body


def main():
    dry = "--dry-run" in sys.argv
    try:
        machines = json.loads(fetch(f"{MAIN}/models/index.json"))
    except Exception as err:
        print(f"::warning::Could not read {MAIN}/models/index.json ({err}); nothing to do today.")
        return 0
    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).date().isoformat()
    new = [m for m in machines if not has_post(m["id"])]
    if not new:
        print("Every machine already has a post.")
    urls = []
    for m in new:
        slug = f"{today}-{m['page']}-3d-model"
        print(("would write " if dry else "writing ") + f"posts/{slug}.md")
        if dry:
            continue
        (ROOT / "assets" / f"{slug}.jpg").write_bytes(fetch(m["image"]))
        (ROOT / "posts" / f"{slug}.md").write_text(post_for(m, today), encoding="utf-8")
        urls.append(f"{BLOG}/posts/{slug}.html")
    if urls:
        Path(ROOT / ".new_post_urls").write_text(" ".join(urls))
    return 0


if __name__ == "__main__":
    sys.exit(main())
