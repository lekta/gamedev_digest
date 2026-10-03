#!/usr/bin/env python3
"""Собирает feed.xml (RSS 2.0) из последних выпусков в digests/
и digests/index.json — список всех выпусков для сайта (без GitHub API)."""
import datetime
import email.utils
import glob
import json
import os

import markdown

SITE = "https://lekta.github.io/gamedev_digest/"
LIMIT = 14

items = []
for path in sorted(glob.glob("digests/[0-9]*.md"), reverse=True)[:LIMIT]:
    date = os.path.basename(path)[:-3]
    with open(path, encoding="utf-8") as fh:
        body = markdown.markdown(fh.read()).replace("]]>", "]]&gt;")
    dt = datetime.datetime.strptime(date, "%Y-%m-%d").replace(
        hour=7, tzinfo=datetime.timezone.utc
    )
    items.append(
        "<item>"
        f"<title>Выпуск {date}</title>"
        f"<link>{SITE}</link>"
        f'<guid isPermaLink="false">gamedev-digest-{date}</guid>'
        f"<pubDate>{email.utils.format_datetime(dt)}</pubDate>"
        f"<description><![CDATA[{body}]]></description>"
        "</item>"
    )

feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0"><channel>'
    "<title>GameDev Digest</title>"
    f"<link>{SITE}</link>"
    "<description>Ежедневная сводка новостей геймдева для Unity/C#-разработчика</description>"
    "<language>ru</language>"
    + "".join(items)
    + "</channel></rss>\n"
)

with open("feed.xml", "w", encoding="utf-8") as fh:
    fh.write(feed)
print(f"feed.xml: {len(items)} выпусков")

# Список выпусков для index.html: сайт читает его со своего же домена,
# не завися от api.github.com (лимит 60 запросов/час на IP, у мобильных операторов общий).
dates = sorted(
    (os.path.basename(p)[:-3] for p in glob.glob("digests/[0-9]*.md")), reverse=True
)
with open("digests/index.json", "w", encoding="utf-8") as fh:
    json.dump(dates, fh)
    fh.write("\n")
print(f"digests/index.json: {len(dates)} выпусков")
