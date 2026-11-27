"""Post 010 · Istruttoria «1° dicembre: Antartide» · stile v2, carosello 7 slide (27/11/2026).
Uso: python3 build_antartide_v2.py <cartella foto> <cartella output>   (foto: blood_falls.jpg, polo_sud.jpg)
Senza una foto la slide esce su carta.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "strumenti"))
import stile_v2 as v
from PIL import Image, ImageDraw

FOTO, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
R, N, TOT = "ISTRUTTORIA", "010", 7

def foto(n):
    p = os.path.join(FOTO, n)
    return Image.open(p).convert("RGB") if os.path.exists(p) else None
def frac(img, x0, y0, x1, y1):
    if img is None: return None
    w, h = img.size
    return (int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))
def pts(photo, crop, label, sub, body, page, quote=False, credit=None):
    if photo is None:
        return v.text_slide(R, N, label, sub, body, page, quote)
    return v.photo_text_slide(photo, crop, R, N, label, sub, body, page, quote, credit)
def fonti(img, testo):
    d = ImageDraw.Draw(img); f = v.B_LIGHT(17); y = v.H - 138
    for riga in v.wrap(d, "Fonti: " + testo, f, v.W - 2 * v.M)[:2][::-1]:
        d.text((v.M, y), riga, font=f, fill=(120, 116, 108)); y -= 24
    return img

S_TRATTATO = "Trattato Antartico (testo ufficiale, Washington 1/12/1959), artt. I, IV, V, VI · ats.aq"
S_PARTI = "Segreteria del Trattato Antartico, ats.aq: elenco delle Parti"
S_MADRID = "Segreteria del Trattato Antartico, ats.aq: Protocollo di Madrid, artt. 7 e 25"
S_NOR = "Governo norvegese, Meld. St. 32 (2014–2015), cap. 3"
S_BF = "Zoumplis et al., Nature Geoscience, online 3/8/2026, DOI 10.1038/s41561-026-02054-6 · Google Trends Italia, 22–26/11/2026"
S_ALL = "ats.aq · Governo norvegese · Nature Geoscience"

bf, polo = foto("blood_falls.jpg"), foto("polo_sud.jpg")
C_BF = "Blood Falls, ghiacciaio Taylor · NSF/Peter Rejcek · pubblico dominio"
C_PO = "Polo Sud cerimoniale con le bandiere dei 12 firmatari · NSF/Josh Landis, 1999 · pubblico dominio"

s = []
cop = bf if bf is not None else polo
s.append(fonti(v.photo_cover(cop, R, N, "Washington · 1° dicembre 1959",
    "Un continente\ndi nessuno.", "Per ora. Le pretese sono solo congelate.",
    C_BF if bf is not None else C_PO, f"1/{TOT}") if cop is not None else
    v.text_slide(R, N, "Un continente di nessuno.", "Washington · 1° dicembre 1959", "Per ora. Le pretese sono solo congelate.", f"1/{TOT}"), S_ALL))
s.append(fonti(pts(polo, frac(polo, 0, 0.1, 1, 0.9), "1959", "Carmela · la giornalista · i fatti",
    "A Washington dodici Paesi firmano: l’Antartide sarà usata «solo per scopi pacifici». "
    "Vietate le basi militari, i test di armi, le esplosioni nucleari, le scorie radioattive. "
    "Vale per tutto ciò che sta a sud del 60° parallelo. Oggi le Parti sono 58.", f"2/{TOT}", credit=C_PO),
    S_TRATTATO + " · " + S_PARTI))
s.append(fonti(pts(bf, frac(bf, 0.25, 0, 1, 1), "Il ghiaccio che sanguina", "Carmela · la giornalista",
    "Ai piedi del ghiacciaio Taylor il ghiaccio diventa rosso: è acqua salata, ricca di ferro, che risale da sotto il ghiacciaio. "
    "Ad agosto uno studio su 167 campioni vi ha trovato microrganismi marini ancora attivi: "
    "l’eredità di un mare rimasto intrappolato sotto il ghiaccio.", f"3/{TOT}", credit=C_BF), S_BF))
s.append(fonti(pts(bf, frac(bf, 0, 0.1, 0.6, 1), "Teng", "il finanziatore",
    "Dal 1998 il Protocollo di Madrid vieta di estrarre minerali. Ma dal 2048 una qualsiasi delle Parti consultive "
    "potrà chiedere di riesaminarlo. Mancano ventidue anni. Io un’opzione la riconosco, quando la vedo.",
    f"4/{TOT}", quote=True, credit=C_BF), S_MADRID))
s.append(fonti(pts(polo, frac(polo, 0.2, 0.2, 0.8, 0.8), "George", "quello che fa domande",
    "Il 1° dicembre 1927 una spedizione norvegese sbarca sull’isola Bouvet e la annette. "
    "Il 1° dicembre 1959, stesso giorno, si firma il trattato che congela le rivendicazioni. "
    "Bouvet però sta a 54° Sud: fuori dal trattato. È solo una coincidenza di calendario? Qualcuno l’ha mai chiesto?",
    f"5/{TOT}", quote=True, credit=C_PO), S_NOR + " · " + S_TRATTATO + " · La coincidenza di date è una domanda, non un fatto."))
s.append(fonti(pts(bf, frac(bf, 0.4, 0.2, 1, 0.9), "Diana", "la più responsabile",
    "Articolo IV: firmare non vuol dire rinunciare. Le pretese sono ferme, non cancellate. "
    "La Norvegia rivendica ancora la Terra della Regina Maud e l’isola Peter I; il Perù siede al tavolo come Parte consultiva dal 1989. "
    "Non è una linea tracciata per sempre. È una linea tracciata finché regge.",
    f"6/{TOT}", quote=True, credit=C_BF), S_TRATTATO + " · " + S_NOR + " · " + S_PARTI))
s.append(fonti(v.text_slide(R, N, "Fin dove arriva?", "Una linea bianca",
    "Fin dove arriva una linea bianca, tracciata finché regge? Scrivilo nei commenti.\n\n"
    "La linea bianca · Saga della Linea Bianca, volume I", f"7/{TOT}"), S_ALL))

for i, im in enumerate(s, 1):
    im.save(os.path.join(OUT, f"10v2_antartide_{i}.png"), optimize=True)
print("ok", len(s))
