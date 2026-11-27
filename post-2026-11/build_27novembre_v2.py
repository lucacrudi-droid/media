"""Post 009 · Istruttoria «27 novembre» · rifacimento in stile v2 (27/11/2026).
Uso: python3 build_27novembre_v2.py <cartella foto> <cartella output>
Foto (Wikimedia Commons, vedi foto/crediti_09.txt): nobel.jpg, testamento.jpg, marte.jpg, osiride.jpg
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "strumenti"))
import stile_v2 as v
from PIL import Image, ImageDraw

FOTO, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
R, N, TOT = "ISTRUTTORIA", "009", 9

def foto(nome):
    p = os.path.join(FOTO, nome)
    return Image.open(p).convert("RGB") if os.path.exists(p) else None

_pts = v.photo_text_slide
def pts(photo, crop, rubric, num, label, sub, body, page=None, quote=False, credit=None):
    """Senza la foto giusta la slide esce su carta: mai una foto non coerente."""
    if photo is None:
        return v.text_slide(rubric, num, label, sub, body, page, quote)
    return _pts(photo, crop, rubric, num, label, sub, body, page, quote, credit)

def fonti(img, testo):
    d = ImageDraw.Draw(img)
    f = v.B_LIGHT(17)
    y = v.H - 138
    for riga in v.wrap(d, "Fonti: " + testo, f, v.W - 2 * v.M)[:2][::-1]:
        d.text((v.M, y), riga, font=f, fill=(120, 116, 108))
        y -= 24
    return img

S_NOBEL = "NobelPrize.org, «Alfred Nobel’s will» e testo integrale del testamento"
S_MARS = "NASA Science, PIA18888 · The Planetary Society"
S_OSIRIS = "Spaceflight Now 27/11/2001 (NASA/Hubble) · ESA, comunicato 15-2003 · Vidal-Madjar et al. 2003"
S_ALL = "NobelPrize.org · NASA Science · ESA · The Planetary Society · Spaceflight Now"

C_NOBEL = "Alfred Nobel, foto Gösta Florman · pubblico dominio"
C_TEST = "Testamento di Alfred Nobel, 27/11/1895 · pubblico dominio"
C_MARTE = "Marte prima e durante la tempesta globale del 2001 · NASA/Hubble · CC BY 2.0"
C_OSIR = "HD 209458 b «Osiride», illustrazione · ESA/NASA · CC BY 4.0"

nobel, test, marte, osir = foto("nobel.jpg"), foto("testamento.jpg"), foto("marte.jpg"), foto("osiride.jpg")
def frac(img, x0, y0, x1, y1):
    if img is None: return None
    w, h = img.size
    return (int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))
ritagli = {
    "nobel_volto": frac(nobel, 0.12, 0.08, 0.92, 0.55),
    "nobel_busto": frac(nobel, 0.0, 0.08, 1.0, 0.50),
    "test_firma": frac(test, 0.52, 0.45, 1.0, 0.95),
    "test_alto": frac(test, 0.0, 0.0, 0.5, 0.45),
    "marte": frac(marte, 0.5, 0.05, 1.0, 0.95),
    "osir": frac(osir, 0.0, 0.15, 1.0, 0.75),
}

slides = []
copertina, credito_cop = (test, C_TEST) if test is not None else (nobel.crop(frac(nobel, 0.0, 0.05, 1.0, 0.62)), C_NOBEL)
slides.append(fonti(v.photo_cover(copertina, R, N, "Parigi · Marte · Pegaso",
    "Il 27 novembre,\ntre linee.", "Ognuna ha lasciato qualcosa dall’altra parte.", credito_cop, f"1/{TOT}"), S_ALL))
slides.append(fonti(pts(nobel, ritagli["nobel_busto"], R, N, "1895", "Carmela · la giornalista · i fatti",
    "Parigi, Club svedese-norvegese. Alfred Nobel, l’uomo della dinamite, firma il suo terzo e ultimo testamento. "
    "Il patrimonio andrà in cinque parti a chi ha portato «il massimo beneficio all’umanità». "
    "Il premio per la pace lo sceglierà un comitato di cinque persone nominato dal Parlamento norvegese.",
    f"2/{TOT}", credit=C_NOBEL), S_NOBEL))
slides.append(fonti(pts(test, ritagli["test_firma"], R, N, "L’ultima clausola", "Carmela · la giornalista",
    "Nello stesso testamento Nobel chiede che, dopo la sua morte, gli vengano recise le arterie. "
    "Solo quando medici competenti avranno confermato «chiari segni di morte», il suo corpo potrà essere cremato.",
    f"3/{TOT}", credit=C_TEST), S_NOBEL))
slides.append(fonti(pts(marte, ritagli["marte"], R, N, "1971", "Carmela · la giornalista · i fatti",
    "Il modulo sovietico Mars 2 arriva su Marte durante una delle più grandi tempeste di polvere mai registrate, e si schianta. "
    "È il primo oggetto umano a toccare la superficie del pianeta. A bordo c’era un piccolo rover, legato da un cavo di 15 metri. "
    "Secondo la NASA, il relitto non è ancora stato localizzato.",
    f"4/{TOT}", credit=C_MARTE), S_MARS))
slides.append(fonti(pts(osir, ritagli["osir"], R, N, "2001", "Carmela · la giornalista · i fatti",
    "La NASA annuncia: Hubble ha letto, per la prima volta, l’atmosfera di un pianeta fuori dal Sistema solare. "
    "Si chiama HD 209458 b, è a 150 anni luce. Nel 2003 si scopre che sta evaporando: "
    "almeno 10.000 tonnellate di idrogeno al secondo, una coda di oltre 200.000 km. Lo chiamano Osiride.",
    f"5/{TOT}", credit=C_OSIR), S_OSIRIS))
slides.append(fonti(pts(nobel, ritagli["nobel_volto"], R, N, "Teng", "il finanziatore",
    "Il 94% di una fortuna costruita sugli esplosivi, trasformato in un premio per chi fa del bene. "
    "Oltrepassare una linea ha sempre un costo. Nobel, almeno, ha deciso lui a chi lasciare il conto.",
    f"6/{TOT}", quote=True, credit=C_NOBEL), S_NOBEL + " · Wikipedia (dato del 94%)"))
slides.append(fonti(pts(test, ritagli["test_alto"], R, N, "George", "quello che fa domande",
    "Si racconta che Nobel abbia letto il proprio necrologio, pubblicato per errore. Qualcuno l’ha mai trovato, quel giornale? "
    "E di cosa aveva paura un uomo che chiede di farsi tagliare le arterie dopo morto?",
    f"7/{TOT}", quote=True, credit=C_TEST), S_NOBEL + " · Il necrologio prematuro è un aneddoto tramandato: qui è una domanda, non un fatto."))
slides.append(fonti(pts(marte, frac(marte, 0.0, 0.05, 0.5, 0.95), R, N, "Diana", "la più responsabile",
    "Restiamo sui fatti. Un testamento firmato. Un relitto mai ritrovato. Un pianeta che perde la sua aria. "
    "Il necrologio? Finché non vedo quel giornale, per me resta un racconto.",
    f"8/{TOT}", quote=True, credit=C_MARTE), S_ALL))
slides.append(fonti(v.text_slide(R, N, "E tu?", "Dall’altra parte della linea",
    "Cosa lasceresti tu, dall’altra parte della linea? Scrivilo nei commenti.\n\n"
    "La linea bianca · Saga della Linea Bianca, volume I",
    f"9/{TOT}"), S_ALL))

for i, im in enumerate(slides, 1):
    im.save(os.path.join(OUT, f"09v2_27novembre_{i}.png"), optimize=True)
print("ok", len(slides))
