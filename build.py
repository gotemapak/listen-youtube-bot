"""Static site generator: content.py → docs/ (served by GitHub Pages).

Usage: python3 build.py            # uses SITE_URL below
       SITE_URL=https://example.com python3 build.py

When a custom domain is attached, set SITE_URL to it and rebuild — every
canonical, hreflang, sitemap and internal link follows. CNAME is written
only for a custom domain.
"""

import html
import json
import os
import shutil
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from content import BOT, EN, PAGES, RU, UI

SITE_URL = os.environ.get("SITE_URL", "https://gotemapak.github.io/listen-youtube-bot").rstrip("/")
BASE = urlparse(SITE_URL).path.rstrip("/")  # "" on a custom domain
GITHUB_IO = urlparse(SITE_URL).hostname.endswith(".github.io")
# Search-console verification tokens (paste the content="" value only).
GOOGLE_VERIFY = os.environ.get("GOOGLE_VERIFY", "8WulXXeHGJh3L7MC95MB2Re9TBSGH2N17WCtMh0Dzd8")
YANDEX_VERIFY = os.environ.get("YANDEX_VERIFY", "")
BING_VERIFY = os.environ.get("BING_VERIFY", "")
# Yandex Metrika counter id (digits). Empty → no counter, CTA clicks still work.
METRIKA_ID = os.environ.get("METRIKA_ID", "")

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
TODAY = date.today().isoformat()
OG_LOCALE = {RU: "ru_RU", EN: "en_US"}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def url(path: str) -> str:
    return SITE_URL + path


def link(path: str) -> str:
    return BASE + path


def rebase(fragment: str) -> str:
    """Root-relative links in content.py → links under BASE (github.io subpath)."""
    return fragment.replace('href="/', f'href="{BASE}/')


def bot_link(src: str) -> str:
    return f"https://t.me/{BOT}?start={src}"


def twin(page: dict) -> dict:
    return next(p for p in PAGES if p["pair"] == page["pair"] and p["lang"] != page["lang"])


def json_ld(page: dict) -> str:
    lang = page["lang"]
    app = {
        "@type": "SoftwareApplication",
        "@id": url("/#app"),
        "name": "Listen YouTube — Telegram bot",
        "alternateName": f"@{BOT}",
        "url": f"https://t.me/{BOT}",
        "applicationCategory": "MultimediaApplication",
        "operatingSystem": "Telegram (Android, iOS, Windows, macOS, Linux, Web)",
        "inLanguage": ["ru", "en"],
        "image": url(f"/img/welcome-{lang}.png"),
        "description": next(p for p in PAGES if p["pair"] == "home" and p["lang"] == lang)["description"],
        "featureList": [
            "YouTube to audio (MP3) in Telegram",
            "Background playback and screen-off listening",
            "Video transcript from YouTube subtitles",
            "Playlists and videos up to 11 hours",
        ],
        "offers": [
            {"@type": "Offer", "price": "0", "priceCurrency": "RUB", "description": "First 2 links free (one-time)"},
            {"@type": "Offer", "price": "299", "priceCurrency": "RUB", "description": "Unlimited, monthly"},
            {"@type": "Offer", "price": "1990", "priceCurrency": "RUB", "description": "Unlimited, yearly"},
        ],
    }
    graph = [
        {
            "@type": "WebSite",
            "@id": url("/#website"),
            "url": url("/"),
            "name": "Listen YouTube bot",
            "inLanguage": ["ru", "en"],
        },
        {
            "@type": "WebPage",
            "@id": url(page["path"]),
            "url": url(page["path"]),
            "name": page["title"],
            "description": page["description"],
            "inLanguage": lang,
            "isPartOf": {"@id": url("/#website")},
            "about": {"@id": url("/#app")},
            "dateModified": TODAY,
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in page["faq"]
            ],
        },
    ]
    if page["pair"] == "home":
        graph.insert(1, app)
    else:
        home = next(p for p in PAGES if p["pair"] == "home" and p["lang"] == lang)
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": home["nav"], "item": url(home["path"])},
                {"@type": "ListItem", "position": 2, "name": page["nav"], "item": url(page["path"])},
            ],
        })
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    return data.replace("</", "<\\/")


