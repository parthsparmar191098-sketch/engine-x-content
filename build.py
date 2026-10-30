#!/usr/bin/env python3
"""Build the Engine-X blog (static site) from posts/*.md into _site/.

Each post is a Markdown file with a simple header:

    ---
    title: The Ships Building Europe's Offshore Wind Farms
    date: 2026-10-10
    updated: 2026-10-14       # optional: date of a real content update
    category: news            # news | comparison | case-study | field-notes | learn
    tag: machines             # news only: machines | automation | space | design
    summary: One or two sentences shown on the blog card and in the "In short" box.
    seo_title: Short title for Google, max 60 characters    # optional
    seo_description: Search snippet, 120-155 characters      # optional
    image: assets/2026-10-10-jackup.svg      # optional
    image_alt: Diagram of a jack-up vessel    # optional
    image_credit: Diagram: Engine-X           # optional
    model: turbo              # optional: link to an Engine-X 3D machine
    keywords: jack-up vessel, offshore wind, monopile   # optional, comma separated
    video: https://www.youtube.com/watch?v=XXXXXXXXXXX  # optional, YouTube only
    tldr: One sentence shown at the end of the post.    # optional
    field_note: What Parth has seen first-hand on this topic (dry dock, workshop)  # optional
    draft: false              # optional, true = not published
    takeaways:                # optional, 3-5 short bullet points
    - First key point
    - Second key point
    faq:                      # optional, 2-4 questions, "Question | Answer"
    - What is a jack-up vessel? | A ship that lowers legs to the seabed...
    sources:
    - Offshore Magazine | https://...
    - OE Digital | https://...
    ---
    Markdown body...

Everything else on a post page (contents list, breadcrumbs, reading time,
author bio, share buttons, related and latest posts, 3D machines, services
and schema.org data) is generated automatically.
"""

import html
import json
import re
import shutil
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote, urlparse, parse_qs

import markdown

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_site"
SITE = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
BASE = SITE["base_url"].rstrip("/")
MAIN = SITE["main_site"].rstrip("/")

AUTHOR = {
    "name": "Parth Parmar",
    "url": f"{MAIN}/about",
    "job": "Mechanical Engineer & Designer, creator of Engine-X",
    "linkedin": "https://www.linkedin.com/in/parth-parmar-767608309",
    "bio": ("Mechanical engineer and designer from India. He has designed and drafted marine engineering "
            "projects in AutoCAD and SolidWorks, and works in ship repair and dry docking, with hands-on "
            "experience in piping, valves, fabrication and pressure testing. He builds Engine-X, a free "
            "interactive 3D atlas that shows how real machines work inside."),
    "knows": ["Mechanical design", "AutoCAD", "SolidWorks", "2D drafting and 3D modeling", "Ship repair and dry docking", "Piping and valves", "Pressure and leak testing", "Fabrication", "Interactive 3D web visualization", "AI automation"],
}
LOGO = f"{MAIN}/og-image.jpg"

CATEGORIES = {
    "news": "News",
    "guide": "Guide",
    "comparison": "Comparison",
    "case-study": "Case Study",
    "field-notes": "Field Notes",
    "learn": "Learn Engineering",
}
FILTERS = [("all", "All"), ("news", "News"), ("comparison", "Comparisons"),
           ("case-study", "Case Studies"), ("field-notes", "Field Notes"), ("learn", "Learn")]
TAGS = {"machines": "⚙️ Machines", "automation": "🤖 Automation",
        "space": "🚀 Space", "design": "✏️ Design"}
