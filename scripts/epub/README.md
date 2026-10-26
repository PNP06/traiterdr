# Version liseuse (EPUB)

Le fichier publié est `public/traite-rdr.epub`. Il part du même HTML que le PDF (`scripts/pdf/refonte/`), donc du fichier Word du traité : même texte, mêmes corrections, même numérotation des titres.

```sh
# étapes 1 à 3 de scripts/pdf/refonte/README.md : traite.docx -> prep.html -> traite.html
node scripts/epub/couverture.cjs couverture.jpg          # couverture du PDF en image
python3 scripts/epub/build_epub.py traite.html couverture.jpg public/traite-rdr.epub
java -jar epubcheck.jar public/traite-rdr.epub          # facultatif : vérification (EPUBCheck 5)
```

Il faut `traite.html` et son dossier `media/` côte à côte. Le script découpe un fichier par chapitre, fait de chaque note une note cliquable en fin de chapitre, réduit les images (1200 px max.) et reprend la page de version du PDF (`scripts/pdf/version.html`).

À refaire à chaque nouveau PDF, pour que les deux versions restent identiques.
