# Audit du prompt initial

## Statut
- audit documentaire realise le 2026-05-27
- source locale consultee : `sources/prompt initial.html`
- export HTML brut et assets UI conserves localement, ignores par Git

## Synthese

Le prompt initial demandait de transformer le traite en base documentaire Markdown structuree, tracable et exploitable par CultureRDR, Codex ou d'autres IA, sans creer d'application, de score, de regles finales, de modules finaux ou de recommandations non sourcees. Le corpus actuel couvre cette demande de facon provisoire et documentaire.

## Exigences et statut

| Exigence du prompt initial | Statut dans le repo | Preuve / fichier |
|---|---|---|
| Phase 0 : cadrage, pagination, lisibilite, sommaire, arborescence | realise | `00_pilotage/00_index_global.md`, `00_pilotage/08_bilan_phase1.md` |
| Phase 1 : source canonique complete par blocs | realise provisoirement | `01_source_canonique/` ; couverture p. 0-332 / PDF 1-333 |
| Maintenir matrice, index visuels, notions, glossaire, journal, pages a relire | realise provisoirement | `00_pilotage/01_matrice_couverture.md` a `00_pilotage/07_decisions_documentaires.md` |
| Extraire/decrire les visuels informatifs | realise provisoirement | `05_assets_visuels/`, `00_pilotage/02_index_visuels_tableaux_figures.md`, `00_pilotage/09_controle_qualite_phase1.md` |
| Phase 2 : themes transversaux apres source canonique | realise provisoirement | `02_themes_transversaux/00_index_themes.md` et 27 themes |
| Phase 3 : derives CultureRDR candidats non valides | realise provisoirement | `03_derives_culturerdr/00_index_derives.md` |
| Ne pas creer de code applicatif, backend, migrations, secrets ou `.env` | respecte | aucun fichier applicatif ajoute ; corpus documentaire uniquement |
| Ne pas transformer en score, module final ou regle metier validee | respecte | derives marques candidats non valides ; no-go dans `03_derives_culturerdr/08_no_go_automation.md` |
| Sources lourdes et brutes locales non versionnees | respecte apres cette passe | `.gitignore` ignore PDF/DOCX, HTML Word brut et export prompt initial |
| Fichiers substances : ne remplir que si matiere suffisante, sinon indexer | ecart detecte puis a corriger | squelettes dans `04_substances_mentions/` avant cloture ; finalisation prevue dans cette passe |

## Ecarts identifies

| Ecart | Impact | Correction prevue / realisee |
|---|---|---|
| `04_substances_mentions/*.md` encore en squelette | Le prompt demandait que les fichiers substances ne restent pas vides si une mention exploitable existe. | Remplacer les squelettes par des fiches provisoires sourcees, sans monographie abusive. |
| `sources/prompt initial.html` et `sources/prompt initial_files/` non suivis mais non ignores | Bruit Git et risque d'indexer un export ChatGPT UI au lieu d'un document utile. | Ajout a `.gitignore`; conservation locale uniquement. |
| Bilan final ne comptait pas les squelettes substances | Risque de croire le corpus totalement clos alors que la couche substances restait incomplete. | Mettre a jour `00_pilotage/10_bilan_final_corpus.md` apres finalisation substances. |

## Decision documentaire

- L'export HTML du prompt initial n'est pas un livrable documentaire : il sert seulement de controle local.
- Le corpus versionne doit rester centre sur Markdown propre, sources canoniques, themes, derives candidats, substances et pilotage.
- Les fiches substances restent provisoires : aucune connaissance externe n'est ajoutee et aucune monographie complete n'est creee si le traite ne fournit pas assez de matiere.
