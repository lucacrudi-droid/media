"""Post 006 · slide fotografiche (Harry Burton, 1922, pubblico dominio).
Uso: python3 build_carter_foto.py  (scarica le foto da upload.wikimedia.org)"""
import pathlib, base64, urllib.request
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent
SLIDES = [
    {"file": "06_carter_2.png", "n": "2/3",
     "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Howard_Carter%2C_Lord_Carnarvon_and_Lady_Evelyn_Herbert_at_Tutankhamen%27s_tomb.jpg",
     "title": "Novembre 1922. All’ingresso della tomba appena scoperta.",
     "cap": "Lord Carnarvon, la figlia Lady Evelyn Herbert e Howard Carter all’ingresso della tomba KV62, Valle dei Re.",
     "credit": "Foto Harry Burton, 1922 · Griffith Institute, Oxford · pubblico dominio (Wikimedia Commons)"},
    {"file": "06_carter_3.png", "n": "3/3",
     "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Carter_tuttumb.jpg",
     "title": "Tre anni dopo, Carter arriva al sarcofago più interno.",
     "cap": "Tra le bende della mummia lo aspetta il pugnale di ferro.",
     "credit": "Foto Harry Burton, stagione 1925–26 (datazione: Metropolitan Museum of Art, «Cleaning the Innermost Coffin») · pubblico dominio (Wikimedia Commons)"},
]

CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#0b0b0c;color:#f2efe9;font-family:'Inter',sans-serif;position:relative}
.top{position:absolute;top:96px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.32em}
.top span:first-child{color:#9b968e} .top span:last-child{color:#c8211f}
.ph{position:absolute;top:170px;left:96px;right:96px;height:640px;display:flex;align-items:center;justify-content:center;background:#141416;border:1px solid #2c2b2e}
.ph img{max-width:100%;max-height:100%;filter:grayscale(1) contrast(1.05)}
h1{position:absolute;left:96px;right:96px;top:850px;font-family:'Crimson Text',serif;font-weight:400;font-size:56px;line-height:1.2}
.cap{position:absolute;left:96px;right:96px;top:1010px;font-family:'Crimson Text',serif;font-style:italic;font-size:34px;line-height:1.3;color:#c8211f}
.cr{position:absolute;left:96px;right:96px;top:1150px;font-size:18px;color:#7d7870;letter-spacing:.02em}
.foot{position:absolute;left:96px;right:96px;bottom:84px;display:flex;justify-content:space-between;align-items:baseline}
.foot b{font-size:24px;letter-spacing:.42em;font-weight:600} .foot span{font-size:22px;color:#7d7870}"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    for s in SLIDES:
        cache = OUT / ("_cache_" + s["file"].replace(".png", ".jpg"))
        if not cache.exists():
            req = urllib.request.Request(s["url"], headers={"User-Agent": "crudiluca-archive/1.0"})
            cache.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        data = base64.b64encode(cache.read_bytes()).decode()
        html = f"""<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>
<div class='top'><span>CURIOSITÀ DISTURBANTE · 006</span><span>{s['n']}</span></div>
<div class='ph'><img src='data:image/jpeg;base64,{data}'></div>
<h1>{s['title']}</h1><div class='cap'>{s['cap']}</div><div class='cr'>{s['credit']}</div>
<div class='foot'><b>LUCA CRUDI</b><span>@crudiluca</span></div></body></html>"""
        pg.set_content(html); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT / s["file"]))
    b.close()
print("ok")
