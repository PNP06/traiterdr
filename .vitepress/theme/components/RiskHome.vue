<template>
  <section class="risk-home">
    <header class="risk-hero">
      <div class="risk-hero-copy">
        <p class="risk-kicker">Traité documentaire</p>
        <h1>Réduction des risques et des dommages</h1>
        <p class="risk-lead">
          Une lecture structurée du traité : commencer par le cadre, suivre les parties
          dans l'ordre, ou retrouver directement un passage précis.
        </p>
        <div class="risk-hero-actions" aria-label="Action principale">
          <a class="risk-button risk-button--primary" href="/lire">Commencer la lecture</a>
          <a class="risk-text-link" href="/sommaire">Sommaire complet</a>
          <a class="risk-text-link" href="/traite-rdr.pdf">PDF</a>
        </div>
      </div>

      <aside class="risk-search-panel" aria-label="Recherche dans le traité">
        <div>
          <p class="panel-eyebrow">Recherche</p>
          <h2>Retrouver une notion</h2>
          <p>Produit, interaction, risque, preuve, figure ou chapitre.</p>
        </div>
        <SearchLauncher />
      </aside>
    </header>

    <section class="home-reading-map" aria-labelledby="reading-map-title">
      <div class="home-reading-intro">
        <p class="section-kicker">Prise de lecture</p>
        <h2 id="reading-map-title">Lire par parties du traité</h2>
        <p>
          Ces entrées ne remplacent pas le sommaire : elles donnent une progression
          lisible dans le corpus, depuis le cadre jusqu'aux situations concrètes.
        </p>
      </div>

      <ol class="home-reading-list">
        <li>
          <a href="/01_source_canonique/01_introduction_cadre_objectif_sources">
            <span class="home-step">01</span>
            <strong>Cadre, sources et posture RDR</strong>
            <span>Comprendre le périmètre du traité et son mode de lecture.</span>
          </a>
        </li>
        <li>
          <a href="/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes">
            <span class="home-step">02</span>
            <strong>Croyances, biais et réception de l'information</strong>
            <span>Identifier les raccourcis mentaux et les freins à une information utile.</span>
          </a>
        </li>
        <li>
          <a href="/01_source_canonique/04_comprendre_science_preuves_causalite">
            <span class="home-step">03</span>
            <strong>Preuves, science et gestion des risques</strong>
            <span>Distinguer ce qui est établi, incertain, probable ou seulement rapporté.</span>
          </a>
        </li>
        <li>
          <a href="/01_source_canonique/09_cerveau_synapses_neurotransmetteurs_circuits">
            <span class="home-step">04</span>
            <strong>Corps, cerveau, effets et classifications</strong>
            <span>Lire les bases biologiques, pharmacologiques et les classifications.</span>
          </a>
        </li>
        <li>
          <a href="/01_source_canonique/14_risques_generiques_sommeil_juridique">
            <span class="home-step">05</span>
            <strong>Risques transversaux et situations critiques</strong>
            <span>Sommeil, sexualité, thermie, badtrip, overdose et vulnérabilités.</span>
          </a>
        </li>
        <li>
          <a href="/01_source_canonique/18_interactions_melanges">
            <span class="home-step">06</span>
            <strong>Interactions, testing, descente et dépendance</strong>
            <span>Comprendre les mélanges, les analyses, les suites et les usages problématiques.</span>
          </a>
        </li>
      </ol>
    </section>

    <nav class="home-reference-row" aria-label="Index secondaires">
      <a href="/essentiels">
        <strong>Passages essentiels</strong>
        <span>Une entrée courte pour s'orienter.</span>
      </a>
      <a href="/figures">
        <strong>Figures</strong>
        <span>Schémas et infographies contextualisés.</span>
      </a>
      <a href="/substances">
        <strong>Substances citées</strong>
        <span>Retrouver les passages par produit mentionné.</span>
      </a>
    </nav>

    <p class="reader-note">
      Ressource documentaire de réduction des risques. Information générale, non incitative,
      non médicale personnalisée.
    </p>
  </section>
</template>
