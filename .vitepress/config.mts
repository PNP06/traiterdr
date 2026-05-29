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
  title: 'Traite RDR',
  description: 'Traite de reduction des risques - version web documentaire.',
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
    siteTitle: 'Traite RDR',
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Accueil', link: '/' },
      { text: 'Lire', link: '/lire' },
      { text: 'Essentiels', link: '/essentiels' },
      { text: 'Sommaire', link: '/sommaire' },
      { text: 'Figures', link: '/figures' },
      { text: 'PDF', link: '/pdf' }
    ],
    sidebar: [
      {
        text: 'Commencer',
        collapsed: false,
        items: [
          { text: 'Accueil', link: '/' },
          { text: 'Lire le traite', link: '/lire' },
          { text: 'Parties importantes', link: '/essentiels' },
          { text: 'Sommaire complet', link: '/sommaire' },
          { text: 'Telecharger le PDF', link: '/pdf' }
        ]
      },
      {
        text: 'Parcours thematiques',
        collapsed: false,
        items: [
          { text: 'Croyances et biais', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
          { text: 'Science et preuves', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
          { text: 'Gestion des risques', link: '/01_source_canonique/08_gestion_des_risques' },
          { text: 'Badtrip et overdose', link: '/01_source_canonique/17_badtrip_overdose' },
          { text: 'Interactions et melanges', link: '/01_source_canonique/18_interactions_melanges' },
          { text: 'Testing et analyses', link: '/01_source_canonique/19_testing_analyses_produits_biologie' }
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
          { text: 'Index visuels technique', link: '/00_pilotage/02_index_visuels_tableaux_figures' }
        ]
      },
      {
        text: 'Corpus technique',
        collapsed: true,
        items: [
          { text: 'Index general du corpus', link: '/corpus-index' },
          { text: 'Glossaire', link: '/00_pilotage/04_glossaire' },
          { text: 'Matrice de couverture', link: '/00_pilotage/01_matrice_couverture' },
          { text: 'Index notions', link: '/00_pilotage/03_index_notions' },
          { text: 'Themes transversaux', link: '/02_themes_transversaux/00_index_themes' },
          { text: 'Substances mentionnees', link: '/04_substances_mentions/00_index_substances' },
          { text: 'Derives CultureRDR candidates', link: '/03_derives_culturerdr/00_index_derives' },
          { text: 'Bilan final corpus', link: '/00_pilotage/10_bilan_final_corpus' }
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
    lastUpdated: {
      text: 'Derniere mise a jour',
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
      message: 'Ressource documentaire RDR. Information generale, non incitative, non medicale personnalisee.',
      copyright: 'CultureRDR / Traite RDR'
    }
  }
})
