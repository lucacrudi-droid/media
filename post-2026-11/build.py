import html, pathlib
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#0d0d0f;color:#f2efe9;font-family:'Inter',sans-serif;}
.s{position:relative;width:1080px;height:1350px;padding:110px 100px;display:flex;flex-direction:column}
.line{position:absolute;left:100px;right:100px;top:70px;height:3px;background:#f2efe9;opacity:.9}
.kick{font-size:26px;letter-spacing:.18em;text-transform:uppercase;color:#9b968e;margin-top:20px}
.who{font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:#c8211f;font-weight:600;margin-top:20px}
.role{font-size:26px;color:#9b968e;margin-top:8px}
h1{font-family:'Crimson Text',serif;font-weight:600;font-size:96px;line-height:1.05;margin-top:auto}
h1.m{font-size:78px}
.red{font-family:'Crimson Text',serif;font-style:italic;font-size:62px;color:#c8211f;margin-top:34px;line-height:1.1}
.body{font-size:34px;line-height:1.5;color:#d9d5ce;margin-top:56px}
.quote{font-family:'Crimson Text',serif;font-size:58px;line-height:1.25;margin-top:auto;margin-bottom:auto}
.foot{margin-top:auto;padding-top:40px;display:flex;justify-content:space-between;font-size:22px;color:#7d7870;border-top:1px solid #2c2b2e}
.foot b{color:#f2efe9;font-weight:600}
.n{position:absolute;right:100px;top:100px;font-size:24px;color:#7d7870}
"""

def page(inner, n=None):
    num = f'<div class="n">{n}</div>' if n else ''
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='s'><div class='line'></div>{num}{inner}</div></body></html>"

def foot(src):
    return f"<div class='foot'><span>Fonti: {src}</span><span><b>@crudiluca</b> · La linea bianca</span></div>"

slides = {}

# 1 ESSEX
slides["01_essex"] = page(
    "<div class='kick'>20 novembre 1820 · Oceano Pacifico</div>"
    "<h1>Avevano paura dei cannibali.</h1>"
    "<div class='red'>Per questo lo diventarono.</div>"
    "<div class='body'>Un capodoglio affonda la baleniera <i>Essex</i>. Le isole più vicine, si dice, sono abitate da cannibali. "
    "I 20 uomini scelgono il continente sudamericano: circa 2.000 miglia di mare aperto. "
    "Sopravvivono in 8. Per restare vivi, mangiano i compagni morti.</div>"
    + foot("Smithsonian Magazine · Mass Moments"))

# 2 EGITTO
slides["02_egitto"] = page(
    "<div class='kick'>Egitto · annuncio del 18 novembre 2026</div>"
    "<h1>Li seppellirono con una lingua d’oro.</h1>"
    "<div class='red'>Per parlare ancora, dopo.</div>"
    "<div class='body'>Tell Abu Bellou, delta del Nilo. In un solo cortile funerario, centinaia di sepolture e sarcofagi in pietra, "
    "per lo più del III–II secolo a.C. Tra gli oggetti, lingue d’oro: secondo l’interpretazione più diffusa, "
    "servivano al defunto per parlare nell’aldilà.</div>"
    + foot("Ministero Antichità d’Egitto · HeritageDaily"))

# 3 BOG BODY carousel
SRC3 = "ITV News · Arkeonews"
slides["03_istruttoria_1"] = page(
    "<div class='kick'>Istruttoria · Belfast, 16 novembre 2026</div>"
    "<h1>Un’inchiesta per una morte di 2.000 anni fa.</h1>"
    "<div class='red'>Il colpevole non ha nome.</div>"
    + foot(SRC3), "1/6")
slides["03_istruttoria_2"] = page(
    "<div class='who'>Carmela</div><div class='role'>la giornalista · i fatti</div>"
    "<div class='quote'>Torbiera vicino a Bellaghy, Irlanda del Nord, 2023. Una ragazza tra i 15 e i 22 anni, Età del Ferro. "
    "Decapitata da dietro, con una lama. La testa non è mai stata trovata. Il 16 novembre un coroner ha esaminato il caso in un’udienza simulata.</div>"
    + foot(SRC3), "2/6")
slides["03_istruttoria_3"] = page(
    "<div class='who'>Teng</div><div class='role'>il finanziatore</div>"
    "<div class='quote'>Micro-TAC, scansioni 3D, due università, un museo, un coroner. Tutto per una ragazza senza nome. "
    "Quanto vale la verità su una morte che nessuno potrà più punire?</div>"
    + foot(SRC3), "3/6")
slides["03_istruttoria_4"] = page(
    "<div class='who'>George</div><div class='role'>quello che fa domande</div>"
    "<div class='quote'>«Forse un rituale», dicono. Ma chi lo decide che era un rituale? "
    "E un sacrificio è qualcosa di diverso da un omicidio, se chi uccide è convinto di fare il bene?</div>"
    + foot(SRC3), "4/6")
slides["03_istruttoria_5"] = page(
    "<div class='who'>Diana</div><div class='role'>la più responsabile</div>"
    "<div class='quote'>Sappiamo come è morta. Non sappiamo perché. Il rituale è un’ipotesi, non una prova. "
    "E il museo racconterà la sua storia senza esporre i suoi resti.</div>"
    + foot(SRC3), "5/6")
slides["03_istruttoria_6"] = page(
    "<h1 class='m'>Dove passa la linea tra sacrificio e omicidio?</h1>"
    "<div class='red'>Scrivilo nei commenti.</div>"
    "<div class='body'><i>La linea bianca</i> · Saga della Linea Bianca, volume I</div>"
    + foot(SRC3), "6/6")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=1)
    for name, h in slides.items():
        pg.set_content(h); pg.wait_for_timeout(150)
        pg.screenshot(path=str(OUT/f"{name}.png"))
    b.close()
print("ok")
