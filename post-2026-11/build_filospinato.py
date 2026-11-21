import pathlib, math
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent

# Filo spinato disegnato: due trefoli intrecciati + spine a intervalli regolari
def strand(phase, y0=280, amp=7, x0=40, x1=1040):
    pts = []
    for x in range(x0, x1 + 1, 4):
        pts.append(f"{x},{y0 + amp * math.sin((x / 22.0) + phase):.1f}")
    return " ".join(pts)

barbs = ""
for i, x in enumerate(range(130, 1000, 150)):
    red = (i == 3)
    c = "#c8211f" if red else "#f2efe9"
    barbs += (f"<g stroke='{c}' stroke-width='3' stroke-linecap='round'>"
              f"<line x1='{x-26}' y1='{280-30}' x2='{x+26}' y2='{280+30}'/>"
              f"<line x1='{x+26}' y1='{280-30}' x2='{x-26}' y2='{280+30}'/>"
              f"</g><circle cx='{x}' cy='280' r='6' fill='none' stroke='{c}' stroke-width='3'/>")

SVG = f"""
<svg width='1080' height='560' viewBox='0 0 1080 560' xmlns='http://www.w3.org/2000/svg'>
 <defs>
  <linearGradient id='f' gradientUnits='userSpaceOnUse' x1='0' y1='0' x2='1080' y2='0'>
   <stop offset='0' stop-color='#f2efe9' stop-opacity='0'/>
   <stop offset='.12' stop-color='#f2efe9' stop-opacity='1'/>
   <stop offset='.88' stop-color='#f2efe9' stop-opacity='1'/>
   <stop offset='1' stop-color='#f2efe9' stop-opacity='0'/>
  </linearGradient>
  <mask id='m'><rect width='1080' height='560' fill='url(#f)'/></mask>
 </defs>
 <g mask='url(#m)'>
  <polyline points='{strand(0)}' fill='none' stroke='#f2efe9' stroke-width='3'/>
  <polyline points='{strand(math.pi)}' fill='none' stroke='#bdb8b0' stroke-width='3'/>
  {barbs}
 </g>
 <text x='540' y='150' fill='#9b968e' font-family='Inter' font-size='22' letter-spacing='4' text-anchor='middle'>U.S. PATENT N. 157.124</text>
 <text x='540' y='420' fill='#c8211f' font-family='Inter' font-size='26' letter-spacing='6' text-anchor='middle'>24 NOVEMBRE 1874</text>
 <text x='540' y='470' fill='#7d7870' font-family='Inter' font-size='22' letter-spacing='3' text-anchor='middle'>J. F. GLIDDEN · DE KALB, ILLINOIS</text>
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
<div class='top'><span>CURIOSITÀ DISTURBANTE</span><span>008</span></div>
<div class='art'>{SVG}</div>
<h1>Il 24 novembre 1874 qualcuno brevettò una linea.</h1>
<div class='rule'></div>
<div class='red'>Da allora, le linee pungono.</div>
<div class='foot'><b>LUCA CRUDI</b><span>@crudiluca</span></div>
</body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.set_content(HTML); pg.wait_for_timeout(200)
    pg.screenshot(path=str(OUT / "08_filospinato.png"))
    b.close()
print("ok")
