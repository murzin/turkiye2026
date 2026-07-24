from pathlib import Path
from html import escape

root = Path(__file__).parent
cities = sorted(p.name for p in root.iterdir() if p.is_dir() and p.name != "assets" and not p.name.startswith("."))

def nav(active=None, prefix=""):
    items = [f'<a href="{prefix}index.html"{" aria-current=\"page\"" if active == "home" else ""}>Главная</a>']
    for city in cities:
        current = ' aria-current="page"' if active == city else ''
        items.append(f'<a href="{prefix}{city}/index.html"{current}>{escape(city)}</a>')
    return '<nav class="site-nav" aria-label="Города">' + ''.join(items) + '</nav>'

def header(active=None, prefix=""):
    return f'''<header class="site-header"><div class="kilim-band"></div><div class="header-inner"><a class="brand" href="{prefix}index.html"><span class="brand-mark">☾</span> Турция</a>{nav(active, prefix)}</div></header>'''

def footer():
    return '<footer class="site-footer"><div class="footer-inner">Турция · Март 2026 · Фотоальбом путешествия</div></footer>'

turkiye_map = '''<figure class="turkiye-map" aria-labelledby="map-caption"><svg viewBox="0 0 620 350" role="img" aria-labelledby="map-title map-description"><title id="map-title">Карта маршрута по Турции</title><desc id="map-description">Схематичная карта Турции. Каждая отмеченная точка является ссылкой на фотоальбом места.</desc><path class="map-land" d="M18 146 L29 132 L25 119 L39 108 L53 110 L65 101 L82 108 L95 101 L113 94 L143 91 L171 97 L204 91 L235 96 L271 88 L304 89 L335 83 L369 90 L407 80 L441 84 L473 75 L509 82 L541 80 L570 96 L592 101 L607 119 L603 138 L590 153 L594 169 L611 185 L605 204 L591 212 L578 230 L559 229 L545 240 L532 232 L517 244 L490 246 L471 262 L449 260 L431 277 L404 272 L387 284 L367 277 L348 290 L327 279 L306 287 L287 271 L264 281 L242 275 L216 280 L197 264 L178 275 L157 264 L138 271 L118 256 L105 261 L91 246 L76 247 L63 232 L50 231 L45 218 L32 212 L24 195 L28 182 L19 168 L26 155 Z"/><path class="map-coast" d="M18 146 L29 132 L25 119 L39 108 L53 110 L65 101 L82 108 L95 101 L113 94 L143 91 L171 97 L204 91 L235 96 L271 88 L304 89 L335 83 L369 90 L407 80 L441 84 L473 75 L509 82 L541 80 L570 96 L592 101 L607 119"/><g class="map-route" aria-hidden="true"><path d="M36 108 L64 153 L69 214 L164 228 L284 104 L405 197 L407 240 L410 236 L414 256 L428 241"/></g><g class="map-locations"><a href="Troya/index.html" class="map-place"><title>Troya</title><circle cx="36" cy="108" r="5"/><text x="47" y="101">Troya</text></a><a href="Pergam/index.html" class="map-place"><title>Pergam</title><circle cx="64" cy="153" r="5"/><text x="75" y="148">Pergam</text></a><a href="Efes/index.html" class="map-place"><title>Efes</title><circle cx="69" cy="214" r="5"/><text x="80" y="229">Efes</text></a><a href="Sagalassos/index.html" class="map-place"><title>Sagalassos</title><circle cx="164" cy="228" r="5"/><text x="175" y="221">Sagalassos</text></a><a href="Hatussa/index.html" class="map-place"><title>Hatussa</title><circle cx="284" cy="104" r="5"/><text x="295" y="98">Hatussa</text></a><a href="Nemrut/index.html" class="map-place"><title>Nemrut</title><circle cx="405" cy="197" r="5"/><text x="416" y="185">Nemrut</text></a><a href="Urfa/index.html" class="map-place"><title>Urfa</title><circle cx="407" cy="240" r="5"/><text x="352" y="239">Urfa</text></a><a href="GedekliTepe/index.html" class="map-place"><title>Gedekli Tepe</title><circle cx="410" cy="236" r="5"/><text x="421" y="218">Gedekli Tepe</text></a><a href="Harran/index.html" class="map-place"><title>Harran</title><circle cx="414" cy="256" r="5"/><text x="357" y="276">Harran</text></a><a href="Sogmatar/index.html" class="map-place"><title>Sogmatar</title><circle cx="428" cy="241" r="5"/><text x="440" y="257">Sogmatar</text></a></g></svg><figcaption id="map-caption">Маршрут по Турции · выберите место</figcaption></figure>'''

