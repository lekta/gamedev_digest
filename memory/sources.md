# Реестр источников

Создан 2026-06-29 по запросу «расширить пул, источники узкие».

## Проблема, которую чиним
За 2 недели из ~90 ссылок **23 — gamedeveloper.com** (в основном колонка Patch Notes). Это перекос: один источник задаёт повестку и тащит инерционные сюжеты. Цель — раскидать нагрузку.

**Правило ротации:** при сборке тянуть кандидатов минимум из 3-4 разных групп ниже. Game Developer — ок как один из, но не основа выпуска. Если за выпуск >2 ссылок ведут на один домен — искать альтернативу.

🟢 = уникальный/нишевый источник, который раньше не использовали или использовали мало. Проверять в первую очередь — там то, чего нет у всех.

---

## Unity (движок, технологии)
- **unity.com/blog**, **unity.com/news** — официальные анонсы, релизы.
- **discussions.unity.com** — форум: релиз-ноты, deprecations, бета-ветки. 🟢 ранние сигналы по версиям/таргетам (Intel Mac deprecation, CoreCLR migration брались отсюда).
- Unity roadmap (unity.com/roadmap), GitHub-релизы.
- **r/Unity3D** 🟢 — инди-практика, реальные баги, что ломается на проде.

## C# / .NET
- **devblogs.microsoft.com/dotnet** — официальный блок (язык, перформанс, Roslyn).
- **dotnetnews.co** 🟢 — агрегатор 140+ .NET-источников, ручной отбор. Одно место — широкий охват.
- **GitHub: dotnet/runtime, dotnet/csharplang (discussions), dotnet/announcements** 🟢 — первоисточник решений по языку до того, как про них напишут.
- **Morning Dew (Alvin Ashcraft)**, **The Morning Brew (Chris Alcock)** 🟢 — ежедневные дайджесты ссылок.
- **Milan Jovanović — .NET Weekly**, **Andrew Lock (andrewlock.net)**, **Konrad Kokosa** 🟢 (перформанс/GC), Nick Chapsas (YouTube), Stephen Toub / David Fowler (посты).
- JetBrains .NET blog + **.NET Annotated** (рассылка).
- r/dotnet, r/csharp.

## Индустрия / инди-кейсы / постмортемы
- **gamedeveloper.com** — основной, НЕ злоупотреблять (см. перекос выше).
- **GameDiscoverCo / newsletter.gamediscover.co (Simon Carless)** 🟢 — Steam-алгоритм, разборы Next Fest, видимость инди. Уже зашло.
- **How To Market A Game (Chris Zukowski)** 🟢 — инди-маркетинг и продажи, прикладные разборы.
- **Aftermath (aftermath.site)** 🟢 — независимое (экс-Kotaku): труд, эмерджентные истории, разборы. Уже зашло (Meccha Chameleon).
- **Game File (Стивен Тотило)** 🟢 — сольные расследования по индустрии.
- **Remap Radio**, **Second Wind** 🟢 — независимые команды (экс-Waypoint / экс-Escapist).
- **80.lv** 🟢 — арт/тех-пайплайны, интервью разработчиков.
- r/gamedev.

## Данные о продажах и онлайне (для «план vs реальность» и оттоков)
- **SteamDB (steamdb.info)** 🟢 — CCU, чарты, история цен/игроков. Проактивный трекер, а не ожидание статьи.
- **VG Insights / Video Game Insights** 🟢 — оценки продаж (консервативны, занижают).
- **Gamalytic, Game Oracle, Steam Spy** — перекрёстная проверка оценок.
- Steam review trend — смена статуса («Very Positive → Mixed») как сигнал UX-провала.

## Внутриигровые события / сообщества
- **SteamDB — крупнейшие падения онлайна за неделю** 🟢 — детектим оттоки сами.
- **Massively Overpowered (massivelyop.com)** 🟢 — MMO-драма, оттоки, конфликты комьюнити.
- r/Games, r/MMORPG, r/EVE, профильные сабреддиты конкретных игр.
- speedrun.com, PacePals (pacepals.gg), GDQ/ESA — спидран фоном.
- PCGamer / GamesRadar теги «weird», Aftermath — эмерджентные истории.

## AI (модели и интеграции)
- anthropic.com/news, openai.com/news, blog.google, deepmind.google.
- IDE-агенты: cursor.com, Rider/VS devblogs, Claude Code, JetBrains AI.

## РФ (обязательный пункт)
- **dtf.ru**, **app2top.ru**, **vc.ru/games** — рынок, студии, релокация.
- **Habr — «Недельный геймдев»** 🟢 — еженедельный RU-агрегатор геймдев-новостей.
- IT-World, Рамблер/игры — рынок труда, отъезд специалистов, обходы санкций.

---
Связь: `config.md` (секции «Тематика», «Поисковая дисциплина»).
