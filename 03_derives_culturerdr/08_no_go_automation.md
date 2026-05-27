# No-go automation

## Statut
Candidats non validés.

## Méthode
Ces éléments sont dérivés du traité et nécessitent une validation humaine avant intégration.

## Éléments candidats issus du bloc 1

| ID | Domaine | À ne pas automatiser | Source | Justification | Statut |
|---|---|---|---|---|---|
| NO-GO-DOC-001 | documentation | Ne pas transformer les notes de suivi (`testing`, `taux de conversion`, `Reprendre science`, `placebo`) en faits scientifiques ou messages utilisateur. | pages 0-1 | Ce sont des statuts éditoriaux ou notes isolées. | actif |
| NO-GO-DOC-002 | modules Académie | Ne pas créer de modules à partir de la table des matières seule. | pages 4-7 | Une entrée de TOC n'est pas un contenu source suffisant. | actif |
| NO-GO-DOC-003 | personnes citées | Ne pas utiliser les remerciements comme preuve de validation scientifique formelle ou comme contenu app. | page 7 | Les remerciements signalent des échanges/relectures, pas un protocole de validation. | actif |

## Éléments candidats issus du bloc 2

| ID | Domaine | À ne pas automatiser | Source | Justification | Statut |
|---|---|---|---|---|---|
| NO-GO-INTRO-001 | diagnostic / addiction | Ne pas déduire automatiquement qu'un utilisateur relève d'un `usage simple` ou qu'il n'a pas de trouble de l'usage. | pages 9-10 | Le traité décrit une catégorie générale ; aucun diagnostic individuel n'est possible. | actif |
| NO-GO-INTRO-002 | ton RDR | Ne pas transformer l'absence de moralisation en banalisation ou en validation de la consommation. | page 10 | La posture vise la compréhension des risques, pas leur suppression. | actif |
| NO-GO-INTRO-003 | juridique | Ne pas utiliser l'encadré légal du traité comme protection juridique de CultureRDR. | page 15 | Un avertissement source ne remplace pas une revue juridique d'application. | actif |
| NO-GO-INTRO-004 | juridique | Ne pas produire automatiquement d'avis juridique à partir des articles L3421-4, L3411-8 ou 122-4. | pages 13-14 | L'interprétation dépend du contexte, de la date, du pays et de la formulation exacte du contenu. | actif |
| NO-GO-INTRO-005 | recommandations | Ne pas présenter des résumés RDR comme prescriptions garantissant l'absence de problème. | page 15 | Le traité indique explicitement que les résumés ne sont pas des prescriptions et n'évitent pas de façon certaine les problèmes. | actif |
| NO-GO-INTRO-006 | scoring | Ne pas créer de score RDR à partir du seul positionnement en prévention secondaire. | pages 9-10 | Le bloc ne fournit ni pondération, ni seuil, ni variables individuelles suffisantes. | actif |
| NO-GO-INTRO-007 | sources | Ne pas considérer une relecture par professionnels de santé comme une certification médicale formelle. | page 12 | La source mentionne des relectures, sans protocole ni validation formelle. | actif |
| NO-GO-INTRO-008 | actualité juridique/institutionnelle | Ne pas intégrer les éléments CND/ONU 2024 sans vérification si affichés publiquement. | pages 14-15 | L'extraction conserve la source, mais ne vérifie pas l'actualité ou la formulation institutionnelle. | actif |


## Éléments candidats issus du bloc 3

| ID | Domaine | À ne pas automatiser | Source | Justification | Statut |
|---|---|---|---|---|---|
| NO-GO-COG-001 | UX / communication | Ne pas dire directement à l'utilisateur `tu es biaisé` ou `c'est un sophisme`. | pages 21-28 | Ces formulations peuvent déclencher défensive et déplacement du débat ; préférer des questions de méthode. | actif |
| NO-GO-COG-002 | scoring | Ne pas créer un score cognitif ou score de rationalité à partir des heuristiques/biais/sophismes. | pages 18-28 | Le bloc fournit une grille d'analyse, pas une échelle validée. | actif |
| NO-GO-COG-003 | risque individuel | Ne pas déduire un niveau de risque individuel du seul manque de dose/fréquence/contexte dans une phrase. | pages 19-20 | L'absence de paramétrage signale une information insuffisante, pas un risque quantifié. | actif |
| NO-GO-COG-004 | preuves | Ne pas figer une hiérarchie de preuves avant extraction du bloc `Comprendre la science`. | pages 21-22 | Le bloc donne des repères, mais la méthodologie science/preuves est prévue ensuite. | actif |
| NO-GO-COG-005 | naturalité | Ne pas transformer `naturel ≠ sûr` en `naturel = dangereux`. | pages 17, 19, 25 | Le traité dit que l'origine naturelle ne suffit pas ; il ne pose pas l'inverse. | actif |
| NO-GO-COG-006 | témoignages | Ne pas invalider automatiquement l'expérience vécue au motif qu'elle n'est pas une preuve scientifique. | pages 26-28 | L'expérience peut éclairer les pratiques, mais ne suffit pas à établir une règle générale. | actif |
| NO-GO-COG-007 | données chiffrées | Ne pas transformer les exemples pédagogiques de risque absolu en seuils ou statistiques génériques. | page 22 | Les chiffres doivent être vérifiés, sourcés et contextualisés. | actif |

## Complements Phase 3 depuis themes transversaux

| ID | Domaine | No-go | Source | Niveau de confiance | Limite |
|---|---|---|---|---|---|
| NOGO-P3-001 | global | Ne pas presenter les themes comme validation scientifique finale. | `02_themes_transversaux/00_index_themes.md` | eleve | validation humaine requise |
| NOGO-P3-002 | scoring | Ne pas calculer de score RDR global depuis les seuls themes. | `03_derives_culturerdr/05_scoring_implications.md` | eleve | scoring hors phase |
| NOGO-P3-003 | urgence | Ne pas remplacer secours, avis medical ou cadre legal. | themes 18, 19, 21 | eleve | messages urgence a valider |
