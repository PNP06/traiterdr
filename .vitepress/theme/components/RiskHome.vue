<script setup lang="ts">
import SearchLauncher from './SearchLauncher.vue'

const base = '/01_source_canonique/'

const questions = [
  { q: 'Un verre de vin, c’est bon pour la santé ?', tag: 'Alcool', link: `${base}05_mythes_alcool_tabac_prix_sante_publique#boire-un-verre-de-vin-est-bon-pour-la-sante` },
  { q: 'L’alcool, ça réchauffe ?', tag: 'Thermie', link: `${base}16_allergie_convulsions_hydratation_thermie#hyper-et-hypothermie` },
  { q: 'Naturel, donc plus sûr ?', tag: 'Croyances', link: `${base}06_mythes_sucre_naturel_reste_perche_contact_addiction#naturel-plus-sur` },
  { q: 'Accro dès la première prise ?', tag: 'Addiction', link: `${base}06_mythes_sucre_naturel_reste_perche_contact_addiction#accro-a-la-premiere-prise` },
  { q: 'Le placebo, ça marche vraiment ?', tag: 'Psychologie', link: `${base}12_psychologie_placebo_nocebo_troubles_psychologiques#effets-placebo-et-nocebo` },
  { q: 'Quelle drogue fait le plus de dégâts ?', tag: 'Classifications', link: `${base}13_classifications_substances#classification-selon-les-dommages-causes-a-soi-et-aux-autres` }
]

const parts = [
  { n: '01', title: 'Cadre, sources et posture RDR', text: 'Le périmètre du traité et comment le lire.', link: `${base}01_introduction_cadre_objectif_sources` },
  { n: '02', title: 'Croyances, biais et idées reçues', text: 'Les raccourcis mentaux qui faussent nos choix.', link: `${base}02_mythes_croyances_heuristiques_biais_sophismes` },
  { n: '03', title: 'Science et preuves', text: 'Distinguer l’établi, le probable et le rapporté.', link: `${base}04_comprendre_science_preuves_causalite` },
  { n: '04', title: 'Corps, cerveau et produits', text: 'Synapses, tolérance, pharmacologie, classifications.', link: `${base}09_cerveau_synapses_neurotransmetteurs_circuits` },
  { n: '05', title: 'Situations à risque', text: 'Sommeil, sexualité, chaleur, badtrip, overdose.', link: `${base}14_risques_generiques_sommeil_juridique` },
  { n: '06', title: 'Mélanges, testing et après', text: 'Interactions, analyses, descente et dépendance.', link: `${base}18_interactions_melanges` }
]
</script>

<template>
  <div class="rk-home">
    <section class="rk-hero">
      <div class="rk-hero-inner">
        <div class="rk-hero-copy">
          <p class="rk-brand">risky</p>
          <h1>Le traité de <mark>réduction des risques</mark></h1>
          <p class="rk-lead">
            Substances psychoactives &amp; santé : comprendre sans bac+5.
            Factuel, sourcé, sans jugement.
          </p>
          <div class="rk-actions">
            <a class="rk-btn rk-btn--anis" href="/lire">Commencer la lecture</a>
            <a class="rk-btn rk-btn--ghost" href="/sommaire">Sommaire</a>
            <a class="rk-btn rk-btn--ghost" href="/pdf">PDF</a>
          </div>
          <div class="rk-search">
            <SearchLauncher />
          </div>
        </div>
        <div class="rk-hero-koala" aria-hidden="true">
          <img src="/koala.webp" alt="" width="512" height="512">
        </div>
      </div>
    </section>

    <section class="rk-section">
      <p class="rk-pill">Les idées reçues</p>
      <h2>Commence par une <mark>question</mark></h2>
      <p class="rk-sub">Les mêmes que sur Instagram, avec la réponse complète et ses sources.</p>
      <div class="rk-questions">
        <a v-for="item in questions" :key="item.q" class="rk-question" :href="item.link">
          <span class="rk-question-tag">{{ item.tag }}</span>
          <strong>{{ item.q }}</strong>
          <span class="rk-question-cta">Lire la réponse →</span>
        </a>
      </div>
    </section>

    <section class="rk-section">
      <p class="rk-pill">Le traité</p>
      <h2>Lire par <mark>grandes parties</mark></h2>
      <ol class="rk-parts">
        <li v-for="part in parts" :key="part.n">
          <a :href="part.link">
            <span class="rk-part-n">{{ part.n }}</span>
            <span>
              <strong>{{ part.title }}</strong>
              <span>{{ part.text }}</span>
            </span>
          </a>
        </li>
      </ol>
      <div class="rk-links">
        <a href="/essentiels">Passages essentiels</a>
        <a href="/figures">Galerie des figures</a>
        <a href="/substances">Substances citées</a>
        <a href="/references">Références</a>
      </div>
    </section>

    <section class="rk-insta">
      <div>
        <p class="rk-brand rk-brand--small">risky</p>
        <h2>Une idée reçue par semaine sur Instagram</h2>
        <p>Des carrousels courts, tirés de ce traité, pour comprendre pour mieux choisir.</p>
      </div>
      <a class="rk-btn rk-btn--anis" href="https://www.instagram.com/risky.asso/" target="_blank" rel="noopener">Suivre @risky.asso</a>
    </section>

  </div>
</template>
