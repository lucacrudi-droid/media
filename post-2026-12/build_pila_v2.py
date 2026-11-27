"""Post 012 · Istruttoria «Il navigatore italiano» (Chicago Pile-1) · stile v2, carosello 7 slide (27/11/2026).
Uso: python3 build_pila_v2.py <cartella foto> <cartella output>
Foto: cp1_costruzione.jpg, squadra_1946.jpg, cp1_dipinto.jpg. Senza una foto la slide esce su carta.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "strumenti"))
import stile_v2 as v
from PIL import Image, ImageDraw

FOTO, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
R, N, TOT = "ISTRUTTORIA", "012", 7

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

S_OSTI = "OSTI · Dipartimento dell’Energia USA, «Manhattan Project: CP-1 Goes Critical, Met Lab, December 2, 1942»"
S_ANL = "Argonne National Laboratory, «The Italian Navigator Lands»"
S_NOBEL = "NobelPrize.org, Enrico Fermi – Biographical"
S_ALL = "OSTI/DOE · Argonne National Laboratory · NobelPrize.org"

cost, squadra, dip = foto("cp1_costruzione.jpg"), foto("squadra_1946.jpg"), foto("cp1_dipinto.jpg")
C_COST = "CP-1 in costruzione, 1942: il 7° strato di grafite · Argonne/DOE · pubblico dominio"
C_SQ = "La squadra di CP-1, Chicago 2/12/1946 · LANL/NSRC · CC BY-SA 4.0"
C_HIL = "Norman Hilberry (ultima fila, primo a sinistra), Chicago 2/12/1946 · LANL/NSRC · CC BY-SA 4.0"
C_FER = "Enrico Fermi (prima fila, a sinistra), Chicago 2/12/1946 · LANL/NSRC · CC BY-SA 4.0"
C_DIP = "CP-1 il 2/12/1942, ricostruzione pittorica · DOE · pubblico dominio"

s = []
cop, ccop = (cost, C_COST)
s.append(fonti(v.photo_cover(cop, R, N, "Chicago · 2 dicembre 1942 · ore 15:25",
    "Il navigatore\nitaliano.", "Era un messaggio in codice.", ccop, f"1/{TOT}") if cop is not None else
    v.text_slide(R, N, "Il navigatore italiano.", "Chicago · 2 dicembre 1942", "Era un messaggio in codice.", f"1/{TOT}"), S_ALL))
s.append(fonti(pts(cost, frac(cost, 0, 0.5, 1, 1.0), "1942", "Carmela · la giornalista · i fatti",
    "In un campo da squash abbandonato, sotto le tribune dello stadio dell’Università di Chicago, "
    "la squadra di Enrico Fermi accende la prima reazione nucleare a catena controllata e autosostenuta. "
    "Ore 15:25. Dura 28 minuti. Potenza: circa mezzo watt, appena quanto basta per una piccola lampadina.",
    f"2/{TOT}", credit=C_COST), S_OSTI + " · " + S_NOBEL))
s.append(fonti(pts(squadra, frac(squadra, 0, 0.40, 1, 0.95), "La telefonata", "Carmela · la giornalista",
    "Arthur Compton chiama James Conant a Washington.\n«Il navigatore italiano è sbarcato nel Nuovo Mondo.»\n"
    "«Com’erano gli indigeni?»\n«Molto amichevoli.»", f"3/{TOT}", credit=C_SQ), S_OSTI + " · " + S_ANL))
s.append(fonti(pts(cost, frac(cost, 0.05, 0.15, 0.95, 0.6), "Teng", "il finanziatore",
    "Mezzo watt. Non illumini nemmeno una stanza. Ma chi pagava quel campo da squash non stava comprando luce. "
    "Stava comprando il passo successivo.", f"4/{TOT}", quote=True, credit=C_COST), S_OSTI))
s.append(fonti(pts(squadra, frac(squadra, 0.0, 0.31, 0.6, 0.57), "George", "quello che fa domande",
    "Sulla balconata Norman Hilberry aspettava con un’ascia, pronto a tagliare una fune e far cadere una barra di controllo. "
    "Su una piattaforma, una squadra era pronta ad allagare la pila con una soluzione di cadmio. "
    "Che cosa avevano immaginato, per prepararsi così? E chi si offre di stare lassù?",
    f"5/{TOT}", quote=True, credit=C_HIL), S_OSTI))
s.append(fonti(pts(squadra, frac(squadra, 0.03, 0.48, 0.55, 0.76), "Diana", "la più responsabile",
    "Restiamo sui fatti. Fermi aveva lasciato l’Italia nel 1938, subito dopo il Nobel, soprattutto per sfuggire alla dittatura fascista. "
    "Quella pila era un passo del Progetto Manhattan. La linea è stata oltrepassata in 28 minuti. "
    "Non esiste una barra di controllo per tornare indietro.", f"6/{TOT}", quote=True, credit=C_FER), S_NOBEL + " · " + S_OSTI))
s.append(fonti(v.text_slide(R, N, "Chi decide?", "Quando una linea va oltrepassata",
    "Chi decide quando una linea va oltrepassata? Scrivilo nei commenti.\n\n"
    "La linea bianca · Saga della Linea Bianca, volume I", f"7/{TOT}"), S_ALL))

for i, im in enumerate(s, 1):
    im.save(os.path.join(OUT, f"12v2_pila_{i}.png"), optimize=True)
print("ok", len(s))
