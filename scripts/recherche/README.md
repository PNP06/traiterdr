# Index de la page Rechercher

La page `/recherche` cherche dans `public/recherche-index.json`, fabriqué à partir du PDF :

    python3 scripts/recherche/build_index.py

À relancer après chaque nouvelle version de `public/traite-rdr.pdf` (il faut `pdftotext` de poppler et `pypdf`), puis commiter le JSON.

- Le texte est lu page par page dans la colonne de texte (sans les onglets ni l'en-tête courant).
- Les parties (A.1, G.7.4…) viennent des signets du PDF.
- Les thèmes et produits se règlent dans `themes.json` : `sections` liste les codes de parties du thème (le script s'arrête si un code n'existe plus), `mots` les mots cherchés, exacts sauf s'ils finissent par `*`.

Liens partageables (bio Instagram, légendes) : `/recherche?q=ghb`, `/recherche?theme=overdose`, `/recherche?produit=alcool`.
