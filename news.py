"""جلب أخبار الطاقات المتجددة في الجزائر من Google News RSS مع تخزين مؤقت."""
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

from i18n import FALLBACK_NEWS, NEWS_QUERY

CACHE_SECONDS = 30 * 60
_cache: dict[str, tuple[float, list]] = {}


def _fetch(lang: str, limit: int = 12) -> list[dict]:
    q, hl, gl, ceid = NEWS_QUERY[lang]
    url = ("https://news.google.com/rss/search?" +
           urllib.parse.urlencode({"q": q, "hl": hl, "gl": gl, "ceid": ceid}))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=8) as r:
        root = ET.fromstring(r.read())
    items = []
    for it in root.iter("item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        src_el = it.find("source")
        source = (src_el.text or "").strip() if src_el is not None else ""
        # العنوان في Google News ينتهي عادة بـ " - اسم المصدر"
        if source and title.endswith(" - " + source):
            title = title[: -len(source) - 3]
        date = ""
        try:
            date = parsedate_to_datetime(it.findtext("pubDate")).strftime("%Y-%m-%d")
        except Exception:
            pass
        if title and link.startswith("http"):
            items.append({"title": title, "link": link, "source": source, "date": date})
        if len(items) >= limit:
            break
    return items


def get_news(lang: str) -> tuple[list[dict], bool]:
    """يعيد (القائمة، هل هي أخبار حية؟)."""
    now = time.time()
    hit = _cache.get(lang)
    if hit and now - hit[0] < CACHE_SECONDS:
        return hit[1], True
    try:
        items = _fetch(lang)
        if items:
            _cache[lang] = (now, items)
            return items, True
    except Exception:
        if hit:  # استخدم آخر نسخة ناجحة
            return hit[1], True
    fb = [{"title": t, "link": u, "source": s, "date": ""} for t, u, s in FALLBACK_NEWS[lang]]
    return fb, False
