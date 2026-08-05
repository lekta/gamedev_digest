# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-05
- Unity 6.6 beta b6 (04.08): чистка API — Component/GameObject.rigidbody удалены, 50+ методов InstanceID→EntityId устарели, Dynamic Batching выпилен; 2D-физика получила плавучесть/ветер (PhysicsBody/PhysicsWorld) + PhysicsSpace для своих broad/narrowphase; DOTS: managed-компоненты под удаление, EntityCommandBuffer только single-playback. [unityreleases](https://unityreleases.com/releases/6000.6.0b6)
- Локальная речь-в-текст на C# (04.08): .NET Blog (Bruno Capuano) — консольное .NET 10 приложение, потоковый ASR без облака; модель NVIDIA Nemotron 0.6B (англ.), Microsoft.AI.Foundry.Local.WinML + NAudio (16кГц/16бит/моно), API совместим с OpenAI Realtime, только Windows (WinML). [.NET Blog](https://devblogs.microsoft.com/dotnet/foundry-local-live-speech-to-text-csharp/)
- По диагонали: CNA (04.08) — реализация XNA 4.0 на C++23 поверх SDL3, Ms-PL; 92,7% типов XNA (227/245), 8 графбэкендов, ENet-сеть; C++-двойник линии MonoGame/FNA. 55★. [GameFromScratch](https://gamefromscratch.com/cna-its-c-xna/)
- По диагонали: NuGet (03.08) — срок жизни API-ключей режут 365→30 дней (новые с 17.08, старые off 01.11); рекомендуют Trusted Publishing (OIDC); повод — атака на NX Console. [.NET Blog](https://devblogs.microsoft.com/dotnet/strengthening-nuget-supply-chain-security-reducing-api-key-lifetime/)
- По диагонали: 80.lv (04.08) — Дмитрий Безродний, персонаж Ариадны (крито-микенский стиль): MetaHuman для пропорций, одетый 3D-скан, AI-вывод → кисти ZBrush. [80.lv](https://80.lv/articles/creating-a-detailed-and-expressive-character-inspired-by-cretan-mycenaean-culture)
- Из прошлого: XNA (Microsoft 2006–2013, C#, Xbox 360/Zune; Bastion/Terraria/Stardew) свёрнут в 2013 → MonoGame/FNA продлили API, теперь и C++-порт CNA.

## 2026-08-04
- Grabbit 2 (03.08): редакторный плагин Unity — физика Unity прямо в сцене без запуска игры, коллайдеры выпуклой декомпозицией (воксель/точность/скорость), 5 режимов, bake в рантайм, обход «только выпуклое» PhysX; Уильям Беснар/Jungle, Unity 6, Built-in/URP/HDRP, $40. [80.lv](https://80.lv/articles/how-grabbit-2-simulates-physics-inside-the-unity-editor)
- Sedulous Engine (03.08): открытый 3D-движок с редактором на языке Beef (гибрид C#/C++), MIT; Jolt-физика, Vulkan 1.3/DX12, Forward PBR, ECS-сцена, Recast/Detour, SDL3, UI на XML+CSS; 74★, в активной разработке. [GitHub](https://github.com/SedulousWorks/SedulousEngine)
- По диагонали: Refactor Games / Delphi Interactive (03.08) — студия FIFA World Cup: Launch Edition для Netflix закрыта через 8 недель после релиза; финансирование свёрнуто, Netflix называл «успехом». [Game Developer](https://www.gamedeveloper.com/production/report-refactor-games-shuttered-by-delphi-interactive)
- По диагонали: Big Walk (04.08) — House House (Untitled Goose Game на Unity), кооп-«гулялка» с proximity voice chat (затухание/эхо/стены/рации); PS5/Switch 2/PC, изд. Panic, день 1 в PS Plus Essential. [Big Walk](https://bigwalk.game/)
- По диагонали: Houdini (03.08) — симуляция лесного ручья на GPU-солвере Paradigm, разбор пайплайна жидкости (Энрике Де ла Гарса). [80.lv](https://80.lv/articles/stunning-forest-stream-simulation-made-with-houdini)
- Из прошлого: PhysX (Ageia, плата-ускоритель сер.2000-х → NVIDIA 2008) — штатный 3D-физдвижок Unity, отсюда «только выпуклые коллайдеры» для динамики.

## 2026-08-03
- Vulkan 1.4.358 (31.07): расширение VK_EXT_image_tiling_control — попиксельный выбор раскладки текстуры в памяти (память vs скорость доступа GPU); делали AMD/Valve/Samsung/NVIDIA/Intel/Nintendo; уровень API/драйвера. [Phoronix](https://www.phoronix.com/news/Vulkan-1.4.358)
- Steam на Linux (июль): доля игроков 4,01% (+0,32 к июню 3,69%), ~22% систем — SteamOS Holo; рекорд был март 5,33%. [GamingOnLinux](https://www.gamingonlinux.com/2026/08/linux-back-over-4-percent-in-the-july-2026-steam-survey/)
- По диагонали: Nouveau/NVK (31.07) — патч включает Vulkan Video поверх аппаратного NVDEC в открытом драйвере NVIDIA; путь к аппаратному декоду FMV под Linux. [Phoronix](https://www.phoronix.com/news/NVK-NVDEC-Vulkan-Video)
- Из прошлого: Vulkan вырос из Mantle (AMD+DICE, 2013), переданного Khronos в 2015; Vulkan 1.0 — февраль 2016.

