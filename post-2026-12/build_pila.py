"""Post 012 · Istruttoria «Il navigatore italiano» (Chicago Pile-1, 2/12/1942) · carosello 7 slide 1080×1350.
Stile del post 009/010: fondo #0b0b0c, Crimson Text, rosso #c8211f, intestazione ISTRUTTORIA + numero, firma LUCA CRUDI / @crudiluca.
Uso: python3 build_pila.py → 12_pila_1.png … 12_pila_7.png
"""
import pathlib
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent
N = "012"

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

# pila schematica: strati di blocchi di grafite, una barra di controllo rossa
def pila():
    rows, out = [(6,0),(10,1),(14,2),(16,3),(16,4),(14,5),(10,6),(6,7)], []
    for n, r in rows:
        w = 34; x0 = 444 - n * w / 2; y = 20 + r * 22
        for k in range(n):
            out.append(f"<rect x='{x0 + k*w:.0f}' y='{y}' width='{w-3}' height='19' fill='#1f1e23' stroke='#4a4750' stroke-width='1'/>")
    out.append("<rect x='436' y='0' width='16' height='170' fill='#c8211f'/>")
    return "<svg class='art' width='888' height='200' viewBox='0 0 888 200' xmlns='http://www.w3.org/2000/svg'>" + "".join(out) + "</svg>"
ART = pila()

S_OSTI = "OSTI · Dipartimento dell’Energia USA, «Manhattan Project: CP-1 Goes Critical, Met Lab, December 2, 1942»"
S_ANL = "Argonne National Laboratory, «The Italian Navigator Lands»"
S_NOBEL = "NobelPrize.org, Enrico Fermi – Biographical"
S_ALL = "OSTI/DOE · Argonne National Laboratory · NobelPrize.org"

slides = [
 ("<div class='kick'>Chicago · 2 dicembre 1942 · ore 15:25</div>"
  + ART +
  "<h1 class='m'>«Il navigatore italiano è sbarcato nel Nuovo Mondo.»</h1>"
  "<div class='rule'></div>"
  "<div class='red'>Era un messaggio in codice.</div>", S_ALL),

 ("<div class='who'>Carmela</div><div class='role'>la giornalista · i fatti</div>"
  "<div class='year'>1942</div>"
  "<div class='quote s'>In un campo da squash abbandonato, sotto le tribune dello stadio dell’Università di Chicago, "
  "la squadra di Enrico Fermi accende la prima reazione nucleare a catena controllata e autosostenuta. "
  "Ore 15:25. Dura <i>28 minuti</i>. Potenza: circa mezzo watt, appena quanto basta per una piccola lampadina.</div>", S_OSTI + " · " + S_NOBEL),

 ("<div class='who'>Carmela</div><div class='role'>la giornalista · la telefonata</div>"
  "<div class='quote'>Arthur Compton chiama James Conant a Washington.<br>"
  "«Il navigatore italiano è sbarcato nel Nuovo Mondo.»<br>"
  "«Com’erano gli indigeni?»<br>"
  "«<i>Molto amichevoli.</i>»</div>", S_OSTI + " · " + S_ANL),

 ("<div class='who'>Teng</div><div class='role'>il finanziatore</div>"
  "<div class='quote'>Mezzo watt. Non illumini nemmeno una stanza. "
  "Ma chi pagava quel campo da squash non stava comprando luce. "
  "<i>Stava comprando il passo successivo.</i></div>", S_OSTI),

 ("<div class='who'>George</div><div class='role'>quello che fa domande</div>"
  "<div class='quote s'>Sulla balconata Norman Hilberry aspettava con un’ascia, pronto a tagliare una fune e far cadere una barra di controllo. "
  "Su una piattaforma, una squadra era pronta ad allagare la pila con una soluzione di cadmio. "
  "Che cosa avevano immaginato, per prepararsi così? <i>E chi si offre di stare lassù?</i></div>", S_OSTI),

 ("<div class='who'>Diana</div><div class='role'>la più responsabile</div>"
  "<div class='quote s'>Restiamo sui fatti. Fermi aveva lasciato l’Italia nel 1938, subito dopo il Nobel, soprattutto per sfuggire alla dittatura fascista. "
  "Quella pila era un passo del Progetto Manhattan, il programma della bomba atomica. "
  "La linea è stata oltrepassata in 28 minuti. <i>Non esiste una barra di controllo per tornare indietro.</i></div>", S_NOBEL + " · " + S_OSTI),

 ("<h1 class='m'>Chi decide quando una linea va oltrepassata?</h1>"
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
        pg.screenshot(path=str(OUT / f"12_pila_{i}.png"))
    b.close()
print("ok")
