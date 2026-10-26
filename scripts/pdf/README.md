# Retouches du PDF du traité

Le PDF publié (`public/traite-rdr.pdf`) part de l'export PDF du fichier Word du traité, puis passe par ces retouches :

1. `build.py` : couverture RISKY et page de version (`cover.html`, `version.html`, imprimées en PDF par `render.cjs`), signature remplacée par @risky.asso, retrait des notes de travail et des pages vides de fin, en-têtes corrigés, signets construits depuis le sommaire, métadonnées, compression des images.
2. `subset_emoji.py` : réduit la police Segoe UI Emoji que Word intègre en entier (3,7 Mo) aux seuls glyphes utilisés.
3. `jpeg_flate.py` : réencode en JPEG les images qui y gagnent beaucoup, puis optimise le fichier pour le web.

```sh
pip install pymupdf pikepdf fonttools pillow
node render.cjs cover version   # produit cover.pdf et version.pdf
python3 build.py export-word.pdf cover.pdf version.pdf etape1.pdf
python3 subset_emoji.py etape1.pdf etape2.pdf
python3 jpeg_flate.py etape2.pdf ../../public/traite-rdr.pdf
```

Les zones retirées et les en-têtes corrigés sont repérés par numéro de page dans `build.py` : à revoir à chaque nouvel export Word si la pagination change.
