# Техотчёт сборки

Окно 7 дней. По строке на пункт. Тех-заметки, которые НЕ идут в публикуемый текст.

---

## 2026-08-24
- Репортёр: Ником (ротация: искл. Игорь/23, Пётр/22, Геннадий/21; Ником вёл 18, вне окна 3). Файл memory/reporters.md отсутствует — персонаж восстановлен по подписи и стилю digests/2026-08-18.
- Ядро тихое: блог .NET стоит с 13.08, unity.com/blog отдаёт 403, свежих первоисточников строго 22–24.08 почти нет (подтвердили 4 подагента-разведчика). Собран выпуск из свежих кейсов/тулов + один догоняющий.
- Главное: Vapor World (Steam og:image ✓, движок НЕ подтверждён — вывод дан engine-agnostic «на любом движке»; факты сверены: 25%→38%/65, EA 18.08, $13,49, цитаты Ён Кима — GamesRadar + Steam news post, прямой fetch Steam news отдал только навигацию, факты через WebSearch-сводку GamesRadar/Sankaku/DualShockers). River Modeler (без картинки — Asset Store og:image не отдался через доступный fetch, отдельный поиск не делал; факты из discussions.unity.com: Staggart Creations, Job System+Burst +2400%, сегментация, пул аудио-эмиттеров, становится расширением Stylized Water 3, $35). ECS Stack Review (10.08, догоняющий, без картинки — форум; заявления автора DreamingImLatios поданы как его оценка, не факт Unity).
- Диагональ: VHOLUME (движок VHOLUME не назван, Straftat=Unity подтверждён Wikipedia — подано как родословная), Tencent Central Tech/LAP (21.08, к gamescom 26–30.08), Grow a Garden дюп (Roblox, дата «август», подано без точного числа), MrFreezy (демо 20.08), Proton 11.0-2 (21.08).
- Кулдаун-чек covered.md (22–23) + 3-дневное окно: совпадений по субъектам нет. Отброшено по кулдауну/повтору: C# 16 LDM 05.08 (C# освещён 22.08 — придержан, ушёл в to_explore), Rider/ReSharper 2026.2.1 point-release (Rider — 21.08), CS2 wall-surfing exploit (Valve/Deadlock — 21.08, к тому же без цифр CCU), Mesa 26.2.1 (Mesa 26.2 — главное 08.08, слабый point-release). Proton взят как отдельный продукт-инфраструктура, не «игра Valve».
- Отброшено по свежести/профилю: Hell Let Loose: Vietnam (13.08, уже 17.08), Throne&Liberty Amazon exit (12.08, бизнес), Compulsion/Double Fine выкуп IP (20–21.08, ближе к финансам), .NET 11 Preview 7 (отыгран 13.08), Microsoft.Extensions.AI routing (отыгран 14.08), EfT Unity 6 (dtf-статья от 20.06, несвежая).

## 2026-08-23
- Репортёр: Игорь Потусторонний (ротация: искл. Пётр/22, Геннадий/21, Мирча/19).
- Главное: Big Walk (Unity, картинка Steam og:image ✓), Stars Reach (Steam og:image ✓), VS Copilot modernization agent (без картинки — devblogs без осмысленного og:image, только логотип).
- Big Walk: движок Unity подтверждён косвенно (House House = Untitled Goose Game на Unity; GameDiscoverCo движок не называет). Цифры сверены: 1 млн/6 дней, 46k пик, ~1 млн вишлистов, 6% пересечения — GameDiscoverCo; 95%/15,9k, кооп 2–12 — Steam.
- Stars Reach: первоисточник starsreach.com/hotfix-... → HTTP 403 (и MassivelyOP тоже 403 на прямой fetch); факты (утечка памяти → резинение, хотфикс + incident-мониторинг, mixed 51%/250, <1000 CCU, EA 18.08) сверены через WebSearch-сводку + Steam. Ссылка — пересказ MassivelyOP. Rolling-release деталь придержана как неподтверждённая, в текст не пошла.
- Диагональ: Battlefield 6 (патч 1.4.2.0 18.08, всплеск в окне — подан с датой 18.08), Cursor 19.08, Neuron Activation 22.08, Monsters & Memories 21.08.
- Отброшено по кулдауну: Rider 2026.2.1 point-release (Rider освещён 21.08), Godot 4.7.2/3.6.3 maintenance (Godot — 22.08), .NET 11 Preview 7 (отыгран 13.08), GitHub Copilot Slack/Teams (слабо для Unity/C#, AI-блок и так занят VS+Cursor).
- Кулдаун-чек covered.md (3 дня 19–22): совпадений по выбранным субъектам нет.