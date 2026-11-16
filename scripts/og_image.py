#!/usr/bin/env python3
"""Достаёт адрес картинки для новости и проверяет, что он открывается.

    python3 scripts/og_image.py <адрес страницы>      — og:image / twitter:image страницы
    python3 scripts/og_image.py --steam <название>    — шапка игры из магазина Steam
    python3 scripts/og_image.py --steam <appid>

Печатает ровно одну строку: адрес картинки либо `NONE: причина`.
WebFetch метатеги не отдаёт, поэтому картинки из выпусков пропали — скрипт закрывает эту дыру.
"""
import html
import json
import re
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
# Генерируемые карточки и логотипы — не картинка к новости
BAD = re.compile(
    r"opengraph\.githubassets\.com|/logo|logo\.|favicon|default[-_]?(og|share|social)|placeholder|"
    r"site[-_]?(image|logo)|avatar|sprite|/icons?/|\.svg(\?|$)",
    re.I,
)


def get(url, limit=400_000):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en,ru;q=0.8"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read(limit), r.headers.get("Content-Type", ""), r.geturl()


def check(img):
    """Картинка должна реально отдаваться и быть картинкой."""
    if not re.match(r"https://[^\s\"'<>()]+$", img):
        return "адрес не https или с мусором"
    if BAD.search(img):
        return "похоже на логотип или заглушку"
    try:
        _, ctype, _ = get(img, limit=2048)
    except Exception as e:  # noqa: BLE001
        return f"не открывается ({e})"
    if not ctype.startswith("image/") or "svg" in ctype:
        return f"не картинка ({ctype})"
    return None


def from_page(url):
    try:
        body, _, final = get(url)
    except Exception as e:  # noqa: BLE001
        return None, f"страница не открылась ({e})"
    text = body.decode("utf-8", "replace")
    for prop in ("og:image:secure_url", "og:image", "twitter:image", "twitter:image:src"):
        for tag in re.findall(r"<meta\b[^>]*>", text, re.I):
            if re.search(r"(property|name)\s*=\s*[\"']%s[\"']" % re.escape(prop), tag, re.I):
                m = re.search(r"content\s*=\s*[\"']([^\"']+)[\"']", tag, re.I)
                if m:
                    return urllib.parse.urljoin(final, html.unescape(m.group(1).strip())), None
    return None, "на странице нет og:image"


def from_steam(query):
    try:
        if not query.isdigit():
            url = "https://store.steampowered.com/api/storesearch/?cc=us&l=en&term=" + urllib.parse.quote(query)
            items = json.loads(get(url)[0]).get("items") or []
            if not items:
                return None, "игра в Steam не нашлась"
            query = str(items[0]["id"])
        url = "https://store.steampowered.com/api/appdetails?filters=basic&appids=" + query
        data = json.loads(get(url)[0]).get(query, {})
        img = (data.get("data") or {}).get("header_image")
        return (img.split("?")[0], None) if img else (None, "у приложения нет шапки")
    except Exception as e:  # noqa: BLE001
        return None, f"Steam не ответил ({e})"


def main():
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == "--steam":
        img, err = from_steam(" ".join(args[1:]).strip())
    elif len(args) == 1 and re.match(r"https?://", args[0]):
        img, err = from_page(args[0])
    else:
        print("NONE: нужен адрес страницы или --steam <название|appid>")
        return
    if img and not err:
        err = check(img)
    print(img if img and not err else f"NONE: {err}")


if __name__ == "__main__":
    main()
