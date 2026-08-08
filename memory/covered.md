# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-08
- Mesa 26.2 stable (05.08): открытый Linux-стек — NVK получил VK_EXT_mesh_shader и экспериментальный DLSS (VK_NVX_binary_import, NVK_EXPERIMENTAL=dlss, грузит CUDA-бинарники); KosmicKrisp Vulkan→Metal дорос до Vulkan 1.4; оптимизации Intel ANV/AMD RADV. Шаг к апскейл-паритету для SteamOS/Proton. [Phoronix](https://www.phoronix.com/news/Mesa-26.2-Released)
- По диагонали: Godot 4.8 dev 3 (07.08) — снапшот редактора: подчёркивание ошибок/предупреждений GDScript по месту, Ctrl+scroll зум панели файлов, glob-поиск файлов, буфер свойств из скриптов, visionOS→модуль (задел tvOS), RigidBody get_velocity_at_position. [Godot](https://godotengine.org/article/dev-snapshot-godot-4-8-dev-3/)
- По диагонали: Ричард Бартл (07.08) — соавтор MUD1 в интервью 80.lv: free-to-play/pay-to-win/Web3 разъедают договор игрока и разработчика; линза доверия в живых сервисах. [80.lv](https://80.lv/articles/virtual-worlds-were-supposed-to-let-players-be-themselves-but-monetization-forgets-that)
- По диагонали: BR1: INFINITE (07.08) — экстракшн-шутер Bravo Ready (Krafton/Solana Ventures): $1 за кил, ~$10/час, $1 за вход; экономика на Solana-стейблкоине, выведено >$100k. Play-to-earn с криптоворотами, много скепсиса. [Dexerto](https://www.dexerto.com/gaming/viral-extraction-shooter-says-it-will-pay-you-real-money-just-for-playing-3395532/)
- Из прошлого: Loki Software (США, 1998–2002) — первые серьёзные Linux-порты западных игр (Civ: Call to Power, HoMM III, Quake III), не выжила коммерчески, но оставила SDL.

## 2026-08-07
- Unity 6.7 alpha 4 (06.08): 6000.7.0a4 — CoreCLR-рантайм обновлён до нового сервисного билда .NET 10 (фиксы JIT/GC); DOTS настраиваемые бюджеты аллокаторов архетипов/запросов на платформу + расход в профайлере памяти, поиск сущностей по id, Frame Selected для entity; on-tile у deferred URP, stencil в Shader Graph, Variable Set-mode; ~661 фикс. [unityreleases](https://unityreleases.com/releases/6000.7.0a4)
- .NET Testing Platform reporting (06.08): .NET Blog (Amaury Levé) — MTP приземляет падения тестов в CI; --report-gh/--report-azdo аннотации на упавших строках; --report-azdo-flaky-history 14 делит «[flaky: 3/20 за 14д]» vs «[REGRESSION]»; TRX/HTML/JUnit/CTRF, --crashdump. Unity Test Runner на MTP не работает. [.NET Blog](https://devblogs.microsoft.com/dotnet/microsoft-testing-platform-reporting/)
- По диагонали: Esoterica (06.08) — Бобби Ангелов (Steam/Valve) + Кирилл Баженов, открытый C++ прототип-движок: bindless DX12, AAA-граф анимации, C++-рефлексия через libclang, hot-reload, Actor/ECS, редактор Dear ImGui; не продакшен-движок, конструктор/образец. [GameFromScratch](https://gamefromscratch.com/esoterica-game-engine/)
- По диагонали: Kidbash: Super Legend (06.08) — Unity-инди ретро-пайплайн: модели в Blender → спрайт-листы → Aseprite → Unity. [80.lv](https://80.lv/articles/interview-how-kidbash-super-legend-adapts-retro-style-graphics-with-a-modern-art-pipeline)
- По диагонали: Tenebris Somnia (06.08) — Андрес Борги, сурвайвл-хоррор: 2D-ретро + живые FMV-вставки; движок не назван. [80.lv](https://80.lv/articles/creating-a-survival-horror-game-that-blends-a-2d-retro-style-and-live-action-cutscenes)
- Из прошлого: Mono (де Иказа/Ximian, ~2001–2004, открытая .NET) — скриптовый рантайм Unity; из линии выросли IL2CPP и переезд на CoreCLR.

## 2026-08-06
- SEED (Klang, 05.08): симулятор общества без прописанных NPC — каждый житель игрок или автономный ИИ-«сидлинг»; модель на базе Google Gemma дообучена и крутится на своём железе, облачный Gemini 2.0 Flash для латентных ответов, у каждого свой Knowledge Graph (память/связи субъективны), «социальная батарейка»; EA стартовал 21.07, Steam осенью; рецензии бьют по диалогам. [80.lv](https://80.lv/articles/this-new-24-7-society-simulator-is-powered-by-thousands-of-ai-controlled-npcs)
- Unity 6000.5.7f1 (05.08): сервисный патч 6.5 LTS, 25 фиксов — очистка MostRecentFixedTime в Physics GraphicsIntegration (DOTS-сглаживание), сломанная серверная сборка macOS (libMonoPosixHelper.dylib), тени ShadowCaster по Renderer Shader User Value в рантайме, iOS-аудио при Пункте управления, D-Pad/Bluetooth Xbox-контроллера под Linux; 5 блокеров. [unityreleases](https://unityreleases.com/releases/6000.5.7f1)
- По диагонали: Gunstoppable (05.08) — Салаар Кохари, рогалик-шутер «скорость это урон» на UE 5.6; скорость как ресурс (копят/тратят на бой), почти вся механика самописная, инструменты бесплатные (UE/Blender/Audacity/DaVinci). [80.lv](https://80.lv/articles/gunstoppable-how-speed-is-damage-defined-a-roguelite-fps)
- По диагонали: Sculptools: Palette (05.08) — ProjectArgo, бесплатный аддон Blender: радиальное меню кистей в Sculpt Mode, до 8 палитр, слайдеры радиуса/силы, свои хоткеи, импорт/экспорт пресетов. [extensions.blender.org](https://extensions.blender.org/add-ons/sculptools-palette/)
- Из прошлого: Façade (2005, Матеас/Стерн) — интерактивная драма с вводом текста и парой Trip/Grace; понимание речи на рукописных шаблонах, провалы маскировали самопоглощёнными NPC; предок разговорных NPC, жалоба на диалог та же.

