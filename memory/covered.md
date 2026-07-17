# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-07-17
- Moss: The Forgotten Relic (16.07): Polyarc сняла VR-эксклюзив Moss (Unity) с VR на плоский экран — Switch/PS5/Xbox/Steam, «умная камера» держит четвёртую стену; OpenCritic 80, 94% рекомендуют. [Tech Times](https://www.techtimes.com/articles/320694/20260716/moss-forgotten-relic-launches-consoles-today-after-8-years-vr-smart-camera-makes-it-work.htm)
- По диагонали: ZeniMax Online (16.07) — 379 увольнений по Xbox-волне, вся верхушка студии ESO снесена (Берба/Кат/Диаз/Ламберт), QA -89 человек. [Game Developer](https://www.gamedeveloper.com/business/zenimax-online-studios-leadership-is-part-of-the-379-laid-off-workers)
- По диагонали: The Mermaid Mask (16.07) — детектив от SFB Games (Unity, авторы Tangle Tower), рецензий ещё нет. [Nintendo Life](https://www.nintendolife.com/games/nintendo-switch-2/mermaids-mask)
- По диагонали: Blender 5.2 LTS вышла (14.07) — XPBD-симуляция ткани/волос в Geometry Nodes, узел Mesh Bevel, аудио-реактивные узлы. [Blender.org](https://www.blender.org/press/blender-5-2-lts-release/)
- По диагонали: Unity Cloud Build — дедлайн 21.08 по устаревшим зависимостям CI (Xcode/Android SDK/старые LTS), V1 API отключат 21.12. [Unity Discussions](https://discussions.unity.com/t/unity-devops-build-automation-2026-dependency-deprecation-cycle/1724029)
- Проверено и отброшено как несвежее: обзоры Steam Machine (реально эмбарго конца июня к запуску 30.06, не эта неделя), Rostelecom Games (похоже на дубль новости 2025 года), Unity 6.3 LTS (дек 2025), дюп Dune: Awakening (июль 2025), Burst 1.8.25 «cross-CPU determinism» (нет такого; 1.8.25 — сен 2025).

## 2026-07-16
- Rider 2026.2 RC (15.07): agent skills открывают аналитику IDE (покрытие/профайлер/инспекции) внешним AI-агентам, нативный GitHub Copilot, ветки в Roslyn 2–3× быстрее, старт отладчика −2.8с, Natvis на Linux/macOS. GA скоро. [JetBrains](https://blog.jetbrains.com/dotnet/2026/07/15/rider-2026-2-release-candidate-is-out/)
- Fields of Mistria v0.16.2 (07.07): уход с GameMaker на внутренний движок Mistria SDK перед 1.0 (05.08); нативные Linux/SteamOS через steamrt4, интегрированная графика, два старых бага закрыты, старые моды отвалились. [Patch Notes](https://www.fieldsofmistria.com/post/new-engine-v0-16-2-patch-notes)
- По диагонали: ReSharper 2026.2 RC (15.07) — отладчик впервые в расширении для VS Code/Cursor (движок Rider) + первый шаг к ACP-агентам в VS (Junie превью). [JetBrains](https://blog.jetbrains.com/dotnet/2026/07/13/rs-vsc-debugging/)
- По диагонали: спор о маркировке AI на Steam разгорелся заново (кейс ARPG Bahast); AI-метка ≈ вдвое меньше отзывов, продажи −40–60%. Сигнал Unity-инди с Inference Engine/AI-ассетами. [GamesRadar](https://www.gamesradar.com/games/devs-dont-buy-steam-disclosure-claiming-gen-ai-was-a-necessity-im-literally-unemployed-and-i-still-make-all-of-my-assets-by-hand/)
- По диагонали: .NET июльское сервисное обновление (14.07) — заплатки безопасности для .NET 8/9/10, по фичам без нового. [.NET Blog](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-july-2026-servicing-updates/)
- По диагонали: Palworld вышла из EA (1.0, 10.07), 40+ млн игроков, 94% положительных; путь движка Unity → UE5 (пара к Mistria). [Steam](https://store.steampowered.com/app/1623730/Palworld/)

## 2026-07-15
- .NET 11 Preview 6 вышел официально (14.07): runtime-native async без флага EnablePreviewFeatures на net11.0, JIT-оптимизации (bounds-check elim, switch/SequenceEqual folding, Arm SVE2), C# 15 обкатывается; GA ноябрь. Линза Unity→CoreCLR. [.NET Blog](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-6/)
- По диагонали: Ubisoft Barcelona (AC Black Flag Resynced, движок Anvil) — забастовка 14–16.07 против 51 сокращения (~28% штата), паттерн «зашипили и режут». [VGC](https://www.videogameschronicle.com/news/assassins-creed-black-flag-resynced-studio-ubisoft-barcelona-strikes-to-protest-51-staff-being-laid-off/)
- По диагонали: Spin Master закрыла Originator через 2 дня после релиза мобильной F2P Paw Patrol: The Game (6→8.07), проекты в Sago Mini; тот же паттерн «зашипили и сократили». [Game Developer](https://www.gamedeveloper.com/mobile/spin-master-lays-off-paw-patrol-the-game-devs-two-days-after-launch)
- Из прошлого: Unity годами сидела на форке Mono (C# 4 / .NET 3.5), async/await и .NET 4.6 завезли только ~Unity 2017→дефолт 2018.1; CoreCLR — следующий шаг той же истории.
