"""Tell Bing, Yandex and other IndexNow engines (and through Bing, ChatGPT search)
that pages are new or changed, so they re-crawl them within minutes.

  python indexnow.py posts/2026-10-26-x.md ...   # ping these posts
  python indexnow.py --all                        # ping every post + main-site page
  add --dry-run to print the URLs without sending
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
BASE = SITE["base_url"].rstrip("/")
MAIN = SITE["main_site"].rstrip("/")
KEY = SITE["indexnow_key"]
HOST = MAIN.split("//", 1)[1]


def post_url(path):
    path = Path(path)
    if not path.exists() or re.search(r"^draft:\s*true", path.read_text(encoding="utf-8"), re.M | re.I):
        return None  # deleted or draft: nothing to announce
    return f"{BASE}/posts/{path.stem}.html"


def main_site_urls():
    xml = urllib.request.urlopen(f"{MAIN}/sitemap.xml", timeout=30).read().decode()
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def main(args):
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if "--all" in args:
        urls = [post_url(p) for p in sorted((ROOT / "posts").glob("*.md"))] + main_site_urls()
    else:
        urls = [post_url(a) for a in args if a.endswith(".md")]
    urls = [u for u in urls if u]
    if not urls:
        print("indexnow: nothing to ping")
        return
    urls = sorted(set(urls + [f"{BASE}/", f"{BASE}/llms.txt", f"{BASE}/llms-full.txt"]))
    print("\n".join(urls))
    if dry:
        return
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"{MAIN}/{KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:  # raises on 4xx/5xx so the job shows red
        print(f"indexnow: {r.status} for {len(urls)} URLs")


if __name__ == "__main__":
    main(sys.argv[1:])