MODELS = {
    "turbo": ("Turbocharger", "Exhaust-driven turbine spinning a compressor, with journal bearings and a wastegate."),
    "pulleybelt": ("V-Belt Pulley Drive", "Two pulleys and a V-belt reducing speed with true belt kinematics."),
    "pump": ("Centrifugal Pump", "End-suction pump with a backward-curved impeller and volute casing."),
    "gearbox": ("Helical Gear Reducer", "Two-stage helical gearbox, 16 : 1, with meshing helical gears and tapered roller bearings."),
    "gatevalve": ("Gate Valve", "NPS 4 Class 150 OS&Y wedge gate valve with a rising stem, seat rings, packing and handwheel."),
}
# Free 3D model pages on engx3d.com/3d-models/ (slug, different parts to download)
MODEL_PAGES = {"turbo": ("turbocharger", 34), "pump": ("centrifugal-pump", 20), "pulleybelt": ("v-belt-drive", 20),
               "gearbox": ("gear-reducer", 29), "gatevalve": ("gate-valve", 22)}
LIST_KEYS = ("sources", "takeaways", "faq")
SIMPLE_KEYS = ("category", "tag", "date", "updated", "model", "draft", "image", "video")
WORDS_PER_MIN = 220

e = html.escape


def download_box(model):
    """Free 3D model download box: the post's own machine in detail, or all machines in a strip."""
    if model in MODEL_PAGES:
        slug, n = MODEL_PAGES[model]
        name, desc = MODELS[model]
        page = f"{MAIN}/3d-models/{slug}"
        return ('  <section class="dlbox">\n'
                f'    <a class="dl-img" href="{page}"><img src="{MAIN}/3d-models/img/{slug}.jpg" alt="{e(name)} 3D model" width="1200" height="900" loading="lazy"></a>\n'
                '    <div class="dl-body"><div class="box-title">Free 3D model &middot; download</div>\n'
                f'      <h3>{e(name)}</h3>\n'
                f'      <p>{e(desc)} Real scale, every part named. Download the whole machine as GLB or STL, '
                f'grab any of its {n} parts as its own STL, or view it in AR on your phone.</p>\n'
                f'      <div class="dl-act"><a class="btn" href="{page}">Download the model &rarr;</a>'
                f'<a class="more" href="{page}#parts">All {n} parts</a>'
                f'<a class="more" href="{MAIN}/atlas#m={model}">Open in 3D</a></div>\n'
                '      <p class="small">Free for personal and educational use (CC BY-NC 4.0), credit Engine&#8209;X.</p>\n'
                '    </div>\n  </section>\n')
    cards = "".join(
        f'<a class="dl-mini" href="{MAIN}/3d-models/{slug}"><img src="{MAIN}/3d-models/img/{slug}.jpg" alt="{e(MODELS[k][0])} 3D model" '
        f'width="1200" height="900" loading="lazy"><b>{e(MODELS[k][0])}</b><span>{n} parts &middot; GLB &middot; STL</span></a>'
        for k, (slug, n) in MODEL_PAGES.items())
    return ('  <section class="dlbox all">\n    <div class="box-title">Free 3D models to download</div>\n'
            '    <p>Real-scale machines with every part named: download GLB or STL, single parts, or view them in AR.</p>\n'
            f'    <div class="dl-row">{cards}</div>\n'
            f'    <a class="more" href="{MAIN}/3d-models/">All free 3D models &rarr;</a>\n  </section>\n')


