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

## Complements Phase 3 depuis themes transversaux

| ID | Domaine | Variable candidate | Type possible | Valeurs possibles | Source | Niveau de confiance | Limite | A ne pas faire |
|---|---|---|---|---|---|---|---|---|
| VAR-TH-01 | theme | `posture_rdr_cadre_legal_et_ethique_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/01_posture_rdr_cadre_legal_ethique.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-02 | theme | `publics_prevention_secondaire_et_non_stigmatisat_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/02_publics_prevention_secondaire_non_stigmatisation.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-03 | theme | `croyances_biais_sophismes_et_decision_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/03_croyances_biais_sophismes_decision.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-04 | theme | `mythes_specifiques_et_recits_sociaux_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/04_mythes_specifiques_et_recits_sociaux.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-05 | theme | `methode_scientifique_preuves_causalite_et_incert_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/05_methode_scientifique_preuves_causalite_incertitude.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-06 | theme | `gestion_des_risques_gravite_probabilite_et_barri_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/06_gestion_des_risques_gravite_probabilite_barrieres.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-07 | theme | `neurobiologie_synapses_neurotransmetteurs_et_cir_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/07_neurobiologie_synapses_neurotransmetteurs_circuits.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-08 | theme | `pk_pd_absorption_distribution_metabolisme_et_eli_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/08_pk_pd_absorption_distribution_metabolisme_elimination.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-09 | theme | `tolerance_accoutumance_tachyphylaxie_et_developp_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/09_tolerance_accoutumance_tachyphylaxie_developpement_15_25.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-10 | theme | `psychologie_placebo_nocebo_et_troubles_psycholog_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/10_psychologie_placebo_nocebo_troubles_psychologiques.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-11 | theme | `classifications_dangerosite_dommages_et_toxicite_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/11_classifications_dangerosite_dommages_toxicite.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-12 | theme | `juridique_classifications_risques_et_limites_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/12_juridique_classifications_risques_et_limites.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-13 | theme | `produit_marche_testing_analyses_biologiques_et_a_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/13_produit_marche_testing_analyses_biologiques_alertes.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-14 | theme | `rc_nps_darknet_marche_illicite_et_incertitude_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/14_rc_nps_darknet_marche_illicite_incertitude.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-15 | theme | `dose_exposition_frequence_conversion_seuils_et_l_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/15_dose_exposition_frequence_conversion_seuils_limites.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-16 | theme | `polyconsommations_interactions_et_methodes_d_ana_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/16_polyconsommations_interactions_methodes_analyse.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-17 | theme | `contexte_set_and_setting_preparation_sommeil_et__present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/17_contexte_set_setting_preparation_sommeil_fatigue.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-18 | theme | `thermie_hydratation_convulsions_et_allergies_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/18_thermie_hydratation_convulsions_allergies.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-19 | theme | `sexualite_consentement_soumission_et_vulnerabili_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/19_sexualite_consentement_soumission_vulnerabilite.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-20 | theme | `badtrip_crise_mal_etre_et_accompagnement_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/20_badtrip_crise_mal_etre_accompagnement.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-21 | theme | `overdose_intoxication_signaux_et_secours_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/21_overdose_intoxication_signaux_secours.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-22 | theme | `descente_recuperation_et_sevrage_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/22_descente_recuperation_sevrage.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-23 | theme | `addiction_dependance_craving_et_usages_problemat_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/23_addiction_dependance_craving_usages_problematiques.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-24 | theme | `risques_chroniques_et_cancer_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/24_risques_chroniques_cancer.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-25 | theme | `sante_publique_economie_prix_et_politiques_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/25_sante_publique_economie_prix_politiques.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-26 | theme | `communication_pairs_entourage_et_professionnels_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/26_communication_pairs_entourage_professionnels.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
| VAR-TH-27 | theme | `messages_rdr_terrain_et_ton_operationnel_present` | booleen/tag | oui/non/incertain | `02_themes_transversaux/27_messages_rdr_terrain_ton_operationnel.md` | moyen | depend de la qualite de l assemblage theme | Ne pas deduire un profil utilisateur. |
