<template>
  <section class="risk-home">
    <div class="risk-hero">
      <img class="risk-hero-logo" src="/risky-logo.png" alt="Risky">
      <div class="risk-hero-copy">
        <p class="risk-kicker">Risky</p>
        <h1>Traité de réduction des risques et des dommages</h1>
        <p class="risk-lead">Lire le traité, retrouver une information, comprendre un risque, vérifier un sujet sans devoir fouiller partout.</p>
      </div>
    </div>

    <div class="home-action-grid" aria-label="Acces principaux">
      <a class="home-action-card home-action-card--pdf" href="/traite-rdr.pdf">
        <span class="home-action-label">1</span>
        <strong>Telecharger gratuitement le traite en PDF</strong>
        <span>La version complete, figee, lisible hors ligne et facile a partager.</span>
      </a>

      <div class="home-action-card home-action-card--search">
        <span class="home-action-label">2</span>
        <strong>Chercher par mots-cles</strong>
        <span>Utilise la recherche locale du site pour retrouver un produit, une notion ou un passage precis.</span>
        <SearchLauncher />
      </div>

      <a class="home-action-card" href="/themes">
        <span class="home-action-label">3</span>
        <strong>Chercher par theme</strong>
        <span>Parcours le traite par grandes questions : croyances, science, produits, corps, situations critiques, testing.</span>
      </a>

      <a class="home-action-card" href="/sommaire">
        <span class="home-action-label">4</span>
        <strong>Voir le sommaire complet</strong>
        <span>Accede aux 22 chapitres canoniques dans l'ordre du traite, avec les pages PDF.</span>
      </a>
    </div>

    <div class="quick-topic-band">
      <h2>Acces rapides</h2>
      <div class="topic-chip-grid">
        <a href="/01_source_canonique/02_mythes_croyances_heuristiques_biais_sophismes">Mythes et biais</a>
        <a href="/01_source_canonique/04_comprendre_science_preuves_causalite">Science et preuves</a>
        <a href="/01_source_canonique/08_gestion_des_risques">Gestion des risques</a>
        <a href="/01_source_canonique/17_badtrip_overdose">Badtrip / overdose</a>
        <a href="/01_source_canonique/18_interactions_melanges">Interactions / melanges</a>
        <a href="/01_source_canonique/19_testing_analyses_produits_biologie">Testing / analyses</a>
        <a href="/01_source_canonique/15_sexualite_vulnerabilite_consentement">Sexualite / consentement</a>
        <a href="/substances">Substances mentionnees</a>
      </div>
    </div>

    <div class="reader-note">
      <h2>Ce site sert a quoi ?</h2>
      <p>Le traite complet reste disponible, mais l'accueil sert de boussole : chercher vite, lire par theme, ouvrir le PDF ou reprendre le document dans l'ordre.</p>
      <p>Cette ressource donne de l'information generale de reduction des risques. Elle ne remplace pas une aide medicale, ne garantit pas la securite d'une pratique et ne constitue pas une incitation a consommer.</p>
    </div>
  </section>
</template>
