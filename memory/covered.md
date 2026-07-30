# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-07-30
- Unity 6.7 Alpha a3 (23.07): редактор собирает экспериментальные CoreCLR Player builds (Win/macOS/Linux); +URP on-tile deferred, SSR renderer feature, Shader Graph Set-mode; Mono уходит в 6.8. [Unity Releases](https://unityreleases.com/releases/6000.7.0a3)
- Steamworks SDK 1.65 (23.07, переизд. 27.07): удалён IsRunningOnSteamDeck(), добавлен IsRunningOnSteamHardware()→ESteamHardwareType; поддержка Steam Frame; пересобранные Win32 steam_api. [Steamworks](https://steamcommunity.com/groups/steamworks/announcements/detail/678504885369439021)
- По диагонали: Люк Дикен (экс-Head of AI Take-Two, 29.07) — ИИ уместен в адаптивном опыте, не в генерации контента; риски недетерминизма/деградации/цены, GenAI как «леса». [80.lv](https://80.lv/articles/game-ai-expert-explains-where-ai-actually-belongs-in-game-development-and-the-risks)
- По диагонали: Double Fine (28.07) — 23 увольнения (~25%) сразу после выхода из-под Microsoft независимой; Тим Шафер. [Game Informer](https://gameinformer.com/2026/07/28/double-fine-announces-layoffs-following-split-from-xbox)
- Из прошлого: Mono (2001, Мигель де Икаса / Ximian) — рантайм скриптинга Unity, теперь заменяется на CoreCLR.

## 2026-07-29
- MCP C# SDK 2.0 (28.07): официальный C#-набор для Model Context Protocol; HTTP-транспорт по умолчанию безсессионный (убраны initialize и Mcp-Session-Id), Multi Round-Trip Requests, стандартизированы заголовки; NuGet ModelContextProtocol* под .NET 8/9/10 + netstandard2.0; реализует редакцию спеки 2026-07-28; v1-код совместим. [.NET Blog](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/)
- EverQuest Legends (28.07): Daybreak + Game Jawn перезапустили MMORPG 1999; свой двусторонний конвертер старых форматов, правка в Blender/3ds Max с реэкспортом в родные форматы; ~1250 вершин, восстановлены заклинательные партиклы; $19.99 + $9.99/мес; движок не назван. [80.lv](https://80.lv/articles/interview-how-everquest-legends-recreates-classic-everquest-s-iconic-visual-style)
- По диагонали: бесплатные ассеты (28.07–11.08) — Fab (Surface Forge 1.1/Dragon Cave/Atlantis Ruins, 1 под Unity) + Unity Asset Store (RPG-анимации код DOUBLEL2026, Bunny Blitz 2D/3D). [GameFromScratch](https://gamefromscratch.com/august-2026-free-gamedev-asset-round-up/)
- По диагонали: SpiritVale (21.07) — инди-MMO ~20k CCU, студия Baikun воюет с ботоводством/RMT через открытое демо; урок про server-authoritative экономику. [Massively OP](https://massivelyop.com/2026/07/21/indie-mmorpg-spiritvale-sees-20000-concurrent-players-as-the-dev-fights-economy-wrecking-bots/)
- По диагонали: side-work clauses (28.07) — Game Developer о давлении HR/юристов студий из-за сторонних проектов сотрудников. [Game Developer](https://www.gamedeveloper.com/business/i-have-been-hunted-down-by-hr-reps-lawyers-and-comms-people-developers-discuss-the-pain-and-prevalence-of-side-work-clauses)
- По диагонали: умерла соосновательница TaleWorlds Ипек Явуз (28.07) — студия Mount & Blade/Bannerlord. [Game Developer](https://www.gamedeveloper.com/business/obituary-taleworlds-entertainment-co-founder-ipek-yavuz-has-passed-away)

## 2026-07-28
- Halo: Campaign Evolved (28.07): ремейк кампании Halo CE на Unreal 5, Slipspace на покой; дебют MegaLights + аппаратный Lumen в большой игре, впервые Halo на PS5; Steam 71% из ~3,4k. [Steam](https://store.steampowered.com/app/2806050/Halo_Campaign_Evolved)
- .NET MSBuild Binlog Analyzer для VS Code (27.07): Copilot читает .binlog, объясняет/чинит падения сборки в 1 клик, ранжирует медленные цели/критический путь; MCP-сервер Microsoft.AITools.BinlogMcp, сравнение с базовым логом. [.NET Blog](https://devblogs.microsoft.com/dotnet/msbuild-binlog-analyzer-vscode/)
- По диагонали: GodotHub (27.07) — open-source кросс-платформенный лаунчер Godot: версии движка, проекты, шаблоны. [GameFromScratch](https://gamefromscratch.com/godothub-awesome-new-launcher-for-godot/)
- По диагонали: BlendCap (27.07) — Blender-аддон мокапа тела/рук/лица из одного видео, локально/офлайн, ретаргет на Rigify/Auto-Rig Pro/Mixamo/CloudRig. [80.lv](https://80.lv/articles/full-body-hand-facial-motion-capture-from-any-video-in-blender)
- По диагонали: noio fake tube interior (27.07) — параллакс-интерьер на цилиндре одним шейдером, дёшево фейкнуть объём. [X](https://x.com/noio_games/status/2080550601188880595)
