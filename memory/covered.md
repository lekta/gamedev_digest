# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-02
- ИИ-агент тестов Microsoft (31.07): открытый плагин dotnet-test в репо dotnet/skills пишет юнит-тесты и сам проверяет мутационно; Copilot CLI/VS Code, .NET+десяток языков; 92,1% vs 78,9% Copilot, −67% провалов на туманных заданиях. [.NET Blog](https://devblogs.microsoft.com/dotnet/polyglot-unit-testing-agent)
- Honami Animation System (кон. июля): MIT-замена Animator'у Unity 6, свой PlayableGraph без аллокаций в кадре, нодовый граф+Timeline, процедурный риггинг, повесочные маски 0–1; бета, 243★, крутит анимацию в Steam-экшене Daisen. [GitHub](https://github.com/loyal-studio/Honami-Animation-System)
- По диагонали: Lazy3D Physical Fog (01.08) — аддон объёмного тумана для Blender, автодомены/пресеты/физрассеяние. [Superhive](https://superhivemarket.com/products/physical-fog-addon)
- По диагонали: Fab free asset round-up (28.07–11.08) — Epic раздаёт 3 UE + 1 кросс-платформенный ассет, окно открыто. [GameFromScratch](https://gamefromscratch.com/august-2026-free-gamedev-asset-round-up/)
- По диагонали: ретро-LCD про робота и опухоль (01.08, по фану) — эстетика карманных LCD, кивок на Сатоси Кона. [80.lv](https://80.lv/articles/this-retro-lcd-game-will-have-you-playing-as-a-robot-and-its-tumor)
- Из прошлого: Mecanim — технология монреальской компании, купленной Unity в 2011; дебют в Unity 4.0 (2012) как Animator Controller.

## 2026-08-01
- Unity внутри Unreal / PolySpatial (21.07, догоняющая): Fantasy Kingdom считается в Unity, рисуется в Unreal; безголовый Unity-сервер, только URP+Shader Graph, цель — Fortnite как целевая платформа, ранний доступ не раньше 2027. [Unity Discussions](https://discussions.unity.com/t/unity-x-fortnite-how-unity-runs-inside-unreal-engine/1731630)
- Веб-платформа Unity (28.07): WebAssembly64 в бете 6.6 снимает потолок памяти 2–4 ГБ (указатели 4→8 байт, Safari не поддерживает), прогрессивная загрузка по сценам; в 6.5 — Wasm2023 по умолчанию, стили UI Toolkit в неуправляемой памяти. [Unity Discussions](https://discussions.unity.com/t/web-platform-what-shipped-in-6-5-and-whats-coming-in-6-6/1732387)
- Unity 6000.5.6f1 (29.07): ScheduleUpdateBroadphase затирал дескриптор задачи динамического дерева (ошибки безопасности заданий при ручном вызове Unity.Physics); SortingCriteria.OptimizeStateChanges не ломает SRP-батчи; Resolution/RefreshRate без мусора. [Unity Releases](https://unityreleases.com/releases/6000.5.6f1)
- По диагонали: Multiplayer Services 2.3.0 (28.07) — SessionConnector умеет Join по коду/идентификатору; обработчики распределённой ответственности и реле не пишут неперехватываемый LogError перед SessionException. [Unity Discussions](https://discussions.unity.com/t/multiplayer-service-package-v2-3-0-is-now-publicly-available/1732363)
- По диагонали: Unity Hub 3.20.0 (29.07) — проверка загрузок до установки, повторы, помодульная установка; закрыты внедрение команд через путь установки и подсадка библиотек на macOS. [Unity](https://unity.com/unity-hub/release-notes#3.20.0)
- По диагонали: Input System 1.20.0 (21.07) — устройства не пропадают после обновления пакета при открытом редакторе; InputSystemProvider не выключает общепроектные действия. [Документация Unity](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/changelog/CHANGELOG.html)
- Из прошлого: Unity Web Player (2005–2015) — умер вместе с NPAPI в Chrome, отсюда путь asm.js → WebAssembly.

## 2026-07-31
- Unity → Netflix Games (30.07): выделенная поддержка движка для доставки на мобилки/ТВ + оптимизация под облачный гейминг Netflix; каталог уже частично на Unity (Unhinged, Minigolf). [GamesBeat](https://gamesbeat.com/unity-rolls-out-dedicated-engine-support-to-netflix-games/)
- Doriax (30.07): открытый 2D/3D ECS/data-oriented движок (экс-Supernova) под MIT, v0.6 (тег 24.07), настольный редактор, скриптинг C++/Lua. [GameFromScratch](https://gamefromscratch.com/doriax-game-engine-hands-on/)
- По диагонали: Poinpy (30.07) — Одзиро Фумото/Devolver, эксклюзив Netflix истёк, релиз на мобилки бесплатно (тип-джар, без IAP/рекламы). [Game Developer](https://www.gamedeveloper.com/business/the-truth-behind-the-resurrection-of-poinpy)
- По диагонали: HDR10+ Gaming (30.07) — тон-маппинг на стороне движка со знанием дисплея, авторская картинка; интервью 80.lv (контекст Unreal). [80.lv](https://80.lv/articles/interview-how-hdr10-can-help-game-devs-preserve-their-artistic-vision)
- По диагонали: Don't Lose Aggro (31.07) — MMO-танкинг в соло-рогалик; соло-дев Орен Корен, интервью 80.lv (EA c 15.04). [80.lv](https://80.lv/articles/how-don-t-lose-aggro-reimagines-mmo-tanking-as-a-solo-roguelite)
