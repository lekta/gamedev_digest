# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

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

## 2026-07-30
- Unity 6.7 Alpha a3 (23.07): редактор собирает экспериментальные CoreCLR Player builds (Win/macOS/Linux); +URP on-tile deferred, SSR renderer feature, Shader Graph Set-mode; Mono уходит в 6.8. [Unity Releases](https://unityreleases.com/releases/6000.7.0a3)
- Steamworks SDK 1.65 (23.07, переизд. 27.07): удалён IsRunningOnSteamDeck(), добавлен IsRunningOnSteamHardware()→ESteamHardwareType; поддержка Steam Frame; пересобранные Win32 steam_api. [Steamworks](https://steamcommunity.com/groups/steamworks/announcements/detail/678504885369439021)
- По диагонали: Люк Дикен (экс-Head of AI Take-Two, 29.07) — ИИ уместен в адаптивном опыте, не в генерации контента; риски недетерминизма/деградации/цены, GenAI как «леса». [80.lv](https://80.lv/articles/game-ai-expert-explains-where-ai-actually-belongs-in-game-development-and-the-risks)
- По диагонали: Double Fine (28.07) — 23 увольнения (~25%) сразу после выхода из-под Microsoft независимой; Тим Шафер. [Game Informer](https://gameinformer.com/2026/07/28/double-fine-announces-layoffs-following-split-from-xbox)
- Из прошлого: Mono (2001, Мигель де Икаса / Ximian) — рантайм скриптинга Unity, теперь заменяется на CoreCLR.
