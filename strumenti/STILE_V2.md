# Stile grafico v2 (dal 27/11/2026) — allineato a lucacrudi.com

Da usare per TUTTI i nuovi post di @crudiluca. Lo stile scuro dei post 001–013 (fondo #0b0b0c, Crimson Text) non si usa più.

## Palette e font (dal sito)
- Carta #F5F2EB, carta 2 #E9E3D6, oro #B08A47, rosso #B92D35, inchiostro #171B1D
- Titoli: Barlow Condensed Bold, maiuscolo (sostituto di Limes Display)
- Testo: EB Garamond; frase rossa in EB Garamond corsivo
- Firma: LUCA CRUDI (Barlow Condensed SemiBold, spaziato) + @crudiluca in oro
- Formato 1080×1350

## Modulo: `strumenti/stile_v2.py` (font in `strumenti/fonts/`)
- `photo_cover(foto, rubrica, numero, kicker, titolo, frase_rossa, credito)` — copertina: foto d'archivio in alto (800 px, viraggio caldo e vignettatura), filo rosso, titolo su carta
- `photo_text_slide(foto, ritaglio, rubrica, numero, etichetta, sotto, testo, page="2/8", quote=False, credit=...)` — slide con dettaglio fotografico in alto e testo sotto (per l'Istruttoria: un dettaglio per ogni personaggio)
- `text_slide(...)` — solo carta, per la domanda finale
- Rubriche: «ISTRUTTORIA» o «CURIOSITÀ DISTURBANTE», numerazione progressiva da ARCHIVIO.md

## Foto
- Solo immagini reali d'archivio, di pubblico dominio o con licenza libera, da Wikimedia Commons: trovare la pagina del file con firecrawl_search (`site:commons.wikimedia.org …`), scaricare da upload.wikimedia.org con un User-Agent descrittivo (es. `crudiluca-media/1.0 (github.com/lucacrudi-droid/media)`), poche richieste distanziate. Se risponde 429, attendere qualche minuto e riprovare; non usare altri percorsi.
- Verificare licenza e autore sulla pagina Commons; credito sempre visibile sulla foto (es. «Foto Harry Burton, 1922 · pubblico dominio» o «NASA/ESA · pubblico dominio») e ripetuto in didascalia.
- Foto di Luca solo se le manda lui. Mai foto di persone ritratte da paparazzi o materiale protetto.
- Archiviare le foto originali usate nella cartella del mese, sottocartella `foto/`, con un file `crediti.txt`.

## Controllo
Prima di consegnare: aprire ogni immagine, niente testo che sborda, crediti leggibili, almeno una foto coerente per slide dove possibile.
