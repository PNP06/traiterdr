<script setup lang="ts">
function openSearch() {
  const selectors = [
    '.DocSearch-Button',
    '.VPNavBarSearch button',
    '.VPSearch button',
    'button[aria-label*="Search"]',
    'button[aria-label*="search"]',
    'button[aria-label*="Rechercher"]',
    'button[aria-label*="rechercher"]'
  ]

  for (const selector of selectors) {
    const target = document.querySelector<HTMLElement>(selector)
    if (target) {
      target.click()
      target.focus()
      return
    }
  }

  window.dispatchEvent(new KeyboardEvent('keydown', {
    key: 'k',
    code: 'KeyK',
    ctrlKey: true,
    bubbles: true
  }))
}
</script>

<template>
  <button class="search-launcher" type="button" @click="openSearch">
    Chercher par mots-cles
  </button>
</template>
