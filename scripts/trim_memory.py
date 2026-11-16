#!/usr/bin/env python3
"""Держит файлы памяти в рамках, не полагаясь на аккуратность сборщика.

- memory/covered.md   — последние 3 дня (секции `## ГГГГ-ММ-ДД`);
- memory/buildlog.md  — последние 7 дней (такие же секции);
- memory/to_explore.md — строки `- **Тема** — … (ДД.ММ)`: старше 28 дней удаляются,
  строка режется до 400 знаков, остаётся не больше 40 самых свежих.

Запускается шагом workflow после сборки выпуска. Без аргументов, из корня репозитория.
"""
import datetime
import re

TODAY = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).date()
QUEUE_MAX_AGE = 28
QUEUE_MAX_ITEMS = 40
QUEUE_MAX_LEN = 400


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text.rstrip("\n") + "\n")


def trim_sections(path, days):
    """Оставляет шапку файла и секции `## ГГГГ-ММ-ДД` не старше days дней."""
    try:
        text = read(path)
    except FileNotFoundError:
        return
    parts = re.split(r"(?m)^(?=## \d{4}-\d{2}-\d{2})", text)
    head, sections = parts[0], parts[1:]
    kept = []
    for sec in sections:
        date = datetime.date.fromisoformat(sec[3:13])
        if (TODAY - date).days < days:
            kept.append(sec.rstrip("\n") + "\n\n")
    kept.sort(key=lambda s: s[3:13], reverse=True)
    write(path, head.rstrip("\n") + "\n\n" + "".join(kept))
    print(f"{path}: секций {len(sections)} -> {len(kept)}")


def entry_date(line):
    """Дата из хвоста строки `(ДД.ММ)`; год подбирается так, чтобы дата не была в будущем."""
    m = re.search(r"\((\d{2})\.(\d{2})[^()]*\)\s*$", line)
    if not m:
        return None
    day, month = int(m.group(1)), int(m.group(2))
    for year in (TODAY.year, TODAY.year - 1):
        try:
            date = datetime.date(year, month, day)
        except ValueError:
            return None
        if date <= TODAY + datetime.timedelta(days=1):
            return date
    return None


def trim_queue(path):
    try:
        lines = read(path).split("\n")
    except FileNotFoundError:
        return
    head = [l for l in lines if not l.startswith("- ")]
    while head and not head[-1].strip():
        head.pop()
    entries = []
    for line in lines:
        if not line.startswith("- "):
            continue
        date = entry_date(line) or TODAY  # без даты считаем свежей: дату допишет следующий прогон
        if (TODAY - date).days > QUEUE_MAX_AGE:
            continue
        if len(line) > QUEUE_MAX_LEN:
            tail = f" ({date:%d.%m})"
            line = line[: QUEUE_MAX_LEN - len(tail) - 1].rstrip(" ,;.") + "…" + tail
        elif entry_date(line) is None:
            line = line.rstrip() + f" ({date:%d.%m})"
        entries.append((date, line))
    total = len(entries)
    entries.sort(key=lambda e: e[0], reverse=True)
    entries = entries[:QUEUE_MAX_ITEMS]
    write(path, "\n".join(head + [""] + [e[1] for e in entries]))
    print(f"{path}: тем {total} -> {len(entries)}")


trim_sections("memory/covered.md", 3)
trim_sections("memory/buildlog.md", 7)
trim_queue("memory/to_explore.md")
