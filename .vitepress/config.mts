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
    'AGENTS.md',
    'llms.txt',
    'readme.md'
  ],
  lastUpdated: false,
  ignoreDeadLinks: true,
  head: [
    ['meta', { name: 'theme-color', content: '#123a33' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&display=swap' }],
    ['meta', { property: 'og:image', content: '/koala.webp' }],
    ['meta', { name: 'robots', content: 'index,follow' }],
    ['link', { rel: 'icon', href: '/risky-logo.png' }]
  ],
  themeConfig: {
    logo: '/risky-logo.png',
    siteTitle: 'Traité RDR',
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: 'Rechercher', buttonAriaLabel: 'Rechercher dans le traité' },
          modal: {
            displayDetails: 'Afficher la liste détaillée',
            resetButtonTitle: 'Effacer la recherche',
            backButtonTitle: 'Fermer la recherche',
            noResultsText: 'Aucun résultat pour',
            footer: {
              selectText: 'pour ouvrir',
              selectKeyAriaLabel: 'Entrée',
              navigateText: 'pour naviguer',
              navigateUpKeyAriaLabel: 'Flèche haut',
              navigateDownKeyAriaLabel: 'Flèche bas',
              closeText: 'pour fermer',
              closeKeyAriaLabel: 'Échap'
            }
          }
        }
      }
    },
    darkModeSwitchLabel: 'Apparence',
    lightModeSwitchTitle: 'Passer en mode clair',
    darkModeSwitchTitle: 'Passer en mode sombre',
    sidebarMenuLabel: 'Menu',
    returnToTopLabel: 'Retour en haut',
    langMenuLabel: 'Langue',
    socialLinks: [
      { icon: 'instagram', link: 'https://www.instagram.com/risky.asso/', ariaLabel: 'Instagram @risky.asso' }
    ],
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
          { text: 'Références', link: '/references' },
          { text: 'Substances citées', link: '/substances' },
          { text: 'Repères transversaux', link: '/themes' },
          { text: 'Présentation : hydratation', link: '/prez-hydratation' },
          { text: 'Télécharger le PDF', link: '/pdf' }
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
