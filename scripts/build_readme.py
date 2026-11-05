"""Rebuild README.md from the portfolio's Pages CMS data (a1if/a1if.github.io/_data).

Run by .github/workflows/sync-readme.yml. Edit your content in Pages CMS, not in README.md:
manual edits here are overwritten on the next sync.
"""
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

import yaml

SITE = "https://a1if.github.io"
RAW = "https://raw.githubusercontent.com/a1if/a1if.github.io/main/"
LOCAL = os.environ.get("SITE_DIR")  # optional local checkout, for testing


def fetch(path):
    if LOCAL:
        with open(os.path.join(LOCAL, path), encoding="utf-8") as f:
            return f.read()
    with urllib.request.urlopen(RAW + path, timeout=30) as r:
        return r.read().decode("utf-8")


def data(name):
    return yaml.safe_load(fetch(f"_data/{name}.yml")) or []


def absolute(url):
    return url if "://" in url or url.startswith("mailto:") else f"{SITE}/{url.lstrip('/')}"


def latest_posts(limit=3):
    try:
        with urllib.request.urlopen(f"{SITE}/feed.xml", timeout=30) as r:
            root = ET.fromstring(r.read())
    except Exception:
        return []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    posts = []
    for e in root.findall("a:entry", ns)[:limit]:
        link = e.find("a:link", ns)
        posts.append({
            "title": (e.findtext("a:title", "", ns) or "").strip(),
            "url": link.get("href") if link is not None else SITE + "/blog/",
            "date": (e.findtext("a:published", "", ns) or "")[:10],
        })
    return posts


EMOJI = {"linkedin": "💼", "email": "📫", "cv": "📄", "x": "𝕏", "orcid": "🆔",
         "scholar": "🎓", "website": "🌐", "other": "🔗"}


WORDS = {"llms": "LLMs", "llm": "LLM", "rag": "RAG", "ml": "ML", "dl": "DL", "ai": "AI",
         "apis": "APIs", "api": "API", "mlops": "MLOps", "nlp": "NLP"}


def nice_category(cat):
    words = [WORDS.get(w.lower(), w) for w in str(cat).split()]
    if words and words[0] == str(cat).split()[0]:
        words[0] = words[0][:1].upper() + words[0][1:]
    return " ".join(words)


def build():
    profile = yaml.safe_load(fetch("_data/profile.yml")) or {}
    projects, contact = data("projects"), data("contact")
    pubs, skills, education = data("publications"), data("skills"), data("education")
    location = (profile.get("status") or "").split(" · ")
    city = next((p for p in location if "," in p or p.istitle()), "")

    out = [f"## Hi, I'm {profile.get('name', 'Alif Tasbir')} 👋", ""]
    out += [f"**{profile.get('role', '')}**" + (f", based in {city}" if city else ""), ""]
    out += [" ".join(str(profile.get("about", "")).split()), ""]

    links = [f"🌐 **Portfolio:** [{SITE.split('//')[1]}]({SITE})"]
    if not any((c.get("icon") == "cv") for c in contact):
        # The CV button sits at the top of the homepage rather than in the contact buttons.
        links.append(f"📄 **CV:** [Download PDF]({SITE}/Alif_Tasbir_CV.pdf)")
    for c in contact:
        icon = c.get("icon") or "other"
        if icon == "github":
            continue  # this README already lives on GitHub
        label = c.get("label", "")
        name = {"email": "Email", "cv": "CV", "linkedin": "LinkedIn"}.get(icon, label)
        if icon == "cv":
            text = "Download PDF"
        elif icon == "email":
            text = c["url"].replace("mailto:", "")
        elif icon == "orcid":
            text = c["url"].rstrip("/").rsplit("/", 1)[-1]
        else:
            text = re.sub(r"^https?://(www\.)?", "", c["url"]).rstrip("/")
        links.append(f"{EMOJI.get(icon, '🔗')} **{name}:** [{text}]({absolute(c['url'])})")
    out += ["  \n".join(links), "", "---", ""]

    posts = latest_posts()
    if posts:
        out += ["### ✍️ Latest posts", ""]
        out += [f"- [{p['title']}]({p['url']})" + (f" · {p['date']}" if p["date"] else "") for p in posts]
        out += ["", f"[All posts →]({SITE}/blog/)", ""]

    for p in [p for p in projects if p.get("featured")]:
        out += [f"### 🔬 Featured: {p['title']}", ""]
        if p.get("description"):
            out += [" ".join(str(p["description"]).split()), ""]
        out += [f"- {pt}" for pt in p.get("points") or []]
        if p.get("points"):
            out.append("")
        btns = []
        for i, l in enumerate(p.get("links") or []):
            label = l.get("label", "").replace(" ↗", "")
            btns.append(f"**[▶ {label}]({l['url']})**" if l.get("primary") else f"[{label}]({l['url']})")
        if btns:
            out += [" · ".join(btns), ""]

    others = [p for p in projects if not p.get("featured")]
    if others:
        out += ["### 🛠 Other projects", "", "| Project | What it does | Stack |", "|---|---|---|"]
        for p in others:
            url = p.get("url") or ((p.get("links") or [{}])[0].get("url", ""))
            name = f"[{p['title']}]({url})" if url else p["title"]
            parts = ([p["description"]] if p.get("description") else []) + list(p.get("points") or [])
            what = "<br>".join(" ".join(str(x).split()) for x in parts)
            stack = (p.get("stack") or p.get("language") or "").replace(" · ", ", ")
            out.append(f"| {name} | {what.replace('|', '/')} | {stack} |")
        out.append("")

    if pubs:
        out += ["### 📄 Publications", ""]
        for pub in pubs:
            venue = (pub.get("venue") or "").split(" · ")
            year = next((v for v in reversed(venue) if re.fullmatch(r"\d{4}", v.strip())), "")
            title = f"[{pub['title']}]({pub['url']})" if pub.get("url") else pub["title"]
            out.append(f"- {title}, *{venue[0]}*" + (f" ({year})" if year else ""))
        out.append("")

    if skills:
        out += ["### 🧰 Tech stack", ""]
        rows = [f"**{nice_category(s['category'])}:** " + " ".join(str(s["items"]).split()) for s in skills]
        out += ["  \n".join(rows), ""]
        out += ["<p>"]
        icons = ["python/python-original", "pytorch/pytorch-original", "tensorflow/tensorflow-original",
                 "scikitlearn/scikitlearn-original", "fastapi/fastapi-original", "docker/docker-original",
                 "streamlit/streamlit-original"]
        out += [f'<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{i}.svg" width="36" alt="{i.split("/")[0]}"/>'
                + ("&nbsp;" if n < len(icons) - 1 else "") for n, i in enumerate(icons)]
        out += ["</p>", ""]

    if education:
        out += ["### 🎓 Education", ""]
        for e in education:
            inst = (e.get("institution") or "").replace(" · ", ", ")
            line = f"- **{e['degree']}**, {inst}" + (f" ({e['dates'].replace(' – ', '–')})" if e.get("dates") else "")
            if e.get("grade"):
                line += f", **{e['grade']}**"
            out.append(line)
        out.append("")

    out += ["<sub>This README is generated from my portfolio's content and updates automatically.</sub>", ""]
    return "\n".join(out)


if __name__ == "__main__":
    text = build()
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
