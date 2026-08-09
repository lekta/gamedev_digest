# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-09
- Triton (07-08.08): открытый драйвер DirectX 11 для гостевых Windows в QEMU (osy/UTM), реализует DDI ниже уровня API (в отличие от Neptune на DXVK/Vulkan); команды → VirtIO → QEMU → virglrenderer → Mesa; собран с помощью Claude Opus 5/Fable 5. [UTM](https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/)
- Wine 11.15 (08.08): 41 фикс, база Proton; два Wayland-фикса (двойная sRGB «вымывала» цвета, смещение 4:3 fullscreen), баг 4811 XMLDOMDocument 2006 закрыт, ARM64EC MinGW, локальная NTLM, KDF в BCrypt, конверсии WindowsCodecs. [GamingOnLinux](https://www.gamingonlinux.com/2026/08/wine-11-15-brings-improvements-for-wayland-more-format-conversions-in-windowscodecs/)
- По диагонали: BlendKit (04.08) — 67k бесплатных CC0/RF-ассетов (22k моделей, 36k материалов, 4k HDRI, 1k кистей), экспансия на Maya/Rhino 8+/Godot 4.0+ (Godot standalone, Maya/Rhino требуют Blender); Unity-плагина нет. [CG Channel](https://www.cgchannel.com/2026/08/get-60000-free-3d-assets-for-maya-godot-and-rhino-from-blendkit/)
- По диагонали: The Void (06.08) — соло-хоррор-FPS Джеффи Захарии (Керала) по мотивам «Мглы»; волновой сурвайвл, одно оружие, уклонение; движок не назван; релиз Q4 2026. [80.lv](https://80.lv/articles/the-void-how-to-create-a-survival-horror-fps-inspired-by-the-mist-movie)
- По диагонали: .NET 11 «Performance Edition» (01.08, Стивен Гизель) — сводка перф-правок: рантайм-нативный async, Zstandard, JIT, поднятые мин. требования x86/Arm64. [steven-giesel.com](https://steven-giesel.com/blogPost/86620358-bb91-4295-84fc-a1329b2567ae/net-11-performance-edition)
- Из прошлого: DXVK (Филип Ребохле, 2018) — Direct3D 9/10/11 → Vulkan; вытащила Proton в «работает почти всё», опора Steam Deck.

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

