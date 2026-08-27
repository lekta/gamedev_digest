# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-27
- W4 Games (gamedeveloper 25.08): Series B $18 млн во главе с Tencent в коммерческую руку Godot; всего $33 млн (OSS Capital/LUX/Наваль Равикант/офис Лютке); партнёрство по Азии; +50% команды; enterprise-плечо против Unity/Unreal. [Game Developer](https://www.gamedeveloper.com/business/w4-games-raises-18m-to-expand-its-international-team)
- Отладчик-агент Visual Studio (devblogs 26.08): режим «расследования через тесты» — агент создаёт сфокусированный тест на баг, чинит под отладчиком, перепрогоняет + проверяет регресс; нужна существующая тест-обвязка, цифр нет. [.NET Blog](https://devblogs.microsoft.com/visualstudio/the-visual-studio-debugger-agentic-workflow-gets-a-test-driven-upgrade/)
- Environment.ProcessorCount (Andrew Lock 25.08): с .NET Core 6+ отдаёт ядра процесса, а не хоста — врёт в контейнерах/cgroups/affinity; хост берут через GetActiveProcessorCount/sysctlbyname/sys...cpu/online. [andrewlock.net](https://andrewlock.net/finding-the-total-number-of-processors-on-a-machine-with-dotnet/)
- По диагонали: Unity 6.3 LTS 6000.3.23f1 (26.08) — 42 фикса; утечка VRAM мелких текстур D3D12, артефакты dynamic res HDRP D3D12, флаг пропуска VC++2010, фикс ручной активации лицензии. [Unity Releases](https://unityreleases.com/releases/6000.3.23f1)
- По диагонали: Farm & Feast (dummy dino, Unity, 27.08) — поливочный шланг как particle rope (distance constraints), меш по кривой; струя — сплайновая дуга, не симуляция; плейтест. [80.lv](https://80.lv/articles/farming-game-with-seriously-interactive-physics-based-water-hose)
- По диагонали: Godot 4.8 dev 4 (26.08) — Trail3D, VisualShader Node Groups, multi-bounce AO, directional lightmap specular; 86 контриб/224 правки. [Godot](https://godotengine.org/article/dev-snapshot-godot-4-8-dev-4/)
- По диагонали: Aliens: Fireteam Elite 2 (Cold Iron/Daybreak, 25.08) — провальный старт $50 без маркетинга/пре-ордеров/обзоров, резко отрицательные, ~2–5k CCU; плохая оптимизация даже на мощных ПК. [Massively OP](https://massivelyop.com/2026/08/25/aliens-fireteam-elite-2-has-officially-launched-under-the-daybreak-banner/)
- По диагонали: .NET Conf 2026 (25.08) — 10–12 ноября, .NET 11 GA 10.11 с C# 15/union-типами; MAUI→CoreCLR; MCP C# SDK v2.0. [.NET Blog](https://devblogs.microsoft.com/dotnet/dotnet-conf-2026/)

## 2026-08-26
- C# 15 (Microsoft, devblog 24.08): официальный разбор перед релизом с .NET 11 — union-типы, closed-иерархии, новая модель unsafe (указатели/&/sizeof без unsafe, разыменование в unsafe), with(...) в коллекц. выражениях, расширяющие индексаторы, labeled break/continue; GA 10.11. [.NET Blog](https://devblogs.microsoft.com/dotnet/explore-csharp-15/)
- Ichor Online (инди FR3NKD+LeoDev, 80.lv 24.08): экшн-MMO в духе WoW/RuneScape на открытом стеке Godot + SpacetimeDB + Blender; без квест-маркеров/pay-to-win/подписки; неткод не раскрыт. [80.lv](https://80.lv/articles/indie-devs-show-action-mmorpg-built-with-open-source-software)
- Combos (Converge.AI, Gamescom 25.08): браузерные игры генерит ИИ-агент Boo по тексту (дизайн/ассеты/звук/публикация); 300k+ создателей, 110+ стран, 10k+ игр; стенд 26–30.08; один тайтл собран через GB Studio на Game Boy. [PR Newswire](https://www.prnewswire.com/news-releases/combos-makes-its-global-debut-at-gamescom-bringing-ai-created-games-by-everyday-creators-302859934.html)
- По диагонали: How to Fish (Dazed Games/изд. Landfall, 25.08) — физ ко-оп рыбалка дуэта, пик 356 099 CCU, ~1M продаж за 48ч, 94% (18 088/19 151); патчи лобби 4→8, приватные лобби, закрыт грифинг; движок не назван. [activeplayer](https://activeplayer.io/how-to-fish-player-count-hits-356k/)
- По диагонали: DXVK-Sarek 1.13.0 «Pacemaker» (24.08) — форк DXVK для старых GPU; DXVK_FRAME_PACE, дефолт dyasync-шейдеры против статтеров, динамич. аллокатор против OOM на iGPU; сверка для Unity DirectX под Proton. [GamingOnLinux](https://www.gamingonlinux.com/2026/08/dxvk-sarek-1-13-0-is-a-big-release-for-older-gpus-to-play-modern-games-on-linux/)
- По диагонали: LLVM/Clang 23.1 (25.08) — Zen 6 + AVX-512 BMM, частичный C++26, AMDGPU/RISC-V; косвенно Burst(LLVM)/IL2CPP. [Phoronix](https://www.phoronix.com/news/LLVM-23.1-Released)
- По диагонали: Marathon (Bungie, 24.08) — онлайн впервые <1000 (мин 987 CCU, ~1015 час. среднее); ретеншен-дно без разбора причин студией. [OpenCritic](https://opencritic.com/news/35695/concern-for-marathon-grows-as-pc-player-count-drops-to-triple-digits)

## 2026-08-25
- DLSS 4.5 Ray Reconstruction (NVIDIA, Gamescom 25.08): трансформер 2-го поколения слил денойз трассировки и апскейл в одну модель; +35% вычислений/+20% параметров при той же скорости; все RTX 20–50, 27 игр, раздача через приложение NVIDIA, денойз в Blender 5.3 осенью. [NVIDIA](https://www.nvidia.com/en-us/geforce/news/dlss-4-5-ray-reconstruction-1000-rtx-games-apps-out-now/)
- Roblox open-source модерация (ROOST, 19.08): три модели — PII Classifier v2.0 (189 языков, F1 63,41→90,52), Sentinel v2 (~70% ранних детектов, ROC-AUC 0,996), голосовой v3 (30 языков, 8 категорий, 61% полноты при 1% FP); Hugging Face/GitHub. [Roblox](https://about.roblox.com/newsroom/2026/08/roblox-open-source-safety-models-roost)
- Свиток Тайу (ConchShip, интервью 80.lv 24.08): уся-песочница на Unity держит 5000–10000 процедурных NPC с целями/связями/биографией, эмерджентная драма; 16 регионов, ~4,5 млн иероглифов, 8 лет; рантайм не раскрыт. [80.lv](https://80.lv/articles/interview-building-a-wuxia-sandbox-rpg-with-up-to-10-000-dynamic-npcs)
- По диагонали: Infinity Code Online Maps v5 (24.08) — карты 2D/3D в Unity, маршруты/геокодинг/GPS/высоты, C# без зависимостей, 16+ провайдеров, mobile/desktop/WebGL/AR-VR. [80.lv](https://80.lv/articles/this-unity-asset-pack-allows-you-to-add-interactive-2d-and-3d-maps-to-your-games)
- По диагонали: AMD attention-based indirect illumination (SIGGRAPH 2026, 20.08) — нейро-GI diffuse+specular по буферам камеры и RSM, 2,19M параметров, ~45мс 512×512 на MI250; до реалтайма далеко. [GPUOpen](https://gpuopen.com/learn/lightweight-attention-based-indirect-illumination/)
- По диагонали: VKD3D 2.1 (24.08) — D3D12 поверх Vulkan (Wine/Proton), улучшен HLSL-компилятор (dead store elim), FP-конверсии DXIL, совместимость GLSL; сверка для DirectX-сборок под SteamOS. [Phoronix](https://www.phoronix.com/news/VKD3D-2.1-Released)
- По диагонали: Defold 1.13.1 (17.08) — свет для 2D/3D (4 типа через LightBuffer), база геймпадов SDL, тёплые сборки до -19%, экспериментальный Metal; Lua-движок. [Defold](https://defold.com/2026/08/17/Defold-1-13-1/)
- По диагонали: Neotolis Engine (19.08) — свой движок на C17 за 5 мес (WASM+WebGL2/OpenGL3.3, code-first), игра за месяц, код через Claude; показан на Comic Con Tashkent. [Habr](https://habr.com/ru/articles/1072162/)
