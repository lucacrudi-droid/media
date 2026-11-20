import pathlib, random
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent
random.seed(1922)
dust = "".join(
    f"<circle cx='{random.randint(0,1080)}' cy='{random.randint(0,700)}' r='{random.choice([0.8,1,1.3])}' fill='#f2efe9' opacity='{random.uniform(.15,.5):.2f}'/>"
    for _ in range(90))

SVG = f"""
<svg width='1080' height='560' viewBox='0 0 1080 560' xmlns='http://www.w3.org/2000/svg'>
 <defs>
  <radialGradient id='g' cx='50%' cy='50%' r='50%'>
   <stop offset='0' stop-color='#ffd98a' stop-opacity='1'/>
   <stop offset='.35' stop-color='#e0a040' stop-opacity='.55'/>
   <stop offset='1' stop-color='#e0a040' stop-opacity='0'/>
  </radialGradient>
 </defs>
 {dust}
 <!-- porta sigillata -->
 <rect x='370' y='60' width='340' height='470' fill='#141416' stroke='#5a5650' stroke-width='2'/>
 <rect x='390' y='80' width='300' height='450' fill='none' stroke='#2c2b2e' stroke-width='1'/>
 <!-- sigilli -->
 {''.join(f"<ellipse cx='{x}' cy='{y}' rx='22' ry='14' fill='none' stroke='#6e6a63' stroke-width='1.5'/>" for x,y in [(450,160),(540,150),(630,160),(450,440),(540,450),(630,440)])}
 <!-- breccia illuminata -->
 <circle cx='540' cy='300' r='120' fill='url(#g)'/>
 <polygon points='522,282 560,278 566,306 548,322 518,314' fill='#ffe7b0'/>
</svg>"""

HTML = f"""<html><head><meta charset='utf-8'><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#0b0b0c;color:#f2efe9;font-family:'Inter',sans-serif;position:relative}}
.top{{position:absolute;top:96px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.32em}}
.top span:first-child{{color:#9b968e}} .top span:last-child{{color:#c8211f}}
.art{{position:absolute;top:150px;left:0}}
h1{{position:absolute;left:96px;right:96px;top:740px;font-family:'Crimson Text',serif;font-weight:400;font-size:68px;line-height:1.22}}
.rule{{position:absolute;left:96px;right:96px;top:1000px;height:3px;background:#f2efe9}}
.red{{position:absolute;left:96px;right:96px;top:1030px;font-family:'Crimson Text',serif;font-style:italic;font-size:50px;color:#c8211f}}
.foot{{position:absolute;left:96px;right:96px;bottom:84px;display:flex;justify-content:space-between;align-items:baseline}}
.foot b{{font-size:24px;letter-spacing:.42em;font-weight:600}} .foot span{{font-size:22px;color:#7d7870}}
</style></head><body>
<div class='top'><span>CURIOSITÀ DISTURBANTE</span><span>006</span></div>
<div class='art'>{SVG}</div>
<h1>Il 26 novembre 1922 Carter guardò oltre la porta sigillata.</h1>
<div class='rule'></div>
<div class='red'>Il re portava un pugnale caduto dal cielo.</div>
<div class='foot'><b>LUCA CRUDI</b><span>@crudiluca</span></div>
</body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.set_content(HTML); pg.wait_for_timeout(200)
    pg.screenshot(path=str(OUT / "06_carter.png"))
    b.close()
print("ok")
