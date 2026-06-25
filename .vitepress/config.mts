import { defineConfig, type DefaultTheme } from 'vitepress'
import { treatyTocSections, type TreatyTocEntry } from './treatyToc'

const chapterSidebar: DefaultTheme.SidebarItem[] = treatyTocSections.map((section) => {
  return {
    text: section.text,
    link: section.link,
    collapsed: true,
    items: buildTocSidebar(section.entries)
  }
})

function buildTocSidebar(entries: TreatyTocEntry[]): DefaultTheme.SidebarItem[] {
  const roots: DefaultTheme.SidebarItem[] = []
  const stack: Array<{ level: number; item: DefaultTheme.SidebarItem }> = []

  for (const entry of entries) {
    const item: DefaultTheme.SidebarItem = {
      text: entry.text,
      link: entry.link
    }

    while (stack.length > 0 && stack[stack.length - 1].level >= entry.level) {
      stack.pop()
    }

    const parent = stack[stack.length - 1]?.item

    if (parent) {
      parent.items = parent.items ?? []
      parent.items.push(item)
    } else {
      roots.push(item)
    }

    stack.push({ level: entry.level, item })
  }

  return roots
}

export default defineConfig({
  lang: 'fr-FR',
  title: 'Traité de réduction des risques et des dommages',
  description: 'Lecture guidée du traité de réduction des risques et des dommages.',
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
    siteTitle: 'Traité RDR',
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Accueil', link: '/' },
      { text: 'Lire', link: '/lire' },
      { text: 'Sommaire', link: '/sommaire' },
      { text: 'PDF', link: '/pdf' },
      {
        text: 'Présentations',
        items: [
          { text: 'Hydratation', link: '/prez-hydratation' }
        ]
      }
    ],
    sidebar: [
      {
        text: 'Sommaire du traité',
        collapsed: false,
        items: chapterSidebar
      },
      {
        text: 'Accès rapide',
        collapsed: false,
        items: [
          { text: 'Accueil', link: '/' },
          { text: 'Lire le traité', link: '/lire' },
          { text: 'Passages à lire en premier', link: '/essentiels' },
          { text: 'Sommaire complet', link: '/sommaire' },
          { text: 'Galerie des figures', link: '/figures' },
          { text: 'Télécharger le PDF', link: '/pdf' }
        ]
      },
      {
        text: 'Présentations',
        collapsed: false,
        items: [
          { text: 'Hydratation', link: '/prez-hydratation' }
        ]
      },
      {
        text: 'Entrer par partie',
        collapsed: false,
        items: [
          { text: 'Cadre, sources et posture RDR', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
          { text: 'Croyances et esprit critique', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
          { text: 'Preuves, science et causalité', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
          { text: 'Produits, effets et corps humain', link: '/01_source_canonique/09_cerveau_synapses_neurotransmetteurs_circuits' },
          { text: 'Classifications des substances', link: '/01_source_canonique/13_classifications_substances' },
          { text: 'Risques et situations critiques', link: '/01_source_canonique/14_risques_generiques_sommeil_juridique' },
          { text: 'Interactions, testing et suites', link: '/01_source_canonique/18_interactions_melanges' }
        ]
      },
      {
        text: 'Parcours de lecture',
        collapsed: false,
        items: [
          { text: 'Vue guidée des parcours', link: '/lire' },
          { text: 'Lire depuis le début', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
          { text: 'Comprendre les croyances', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
          { text: 'Comprendre les risques', link: '/01_source_canonique/08_gestion_des_risques' },
          { text: 'Gérer une situation concrète', link: '/01_source_canonique/17_badtrip_overdose' },
          { text: 'Lire les parties scientifiques', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
          { text: 'Retrouver une substance citée', link: '/substances' }
        ]
      },
      {
        text: 'Index secondaires',
        collapsed: true,
        items: [
          { text: 'Repères transversaux', link: '/themes' },
          { text: 'Galerie des figures', link: '/figures' },
          { text: 'Substances mentionnées', link: '/substances' }
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
    footer: {
      message: 'Ressource documentaire de réduction des risques. Information générale, non incitative, non médicale personnalisée.',
      copyright: 'Risky / Traité RDR'
    }
  }
})
