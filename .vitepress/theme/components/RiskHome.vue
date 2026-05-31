<template>
  <section class="risk-home">
    <div class="risk-hero">
      <div class="risk-hero-copy">
        <p class="risk-kicker">Portail documentaire RDR</p>
        <h1>Traité de réduction des risques et des dommages</h1>
        <p class="risk-lead">Lire le traité, retrouver une notion, explorer les risques par thème ou ouvrir le PDF complet sans devoir fouiller dans tout le corpus.</p>
        <div class="risk-hero-actions" aria-label="Actions prioritaires">
          <a class="risk-button risk-button--primary" href="/lire">Lire le traité</a>
          <a class="risk-button" href="/themes">Explorer par thème</a>
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
        <strong>Suivre un parcours guidé</strong>
        <span>Commencer par les passages prioritaires selon le temps disponible et l'objectif de lecture.</span>
      </a>

      <a class="home-action-card" href="/themes">
        <span class="home-action-label">Thèmes</span>
        <strong>Explorer par grande question</strong>
        <span>Croyances, science, produits, corps, situations critiques, interactions et testing.</span>
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
          <p class="section-kicker">Explorer vite</p>
          <h2>Thèmes fréquents</h2>
        </div>
        <div class="topic-chip-grid">
          <a href="/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes">Mythes et biais</a>
          <a href="/01_source_canonique/04_comprendre_science_preuves_causalite">Science et preuves</a>
          <a href="/01_source_canonique/08_gestion_des_risques">Gestion des risques</a>
          <a href="/01_source_canonique/13_classifications_substances">Classifications</a>
          <a href="/01_source_canonique/17_badtrip_overdose">Badtrip / overdose</a>
          <a href="/01_source_canonique/18_interactions_melanges">Interactions</a>
          <a href="/01_source_canonique/19_testing_analyses_produits_biologie">Testing / analyses</a>
          <a href="/substances">Substances mentionnées</a>
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
      <p>Le site organise le traité pour faciliter la consultation : recherche, thèmes, figures et PDF restent des portes d'entrée vers le même contenu documentaire.</p>
      <p>Ressource d'information générale de réduction des risques, sans personnalisation médicale ni incitation.</p>
    </div>
  </section>
</template>
