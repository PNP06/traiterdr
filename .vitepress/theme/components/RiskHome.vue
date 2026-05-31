<template>
  <section class="risk-home">
    <div class="risk-hero">
      <div class="risk-hero-copy">
        <p class="risk-kicker">Portail documentaire RDR</p>
        <h1>Traité de réduction des risques et des dommages</h1>
        <p class="risk-lead">Lire le traité, choisir une partie, retrouver une notion ou ouvrir le PDF complet sans devoir fouiller dans tout le corpus.</p>
        <div class="risk-hero-actions" aria-label="Actions prioritaires">
          <a class="risk-button risk-button--primary" href="/lire">Lire le traité</a>
          <a class="risk-button" href="/essentiels">Passages prioritaires</a>
          <a class="risk-button risk-button--quiet" href="/traite-rdr.pdf">PDF complet</a>
        </div>
        <div class="risk-trust-row" aria-label="Repères du corpus">
          <span>22 chapitres canoniques</span>
          <span>Recherche locale</span>
          <span>Figures contextualisées</span>
        </div>
      </div>

      <aside class="risk-hero-panel" aria-label="Recherche rapide">
        <img class="risk-hero-logo" src="/risky-logo.png" alt="Risky">
        <div>
          <span class="panel-eyebrow">Accès direct</span>
          <h2>Chercher une notion</h2>
          <p>Produit, interaction, risque, preuve, situation critique ou passage du traité.</p>
        </div>
        <SearchLauncher />
        <a class="panel-link" href="/sommaire">Voir le sommaire complet</a>
      </aside>
    </div>

    <div class="home-section-heading">
      <p class="section-kicker">Choisir une entrée</p>
      <h2>Les chemins les plus utiles</h2>
    </div>

    <div class="home-action-grid" aria-label="Accès principaux">
      <a class="home-action-card home-action-card--featured" href="/traite-rdr.pdf">
        <span class="home-action-label">PDF</span>
        <strong>Télécharger le traité complet</strong>
        <span>Version figée, lisible hors ligne, pratique à partager ou annoter.</span>
      </a>

      <a class="home-action-card" href="/lire">
        <span class="home-action-label">Lire</span>
        <strong>Suivre un parcours de lecture</strong>
        <span>Entrer dans le traité par objectif de lecture, sans perdre l'ordre des chapitres.</span>
      </a>

      <a class="home-action-card" href="/sommaire">
        <span class="home-action-label">Sommaire</span>
        <strong>Voir toutes les parties</strong>
        <span>Parcourir les 22 chapitres canoniques dans l'ordre du traité.</span>
      </a>

      <a class="home-action-card" href="/figures">
        <span class="home-action-label">Figures</span>
        <strong>Voir les figures utiles</strong>
        <span>Retrouver les schémas et infographies avec le chapitre qui leur donne leur contexte.</span>
      </a>
    </div>

    <div class="home-split-section">
      <section class="home-library-card">
        <div class="home-section-heading home-section-heading--compact">
          <p class="section-kicker">Entrer dans le texte</p>
          <h2>Parties du traité</h2>
        </div>
        <div class="topic-chip-grid">
          <a href="/01_source_canonique/01_introduction_cadre_objectif_sources">Cadre et sources</a>
          <a href="/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes">Croyances et biais</a>
          <a href="/01_source_canonique/04_comprendre_science_preuves_causalite">Science et preuves</a>
          <a href="/01_source_canonique/09_cerveau_synapses_neurotransmetteurs_circuits">Corps et effets</a>
          <a href="/01_source_canonique/13_classifications_substances">Classifications</a>
          <a href="/01_source_canonique/14_risques_generiques_sommeil_juridique">Risques transversaux</a>
          <a href="/01_source_canonique/18_interactions_melanges">Interactions et testing</a>
          <a href="/01_source_canonique/20_descente_sevrage_addiction_dependance">Suites et dépendance</a>
        </div>
      </section>

      <section class="home-library-card home-library-card--index">
        <div class="home-section-heading home-section-heading--compact">
          <p class="section-kicker">Organisation</p>
          <h2>Structure du portail</h2>
        </div>
        <ol class="home-index-list">
          <li><a href="/sommaire">Sommaire complet</a><span>Les 22 chapitres dans l'ordre du traité.</span></li>
          <li><a href="/essentiels">Passages à lire en premier</a><span>Une entrée plus courte pour s'orienter.</span></li>
          <li><a href="/figures">Galerie des figures</a><span>Repères visuels avec liens vers les chapitres.</span></li>
        </ol>
      </section>
    </div>

    <div class="reader-note">
      <h2>Repère de lecture</h2>
      <p>Le site organise le traité pour faciliter la consultation : sommaire, parcours, recherche, figures et PDF restent des portes d'entrée vers le même contenu documentaire.</p>
      <p>Ressource d'information générale de réduction des risques, sans personnalisation médicale ni incitation.</p>
    </div>
  </section>
</template>
