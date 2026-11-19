"""Mappe per i caroselli. Dati: Natural Earth (pubblico dominio), coordinate da fonti citate.
Uso: python3 mappe.py <cartella_dati_natural_earth>
"""
import json, sys, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from shapely.geometry import shape, box

NE = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(__file__).parent

for f in font_manager.findSystemFonts():
    if "Inter" in f and "Display" not in f:
        font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = "Inter"

BG, LAND, EDGE, TXT, MUTED, RED = "#0d0d0f", "#1f1e23", "#4a4750", "#f2efe9", "#9b968e", "#c8211f"

def load(name):
    return json.load(open(NE / f"{name}.geojson"))["features"]

def draw_geoms(ax, feats, ext, **kw):
    clip = box(ext[0], ext[2], ext[1], ext[3])
    for f in feats:
        g = shape(f["geometry"])
        if not g.intersects(clip):
            continue
        g = g.intersection(clip)
        polys = getattr(g, "geoms", [g])
        for p in polys:
            if p.geom_type == "Polygon":
                x, y = p.exterior.xy
                ax.fill(x, y, **kw)
            elif p.geom_type in ("LineString",):
                x, y = p.xy
                ax.plot(x, y, **kw)

def base(ext, w=8.8, h=7.0):
    fig = plt.figure(figsize=(w, h), dpi=100, facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3])
    ax.set_aspect("auto"); ax.axis("off")
    return fig, ax

def point(ax, x, y, color, size=90, marker="o"):
    ax.scatter([x], [y], s=size, c=color, marker=marker, zorder=5, edgecolors=BG, linewidths=1.5)

def label(ax, x, y, text, color=TXT, size=15, **kw):
    ax.text(x, y, text, color=color, fontsize=size, zorder=6, **kw)

land50, land10 = load("ne_50m_land"), load("ne_10m_land")

# 1 — ESSEX: Pacifico orientale
ext = (-155, -65, -40, 12)
fig, ax = base(ext)
draw_geoms(ax, land50, ext, facecolor=LAND, edgecolor=EDGE, linewidth=0.8)
sx, sy = -119.0, -0.667           # 0°40'S 119°W, stima di Owen Chase (American Heritage)
gx, gy = -89.6, -0.9              # Puerto Baquerizo Moreno, Galápagos (Natural Earth)
px, py = -149.57, -17.53          # Papeete, Tahiti (Natural Earth)
vx, vy = -71.62, -33.05           # Valparaíso (Natural Earth)
ax.annotate("", xy=(-143, -11), xytext=(sx - 2, sy - 1.5),
            arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.6, ls=(0, (4, 4))), zorder=4)
ax.annotate("", xy=(vx - 3, vy + 1), xytext=(sx + 2, sy - 2),
            arrowprops=dict(arrowstyle="-|>", color=TXT, lw=2.6, connectionstyle="arc3,rad=0.25"), zorder=4)
point(ax, sx, sy, RED, 220, "X")
label(ax, sx, sy + 3.2, "Qui affonda la Essex\n20 novembre 1820", RED, 17, ha="center", weight="semibold")
label(ax, sx - 3, sy - 0.2, "0°40′ S · 119° O\n(stima di Chase)", MUTED, 12.5, ha="right", va="center")
point(ax, gx, gy, TXT, 40)
label(ax, gx + 1.5, gy + 1.8, "Galápagos", TXT, 14)
point(ax, px, py, MUTED, 30)
label(ax, -153, -22.5, "Polinesia · Tahiti\n(isole evitate per\npaura dei cannibali)", MUTED, 12.5)
label(ax, -96, -24, "La scelta:\nla costa del Cile", TXT, 15, weight="semibold")
label(ax, -76, -6, "SUD\nAMERICA", MUTED, 13, ha="center")
label(ax, -154, 9.5, "Schema indicativo: le frecce indicano direzioni, non la rotta reale.", MUTED, 11)
fig.savefig(OUT / "mappa_essex.png", facecolor=BG); plt.close(fig)

# 2 — EGITTO: delta occidentale
ext = (29.3, 32.4, 29.6, 31.7)
fig, ax = base(ext)
draw_geoms(ax, land10, ext, facecolor=LAND, edgecolor=EDGE, linewidth=0.8)
nile = [f for f in load("ne_10m_rivers_lake_centerlines") if f["properties"].get("name") == "Nile"]
draw_geoms(ax, nile, ext, color="#3d6b8a", linewidth=1.8)
kx, ky = 30.816667, 30.533333     # Kom Abu Billu / Terenuthis, GEOnet Names Server (NGA)
cx, cy = 31.248022, 30.051906     # Cairo (Natural Earth)
ax_, ay_ = 29.94805, 31.201965    # Alessandria (Natural Earth)
point(ax, kx, ky, RED, 200)
label(ax, kx - 0.08, ky + 0.07, "Tell Abu Bellou\n(Kom Abu Billu, antica Terenuthis)", RED, 16, ha="right", weight="semibold")
point(ax, cx, cy, TXT, 50); label(ax, cx + 0.05, cy - 0.09, "Il Cairo", TXT, 15)
point(ax, ax_, ay_, TXT, 50); label(ax, ax_ + 0.05, ay_ - 0.1, "Alessandria", TXT, 15)
label(ax, 30.75, 31.6, "MAR MEDITERRANEO", MUTED, 12.5, ha="center")
label(ax, 31.33, 29.78, "Nilo", "#6f9ab8", 13, style="italic")
fig.savefig(OUT / "mappa_egitto.png", facecolor=BG); plt.close(fig)

# 3 — IRLANDA DEL NORD
ext = (-8.4, -5.2, 53.95, 55.45)
fig, ax = base(ext)
draw_geoms(ax, land10, ext, facecolor=LAND, edgecolor=EDGE, linewidth=0.8)
lakes = load("ne_10m_lakes")
draw_geoms(ax, lakes, ext, facecolor=BG, edgecolor=EDGE, linewidth=0.6)
bx, by = -6.518998, 54.808072     # Bellaghy (gazetteer.org.uk)
fx, fy = -5.960034, 54.600012     # Belfast (Natural Earth)
point(ax, bx, by, RED, 200)
label(ax, bx - 0.06, by + 0.07, "Vicino a Bellaghy:\nla torbiera (ritrovamento 2023)", RED, 16, ha="right", weight="semibold")
point(ax, fx, fy, TXT, 60)
label(ax, fx, fy - 0.05, "Belfast · Ulster Museum\nudienza del 16/11/2026", TXT, 13, ha="center", va="top")
label(ax, -6.45, 54.6, "Lough\nNeagh", MUTED, 12, ha="center", style="italic")
fig.savefig(OUT / "mappa_irlanda.png", facecolor=BG); plt.close(fig)
print("mappe ok")
