<script setup lang="ts">
import { computed, nextTick, onMounted, ref, watch } from 'vue'

// Index fabriqué par scripts/recherche/build_index.py à partir du PDF.
interface Partie { code: string; titre: string; page: number; fin: number; niveau: number }
interface Page { n: number; p: number; t: string; norm?: string }
interface Groupe { id: string; label: string; mots: string[]; sections?: number[] }
interface Index { pdf: string; parties: Partie[]; pages: Page[]; themes: Groupe[]; produits: Groupe[] }

interface Resultat { page: Page; score: number; extrait: string }

const index = ref<Index | null>(null)
const erreur = ref(false)
const saisie = ref('')
const choix = ref<{ type: 'theme' | 'produit'; id: string } | null>(null)
const limite = ref(20)
const resultats = ref<HTMLElement | null>(null)

// Minuscules sans accents, caractère par caractère, pour garder les positions
// alignées sur le texte d'origine (extraits et surlignage).
function normaliser(s: string) {
  let sortie = ''
  for (const c of s) {
    const base = c === '’' ? "'" : c.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase()
    sortie += base.length === c.length ? base : c
  }
  return sortie
}

const MOTS_VIDES = new Set(['le', 'la', 'les', 'de', 'des', 'du', 'un', 'une', 'et', 'ou', 'en', 'au', 'aux', 'a', 'l', 'd', 'est', 'que', 'qui', 'pour', 'sur', 'par', 'avec'])

function echapperRegex(s: string) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
}

// Un terme commence toujours au début d'un mot. Les termes saisis cherchent aussi
// les mots plus longs (« overdose » trouve « overdoses ») ; les mots des thèmes
// sont exacts sauf s'ils finissent par *.
function motif(terme: string, prefixe: boolean) {
  const ouvert = prefixe || terme.endsWith('*')
  const corps = echapperRegex(normaliser(terme.replace(/\*$/, ''))).replace(/\s+/g, '[\\s-]+')
  return new RegExp(`(?:^|[^\\p{L}\\p{N}])(${corps})${ouvert ? '' : '(?![\\p{L}\\p{N}])'}`, 'gu')
}

function positions(texte: string, re: RegExp) {
  const trouvees: [number, number][] = []
  re.lastIndex = 0
  let m: RegExpExecArray | null
  while ((m = re.exec(texte))) {
    const debut = m.index + m[0].length - m[1].length
    trouvees.push([debut, debut + m[1].length])
    if (m[0].length === 0) re.lastIndex++
  }
  return trouvees
}

function decouper(q: string) {
  const termes: string[] = []
  const re = /"([^"]+)"|«\s*([^»]+?)\s*»|(\S+)/g
  let m: RegExpExecArray | null
  while ((m = re.exec(q))) {
    const t = (m[1] || m[2] || m[3] || '').replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}*]+$/gu, '')
    if (!t) continue
    if (!m[1] && !m[2] && (MOTS_VIDES.has(normaliser(t)) || t.length < 2)) continue
    termes.push(t)
  }
  return termes
}

function echapperHtml(s: string) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

function extrait(page: Page, motifs: RegExp[]) {
  const norm = page.norm!
  const toutes = motifs.flatMap((re) => positions(norm, re)).sort((a, b) => a[0] - b[0])
  if (!toutes.length) return echapperHtml(page.t.slice(0, 220)) + '…'
  // Fenêtre qui contient le plus de mentions (et, à égalité, la première).
  let centre = toutes[0][0]
  let meilleur = 0
  for (const [a] of toutes) {
    const n = toutes.filter(([x]) => x >= a - 90 && x <= a + 190).length
    if (n > meilleur) { meilleur = n; centre = a }
  }
  let debut = Math.max(0, centre - 90)
  let fin = Math.min(page.t.length, centre + 190)
  if (debut > 0) debut = page.t.indexOf(' ', debut) + 1
  if (fin < page.t.length) fin = Math.max(page.t.lastIndexOf(' ', fin), centre + 20)
  let html = debut > 0 ? '…' : ''
  let curseur = debut
  for (const [a, b] of toutes) {
    if (a < curseur || b > fin) continue
    html += echapperHtml(page.t.slice(curseur, a)) + '<mark>' + echapperHtml(page.t.slice(a, b)) + '</mark>'
    curseur = b
  }
  html += echapperHtml(page.t.slice(curseur, fin)) + (fin < page.t.length ? '…' : '')
  return html
}

