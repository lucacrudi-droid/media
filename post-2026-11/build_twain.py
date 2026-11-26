"""Post 011 · Curiosità disturbante «Mark Twain e la cometa di Halley» · immagine singola 1080×1350.
Stile dei post 005/007: fondo #0b0b0c, Crimson Text, rosso #c8211f, firma LUCA CRUDI / @crudiluca.
Uso: python3 build_twain.py → 11_twain.png
"""
import pathlib, random
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent
random.seed(1835)
stars = "".join(
    f"<circle cx='{random.randint(0,1080)}' cy='{random.randint(0,600)}' r='{random.choice([0.8,1,1.3])}' fill='#f2efe9' opacity='{random.uniform(.12,.5):.2f}'/>"
    for _ in range(120))

# orbita schematica: ellisse molto allungata, Sole vicino al fuoco di sinistra
SVG = f"""
<svg width='1080' height='600' viewBox='0 0 1080 600' xmlns='http://www.w3.org/2000/svg'>
 <defs>
  <radialGradient id='s' cx='50%' cy='50%' r='50%'><stop offset='0' stop-color='#f2d9a0'/><stop offset='1' stop-color='#f2d9a0' stop-opacity='0'/></radialGradient>
  <linearGradient id='tailL' x1='1' y1='0' x2='0' y2='0'><stop offset='0' stop-color='#f2efe9' stop-opacity='.85'/><stop offset='1' stop-color='#f2efe9' stop-opacity='0'/></linearGradient>
 </defs>
 {stars}
 <ellipse cx='640' cy='300' rx='360' ry='105' fill='none' stroke='#f2efe9' stroke-opacity='.35' stroke-width='2' stroke-dasharray='3 9'/>
 <circle cx='330' cy='300' r='46' fill='url(#s)'/><circle cx='330' cy='300' r='12' fill='#f2d9a0'/>
 <text x='330' y='372' fill='#9b968e' font-family='Inter' font-size='20' letter-spacing='4' text-anchor='middle'>SOLE</text>
 <!-- cometa al perielio; la coda punta lontano dal Sole (verso sinistra) -->
 <path d='M274 300 Q 230 294 150 278 L 150 322 Q 230 306 274 300 Z' fill='url(#tailL)'/>
 <circle cx='280' cy='300' r='7' fill='#f2efe9'/>
 <line x1='280' y1='180' x2='280' y2='288' stroke='#c8211f' stroke-width='2'/>
 <text x='96' y='118' fill='#f2efe9' font-family='Crimson Text' font-size='46'>1835</text>
 <text x='96' y='152' fill='#9b968e' font-family='Inter' font-size='19' letter-spacing='2'>NASCE DUE SETTIMANE DOPO IL PERIELIO</text>
 <line x1='280' y1='312' x2='280' y2='420' stroke='#c8211f' stroke-width='2'/>
 <text x='96' y='472' fill='#f2efe9' font-family='Crimson Text' font-size='46'>1910</text>
 <text x='96' y='506' fill='#c8211f' font-family='Inter' font-size='19' letter-spacing='2'>MUORE IL GIORNO DOPO IL PERIELIO</text>
 <circle cx='1000' cy='300' r='5' fill='none' stroke='#f2efe9' stroke-opacity='.6' stroke-width='2'/>
 <text x='984' y='256' fill='#9b968e' font-family='Inter' font-size='20' letter-spacing='4' text-anchor='end'>2061</text>
 <text x='984' y='352' fill='#7d7870' font-family='Inter' font-size='17' letter-spacing='2' text-anchor='end'>PROSSIMO RITORNO</text>
</svg>"""

HTML = f"""<html><head><meta charset='utf-8'><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#0b0b0c;color:#f2efe9;font-family:'Inter',sans-serif;position:relative}}
.top{{position:absolute;top:96px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.32em}}
.top span:first-child{{color:#9b968e}} .top span:last-child{{color:#c8211f}}
.art{{position:absolute;top:170px;left:0}}
h1{{position:absolute;left:96px;right:96px;top:820px;font-family:'Crimson Text',serif;font-weight:400;font-size:57px;line-height:1.2}}
.rule{{position:absolute;left:96px;right:96px;top:1032px;height:3px;background:#f2efe9}}
.red{{position:absolute;left:96px;right:96px;top:1060px;font-family:'Crimson Text',serif;font-style:italic;font-size:50px;color:#c8211f}}
.foot{{position:absolute;left:96px;right:96px;bottom:84px;display:flex;justify-content:space-between;align-items:baseline}}
.foot b{{font-size:24px;letter-spacing:.42em;font-weight:600}} .foot span{{font-size:22px;color:#7d7870}}
</style></head><body>
<div class='top'><span>CURIOSITÀ DISTURBANTE</span><span>011</span></div>
<div class='art'>{SVG}</div>
<h1>Mark Twain nacque con la cometa. Disse che se ne sarebbe andato con lei.</h1>
<div class='rule'></div>
<div class='red'>Morì il giorno dopo il suo ritorno.</div>
<div class='foot'><b>LUCA CRUDI</b><span>@crudiluca</span></div>
</body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.set_content(HTML); pg.wait_for_timeout(250)
    pg.screenshot(path=str(OUT / "11_twain.png"))
    b.close()
print("ok")
