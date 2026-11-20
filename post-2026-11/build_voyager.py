import pathlib, random
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent
random.seed(1977)
stars = "".join(
    f"<circle cx='{random.randint(0,1080)}' cy='{random.randint(0,560)}' r='{random.choice([0.8,1,1.3])}' fill='#f2efe9' opacity='{random.uniform(.15,.55):.2f}'/>"
    for _ in range(110))

SVG = f"""
<svg width='1080' height='560' viewBox='0 0 1080 560' xmlns='http://www.w3.org/2000/svg'>
 <defs>
  <radialGradient id='e' cx='50%' cy='50%' r='50%'>
   <stop offset='0' stop-color='#9cc3ff'/><stop offset='1' stop-color='#9cc3ff' stop-opacity='0'/>
  </radialGradient>
  <linearGradient id='l' gradientUnits='userSpaceOnUse' x1='150' y1='0' x2='925' y2='0'>
   <stop offset='0' stop-color='#f2efe9' stop-opacity='.9'/><stop offset='1' stop-color='#f2efe9' stop-opacity='.15'/>
  </linearGradient>
 </defs>
 {stars}
 <circle cx='130' cy='280' r='40' fill='url(#e)'/>
 <circle cx='130' cy='280' r='9' fill='#cfe0ff'/>
 <line x1='150' y1='280' x2='925' y2='280' stroke='url(#l)' stroke-width='2' stroke-dasharray='2 10'/>
 <circle cx='940' cy='280' r='4' fill='#f2efe9'/>
 <circle cx='940' cy='280' r='16' fill='none' stroke='#f2efe9' stroke-opacity='.35'/>
 <text x='130' y='350' fill='#9b968e' font-family='Inter' font-size='22' letter-spacing='4' text-anchor='middle'>TERRA</text>
 <text x='940' y='350' fill='#9b968e' font-family='Inter' font-size='22' letter-spacing='4' text-anchor='middle'>VOYAGER 1</text>
 <text x='540' y='250' fill='#c8211f' font-family='Inter' font-size='26' letter-spacing='6' text-anchor='middle'>24 ORE</text>
 <text x='540' y='320' fill='#7d7870' font-family='Inter' font-size='22' letter-spacing='3' text-anchor='middle'>25,9 MILIARDI DI KM</text>
</svg>"""

HTML = f"""<html><head><meta charset='utf-8'><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#0b0b0c;color:#f2efe9;font-family:'Inter',sans-serif;position:relative}}
.top{{position:absolute;top:96px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.32em}}
.top span:first-child{{color:#9b968e}} .top span:last-child{{color:#c8211f}}
.art{{position:absolute;top:160px;left:0}}
h1{{position:absolute;left:96px;right:96px;top:760px;font-family:'Crimson Text',serif;font-weight:400;font-size:72px;line-height:1.2}}
.rule{{position:absolute;left:96px;right:96px;top:1000px;height:3px;background:#f2efe9}}
.red{{position:absolute;left:96px;right:96px;top:1030px;font-family:'Crimson Text',serif;font-style:italic;font-size:48px;color:#c8211f}}
.foot{{position:absolute;left:96px;right:96px;bottom:84px;display:flex;justify-content:space-between;align-items:baseline}}
.foot b{{font-size:24px;letter-spacing:.42em;font-weight:600}} .foot span{{font-size:22px;color:#7d7870}}
</style></head><body>
<div class='top'><span>CURIOSITÀ DISTURBANTE</span><span>007</span></div>
<div class='art'>{SVG}</div>
<h1>Ogni parola che ci manda arriva da ieri.</h1>
<div class='rule'></div>
<div class='red'>Nessun oggetto umano era arrivato così lontano.</div>
<div class='foot'><b>LUCA CRUDI</b><span>@crudiluca</span></div>
</body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.set_content(HTML); pg.wait_for_timeout(200)
    pg.screenshot(path=str(OUT / "07_voyager.png"))
    b.close()
print("ok")
