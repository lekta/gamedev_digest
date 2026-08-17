# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-17
- Hell Let Loose: Vietnam (Expression Games/Team17, релиз 13.08): пик ~30574 CCU, но отзывы «смешанные» 60% из ~4,6k; AMD-вылеты лечатся флагом `-dx12` (баг в одном граф-бэкенде), отказ VOIP, трение VIP-слотов; хотфикс к выходным. [Steam](https://store.steampowered.com/app/3079210/)
- GunZ: The Duel (Masangsoft, F2P рестарт классики 2013, релиз 13.08): «смешанные» 40% (449/1102), ~1,8k CCU; жалобы — предположительно ИИ-ассеты (иконки/текстуры/карты), пинг, сломанные механики/тикрейт из беты, читеры; фан-серверы лучше официального. [Steam](https://store.steampowered.com/app/3139440/)
- По диагонали: Number Machine: Math Factory (ARIELEK, 80.lv 17.08) — фабрика-головоломка в духе Opus Magnum с одним непрерывным проездом камеры на все переходы; меню спрятано «под» картой, движок не назван. [80.lv](https://80.lv/articles/indie-dev-shows-seamless-animation-made-for-factory-game-inspired-by-opus-magnum-infinifactory)
- По диагонали: The Sinking City 2 (Frogwares, релиз 18.08) — лавкрафт-хоррор переехал на UE5.8 под конец разработки ради оптимизации; демо-бенчмарки показывают стуттеры/рывки на переходах. [Notebookcheck](https://www.notebookcheck.net/The-Sinking-City-2-pre-orders-open-ahead-of-August-18-launch.1349870.0.html)
- По диагонали: Game Animation Sample (Epic) обновлён под UE 5.8 — 500+ анимаций, motion matching, pose search, look-at, экспериментальный Physics Control Component; референс для Unity-аниматора. [Unreal Engine](https://www.unrealengine.com/tech-blog/download-the-latest-game-animation-sample-project-now-updated-for-ue-5-8)
- Из прошлого: GunZ K-style/butterfly — отмена анимаций перезарядки стала фирменной мувмент-метой, которую сообщество вытащило из бага и пережило студию.

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
