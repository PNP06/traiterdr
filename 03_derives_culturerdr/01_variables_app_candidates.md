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
| VAR-COG-001 | croyances | `belief_type` | enum | mythe ; heuristique ; biais ; sophisme ; défense psychologique ; incertain | p. 18 | moyen | classification délicate, possiblement contextuelle | Ne pas étiqueter directement l'utilisateur. |
| VAR-COG-002 | qualité raisonnement | `risk_statement_has_dose` | booléen | oui / non / incertain | p. 19-20 | moyen | détection automatique fragile | Ne pas conclure qu'une affirmation est fausse. |
| VAR-COG-003 | qualité raisonnement | `risk_statement_has_frequency_or_duration` | booléen | oui / non / incertain | p. 19-20 | moyen | ne suffit pas à évaluer le risque | Ne pas calculer un score sans validation. |
| VAR-COG-004 | qualité raisonnement | `risk_statement_has_effect` | booléen | oui / non / incertain | p. 19-20 | moyen | effet discuté à normaliser | Ne pas remplacer une expertise toxicologique. |
| VAR-COG-005 | qualité raisonnement | `risk_statement_context_tags` | liste | conduite ; fatigue ; mélanges ; âge ; médicaments ; comorbidités ; isolement ; chaleur ; autre | p. 19-20 | moyen | liste à enrichir dans futurs blocs | Ne pas supposer le contexte si non déclaré. |
| VAR-COG-006 | argumentation | `argument_red_flags` | liste | donc ; forcément ; toujours ; jamais ; sans danger ; c'est prouvé | p. 23-28 | moyen | risque de faux positifs | Ne pas classer automatiquement en sophisme. |
| VAR-COG-007 | preuve | `evidence_level_hint` | enum | anecdote ; étude isolée ; méta-analyse ; expertise collective ; consensus ; inconnu | p. 21-22 | faible à moyen | attendre bloc science pour méthodologie | Ne pas hiérarchiser définitivement avant validation. |
| VAR-COG-008 | communication risque | `risk_format` | enum | relatif ; absolu ; fréquence naturelle ; non quantifié | p. 22 | moyen | chiffres à sourcer | Ne pas transformer un exemple en seuil. |
