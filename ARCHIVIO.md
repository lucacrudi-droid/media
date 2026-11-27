# Archivio post Instagram @crudiluca

Ogni post viene creato solo dopo il via libera di Luca e archiviato qui, nel ramo `proposte/post-2026-11-20`.

## Struttura
- `post-AAAA-MM/` — una cartella per mese (es. `post-2026-11`, `post-2026-12`)
  - `NN_tema.png` oppure `NN_tema_1.png … NN_tema_N.png` (caroselli), 1080×1350
  - `didascalia_NN_tema.txt` — testo, fonti, hashtag, data di pubblicazione
  - `build_*.py` — script che rigenera le grafiche (Playwright, font Crimson Text e Inter)
- `2026/` — post pubblicati prima di questo archivio (001–005)
- `strumenti/build_reel.py` — trasforma le grafiche 1080×1350 di un post in un Reel verticale 1080×1920 (zoom lento, dissolvenze, traccia audio muta; musica aggiunta da Metricool) più copertina. Dal 27/11/2026 i Reel si archiviano come `NN_tema_reel.mp4` e `NN_tema_reel_cover.jpg` nella cartella del mese.

## Indice
| N. | Data pubblicazione | Tema | File |
|---|---|---|---|
| 006 | 26/11/2026 | Carter 1922, la porta sigillata (carosello 3: grafica + 2 foto Burton) | post-2026-11/06_carter.png, 06_carter_2.png, 06_carter_3.png |
| 007 | 20/11/2026 (extra) | Voyager 1 a un giorno-luce | post-2026-11/07_voyager.png |
| 008 | 24/11/2026 18:30 | Filo spinato, brevetto Glidden 24/11/1874 | post-2026-11/08_filospinato.png |
| 009 | 27/11/2026 18:30 | Istruttoria «27 novembre»: Nobel 1895, Mars 2 1971, Osiride 2001 (carosello 9 slide, musica da aggiungere in app) | post-2026-11/09_27novembre_1…9.png, didascalia_09_27novembre.txt |
| 010 | 01/12/2026 18:30 | Istruttoria «1° dicembre: Antartide»: Trattato Antartico 1959, Bouvet 1927, Blood Falls (carosello 8 slide con mappa polare, musica da aggiungere in app) | post-2026-12/10_antartide_1…8.png, mappa_antartide.png, didascalia_10_antartide.txt, build_antartide.py (argomento: cartella dati Natural Earth) |
| 011 | 30/11/2026 18:30 | Mark Twain e la cometa di Halley (immagine singola, musica da aggiungere in app) | post-2026-11/11_twain.png, didascalia_11_twain.txt, build_twain.py |
| 012 | 02/12/2026 18:30 | Istruttoria «Il navigatore italiano»: Chicago Pile-1, 2/12/1942 (carosello 7 slide, musica da aggiungere in app) | post-2026-12/12_pila_1…7.png, didascalia_12_pila.txt, build_pila.py |
| 013 | 26/11/2026 14:15 (extra di tendenza) | Dimorphos: il cratere lasciato da DART, prime immagini di Hera (ESA, 25/11/2026) (immagine singola, senza musica) | post-2026-11/13_dimorphos.png, didascalia_13_dimorphos.txt, build_dimorphos.py |