def parse(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        raise ValueError(f"{path.name}: missing --- header ---")
    head, body = m.groups()
    meta = {k: [] for k in LIST_KEYS}
    current_list = None
    for line in head.splitlines():
        if not line.strip():
            continue
        if current_list and line.lstrip().startswith("- "):
            meta[current_list].append(line.lstrip()[2:].strip())
            continue
        current_list = None
        key, _, val = line.partition(":")
        key = key.strip().lower()
        val = val.strip()
        if key in SIMPLE_KEYS:
            val = val.split(" #", 1)[0].strip()  # allow trailing comments on simple fields
        if key in LIST_KEYS:
            current_list = key
            continue
        meta[key] = val
    for req in ("title", "date", "category", "summary"):
        if not meta.get(req):
            raise ValueError(f"{path.name}: missing '{req}'")
    if meta["category"] not in CATEGORIES:
        raise ValueError(f"{path.name}: unknown category '{meta['category']}'")
    meta["date_obj"] = datetime.strptime(meta["date"], "%Y-%m-%d")
    if meta.get("updated"):
        meta["updated_obj"] = datetime.strptime(meta["updated"], "%Y-%m-%d")
    meta["sources"] = [(s.rpartition("|")[0].strip(), s.rpartition("|")[2].strip()) if "|" in s else (s.strip(), "")
                       for s in meta["sources"]]
    faq = []
    for item in meta["faq"]:
        q, sep, a = item.partition("|")
        if not sep or not q.strip() or not a.strip():
            raise ValueError(f"{path.name}: faq lines must be 'Question | Answer'")
        faq.append((q.strip(), a.strip()))
    meta["faq"] = faq
    meta["slug"] = path.stem
    meta["url"] = f"{BASE}/posts/{path.stem}.html"
    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc"],
                           extension_configs={"toc": {"toc_depth": "2-2"}})
    meta["body_html"] = md.convert(body)
    meta["toc"] = [(t["id"], t["name"]) for t in md.toc_tokens]
    text = re.sub(r"<[^>]+>", " ", meta["body_html"])
    meta["words"] = len(text.split())
    first = re.search(r"<p>(.*?)</p>", meta["body_html"], re.S)
    meta["lede_words"] = len(re.sub(r"<[^>]+>", " ", first.group(1)).split()) if first else 0
    meta["minutes"] = max(1, round(meta["words"] / WORDS_PER_MIN))
    meta["draft"] = meta.get("draft", "false").lower() == "true"
    return meta


def kicker(p):
    k = CATEGORIES[p["category"]]
    if p["category"] == "news" and p.get("tag") in TAGS:
        k += " · " + TAGS[p["tag"]]
    return k


def nice_date(d):
    return d.strftime("%d %b %Y").lstrip("0")


def youtube_id(url):
    u = urlparse(url)
    if u.hostname in ("youtu.be",):
        return u.path.strip("/") or None
    if u.hostname and "youtube" in u.hostname:
        if u.path.startswith(("/embed/", "/shorts/")):
            return u.path.split("/")[2]
        return parse_qs(u.query).get("v", [None])[0]
    return None


def ld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>")


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Parth Parmar">
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="Engine-X">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="{ogtype}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{image}">
{extra}
<link rel="alternate" type="application/rss+xml" title="Engine-X Blog" href="{base}/rss.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}/style.css">
{jsonld}
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6280235034781345" crossorigin="anonymous"></script>
</head>
<body>
"""

FOOT = """<footer>
  <a href="{home}/">Engine&#8209;X</a> · <a href="{home}/blog">Journal</a> · <a href="{home}/atlas">Atlas</a> · <a href="{home}/about">About</a> · <a href="{home}/privacy">Privacy</a> · <a href="{home}/disclaimer">Disclaimer</a> — engineered by Parth Parmar.
  · <a href="{base}/rss.xml">RSS</a>