turkiye_map = '''<figure class="turkiye-map" aria-labelledby="map-caption"><div class="map-image-wrap"><img class="map-contour" src="assets/turkiye-contur.png" alt="Контурная карта Турции"><a href="Troya/index.html" class="map-place map-place--top" style="--x: 6%; --y: 24%;"><span class="map-dot"></span><span>Troya</span></a><a href="Pergam/index.html" class="map-place map-place--top" style="--x: 11%; --y: 43%;"><span class="map-dot"></span><span>Pergam</span></a><a href="Efes/index.html" class="map-place map-place--bottom" style="--x: 12%; --y: 60%;"><span class="map-dot"></span><span>Efes</span></a><a href="Sagalassos/index.html" class="map-place map-place--top" style="--x: 27%; --y: 64%;"><span class="map-dot"></span><span>Sagalassos</span></a><a href="Hatussa/index.html" class="map-place map-place--top" style="--x: 46%; --y: 36%;"><span class="map-dot"></span><span>Hatussa</span></a><a href="Nemrut/index.html" class="map-place map-place--top" style="--x: 66%; --y: 60%;"><span class="map-dot"></span><span>Nemrut</span></a><a href="Urfa/index.html" class="map-place map-place--left" style="--x: 66.5%; --y: 70%;"><span class="map-dot"></span><span>Urfa</span></a><a href="GedekliTepe/index.html" class="map-place map-place--top" style="--x: 67%; --y: 68%;"><span class="map-dot"></span><span>Gedekli Tepe</span></a><a href="Harran/index.html" class="map-place map-place--bottom-left" style="--x: 68%; --y: 73%;"><span class="map-dot"></span><span>Harran</span></a><a href="Sogmatar/index.html" class="map-place map-place--right" style="--x: 70%; --y: 70%;"><span class="map-dot"></span><span>Sogmatar</span></a></div><figcaption id="map-caption">Маршрут по Турции · выберите место</figcaption></figure>'''

def photo_files(city):
    return sorted(Path(city).glob("*.jpg"))

cards = []
for city in cities:
    photos = photo_files(city)
    if not photos:
        continue
    image = photos[0].as_posix()
    cards.append(f'''<a class="city-card" href="{escape(city)}/index.html"><img src="{escape(image)}" alt="{escape(city)}" loading="lazy"><div class="city-card-text"><h2>{escape(city)}</h2><p>{len(photos)} фотографий</p></div></a>''')

root_html = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Турция — Март 2026</title><link rel="stylesheet" href="assets/style.css"></head>
<body>{header("home")}<main class="page-main"><section class="home-hero"><div class="hero"><p class="eyebrow">Дорожный дневник</p><h1>Турция</h1><p class="subtitle">Март 2026</p><div class="ornament" aria-hidden="true"><span>✦</span></div></div>{turkiye_map}</section><section aria-labelledby="cities-title"><div class="section-heading"><h2 id="cities-title">Города и места</h2><p>{len(cities)} остановок</p></div><div class="city-grid">{''.join(cards)}</div></section></main>{footer()}</body></html>'''
(root / "index.html").write_text(root_html, encoding="utf-8")

for city in cities:
    files = photo_files(city)
    photo_cards = []
    for index, file in enumerate(files, 1):
        src = file.name
        caption = f"{city} · фото {index}"
        photo_cards.append(f'''<button class="photo-card" type="button" data-full="{escape(src)}" data-caption="{escape(caption)}"><img src="{escape(src)}" alt="{escape(caption)}" loading="lazy"></button>''')
    page = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(city)} — Турция, Март 2026</title><link rel="stylesheet" href="../assets/style.css"></head>
<body>{header(city, "../")}<main class="page-main"><section class="album-title"><div><p class="eyebrow">Турция · Март 2026</p><h1>{escape(city)}</h1><p class="photo-count">{len(files)} фотографий</p></div><a class="back-link" href="../index.html">← Все города</a></section><section class="photo-grid" aria-label="Фотографии {escape(city)}">{''.join(photo_cards)}</section></main><dialog class="lightbox" aria-label="Просмотр фотографии"><div class="lightbox-frame"><img class="lightbox-image" src="" alt=""><button class="lightbox-close" type="button" aria-label="Закрыть">×</button><button class="lightbox-arrow lightbox-prev" type="button" aria-label="Предыдущее фото">‹</button><button class="lightbox-arrow lightbox-next" type="button" aria-label="Следующее фото">›</button></div><div class="lightbox-caption"><span data-lightbox-caption></span><span data-lightbox-counter></span></div></dialog>{footer()}<script src="../assets/album.js"></script></body></html>'''
    (root / city / "index.html").write_text(page, encoding="utf-8")
