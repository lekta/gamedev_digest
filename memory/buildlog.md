# Техотчёт сборки

Окно 7 дней. По строке на пункт. Тех-заметки, которые НЕ идут в публикуемый текст.

---

## 2026-08-23
- Репортёр: Игорь Потусторонний (ротация: искл. Пётр/22, Геннадий/21, Мирча/19).
- Главное: Big Walk (Unity, картинка Steam og:image ✓), Stars Reach (Steam og:image ✓), VS Copilot modernization agent (без картинки — devblogs без осмысленного og:image, только логотип).
- Big Walk: движок Unity подтверждён косвенно (House House = Untitled Goose Game на Unity; GameDiscoverCo движок не называет). Цифры сверены: 1 млн/6 дней, 46k пик, ~1 млн вишлистов, 6% пересечения — GameDiscoverCo; 95%/15,9k, кооп 2–12 — Steam.
- Stars Reach: первоисточник starsreach.com/hotfix-... → HTTP 403 (и MassivelyOP тоже 403 на прямой fetch); факты (утечка памяти → резинение, хотфикс + incident-мониторинг, mixed 51%/250, <1000 CCU, EA 18.08) сверены через WebSearch-сводку + Steam. Ссылка — пересказ MassivelyOP. Rolling-release деталь придержана как неподтверждённая, в текст не пошла.
- Диагональ: Battlefield 6 (патч 1.4.2.0 18.08, всплеск в окне — подан с датой 18.08), Cursor 19.08, Neuron Activation 22.08, Monsters & Memories 21.08.
- Отброшено по кулдауну: Rider 2026.2.1 point-release (Rider освещён 21.08), Godot 4.7.2/3.6.3 maintenance (Godot — 22.08), .NET 11 Preview 7 (отыгран 13.08), GitHub Copilot Slack/Teams (слабо для Unity/C#, AI-блок и так занят VS+Cursor).
- Кулдаун-чек covered.md (3 дня 19–22): совпадений по выбранным субъектам нет.