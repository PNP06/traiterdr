# traiterdr

## Statut

Base documentaire Markdown issue du traite `Traite de reduction des risques lies aux drogues - Tome 1`.

Extraction Phase 1 source canonique terminee provisoirement, avec separation stricte entre :

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
| Phase 1 | bloc 7 - sucre/naturel/reste perche/contact/addiction | 70-90 | 71-91 | extrait provisoire |
| Phase 1 | bloc 8 - GHB/drogue du viol/chemsex/3-MMC/RC-NPS | 91-98 | 92-99 | extrait provisoire |
| Phase 1 | bloc 9 - gestion des risques | 99-102 | 100-103 | extrait provisoire |
| Phase 1 | bloc 10 - cerveau/synapses/neurotransmetteurs/circuits | 103-114 | 104-115 | extrait provisoire |
| Phase 1 | bloc 11 - tolerance/developpement 15-25/corps humain | 115-125 | 116-126 | extrait provisoire |
| Phase 1 | bloc 12 - PK/PD/ADME | 126-139 | 127-140 | extrait provisoire |
| Phase 1 | bloc 13 - psychologie/placebo/nocebo/troubles psychologiques | 140-156 | 141-157 | extrait provisoire |
| Phase 1 | bloc 14 - classifications substances | 157-181 | 158-182 | extrait provisoire |
| Phase 1 | bloc 15 - risques generiques sommeil/juridique | 182-184 | 183-185 | extrait provisoire |
| Phase 1 | bloc 16 - sexualite/vulnerabilite/consentement | 185-197 | 186-198 | extrait provisoire |
| Phase 1 | bloc 17 - allergie/convulsions/hydratation/thermie | 198-222 | 199-223 | extrait provisoire |
| Phase 1 | bloc 18 - badtrip/overdose | 223-247 | 224-248 | extrait provisoire |
| Phase 1 | bloc 19 - interactions/melanges | 248-267 | 249-268 | extrait provisoire |
| Phase 1 | bloc 20 - testing/analyses produits/biologie | 268-293 | 269-294 | extrait provisoire |
| Phase 1 | bloc 21 - descente/sevrage/addiction/dependance/cancer | 294-332 | 295-333 | extrait provisoire |

## Prochaine etape

Phase 1 source canonique terminee. Bilan provisoire : `00_pilotage/08_bilan_phase1.md`. Prochaine etape proposee : Phase 2 themes transversaux, sans demarrage automatique.

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
