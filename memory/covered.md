# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

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

## 2026-08-02
- ИИ-агент тестов Microsoft (31.07): открытый плагин dotnet-test в репо dotnet/skills пишет юнит-тесты и сам проверяет мутационно; Copilot CLI/VS Code, .NET+десяток языков; 92,1% vs 78,9% Copilot, −67% провалов на туманных заданиях. [.NET Blog](https://devblogs.microsoft.com/dotnet/polyglot-unit-testing-agent)
- Honami Animation System (кон. июля): MIT-замена Animator'у Unity 6, свой PlayableGraph без аллокаций в кадре, нодовый граф+Timeline, процедурный риггинг, повесочные маски 0–1; бета, 243★, крутит анимацию в Steam-экшене Daisen. [GitHub](https://github.com/loyal-studio/Honami-Animation-System)
- По диагонали: Lazy3D Physical Fog (01.08) — аддон объёмного тумана для Blender, автодомены/пресеты/физрассеяние. [Superhive](https://superhivemarket.com/products/physical-fog-addon)
- По диагонали: Fab free asset round-up (28.07–11.08) — Epic раздаёт 3 UE + 1 кросс-платформенный ассет, окно открыто. [GameFromScratch](https://gamefromscratch.com/august-2026-free-gamedev-asset-round-up/)
- По диагонали: ретро-LCD про робота и опухоль (01.08, по фану) — эстетика карманных LCD, кивок на Сатоси Кона. [80.lv](https://80.lv/articles/this-retro-lcd-game-will-have-you-playing-as-a-robot-and-its-tumor)
- Из прошлого: Mecanim — технология монреальской компании, купленной Unity в 2011; дебют в Unity 4.0 (2012) как Animator Controller.