</footer>
</body>
</html>
"""

POST_JS = """<script>
(function(){
  var toc = document.querySelector('.toc');
  if (toc && window.matchMedia('(min-width: 1200px)').matches) toc.open = true;
  if (toc) {
    var links = toc.querySelectorAll('a');
    var heads = Array.prototype.map.call(links, function(a){ return document.getElementById(a.getAttribute('href').slice(1)); });
    function mark(){
      var cur = 0;
      heads.forEach(function(h, i){ if (h && h.getBoundingClientRect().top < 140) cur = i; });
      links.forEach(function(a, i){ a.classList.toggle('on', i === cur); });
    }
    window.addEventListener('scroll', mark, {passive:true}); mark();
    links.forEach(function(a){ a.addEventListener('click', function(){ if (!window.matchMedia('(min-width: 1200px)').matches) toc.open = false; }); });
  }
  var copy = document.querySelector('.share-copy');
  if (copy) copy.addEventListener('click', function(){
    var url = copy.dataset.url;
    function done(){ copy.textContent = 'Link copied'; setTimeout(function(){ copy.textContent = 'Copy link'; }, 1800); }
    if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, function(){ prompt('Copy this link:', url); });
    else prompt('Copy this link:', url);
  });
  var bar = document.querySelector('.progress');
  if (bar) window.addEventListener('scroll', function(){
    var h = document.documentElement, max = h.scrollHeight - h.clientHeight;
    bar.style.transform = 'scaleX(' + (max > 0 ? h.scrollTop / max : 0) + ')';
  }, {passive:true});
})();
</script>
"""


def page_head(title, desc, canonical, ogtype="website", image=None, jsonld="", extra=""):
    return HEAD.format(title=e(title), desc=e(desc), canonical=e(canonical), ogtype=ogtype,
                       image=e(image or LOGO), base=BASE, jsonld=jsonld, extra=extra)


def related_posts(p, posts, n=3):
    others = [q for q in posts if q["slug"] != p["slug"]]

    def score(q):
        s = 0
        if q["category"] == p["category"]:
            s += 2
        if p.get("tag") and q.get("tag") == p.get("tag"):
            s += 2
        if p.get("model") and q.get("model") == p.get("model"):
            s += 3
        return s
    ranked = sorted(others, key=lambda q: (score(q), q["date"]), reverse=True)
    return ranked[:n]


def mini_cards(items):
    out = ['  <div class="mini-list">\n']
    for q in items:
        out.append(f'    <a class="mini" href="{e(q["url"])}"><span class="kicker">{e(kicker(q))}</span>'
                   f'<span class="mini-title">{e(q["title"])}</span>'
                   f'<span class="mini-date">{nice_date(q["date_obj"])} · {q["minutes"]} min read</span></a>\n')
    out.append("  </div>\n")
    return "".join(out)


def post_schema(p, image_url):
    author = {"@type": "Person", "@id": f"{MAIN}/#parth", "name": AUTHOR["name"], "url": AUTHOR["url"],
              "jobTitle": AUTHOR["job"], "knowsAbout": AUTHOR["knows"],
              "sameAs": [AUTHOR["linkedin"], "https://www.reddit.com/user/Parth_MechEng/"]}
    publisher = {"@type": "Organization", "@id": f"{MAIN}/#org", "name": "Engine-X", "url": f"{MAIN}/",
                 "sameAs": ["https://www.linkedin.com/company/engx3d"],
                 "logo": {"@type": "ImageObject", "url": LOGO}}
    article = {
        "@type": "BlogPosting" if p["category"] in ("news", "field-notes") else "Article",
        "@id": p["url"] + "#article",
        "headline": p["title"],
        "description": p["summary"],
        "image": image_url or LOGO,
        "datePublished": p["date"],
        "dateModified": p.get("updated") or p["date"],
        "author": author,
        "publisher": publisher,
        "mainEntityOfPage": {"@type": "WebPage", "@id": p["url"]},
        "isPartOf": {"@type": "Blog", "@id": f"{BASE}/#blog", "name": SITE["title"], "url": f"{BASE}/"},
        "articleSection": CATEGORIES[p["category"]],
        "wordCount": p["words"],
        "timeRequired": f"PT{p['minutes']}M",
        "inLanguage": "en",
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["article > p:first-of-type", ".tldr"]},
    }
    if p.get("keywords"):
        article["keywords"] = [k.strip() for k in p["keywords"].split(",") if k.strip()]
    if p.get("model") in MODELS:
        article["about"] = {"@type": "Thing", "name": MODELS[p["model"]][0]}
    if p["sources"]:
        article["citation"] = [{"@type": "CreativeWork", "name": n, "url": u} for n, u in p["sources"] if u]
    vid = youtube_id(p["video"]) if p.get("video") else None
    if vid:
        article["video"] = {"@type": "VideoObject", "name": p["title"], "description": p["summary"],
                            "embedUrl": f"https://www.youtube-nocookie.com/embed/{vid}",
                            "thumbnailUrl": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
                            "uploadDate": p["date"]}
    graph = [article, {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Engine-X", "item": f"{MAIN}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": p["url"]},
        ]}]
    if p["faq"]:
        graph.append({"@type": "FAQPage", "@id": p["url"] + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faq"]]})
    return ld({"@context": "https://schema.org", "@graph": graph})


TITLE_SUFFIX = " | Engine-X Blog"
TITLE_MAX, DESC_MAX = 60, 155


def seo_title(p):
    """<title> for a post: seo_title if given, else the headline. The blog
    suffix is only added when the whole thing still fits in Google's ~60
    characters, so search results do not cut the title off."""
    t = (p.get("seo_title") or p["title"]).strip()
    return t + TITLE_SUFFIX if len(t) + len(TITLE_SUFFIX) <= TITLE_MAX else t


def seo_description(p):
    """Meta description: seo_description if given, else the summary,
    shortened on a word boundary to fit Google's ~155 characters."""
    d = (p.get("seo_description") or p["summary"]).strip()
    if len(d) <= DESC_MAX:
        return d
    cut = d[:DESC_MAX - 1].rsplit(" ", 1)[0].rstrip(",;:—-– ")
    return cut + "…"


