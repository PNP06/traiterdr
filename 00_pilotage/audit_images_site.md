# Audit des images du site VitePress

Date de contrôle : 2026-05-31.

## Méthode

- Recherche dans les fichiers Markdown publiés : `<img>`, `<figure>` et `![]()`.
- Contrôle complémentaire du composant d'accueil `.vitepress/theme/components/RiskHome.vue`.
- Croisement avec `05_assets_visuels/README.md`, `00_pilotage/02_index_visuels_tableaux_figures.md`, le nom de fichier et le contexte du chapitre.
- Contrôle des chemins locaux par résolution relative depuis chaque fichier source.

## Résultat synthétique

- Références Markdown publiées recensées : 111.
- Fichiers Markdown publiés contenant des images : 20 (`figures.md` et 19 chapitres canoniques).
- Images distinctes affichées dans les Markdown publiés : 95.
- Chemins cassés détectés : 0.
- Pages contrôlées sans figure de traité affichée : `index.md`, `themes.md`, `sommaire.md`, `substances.md`, `lire.md`, `essentiels.md`, `pdf.md`.
- Accueil : `RiskHome.vue` affiche uniquement le logo `/risky-logo.png`, hors figure scientifique.
- Images de classification des substances : présentes uniquement dans `01_source_canonique/13_classifications_substances.md` et dans la galerie `figures.md`.

## Corrections effectuées

| Fichier | Image | Problème | Correction |
|---|---|---|---|
| `01_source_canonique/21_cancer.md` | `p328_figure_01_descente_sevrage_addiction_dependa.png` | Alt et légende héritaient du libellé générique `Descente Sevrage Addiction Dependa`, incohérent dans le chapitre cancer. | Alt et légende corrigés pour décrire le schéma de dommage cellulaire, réparation, élimination immunitaire ou évolution vers un cancer. |
| `01_source_canonique/21_cancer.md` | `p330_figure_01_descente_sevrage_addiction_dependa.png` | Alt et légende héritaient du même libellé générique, incohérent avec le graphique cancer. | Alt et légende corrigés pour décrire le graphique CIRC/OMS/Institut National du Cancer sur les cancers attribuables au mode de vie et à l'environnement. |
| `05_assets_visuels/README.md` | `p328_figure_01_descente_sevrage_addiction_dependa.png`, `p330_figure_01_descente_sevrage_addiction_dependa.png` | Descriptions trop génériques pour deux images du chapitre cancer. | Descriptions précisées sans renommer les fichiers. |
| `00_pilotage/02_index_visuels_tableaux_figures.md` | `p328_figure_01_descente_sevrage_addiction_dependa.png`, `p330_figure_01_descente_sevrage_addiction_dependa.png` | Entrées `a confirmer` trop génériques. | Titre visible, description, données extraites et justification documentaire complétés. |

## Liste de contrôle par page publiée