def head(page: dict, title: str, description: str, canonical: str | None) -> str:
    lang = page["lang"]
    lines = [
        "<!doctype html>",
        f'<html lang="{lang}">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(description)}">',
        '<meta name="theme-color" content="#0b0b0d">',
        f'<link rel="icon" href="{link("/favicon.svg")}" type="image/svg+xml">',
        f'<link rel="stylesheet" href="{link("/style.css")}">',
    ]
    if canonical is None:
        lines.append('<meta name="robots" content="noindex">')
    else:
        other = twin(page)
        lines += [
            f'<link rel="canonical" href="{canonical}">',
            f'<link rel="alternate" hreflang="{lang}" href="{canonical}">',
            f'<link rel="alternate" hreflang="{other["lang"]}" href="{url(other["path"])}">',
            f'<link rel="alternate" hreflang="x-default" href="{url(page["path"] if lang == RU else other["path"])}">',
            f'<meta property="og:type" content="website">',
            f'<meta property="og:site_name" content="Listen YouTube bot">',
            f'<meta property="og:title" content="{esc(title)}">',
            f'<meta property="og:description" content="{esc(description)}">',
            f'<meta property="og:url" content="{canonical}">',
            f'<meta property="og:image" content="{url(f"/img/welcome-{lang}.png")}">',
            '<meta property="og:image:width" content="1280">',
            '<meta property="og:image:height" content="720">',
            f'<meta property="og:locale" content="{OG_LOCALE[lang]}">',
            f'<meta property="og:locale:alternate" content="{OG_LOCALE[other["lang"]]}">',
            '<meta name="twitter:card" content="summary_large_image">',
            f'<link rel="alternate" type="text/plain" title="llms.txt" href="{link("/llms.txt")}">',
            f'<script type="application/ld+json">\n{json_ld(page)}\n</script>',
        ]
        for name, token in (("google-site-verification", GOOGLE_VERIFY),
                            ("yandex-verification", YANDEX_VERIFY),
                            ("msvalidate.01", BING_VERIFY)):
            if token:
                lines.append(f'<meta name="{name}" content="{esc(token)}">')
    if METRIKA_ID:
        lines.append(metrika())
    lines.append("</head>")
    return "\n".join(lines)


def metrika() -> str:
    """Yandex Metrika tag. CTA clicks are sent as the goal `tg_click` (see CTA_JS)."""
    return f"""<script>
(function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};
m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})
(window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
ym({METRIKA_ID}, "init", {{clickmap:true, trackLinks:true, accurateTrackBounce:true, webvisor:true}});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/{METRIKA_ID}" style="position:absolute; left:-9999px;" alt=""></div></noscript>"""


# ES5 only (old Android browsers / iOS 9+): no arrows, const, fetch or
# IntersectionObserver. Does three things:
#  - ad source passthrough: /?s=ya_lectures → every bot link gets
#    ?start=ya_lectures, so /stats shows which campaign brought the user
#    (Telegram allows [A-Za-z0-9_-], max 64);
#  - Metrika goal `tg_click` on every bot link + reveal the "Telegram didn't
#    open?" hint (Telegram is throttled in Russia; some clicks go nowhere);
#  - sticky bottom CTA on phones once the hero button has scrolled away.
CTA_JS = """<script>
(function(){
  var m = /[?&](?:s|utm_campaign)=([A-Za-z0-9_-]{1,40})/.exec(location.search);
  var links = document.querySelectorAll('a[href^="https://t.me/"]');
  var i;
  for (i = 0; i < links.length; i++) {
    if (m) links[i].href = /start=/.test(links[i].href)
      ? links[i].href.replace(/start=[^&]*/, 'start=' + m[1])
      : links[i].href + '?start=' + m[1];
    links[i].onclick = function(){
      if (window.ym && window.YM_ID) { try { ym(window.YM_ID, 'reachGoal', 'tg_click'); } catch (e) {} }
      var fb = document.getElementById('fallback');
      if (fb) setTimeout(function(){ fb.className = 'fallback show'; }, 1500);
    };
  }
  var btn = document.getElementById('copy');
  if (btn) btn.onclick = function(){
    var t = document.getElementById('botname');
    var ok = false;
    try {
      var r = document.createRange(); r.selectNodeContents(t);
      var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
      ok = document.execCommand('copy');
    } catch (e) {}
    if (ok) btn.innerHTML = btn.getAttribute('data-done');
  };
  var hero = document.getElementById('hero-cta'), bar = document.getElementById('sticky');
  if (hero && bar) {
    var check = function(){
      var r = hero.getBoundingClientRect();
      bar.className = (r.bottom < 0) ? 'sticky show' : 'sticky';
    };
    window.addEventListener('scroll', check, false);
    check();
  }
})();
</script>"""