// tous = true : chaque terme doit être sur la page ; sinon un seul suffit.
function chercher(termes: string[], prefixe: boolean, tous: boolean, exclure = new Set<number>()) {
  if (!index.value || !termes.length) return []
  const motifs = termes.map((t) => motif(t, prefixe))
  const sortie: Resultat[] = []
  for (const page of index.value.pages) {
    if (exclure.has(page.n)) continue
    let score = 0
    let manquant = false
    for (const re of motifs) {
      const n = positions(page.norm!, re).length
      if (!n && tous) { manquant = true; break }
      score += n
    }
    if (manquant || !score) continue
    // Bonus si la partie de la page porte le terme dans son titre.
    const partie = index.value.parties[page.p]
    if (partie && motifs.some((re) => positions(normaliser(partie.titre), re).length)) score += 5
    sortie.push({ page, score, extrait: '' })
  }
  sortie.sort((a, b) => b.score - a.score || a.page.n - b.page.n)
  for (const r of sortie.slice(0, 200)) r.extrait = extrait(r.page, motifs)
  return sortie
}

function partiesParTitre(termes: string[], prefixe: boolean, tous: boolean) {
  if (!index.value || !termes.length) return []
  const motifs = termes.map((t) => motif(t, prefixe))
  return index.value.parties.filter((p) => {
    const titre = normaliser(`${p.code} ${p.titre}`)
    const ok = motifs.map((re) => positions(titre, re).length > 0)
    return tous ? ok.every(Boolean) : ok.some(Boolean)
  })
}

const groupe = computed(() => {
  if (!index.value || !choix.value) return null
  const liste = choix.value.type === 'theme' ? index.value.themes : index.value.produits
  return liste.find((g) => g.id === choix.value!.id) || null
})

const termes = computed(() => decouper(saisie.value))

const vue = computed(() => {
  if (!index.value) return null
  const g = groupe.value
  if (g) {
    const sections = (g.sections || []).map((i) => index.value!.parties[i])
    const couvertes = new Set<number>()
    for (const s of sections) for (let n = s.page; n <= s.fin; n++) couvertes.add(n)
    const titres = sections.length ? sections : partiesParTitre(g.mots, false, false)
    return {
      titre: g.label,
      mots: g.mots.map((m) => m.replace(/\*$/, '…')),
      parties: titres,
      resultats: chercher(g.mots, false, false, couvertes),
      autres: sections.length > 0
    }
  }
  if (!termes.value.length) return null
  return {
    titre: '',
    mots: [],
    parties: partiesParTitre(termes.value, true, true),
    resultats: chercher(termes.value, true, true),
    autres: false
  }
})

function partieDe(page: Page) {
  return index.value?.parties[page.p]
}

function chapitre(partie?: Partie) {
  if (!partie?.code) return ''
  const lettre = partie.code[0]
  const chap = index.value?.parties.find((p) => p.code === lettre)
  return chap ? `Partie ${lettre} · ${chap.titre}` : ''
}

function lien(n: number) {
  return `${index.value?.pdf || '/traite-rdr.pdf'}#page=${n}`
}

function pages(p: Partie) {
  return p.fin > p.page ? `p. ${p.page}-${p.fin}` : `p. ${p.page}`
}

function choisir(type: 'theme' | 'produit', id: string) {
  const deja = choix.value?.type === type && choix.value.id === id
  choix.value = deja ? null : { type, id }
  if (!deja) saisie.value = ''
  limite.value = 20
  if (!deja) nextTick(() => resultats.value?.scrollIntoView({ behavior: 'smooth', block: 'start' }))
}

let minuteur: ReturnType<typeof setTimeout> | undefined
watch(saisie, (v) => {
  if (v) choix.value = null
  limite.value = 20
  clearTimeout(minuteur)
  minuteur = setTimeout(majUrl, 400)
})
watch(choix, majUrl)

function majUrl() {
  const params = new URLSearchParams()
  if (choix.value) params.set(choix.value.type, choix.value.id)
  else if (saisie.value.trim()) params.set('q', saisie.value.trim())
  const qs = params.toString()
  history.replaceState(history.state, '', `${location.pathname}${qs ? '?' + qs : ''}`)
}

onMounted(async () => {
  const params = new URLSearchParams(location.search)
  try {
    const reponse = await fetch('/recherche-index.json')
    const donnees: Index = await reponse.json()
    for (const page of donnees.pages) page.norm = normaliser(page.t)
    index.value = donnees
  } catch {
    erreur.value = true
    return
  }
  if (params.get('theme')) choix.value = { type: 'theme', id: params.get('theme')! }
  else if (params.get('produit')) choix.value = { type: 'produit', id: params.get('produit')! }
  else if (params.get('q')) saisie.value = params.get('q')!
})
</script>

