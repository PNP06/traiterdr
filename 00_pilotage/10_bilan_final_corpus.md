# Bilan final corpus documentaire

## Statut
- Phase 1 source canonique : terminee provisoirement.
- Phase 1.5 controle qualite : terminee provisoirement.
- Phase 2 themes transversaux : assemblee provisoirement.
- Phase 3 derives CultureRDR : candidats non valides produits.
- Phase 4 indexation IA : terminee provisoirement.

## Couverture

| Couche | Nombre | Statut |
|---|---:|---|
| Fichiers source canonique | 22 | couverture p. 0-332 / PDF 1-333 |
| Themes transversaux | 27 + index | assembles depuis sources canoniques |
| Fichiers derives CultureRDR | 11 | candidats non valides |
| Assets visuels publies | 97 | controles automatiquement, relire visuellement si usage final |
| Manifest indexable | 1 | `corpus_manifest.json` regenere |
| Fichiers substances | 13 + index | finalises en fiches documentaires provisoires, sans monographie abusive |

## Controle final

- Themes avec placeholder documentaire non rempli : 0.
- Derives avec placeholder documentaire non rempli : 0.
- Substances avec placeholder documentaire non rempli : 0.
- Audit du prompt initial : `00_pilotage/11_audit_prompt_initial.md`.
- Sources lourdes PDF/DOCX : conservees localement, ignorees par Git.
- HTML brut Word : conserve localement dans `sources/traite/raw_html_export/`, ignore par Git.

## Ordre de lecture IA recommande

1. `README.md`
2. `llms.txt`
3. `00_pilotage/00_index_global.md`
4. `00_pilotage/08_bilan_phase1.md`
5. `00_pilotage/09_controle_qualite_phase1.md`
6. `01_source_canonique/`
7. `02_themes_transversaux/00_index_themes.md`
8. `03_derives_culturerdr/00_index_derives.md`
9. `04_substances_mentions/00_index_substances.md`

## Limites avant integration CultureRDR

- Relire les assets et les points ouverts de `00_pilotage/06_pages_a_relire.md`.
- Relire les fiches substances avant toute transformation en contenu CultureRDR final.
- Valider medicalement, scientifiquement, juridiquement et UX les derives avant usage.
- Ne pas transformer les candidats en scores, modules ou messages finaux sans revue humaine.
