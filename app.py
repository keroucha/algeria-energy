"""موقع الطاقات المتجددة في الجزائر — Flask."""
import os
import re
import secrets
import time
from collections import defaultdict, deque

from dotenv import load_dotenv
from flask import Flask, Response, abort, redirect, render_template, request, session, url_for

load_dotenv()

import db
from i18n import DEFAULT_LANG, LANGS, RTL, TEXT
from mailer import notify_owner
from news import get_news

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or secrets.token_hex(32)
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax")
db.init()

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]{2,}$")

# حدّ بسيط: 5 محاولات لكل IP كل 10 دقائق
_hits: dict[str, deque] = defaultdict(deque)


def rate_limited(ip: str, limit: int = 5, window: int = 600) -> bool:
    now, q = time.time(), _hits[ip]
    while q and now - q[0] > window:
        q.popleft()
    if len(q) >= limit:
        return True
    q.append(now)
    return False


def pick_lang(value: str | None) -> str:
    return value if value in LANGS else DEFAULT_LANG


def site_url() -> str:
    return (os.getenv("SITE_URL") or request.url_root).rstrip("/")


def ctx(lang: str) -> dict:
    return {"site_url": site_url(), "lang": lang, "t": TEXT[lang], "dir": "rtl" if lang in RTL else "ltr", "langs": LANGS}


def client_ip() -> str:
    return (request.headers.get("X-Forwarded-For", request.remote_addr or "")
            .split(",")[0].strip())


@app.get("/")
def index():
    lang = pick_lang(request.args.get("lang"))
    session["csrf"] = secrets.token_urlsafe(24)
    return render_template("index.html", csrf=session["csrf"], error=None, email="", **ctx(lang))


@app.post("/enter")
def enter():
    lang = pick_lang(request.form.get("lang"))
    email = (request.form.get("email") or "").strip()[:254]
    t = TEXT[lang]

    def fail(msg):
        session["csrf"] = secrets.token_urlsafe(24)
        return render_template("index.html", csrf=session["csrf"], error=msg, email=email,
                               **ctx(lang)), 400

    if request.form.get("website"):            # honeypot ضد البوتات
        abort(400)
    token = session.get("csrf")
    if not token or not secrets.compare_digest(token, request.form.get("csrf", "")):
        return fail(t["bad_token"])
    if rate_limited(client_ip()):
        return fail(t["too_many"])
    if not EMAIL_RE.match(email):
        return fail(t["bad_email"])

    db.add(email, lang)
    notify_owner(email, lang, client_ip())     # يصلك الإيميل هنا
    session["entered"] = True
    session["email"] = email
    return redirect(url_for("news_page", lang=lang))


@app.get("/news")
def news_page():
    lang = pick_lang(request.args.get("lang"))
    if not session.get("entered"):
        return redirect(url_for("index", lang=lang))
    items, live = get_news(lang)
    return render_template("news.html", items=items, live=live, **ctx(lang))


@app.get("/robots.txt")
def robots():
    body = f"User-agent: *\nAllow: /\nDisallow: /news\nDisallow: /enter\n\nSitemap: {site_url()}/sitemap.xml\n"
    return Response(body, mimetype="text/plain")


@app.get("/sitemap.xml")
def sitemap():
    base = site_url()
    urls = [f"{base}/"] + [f"{base}/?lang={c}" for c in LANGS]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f"<url><loc>{u}</loc></url>" for u in urls]
    xml.append("</urlset>")
    return Response("\n".join(xml), mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", "5000")))
