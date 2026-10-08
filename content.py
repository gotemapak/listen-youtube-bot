"""Page copy for the site. One dict per page; `pair` links RU and EN twins
for hreflang. Body sections are trusted HTML fragments.

Keyword clusters (RU: Yandex Wordstat May 2026 + Yandex/Google suggest
Oct 2026; EN: Google US suggest Oct 2026):
  home       — видео ютуб в аудио, бот ютуб в аудио тг, слушать ютуб без видео
               youtube to audio telegram bot, youtube audio only
  background — слушать ютуб в фоновом режиме / с выключенным экраном (андроид, айфон)
               listen to youtube in background (without premium, iphone, android)
  transcript — расшифровка видео ютуб в текст по ссылке, конспект видео ютуб нейросеть
               get transcript of youtube video, youtube video to text, summarize
  listen     — ютуб слушать лекции, подкасты, аудиокниги, аудиорассказы
               youtube podcasts / lectures / audiobooks offline
"""

BOT = "Listen_youtubeapp_bot"

RU = "ru"
EN = "en"

UI = {
    RU: {
        "cta": "Открыть бота в Telegram",
        "cta_short": "Открыть бота",
        "how": "Как это работает",
        "steps": [
            ("Откройте бота", "Нажмите кнопку — бот откроется в Telegram на телефоне или компьютере."),
            ("Пришлите ссылку", "Видео, Shorts или целый плейлист с YouTube — просто вставьте ссылку."),
            ("Слушайте", "Через минуту придёт аудио в плеере Telegram и кнопка «📄 Текст видео»."),
        ],
        "faq": "Частые вопросы",
        "more": "Ещё по теме",
        "lang_switch": "English",
        "free_note": "Первые 2 ссылки бесплатно · дальше безлимит — 299 ₽/мес или 1990 ₽/год",
        "footer": "Telegram-бот, который превращает видео YouTube в аудио и текст. Не связан с YouTube и Google.",
        "img_alt": "Ссылка YouTube превращается в аудио MP3 и текстовый файл с расшифровкой в Telegram",
        "trust": "2 ссылки бесплатно · без регистрации · работает на любом телефоне с Telegram",
        "fallback": "Telegram не открылся? Найдите в поиске Telegram бота",
        "copy": "Скопировать",
        "copied": "Скопировано",
        "nf_title": "Страница не найдена",
        "nf_text": "Такой страницы нет. Зато есть бот, который превращает YouTube в аудио:",
    },
    EN: {
        "cta": "Open the bot in Telegram",
        "cta_short": "Open the bot",
        "how": "How it works",
        "steps": [
            ("Open the bot", "Tap the button — the bot opens in Telegram on your phone or computer."),
            ("Send a link", "A YouTube video, Short or a whole playlist — just paste the link."),
            ("Listen", "In about a minute you get audio in Telegram's player plus a “📄 Video text” button."),
        ],
        "faq": "FAQ",
        "more": "Related guides",
        "lang_switch": "Русский",
        "free_note": "Your first 2 links are free · then an unlimited plan in the bot",
        "footer": "A Telegram bot that turns YouTube videos into audio and text. Not affiliated with YouTube or Google.",
        "img_alt": "A YouTube link turns into an MP3 audio file and a transcript text file in Telegram",
        "trust": "2 links free · no sign-up · works on any phone with Telegram",
        "fallback": "Telegram didn't open? Search Telegram for the bot",
        "copy": "Copy",
        "copied": "Copied",
        "nf_title": "Page not found",
        "nf_text": "This page doesn't exist. But the bot that turns YouTube into audio does:",
    },
}

