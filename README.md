# engine-x-content

Content for the **Engine-X Blog** — machine news, 3D machine guides, engineering case studies and field notes by Parth Parmar.

- Posts live in `posts/` as Markdown files (see the header format at the top of `build.py`).
- Images and diagrams live in `assets/`.
- On every push to `main`, GitHub Actions runs `build.py` and publishes the static site to GitHub Pages.
- `feed.json` on the published site lists the latest posts; the Engine-X site (engx3d.com/blog.html) reads it to show the newest articles.

See `WRITING_GUIDE.md` for content rules.

© Parth Parmar. All rights reserved.
