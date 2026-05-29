import { defineConfig } from 'vitepress'

const chapters = [
  { text: 'Avant-propos et table des matieres', link: '/01_source_canonique/00_front_matter_suivi_remerciements' },
  { text: 'Introduction, cadre et sources', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
  { text: 'Mythes, croyances, biais et sophismes', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
  { text: 'Mecanismes de protection et approche RDR', link: '/01_source_canonique/03_mecanismes_protection_approche_rdr' },
  { text: 'Science, preuves et causalite', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
  { text: 'Alcool, tabac, prix et sante publique', link: '/01_source_canonique/05_mythes_alcool_tabac_prix_sante_publique' },
  { text: 'Sucre, naturel, contact et addiction', link: '/01_source_canonique/06_mythes_sucre_naturel_reste_perche_contact_addiction' },
  { text: 'GHB, chemsex, 3-MMC, RC et NPS', link: '/01_source_canonique/07_ghb_drogue_du_viol_chemsex_3mmc_rc_nps' },
  { text: 'Gestion des risques', link: '/01_source_canonique/08_gestion_des_risques' },
  { text: 'Cerveau, synapses et circuits', link: '/01_source_canonique/09_cerveau_synapses_neurotransmetteurs_circuits' },
  { text: 'Tolerance et developpement 15-25 ans', link: '/01_source_canonique/10_tolerance_developpement_15_25_corps_humain' },
  { text: 'PK/PD, absorption et elimination', link: '/01_source_canonique/11_pk_pd_absorption_distribution_metabolisme_elimination' },
  { text: 'Psychologie, placebo et nocebo', link: '/01_source_canonique/12_psychologie_placebo_nocebo_troubles_psychologiques' },
  { text: 'Classifications des substances', link: '/01_source_canonique/13_classifications_substances' },
  { text: 'Risques generiques, sommeil et juridique', link: '/01_source_canonique/14_risques_generiques_sommeil_juridique' },
  { text: 'Sexualite, vulnerabilite et consentement', link: '/01_source_canonique/15_sexualite_vulnerabilite_consentement' },
  { text: 'Allergie, convulsions, hydratation et thermie', link: '/01_source_canonique/16_allergie_convulsions_hydratation_thermie' },
  { text: 'Badtrip et overdose', link: '/01_source_canonique/17_badtrip_overdose' },
  { text: 'Interactions et melanges', link: '/01_source_canonique/18_interactions_melanges' },
  { text: 'Testing, analyses et biologie', link: '/01_source_canonique/19_testing_analyses_produits_biologie' },
  { text: 'Descente, sevrage, addiction et dependance', link: '/01_source_canonique/20_descente_sevrage_addiction_dependance' },
  { text: 'Cancer', link: '/01_source_canonique/21_cancer' }
]

export default defineConfig({
  lang: 'fr-FR',
  title: 'Risky - Traite RDR',
  description: 'Lecture guidee du traite de reduction des risques Risky.',
  cleanUrls: true,
  srcExclude: [
    'sources/**',
    '00_pilotage/**',
    '02_themes_transversaux/**',
    '03_derives_culturerdr/**',
    '04_substances_mentions/**',
    'corpus-index.md',
    'README.md',
    'readme.md'
  ],
  lastUpdated: false,
  ignoreDeadLinks: true,
  head: [
    ['meta', { name: 'theme-color', content: '#0f766e' }],
    ['meta', { name: 'robots', content: 'index,follow' }],
    ['link', { rel: 'icon', href: '/risky-logo.png' }]
  ],
  themeConfig: {
    logo: '/risky-logo.png',
    siteTitle: 'Risky',
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Accueil', link: '/' },
      { text: 'Themes', link: '/themes' },
      { text: 'Sommaire', link: '/sommaire' },
      { text: 'PDF', link: '/pdf' }
    ],
    sidebar: [
      {
        text: 'Commencer',
        collapsed: false,
        items: [
          { text: 'Accueil', link: '/' },
          { text: 'Chercher par theme', link: '/themes' },
          { text: 'Parcours de lecture', link: '/lire' },
          { text: 'Passages a lire en premier', link: '/essentiels' },
          { text: 'Sommaire complet', link: '/sommaire' },
          { text: 'Telecharger le PDF', link: '/pdf' }
        ]
      },
      {
        text: 'Chercher par theme',
        collapsed: false,
        items: [
          { text: 'Tous les themes', link: '/themes' },
          { text: 'Comprendre la RDR', link: '/themes#comprendre-la-rdr' },
          { text: 'Croyances et esprit critique', link: '/themes#croyances-mythes-et-esprit-critique' },
          { text: 'Science et incertitude', link: '/themes#science-preuves-et-incertitude' },
          { text: 'Produits et marches', link: '/themes#produits-classifications-et-marches' },
          { text: 'Situations critiques', link: '/themes#situations-critiques' },
          { text: 'Interactions et testing', link: '/themes#interactions-testing-et-incertitude-produit' }
        ]
      },
      {
        text: 'Parcours de lecture',
        collapsed: true,
        items: [
          { text: 'Lire depuis le debut', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
          { text: 'Comprendre les croyances', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
          { text: 'Comprendre les risques', link: '/01_source_canonique/08_gestion_des_risques' },
          { text: 'Gerer une situation concrete', link: '/01_source_canonique/17_badtrip_overdose' },
          { text: 'Lire les parties scientifiques', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
          { text: 'Lire par substances', link: '/substances' }
        ]
      },
      {
        text: 'Chapitres du traite',
        collapsed: true,
        items: chapters
      },
      {
        text: 'Figures utiles',
        collapsed: true,
        items: [
          { text: 'Galerie des figures', link: '/figures' },
          { text: 'Substances mentionnees', link: '/substances' }
        ]
      }
    ],
    outline: {
      level: [2, 3],
      label: 'Sur cette page'
    },
    docFooter: {
      prev: 'Page precedente',
      next: 'Page suivante'
    },
    footer: {
      message: 'Ressource documentaire de reduction des risques. Information generale, non incitative, non medicale personnalisee.',
      copyright: 'Risky / Traite RDR'
    }
  }
})
