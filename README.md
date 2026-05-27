# traiterdr

## Statut

Base documentaire Markdown issue du traité `Traité de réduction des risques liés aux drogues — Tome 1`.

Extraction en cours, par blocs, avec séparation stricte entre :

- contenu source canonique ;
- thèmes transversaux à assembler ultérieurement ;
- dérivés CultureRDR candidats non validés ;
- substances seulement mentionnées ou traitées.

## Convention de pagination

Le document source a été vérifié avec la convention suivante :

```text
page PDF = page imprimée + 1
```

Exemple : page imprimée 8 = page PDF 9 ; page imprimée 15 = page PDF 16.

## État d'extraction

| Phase | Bloc | Pages imprimées | Pages PDF | Statut |
|---|---|---:|---:|---|
| Phase 0 | cadrage initial | 0-332 | 1-333 | terminé |
| Phase 1 | bloc 1 - front matter, suivi, table des matières, remerciements | 0-7 | 1-8 | extrait provisoire |
| Phase 1 | bloc 2 - introduction, objectif, publics, sources, cadre juridique | 8-15 | 9-16 | extrait provisoire |

## Prochaine étape

Bloc 3 : `01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes.md`, pages imprimées 16-28 / pages PDF 17-29.

## Indexation ChatGPT / IA

Point d'entrée recommandé pour les assistants IA : `llms.txt`.

Ordre de lecture conseillé :

1. `README.md`
2. `llms.txt`
3. `INDEX.md`
4. `00_pilotage/00_index_global.md`
5. `00_pilotage/03_index_notions.md`
6. `04_substances_mentions/00_index_substances.md`

Fichiers d'index disponibles :

- `INDEX.md` : index racine humain avec liens vers tous les fichiers indexables.
- `corpus_manifest.json` : manifeste machine-readable du corpus.

Pour ChatGPT, connecter ou ajouter le dépôt GitHub `PNP06/traiterdr`, puis demander explicitement d'utiliser `llms.txt` comme carte du corpus avant de lire les fichiers spécialisés.
