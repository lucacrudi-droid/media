"""Stile v2 dei post @crudiluca, allineato a lucacrudi.com.
Palette del sito: carta #F5F2EB, carta scura #E9E3D6, oro #B08A47, rosso #B92D35, inchiostro #171B1D.
Titoli: condensato maiuscolo (Barlow Condensed, al posto del Limes Display). Testo: Barlow (simile a Bahnschrift/DIN).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps
import random

W, H = 1080, 1350
import os
F = os.environ.get("CRUDI_FONTS", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")) + "/"
PAPER = (245, 242, 235)
PAPER2 = (233, 227, 214)
GOLD = (176, 138, 71)
RED = (185, 45, 53)
INK = (23, 27, 29)
M = 72


def font(name, size):
    return ImageFont.truetype(F + name, size)


H_BOLD = lambda s: font("BarlowCondensed-Bold.ttf", s)
H_SEMI = lambda s: font("BarlowCondensed-SemiBold.ttf", s)
B_REG = lambda s: font("Barlow-Regular.ttf", s)
B_MED = lambda s: font("Barlow-Medium.ttf", s)
B_LIGHT = lambda s: font("Barlow-Light.ttf", s)


def tracked(d, x, y, text, f, fill, track):
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + track
    return x


def tw(d, text, f, track=0):
    return sum(d.textlength(c, font=f) + track for c in text) - track


def wrap(d, text, f, maxw):
    out = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) <= maxw:
                cur = t
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return out


def grade(photo, size):
    """Ritaglio a riempimento, toni caldi e desaturati, grana fine: il trattamento 'archivio'."""
    p = ImageOps.fit(photo.convert("RGB"), size, Image.LANCZOS, centering=(0.5, 0.45))
    p = ImageEnhance.Color(p).enhance(0.55)
    p = ImageEnhance.Contrast(p).enhance(1.12)
    warm = Image.new("RGB", size, (176, 138, 71))
    p = Image.blend(p, warm, 0.10)
    random.seed(7)
    noise = Image.effect_noise(size, 22).convert("RGB")
    p = Image.blend(p, noise, 0.05)
    return p


def vignette(img, strength=0.55):
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([-w * 0.25, -h * 0.2, w * 1.25, h * 1.2], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(min(w, h) // 5))
    dark = Image.new("RGB", (w, h), INK)
    return Image.composite(img, Image.blend(img, dark, strength), mask)


def header(d, rubric, num, color=INK):
    tracked(d, M, 64, rubric.upper(), B_MED(22), GOLD, 5)
    tracked(d, W - M - tw(d, num, B_MED(22), 5), 64, num, B_MED(22), RED, 5)


def footer(d, page=None, color=INK):
    tracked(d, M, H - 92, "LUCA CRUDI", H_SEMI(26), color, 7)
    r = page or "@crudiluca"
    d.text((W - M - d.textlength(r, font=B_REG(22)), H - 90), r, font=B_REG(22), fill=GOLD)


def photo_cover(photo, rubric, num, kicker, title, red, credit, page=None):
    """Foto in alto (60%), pannello carta in basso con titolo condensato."""
    img = Image.new("RGB", (W, H), PAPER)
    ph = 800
    p = vignette(grade(photo, (W, ph)), 0.35)
    img.paste(p, (0, 0))
    d = ImageDraw.Draw(img)
    # fascia scura in alto per leggibilità della testata
    top = Image.new("L", (W, 150), 0)
    td = ImageDraw.Draw(top)
    for y in range(150):
        td.line([(0, y), (W, y)], fill=int(150 * (1 - y / 150)))
    img.paste(Image.new("RGB", (W, 150), INK), (0, 0), top)
    d = ImageDraw.Draw(img)
    tracked(d, M, 52, rubric.upper(), B_MED(22), PAPER, 5)
    tracked(d, W - M - tw(d, num, B_MED(22), 5), 52, num, B_MED(22), PAPER, 5)
    if credit:
        cf = B_LIGHT(16)
        cw = d.textlength(credit, font=cf); cx = W - M - cw; cy = ph - 34
        d.rectangle((cx - 10, cy - 5, W - M + 10, cy + 22), fill=(23, 27, 29))
        d.text((cx, cy), credit, font=cf, fill=(235, 232, 225))
    # linea rossa di confine
    d.rectangle([0, ph, W, ph + 6], fill=RED)
    y = ph + 46
    tracked(d, M, y, kicker.upper(), B_MED(22), GOLD, 5)
    y += 44
    tf = H_BOLD(96)
    for line in wrap(d, title.upper(), tf, W - 2 * M):
        d.text((M, y), line, font=tf, fill=INK)
        y += 96
    d.text((M, y + 14), red, font=font("EBGaramond-Italic.ttf", 46), fill=RED)
    footer(d, page)
    return img


def text_slide(rubric, num, label, sub, body, page=None, quote=False):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    header(d, rubric, num)
    d.rectangle([M, 120, W - M, 121], fill=GOLD)
    y = 230
    tf = H_BOLD(64)
    d.text((M, y), label.upper(), font=tf, fill=INK)
    y += 78
    if sub:
        tracked(d, M, y, sub.upper(), B_MED(22), GOLD, 5)
        y += 50
    d.rectangle([M, y, M + 120, y + 6], fill=RED)
    y += 60
    bf = font("EBGaramond-Italic.ttf", 50) if quote else font("EBGaramond.ttf", 44)
    lh = 68 if quote else 62
    txt = ("«" + body + "»") if quote else body
    for line in wrap(d, txt, bf, W - 2 * M):
        d.text((M, y), line, font=bf, fill=INK)
        y += lh
    footer(d, page)
    return img


def photo_text_slide(photo, crop, rubric, num, label, sub, body, page=None, quote=False, credit=None):
    """Dettaglio fotografico in alto (45%), testo sul pannello carta."""
    img = Image.new("RGB", (W, H), PAPER)
    ph = 610
    det = photo.convert("RGB").crop(crop)
    p = vignette(grade(det, (W, ph)), 0.3)
    img.paste(p, (0, 0))
    top = Image.new("L", (W, 150), 0)
    td = ImageDraw.Draw(top)
    for y in range(150):
        td.line([(0, y), (W, y)], fill=int(150 * (1 - y / 150)))
    img.paste(Image.new("RGB", (W, 150), INK), (0, 0), top)
    d = ImageDraw.Draw(img)
    tracked(d, M, 52, rubric.upper(), B_MED(22), PAPER, 5)
    tracked(d, W - M - tw(d, num, B_MED(22), 5), 52, num, B_MED(22), PAPER, 5)
    if credit:
        cf = B_LIGHT(16)
        cw = d.textlength(credit, font=cf); cx = W - M - cw; cy = ph - 34
        d.rectangle((cx - 10, cy - 5, W - M + 10, cy + 22), fill=(23, 27, 29))
        d.text((cx, cy), credit, font=cf, fill=(235, 232, 225))
    d.rectangle([0, ph, W, ph + 6], fill=RED)
    y = ph + 50
    d.text((M, y), label.upper(), font=H_BOLD(64), fill=INK)
    y += 74
    if sub:
        tracked(d, M, y, sub.upper(), B_MED(22), GOLD, 5)
        y += 52
    bf = font("EBGaramond-Italic.ttf", 44) if quote else font("EBGaramond.ttf", 40)
    lh = 60 if quote else 56
    txt = ("«" + body + "»") if quote else body
    for line in wrap(d, txt, bf, W - 2 * M):
        d.text((M, y), line, font=bf, fill=INK)
        y += lh
    footer(d, page)
    return img