def image_size(rel):
    """(width, height) of a local SVG/PNG/JPG asset, or None. Lets the browser
    reserve space for the hero image so the page does not jump (CLS)."""
    path = ROOT / rel
    if not path.exists():
        return None
    if path.suffix.lower() == ".svg":
        head = path.read_text(encoding="utf-8", errors="ignore")[:2000]
        m = re.search(r'viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)', head)
        return (round(float(m.group(1))), round(float(m.group(2)))) if m else None
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None


def render_post(p, posts):
    image_url = f"{BASE}/{p['image']}" if p.get("image") else None
    extra = (f'<meta property="article:published_time" content="{p["date"]}">\n'
             f'<meta property="article:modified_time" content="{p.get("updated") or p["date"]}">\n'
             f'<meta property="article:section" content="{e(CATEGORIES[p["category"]])}">')
    out = [page_head(seo_title(p), seo_description(p), p["url"], "article", image_url,
                     post_schema(p, image_url), extra)]
    out.append('<div class="progress" aria-hidden="true"></div>\n<div class="wrap">\n')

    # breadcrumbs
    out.append('  <nav class="crumbs" aria-label="Breadcrumb">'
               f'<a href="{MAIN}/">Engine&#8209;X</a><span>›</span>'
               f'<a href="{BASE}/">Blog</a><span>›</span>'
               f'<span class="here">{e(CATEGORIES[p["category"]])}</span></nav>\n')
    out.append(f'  <div class="kicker">{e(kicker(p))}</div>\n')
    out.append(f'  <h1>{e(p["title"])}</h1>\n')

    # author, dates, reading time
    meta = (f'By <a class="author-link" href="{AUTHOR["url"]}" rel="author">{AUTHOR["name"]}</a>'
            f' · <time datetime="{p["date"]}">{nice_date(p["date_obj"])}</time>')
    if p.get("updated_obj") and p["updated"] != p["date"]:
        meta += f' · Updated <time datetime="{p["updated"]}">{nice_date(p["updated_obj"])}</time>'
    meta += f' · {p["minutes"]} min read'
    out.append(f'  <p class="meta">{meta}</p>\n')

    if image_url:
        size = image_size(p["image"])
        dims = f' width="{size[0]}" height="{size[1]}"' if size else ""
        out.append(f'  <figure class="hero"><img src="{e(image_url)}" alt="{e(p.get("image_alt", ""))}"{dims}>'
                   + (f'<figcaption>{e(p["image_credit"])}</figcaption>' if p.get("image_credit") else "")
                   + "</figure>\n")

    # top summary + key takeaways
    out.append('  <section class="brief"><div class="box-title">In short</div>\n'
               f'    <p>{e(p["summary"])}</p>\n')
    if p["takeaways"]:
        out.append('    <div class="box-sub">Key takeaways</div><ul>\n')
        for t in p["takeaways"]:
            out.append(f"      <li>{e(t)}</li>\n")
        out.append("    </ul>\n")
    out.append("  </section>\n")

    # contents
    if len(p["toc"]) >= 3:
        out.append('  <details class="toc"><summary>Contents</summary><ol>\n')
        for anchor, name in p["toc"]:
            out.append(f'    <li><a href="#{e(anchor)}">{name}</a></li>\n')
        out.append("  </ol></details>\n")

    out.append(f'  <article>{p["body_html"]}</article>\n')

    vid = youtube_id(p["video"]) if p.get("video") else None
    if vid:
        out.append('  <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/'
                   f'{e(vid)}" title="{e(p["title"])}" loading="lazy" allowfullscreen '
                   'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture"></iframe></div>\n')

    if p.get("field_note"):
        out.append(f'  <aside class="field-note"><span>From the field · {AUTHOR["name"]}</span> {e(p["field_note"])}</aside>\n')
    if p.get("tldr"):
        out.append(f'  <div class="tldr"><span>TL;DR</span> {e(p["tldr"])}</div>\n')

    if p["faq"]:
        out.append('  <section class="faq" id="faq"><h2>Frequently asked questions</h2>\n')
        for q, a in p["faq"]:
            out.append(f"    <details><summary>{e(q)}</summary><p>{e(a)}</p></details>\n")
        out.append("  </section>\n")

    if p["sources"]:
        out.append('  <div class="sources"><div class="sources-title">Sources</div><ul>\n')
        for name, url in p["sources"]:
            out.append(f'    <li><a href="{e(url)}" rel="noopener" target="_blank">{e(name)}</a></li>\n')
        out.append("  </ul></div>\n")

    out.append(download_box(p.get("model")))

    # share
    enc_url, enc_title = quote(p["url"], safe=""), quote(p["title"], safe="")
    out.append('  <div class="share"><span class="share-label">Share</span>'
               f'<a href="https://www.linkedin.com/sharing/share-offsite/?url={enc_url}" target="_blank" rel="noopener">LinkedIn</a>'
               f'<a href="https://wa.me/?text={enc_title}%20{enc_url}" target="_blank" rel="noopener">WhatsApp</a>'
               f'<a href="https://twitter.com/intent/tweet?url={enc_url}&amp;text={enc_title}" target="_blank" rel="noopener">X</a>'
               f'<button type="button" class="share-copy" data-url="{e(p["url"])}">Copy link</button></div>\n')

    # related machines (3D atlas) + services offer
    model = p.get("model")
    order = ([model] if model in MODELS else []) + [k for k in MODELS if k != model]
    out.append('  <section class="extras">\n'
               '    <div class="panel"><div class="box-title">'
               + (f"See the {e(MODELS[model][0])} in 3D" if model in MODELS else "Explore machines in 3D")
               + "</div>\n")
    for k in order:
        name, desc = MODELS[k]
        cls = "machine on" if k == model else "machine"
        out.append(f'      <a class="{cls}" href="{MAIN}/atlas#m={k}"><b>{e(name)}</b><span>{e(desc)}</span></a>\n')
    out.append('      <p class="small">Explode, X&#8209;ray and cut them open, free in your browser.</p>\n    </div>\n')
    out.append('    <div class="panel offer"><div class="box-title">Need your machine in 3D?</div>\n'
               '      <p>Engine&#8209;X builds interactive 3D websites for pumps, valves, gearboxes and other '
               'machines that buyers can rotate, explode and section, plus 3D explainers for colleges and trainers. Free quote within 24 hours, 3 rounds of revisions included.</p>\n'
               f'      <a class="btn" href="{MAIN}/services">Get a free quote &rarr;</a>\n'
               f'      <a class="more" href="{MAIN}/services">What\'s included</a>\n    </div>\n'
               "  </section>\n")

    # author bio
    out.append('  <section class="bio"><div class="avatar" aria-hidden="true">PP</div><div>\n'
               f'    <div class="bio-name"><a href="{AUTHOR["url"]}" rel="author">{AUTHOR["name"]}</a></div>\n'
               f'    <p>{e(AUTHOR["bio"])}</p>\n'
               f'    <a href="{AUTHOR["url"]}">About</a> · <a href="{AUTHOR["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a>'
               f' · <a href="{MAIN}/contact">Contact</a>\n'
               "  </div></section>\n")

    related = related_posts(p, posts)
    if related:
        out.append('  <section class="more-posts"><h2>Related posts</h2>\n' + mini_cards(related) + "  </section>\n")
    seen = {p["slug"]} | {q["slug"] for q in related}
    latest = [q for q in posts if q["slug"] not in seen][:3]
    if latest:
        out.append('  <section class="more-posts"><h2>Latest from the blog</h2>\n' + mini_cards(latest) + "  </section>\n")

    out.append("</div>\n")
    out.append(POST_JS)
    out.append(FOOT.format(home=MAIN, base=BASE))
    return "".join(out)


