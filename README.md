# Listen YouTube bot — сайт

Лендинг для [@Listen_youtubeapp_bot](https://t.me/Listen_youtubeapp_bot): RU на `/`, EN на `/en/`.

- Тексты и ключи — `content.py`, шаблоны — `build.py`, стили и картинки — `static/`.
- Сборка: `python3 build.py` → `docs/` (GitHub Pages: ветка `main`, папка `/docs`).
- Свой домен: `SITE_URL=https://domain python3 build.py` — пересоберёт canonical, hreflang, sitemap и запишет CNAME.
- Коды вебмастеров: `GOOGLE_VERIFY=… YANDEX_VERIFY=… BING_VERIFY=… python3 build.py`.
- CTA-диплинки `?start=site_ru*` / `site_en*` — видны как source в /stats бота.
