# Уже разобрано

Окно: последние 3 дня. Всё старше — в `digests/YYYY-MM-DD.md`.
Формат: дата · короткая тема (≤120 символов) · одна ссылка на первоисточник.
При сборке нового дайджеста: добавить день сверху, удалить день, выпавший из окна.

---

## 2026-08-18
- Forbidden Solitaire (Grey Alien Games, постмортем Game Developer 17.08): хоррор-пасьянс на собственном пасьянсном движке студии (16 игр) + боёвка из Shadowhand/Ancient Enemy, раскладка tri-peaks/golf вместо Клондайка, обёртка «запрещённая сатанинская игра из 90-х» (визуал Night Signal); релиз 30.04, 10k копий/48ч, пик 880 vs 98 (Regency Solitaire II)/20 (Shadowhand Solitaire), «крайне положительные» 96% из ~2000. [Game Developer](https://www.gamedeveloper.com/design/how-forbidden-solitaire-brought-solitaire-games-to-the-forefront)
- Claude Code 2.1.234 (17.08): отклонение путей NT-namespace `\??\` при чтении файлов/восстановлении сессий (защита от утечки NTLM-учёток на Windows), фикс потери ответов на запросы прав во время фоновых подагентов, бейдж статуса GitLab MR в статусной строке, авто-продолжение сессии после сброса лимитов Claude.ai. [changelog](https://code.claude.com/docs/en/changelog)
- По диагонали: Plushie Dreadfuls (American McGee/Stunt Puppet Pictures, 80.lv 17.08) — стоп-моушен-пайплайн Dragonframe→After Effects→Photoshop, проволочные скелеты в куклах, ~3с анимации/смену при 24 к/с; текущий Spare Hearts на Godot, крупный Dreadfuland планируют на Unreal. [80.lv](https://80.lv/articles/creating-stop-motion-animation-for-american-mcgee-s-plushie-dreadfuls)
- По диагонали: Mortal Shell II (Cold Symmetry, ранний доступ 17.08, релиз 20.08) — соулслайк на UE5 (1-я часть UE4), пик ~20k, ~80% положительных на старте, «выдержка» вместо стамины, RTX 5090 4K/ultra с RT ~80–90 к/с. [Hardcore Gamer](https://hardcoregamer.com/mortal-shell-ii-review/)
- По диагонали: ядро Linux 7.2 (16.08) — прирост Intel Arc B390, HDMI 2.1 FRL в AMDGPU, ускорение poll/IO; фон для SteamOS/Proton-сборок. [Phoronix](https://www.phoronix.com/news/Linux-7.2-Released)
- Из прошлого: Windows Solitaire (1990, Windows 3.0) — положили в комплект как тренажёр drag-and-drop мышью, не ради игры.

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
