#!/usr/bin/env python3
"""Build the Engine-X blog (static site) from posts/*.md into _site/.

Each post is a Markdown file with a simple header:

    ---
    title: The Ships Building Europe's Offshore Wind Farms
    date: 2026-10-10
    category: news            # news | guide | case-study | field-notes | learn
    tag: machines             # news only: machines | automation | space | design
    summary: One or two sentences shown on the blog card.
    image: assets/2026-10-10-jackup.svg      # optional
    image_alt: Diagram of a jack-up vessel    # optional
    model: turbo              # optional: link to an Engine-X 3D machine
    draft: false              # optional, true = not published
    sources:
    - Offshore Magazine | https://...
    - OE Digital | https://...
    ---
    Markdown body...
"""

import html
import json
import re
import shutil
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_site"
SITE = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
BASE = SITE["base_url"].rstrip("/")

CATEGORIES = {
    "news": "News",
    "guide": "Machine Guide",
    "case-study": "Case Study",
    "field-notes": "Field Notes",
    "learn": "Learn Engineering",
}
FILTERS = [("all", "All"), ("news", "News"), ("guide", "Guides"),
           ("case-study", "Case Studies"), ("field-notes", "Field Notes"), ("learn", "Learn")]
TAGS = {"machines": "⚙️ Machines", "automation": "🤖 Automation",
        "space": "🚀 Space", "design": "✏️ Design"}
MODELS = {
    "turbo": "Turbocharger",
    "pulleybelt": "V-Belt Pulley Drive",
    "pump": "Centrifugal Pump",
}

e = html.escape


