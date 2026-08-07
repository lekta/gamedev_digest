# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

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

## 2026-08-05
- Unity 6.6 beta b6 (04.08): чистка API — Component/GameObject.rigidbody удалены, 50+ методов InstanceID→EntityId устарели, Dynamic Batching выпилен; 2D-физика получила плавучесть/ветер (PhysicsBody/PhysicsWorld) + PhysicsSpace для своих broad/narrowphase; DOTS: managed-компоненты под удаление, EntityCommandBuffer только single-playback. [unityreleases](https://unityreleases.com/releases/6000.6.0b6)
- Локальная речь-в-текст на C# (04.08): .NET Blog (Bruno Capuano) — консольное .NET 10 приложение, потоковый ASR без облака; модель NVIDIA Nemotron 0.6B (англ.), Microsoft.AI.Foundry.Local.WinML + NAudio (16кГц/16бит/моно), API совместим с OpenAI Realtime, только Windows (WinML). [.NET Blog](https://devblogs.microsoft.com/dotnet/foundry-local-live-speech-to-text-csharp/)
- По диагонали: CNA (04.08) — реализация XNA 4.0 на C++23 поверх SDL3, Ms-PL; 92,7% типов XNA (227/245), 8 графбэкендов, ENet-сеть; C++-двойник линии MonoGame/FNA. 55★. [GameFromScratch](https://gamefromscratch.com/cna-its-c-xna/)
- По диагонали: NuGet (03.08) — срок жизни API-ключей режут 365→30 дней (новые с 17.08, старые off 01.11); рекомендуют Trusted Publishing (OIDC); повод — атака на NX Console. [.NET Blog](https://devblogs.microsoft.com/dotnet/strengthening-nuget-supply-chain-security-reducing-api-key-lifetime/)
- По диагонали: 80.lv (04.08) — Дмитрий Безродний, персонаж Ариадны (крито-микенский стиль): MetaHuman для пропорций, одетый 3D-скан, AI-вывод → кисти ZBrush. [80.lv](https://80.lv/articles/creating-a-detailed-and-expressive-character-inspired-by-cretan-mycenaean-culture)
- Из прошлого: XNA (Microsoft 2006–2013, C#, Xbox 360/Zune; Bastion/Terraria/Stardew) свёрнут в 2013 → MonoGame/FNA продлили API, теперь и C++-порт CNA.

