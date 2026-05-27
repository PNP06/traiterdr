# Décisions documentaires

## Statut
- décisions initiales, bloc 1 et bloc 2

| ID | Date | Décision | Justification | Portée | Impact | Statut |
|---|---|---|---|---|---|---|
| DD-001 | 2026-05-27 | Utiliser la convention `page PDF = page imprimée + 1`. | Le rendu PDF comporte 333 pages et la pagination imprimée va de 0 à 332. | Tous les fichiers de pilotage et source. | Toute citation interne doit donner les deux repères si utile. | active |
| DD-002 | 2026-05-27 | Limiter le bloc 1 aux pages imprimées 0-7 / PDF 1-8. | Bloc validé ainsi avant extraction. | `01_source_canonique/00_front_matter_suivi_remerciements.md`. | La note `A faire` de p. 8 est reportée au bloc 2. | active |
| DD-003 | 2026-05-27 | Conserver les notes de suivi et TODO comme statuts éditoriaux. | Elles font partie de la source, mais ne sont pas des faits scientifiques ou règles RDR. | Pages 0-1, 8 et blocs futurs. | Empêche la conversion automatique de brouillons en messages app. | active |
| DD-004 | 2026-05-27 | Conserver les remerciements dans la source canonique, sans les exploiter comme validation formelle. | Ils sont présents dans le traité et renseignent les zones relues ou discutées. | Page 7. | Préserve la trace documentaire tout en évitant une surinterprétation. | active |
| DD-005 | 2026-05-27 | Ne pas écrire dans GitHub depuis le connecteur actuel. | Le connecteur a renvoyé un README `CultureRDR` lors d'une lecture demandée sur `PNP06/traiterdr`. | Travail de dépôt. | Production locale en ZIP avec chemins exacts. | active |
| DD-006 | 2026-05-27 | Extraire uniquement l'image réellement disponible du bloc 1. | Pandoc a extrait l'image de dédicace ; les tableaux sont convertis en Markdown. | `05_assets_visuels/`. | Asset créé : `p001_figure_01_dedicace_image_koala.jpeg`. | active |
| DD-007 | 2026-05-27 | Intégrer la note `A faire` de p. 8 dans le bloc 2 comme TODO source. | La note est située sur la page imprimée 8, première page de l'introduction. | `01_source_canonique/01_introduction_cadre_objectif_sources.md` ; pages à relire. | Clarifie la frontière entre blocs 1 et 2. | active |
| DD-008 | 2026-05-27 | Extraire la figure prévention primaire/secondaire/tertiaire comme asset. | La figure porte une information structurante sur le positionnement du livre. | `05_assets_visuels/` ; index visuels ; fichier source bloc 2. | Asset créé : `p009_figure_01_preventions_primaire_secondaire_tertiaire.png`. | active |
| DD-009 | 2026-05-27 | Conserver les encadrés de lecture, définition et avertissement comme éléments informatifs. | Ils contiennent des consignes de lecture, une définition de périmètre et des limites juridiques. | Bloc 2 ; index visuels. | Les encadrés sont décrits et intégrés au contenu source. | active |
| DD-010 | 2026-05-27 | Traiter les références juridiques du bloc 2 comme contenu source, non comme avis juridique. | Le traité cite des articles et événements, mais l'extraction documentaire ne valide pas leur interprétation. | Cadre juridique, dérivés CultureRDR, no-go automation. | Toute exploitation app demande validation juridique ultérieure. | active |
| DD-011 | 2026-05-27 | Créer seulement des candidats CultureRDR de cadrage, pas des modules finaux. | Les consignes interdisent de produire modules, règles métier ou scores définitifs à ce stade. | `03_derives_culturerdr/`. | Les éléments ajoutés restent explicitement non validés. | active |
