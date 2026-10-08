# Listen YouTube bot — сайт

Лендинг для [@Listen_youtubeapp_bot](https://t.me/Listen_youtubeapp_bot): RU на `/`, EN на `/en/`.

- Тексты и ключи — `content.py`, шаблоны — `build.py`, стили и картинки — `static/`.
- Сборка: `python3 build.py` → `docs/` (GitHub Pages: ветка `main`, папка `/docs`).
- Свой домен: `SITE_URL=https://domain python3 build.py` — пересоберёт canonical, hreflang, sitemap и запишет CNAME.
- Коды вебмастеров: `GOOGLE_VERIFY=… YANDEX_VERIFY=… BING_VERIFY=… python3 build.py`.
- CTA-диплинки `?start=site_ru*` / `site_en*` — видны как source в /stats бота.

## Реклама (Яндекс Директ и др.)

- Ссылка в объявлении: `https://gotemapak.github.io/listen-youtube-bot/?s=<метка>` (или `utm_campaign=<метка>`). Все кнопки на странице ведут в бота с `?start=<метка>` — метка видна в /stats бота. Символы: латиница, цифры, `_`, `-`, до 40.
- Метрика: `METRIKA_ID=… python3 build.py`. Клик по любой кнопке бота — цель `tg_click` (создать в Метрике цель типа «JavaScript-событие» с идентификатором `tg_click`).
- Через 1,5 с после клика показывается подсказка «Telegram не открылся? Найдите бота» с копированием имени — на случай замедления Telegram.
- Старые телефоны: только ES5-JS, без `gap` у flex и без `clamp()` без запасного значения, картинка первого экрана 640px JPEG (~30 КБ). Проверено на 320×568.