PAGES = [
    # ------------------------------------------------------------------ RU
    {
        "lang": RU, "path": "/", "pair": "home", "src": "site_ru",
        "nav": "Главная",
        "title": "Видео YouTube в аудио — Telegram-бот: слушать в фоне + текст",
        "description": "Пришлите ссылку на YouTube в Telegram-бот — получите аудио для прослушивания в фоне и с выключенным экраном, а также текст видео. Лекции, подкасты, плейлисты.",
        "h1": "Слушайте YouTube как подкаст — прямо в Telegram",
        "sub": "Пришлите ссылку — бот вернёт аудио, которое играет в фоне и с выключенным экраном, и текст видео.",
        "lead": "Отправьте боту ссылку на видео или плейлист — он пришлёт аудио, которое играет в фоне и с выключенным экраном, и текст видео, который удобно отдать ChatGPT или сохранить в заметки.",
        "sections": [
            ("Что умеет бот", """
<ul class="features">
<li><b>YouTube в аудио.</b> Звуковая дорожка видео приходит MP3-файлом в плеер Telegram — слушайте без видео, в наушниках, в машине.</li>
<li><b>Фон и выключенный экран.</b> Telegram играет аудио, когда вы свернули приложение или заблокировали телефон. Без YouTube Premium.</li>
<li><b>Текст видео.</b> Кнопка «📄 Текст видео» присылает расшифровку файлом — чтобы попросить ИИ сделать конспект или найти нужное место.</li>
<li><b>Длинные видео и плейлисты.</b> Видео до ~11 часов приходит частями, плейлист — целиком, трек за треком.</li>
<li><b>Всё остаётся у вас.</b> Аудио лежит в чате: можно слушать офлайн, переслать другу или в «Избранное».</li>
</ul>"""),
            ("Кому это нужно", """
<p>Тем, кто смотрит YouTube ушами: <a href="/lekcii-podkasty-audioknigi/">лекции, подкасты и интервью</a>, аудиокниги и аудиорассказы, разборы и обучающие видео. Картинка в таких роликах не важна, а держать экран включённым — неудобно и садит батарею.</p>
<p>Если вы ищете, <a href="/slushat-youtube-v-fone/">как слушать YouTube в фоновом режиме</a> на Android или iPhone, бот — самый простой способ без подписок и хитростей с браузером. А если нужен <a href="/rasshifrovka-video-youtube/">расшифровка видео YouTube в текст</a> — она приходит той же кнопкой.</p>"""),
        ],
        "faq": [
            ("Это бесплатно?", "Первые 2 ссылки — бесплатно, чтобы попробовать. Дальше — безлимит за 299 ₽ в месяц или 1990 ₽ в год, оформляется командой /pay в боте. А если приглашённый вами друг оформит подписку, вы получите +5 бонусных ссылок и +30 дней подписки."),
            ("Как слушать YouTube с выключенным экраном?", "Пришлите ссылку боту и включите полученное аудио в Telegram. Плеер Telegram продолжает играть в фоне и при заблокированном экране — на Android и на iPhone."),
            ("Нужно ли что-то устанавливать?", "Нет. Достаточно Telegram на телефоне или компьютере — бот работает внутри него."),
            ("Какие ссылки поддерживаются?", "Обычные видео YouTube, Shorts и плейлисты. Ссылки вида youtube.com/watch, youtu.be и m.youtube.com."),
            ("Есть ли ограничение по длине?", "Видео до ~11 часов. Длинные записи приходят несколькими частями — так их принимает Telegram."),
            ("Откуда берётся текст видео?", "Из субтитров YouTube: авторских, а если их нет — из автоматических. Если у ролика субтитров нет совсем, бот честно об этом скажет."),
        ],
    },
    {
        "lang": RU, "path": "/slushat-youtube-v-fone/", "pair": "background", "src": "site_ru_fon",
        "nav": "YouTube в фоне",
        "title": "Как слушать YouTube в фоне и с выключенным экраном без Premium",
        "description": "Три способа слушать YouTube в фоне на Android и iPhone: YouTube Premium, браузер и Telegram-бот, который присылает аудио из видео. Без подписки и сложных настроек.",
        "h1": "Как слушать YouTube в фоновом режиме и с выключенным экраном",
        "lead": "Бесплатное приложение YouTube останавливает видео, как только вы сворачиваете его или блокируете телефон. Вот рабочие способы это обойти — от официального до самого простого.",
        "sections": [
            ("Способ 1. YouTube Premium", """
<p>Официальный вариант: фоновое воспроизведение входит в подписку YouTube Premium. Работает надёжно, но стоит денег каждый месяц и доступен не во всех странах.</p>"""),
            ("Способ 2. Браузер вместо приложения", """
<p>Откройте youtube.com в мобильном браузере (Chrome, Safari, Firefox), запустите видео и заблокируйте экран, а затем продолжите воспроизведение из шторки или пункта управления. На Android иногда помогает включить «Версию для ПК».</p>
<p>Минус: способ капризный. YouTube регулярно меняет поведение плеера, и звук может обрываться через пару секунд.</p>"""),
            ("Способ 3. Telegram-бот: ссылка → аудио", """
<p>Отправьте ссылку на видео боту <b>@Listen_youtubeapp_bot</b> — он пришлёт звуковую дорожку файлом. Плеер Telegram играет в фоне и с выключенным экраном на <b>Android</b> и <b>iPhone</b>, без YouTube Premium и без браузерных трюков.</p>
<p>Бонус: аудио остаётся в чате, его можно слушать офлайн — в метро, в самолёте, за городом. А кнопка «📄 Текст видео» пришлёт расшифровку.</p>"""),
            ("Что выбрать", """
<ul>
<li><b>Смотрите и слушаете YouTube весь день, нужна музыка</b> — YouTube Premium.</li>
<li><b>Нужно разово и бесплатно</b> — попробуйте браузер.</li>
<li><b>Лекции, подкасты, аудиокниги, длинные интервью</b> — бот: офлайн, в фоне, с текстом видео.</li>
</ul>"""),
        ],
        "faq": [
            ("Почему YouTube останавливается, когда я блокирую телефон?", "Фоновое воспроизведение в приложении YouTube — функция платной подписки Premium. Бесплатная версия ставит видео на паузу при сворачивании."),
            ("Как слушать YouTube в фоновом режиме на Android?", "Самый простой путь — отправить ссылку в Telegram-бот @Listen_youtubeapp_bot и слушать полученное аудио в Telegram. Он играет в фоне и при выключенном экране."),
            ("Как слушать YouTube в фоне на iPhone?", "Так же: пришлите ссылку боту и включите аудио в Telegram. Управлять воспроизведением можно с экрана блокировки и из Пункта управления."),
            ("Можно ли слушать YouTube в фоне бесплатно, без Premium?", "Да: бот присылает аудио в Telegram, а Telegram играет его в фоне бесплатно. Первые 2 ссылки бесплатны, дальше — подписка."),
            ("Можно ли слушать без интернета?", "Да. Аудио, пришедшее в Telegram, можно сохранить и слушать офлайн."),
        ],
    },
    {
        "lang": RU, "path": "/rasshifrovka-video-youtube/", "pair": "transcript", "src": "site_ru_text",
        "nav": "Расшифровка видео",
        "title": "Расшифровка видео YouTube в текст по ссылке + конспект",
        "description": "Расшифровка видео YouTube в текст по ссылке: файл с таймкодами за несколько секунд в Telegram. Отправьте его нейросети — и получите конспект видео.",
        "h1": "Расшифровка видео YouTube в текст по ссылке",
        "lead": "Пришлите боту ссылку на видео и нажмите «📄 Текст видео» — придёт файл с расшифровкой: по абзацу на минуту с таймкодами [мм:сс], с названием, каналом и описанием ролика.",
        "sections": [
            ("Зачем нужен текст видео", """
<ul>
<li><b>Конспект за минуту.</b> Отправьте файл в ChatGPT, Claude или другой ИИ и попросите выжимку, список идей или ответы на вопросы.</li>
<li><b>Найти нужное место.</b> Поиск по тексту быстрее, чем перематывать двухчасовую лекцию.</li>
<li><b>Цитаты и заметки.</b> Скопируйте фрагмент в Notion, Obsidian или заметки.</li>
<li><b>Читать вместо смотреть.</b> Текст пробегается глазами в 3–4 раза быстрее, чем видео.</li>
</ul>"""),
            ("Как это работает", """
<p>Бот берёт субтитры YouTube: сначала авторские (русские или английские), а если их нет — автоматические субтитры на языке оригинала. Машинный перевод не используется, поэтому текст ближе к сказанному.</p>
<p>Расшифровка приходит за несколько секунд — бот не скачивает видео, чтобы её сделать. Если у ролика нет субтитров вовсе, бот сообщит об этом.</p>"""),
            ("Конспект видео YouTube с помощью нейросети", """
<p>Расшифровка — лучший вход для нейросети: ИИ читает текст целиком и не ошибается, как при «просмотре» видео по ссылке. Отправьте файл в ChatGPT, Claude, Gemini или Алису и попросите, например:</p>
<ul>
<li>«Сделай краткий конспект по пунктам»</li>
<li>«Выпиши главные идеи и таймкоды, где о них говорят»</li>
<li>«Составь вопросы для самопроверки по лекции»</li>
</ul>
<p><b>На телефоне:</b> зажмите сообщение с файлом → «Выбрать» → кнопка «Поделиться» → выберите ChatGPT, Claude или Заметки.<br><b>На компьютере:</b> просто перетащите файл в окно чата с ИИ.</p>"""),
        ],
        "faq": [
            ("Это расшифровка речи или субтитры?", "Субтитры YouTube — авторские или автоматические. Поэтому текст приходит почти мгновенно."),
            ("На каких языках работает?", "На языке оригинала видео. Авторские субтитры бот предпочитает на русском или английском."),
            ("Что делать, если у видео нет субтитров?", "Тогда текст получить не выйдет, но аудио бот всё равно пришлёт."),
            ("Можно получить текст длинного видео?", "Да, текст приходит одним файлом на всё видео, даже если аудио разбито на части."),
            ("Есть ли в расшифровке таймкоды?", "Да: текст разбит на абзацы примерно по минуте, у каждого — метка времени [мм:сс]."),
            ("Как сделать конспект видео с YouTube?", "Получите расшифровку у бота и отправьте файл нейросети (ChatGPT, Claude, Gemini, Алиса) с просьбой сделать конспект. Это быстрее и точнее, чем давать ИИ ссылку на видео."),
        ],
    },
    {
        "lang": RU, "path": "/lekcii-podkasty-audioknigi/", "pair": "listen", "src": "site_ru_lect",
        "nav": "Лекции и подкасты",
        "title": "Лекции, подкасты и аудиокниги с YouTube — слушать в Telegram",
        "description": "Слушайте лекции, подкасты, аудиокниги и аудиорассказы с YouTube в Telegram: в фоне, офлайн и целыми плейлистами. Пришлите ссылку — получите аудио.",
        "h1": "Лекции, подкасты и аудиокниги с YouTube — в формате аудио",
        "lead": "На YouTube лежат тысячи часов лекций, подкастов и аудиокниг, но слушать их через приложение неудобно. Бот превращает их в обычные аудиофайлы в Telegram.",
        "sections": [
            ("Почему удобнее слушать в Telegram", """
<ul>
<li><b>Не нужен экран.</b> Аудио играет в фоне и при заблокированном телефоне — на прогулке, за рулём, в спортзале.</li>
<li><b>Офлайн.</b> Файлы остаются в чате — слушайте в дороге без интернета.</li>
<li><b>Плейлисты целиком.</b> Курс лекций или сезон подкаста — одной ссылкой, трек за треком.</li>
<li><b>Длинные записи.</b> Аудиокниги и многочасовые стримы до ~11 часов приходят частями.</li>
<li><b>Текст рядом.</b> Расшифровка лекции — для конспекта или вопросов к ИИ.</li>
</ul>"""),
            ("Что слушают через бота", """
<p>Университетские и популярные лекции, научпоп, подкасты и интервью, аудиокниги и аудиорассказы, разборы книг, медитации и «звуки на 10 часов» для сна и работы.</p>"""),
        ],
        "faq": [
            ("Можно отправить весь плейлист?", "Да. Пришлите ссылку на плейлист — бот пришлёт все треки по очереди."),
            ("Сохраняется ли аудио?", "Да, оно остаётся в чате с ботом. Можно переслать в «Избранное» или другу."),
            ("Подойдёт для аудиокниг на несколько часов?", "Да, видео до ~11 часов поддерживаются. Длинная книга придёт несколькими частями."),
        ],
    },
    # ------------------------------------------------------------------ EN
    {
        "lang": EN, "path": "/en/", "pair": "home", "src": "site_en",
        "nav": "Home",
        "title": "YouTube to Audio Telegram Bot: Background Play + Transcript",
        "description": "Send a YouTube link to a Telegram bot and get audio that plays in the background with the screen off, plus the video's transcript.",
        "h1": "Listen to YouTube like a podcast — right in Telegram",
        "sub": "Send a link — get audio that plays in the background and with the screen off, plus the video's text.",
        "lead": "Send the bot a video or playlist link. It replies with audio that keeps playing in the background and with the screen off, plus the video's text — ready for ChatGPT or your notes.",
        "sections": [
            ("What the bot does", """
<ul class="features">
<li><b>YouTube to audio.</b> The video's soundtrack arrives as an MP3 in Telegram's player — listen without the video, on headphones or in the car.</li>
<li><b>Background play, screen off.</b> Telegram keeps playing when you switch apps or lock your phone. No YouTube Premium needed.</li>
<li><b>Video transcript.</b> The “📄 Video text” button sends the transcript as a file — ask an AI to summarize it or find a specific moment.</li>
<li><b>Long videos and playlists.</b> Videos up to ~11 hours arrive in parts; playlists arrive in full, track by track.</li>
<li><b>Yours to keep.</b> Audio stays in the chat: listen offline, forward it to a friend or to Saved Messages.</li>
</ul>"""),
            ("Who it's for", """
<p>Anyone who “watches” YouTube with their ears: <a href="/en/youtube-podcasts-lectures-offline/">lectures, podcasts and interviews</a>, audiobooks, explainers and courses. The picture doesn't matter in those videos, and keeping the screen on is awkward and drains the battery.</p>
<p>If you're looking for <a href="/en/listen-to-youtube-in-background/">how to play YouTube in the background</a> on Android or iPhone, the bot is the easiest way — no subscription, no browser tricks. Need a <a href="/en/youtube-transcript/">YouTube transcript</a>? It comes with the same button.</p>"""),
        ],
        "faq": [
            ("Is it free?", "Your first 2 links are free, so you can try it. After that there's an unlimited plan via the /pay command in the bot. If a friend you invite subscribes, you get +5 bonus links and +30 days of subscription."),
            ("How do I listen to YouTube with the screen off?", "Send the link to the bot and play the audio it returns in Telegram. Telegram's player keeps going in the background and on the lock screen, on both Android and iPhone."),
            ("Do I need to install anything?", "No. All you need is Telegram on your phone or computer — the bot runs inside it."),
            ("Which links work?", "Regular YouTube videos, Shorts and playlists: youtube.com/watch, youtu.be and m.youtube.com links."),
            ("Is there a length limit?", "Videos up to about 11 hours. Long recordings arrive in several parts — that's how Telegram accepts them."),
            ("Where does the transcript come from?", "From YouTube's subtitles: the author's own, or the automatic captions if there are none. If a video has no subtitles at all, the bot will tell you."),
        ],
    },
    {
        "lang": EN, "path": "/en/listen-to-youtube-in-background/", "pair": "background", "src": "site_en_bg",
        "nav": "Background play",
        "title": "Listen to YouTube in the Background Without Premium",
        "description": "Three ways to listen to YouTube in the background with the screen off on iPhone and Android — including free ones that work without YouTube Premium.",
        "h1": "How to listen to YouTube in the background (with or without Premium)",
        "lead": "The free YouTube app pauses the moment you switch apps or lock your phone. Here are the ways around it — from the official one to the simplest.",
        "sections": [
            ("Option 1. YouTube Premium", """
<p>The official route: background play is part of a YouTube Premium subscription. It works reliably, but it's a monthly fee and isn't available in every country.</p>"""),
            ("Option 2. A browser instead of the app", """
<p>Open youtube.com in a mobile browser (Chrome, Safari, Firefox), start the video, lock the screen, then resume playback from the notification shade or Control Center. On Android, switching to “Desktop site” sometimes helps.</p>
<p>The catch: it's fragile. YouTube changes its player often, and the sound may stop after a few seconds.</p>"""),
            ("Option 3. A Telegram bot: link → audio", """
<p>Send a video link to <b>@Listen_youtubeapp_bot</b> and it replies with the soundtrack as an audio file. Telegram's player keeps playing in the background and with the screen off on <b>Android</b> and <b>iPhone</b> — no Premium, no browser tricks.</p>
<p>Bonus: the audio stays in the chat, so you can listen offline — on the subway, on a plane, out of signal. The “📄 Video text” button sends the transcript too.</p>"""),
            ("Which one to pick", """
<ul>
<li><b>You use YouTube all day, including music</b> — YouTube Premium.</li>
<li><b>You need it once, for free</b> — try the browser.</li>
<li><b>Lectures, podcasts, audiobooks, long interviews</b> — the bot: offline, in the background, with a transcript.</li>
</ul>"""),
        ],
        "faq": [
            ("Why does YouTube stop when I lock my phone?", "Background play in the YouTube app is a YouTube Premium feature. The free app pauses when it leaves the screen."),
            ("How do I play YouTube in the background on Android?", "The simplest way is to send the link to the Telegram bot @Listen_youtubeapp_bot and play the audio in Telegram. It keeps playing in the background and with the screen off."),
            ("How do I play YouTube in the background on iPhone?", "Same way: send the link to the bot and play the audio in Telegram. You can control playback from the lock screen and Control Center."),
            ("Can you listen to YouTube in the background without Premium?", "Yes. Send the link to the bot and play the audio in Telegram — Telegram plays it in the background for free. Your first 2 links are free; after that it's a subscription."),
            ("Does audio-only use less data and battery?", "Yes. An audio file is a fraction of the size of a video stream, and nothing has to be drawn on the screen."),
            ("Can I listen offline?", "Yes. Audio you receive in Telegram can be saved and played without internet."),
        ],
    },
    {
        "lang": EN, "path": "/en/youtube-transcript/", "pair": "transcript", "src": "site_en_text",
        "nav": "Transcript",
        "title": "Get the Transcript of a YouTube Video from a Link",
        "description": "Get the full transcript of any YouTube video from its link, with timestamps, as a text file in Telegram — ready for ChatGPT, Claude or Gemini to summarize.",
        "h1": "Get the transcript of a YouTube video from a link",
        "lead": "Send the bot a video link and tap “📄 Video text”. You get a file with the full transcript — one paragraph per minute with [mm:ss] timestamps — plus the title, channel and description.",
        "sections": [
            ("Why get the transcript", """
<ul>
<li><b>Summary in a minute.</b> Drop the file into ChatGPT, Claude or another AI and ask for key points or answers.</li>
<li><b>Find the right moment.</b> Searching text beats scrubbing through a two-hour lecture.</li>
<li><b>Quotes and notes.</b> Copy passages into Notion, Obsidian or your notes app.</li>
<li><b>Read instead of watch.</b> Skimming text is 3–4× faster than watching.</li>
</ul>"""),
            ("How it works", """
<p>The bot uses YouTube's subtitles: the author's own (English or Russian) first, otherwise the automatic captions in the video's original language. No machine translation, so the text stays close to what was said.</p>
<p>The transcript arrives in seconds — the bot doesn't need to download the video. If a video has no subtitles at all, the bot will say so.</p>"""),
            ("Summarize a YouTube video with AI", """
<p>A transcript is the best input for an AI: it reads every word instead of guessing from a link. Drop the file into ChatGPT, Claude or Gemini and ask, for example:</p>
<ul>
<li>“Summarize this in bullet points”</li>
<li>“List the key ideas with the timestamps where they're discussed”</li>
<li>“Write quiz questions based on this lecture”</li>
</ul>
<p><b>On a phone:</b> press and hold the file message → Select → Share → pick ChatGPT, Claude or Notes.<br><b>On a computer:</b> drag the file into the AI chat window.</p>"""),
        ],
        "faq": [
            ("Is it speech recognition or subtitles?", "YouTube subtitles — the author's or the automatic ones. That's why the text arrives almost instantly."),
            ("Which languages are supported?", "The video's original language. For author subtitles the bot prefers English or Russian."),
            ("What if the video has no subtitles?", "Then there's no transcript, but the bot will still send the audio."),
            ("Does it work for long videos?", "Yes — the transcript comes as one file for the whole video, even when the audio is split into parts."),
            ("Does the transcript have timestamps?", "Yes: the text is split into roughly one-minute paragraphs, each starting with an [mm:ss] timestamp."),
            ("Can ChatGPT or Gemini get the transcript of a YouTube video?", "Not reliably from a link alone. Get the transcript file from the bot and give it to the AI — the summary will be based on what was actually said."),
        ],
    },
    {
        "lang": EN, "path": "/en/youtube-podcasts-lectures-offline/", "pair": "listen", "src": "site_en_lect",
        "nav": "Podcasts & lectures",
        "title": "Listen to YouTube Podcasts, Lectures & Audiobooks Offline",
        "description": "Listen to YouTube lectures, podcasts and audiobooks in Telegram — in the background, offline and as whole playlists. Send a link, get audio.",
        "h1": "YouTube podcasts, lectures and audiobooks — as audio",
        "lead": "YouTube holds thousands of hours of lectures, podcasts and audiobooks, but the app is a poor way to listen. The bot turns them into regular audio files in Telegram.",
        "sections": [
            ("Why listen in Telegram", """
<ul>
<li><b>No screen needed.</b> Audio plays in the background and on a locked phone — on a walk, while driving, at the gym.</li>
<li><b>Offline.</b> Files stay in the chat — listen on the road without internet.</li>
<li><b>Whole playlists.</b> A lecture course or a podcast season with one link, track by track.</li>
<li><b>Long recordings.</b> Audiobooks and multi-hour streams up to ~11 hours arrive in parts.</li>
<li><b>Text alongside.</b> The lecture transcript — for notes or questions to an AI.</li>
</ul>"""),
            ("What people listen to", """
<p>University and popular-science lectures, podcasts and interviews, audiobooks and stories, book summaries, meditations and “10 hours of rain” videos for sleep and focus.</p>"""),
        ],
        "faq": [
            ("Can you listen to YouTube podcasts offline?", "Yes. Send the episode link to the bot — the audio stays in your Telegram chat and plays without internet."),
            ("Can I send a whole playlist?", "Yes. Send the playlist link and the bot will deliver every track in order — handy for listening to a playlist offline."),
            ("Is the audio saved?", "Yes, it stays in your chat with the bot. Forward it to Saved Messages or a friend."),
            ("Does it work for multi-hour audiobooks?", "Yes, videos up to ~11 hours are supported. A long book arrives in several parts."),
        ],
    },
]
