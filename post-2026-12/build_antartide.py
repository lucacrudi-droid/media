"""Post 010 · Istruttoria «1° dicembre: Antartide» · carosello 8 slide 1080×1350.
Stile del post 005/009: fondo #0b0b0c, Crimson Text, rosso #c8211f, intestazione ISTRUTTORIA + numero, firma LUCA CRUDI / @crudiluca.
Mappa: proiezione stereografica polare sud disegnata a mano, dati Natural Earth (pubblico dominio).
Uso: python3 build_antartide.py <cartella_dati_natural_earth>
     (servono ne_50m_land.geojson e ne_50m_antarctic_ice_shelves_polys.geojson)
     → mappa_antartide.png, 10_antartide_1.png … 10_antartide_8.png
"""
import json, math, sys, pathlib, base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from playwright.sync_api import sync_playwright

NE = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(__file__).parent
N = "010"

# ---------------------------------------------------------------- mappa
for f in font_manager.findSystemFonts():
    if ("Inter" in f and "Display" not in f) or "CrimsonText" in f:
        font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = "Inter"
BG, LAND, SHELF, EDGE, TXT, MUTED, RED = "#0b0b0c", "#1f1e23", "#17161a", "#4a4750", "#f2efe9", "#9b968e", "#c8211f"

def proj(lon, lat):
    """Stereografica polare sud, 0° in alto, 90°E a destra."""
    r = math.tan(math.radians((90 + lat) / 2))
    return r * math.sin(math.radians(lon)), r * math.cos(math.radians(lon))

def rings(geom):
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    for p in polys:
        yield p[0]

def draw(ax, path, face, edge, lw):
    for f in json.load(open(path))["features"]:
        for ring in rings(f["geometry"]):
            if max(pt[1] for pt in ring) > -50:      # solo ciò che sta a sud del 50° S
                continue
            xs, ys = zip(*(proj(lon, lat) for lon, lat in ring))
            ax.fill(xs, ys, facecolor=face, edgecolor="none", zorder=2)
            # contorno senza la «cucitura» lungo l'antimeridiano e attorno al polo
            for (lo1, la1), (lo2, la2) in zip(ring, ring[1:]):
                if la1 < -89 or la2 < -89 or (abs(lo1) > 179.9 and abs(lo2) > 179.9):
                    continue
                (x1, y1), (x2, y2) = proj(lo1, la1), proj(lo2, la2)
                ax.plot([x1, x2], [y1, y2], color=edge, lw=lw, zorder=2.5)