def header(page: dict, switch_path: str) -> str:
    lang, ui = page["lang"], UI[page["lang"]]
    home = next(p for p in PAGES if p["pair"] == "home" and p["lang"] == lang)
    other_lang = EN if lang == RU else RU
    return f"""<header class="top">
<a class="brand" href="{link(home["path"])}"><img src="{link("/favicon.svg")}" width="32" height="32" alt="">Listen YouTube</a>
<nav><a href="{link(switch_path)}" hreflang="{other_lang}" lang="{other_lang}">{ui["lang_switch"]}</a>
<a class="btn btn-sm" href="{bot_link(page["src"])}">{ui["cta_short"]}</a></nav>
</header>"""


def footer(page: dict) -> str:
    lang, ui = page["lang"], UI[page["lang"]]
    links = " · ".join(
        f'<a href="{link(p["path"])}">{esc(p["nav"])}</a>' for p in PAGES if p["lang"] == lang
    )
    return f"""<footer>
<nav>{links}</nav>
<p>{esc(ui["footer"])}</p>
<p><a href="https://t.me/{BOT}">@{BOT}</a></p>
</footer>"""


def render(page: dict) -> str:
    lang, ui = page["lang"], UI[page["lang"]]
    cta = f'<a class="btn" href="{bot_link(page["src"])}">{ui["cta"]}</a>'
    hero_cta = f'<a id="hero-cta" class="btn btn-big" href="{bot_link(page["src"])}">{ui["cta"]}</a>'
    sub = page.get("sub")
    lead_below = f'<p class="lead lead-below">{esc(page["lead"])}</p>' if sub else ""
    steps = "\n".join(f"<li><b>{esc(t)}</b><span>{esc(d)}</span></li>" for t, d in ui["steps"])
    sections = "\n".join(
        f"<section>\n<h2>{esc(h)}</h2>{rebase(body)}\n</section>" for h, body in page["sections"]
    )
    faq = "\n".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in page["faq"]
    )
    related = "\n".join(
        f'<li><a href="{link(p["path"])}">{esc(p["title"])}</a></li>'
        for p in PAGES if p["lang"] == lang and p is not page
    )
    is_home = page["pair"] == "home"
    img_attrs = 'fetchpriority="high"' if is_home else 'loading="lazy"'
    return f"""{head(page, page["title"], page["description"], url(page["path"]))}
<body>
{header(page, twin(page)["path"])}
<main>
<section class="hero">
<h1>{esc(page["h1"])}</h1>
<p class="lead">{esc(sub or page["lead"])}</p>
{hero_cta}
<p class="trust">{esc(ui["trust"])}</p>
<p id="fallback" class="fallback">{esc(ui["fallback"])} <b id="botname">@{BOT}</b> <button id="copy" type="button" data-done="{esc(ui["copied"])}">{esc(ui["copy"])}</button></p>
</section>
<figure class="shot"><img src="{link(f"/img/welcome-{lang}-640.jpg")}" srcset="{link(f"/img/welcome-{lang}-640.jpg")} 640w, {link(f"/img/welcome-{lang}.png")} 1280w" sizes="(max-width: 800px) 100vw, 760px" width="1280" height="720" alt="{esc(ui["img_alt"])}" {img_attrs}></figure>
{lead_below}
<p class="note center">{esc(ui["free_note"])}</p>
<section>
<h2>{ui["how"]}</h2>
<ol class="steps">
{steps}
</ol>
</section>
{sections}
<section class="faq">
<h2>{ui["faq"]}</h2>
{faq}
</section>
<section class="final">
{cta}
</section>
<section>
<h2>{ui["more"]}</h2>
<ul class="related">
{related}
</ul>
</section>
</main>
<div id="sticky" class="sticky"><a class="btn" href="{bot_link(page["src"])}">{ui["cta"]}</a></div>
{footer(page)}
{"<script>window.YM_ID=" + METRIKA_ID + ";</script>" if METRIKA_ID else ""}
{CTA_JS}
</body>
</html>
"""


