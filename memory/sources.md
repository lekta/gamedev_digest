# Реестр источников

Пересобран 2026-11-16 по лайкам за 01.09–15.11 (606 новостей, отмечено 218). В скобках — доля отмеченных новостей со ссылкой на источник.
Правило: кандидаты минимум из 4 групп, хотя бы одна не Unity и не .NET; не больше 2 ссылок на домен в выпуске.

## Перекос, который чиним
За осень 114 ссылок ушло на github.com (25%) и 103 на discussions.unity.com (33%) — это треть всех ссылок при отдаче ниже средней (36%). Баги рантайма из трекеров и одиночные темы форума вытеснили студии, площадки и Россию, которые отмечаются в полтора-два раза чаще. Трекеры и форум — адресный источник под уже найденную тему, а не лента для обхода.

## Ежедневные точки входа
- **unity.com/blog, unity.com/releases, релиз-ноты редактора и Hub** (57%) — официальное Unity. Свежие сборки: Unity Releases API.
- **videogameschronicle.com** (64%), **verticalslice.news** (75%), **kotaku.com** (55%), **aftermath.site** (67%) — студии, сокращения, истории сообществ. Основной вход по индустрии.
- **gamesindustry.biz** (35%) — только через `https://r.jina.ai/<адрес>`: конкретный материал или `/feed/news`.
- **Steamworks: store.steampowered.com/news/group/4145017** (42%) — правила и витрина Steam. Тело постов Steam рисует скрипт: читать через `api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=<id>`.
- **Россия: app2top.ru** (80%), **cnews.ru** (78%), **3dnews.ru** (78%), **dtf.ru** (60%), **habr.com** (44%). vc.ru/games фетчеру не отдаётся.
- **dotnetnews.co**, **devblogs.microsoft.com/dotnet** (38%) — .NET одним заходом, без обхода трекеров.

## По понедельникам
- **«Недельный геймдев» Suvitruf** (habr.com/ru/users/Suvitruf/publications/articles/) — около 40 ссылок, берём как список кандидатов.
- **newsletter.gamediscover.co** (75%), **howtomarketagame.com** — Steam, вишлисты, видимость инди.

## Адресно, когда тема уже всплыла
- **discussions.unity.com** — анонсы и ответы сотрудников. JSON темы: `/t/<id>.json` с браузерным User-Agent; сотрудника отличать по `user_title: Staff` или `primary_group_name: unity_staff`. Лента багов: `latest.json?order=created`.
- **github.com**: dotnet/runtime, dotnet/roslyn, dotnet/csharplang, Unity-Technologies — через api.github.com. Лимит на баги — `config.md`, раздел 1.
- **blog.jetbrains.com/dotnet** — 403 напрямую, читать через `r.jina.ai`. Отдельные посты отмечаются редко (14%): брать релизы Rider и AI-фичи пачкой, не каждую заметку.
- **AI**: anthropic.com/news, openai.com/news, cursor.com/changelog, блоги Rider и VS.
- **dexerto.com** (43%), **dsogaming.com** (50%), **eurogamer.net** (40%, через `r.jina.ai/https://www.eurogamer.net/feed/news`), **pcgamer.com** (33%; тело закрыто, даты и заголовки — `pcgamer.com/rss/`), **gamedeveloper.com** (29%), **80.lv** (26%).
- **Bluesky разработчиков**: `https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor=<handle>&limit=30`.
- **Game File, massivelyop.com, speedrun.com** — под конкретный сюжет.

## Не обходим
- **phoronix.com** (0 из 7), **gamingonlinux.com** (29%) — драйверы и Linux-стек не заходят; SteamOS берём из ленты Steam.
- **pcgamesn.com** (1 из 10), **massivelyop.com** как лента (0 из 4).
- **reddit.com, steamdb.info, gamesradar.com** — закрыты от фетчера и напрямую, и через прокси. Онлайн смотреть на steamcharts.com.
- **gamespress.com** — отдаёт пустой шаблон. **gamedevdigest.com** — мёртв с мая 2026.
- X-аккаунты студий, финансовые PDF, GitHub-релизы списком.
