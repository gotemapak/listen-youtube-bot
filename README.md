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

## Аналитика и вебмастера (настроено 2026-10-24)

| Сервис | Статус | Где |
|---|---|---|
| Google Search Console | подтверждён meta-тегом (`GOOGLE_VERIFY`), sitemap отправлен | ресурс `https://gotemapak.github.io/listen-youtube-bot/` |
| Bing Webmaster Tools | импортирован из GSC, sitemap отправлен | bing.com/webmasters |
| Яндекс Метрика | счётчик **113767924**, цель `tg_click` (JS-событие, клик по кнопке «в бота») | metrika.yandex.ru |
| Яндекс.Вебмастер | права подтверждены 2026-10-24; код `311461a2c8f6c26f`: meta-тег + файл `static/yandex_311461a2c8f6c26f.html` | webmaster.yandex.ru |
| IndexNow | ключ в `static/<key>.txt` | отправка: `POST https://api.indexnow.org/indexnow` |

`METRIKA_ID`, `YANDEX_VERIFY` и `GOOGLE_VERIFY` прописаны в `build.py` как значения по умолчанию, поэтому `python3 build.py` без переменных их сохраняет. Не обнуляй их при пересборке, иначе пропадут счётчик и подтверждения.

### Почему есть отдельный репозиторий `gotemapak/gotemapak.github.io`

Сайт живёт в подпапке чужого домена. Яндекс.Вебмастер подтверждает права только на **весь хост** `gotemapak.github.io` и ищет файл в корне домена. Раньше корень отдавал 404, и подтверждение не проходило. Поэтому создан корневой сайт [gotemapak/gotemapak.github.io](https://github.com/gotemapak/gotemapak.github.io). В нём лежат:
- файл и meta-тег подтверждения Яндекса;
- корневой `robots.txt`: поисковики читают только его, а `docs/robots.txt` в подпапке игнорируют. В нём разрешён весь хост и указан sitemap этого сайта;
- ключ IndexNow;
- `index.html`: переадресация на этот сайт, `noindex`.

Всё в нём публично по необходимости, секретов там нет. **Не удаляй этот репозиторий**, пока сайт живёт на github.io: Яндекс периодически перепроверяет права. Если бот переедет на свой домен (`SITE_URL=https://domain python3 build.py`), корневой репозиторий можно удалить, а сайт заново подтвердить на новом домене во всех трёх вебмастерах.

Ключи API (Google service account, Bing, Яндекс OAuth) хранятся локально в `08-Code/extensions/agents/.env`, в git их нет. Как ими пользоваться, описано в `08-Code/extensions/agents/skills/analytics-seo-ops/SKILL.md`.
