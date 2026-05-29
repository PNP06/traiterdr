import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'fr-FR',
  title: 'Traité RDR',
  description: 'Traité de réduction des risques liés aux substances psychoactives — version web documentaire.',
  cleanUrls: true,
  lastUpdated: true,
  ignoreDeadLinks: true,
  sitemap: {
    hostname: 'https://traiterdr.netlify.app'
  },
  head: [
    ['meta', { name: 'theme-color', content: '#0f172a' }],
    ['meta', { name: 'robots', content: 'index,follow' }]
  ],
  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'Traité RDR',
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Accueil', link: '/' },
      { text: 'Lire le traité', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
      { text: 'Thèmes', link: '/02_themes_transversaux/00_index_themes' },
      { text: 'Substances', link: '/04_substances_mentions/00_index_substances' },
      { text: 'PDF', link: '/pdf' },
      { text: 'GitHub', link: 'https://github.com/PNP06/traiterdr' }
    ],
    sidebar: [
      {
        text: 'Entrée',
        items: [
          { text: 'Accueil', link: '/' },
          { text: 'Télécharger le PDF', link: '/pdf' },
          { text: 'Index général', link: '/INDEX' },
          { text: 'Glossaire', link: '/00_pilotage/04_glossaire' }
        ]
      },
      {
        text: 'Source canonique',
        collapsed: false,
        items: [
          { text: 'Introduction, cadre, objectifs', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
          { text: 'Mythes, biais, sophismes', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
          { text: 'Mécanismes de protection et approche RDR', link: '/01_source_canonique/03_mecanismes_protection_approche_rdr' },
          { text: 'Science, preuves, causalité', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
          { text: 'Gestion des risques', link: '/01_source_canonique/08_gestion_des_risques' },
          { text: 'Cerveau, synapses, neurotransmetteurs', link: '/01_source_canonique/09_cerveau_synapses_neurotransmetteurs_circuits' },
          { text: 'Tolérance et développement', link: '/01_source_canonique/10_tolerance_developpement_15_25_corps_humain' },
          { text: 'PK / PD / ADME', link: '/01_source_canonique/11_pk_pd_absorption_distribution_metabolisme_elimination' },
          { text: 'Psychologie, placebo, troubles psychologiques', link: '/01_source_canonique/12_psychologie_placebo_nocebo_troubles_psychologiques' },
          { text: 'Classifications des substances', link: '/01_source_canonique/13_classifications_substances' },
          { text: 'Risques génériques', link: '/01_source_canonique/14_risques_generiques_sommeil_juridique' },
          { text: 'Sexualité, vulnérabilité, consentement', link: '/01_source_canonique/15_sexualite_vulnerabilite_consentement' },
          { text: 'Allergie, convulsions, hydratation, thermie', link: '/01_source_canonique/16_allergie_convulsions_hydratation_thermie' },
          { text: 'Bad trip et overdose', link: '/01_source_canonique/17_badtrip_overdose' },
          { text: 'Interactions et mélanges', link: '/01_source_canonique/18_interactions_melanges' },
          { text: 'Testing, analyses, biologie', link: '/01_source_canonique/19_testing_analyses_produits_biologie' },
          { text: 'Descente, sevrage, addiction', link: '/01_source_canonique/20_descente_sevrage_addiction_dependance' },
          { text: 'Cancer', link: '/01_source_canonique/21_cancer' }
        ]
      },
      {
        text: 'Thèmes transversaux',
        collapsed: true,
        items: [
          { text: 'Index des thèmes', link: '/02_themes_transversaux/00_index_themes' },
          { text: 'Posture RDR, cadre légal, éthique', link: '/02_themes_transversaux/01_posture_rdr_cadre_legal_ethique' },
          { text: 'Croyances, biais, décision', link: '/02_themes_transversaux/03_croyances_biais_sophismes_decision' },
          { text: 'Méthode scientifique', link: '/02_themes_transversaux/05_methode_scientifique_preuves_causalite_incertitude' },
          { text: 'Produit, marché, testing', link: '/02_themes_transversaux/13_produit_marche_testing_analyses_biologiques_alertes' },
          { text: 'Dose, exposition, fréquence', link: '/02_themes_transversaux/15_dose_exposition_frequence_conversion_seuils_limites' },
          { text: 'Polyconsommations et interactions', link: '/02_themes_transversaux/16_polyconsommations_interactions_methodes_analyse' },
          { text: 'Set & setting', link: '/02_themes_transversaux/17_contexte_set_setting_preparation_sommeil_fatigue' },
          { text: 'Thermie, hydratation, convulsions', link: '/02_themes_transversaux/18_thermie_hydratation_convulsions_allergies' },
          { text: 'Bad trip, crise, accompagnement', link: '/02_themes_transversaux/20_badtrip_crise_mal_etre_accompagnement' },
          { text: 'Overdose, intoxication, secours', link: '/02_themes_transversaux/21_overdose_intoxication_signaux_secours' },
          { text: 'Descente et récupération', link: '/02_themes_transversaux/22_descente_recuperation_sevrage' },
          { text: 'Addiction, dépendance, craving', link: '/02_themes_transversaux/23_addiction_dependance_craving_usages_problematiques' }
        ]
      },
      {
        text: 'Substances mentionnées',
        collapsed: true,
        items: [
          { text: 'Index substances', link: '/04_substances_mentions/00_index_substances' },
          { text: 'Alcool', link: '/04_substances_mentions/alcool' },
          { text: 'Tabac / nicotine', link: '/04_substances_mentions/tabac_nicotine' },
          { text: 'Cannabis', link: '/04_substances_mentions/cannabis' },
          { text: 'MDMA', link: '/04_substances_mentions/mdma' },
          { text: 'Cocaïne', link: '/04_substances_mentions/cocaine' },
          { text: 'GHB / GBL', link: '/04_substances_mentions/ghb_gbl' },
          { text: 'Kétamine', link: '/04_substances_mentions/ketamine' },
          { text: 'Benzodiazépines', link: '/04_substances_mentions/benzodiazepines' },
          { text: 'Opioïdes', link: '/04_substances_mentions/opioides' },
          { text: 'Psychédéliques', link: '/04_substances_mentions/psychedeliques_lsd_psilocybine' },
          { text: 'RC / NPS', link: '/04_substances_mentions/rc_nps' },
          { text: '3-MMC / chemsex', link: '/04_substances_mentions/3mmc_chemsex' }
        ]
      },
      {
        text: 'Pilotage et qualité',
        collapsed: true,
        items: [
          { text: 'Index global', link: '/00_pilotage/00_index_global' },
          { text: 'Matrice de couverture', link: '/00_pilotage/01_matrice_couverture' },
          { text: 'Index visuels', link: '/00_pilotage/02_index_visuels_tableaux_figures' },
          { text: 'Index notions', link: '/00_pilotage/03_index_notions' },
          { text: 'Journal d’extraction', link: '/00_pilotage/05_journal_extraction' },
          { text: 'Bilan final corpus', link: '/00_pilotage/10_bilan_final_corpus' }
        ]
      }
    ],
    outline: {
      level: [2, 3],
      label: 'Sur cette page'
    },
    docFooter: {
      prev: 'Page précédente',
      next: 'Page suivante'
    },
    lastUpdated: {
      text: 'Dernière mise à jour',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'short'
      }
    },
    editLink: {
      pattern: 'https://github.com/PNP06/traiterdr/edit/master/:path',
      text: 'Modifier cette page sur GitHub'
    },
    footer: {
      message: 'Ressource documentaire RDR. Information générale, non incitative, non médicale personnalisée.',
      copyright: 'CultureRDR / Traité RDR'
    }
  }
})
