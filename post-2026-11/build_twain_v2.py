"""Post 011 · Curiosità disturbante «Mark Twain e la cometa di Halley» · stile v2, carosello 4 slide (27/11/2026).
Uso: python3 build_twain_v2.py <cartella foto> <cartella output>   (foto: twain.jpg, halley_arequipa.jpg)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "strumenti"))
import stile_v2 as v
from PIL import Image, ImageDraw

FOTO, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
R, N, TOT = "CURIOSITÀ DISTURBANTE", "011", 4

def fonti(img, testo):
    d = ImageDraw.Draw(img); f = v.B_LIGHT(17); y = v.H - 138
    for riga in v.wrap(d, "Fonti: " + testo, f, v.W - 2 * v.M)[:2][::-1]:
        d.text((v.M, y), riga, font=f, fill=(120, 116, 108)); y -= 24
    return img

def frac(img, x0, y0, x1, y1):
    w, h = img.size
    return (int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))

twain = Image.open(os.path.join(FOTO, "twain.jpg")).convert("RGB")
halley = Image.open(os.path.join(FOTO, "halley_arequipa.jpg")).convert("RGB")
C_TW = "Mark Twain, foto A.F. Bradley, 1907 · pubblico dominio"
C_HA = "Cometa di Halley, Arequipa (Perù), 21/4/1910 · Harvard College Observatory · pubblico dominio"
S_NASA = "NASA (J. Uri, 2021) · NASA/JPL, Great Comets in History · The Observatory, vol. 32 (1909)"
S_TW = "The Mark Twain House & Museum · PBS NewsHour (H. Markel, 2022)"
S_ALL = "NASA · NASA/JPL · The Mark Twain House & Museum · Harvard College Observatory"

s = []
s.append(fonti(v.photo_cover(twain.crop(frac(twain, 0, 0.02, 1, 0.62)), R, N, "Florida, Missouri · 30 novembre 1835",
    "Nacque con\nla cometa.", "Disse che se ne sarebbe andato con lei.", C_TW, f"1/{TOT}"), S_NASA))
s.append(fonti(v.photo_text_slide(twain, frac(twain, 0, 0.12, 1, 0.66), R, N, "1909", "Le sue parole",
    "Sono arrivato con la cometa di Halley nel 1835. Torna l’anno prossimo, e mi aspetto di andarmene con lei. "
    "Sarebbe la più grande delusione della mia vita se non andassi via con la cometa di Halley.",
    f"2/{TOT}", quote=True, credit=C_TW), S_TW + " · citazione attribuita, in traduzione italiana"))
s.append(fonti(v.photo_text_slide(halley, frac(halley, 0, 0.2, 1, 0.75), R, N, "21 aprile 1910", "Il giorno dopo il ritorno",
    "La cometa di Halley torna al perielio, il punto più vicino al Sole, il 20 aprile 1910. "
    "Mark Twain muore il giorno dopo, il 21 aprile. Quello stesso 21 aprile, ad Arequipa, in Perù, "
    "l’Osservatorio di Harvard fotografa la cometa con mezz’ora di esposizione. È questa immagine.",
    f"3/{TOT}", credit=C_HA), S_NASA + " · Harvard College Observatory, lastra b41215"))
s.append(fonti(v.text_slide(R, N, "2061", "Il prossimo ritorno",
    "Uno scrittore che annuncia la propria fine con un anno di anticipo. E un cielo che gli dà ragione.\n\n"
    "La cometa tornerà nel 2061. Mandalo a chi ci sarà.\n\n"
    "La linea bianca · Saga della Linea Bianca, volume I", f"4/{TOT}"), "NASA Science, 1P/Halley"))

for i, im in enumerate(s, 1):
    im.save(os.path.join(OUT, f"11v2_twain_{i}.png"), optimize=True)
print("ok", len(s))