R60 = math.tan(math.radians(15))
EXT = 0.43
fig = plt.figure(figsize=(8.88, 8.88), dpi=100, facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(BG)
ax.set_xlim(-EXT, EXT); ax.set_ylim(-EXT, EXT); ax.set_aspect("equal"); ax.axis("off")

draw(ax, NE / "ne_50m_antarctic_ice_shelves_polys.geojson", SHELF, EDGE, 0.5)
draw(ax, NE / "ne_50m_land.geojson", LAND, EDGE, 0.8)

# 60° Sud: limite del Trattato (art. VI)
t = [i / 360 * 2 * math.pi for i in range(361)]
ax.plot([R60 * math.sin(a) for a in t], [R60 * math.cos(a) for a in t], color=TXT, lw=1.6, ls=(0, (6, 5)), zorder=3)
ax.text(*proj(-128, -58.2), "60° SUD · LIMITE DEL TRATTATO", color=TXT, fontsize=12.5, ha="center", va="center",
        rotation=-52, zorder=6, fontweight=600)

# Terra della Regina Maud: settore rivendicato dalla Norvegia, 20° O – 45° E (Meld. St. 32)
for lon in (-20, 45):
    x0, y0 = proj(lon, -66); x1, y1 = proj(lon, -61.5)
    ax.plot([x0, x1], [y0, y1], color=RED, lw=2, zorder=4)
arc = [proj(lon, -62.5) for lon in [-20 + i * 0.5 for i in range(131)]]
ax.plot(*zip(*arc), color=RED, lw=4, zorder=4, solid_capstyle="butt")
# etichetta del settore spostata nella didascalia della slide (sulla mappa si sovrapponeva all'arco)

def pt(lon, lat, color, label, sub, dx, dy, ha="left"):
    x, y = proj(lon, lat)
    ax.scatter([x], [y], s=110, c=color, zorder=7, edgecolors=BG, linewidths=1.8)
    ax.text(x + dx, y + dy, label, color=color if color == RED else TXT, fontsize=14, fontweight=600, ha=ha, zorder=8)
    ax.text(x + dx, y + dy - 0.017, sub, color=MUTED, fontsize=12, ha=ha, zorder=8)

pt(3.35, -54.42, RED, "Isola Bouvet", "annessa il 1/12/1927 · fuori dal trattato", 0.012, 0.004)            # 54°25' S 3°21' E
pt(-90.58, -68.83, RED, "Isola Peter I", "Norvegia · 1929–31", -0.095, -0.006, ha="right")             # 68°50' S 90°35' O
_px, _py = proj(-90.58, -68.83)
ax.plot([_px - 0.088, _px - 0.008], [_py, _py], color=RED, lw=1.2, zorder=6)
pt(162.27, -77.72, TXT, "Blood Falls", "ghiacciaio Taylor", 0.014, -0.006)                              # 77°43' S 162°16' E
ax.text(0, -0.006, "POLO SUD", color=MUTED, fontsize=11, ha="center", va="top", zorder=6)
ax.scatter([0], [0], s=18, c=MUTED, zorder=6)

MAP = OUT / "mappa_antartide.png"
fig.savefig(MAP, facecolor=BG); plt.close(fig)
MAP64 = base64.b64encode(MAP.read_bytes()).decode()

# ---------------------------------------------------------------- slide
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
h1{font-family:'Crimson Text',serif;font-weight:400;font-size:88px;line-height:1.1;margin-top:auto}
h1.m{font-size:76px}
.rule{height:3px;background:#f2efe9;margin-top:48px}
.red{font-family:'Crimson Text',serif;font-style:italic;font-size:56px;color:#c8211f;margin-top:30px;line-height:1.15}
.quote{font-family:'Crimson Text',serif;font-size:50px;line-height:1.3;margin-top:auto;margin-bottom:auto}
.quote.s{font-size:45px}
.quote i{color:#c8211f}
.body{font-size:30px;line-height:1.5;color:#9b968e;margin-top:40px}
.map{width:760px;height:760px;margin:0 auto}
.cap{font-size:24px;line-height:1.45;color:#9b968e;margin-top:4px}
.src{position:absolute;left:96px;right:96px;bottom:150px;font-size:21px;line-height:1.4;color:#7d7870;border-top:1px solid #2c2b2e;padding-top:18px}
.foot{position:absolute;left:96px;right:96px;bottom:84px;display:flex;justify-content:space-between;align-items:baseline}
.foot b{font-size:24px;letter-spacing:.42em;font-weight:600} .foot span{font-size:22px;color:#7d7870}
.line{margin-top:56px;height:150px;position:relative}
.line .w{position:absolute;left:0;right:0;top:70px;height:4px;background:#f2efe9}
.line .r{position:absolute;left:58%;top:30px;width:5px;height:84px;background:#c8211f}
.line .t{position:absolute;left:58%;top:124px;transform:translateX(-50%);font-size:22px;letter-spacing:.3em;color:#9b968e}
"""

S_TRATTATO = "Trattato Antartico (testo ufficiale, Washington 1/12/1959), artt. I, IV, V, VI · Segreteria del Trattato Antartico, ats.aq"
S_PARTI = "Segreteria del Trattato Antartico, ats.aq: elenco delle Parti"
S_MADRID = "Segreteria del Trattato Antartico, ats.aq: Protocollo di Madrid, artt. 7 e 25"
S_NOR = "Governo norvegese, Meld. St. 32 (2014–2015), cap. 3 · Store norske leksikon (coordinate di Peter I)"
S_BF = "Zoumplis et al., Nature Geoscience, online 3/8/2026, DOI 10.1038/s41561-026-02054-6 · Google Trends Italia, 22–26/11/2026"
S_MAP = "Dati Natural Earth (pubblico dominio) · coordinate: Meld. St. 32, Store norske leksikon, Wikipedia (Blood Falls)"
S_ALL = "ats.aq · Governo norvegese · Nature Geoscience · Natural Earth"

slides = [
 ("<div class='kick'>Washington · 1° dicembre 1959</div>"
  "<div class='line'><div class='w'></div><div class='r'></div><div class='t'>60° S</div></div>"
  "<h1>C’è un continente che nessuno può possedere.</h1>"
  "<div class='rule'></div>"
  "<div class='red'>Le pretese sono solo congelate.</div>", S_ALL),

 ("<div class='kick'>Sotto la linea dei 60° Sud</div>"
  f"<img class='map' src='data:image/png;base64,{MAP64}'>"
  "<div class='cap'>Dentro la linea tratteggiata vale il Trattato. In rosso le rivendicazioni norvegesi: l’arco è la Terra della Regina Maud (1939).</div>", S_MAP),

 ("<div class='who'>Carmela</div><div class='role'>la giornalista · i fatti</div>"
  "<div class='year'>1959</div>"
  "<div class='quote s'>A Washington dodici Paesi firmano: l’Antartide sarà usata «solo per scopi pacifici». "
  "Vietate le basi militari, i test di armi, le esplosioni nucleari, le scorie radioattive. "
  "Vale per tutto ciò che sta a sud del 60° parallelo. Oggi le Parti sono <i>58</i>.</div>", S_TRATTATO + " · " + S_PARTI),

 ("<div class='who'>Carmela</div><div class='role'>la giornalista · il ghiaccio che sanguina</div>"
  "<div class='quote s'>Ai piedi del ghiacciaio Taylor il ghiaccio diventa rosso: è acqua salata, ricca di ferro, che risale da sotto il ghiacciaio. "
  "Ad agosto uno studio su 167 campioni vi ha trovato microrganismi marini ancora attivi: "
  "<i>l’eredità di un mare</i> rimasto intrappolato sotto il ghiaccio. In questi giorni in Italia è tra le ricerche in maggiore crescita.</div>", S_BF),

 ("<div class='who'>Teng</div><div class='role'>il finanziatore</div>"
  "<div class='quote'>Dal 1998 il Protocollo di Madrid vieta di estrarre minerali. "
  "Ma dal <i>2048</i> una qualsiasi delle Parti consultive potrà chiedere di riesaminarlo. "
  "Mancano ventidue anni. Io un’opzione la riconosco, quando la vedo.</div>", S_MADRID),

 ("<div class='who'>George</div><div class='role'>quello che fa domande</div>"
  "<div class='quote s'>Il 1° dicembre 1927 una spedizione norvegese sbarca sull’isola Bouvet e la annette. "
  "Il 1° dicembre 1959, stesso giorno, si firma il trattato che congela le rivendicazioni. "
  "Bouvet però sta a 54° Sud: <i>fuori</i> dal trattato. È solo una coincidenza di calendario? Qualcuno l’ha mai chiesto?</div>",
  S_NOR + " · " + S_TRATTATO + " · La coincidenza di date è riportata come domanda, non come fatto."),

 ("<div class='who'>Diana</div><div class='role'>la più responsabile</div>"
  "<div class='quote s'>Articolo IV: firmare non vuol dire rinunciare. Le pretese sono ferme, non cancellate. "
  "La Norvegia rivendica ancora la Terra della Regina Maud e l’isola Peter I; il Perù siede al tavolo come Parte consultiva dal 1989. "
  "Non è una linea tracciata per sempre. <i>È una linea tracciata finché regge.</i></div>", S_TRATTATO + " · " + S_NOR + " · " + S_PARTI),

 ("<h1 class='m'>Fin dove arriva una linea bianca?</h1>"
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
        pg.set_content(page(inner, src, i, len(slides))); pg.wait_for_timeout(250)
        over = pg.evaluate("(()=>{const s=document.querySelector('.src').getBoundingClientRect().top;"
                           "return [...document.querySelectorAll('.c > *')].some(e=>e.getBoundingClientRect().bottom>s-10)})()")
        if over: print(f"ATTENZIONE: slide {i} sborda")
        pg.screenshot(path=str(OUT / f"10_antartide_{i}.png"))
    b.close()
print("ok")
