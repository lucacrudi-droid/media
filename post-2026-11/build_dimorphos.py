"""Post 013 · Curiosità disturbante «Dimorphos» (EXTRA di tendenza) · immagine singola 1080×1350.
Stile dei post 005/007/011: fondo #0b0b0c, Crimson Text, rosso #c8211f, firma LUCA CRUDI / @crudiluca.
Schema non in scala, disegnato a mano (nessuna immagine ESA riprodotta).
Uso: python3 build_dimorphos.py → 13_dimorphos.png
"""
import pathlib, random
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent
random.seed(2022)
stars = "".join(
    f"<circle cx='{random.randint(0,1080)}' cy='{random.randint(0,600)}' r='{random.choice([0.8,1,1.3])}' fill='#f2efe9' opacity='{random.uniform(.10,.4):.2f}'/>"
    for _ in range(110))
# massi in orbita attorno alla coppia
boulders = ""
import math
for i in range(70):
    a = random.uniform(0, 2*math.pi); r = random.uniform(250, 330)
    x = 470 + r*math.cos(a)*1.25; y = 300 + r*math.sin(a)*0.62
    if 40 < x < 1040 and 150 < y < 345 and not (600 < x < 920 and y > 330):
        boulders += f"<circle cx='{x:.0f}' cy='{y:.0f}' r='{random.choice([1.6,2,2.6])}' fill='#b9b3aa' opacity='{random.uniform(.35,.75):.2f}'/>"

SVG = f"""
<svg width='1080' height='600' viewBox='0 0 1080 600' xmlns='http://www.w3.org/2000/svg'>
 <defs>
  <radialGradient id='g' cx='38%' cy='35%' r='70%'><stop offset='0' stop-color='#8a847b'/><stop offset='1' stop-color='#2a2826'/></radialGradient>
  <radialGradient id='d' cx='40%' cy='35%' r='70%'><stop offset='0' stop-color='#9b958c'/><stop offset='1' stop-color='#33302d'/></radialGradient>
 </defs>
 {stars}
 {boulders}
 <!-- orbita di Dimorphos attorno a Didymos -->
 <ellipse cx='470' cy='300' rx='265' ry='92' fill='none' stroke='#f2efe9' stroke-opacity='.35' stroke-width='2' stroke-dasharray='3 9'/>
 <!-- Didymos -->
 <path d='M470 196 C 540 198 582 246 580 302 C 578 362 530 404 466 402 C 404 400 362 352 364 298 C 366 240 410 194 470 196 Z' fill='url(#g)'/>
 <text x='470' y='450' fill='#9b968e' font-family='Inter' font-size='19' letter-spacing='4' text-anchor='middle'>DIDYMOS · 730 m</text>
 <!-- Dimorphos con la faccia appiattita a sinistra -->
 <g transform='translate(735 300) rotate(153)'>
  <path d='M-22 -34 C 10 -42 40 -22 42 4 C 44 30 20 44 -6 42 C -18 41 -24 38 -26 36 L -26 -32 Z' fill='url(#d)'/>
  <line x1='-26' y1='-32' x2='-26' y2='36' stroke='#c8211f' stroke-width='3'/>
 </g>
 <text x='760' y='372' fill='#9b968e' font-family='Inter' font-size='19' letter-spacing='4' text-anchor='middle'>DIMORPHOS · 151 m</text>
 <!-- rotazione caotica -->
 <path d='M690 268 A 58 58 0 0 1 708 236' fill='none' stroke='#c8211f' stroke-width='2'/>
 <path d='M708 236 l -1 12 l -10 -5 z' fill='#c8211f'/>
 <!-- traiettoria di DART -->
 <line x1='1040' y1='150' x2='764' y2='283' stroke='#f2efe9' stroke-opacity='.75' stroke-width='2' stroke-dasharray='10 7'/>
 <text x='1000' y='96' fill='#f2efe9' font-family='Crimson Text' font-size='40' text-anchor='end'>26 settembre 2022</text>
 <text x='1000' y='128' fill='#9b968e' font-family='Inter' font-size='17' letter-spacing='2' text-anchor='end'>LA SONDA DART LO COLPISCE APPOSTA</text>
 <text x='96' y='96' fill='#f2efe9' font-family='Crimson Text' font-size='40'>−33 minuti</text>
 <text x='96' y='128' fill='#9b968e' font-family='Inter' font-size='17' letter-spacing='2'>L'ORBITA SI ACCORCIA PIÙ DEL PREVISTO</text>
 <text x='96' y='528' fill='#f2efe9' font-family='Crimson Text' font-size='40'>25 novembre 2026</text>
 <text x='96' y='560' fill='#c8211f' font-family='Inter' font-size='17' letter-spacing='2'>HERA: CRATERE DA STADIO, ROTAZIONE CAOTICA, CENTINAIA DI MASSI</text>
</svg>"""

HTML = f"""<html><head><meta charset='utf-8'><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#0b0b0c;color:#f2efe9;font-family:'Inter',sans-serif;position:relative}}
.top{{position:absolute;top:96px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.32em}}
.top span:first-child{{color:#9b968e}} .top span:last-child{{color:#c8211f}}
.art{{position:absolute;top:170px;left:0}}
.note{{position:absolute;top:782px;left:96px;font-size:15px;letter-spacing:.2em;color:#5f5b55}}
h1{{position:absolute;left:96px;right:96px;top:830px;font-family:'Crimson Text',serif;font-weight:400;font-size:57px;line-height:1.2}}
.rule{{position:absolute;left:96px;right:96px;top:1032px;height:3px;background:#f2efe9}}
.red{{position:absolute;left:96px;right:96px;top:1060px;font-family:'Crimson Text',serif;font-style:italic;font-size:50px;color:#c8211f}}
.foot{{position:absolute;left:96px;right:96px;bottom:84px;display:flex;justify-content:space-between;align-items:baseline}}
.foot b{{font-size:24px;letter-spacing:.42em;font-weight:600}} .foot span{{font-size:22px;color:#7d7870}}
</style></head><body>
<div class='top'><span>CURIOSITÀ DISTURBANTE</span><span>013</span></div>
<div class='art'>{SVG}</div>
<div class='note'>SCHEMA NON IN SCALA · DATI ESA</div>
<h1>Abbiamo colpito un asteroide per imparare a difenderci.</h1>
<div class='rule'></div>
<div class='red'>Ora gira impazzito.</div>
<div class='foot'><b>LUCA CRUDI</b><span>@crudiluca</span></div>
</body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.set_content(HTML); pg.wait_for_timeout(250)
    pg.screenshot(path=str(OUT / "13_dimorphos.png"))
    b.close()
print("ok")
