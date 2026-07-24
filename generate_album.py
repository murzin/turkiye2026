from pathlib import Path
from html import escape

root = Path(__file__).parent
cities = sorted(p.name for p in root.iterdir() if p.is_dir() and p.name != "assets")

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
<body>{header("home")}<main class="page-main"><section class="hero"><p class="eyebrow">Дорожный дневник</p><h1>Турция</h1><p class="subtitle">Март 2026</p><div class="ornament" aria-hidden="true"><span>✦</span></div></section><section aria-labelledby="cities-title"><div class="section-heading"><h2 id="cities-title">Города и места</h2><p>{len(cities)} остановок</p></div><div class="city-grid">{''.join(cards)}</div></section></main>{footer()}</body></html>'''
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
