"""Post 009 · Istruttoria «27 novembre» · carosello 9 slide 1080×1350.
Stile del post 005/007: fondo #0b0b0c, Crimson Text, rosso #c8211f, intestazione ISTRUTTORIA + numero, firma LUCA CRUDI / @crudiluca.
Uso: python3 build_27novembre.py  → 09_27novembre_1.png … 09_27novembre_9.png
"""
import pathlib
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent
N = "009"

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#0b0b0c;color:#f2efe9;font-family:'Inter',sans-serif;position:relative;overflow:hidden}
.top{position:absolute;top:96px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.32em}
.top span:first-child{color:#9b968e} .top span:last-child{color:#c8211f}
.c{position:absolute;top:190px;left:96px;right:96px;bottom:250px;display:flex;flex-direction:column}
.kick{font-size:26px;letter-spacing:.2em;text-transform:uppercase;color:#9b968e}
.who{font-size:30px;letter-spacing:.16em;text-transform:uppercase;color:#c8211f;font-weight:600}
.role{font-size:26px;color:#9b968e;margin-top:10px}
.year{font-family:'Crimson Text',serif;font-size:150px;line-height:1;color:#f2efe9;margin-top:24px}
h1{font-family:'Crimson Text',serif;font-weight:400;font-size:84px;line-height:1.12;margin-top:auto}
h1.m{font-size:74px}
.rule{height:3px;background:#f2efe9;margin-top:48px}
.red{font-family:'Crimson Text',serif;font-style:italic;font-size:52px;color:#c8211f;margin-top:30px;line-height:1.15}
.quote{font-family:'Crimson Text',serif;font-size:50px;line-height:1.3;margin-top:auto;margin-bottom:auto}
.quote.s{font-size:46px}
.quote i{color:#c8211f}
.body{font-size:30px;line-height:1.5;color:#9b968e;margin-top:40px}
.src{position:absolute;left:96px;right:96px;bottom:150px;font-size:21px;line-height:1.4;color:#7d7870;border-top:1px solid #2c2b2e;padding-top:18px}
.foot{position:absolute;left:96px;right:96px;bottom:84px;display:flex;justify-content:space-between;align-items:baseline}
.foot b{font-size:24px;letter-spacing:.42em;font-weight:600} .foot span{font-size:22px;color:#7d7870}
.art{margin-top:44px}
"""

ART = """
<svg class='art' width='888' height='150' viewBox='0 0 888 150' xmlns='http://www.w3.org/2000/svg'>
 <line x1='0' y1='60' x2='888' y2='60' stroke='#f2efe9' stroke-width='3'/>
 <g font-family='Inter' font-size='24' letter-spacing='4' fill='#9b968e' text-anchor='middle'>
  <line x1='120' y1='30' x2='120' y2='90' stroke='#c8211f' stroke-width='5'/><text x='120' y='135'>1895</text>
  <line x1='444' y1='30' x2='444' y2='90' stroke='#c8211f' stroke-width='5'/><text x='444' y='135'>1971</text>
  <line x1='768' y1='30' x2='768' y2='90' stroke='#c8211f' stroke-width='5'/><text x='768' y='135'>2001</text>
 </g>
</svg>"""

S_NOBEL = "NobelPrize.org, «Alfred Nobel’s will» e testo integrale del testamento"
S_MARS = "NASA Science, PIA18888 «Search for the Mars 2 Debris Field» · The Planetary Society"
S_OSIRIS = "Spaceflight Now 27/11/2001 (annuncio NASA/Hubble) · ESA, comunicato n. 15-2003 · Vidal-Madjar et al., arXiv astro-ph/0312382"
S_ALL = "NobelPrize.org · NASA Science · ESA · The Planetary Society · Spaceflight Now"

slides = [
 ("<div class='kick'>Parigi · Marte · Pegaso</div>"
  + ART +
  "<h1>Il 27 novembre abbiamo oltrepassato tre linee.</h1>"
  "<div class='rule'></div>"
  "<div class='red'>Ognuna ha lasciato qualcosa dall’altra parte.</div>", S_ALL),

 ("<div class='who'>Carmela</div><div class='role'>la giornalista · i fatti</div>"
  "<div class='year'>1895</div>"
  "<div class='quote s'>Parigi, Club svedese-norvegese. Alfred Nobel, l’uomo della dinamite, firma il suo terzo e ultimo testamento. "
  "Il patrimonio andrà in cinque parti a chi ha portato «il massimo beneficio all’umanità». "
  "Il premio per la pace lo sceglierà un comitato di cinque persone nominato dal Parlamento norvegese.</div>", S_NOBEL),

 ("<div class='who'>Carmela</div><div class='role'>la giornalista · l’ultima clausola</div>"
  "<div class='quote'>Nello stesso testamento Nobel chiede che, dopo la sua morte, <i>gli vengano recise le arterie</i>. "
  "Solo quando medici competenti avranno confermato «chiari segni di morte», il suo corpo potrà essere cremato.</div>", S_NOBEL),

 ("<div class='who'>Carmela</div><div class='role'>la giornalista · i fatti</div>"
  "<div class='year'>1971</div>"
  "<div class='quote s'>Il modulo sovietico <i>Mars 2</i> arriva su Marte durante una delle più grandi tempeste di polvere mai registrate, e si schianta. "
  "È il primo oggetto umano a toccare la superficie del pianeta. A bordo c’era un piccolo rover, legato da un cavo di 15 metri. "
  "Secondo la NASA, il relitto non è ancora stato localizzato.</div>", S_MARS),

 ("<div class='who'>Carmela</div><div class='role'>la giornalista · i fatti</div>"
  "<div class='year'>2001</div>"
  "<div class='quote s'>La NASA annuncia: Hubble ha letto, per la prima volta, l’atmosfera di un pianeta fuori dal Sistema solare. "
  "Si chiama HD 209458 b, è a 150 anni luce. Nel 2003 si scopre che sta evaporando: "
  "almeno 10.000 tonnellate di idrogeno al secondo, una coda di oltre 200.000 km. Lo chiamano <i>Osiride</i>.</div>", S_OSIRIS),

 ("<div class='who'>Teng</div><div class='role'>il finanziatore</div>"
  "<div class='quote'>Il 94% di una fortuna costruita sugli esplosivi, trasformato in un premio per chi fa del bene. "
  "Oltrepassare una linea ha sempre un costo. Nobel, almeno, ha deciso lui a chi lasciare il conto.</div>", S_NOBEL + " · Wikipedia (dato del 94%)"),

 ("<div class='who'>George</div><div class='role'>quello che fa domande</div>"
  "<div class='quote'>Si racconta che Nobel abbia letto il proprio necrologio, pubblicato per errore. Qualcuno l’ha mai trovato, quel giornale? "
  "E di cosa aveva paura un uomo che chiede di farsi tagliare le arterie dopo morto?</div>",
  S_NOBEL + " · Il necrologio prematuro è un aneddoto tramandato: qui è una domanda, non un fatto."),

 ("<div class='who'>Diana</div><div class='role'>la più responsabile</div>"
  "<div class='quote'>Restiamo sui fatti. Un testamento firmato. Un relitto mai ritrovato. Un pianeta che perde la sua aria. "
  "Il necrologio? Finché non vedo quel giornale, per me resta un racconto.</div>", S_ALL),

 ("<h1 class='m'>Cosa lasceresti tu, dall’altra parte della linea?</h1>"
  "<div class='rule'></div>"
  "<div class='red'>Scrivilo nei commenti.</div>"
  "<div class='body'><i>La linea bianca</i> · Saga della Linea Bianca, volume I</div>", S_ALL),
]

def page(inner, src, i, tot):
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
            f"<div class='top'><span>ISTRUTTORIA · {N}</span><span>{i}/{tot}</span></div>"
            f"<div class='c'>{inner}</div>"
            f"<div class='src'>Fonti: {src}</div>"
            f"<div class='foot'><b>LUCA CRUDI</b><span>@crudiluca</span></div></body></html>")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    for i, (inner, src) in enumerate(slides, 1):
        pg.set_content(page(inner, src, i, len(slides))); pg.wait_for_timeout(200)
        # controllo: il contenuto non deve sbordare sopra le fonti
        over = pg.evaluate("(()=>{const c=document.querySelector('.c').getBoundingClientRect().bottom;const s=document.querySelector('.src').getBoundingClientRect().top;return [...document.querySelectorAll('.c > *')].some(e=>e.getBoundingClientRect().bottom>s-10)})()")
        if over: print(f"ATTENZIONE: slide {i} sborda")
        pg.screenshot(path=str(OUT / f"09_27novembre_{i}.png"))
    b.close()
print("ok")
