<script setup lang="ts">
import { treatyTocEntryCount, treatyTocSections } from '../../treatyToc'
</script>

<template>
  <nav class="treaty-toc" aria-label="Sommaire complet du traité">
    <div class="treaty-toc-summary" aria-label="Grandes parties">
      <a
        v-for="section in treatyTocSections"
        :key="section.text"
        :href="section.link"
      >
        <strong>{{ section.text }}</strong>
        <span>p. {{ section.page }} / PDF {{ section.pdfPage }}</span>
      </a>
    </div>

    <p class="treaty-toc-count">
      {{ treatyTocEntryCount }} entrées de navigation issues des pages 5 à 8 du PDF.
    </p>

    <section
      v-for="section in treatyTocSections"
      :key="section.text"
      class="treaty-toc-section"
    >
      <header class="treaty-toc-section-header">
        <a :href="section.link">{{ section.text }}</a>
        <a class="treaty-toc-pdf" :href="section.pdfLink">PDF {{ section.pdfPage }}</a>
      </header>

      <ol class="treaty-toc-list">
        <li
          v-for="entry in section.entries"
          :key="`${section.text}-${entry.text}-${entry.page}-${entry.level}`"
          class="treaty-toc-entry"
          :class="`treaty-toc-entry--level-${entry.level}`"
        >
          <a class="treaty-toc-link" :href="entry.link">{{ entry.text }}</a>
          <span class="treaty-toc-page">p. {{ entry.page }} / PDF {{ entry.pdfPage }}</span>
          <a class="treaty-toc-pdf" :href="entry.pdfLink">PDF</a>
        </li>
      </ol>
    </section>
  </nav>
</template>
