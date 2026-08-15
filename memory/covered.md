# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

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

## 2026-08-13
- .NET 11 Preview 7 (Microsoft, 11.08): runtime-async tiering + tail-await, NativeAOT CLI и MSBuild server по умолчанию; C# labeled break/continue, union-паттерны, exhaustiveness для closed-типов; dotnet test --timeout/--maximum-failed-tests; Complex<T>, IEEE754 decimal, STJ closed-полиморфизм; GA ноябрь. [.NET Blog](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-7/)
- Unity 6.7 главная панель (Томас Лопес, анонс 07.08): MainToolbarCustomElement стал public API, свои кнопки через наследование MainToolbarButton + ExecuteMenuItem(), любимые MenuItem на панель через QuickSearch без кода, группы/тоглы визуально отличимы. [Unity Discussions](https://discussions.unity.com/t/customizable-main-toolbar-unity-6-7-improvements/1733331)
- По диагонали: BALL x PIT (Кенни Сан/Devolver, Unity, релиз окт.2025) — брик-брейкер-рогалик перевалил 2 млн копий <за год, вышло финальное бесплатное обновление Naturalist. [Push Square](https://www.pushsquare.com/news/2026/08/devolvers-brilliant-roguelite-dopamine-factory-ball-x-pit-is-a-smash-hit-at-2-million-sales)
- По диагонали: Gamescom Dev опрос (12.08) — 100 спикеров, 83% ждут влияния ИИ на команды/продуктивность, 36% «изменит роли, не срежет штат», 33% меньше команды; ИИ в коде/продакшене 34%, 30% за минимум ИИ; год к году без сдвига. [Game Developer](https://www.gamedeveloper.com/business/developers-expect-generative-ai-to-impact-roles-and-team-sizes-in-the-next-three-years)
- По диагонали: Amazon Games (12.08) выходит из издания Lost Ark и Throne and Liberty на Западе — TL к Q4 2026 к NC (FirstSpark), Lost Ark к нач.2027 к Smilegate; игры/аккаунты остаются. [Massively OP](https://massivelyop.com/2026/08/12/amazon-will-cease-publishing-lost-ark-and-throne-liberty-sending-them-back-to-smilegate-and-ncsoft/)
- Из прошлого: async/await появились в C# 5.0 / .NET Framework 4.5 (август 2012), конечный автомат генерировал компилятор → .NET 11 встраивает async в рантайм.