| Page / composant | Images affichées | Statut |
|---|---:|---|
| `.vitepress/theme/components/RiskHome.vue` | `/risky-logo.png` | OK : logo d'accueil, pas une figure scientifique de chapitre. |
| `figures.md` | 16 images : `p009`, `p020`, `p022`, `p028`, `p034`, `p044`, `p046`, `p049`, `p101`, `p114`, `p127`, `p160`, `p209`, `p235`, `p264`, `p284` | OK : galerie de figures, usage explicitement transversal. |
| `01_source_canonique/01_introduction_cadre_objectif_sources.md` | `p009_figure_01_preventions_primaire_secondaire_tertiaire.png` | OK : cadrage prévention primaire/secondaire/tertiaire, conforme au chapitre. |
| `01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes.md` | `p020_figure_01_heuristiques.png`, `p022_figure_01_biais_cognitifs.png`, `p028_figure_01_sophismes.png` | OK : heuristiques, biais et sophismes dans le chapitre correspondant. |
| `01_source_canonique/03_mecanismes_protection_approche_rdr.md` | `p034_figure_01_mecanismes_protection_psychologique.png`, `p044_figure_01_corriger_croyance_situation.png` | OK : mécanismes de protection et correction de croyance. |
| `01_source_canonique/04_comprendre_science_preuves_causalite.md` | `p046_figure_01_science_vs_recherche.png`, `p049_figure_01_etapes_methode_scientifique.png` | OK : science, recherche et méthode scientifique. |
| `01_source_canonique/05_mythes_alcool_tabac_prix_sante_publique.md` | `p052`, `p062`, `p064`, `p065`, `p066` `alcool_tabac_sante_publique_prix` | OK : bloc alcool/tabac/santé publique/prix. |
| `01_source_canonique/06_mythes_sucre_naturel_reste_perche_contact_addiction.md` | `p078`, `p081`, `p089` `sucre_naturel_reste_perche_contact` | OK : mythes sucre/naturel/contact/addiction. |
| `01_source_canonique/07_ghb_drogue_du_viol_chemsex_3mmc_rc_nps.md` | `p097_figure_01_ghb_drogue_du_viol_chemsex_3_mmc_r.png`, `p097_figure_02_ghb_drogue_du_viol_chemsex_3_mmc_r.png` | OK : GHB, chemsex, 3-MMC, RC/NPS. |
| `01_source_canonique/08_gestion_des_risques.md` | `p101_figure_01_gestion_des_risques.png` | OK : gestion des risques. |
| `01_source_canonique/09_cerveau_synapses_neurotransmetteurs_circuits.md` | `p105`, `p106_01`, `p106_02`, `p107`, `p113`, `p114` `cerveau_synapses_neurotransmetteur` | OK : cerveau, synapses, neurotransmetteurs et circuits. |
| `01_source_canonique/10_tolerance_developpement_15_25_corps_humain.md` | `p115`, `p119`, `p120` `tolerance_developpement_15_25_corp` | OK : tolérance, développement 15-25 ans et corps humain. |
| `01_source_canonique/11_pk_pd_absorption_distribution_metabolisme_elimination.md` | `p127_01`, `p127_02`, `p129`, `p131`, `p132`, `p133`, `p135`, `p137` `pk_pd_adme` | OK : PK/PD/ADME. |
| `01_source_canonique/12_psychologie_placebo_nocebo_troubles_psychologiques.md` | `p145`, `p147` `psychologie_placebo_nocebo_trouble` | OK : psychologie, placebo/nocebo et troubles psychologiques. |
| `01_source_canonique/13_classifications_substances.md` | `p160`, `p162`, `p168`, `p169`, `p178` `classifications_substances` | OK : seul chapitre canonique qui affiche les images de classification. |
| `01_source_canonique/14_risques_generiques_sommeil_juridique.md` | aucune | OK. |
| `01_source_canonique/15_sexualite_vulnerabilite_consentement.md` | aucune | OK. |
| `01_source_canonique/16_allergie_convulsions_hydratation_thermie.md` | `p201`, `p203`, `p209`, `p210`, `p213`, `p216` `allergie_convulsions_hydratation_t` | OK : allergie, convulsions, hydratation et thermie. |
| `01_source_canonique/17_badtrip_overdose.md` | `p231`, `p235`, `p236`, `p239`, `p245` `badtrip_overdose` | OK : badtrip et overdose. |
| `01_source_canonique/18_interactions_melanges.md` | `p252`, `p256`, `p261_01`, `p261_02`, `p264`, `p265_01`, `p265_02`, `p266` `interactions_melanges` | OK : interactions et mélanges. |
| `01_source_canonique/19_testing_analyses_produits_biologie.md` | `p269`, `p275`, `p277`, `p278`, `p280`, `p282_01`, `p282_02`, `p284`, `p285`, `p286_01`, `p286_02`, `p287`, `p288`, `p289`, `p290_01`, `p290_02`, `p292` `testing_analyses_produits_biologie` | OK : testing, analyses produits et biologie. |
| `01_source_canonique/20_descente_sevrage_addiction_dependance.md` | `p297`, `p298`, `p299`, `p300`, `p303`, `p304`, `p305`, `p311_01`, `p311_02`, `p311_03`, `p312_01`, `p312_02`, `p318_01`, `p318_02` `descente_sevrage_addiction_dependa` | OK : descente, sevrage, addiction et dépendance. |
| `01_source_canonique/21_cancer.md` | `p328_figure_01_descente_sevrage_addiction_dependa.png`, `p330_figure_01_descente_sevrage_addiction_dependa.png` | OK après correction : les fichiers ont un nom hérité du bloc 21, mais les deux images affichées appartiennent bien au chapitre cancer et sont maintenant justifiées par alt/légende/index. |

## Images volontairement non affichées

| Image | Motif |
|---|---|
| `p001_figure_01_dedicace_image_koala.jpeg` | Paratexte de dédicace ; pas de figure RDR directe à afficher dans les chapitres du site. |
| `p012_figure_01_icone_koala_encadres.jpeg` | Icône d'encadré ; pas d'information autonome à afficher comme figure scientifique. |

## Incertitudes restantes

- Plusieurs entrées d'assets conservent un statut documentaire `a relire` dans les index historiques parce que le texte visible des figures n'a pas été retranscrit finement. Cette incertitude ne contredit pas l'affectation chapitre/image : les noms de fichiers, pages imprimées et blocs sources correspondent aux chapitres où elles sont affichées.
- Les fichiers `p328` et `p330` gardent leur nom physique historique `descente_sevrage_addiction_dependa`; le renommage aurait un impact plus large que nécessaire. La correction porte donc sur alt, légende et index documentaire.
