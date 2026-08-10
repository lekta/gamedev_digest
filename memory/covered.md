# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-10
- Unity → Supersonic → Tripledot ($40M, 06.08): Unity продала моб. издательский бизнес Supersonic, разворот к движку + рекламной платформе Vector; выход из наследия ironSource ($4,4 млрд, 2022). [Game Developer](https://www.gamedeveloper.com/business/unity-sells-supersonic-publishing-biz-to-tripledot-for-40m)
- Marvel Tokon: Fighting Souls (06.08): разбитый PC-порт (стуттеры, GPU, анти-чит, обяз. вход PSN) обвалил онлайн в Steam с ~24,4k до ~7k; статус «в основном отрицательные», консоль принята тепло. [The Gamer](https://www.thegamer.com/marvel-tokon-fighting-souls-pc-version-playercount-nearly-halved/)
- По диагонали: The Sinking City 2 (Frogwares, 07.08) — ушёл на золото, релиз 18.08 (PS5/Xbox/PC), в конце разработки переезд на Unreal Engine 5.8; студия из Украины, сдвиги из-за войны. [VGTimes](https://vgtimes.com/gaming-news/163461-the-sinking-city-2-goes-gold-ahead-of-its-august-18-release.html)
- По диагонали (по фану): 80.lv (08.08) — оддболл-инди недели: людоед-многоножка и дед с тростью в метроидвании «между Cuphead и Hollow Knight»; движки не названы. [80.lv](https://80.lv/articles/this-metroidvania-will-have-you-playing-as-a-grandpa-fighting-with-his-cane)
- Из прошлого: линия скупки Unity — Weta Digital tools (2021, ~$1,6 млрд) + ironSource (2022, ~$4,4 млрд) → откат к ядру в 2023–2026.

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

