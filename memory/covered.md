# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-25
- DLSS 4.5 Ray Reconstruction (NVIDIA, Gamescom 25.08): трансформер 2-го поколения слил денойз трассировки и апскейл в одну модель; +35% вычислений/+20% параметров при той же скорости; все RTX 20–50, 27 игр, раздача через приложение NVIDIA, денойз в Blender 5.3 осенью. [NVIDIA](https://www.nvidia.com/en-us/geforce/news/dlss-4-5-ray-reconstruction-1000-rtx-games-apps-out-now/)
- Roblox open-source модерация (ROOST, 19.08): три модели — PII Classifier v2.0 (189 языков, F1 63,41→90,52), Sentinel v2 (~70% ранних детектов, ROC-AUC 0,996), голосовой v3 (30 языков, 8 категорий, 61% полноты при 1% FP); Hugging Face/GitHub. [Roblox](https://about.roblox.com/newsroom/2026/08/roblox-open-source-safety-models-roost)
- Свиток Тайу (ConchShip, интервью 80.lv 24.08): уся-песочница на Unity держит 5000–10000 процедурных NPC с целями/связями/биографией, эмерджентная драма; 16 регионов, ~4,5 млн иероглифов, 8 лет; рантайм не раскрыт. [80.lv](https://80.lv/articles/interview-building-a-wuxia-sandbox-rpg-with-up-to-10-000-dynamic-npcs)
- По диагонали: Infinity Code Online Maps v5 (24.08) — карты 2D/3D в Unity, маршруты/геокодинг/GPS/высоты, C# без зависимостей, 16+ провайдеров, mobile/desktop/WebGL/AR-VR. [80.lv](https://80.lv/articles/this-unity-asset-pack-allows-you-to-add-interactive-2d-and-3d-maps-to-your-games)
- По диагонали: AMD attention-based indirect illumination (SIGGRAPH 2026, 20.08) — нейро-GI diffuse+specular по буферам камеры и RSM, 2,19M параметров, ~45мс 512×512 на MI250; до реалтайма далеко. [GPUOpen](https://gpuopen.com/learn/lightweight-attention-based-indirect-illumination/)
- По диагонали: VKD3D 2.1 (24.08) — D3D12 поверх Vulkan (Wine/Proton), улучшен HLSL-компилятор (dead store elim), FP-конверсии DXIL, совместимость GLSL; сверка для DirectX-сборок под SteamOS. [Phoronix](https://www.phoronix.com/news/VKD3D-2.1-Released)
- По диагонали: Defold 1.13.1 (17.08) — свет для 2D/3D (4 типа через LightBuffer), база геймпадов SDL, тёплые сборки до -19%, экспериментальный Metal; Lua-движок. [Defold](https://defold.com/2026/08/17/Defold-1-13-1/)
- По диагонали: Neotolis Engine (19.08) — свой движок на C17 за 5 мес (WASM+WebGL2/OpenGL3.3, code-first), игра за месяц, код через Claude; показан на Comic Con Tashkent. [Habr](https://habr.com/ru/articles/1072162/)

## 2026-08-24
- Vapor World: Over The Mind (ALIVE Inc., 21.08): 2D-соулслайк вырезал все ИИ-катсцены после обвала отзывов (~25%→38%); директор Ён Ким, замена на рисованные вручную; ранний доступ 18.08, Steam+Game Pass. [GamesRadar](https://www.gamesradar.com/games/action/after-25-percent-positive-steam-reviews-soulslike-dev-realizes-people-hate-ai-slop-and-admits-if-it-looks-like-the-effort-is-not-there-that-is-a-fair-reading-of-what-is-on-screen/)
- River Modeler (Staggart Creations, 21.08): сплайновый генератор рек Unity стал расширением Stylized Water 3; Job System+Burst +2400%, сегментация меша, пул аудио-эмиттеров вокруг камеры; $35. [Unity Discussions](https://discussions.unity.com/t/river-modeler-spline-based-river-creation/941439)
- Обзор ECS-стека (DreamingImLatios, 10.08): по оценке автора графика/физика DOTS в режиме поддержки, Havok прекращён, единая система трансформов снова за scripting define, нет колбэков жизненного цикла Entity. [Unity Discussions](https://discussions.unity.com/t/august-2026-ecs-stack-review/1733474)
- По диагонали: VHOLUME (Леонар Леметр / ex-Straftat Unity, 21.08) — паркур-брутализм, «крайне положительные» 97%/876, гонки с «призраками» друзей; движок VHOLUME официально не назван. [PC Gamer](https://www.pcgamer.com/games/action/the-indie-parkour-game-from-one-of-the-french-brothers-behind-2024s-best-fps-is-coming-out-in-just-two-weeks/)
- По диагонали: Tencent Games Central Tech (21.08) — к gamescom показывают LightSpeed AI Platform (LAP), облачный конвейер генерации ассетов, бета сент.; сессии по ИИ-анимации/FPS-агентам/автотестам. [gamespress](https://www.gamespress.com/Tencent-Games-Lights-Up-gamescom-2026-with-Massive-Title-Lineup-Featur)
- По диагонали: Grow a Garden (август) — лаг-дюп редких питомцев (Kitsune) обвалил экономику, Jandel отключил дарение 2-й раз, обещана система обмена; нет проверки провенанса. [Distractify](https://www.distractify.com/p/why-is-pet-gifting-disabled-in-grow-a-garden)
- По диагонали: Aerial_Knight's MrFreezy (демо 20.08) — пазл про выстраивание голов в ряд и снос топором за лимит ходов, ч/б подача; релиз 1.09. [aftermath](https://aftermath.site/mrfreezy-demo-impressions/)
- По диагонали: Proton 11.0-2 (21.08) — Wine 11.0, обновлены VKD3D-Proton/DXVK, фиксы регрессий; точка сверки для DirectX-сборок на SteamOS/Steam Machine. [GamingOnLinux](https://www.gamingonlinux.com/2026/08/proton-11-0-2-is-out-with-lots-of-gaming-fixes-for-linux-steamos-steam-deck-steam-machine/)

## 2026-08-23
- Big Walk (House House, Unity, GameDiscoverCo 21.08): кооп-«болталка» на Unity ~1 млн копий за 6 дней, пик 46k CCU, ~1 млн вишлистов, всего 6% пересечения с Untitled Goose Game; кооп 2–12, изд. Panic, $20, «крайне положительные» 95%/15,9k. [GameDiscoverCo](https://newsletter.gamediscover.co/p/will-big-walks-1m-sales-usher-in)
- Stars Reach (Playable Worlds/Раф Костер, EA 18.08): сырой старт, «резинение» от серверной утечки памяти, хотфикс + система мониторинга инцидентов; «смешанные» 51%/~250, онлайн <1000; движок — своя облачная симуляция. [MassivelyOP](https://massivelyop.com/2026/08/22/stars-reach-puts-out-a-hotfix-that-attacks-a-wide-list-of-bugs-and-issues/)
- Visual Studio Copilot modernization agent (Microsoft, 21.08): агент тащит .NET Framework→.NET 10 пошагово, «направляемый» режим с чекпойнтами и md-отчётом в VCS = точки отката; пример System.Web.Mvc→ASP.NET Core, EF6→EF Core. [VS Blog](https://devblogs.microsoft.com/visualstudio/today-i-will-modernize-a-net-application/)
- По диагонали: Battlefield 6 (DICE, апдейт 1.4.2.0 18.08) — авиарежимы «Top Gun» + возврат Wake Island + бесплатный триал до 25.08 подняли онлайн, пик ~69k, рост в топе Steam. [Steam](https://store.steampowered.com/news/app/2807960/view/685261553769906387)
- По диагонали: Cursor (19.08) — облачные агенты «всегда на связи», команда /goal, субагенты на своих машинах. [Cursor](https://cursor.com/changelog)
- По диагонали: Neuron Activation (80.lv 22.08) — «цифровой фиджет-бокс», тактильные микровзаимодействия, механика Neuron Activation сбрасывает поле и множит счёт; движок не назван, релиз конец 2026. [80.lv](https://80.lv/articles/this-digital-fidget-box-game-has-a-lot-of-satisfying-tactile-interactions)
- По диагонали: Monsters & Memories (MassivelyOP 21.08) — реворк двух классов + новые данжи сдвигают пати-мету в forced-grouping MMO. [MassivelyOP](https://massivelyop.com/2026/08/21/monsters-and-memories-revamps-two-classes-launches-new-dungeons-and-applies-multiple-fixes-and-tweaks/)
