#!/usr/bin/env python3
"""Reel verticale 1080x1920 da grafiche 1080x1350 (stile @crudiluca).

Uso:
  python3 build_reel.py USCITA.mp4 SLIDE1.png [SLIDE2.png ...] [--secondi 4] [--primo 2.5]

- Ogni slide resta al centro su fondo #0b0b0c, con un lento zoom (Ken Burns leggero)
  e una dissolvenza di 0,5 s tra una slide e l'altra.
- --primo: durata della prima slide (il gancio), di norma piu' breve.
- Traccia audio muta AAC (Instagram accetta meglio i video con traccia audio);
  la musica la aggiunge Metricool (audioConfiguration) al momento della programmazione.
- Crea anche la copertina USCITA_cover.jpg (prima slide su fondo 1080x1920).
Durata consigliata del Reel: 15-25 secondi.
"""
import argparse, subprocess, sys
from pathlib import Path

W, H, FPS, BG = 1080, 1920, 30, "0x0b0b0c"
FADE = 0.5

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("slides", nargs="+")
    ap.add_argument("--secondi", type=float, default=4.0)
    ap.add_argument("--primo", type=float, default=2.5)
    a = ap.parse_args()
    slides = [Path(s) for s in a.slides]
    for s in slides:
        if not s.exists():
            sys.exit(f"manca {s}")
    durs = [a.primo] + [a.secondi] * (len(slides) - 1) if len(slides) > 1 else [max(a.primo, a.secondi)]
    inputs, filters = [], []
    for i, (s, d) in enumerate(zip(slides, durs)):
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{d + FADE:.2f}", "-i", str(s)]
        frames = int((d + FADE) * FPS)
        # slide 1080x1350 centrata, zoom dal 100% al 104%
        filters.append(
            f"[{i}:v]scale=1080:1350,setsar=1,"
            f"zoompan=z='1+0.04*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1350:fps={FPS},"
            f"pad={W}:{H}:0:(oh-ih)/2:color={BG},format=yuv420p,trim=duration={d + FADE:.2f},setpts=PTS-STARTPTS[v{i}]"
        )
    last, t = "v0", durs[0]
    for i in range(1, len(slides)):
        filters.append(f"[{last}][v{i}]xfade=transition=fade:duration={FADE}:offset={t:.2f}[x{i}]")
        last, t = f"x{i}", t + durs[i]
    total = sum(durs) + FADE
    n = len(slides)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs,
           "-f", "lavfi", "-t", f"{total:.2f}", "-i", "anullsrc=r=44100:cl=stereo",
           "-filter_complex", ";".join(filters),
           "-map", f"[{last}]", "-map", f"{n}:a",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-profile:v", "high",
           "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "128k",
           "-shortest", "-movflags", "+faststart", a.out]
    subprocess.run(cmd, check=True)
    cover = Path(a.out).with_name(Path(a.out).stem + "_cover.jpg")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(slides[0]),
                    "-vf", f"scale=1080:1350,pad={W}:{H}:0:(oh-ih)/2:color={BG}",
                    "-q:v", "2", str(cover)], check=True)
    print(f"{a.out} ({total:.1f} s) + {cover.name}")

if __name__ == "__main__":
    main()
