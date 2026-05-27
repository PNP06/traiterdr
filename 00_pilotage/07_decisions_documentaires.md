# Décisions documentaires

## Statut
- décisions initiales, blocs 1, 2, 3, 4 et 5

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
| DD-012 | 2026-05-27 | Utiliser `sources/traite/traite_rdr_version_html_clean.md` comme aide d'extraction, sans remplacer la traçabilité par pages. | Le dépôt contient désormais une version Markdown nettoyée du traité, plus facile à exploiter, mais la pagination imprimée/PDF reste la référence de couverture. | Tous les blocs suivants. | Accélère l'extraction tout en maintenant les pages sources. | active |
| DD-013 | 2026-05-27 | Arrêter le bloc 3 avant `Mécanisme de protection psychologique`. | La table des matières sépare `Heuristique/Biais/Sophisme` de `Mécanisme de protection psychologique`; le fichier cible du bloc 3 ne doit pas absorber le bloc suivant. | `01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes.md`. | Le bloc 4 commencera par les mécanismes de protection psychologique. | active |
| DD-014 | 2026-05-27 | Extraire les trois infographies heuristiques, biais cognitifs et sophismes comme assets. | Elles portent une information pédagogique structurante, non décorative. | `05_assets_visuels/` ; index visuels ; fichier source bloc 3. | Assets créés : `p020_figure_01_heuristiques.png`, `p022_figure_01_biais_cognitifs.png`, `p028_figure_01_sophismes.png`. | active |
| DD-015 | 2026-05-27 | Ne pas écrire dans GitHub via les actions `create_file`/`update_file` tant que le routage API renvoie `CultureRDR`. | La lecture par URL GitHub accède bien à `traiterdr`, mais les outils repository_full_name restent liés à `CultureRDR`. | Travail GitHub. | Livraison sous forme d'archive de changements et de patch, sans commit direct. | active |
| DD-016 | 2026-05-27 | Harmoniser localement les blocs 4 et 5 ajoutés via GitHub avant de poursuivre. | Les sources canoniques avaient été ajoutées sur GitHub, mais les fichiers de pilotage, assets nommés et manifestes devaient être remis en cohérence. | `01_source_canonique/03_mecanismes_protection_approche_rdr.md` ; `01_source_canonique/04_comprendre_science_preuves_causalite.md` ; `00_pilotage/` ; `05_assets_visuels/`. | Le travail futur doit repartir de l'état local harmonisé. | active |
| DD-017 | 2026-05-27 | Publier uniquement les visuels utiles sous noms stables, pas le dossier HTML brut. | L'export Word HTML contient des noms génériques et des artefacts ; les visuels utiles doivent être sélectionnés et renommés. | `sources/traite/raw_html_export/` ; `05_assets_visuels/`. | Le brut reste ignoré ; les assets publiés sont ceux référencés par les index. | active |

## Bloc 6

- Bloc 6 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.

## Bloc 7

- Bloc 7 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.

## Bloc 8

- Bloc 8 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.

## Bloc 9

- Bloc 9 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.

## Bloc 10

- Bloc 10 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.

## Bloc 11

- Bloc 11 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.

## Bloc 12

- Bloc 12 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.

## Bloc 13

- Bloc 13 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.

## Bloc 14

- Bloc 14 : extraction source canonique conservee au plus pres du Markdown nettoye ; les assets raster nouveaux sont nommes de facon stable ; les fichiers PDF/DOCX restent locaux via `.gitignore`.
