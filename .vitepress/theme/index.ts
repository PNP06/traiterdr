import DefaultTheme from 'vitepress/theme'
import RiskHome from './components/RiskHome.vue'
import SearchLauncher from './components/SearchLauncher.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('RiskHome', RiskHome)
    app.component('SearchLauncher', SearchLauncher)
  }
}
