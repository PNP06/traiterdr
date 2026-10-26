# Refonte complète du PDF (gabarit de la maquette de l'Introduction)

Source : le fichier Word du traité (non versionné). Chaîne :

1. `python3 prep_docx.py traite.docx prep.docx` : retire les notes de travail, marque les encadrés et les schémas Word.
2. `pandoc -f docx+styles prep.docx -t html --extract-media=. -o prep.html`
3. `python3 build_html.py prep.html traite.html [corrections.json]` : applique le gabarit (`gabarit.css`, `page.html`, `debut.html`, `remplacements/`).
4. `python3 split_parts.py traite.html parts/` puis `node render.cjs parts/0*.html` (paged.js + Chromium, une partie à la fois ; copier `koala.jpg` et lier `media/` dans `parts/`).
5. `python3 assemble.py parts/ cover.pdf version.pdf traite.pdf` : sommaire, numéros de page, signets, métadonnées.
6. `python3 check_text.py prep.html traite.pdf` : liste les suites de mots du Word absentes du PDF (les tableaux sortent souvent en faux positifs, l'ordre des cellules change).

Plan de travail et journal : `Traité/00_pilotage/14_plan_refonte_pdf.md`.

Après chaque nouveau PDF publié dans `public/traite-rdr.pdf`, relancer `python3 scripts/recherche/build_index.py` pour mettre à jour la page Rechercher.