def render_404() -> str:
    page = next(p for p in PAGES if p["pair"] == "home" and p["lang"] == RU)
    blocks = []
    for lang in (RU, EN):
        ui = UI[lang]
        home = next(p for p in PAGES if p["pair"] == "home" and p["lang"] == lang)
        blocks.append(
            f'<section lang="{lang}"><h1>{ui["nf_title"]}</h1><p>{ui["nf_text"]}</p>'
            f'<p><a class="btn" href="{bot_link(home["src"])}">{ui["cta"]}</a></p>'
            f'<p><a href="{link(home["path"])}">{esc(home["nav"])}</a></p></section>'
        )
    return f"""{head(page, "404", UI[RU]["nf_title"], None)}
<body>
<main>
{"".join(blocks)}
</main>
</body>
</html>
"""


def sitemap() -> str:
    items = []
    for p in PAGES:
        other = twin(p)
        x_default = p if p["lang"] == RU else other
        items.append(f"""<url>
<loc>{url(p["path"])}</loc>
<lastmod>{TODAY}</lastmod>
<xhtml:link rel="alternate" hreflang="{p["lang"]}" href="{url(p["path"])}"/>
<xhtml:link rel="alternate" hreflang="{other["lang"]}" href="{url(other["path"])}"/>
<xhtml:link rel="alternate" hreflang="x-default" href="{url(x_default["path"])}"/>
</url>""")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(items) + "\n</urlset>\n")


def robots() -> str:
    # AI crawlers are welcome: being quoted by ChatGPT / Perplexity / Claude
    # / YandexGPT is the point. Listed explicitly so the intent is obvious.
    return (
        "User-agent: *\nAllow: /\n\n"
        "User-agent: GPTBot\nUser-agent: OAI-SearchBot\nUser-agent: ChatGPT-User\n"
        "User-agent: ClaudeBot\nUser-agent: Claude-SearchBot\nUser-agent: PerplexityBot\n"
        "User-agent: Google-Extended\nUser-agent: Applebot-Extended\nAllow: /\n\n"
        f"Sitemap: {url('/sitemap.xml')}\n"
    )


def llms_txt() -> str:
    lines = [
        "# Listen YouTube — Telegram bot (@Listen_youtubeapp_bot)",
        "",
        "> Telegram bot that turns a YouTube link (video, Short or playlist) into an audio file "
        "in Telegram's player plus the video's transcript. Audio plays in the background and with "
        "the screen off on Android and iPhone, works offline, no YouTube Premium needed. "
        "Bot interface in Russian and English.",
        "",
        f"- Bot: https://t.me/{BOT}",
        "- Pricing: first 2 links free (one-time, no monthly refill); unlimited 299 RUB/month or 1990 RUB/year (/pay in the bot); +5 bonus links and +30 days when an invited friend subscribes",
        "- Limits: videos up to ~11 hours (long ones arrive in parts); playlists arrive in full",
        "- Transcript: from YouTube subtitles (author's, else automatic captions in the original language); none if the video has no subtitles",
        "- Not affiliated with YouTube or Google",
        "",
        "## Guides (English)",
    ]
    lines += [f"- [{p['title']}]({url(p['path'])}): {p['description']}" for p in PAGES if p["lang"] == EN]
    lines += ["", "## Страницы (русский)"]
    lines += [f"- [{p['title']}]({url(p['path'])}): {p['description']}" for p in PAGES if p["lang"] == RU]
    lines += ["", "## FAQ"]
    lines += [f"- {q} {a}" for q, a in next(p for p in PAGES if p["pair"] == "home" and p["lang"] == EN)["faq"]]
    return "\n".join(lines) + "\n"


def write(rel: str, text: str) -> None:
    path = OUT / rel.lstrip("/")
    if rel.endswith("/"):
        path = path / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)
    for page in PAGES:
        write(page["path"], render(page))
    write("/404.html", render_404())
    write("/sitemap.xml", sitemap())
    write("/robots.txt", robots())
    write("/llms.txt", llms_txt())
    write("/.nojekyll", "")
    if not GITHUB_IO:
        write("/CNAME", urlparse(SITE_URL).hostname + "\n")
    print(f"built {len(PAGES)} pages → {OUT} for {SITE_URL}")


if __name__ == "__main__":
    main()
