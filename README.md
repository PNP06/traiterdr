# traiterdr

## Statut

Base documentaire Markdown issue du traite `Traite de reduction des risques lies aux drogues - Tome 1`.

Extraction Phase 1 source canonique en cours, par blocs, avec separation stricte entre :

- contenu source canonique ;
- themes transversaux a assembler ulterieurement ;
- derives CultureRDR candidats non valides ;
- substances seulement mentionnees ou traitees.

## Convention de pagination

Le document source a ete verifie avec la convention suivante :

```text
page PDF = page imprimee + 1
```

Exemple : page imprimee 45 = page PDF 46 ; page imprimee 51 = page PDF 52.

## Etat d'extraction

| Phase | Bloc | Pages imprimees | Pages PDF | Statut |
|---|---|---:|---:|---|
| Phase 0 | cadrage initial | 0-332 | 1-333 | termine |
| Phase 1 | bloc 1 - front matter, suivi, table des matieres, remerciements | 0-7 | 1-8 | extrait provisoire |
| Phase 1 | bloc 2 - introduction, objectif, publics, sources, cadre juridique | 8-15 | 9-16 | extrait provisoire |
| Phase 1 | bloc 3 - mythes, croyances, heuristiques, biais, sophismes | 16-28 | 17-29 | extrait provisoire |
| Phase 1 | bloc 4 - mecanismes de protection psychologique et approche RDR | 29-44 | 30-45 | extrait provisoire |
| Phase 1 | bloc 5 - comprendre la science, preuves, causalite, methode scientifique | 45-51 partielle | 46-52 partielle | extrait provisoire |
| Phase 1 | bloc 6 - alcool/tabac/sante publique/prix | 51-69 | 52-70 | extrait provisoire |

## Prochaine etape

Bloc 7 : `01_source_canonique/06_mythes_sucre_naturel_reste_perche_contact_addiction.md`, pages imprimees 70-90 / pages PDF 71-91.

## Indexation ChatGPT / IA

Point d'entree recommande pour les assistants IA : `llms.txt`.

Ordre de lecture conseille :

1. `README.md`
2. `llms.txt`
3. `INDEX.md`
4. `00_pilotage/00_index_global.md`
5. `00_pilotage/03_index_notions.md`
6. `sources/traite/traite_rdr_version_html_clean.md`
7. `04_substances_mentions/00_index_substances.md`

Fichiers d'index disponibles :

- `INDEX.md` : index racine humain avec liens vers tous les fichiers indexables.
- `corpus_manifest.json` : manifeste machine-readable du corpus.
- `sources/traite/rapport_nettoyage_html.md` : diagnostic du HTML Word source et de sa conversion Markdown.

Pour ChatGPT, connecter ou ajouter le depot GitHub `PNP06/traiterdr`, puis demander explicitement d'utiliser `llms.txt` comme carte du corpus avant de lire les fichiers specialises.