def render_index(posts):
    schema = ld({"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": f"{BASE}/#blog", "name": SITE["title"], "description": SITE["description"],
         "url": f"{BASE}/", "inLanguage": "en",
         "publisher": {"@type": "Organization", "@id": f"{MAIN}/#org", "name": "Engine-X", "url": f"{MAIN}/",
                       "logo": {"@type": "ImageObject", "url": LOGO}},
         "author": {"@type": "Person", "@id": f"{MAIN}/#parth", "name": AUTHOR["name"], "url": AUTHOR["url"]},
         "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": p["url"],
                       "datePublished": p["date"]} for p in posts[:20]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Engine-X", "item": f"{MAIN}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/"}]}]})
    out = [page_head(SITE.get("seo_title") or SITE["title"], SITE["description"], f"{BASE}/", jsonld=schema)]
    out.append('<div class="wrap">\n')
    out.append('  <nav class="crumbs" aria-label="Breadcrumb">'
               f'<a href="{MAIN}/">Engine&#8209;X</a><span>›</span><span class="here">Blog</span></nav>\n')
    out.append(f'  <h1>{e(SITE["title"])}</h1>\n')
    out.append(f'  <p class="sub">{e(SITE["description"])}</p>\n')
    out.append('  <div class="filters" role="tablist">\n')
    for key, label in FILTERS:
        cls = "chip on" if key == "all" else "chip"
        out.append(f'    <button class="{cls}" data-f="{key}">{e(label)}</button>\n')
    out.append('  </div>\n  <div id="list">\n')
    for p in posts:
        out.append(f'  <a class="card" data-c="{p["category"]}" href="{e(p["url"])}">\n'
                   f'    <div class="kicker">{e(kicker(p))} <span class="date">· {nice_date(p["date_obj"])} · {p["minutes"]} min read</span></div>\n'
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
    out.append(FOOT.format(home=MAIN, base=BASE))
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
    urls += [f"<url><loc>{e(p['url'])}</loc><lastmod>{p.get('updated') or p['date']}</lastmod></url>" for p in posts]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            + "".join(urls) + "</urlset>\n")


def render_llms(posts):
    lines = [f"# {SITE['title']}", "", f"> {SITE['description']}", "",
             f"Every post on {BASE}/ with a one-line answer. Main site guide: {MAIN}/llms.txt", "", "## Posts", ""]
    for p in posts:
        lines.append(f"- [{p['title']}]({p['url']}): {p.get('tldr') or p['summary']}")
    lines += ["", "## Optional", "", f"- [Full text of key facts and FAQ answers]({BASE}/llms-full.txt)", ""]
    return "\n".join(lines)


def render_llms_full(posts):
    out = [f"# {SITE['title']} - key facts and answers", "",
           f"> Author: Parth Parmar, Engine-X ({MAIN}). Each post: answer, key facts, FAQ.", ""]
    for p in posts:
        out += [f"## {p['title']}", "", f"URL: {p['url']}", f"Published: {p['date']}"
                + (f" (updated {p['updated']})" if p.get("updated") else ""), "",
                p.get("tldr") or p["summary"], ""]
        if p.get("field_note"):
            out += [f"First-hand note from Parth Parmar: {p['field_note']}", ""]
        out += [f"- {t}" for t in p["takeaways"]]
        if p["takeaways"]:
            out.append("")
        for q, a in p["faq"]:
            out += [f"Q: {q}", f"A: {a}", ""]
    return "\n".join(out)


def long_answers(body_html, limit=60):
    """(question, words) for question headings whose first paragraph is longer
    than `limit` words. Answer engines quote 40-60 word answers."""
    out = []
    for m in re.finditer(r"<h([23])[^>]*>((?:(?!</?h[1-6]).)*?)</h\1>\s*<p>(.*?)</p>", body_html, re.S):
        q = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if not q.endswith("?"):
            continue
        n = len(re.sub(r"<[^>]+>", " ", m.group(3)).split())
        if n > limit:
            out.append((q, n))
    return out


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
        (OUT / "posts" / f"{p['slug']}.html").write_text(render_post(p, posts), encoding="utf-8")
    (OUT / "index.html").write_text(render_index(posts), encoding="utf-8")
    (OUT / "rss.xml").write_text(render_rss(posts), encoding="utf-8")
    (OUT / "sitemap.xml").write_text(render_sitemap(posts), encoding="utf-8")
    (OUT / "llms.txt").write_text(render_llms(posts), encoding="utf-8")
    (OUT / "llms-full.txt").write_text(render_llms_full(posts), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    feed = [{"title": p["title"], "url": p["url"], "date": p["date"], "category": p["category"],
             "category_label": CATEGORIES[p["category"]], "tag": p.get("tag", ""),
             "kicker": kicker(p), "summary": p["summary"], "minutes": p["minutes"]} for p in posts[:30]]
    (OUT / "feed.json").write_text(json.dumps({"base": BASE, "posts": feed}, ensure_ascii=False, indent=1),
                                   encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    if SITE.get("custom_domain"):
        (OUT / "CNAME").write_text(SITE["custom_domain"] + "\n")
    for p in posts:
        if p["lede_words"] > 60:  # WRITING_GUIDE: answer-first paragraph is 40-60 words
            print(f"warning: {p['slug']}: first paragraph is {p['lede_words']} words, keep it to 40-60")
        if not p.get("seo_title") or not p.get("seo_description"):
            print(f"warning: {p['slug']}: add seo_title (max 60) and seo_description (120-155), see WRITING_GUIDE.md")
        elif len(seo_title(p)) > TITLE_MAX or len(p["seo_description"]) > DESC_MAX:
            print(f"warning: {p['slug']}: seo_title is {len(seo_title(p))} chars / seo_description {len(p['seo_description'])} chars, keep to 60 / 155")
        for q, n in long_answers(p["body_html"]):
            print(f"warning: {p['slug']}: answer under '{q}' is {n} words, keep the first paragraph to 40-60")
    print(f"built {len(posts)} posts -> {OUT}")


if __name__ == "__main__":
    main()