def parse(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        raise ValueError(f"{path.name}: missing --- header ---")
    head, body = m.groups()
    meta, sources, in_sources = {}, [], False
    for line in head.splitlines():
        if not line.strip():
            continue
        if in_sources and line.lstrip().startswith("- "):
            item = line.lstrip()[2:]
            name, _, url = item.partition("|")
            sources.append((name.strip(), url.strip()))
            continue
        in_sources = False
        key, _, val = line.partition(":")
        key = key.strip().lower()
        val = val.strip()
        if key in ("category", "tag", "date", "model", "draft", "image"):
            val = val.split("#", 1)[0].strip()  # allow trailing comments on simple fields
        if key == "sources":
            in_sources = True
            continue
        meta[key] = val
    for req in ("title", "date", "category", "summary"):
        if not meta.get(req):
            raise ValueError(f"{path.name}: missing '{req}'")
    if meta["category"] not in CATEGORIES:
        raise ValueError(f"{path.name}: unknown category '{meta['category']}'")
    meta["date_obj"] = datetime.strptime(meta["date"], "%Y-%m-%d")
    meta["sources"] = sources
    meta["slug"] = path.stem
    meta["url"] = f"{BASE}/posts/{path.stem}.html"
    meta["body_html"] = markdown.markdown(body, extensions=["extra", "sane_lists"])
    meta["draft"] = meta.get("draft", "false").lower() == "true"
    return meta


def kicker(p):
    k = CATEGORIES[p["category"]]
    if p["category"] == "news" and p.get("tag") in TAGS:
        k += " · " + TAGS[p["tag"]]
    return k


def nice_date(d):
    return d.strftime("%d %b %Y").lstrip("0")


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="{ogtype}">
{ogimage}
<link rel="alternate" type="application/rss+xml" title="Engine-X Blog" href="{base}/rss.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}/style.css">
{jsonld}
</head>
<body>
"""

FOOT = """<footer>
  <a href="{home}">Engine&#8209;X</a> — interactive 3D machines, engineered by Parth Parmar.
  · <a href="{base}/rss.xml">RSS</a>
</footer>
</body>
</html>
"""


def page_head(title, desc, canonical, ogtype="website", image=None, jsonld=""):
    og = f'<meta property="og:image" content="{e(image)}">' if image else ""
    return HEAD.format(title=e(title), desc=e(desc), canonical=e(canonical), ogtype=ogtype,
                       ogimage=og, base=BASE, jsonld=jsonld)


def render_post(p):
    image_url = f"{BASE}/{p['image']}" if p.get("image") else None
    ld = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": p["title"],
        "description": p["summary"],
        "datePublished": p["date"],
        "author": {"@type": "Person", "name": "Parth Parmar"},
        "publisher": {"@type": "Person", "name": "Parth Parmar"},
        "mainEntityOfPage": p["url"],
    }
    if image_url:
        ld["image"] = image_url
    jsonld = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    out = [page_head(f"{p['title']} | Engine-X Blog", p["summary"], p["url"], "article", image_url, jsonld)]
    out.append('<div class="wrap">\n')
    out.append(f'  <a class="back" href="{BASE}/">&larr; All posts</a>\n')
    out.append(f'  <div class="kicker">{e(kicker(p))}</div>\n')
    out.append(f'  <h1>{e(p["title"])}</h1>\n')
    out.append(f'  <p class="meta">By Parth Parmar · {nice_date(p["date_obj"])}</p>\n')
    if image_url:
        out.append(f'  <figure class="hero"><img src="{e(image_url)}" alt="{e(p.get("image_alt", ""))}">'
                   + (f'<figcaption>{e(p["image_credit"])}</figcaption>' if p.get("image_credit") else "")
                   + "</figure>\n")
    out.append(f'  <article>{p["body_html"]}</article>\n')
    model = p.get("model")
    if model:
        name = MODELS.get(model, model)
        out.append('  <div class="cta">\n'
                   f'    <div class="cta-title">See a {e(name)} in 3D</div>\n'
                   '    <p>Explode it, cut it open and watch it run — free, in your browser.</p>\n'
                   f'    <a class="btn" href="{SITE["main_site"]}/atlas.html">Open the Engine-X Atlas &rarr;</a>\n'
                   '  </div>\n')
    else:
        out.append('  <div class="cta">\n'
                   '    <div class="cta-title">Explore machines in 3D</div>\n'
                   '    <p>Turbochargers, pumps and belt drives you can explode and section, part by part.</p>\n'
                   f'    <a class="btn" href="{SITE["main_site"]}/atlas.html">Open the Engine-X Atlas &rarr;</a>\n'
                   '  </div>\n')
    if p["sources"]:
        out.append('  <div class="sources"><div class="sources-title">Sources</div><ul>\n')
        for name, url in p["sources"]:
            out.append(f'    <li><a href="{e(url)}" rel="noopener" target="_blank">{e(name)}</a></li>\n')
        out.append("  </ul></div>\n")
    out.append("</div>\n")
    out.append(FOOT.format(home=SITE["main_site"], base=BASE))
    return "".join(out)


def render_index(posts):
    out = [page_head(SITE["title"], SITE["description"], f"{BASE}/")]
    out.append('<div class="wrap">\n')
    out.append(f'  <a class="back" href="{SITE["main_site"]}/">&larr; Engine-X home</a>\n')
    out.append(f'  <h1>{e(SITE["title"])}</h1>\n')
    out.append(f'  <p class="sub">{e(SITE["description"])}</p>\n')
    out.append('  <div class="filters" role="tablist">\n')
    for key, label in FILTERS:
        cls = "chip on" if key == "all" else "chip"
        out.append(f'    <button class="{cls}" data-f="{key}">{e(label)}</button>\n')
    out.append('  </div>\n  <div id="list">\n')
    for p in posts:
        out.append(f'  <a class="card" data-c="{p["category"]}" href="{e(p["url"])}">\n'
                   f'    <div class="kicker">{e(kicker(p))} <span class="date">· {nice_date(p["date_obj"])}</span></div>\n'
                   f'    <h2>{e(p["title"])}</h2>\n'
                   f'    <p>{e(p["summary"])}</p>\n'
                   "  </a>\n")
    if not posts:
        out.append('  <p class="sub">First posts are on the way.</p>\n')
    out.append('  </div>\n  <p class="empty" hidden>No posts in this category yet.</p>\n</div>\n')
    out.append("""<script>
document.querySelectorAll('.chip').forEach(function(b){
  b.addEventListener('click', function(){
    var f = b.dataset.f, shown = 0;
    document.querySelectorAll('.chip').forEach(function(x){ x.classList.toggle('on', x === b); });
    document.querySelectorAll('#list .card').forEach(function(c){
      var ok = f === 'all' || c.dataset.c === f;
      c.style.display = ok ? '' : 'none';
      if (ok) shown++;
    });
    document.querySelector('.empty').hidden = shown > 0;
  });
});
</script>
""")
    out.append(FOOT.format(home=SITE["main_site"], base=BASE))
    return "".join(out)


def render_rss(posts):
    items = []
    for p in posts[:30]:
        pub = format_datetime(p["date_obj"].replace(hour=8, tzinfo=timezone.utc))
        items.append(f"<item><title>{e(p['title'])}</title><link>{e(p['url'])}</link>"
                     f"<guid>{e(p['url'])}</guid><pubDate>{pub}</pubDate>"
                     f"<category>{e(CATEGORIES[p['category']])}</category>"
                     f"<description>{e(p['summary'])}</description></item>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
            f"<title>{e(SITE['title'])}</title><link>{BASE}/</link>"
            f"<description>{e(SITE['description'])}</description>"
            + "".join(items) + "</channel></rss>\n")


def render_sitemap(posts):
    urls = [f"<url><loc>{BASE}/</loc><changefreq>daily</changefreq></url>"]
    urls += [f"<url><loc>{e(p['url'])}</loc><lastmod>{p['date']}</lastmod></url>" for p in posts]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            + "".join(urls) + "</urlset>\n")


def main():
    posts = []
    for path in sorted((ROOT / "posts").glob("*.md")):
        p = parse(path)
        if not p["draft"]:
            posts.append(p)
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "posts").mkdir(parents=True)
    shutil.copy(ROOT / "style.css", OUT / "style.css")
    if (ROOT / "assets").exists():
        shutil.copytree(ROOT / "assets", OUT / "assets")

    for p in posts:
        (OUT / "posts" / f"{p['slug']}.html").write_text(render_post(p), encoding="utf-8")
    (OUT / "index.html").write_text(render_index(posts), encoding="utf-8")
    (OUT / "rss.xml").write_text(render_rss(posts), encoding="utf-8")
    (OUT / "sitemap.xml").write_text(render_sitemap(posts), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    feed = [{"title": p["title"], "url": p["url"], "date": p["date"], "category": p["category"],
             "category_label": CATEGORIES[p["category"]], "tag": p.get("tag", ""),
             "kicker": kicker(p), "summary": p["summary"]} for p in posts[:30]]
    (OUT / "feed.json").write_text(json.dumps({"base": BASE, "posts": feed}, ensure_ascii=False, indent=1),
                                   encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    if SITE.get("custom_domain"):
        (OUT / "CNAME").write_text(SITE["custom_domain"] + "\n")
    print(f"built {len(posts)} posts -> {OUT}")


if __name__ == "__main__":
    main()
