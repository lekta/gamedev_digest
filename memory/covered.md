# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-16
- Unity 6.6 beta (снапшот 6000.6.0b8, 12.08): Compute GPU Light Baker (компьют-шейдеры + аппаратный RT, эмуляция без RT), Mesh LOD GPU Instancing, плавучесть/ветер в 2D-физике (PhysicsBody.BuoyancyInput/WindInput), on-tile постобработка, GetInstanceID()→GetEntityId() в Physics/Raycast, managed-компоненты и мульти-playback ECB под удаление. [Unity Releases](https://unityreleases.com/releases/6000.6.0b8)
- NuGet: ключи публикации 30 дней (анонс .NET Team 03.08, дедлайн 17.08): новые ключи ≤30 дн, 365-дн опция убрана, старые умрут 01.11; альтернатива — Trusted Publishing (OIDC, GitHub Actions/GitLab; Azure DevOps нет). [.NET Blog](https://devblogs.microsoft.com/dotnet/strengthening-nuget-supply-chain-security-reducing-api-key-lifetime/)
- По диагонали: Memoirium (80.lv, 12.08) — соло PS1-Souls за 3–4 года, Blender-ассеты 256×256, анимации с Unreal Marketplace, издатель Outersloth; движок не назван. [80.lv](https://80.lv/articles/memoirium-building-a-soulslike-retro-game-as-a-solo-developer)
- По диагонали: SpriteLoop (Balkan Ram Games, 13.08) — бесплатный cut-out аниматор Win/Mac/Linux, экспорт спрайтшитов/GIF/WebP, рантайм под Defold, в Unity через спрайтшиты; урезанный Spriter/Spine. [GameFromScratch](https://gamefromscratch.com/spriteloop-free-2d-animation-tool/)
- По диагонали: Godot 4.8 dev3 (10.08) — 176 фиксов/91 контрибьютор после GodotCon Boston, visionOS в XR-подсистему, high-polling мышь на Windows, не для прода. [Godot](https://godotengine.org/article/dev-snapshot-godot-4-8-dev-3/)
- Из прошлого: эволюция запекания света Unity — Beast → Enlighten → Progressive Lightmapper → Compute GPU Light Baker.

## 2026-08-15
- Visual Studio 2026 18.9 (11.08): у Copilot переключатель усилия низкий/средний/высокий + цена/окно контекста моделей, рабочие деревья Git, свои агенты на уровне организации, проверка незакоммиченного кода агентом. [Microsoft Learn](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes)
- VS Code 1.133 (12.08): окно агентов по своему ключу Claude без входа в GitHub, смена провайдера между ходами (Anthropic/Copilot рядом), один сеанс на несколько окон (Agent Host Protocol). [VS Code](https://code.visualstudio.com/updates)
- По диагонали: Instructions Hygiene (.NET Blog, Уэнди Брайдинг, 12.08) — файл инструкций для ИИ-агента как бюджет контекста: держать только неочевидное/проверенное, ревизия «оставить/убрать/перенести/проверить»; принцип общий. [.NET Blog](https://devblogs.microsoft.com/dotnet/instructions-hygiene-what-frontier-models-still-need-you-to-say/)
- По диагонали: Phantom Blade Zero (S-GAME, 14.08) — боёвку строили из mocap Донни Йена на полной скорости, реакции боссов проектировали под длину комбо; движок не назван. [80.lv](https://80.lv/articles/phantom-blade-zero-uses-authentic-kung-fu-motion-capture)
- По диагонали: Downtown Generator V2 (Мохамед Эльшериф, 14.08) — процедурный центр города для Blender 5.0+, облегчённый режим, 180+ зданий и 50+ пропсов. [80.lv](https://80.lv/articles/procedural-american-downtown-generator-for-blender)
- Из прошлого: IntelliSense (Visual Basic 5.0 / Visual C++ 5.0, 1997) — автодополнение по членам типа; 29 лет спустя та же подсказка в VS получила переключатель усилия и ценник в токенах.

## 2026-08-14
- Netflix закрывает Night School Studio (Oxenfree на Unity, Oxenfree II, Unhinged) + Moonloot Games (13.08); Night School — первая покупка Netflix (сен.2021), Unhinged хвалили за месяц до конца; подписочный капкан как у Refactor/FIFA World Cup — «успех на сервисе» ≠ выживание. [PC Gamer](https://www.pcgamer.com/gaming-industry/netflix-closes-oxenfree-developer-night-school-just-a-month-after-praising-its-new-game-as-one-of-the-companys-most-successful-cloud-game-debuts/)
- Microsoft.Extensions.AI 10.9.0+ (Джошуа Юэ, 13.08): экспериментальные RoutingChatClient / SemanticRoutingChatClient (эмбеддинги) / FailoverChatClient(+Ordered), атрибут Experimental MEAI001; маршрут по стоимости/смыслу + резерв при сбое провайдера; .NET 8+, в Unity-Mono не из коробки (ждёт CoreCLR-плеер). [.NET Blog](https://devblogs.microsoft.com/dotnet/routing-and-failover-for-microsoft-extensions-ai/)
- По диагонали: Saber Interactive (13.08) согласилась добавить ИИ-дисклеймер в Rideshare Simulator после критики, сначала отрицав «замену сценаристов ИИ»; маркировка то за студию, то против. [Game Developer](https://www.gamedeveloper.com/business/saber-interactive-to-add-rideshare-stimulator-ai-disclosure-after-public-controversy)
- По диагонали: Meccha Chameleon (Lemorion_1224/Haganeiro, UE5, 12.08) — 20 млн продаж за 2 мес (было 7 млн/2 нед); концепт из Fortnite UEFN → свой Steam-релиз; у Unity своего UGC-маркетплейса под этот путь нет. [Game Developer](https://www.gamedeveloper.com/business/meccha-chameleon-sells-7m-copies-in-first-two-weeks)
- По диагонали: 2K / Small Axe Studios (13.08) — новая ванкуверская студия под спортивный ААА, глава Аарон Макхарди (экс-EP Madden/FIFA, ~18 лет в EA); движок не назван; контрбаланс к закрытиям. [Inven Global](https://www.invenglobal.com/articles/24778/2k-establishes-new-sports-studio-with-former-fifa-developers)
- Из прошлого: Night School (осн.2014 экс-Telltale/Disney), дебют Oxenfree (2016, Unity) с «живым» диалогом по рации → куплена Netflix первой в сен.2021 → закрыта 5 лет спустя.
