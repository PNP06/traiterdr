import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'fr-FR',
  title: 'Traité de réduction des risques et des dommages',
  description: 'Le traité de réduction des risques de l’association Risky : substances psychoactives et santé, comprendre sans bac+5. À lire en ligne ou en PDF.',
  cleanUrls: true,
  srcExclude: [
    'sources/**',
    'scripts/**',
    '00_pilotage/**',
    '02_themes_transversaux/**',
    '03_derives_culturerdr/**',
    '04_substances_mentions/**',
    '01_source_canonique/**',
    'lire.md',
    'sommaire.md',
    'essentiels.md',
    'figures.md',
    'substances.md',
    'themes.md',
    'references.md',
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
      { text: 'Le traité', link: '/#lire' },
      { text: 'Télécharger le PDF', link: '/traite-rdr.pdf', target: '_blank' }
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
