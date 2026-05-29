import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'fr-FR',
  title: 'Traité RDR',
  description: 'Traité de réduction des risques — version web documentaire.',
  cleanUrls: true,
  srcExclude: [
    'sources/**'
  ],
  lastUpdated: true,
  ignoreDeadLinks: true,
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
      { text: 'Lire', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
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
        text: 'Corpus',
        collapsed: false,
        items: [
          { text: 'Introduction', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
          { text: 'Index des thèmes', link: '/02_themes_transversaux/00_index_themes' },
          { text: 'Index substances', link: '/04_substances_mentions/00_index_substances' },
          { text: 'Index notions', link: '/00_pilotage/03_index_notions' },
          { text: 'Index visuels', link: '/00_pilotage/02_index_visuels_tableaux_figures' },
          { text: 'Bilan final corpus', link: '/00_pilotage/10_bilan_final_corpus' }
        ]
      },
      {
        text: 'Lecture canonique',
        collapsed: true,
        items: [
          { text: 'Bloc 00', link: '/01_source_canonique/00_front_matter_suivi_remerciements' },
          { text: 'Bloc 01', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
          { text: 'Bloc 02', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
          { text: 'Bloc 03', link: '/01_source_canonique/03_mecanismes_protection_approche_rdr' },
          { text: 'Bloc 04', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
          { text: 'Bloc 05', link: '/01_source_canonique/05_mythes_alcool_tabac_prix_sante_publique' },
          { text: 'Bloc 06', link: '/01_source_canonique/06_mythes_sucre_naturel_reste_perche_contact_addiction' },
          { text: 'Bloc 07', link: '/01_source_canonique/07_ghb_drogue_du_viol_chemsex_3mmc_rc_nps' },
          { text: 'Bloc 08', link: '/01_source_canonique/08_gestion_des_risques' },
          { text: 'Bloc 09', link: '/01_source_canonique/09_cerveau_synapses_neurotransmetteurs_circuits' },
          { text: 'Bloc 10', link: '/01_source_canonique/10_tolerance_developpement_15_25_corps_humain' },
          { text: 'Bloc 11', link: '/01_source_canonique/11_pk_pd_absorption_distribution_metabolisme_elimination' },
          { text: 'Bloc 12', link: '/01_source_canonique/12_psychologie_placebo_nocebo_troubles_psychologiques' },
          { text: 'Bloc 13', link: '/01_source_canonique/13_classifications_substances' },
          { text: 'Bloc 14', link: '/01_source_canonique/14_risques_generiques_sommeil_juridique' },
          { text: 'Bloc 15', link: '/01_source_canonique/15_sexualite_vulnerabilite_consentement' },
          { text: 'Bloc 16', link: '/01_source_canonique/16_allergie_convulsions_hydratation_thermie' },
          { text: 'Bloc 17', link: '/01_source_canonique/17_badtrip_overdose' },
          { text: 'Bloc 18', link: '/01_source_canonique/18_interactions_melanges' },
          { text: 'Bloc 19', link: '/01_source_canonique/19_testing_analyses_produits_biologie' },
          { text: 'Bloc 20', link: '/01_source_canonique/20_descente_sevrage_addiction_dependance' },
          { text: 'Bloc 21', link: '/01_source_canonique/21_cancer' }
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
