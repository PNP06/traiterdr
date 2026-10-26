<script setup lang="ts">
const pdf = '/traite-rdr.pdf'
const epub = '/traite-rdr.epub'

const questions = [
  'Un verre de vin par jour, c’est bon pour la santé ?',
  'L’alcool, ça réchauffe ?',
  'Naturel, donc plus sûr ?',
  'Accro dès la première prise ?',
  'Le placebo, ça marche vraiment ?',
  'Quelle drogue fait le plus de dégâts ?'
]

const raccourcis = [
  { label: 'Overdose et secours', href: '/recherche?theme=overdose' },
  { label: 'Mélanges', href: '/recherche?theme=melanges' },
  { label: 'Chaleur et hydratation', href: '/recherche?theme=chaleur' },
  { label: 'Sexualité et consentement', href: '/recherche?theme=sexualite' },
  { label: 'Alcool', href: '/recherche?produit=alcool' },
  { label: 'GHB', href: '/recherche?produit=ghb' },
  { label: 'Cannabis', href: '/recherche?produit=cannabis' },
  { label: 'MDMA', href: '/recherche?produit=mdma' }
]

const parts = [
  { title: 'Bien raisonner', text: 'Mythes, heuristiques, biais, sophismes : pourquoi on se trompe sur les drogues, et comment corriger une croyance sans braquer.' },
  { title: 'Comprendre la science', text: 'Ce qu’est une preuve, la différence entre corrélation et causalité, comment lire une étude.' },
  { title: 'Les idées reçues', text: 'Dry January, prix de l’alcool, verre de vin, sucre, naturel, contamination par contact, GHB, chemsex, RC.' },
  { title: 'Le corps et le cerveau', text: 'Synapses et neurotransmetteurs, tolérance, cerveau de 15 à 25 ans, ce que devient une substance dans le corps.' },
  { title: 'Les produits', text: 'Classifications des substances par effets, par dommages et par statut légal.' },
  { title: 'Les risques', text: 'Sommeil, sexualité et consentement, chaleur et hydratation, badtrip, overdose, mélanges, testing, descente et addiction.' }
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
            <a class="rk-btn rk-btn--anis" href="#lire">Lire le traité</a>
            <a class="rk-btn rk-btn--ghost" :href="pdf" download>Télécharger le PDF</a>
          </div>
        </div>
        <div class="rk-hero-koala" aria-hidden="true">
          <img src="/koala.webp" alt="" width="512" height="512">
        </div>
      </div>
    </section>

    <section class="rk-section">
      <p class="rk-pill">Le projet</p>
      <h2>Ce qu’on aurait aimé <mark>savoir plus tôt</mark></h2>
      <div class="rk-about">
        <p>
          Les infos sur les drogues sont souvent fausses, trop techniques ou trop simplifiées.
          Ce traité rassemble les bases scientifiques utiles pour réduire les risques : ce que
          fait une substance dans le corps, pourquoi certaines croyances sont dangereuses, et
          quoi faire quand ça se passe mal.
        </p>
        <p>
          Commencé en 2020 par l’association Risky, il est enrichi d’échanges avec des médecins
          et des associations de réduction des risques. Il ne dit pas quoi faire : il donne de quoi
          choisir en connaissance de cause.
        </p>
      </div>
    </section>

    <section class="rk-section rk-cherche">
      <p class="rk-pill">Chercher</p>
      <h2>Une question précise ? <mark>Cherche-la</mark></h2>
      <form class="rk-champ" action="/recherche" method="get" role="search">
        <label for="rk-accueil-q" class="rk-sr">Mot-clé</label>
        <input id="rk-accueil-q" name="q" type="search" placeholder="Ex. : hydratation, GHB, placebo…">
        <button class="rk-btn rk-btn--sapin" type="submit">Rechercher</button>
      </form>
      <div class="rk-pastilles">
        <a v-for="r in raccourcis" :key="r.href" :href="r.href">{{ r.label }}</a>
        <a href="/recherche" class="rk-pastille-tout">Tous les thèmes →</a>
      </div>
    </section>

    <section class="rk-section">
      <p class="rk-pill">Au sommaire</p>
      <h2>Ce que tu trouves <mark>dedans</mark></h2>
      <ul class="rk-parts">
        <li v-for="part in parts" :key="part.title">
          <strong>{{ part.title }}</strong>
          <span>{{ part.text }}</span>
        </li>
      </ul>
    </section>

    <section class="rk-section">
      <p class="rk-pill">Les idées reçues</p>
      <h2>Des questions qu’on se pose <mark>en soirée</mark></h2>
      <p class="rk-sub">Le traité y répond, sources à l’appui. On en traite une par semaine sur Instagram.</p>
      <ul class="rk-questions">
        <li v-for="q in questions" :key="q" class="rk-question">{{ q }}</li>
      </ul>
    </section>

    <section id="lire" class="rk-section rk-reader">
      <p class="rk-pill">Lire</p>
      <h2>Le traité, <mark>en entier</mark></h2>
      <div class="rk-reader-actions">
        <a class="rk-btn rk-btn--sapin" :href="pdf" target="_blank" rel="noopener">Ouvrir en plein écran</a>
        <a class="rk-btn rk-btn--line" :href="pdf" download>Télécharger le PDF</a>
        <a class="rk-btn rk-btn--line" :href="epub" download>Télécharger pour liseuse</a>
      </div>
      <p class="rk-sub rk-epub-note">Version liseuse (EPUB) : Kobo, Kindle, Apple Livres, Google Play Livres. Le texte s'adapte à l'écran, les notes s'ouvrent d'un clic.</p>
      <div class="rk-pdf">
        <iframe :src="`${pdf}#view=FitH`" title="Traité de réduction des risques (PDF)" loading="lazy"></iframe>
      </div>
      <p class="rk-sub rk-pdf-mobile">Sur téléphone, ouvre le PDF en plein écran ou télécharge-le pour le lire tranquillement.</p>
    </section>

    <section class="rk-insta">
      <div>
        <p class="rk-brand rk-brand--small">risky</p>
        <h2>Une idée reçue par semaine sur Instagram</h2>
        <p>Des carrousels courts, tirés du traité. Comprendre pour mieux choisir.</p>
      </div>
      <a class="rk-btn rk-btn--anis" href="https://www.instagram.com/risky.asso/" target="_blank" rel="noopener">Suivre @risky.asso</a>
    </section>
  </div>
</template>
