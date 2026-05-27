# Règles métier candidates

## Statut
Candidats non validés.

## Méthode
Éléments dérivés du traité, à valider humainement avant intégration. Les règles ci-dessous sont des règles de cadrage documentaire et UX, non des règles de décision médicale, toxicologique ou juridique.

| ID | Domaine | Règle candidate | Déclencheur possible | Données nécessaires | Message possible | Source | Niveau de confiance | Limite | À ne pas faire |
|---|---|---|---|---|---|---|---|---|---|
| R-CADRAGE-001 | cadrage contenu | Tout contenu issu du traité doit être présenté comme information de réduction des risques, non comme incitation ni prescription. | Ouverture d'un module ou affichage d'une fiche issue du traité | type de contenu ; statut de validation ; source | `Information de réduction des risques : ne remplace pas un avis médical ou juridique.` | p. 15 | élevé pour le principe | Formulation finale à valider juridiquement et UX. | Ne pas promettre protection légale ou médicale. |
| R-PREVENTION-001 | pédagogie | Classer les contenus généraux du traité en prévention secondaire par défaut, sauf chapitre explicitement tertiaire ou urgence. | Indexation d'un module général | fichier source ; chapitre ; niveau de prévention | `Objectif : comprendre et réduire les risques, pas moraliser.` | p. 9-10 | moyen | Les chapitres overdose, sevrage ou addiction peuvent relever d'autres niveaux. | Ne pas assimiler prévention secondaire à usage sans risque. |
| R-SOURCES-001 | qualité documentaire | Toute fiche issue du traité doit conserver les sources et limites lorsqu'elles existent. | Création d'une fiche Académie, message long ou résumé | références ; page ; type de source ; limites | `Sources et limites à vérifier avant application.` | p. 12, p. 15 | moyen | Le traité ne fournit pas encore une grille complète de niveau de preuve. | Ne pas produire de règle métier sans source canonique. |
| R-LEGAL-001 | juridique | Les contenus mentionnant substances illégales, facilitation ou provocation doivent déclencher une revue juridique avant publication externe. | Contenu avec termes `illégal`, `stupéfiant`, `facilitation`, `provocation`, `présentation favorable` | pays ; date ; contenu exact ; public visé | `Ce contenu nécessite validation juridique avant diffusion.` | p. 13-15 | élevé pour le besoin de revue | La revue juridique n'est pas réalisée dans cette extraction. | Ne pas générer un avis juridique automatique. |