<template>
  <div class="rk-recherche">
    <section class="rk-recherche-tete">
      <p class="rk-pill">Rechercher</p>
      <h1>Chercher dans <mark>le traité</mark></h1>
      <p class="rk-sub">Un mot, un produit, une question : on te montre les pages qui en parlent. Un clic ouvre le PDF à la bonne page.</p>
      <form class="rk-champ" role="search" @submit.prevent>
        <label for="rk-q" class="rk-sr">Mot-clé</label>
        <input
          id="rk-q"
          v-model="saisie"
          type="search"
          autocomplete="off"
          placeholder="Ex. : hydratation, GHB, placebo, « coup de chaleur »"
        >
      </form>
      <p class="rk-astuce">Les accents et majuscules ne comptent pas. Plusieurs mots : on garde les pages qui les contiennent tous. Entre guillemets : l’expression exacte.</p>
    </section>

    <p v-if="erreur" class="rk-sub">L’index de recherche n’a pas pu être chargé. Recharge la page, ou ouvre directement le PDF.</p>
    <p v-else-if="!index" class="rk-sub">Chargement de l’index…</p>

    <template v-else>

      <section v-if="vue" ref="resultats" class="rk-resultats" aria-live="polite">
        <header>
          <h2 v-if="vue.titre">{{ vue.titre }}</h2>
          <p v-if="vue.mots.length" class="rk-astuce">Mots cherchés : {{ vue.mots.join(', ') }}</p>
        </header>

        <div v-if="vue.parties.length" class="rk-parties">
          <h3>{{ vue.autres ? 'Les parties du traité sur ce thème' : 'Parties dont le titre correspond' }}</h3>
          <ul>
            <li v-for="p in vue.parties" :key="p.page + p.titre">
              <a :href="lien(p.page)" target="_blank" rel="noopener">
                <span class="rk-code">{{ p.code || '·' }}</span>
                <span>{{ p.titre }}</span>
                <span class="rk-p">{{ pages(p) }}</span>
              </a>
            </li>
          </ul>
        </div>

        <h3>
          <template v-if="vue.autres">Ailleurs dans le traité</template>
          <template v-else>Pages qui en parlent</template>
          <span class="rk-compte">{{ vue.resultats.length }} page{{ vue.resultats.length > 1 ? 's' : '' }}</span>
        </h3>
        <p v-if="!vue.resultats.length" class="rk-sub">
          Rien trouvé{{ termes.length > 1 ? ' avec tous ces mots sur une même page. Essaie avec moins de mots' : '. Essaie un autre mot ou le début du mot' }}.
        </p>
        <ol class="rk-liste">
          <li v-for="r in vue.resultats.slice(0, limite)" :key="r.page.n">
            <a :href="lien(r.page.n)" target="_blank" rel="noopener">
              <span class="rk-fil">{{ chapitre(partieDe(r.page)) }}</span>
              <strong>
                <span v-if="partieDe(r.page)?.code" class="rk-code">{{ partieDe(r.page)!.code }}</span>
                {{ partieDe(r.page)?.titre }}
              </strong>
              <span class="rk-extrait" v-html="r.extrait"></span>
              <span class="rk-p">Page {{ r.page.n }} · {{ r.score }} mention{{ r.score > 1 ? 's' : '' }} →</span>
            </a>
          </li>
        </ol>
        <button v-if="vue.resultats.length > limite" type="button" class="rk-btn rk-btn--line rk-plus" @click="limite += 20">
          Voir plus de pages
        </button>
      </section>
      <section class="rk-filtres">
        <p v-if="vue" class="rk-astuce">Ou explore autrement :</p>
        <h2>Par thème</h2>
        <div class="rk-pastilles">
          <button
            v-for="t in index.themes"
            :key="t.id"
            type="button"
            :class="{ actif: choix?.type === 'theme' && choix.id === t.id }"
            :aria-pressed="choix?.type === 'theme' && choix.id === t.id"
            @click="choisir('theme', t.id)"
          >{{ t.label }}</button>
        </div>
        <h2>Par produit</h2>
        <div class="rk-pastilles rk-pastilles--produits">
          <button
            v-for="p in index.produits"
            :key="p.id"
            type="button"
            :class="{ actif: choix?.type === 'produit' && choix.id === p.id }"
            :aria-pressed="choix?.type === 'produit' && choix.id === p.id"
            @click="choisir('produit', p.id)"
          >{{ p.label }}</button>
        </div>
      </section>
    </template>

    <p class="rk-astuce rk-pied">Les liens ouvrent le PDF dans un nouvel onglet, à la page indiquée. Sur certains téléphones, le PDF s’ouvre au début : la page est indiquée sur chaque résultat.</p>
  </div>
</template>
