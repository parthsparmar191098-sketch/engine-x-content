"""Tell Bing, Yandex and other IndexNow engines (and through Bing, ChatGPT search)
that pages are new or changed, so they re-crawl them within minutes.

  python indexnow.py posts/2026-10-26-x.md ...   # ping these posts
  python indexnow.py --all                        # ping every post + main-site page
  python indexnow.py https://engx3d.com/page ...  # ping exact URLs
  add --dry-run to print the URLs without sending
"""
import json
import re
import sys
import urllib.error
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
    req = urllib.request.Request(f"{MAIN}/sitemap.xml", headers={"User-Agent": "Mozilla/5.0 (compatible; Engine-X-IndexNow/1.0)"})
    try:
        xml = urllib.request.urlopen(req, timeout=30).read().decode()
    except Exception as ex:  # Cloudflare may challenge CI runners; posts still get pinged
        print(f"::warning::could not read {MAIN}/sitemap.xml ({ex}); pinging blog posts only")
        return []
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def main(args):
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if "--all" in args:
        urls = [post_url(p) for p in sorted((ROOT / "posts").glob("*.md"))] + main_site_urls()
    else:
        urls = [post_url(a) if a.endswith(".md") else a for a in args
                if a.endswith(".md") or a.startswith(MAIN + "/")]
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
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"::notice::indexnow: {r.status} for {len(urls)} URLs")
    except urllib.error.HTTPError as ex:  # print IndexNow's reason, then fail the job
        print(f"::error::indexnow: HTTP {ex.code} {ex.read().decode(errors='replace')[:300]}")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
