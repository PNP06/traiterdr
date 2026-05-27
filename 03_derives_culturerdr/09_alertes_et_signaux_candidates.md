# Alertes et signaux candidates

## Statut
Candidats non valides.

## Methode
Signaux documentaires a valider medicalement, juridiquement, metier et UX avant integration. Ils doivent pointer vers les themes et sources canoniques.

## Elements candidats

| ID | Domaine | Signal candidat | Source | Niveau de confiance | Limite | A ne pas faire |
|---|---|---|---|---|---|---|
| ALERT-001 | overdose/intoxication | Signes d alerte ou urgence decrits dans le theme overdose. | `02_themes_transversaux/21_overdose_intoxication_signaux_secours.md` | moyen | validation medicale obligatoire | Ne pas remplacer les secours. |
| ALERT-002 | thermie/hydratation | Hyperthermie, hypothermie, hyponatremie, convulsions ou anaphylaxie. | `02_themes_transversaux/18_thermie_hydratation_convulsions_allergies.md` | moyen | validation medicale obligatoire | Ne pas donner de protocole clinique final. |
| ALERT-003 | consentement | Vulnerabilite, soumission chimique ou consentement altere. | `02_themes_transversaux/19_sexualite_consentement_soumission_vulnerabilite.md` | moyen | validation juridique/UX obligatoire | Ne pas culpabiliser ni interroger de facon intrusive. |
| ALERT-004 | produit inconnu | RC/NPS, produit non teste, discordance analyse/effet. | `02_themes_transversaux/13_produit_marche_testing_analyses_biologiques_alertes.md` ; theme 14 | moyen | depend de donnees produit | Ne pas garantir la composition. |
