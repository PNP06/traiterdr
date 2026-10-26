import DefaultTheme from 'vitepress/theme'
import { inBrowser } from 'vitepress'
import RiskHome from './components/RiskHome.vue'
import RiskSearch from './components/RiskSearch.vue'
import SearchLauncher from './components/SearchLauncher.vue'
import TreatyToc from './components/TreatyToc.vue'
import './custom.css'

// Agrandit une figure du traité au clic ; un second clic ou Échap referme.
function setupFigureZoom() {
  document.addEventListener('click', (event) => {
    const img = (event.target as HTMLElement).closest<HTMLImageElement>('.doc-figure img, .figure-card img')
    if (!img) return

    const overlay = document.createElement('div')
    overlay.className = 'rk-lightbox'
    overlay.setAttribute('role', 'dialog')
    overlay.setAttribute('aria-label', img.alt || 'Figure agrandie')

    const large = document.createElement('img')
    large.src = img.currentSrc || img.src
    large.alt = img.alt
    overlay.appendChild(large)

    const close = () => {
      overlay.remove()
      document.removeEventListener('keydown', onKey)
    }
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') close()
    }

    overlay.addEventListener('click', close)
    document.addEventListener('keydown', onKey)
    document.body.appendChild(overlay)
  })
}

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('RiskHome', RiskHome)
    app.component('RiskSearch', RiskSearch)
    app.component('SearchLauncher', SearchLauncher)
    app.component('TreatyToc', TreatyToc)

    if (inBrowser) setupFigureZoom()
  }
}
