import { existsSync, readFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig, type DefaultTheme } from 'vitepress'

const chapters = [
  { text: 'Avant-propos et table des matieres', file: '00_front_matter_suivi_remerciements.md', link: '/01_source_canonique/00_front_matter_suivi_remerciements' },
  { text: 'Introduction, cadre et sources', file: '01_introduction_cadre_objectif_sources.md', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
  { text: 'Mythes, croyances, biais et sophismes', file: '02_mythes_croyances_heuristiques_biais_sophismes.md', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
  { text: 'Mecanismes de protection et approche RDR', file: '03_mecanismes_protection_approche_rdr.md', link: '/01_source_canonique/03_mecanismes_protection_approche_rdr' },
  { text: 'Science, preuves et causalite', file: '04_comprendre_science_preuves_causalite.md', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
  { text: 'Alcool, tabac, prix et sante publique', file: '05_mythes_alcool_tabac_prix_sante_publique.md', link: '/01_source_canonique/05_mythes_alcool_tabac_prix_sante_publique' },
  { text: 'Sucre, naturel, contact et addiction', file: '06_mythes_sucre_naturel_reste_perche_contact_addiction.md', link: '/01_source_canonique/06_mythes_sucre_naturel_reste_perche_contact_addiction' },
  { text: 'GHB, chemsex, 3-MMC, RC et NPS', file: '07_ghb_drogue_du_viol_chemsex_3mmc_rc_nps.md', link: '/01_source_canonique/07_ghb_drogue_du_viol_chemsex_3mmc_rc_nps' },
  { text: 'Gestion des risques', file: '08_gestion_des_risques.md', link: '/01_source_canonique/08_gestion_des_risques' },
  { text: 'Cerveau, synapses et circuits', file: '09_cerveau_synapses_neurotransmetteurs_circuits.md', link: '/01_source_canonique/09_cerveau_synapses_neurotransmetteurs_circuits' },
  { text: 'Tolerance et developpement 15-25 ans', file: '10_tolerance_developpement_15_25_corps_humain.md', link: '/01_source_canonique/10_tolerance_developpement_15_25_corps_humain' },
  { text: 'PK/PD, absorption et elimination', file: '11_pk_pd_absorption_distribution_metabolisme_elimination.md', link: '/01_source_canonique/11_pk_pd_absorption_distribution_metabolisme_elimination' },
  { text: 'Psychologie, placebo et nocebo', file: '12_psychologie_placebo_nocebo_troubles_psychologiques.md', link: '/01_source_canonique/12_psychologie_placebo_nocebo_troubles_psychologiques' },
  { text: 'Classifications des substances', file: '13_classifications_substances.md', link: '/01_source_canonique/13_classifications_substances' },
  { text: 'Risques generiques, sommeil et juridique', file: '14_risques_generiques_sommeil_juridique.md', link: '/01_source_canonique/14_risques_generiques_sommeil_juridique' },
  { text: 'Sexualite, vulnerabilite et consentement', file: '15_sexualite_vulnerabilite_consentement.md', link: '/01_source_canonique/15_sexualite_vulnerabilite_consentement' },
  { text: 'Allergie, convulsions, hydratation et thermie', file: '16_allergie_convulsions_hydratation_thermie.md', link: '/01_source_canonique/16_allergie_convulsions_hydratation_thermie' },
  { text: 'Badtrip et overdose', file: '17_badtrip_overdose.md', link: '/01_source_canonique/17_badtrip_overdose' },
  { text: 'Interactions et melanges', file: '18_interactions_melanges.md', link: '/01_source_canonique/18_interactions_melanges' },
  { text: 'Testing, analyses et biologie', file: '19_testing_analyses_produits_biologie.md', link: '/01_source_canonique/19_testing_analyses_produits_biologie' },
  { text: 'Descente, sevrage, addiction et dependance', file: '20_descente_sevrage_addiction_dependance.md', link: '/01_source_canonique/20_descente_sevrage_addiction_dependance' },
  { text: 'Cancer', file: '21_cancer.md', link: '/01_source_canonique/21_cancer' }
]

const projectRoot = join(dirname(fileURLToPath(import.meta.url)), '..')
const sourceDir = join(projectRoot, '01_source_canonique')

const chapterSidebar = chapters.map((chapter) => {
  const items = extractChapterHeadings(chapter.file, chapter.link)

  return {
    text: chapter.text,
    link: chapter.link,
    collapsed: true,
    items
  }
})

function extractChapterHeadings(file: string, chapterLink: string): DefaultTheme.SidebarItem[] {
  const filePath = join(sourceDir, file)

  if (!existsSync(filePath)) return []

  const usedSlugs = new Map<string, number>()
  const lines = readFileSync(filePath, 'utf8').split(/\r?\n/)
  const headings: DefaultTheme.SidebarItem[] = []

  for (const line of lines) {
    const match = /^(#{1,6})\s+(.+?)\s*#*\s*$/.exec(line)

    if (!match) continue

    const level = match[1].length
    const text = cleanHeadingText(match[2])
    const slug = uniqueSlug(text, usedSlugs)

    if (level < 2 || level > 3 || !text) continue

    headings.push({
      text,
      link: `${chapterLink}#${slug}`
    })
  }

  return headings
}

function cleanHeadingText(text: string) {
  return text
    .replace(/`([^`]+)`/g, '$1')
    .replace(/!\[([^\]]*)\]\([^)]+\)/g, '$1')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/<[^>]+>/g, '')
    .replace(/[*_~]/g, '')
    .trim()
}

function uniqueSlug(text: string, usedSlugs: Map<string, number>) {
  const base = slugify(text)
  const seen = usedSlugs.get(base) ?? 0

  usedSlugs.set(base, seen + 1)

  return seen === 0 ? base : `${base}-${seen}`
}

function slugify(text: string) {
  return text
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[\u0000-\u001f]/g, '')
    .replace(/[\s~`!@#$%^&*()\-_+=[\]{}|\\;:"'“”‘’<>,.?/]+/g, '-')
    .replace(/-{2,}/g, '-')
    .replace(/^-+|-+$/g, '')
    .replace(/^(\d)/, '_$1')
    .toLowerCase()
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
      { text: 'PDF', link: '/pdf' }
    ],
    sidebar: [
      {
        text: 'Sommaire du traite',
        collapsed: false,
        items: chapterSidebar
      },
      {
        text: 'Acces rapide',
        collapsed: false,
        items: [
          { text: 'Accueil', link: '/' },
          { text: 'Lire le traite', link: '/lire' },
          { text: 'Passages a lire en premier', link: '/essentiels' },
          { text: 'Sommaire complet', link: '/sommaire' },
          { text: 'Galerie des figures', link: '/figures' },
          { text: 'Telecharger le PDF', link: '/pdf' }
        ]
      },
      {
        text: 'Entrer par partie',
        collapsed: false,
        items: [
          { text: 'Cadre, sources et posture RDR', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
          { text: 'Croyances et esprit critique', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
          { text: 'Preuves, science et causalite', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
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
          { text: 'Vue guidee des parcours', link: '/lire' },
          { text: 'Lire depuis le debut', link: '/01_source_canonique/01_introduction_cadre_objectif_sources' },
          { text: 'Comprendre les croyances', link: '/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes' },
          { text: 'Comprendre les risques', link: '/01_source_canonique/08_gestion_des_risques' },
          { text: 'Gerer une situation concrete', link: '/01_source_canonique/17_badtrip_overdose' },
          { text: 'Lire les parties scientifiques', link: '/01_source_canonique/04_comprendre_science_preuves_causalite' },
          { text: 'Retrouver une substance citee', link: '/substances' }
        ]
      },
      {
        text: 'Index secondaires',
        collapsed: true,
        items: [
          { text: 'Reperes transversaux', link: '/themes' },
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
      copyright: 'Risky / Traité RDR'
    }
  }
})
