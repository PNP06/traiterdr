# Variables App Candidates

## Statut
Candidats non validés.

## Méthode
Éléments dérivés du traité, à valider humainement avant toute intégration. Les variables ci-dessous servent à préparer une structuration documentaire, pas à personnaliser un conseil médical ou juridique.

## Éléments candidats

| ID | Domaine | Variable candidate | Type possible | Valeurs possibles | Source | Niveau de confiance | Limite | À ne pas faire |
|---|---|---|---|---|---|---|---|---|
| VAR-DOC-001 | traçabilité | `source_page_printed` | entier / plage | pages imprimées | bloc 1-2 | élevé | doit toujours être couplé au décalage PDF si citation interne | Ne pas confondre avec page PDF. |
| VAR-DOC-002 | traçabilité | `source_page_pdf` | entier / plage | page imprimée + 1 | bloc 1-2 | élevé | dépend du rendu PDF actuel | Ne pas l'utiliser seule si le traité est repaginé. |
| VAR-INTRO-001 | pédagogie | `prevention_level` | enum | primaire ; secondaire ; tertiaire | p. 9 | élevé pour le cadrage | un contenu peut toucher plusieurs niveaux | Ne pas déduire le niveau de risque individuel. |
| VAR-INTRO-002 | pédagogie | `target_audience` | enum multi-valeur | consommateur ; entourage ; association ; travailleur social ; clinicien ; scientifique ; journaliste | p. 10-11 | moyen | segmentation documentaire seulement | Ne pas personnaliser un avis médical. |
| VAR-INTRO-003 | navigation | `reading_mode` | enum | rapide_encadres ; intermediaire_titres_violets ; approfondi_parties_1_2 | p. 11 | moyen | `titres violets` à repérer dans la source | Ne pas masquer les limites ou sources en mode rapide. |
| VAR-INTRO-004 | qualité documentaire | `source_type` | enum | publication scientifique ; association ; média ; texte juridique ; source institutionnelle ; note auteur | p. 12-15 | moyen | typologie à définir en phase 2 | Ne pas hiérarchiser automatiquement sans méthodologie. |
| VAR-INTRO-005 | cadre légal | `legal_context_required` | booléen | oui / non | p. 13-15 | élevé pour les contenus juridiques | dépend du pays, de la date et du contexte d'usage | Ne pas produire d'avis juridique. |
| VAR-INTRO-006 | statut contenu | `not_a_prescription` | booléen | vrai pour contenus RDR généraux | p. 15 | élevé pour cadrage | formulation UX/juridique à valider | Ne pas promettre une absence de risque. |
