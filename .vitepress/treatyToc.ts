export interface TreatyTocEntry {
  text: string
  page: number
  pdfPage: number
  link: string
  pdfLink: string
  level: 1 | 2
}

export interface TreatyTocSection {
  text: string
  page: number
  pdfPage: number
  link: string
  pdfLink: string
  entries: TreatyTocEntry[]
}

const files = {
  front: '00_front_matter_suivi_remerciements',
  intro: '01_introduction_cadre_objectif_sources',
  croyances: '02_mythes_croyances_heuristiques_biais_sophismes',
  protections: '03_mecanismes_protection_approche_rdr',
  science: '04_comprendre_science_preuves_causalite',
  alcool: '05_mythes_alcool_tabac_prix_sante_publique',
  naturel: '06_mythes_sucre_naturel_reste_perche_contact_addiction',
  ghb: '07_ghb_drogue_du_viol_chemsex_3mmc_rc_nps',
  risques: '08_gestion_des_risques',
  cerveau: '09_cerveau_synapses_neurotransmetteurs_circuits',
  tolerance: '10_tolerance_developpement_15_25_corps_humain',
  pkpd: '11_pk_pd_absorption_distribution_metabolisme_elimination',
  psychologie: '12_psychologie_placebo_nocebo_troubles_psychologiques',
  classifications: '13_classifications_substances',
  generiques: '14_risques_generiques_sommeil_juridique',
  sexualite: '15_sexualite_vulnerabilite_consentement',
  hydratation: '16_allergie_convulsions_hydratation_thermie',
  badtrip: '17_badtrip_overdose',
  interactions: '18_interactions_melanges',
  testing: '19_testing_analyses_produits_biologie',
  apres: '20_descente_sevrage_addiction_dependance',
  cancer: '21_cancer'
} as const

export const sourceFiles = files

function source(file: string, anchor?: string) {
  return `/01_source_canonique/${file}${anchor ? `#${anchor}` : ''}`
}

function pdfLink(page: number) {
  return `/traite-rdr.pdf#page=${page + 1}`
}

function section(text: string, page: number, link: string, entries: TreatyTocEntry[]): TreatyTocSection {
  return {
    text,
    page,
    pdfPage: page + 1,
    link,
    pdfLink: pdfLink(page),
    entries
  }
}

function item(text: string, page: number, link: string, level: 1 | 2 = 1): TreatyTocEntry {
  return {
    text,
    page,
    pdfPage: page + 1,
    link,
    pdfLink: pdfLink(page),
    level
  }
}

function heading(file: string, text: string, duplicate = 0) {
  const slug = slugify(text)
  return source(file, duplicate === 0 ? slug : `${slug}-${duplicate}`)
}

function slugify(text: string) {
  return text
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[\u0000-\u001f]/g, '')
    .replace(/[\s~`!@#$%^&*()\-_+=[\]{}|\\;:"'“”‘’<>,.?/]+/g, '-')
    .replace(/-{2,}/g, '-')
    .replace(/^-+|-+$/g, '')
    .replace(/^(\d)/, '_$1')
    .toLowerCase()
}

export const treatyTocSections: TreatyTocSection[] = [
  section('Ouverture', 0, source(files.front), [
    item('SUIVI', 0, heading(files.front, 'Page imprimée 0 / PDF 1 - Suivi éditorial et page titre')),
    item('Remerciements', 7, heading(files.front, 'Page imprimée 7 / PDF 8 - Remerciements')),
    item('Introduction', 8, source(files.intro))
  ]),
  section('Mythes', 16, source(files.croyances), [
    item('Création des croyances', 18, heading(files.croyances, 'Page imprimée 18 / PDF 19 — Croyances et risques')),
    item('Heuristique', 18, heading(files.croyances, 'Pages imprimées 18-20 / PDF 19-21 — Heuristiques'), 2),
    item('Biais', 21, heading(files.croyances, 'Pages imprimées 21-22 / PDF 22-23 — Biais cognitifs'), 2),
    item('Sophisme', 23, heading(files.croyances, 'Pages imprimées 23-28 / PDF 24-29 — Sophismes'), 2),
    item('Mécanisme de protection psychologique', 29, heading(files.protections, '1. Pourquoi la logique ne suffit pas'), 2),
    item('Approche en réduction des risques', 34, heading(files.protections, '8. Approche en réduction des risques'), 2),
    item('Conclusion', 42, heading(files.protections, '12. Conclusion'), 2),
    item('Comprendre la science', 45, source(files.science)),
    item('Science et recherche', 45, heading(files.science, '2. Science et recherche'), 2),
    item('La méthode Scientifique', 48, heading(files.science, '7. La méthode scientifique'), 2),
    item('Le mois sans alcool/sans tabac est inutile', 51, heading(files.alcool, 'Le mois sans alcool/sans tabac est inutile')),
    item('Effet individuel', 51, heading(files.alcool, 'Effet individuel'), 2),
    item('Effet sur la santé publique', 53, heading(files.alcool, 'Effet sur la santé publique'), 2),
    item('L’alcool et le tabac sont rentables pour l’état', 54, heading(files.alcool, 'L’alcool et le tabac sont rentables pour l’état')),
    item('Focus sur les finances publiques pour l’alcool', 54, heading(files.alcool, 'Focus sur les finances publiques pour l’alcool'), 2),
    item('Cout social total', 55, heading(files.alcool, 'Cout social total'), 2),
    item('Augmentation des taxes pour l’équilibre', 58, heading(files.alcool, 'Augmentation des taxes pour l’équilibre'), 2),
    item('Effet du prix sur la consommation', 59, heading(files.alcool, 'Effet du prix sur la consommation')),
    item('Boire un verre de vin est bon pour la santé', 61, heading(files.alcool, 'Boire un verre de vin est bon pour la santé')),
    item('Le problème général : prouver le lien de causalité', 61, heading(files.alcool, 'Le problème général : prouver le lien de causalité'), 2),
    item('Conclusion', 67, heading(files.alcool, 'Conclusion'), 2),
    item('Toxicité comparée des différents alcools', 69, heading(files.alcool, 'Toxicité comparée des différents alcools'), 2),
    item('« Addiction » au sucre ?', 70, heading(files.naturel, '« Addiction » au sucre ?')),
    item('Naturel = plus sûr ?', 73, heading(files.naturel, 'Naturel = plus sûr ?')),
    item('Biais de naturalité', 74, heading(files.naturel, 'Biais de naturalité'), 2),
    item('Une frontière assez fine', 77, heading(files.naturel, 'Une frontière assez fine'), 2),
    item('Le milieu et la transformation', 79, heading(files.naturel, 'Le milieu et la transformation'), 2),
    item('La Naturalité n\'équivaut pas à la Sécurité', 83, heading(files.naturel, 'La Naturalité n\'équivaut pas à la Sécurité'), 2),
    item('Resté perché ?', 85, heading(files.naturel, 'Resté perché ?')),
    item('Badtrip traumatisant', 85, heading(files.naturel, 'Badtrip traumatisant'), 2),
    item('Trouble sous-jacent', 85, heading(files.naturel, 'Trouble sous-jacent'), 2),
    item('Flashbacks et HPPD', 86, heading(files.naturel, 'Flashbacks et HPPD'), 2),
    item('Atteinte neurologique lié à un usage chronique', 87, heading(files.naturel, 'Atteinte neurologique lié à un usage chronique'), 2),
    item('Problèmes liés à l’addiction', 87, heading(files.naturel, 'Problèmes liés à l’addiction'), 2),
    item('Contamination par contact', 88, heading(files.naturel, 'Contamination par contact')),
    item('Accro à la première prise', 88, heading(files.naturel, 'Accro à la première prise')),
    item('Le taux de conversion en fonction des substances', 90, heading(files.naturel, 'Le taux de conversion en fonction des substances'), 2),
    item('Drogue du zombie', 91, heading(files.ghb, 'Drogue du zombie')),
    item('Drogue du viol', 92, heading(files.ghb, 'Drogue du viol')),
    item('Position des associations de réduction des risques sur le GHB', 94, heading(files.ghb, 'Position des associations de réduction des risques sur le GHB'), 2),
    item('Chemsex, usage sexualisé des drogues et 3-MMC', 94, heading(files.ghb, 'Chemsex, usage sexualisé des drogues et 3-MMC')),
    item('Zoom sur la 3-MMC', 95, heading(files.ghb, 'Zoom sur la 3-MMC'), 2),
    item('Les « research chemical » ou « Nouveau produits de synthèses »', 95, heading(files.ghb, 'Les « research chemical » ou « Nouveau produits de synthèses »')),
    item('La réglementation antidrogue', 96, heading(files.ghb, 'La réglementation antidrogue'), 2),
    item('La synthèse de prodrogue', 96, heading(files.ghb, 'La synthèse de prodrogue'), 2),
    item('Les dosages de RC', 97, heading(files.ghb, 'Les dosages de RC'), 2),
    item('Le jeu du « chat et la souris »', 97, heading(files.ghb, 'Le jeu du « chat et la souris »'), 2),
    item('Les risques juridiques', 98, heading(files.ghb, 'Les risques juridiques'), 2),
    item('Darknet versus sites de RC', 98, heading(files.ghb, 'Darknet versus sites de RC'), 2)
  ]),
  section('La gestion des risques', 99, heading(files.risques, 'La gestion des risques'), [
    item('Risques majeurs, risques mineurs', 100, heading(files.risques, 'Risques majeurs, risques mineurs')),
    item('Diminuer les risques', 102, heading(files.risques, 'Diminuer les risques'))
  ]),
  section('Le cerveau et le corps', 103, heading(files.cerveau, 'Le cerveau et le corps'), [
    item('Le cerveau', 104, heading(files.cerveau, 'Le cerveau')),
    item('Le fonctionnement des synapses', 105, heading(files.cerveau, 'Le fonctionnement des synapses'), 2),
    item('Les neurotransmetteurs', 109, heading(files.cerveau, 'Les neurotransmetteurs'), 2),
    item('Les circuits cérébraux', 113, heading(files.cerveau, 'Les circuits cérébraux'), 2),
    item('Tolérance, Accoutumance, Tachyphylaxie', 115, heading(files.tolerance, 'Tolérance, Accoutumance, Tachyphylaxie'), 2),
    item('Le développement du cerveau de 15 à 25 ans', 120, heading(files.tolerance, 'Le développement du cerveau de 15 à 25 ans'), 2),
    item('Le corps humain', 122, heading(files.tolerance, 'Le corps humain')),
    item('Le système nerveux', 122, heading(files.tolerance, 'Le système nerveux'), 2),
    item('Le système cannabinoïde endogène', 125, heading(files.tolerance, 'Le système cannabinoïde endogène'), 2),
    item('Le système opioïde endogène', 125, heading(files.tolerance, 'Le système opioïde endogène'), 2),
    item('Le devenir des drogues : métabolisme', 126, heading(files.pkpd, 'Le devenir des drogues : metabolisme')),
    item('Absorption et distribution', 126, heading(files.pkpd, 'Absorption et distribution'), 2),
    item('Le métabolisme : la digestion', 132, heading(files.pkpd, 'Le métabolisme : la digestion'), 2),
    item('L’élimination', 137, heading(files.pkpd, 'L’élimination'), 2),
    item('Psychologie', 140, heading(files.psychologie, 'Psychologie')),
    item('Effets placebo et nocebo', 140, heading(files.psychologie, 'Effets placebo et nocebo'), 2),
    item('Lien entre drogues et troubles psychologique', 155, heading(files.psychologie, 'Lien entre drogues et troubles psychologique'), 2)
  ]),
  section('Classification des substances', 157, heading(files.classifications, 'Classification des substances'), [
    item('Classification selon les types d’effets', 158, heading(files.classifications, 'Classification selon les types d’effets')),
    item('Les quatre grandes catégories', 158, heading(files.classifications, 'Les quatre grandes catégories'), 2),
    item('Classification générale de Derek Snider', 159, heading(files.classifications, 'Classification générale de Derek Snider'), 2),
    item('Les sous-familles', 161, heading(files.classifications, 'Les sous-familles'), 2),
    item('Classification selon les dommages causés à soi et aux autres', 164, heading(files.classifications, 'Classification selon les dommages causés à soi et aux autres')),
    item('QQOQCCP', 164, heading(files.classifications, 'QQOQCCP'), 2),
    item('Validation et limites', 165, heading(files.classifications, 'Validation et limites'), 2),
    item('Le baccalauréat TNIC « Techniques de Nuisances Individuelles et Collectives »', 166, heading(files.classifications, 'Le baccalauréat TNIC « Techniques de Nuisances Individuelles et Collectives »'), 2),
    item('Les critères et pondérations', 166, heading(files.classifications, 'Les critères et pondérations'), 2),
    item('Résultats globaux', 167, heading(files.classifications, 'Résultats globaux'), 2),
    item('Résultats pour le consommateur', 168, heading(files.classifications, 'Résultats pour le consommateur'), 2),
    item('Classifications diverses', 170, heading(files.classifications, 'Classifications diverses')),
    item('Juridique', 171, heading(files.classifications, 'Juridique'), 2),
    item('Toxicité aigüe (risque et danger)', 175, heading(files.classifications, 'Toxicité aigüe (risque et danger)'), 2),
    item('Nombres d’interactions', 179, heading(files.classifications, 'Nombres d’interactions'), 2),
    item('Criminogène', 180, heading(files.classifications, 'Criminogène'), 2),
    item('Chimique', 181, heading(files.classifications, 'Chimique'), 2)
  ]),
  section('Risques génériques', 182, heading(files.generiques, 'Risques génériques'), [
    item('Trouble du sommeil', 183, heading(files.generiques, 'Trouble du sommeil')),
    item('Risques juridiques', 183, heading(files.generiques, 'Risques juridiques')),
    item('L’amende forfaitaire délictuelle', 183, heading(files.generiques, 'L’amende forfaitaire délictuelle'), 2),
    item('Contestation de l’amende', 184, heading(files.generiques, 'Contestation de l’amende'), 2),
    item('Distinction entre les drogues', 184, heading(files.generiques, 'Distinction entre les drogues'), 2)
  ]),
  section('Risques durant la prise', 185, heading(files.sexualite, 'Risques durant la prise'), [
    item('La sexualité', 186, heading(files.sexualite, 'La sexualité')),
    item('Soumission et vulnérabilité', 186, heading(files.sexualite, 'Soumission et vulnérabilité'), 2),
    item('Alcool et sexualité', 194, heading(files.sexualite, 'Alcool et sexualité'), 2),
    item('Allergie et crise d’anaphylaxie', 198, heading(files.hydratation, 'Allergie et crise d’anaphylaxie')),
    item('Le mécanisme allergique', 198, heading(files.hydratation, 'Le mécanisme allergique'), 2),
    item('Faire un test allergique', 199, heading(files.hydratation, 'Faire un test allergique'), 2),
    item('Convulsions', 199, heading(files.hydratation, 'Convulsions')),
    item('L’hydratation', 200, heading(files.hydratation, 'L’hydratation')),
    item('Principes physiologiques de l’hydratation', 200, heading(files.hydratation, 'Principes physiologiques de l’hydratation'), 2),
    item('Bilan', 202, heading(files.hydratation, 'Bilan'), 2),
    item('Troubles de l’hydratation', 203, heading(files.hydratation, 'Troubles de l’hydratation'), 2),
    item('Hyper et hypothermie', 208, heading(files.hydratation, 'Hyper et hypothermie')),
    item('Principes physiologiques de régulation de la température', 208, heading(files.hydratation, 'Principes physiologiques de régulation de la température'), 2),
    item('Bilan', 215, heading(files.hydratation, 'Bilan', 1), 2),
    item('Troubles de la température', 216, heading(files.hydratation, 'Troubles de la température'), 2),
    item('Approche générale : Thermie et Hydratation', 222, heading(files.hydratation, 'Approche générale : Thermie et Hydratation')),
    item('Badtrip', 223, heading(files.badtrip, 'Badtrip')),
    item('Définition', 223, heading(files.badtrip, 'Définition'), 2),
    item('Eviter le badtrip', 224, heading(files.badtrip, 'Eviter le badtrip'), 2),
    item('Overdose', 230, heading(files.badtrip, 'Overdose')),
    item('Dose létale', 232, heading(files.badtrip, 'Dose létale'), 2),
    item('Échelle de toxicité aiguë', 232, heading(files.badtrip, 'Échelle de toxicité aiguë'), 2),
    item('Étapes des overdoses', 233, heading(files.badtrip, 'Étapes des overdoses'), 2),
    item('Prévenir les overdoses', 234, heading(files.badtrip, 'Prévenir les overdoses'), 2),
    item('Application à l’alcool', 237, heading(files.badtrip, 'Application à l’alcool'), 2),
    item('Interactions, mélanges', 248, heading(files.interactions, 'Interactions, mélanges')),
    item('Exemple de l’alcool', 248, heading(files.interactions, 'Exemple de l’alcool'), 2),
    item('Modes d’interaction', 249, heading(files.interactions, 'Modes d’interaction'), 2),
    item('Outils d’aide', 260, heading(files.interactions, 'Outils d’aide'), 2),
    item('Analyser des interactions', 266, heading(files.interactions, 'Analyser des interactions'), 2),
    item('Analyses des produits et analyses biologiques', 268, heading(files.testing, 'Analyses des produits et analyses biologiques')),
    item('Ou faire tester ses produits ?', 271, heading(files.testing, 'Ou faire tester ses produits ?'), 2),
    item('État des lieux du marché', 272, heading(files.testing, 'État des lieux du marché'), 2),
    item('Les différents types de tests', 279, heading(files.testing, 'Les différents types de tests'), 2)
  ]),
  section('Risques APRES', 294, heading(files.apres, 'Risques APRES'), [
    item('La descente', 294, heading(files.apres, 'La descente')),
    item('Syndrome de sevrage et delirium tremens', 294, heading(files.apres, 'Syndrome de sevrage et delirium tremens')),
    item('Addiction et dépendance', 295, heading(files.apres, 'Addiction et dépendance')),
    item('Généralités sur l’addiction', 295, heading(files.apres, 'Généralités sur l’addiction'), 2),
    item('Comment devient-on addict ?', 298, heading(files.apres, 'Comment devient-on addict ?'), 2),
    item('Se repérer dans l’addiction', 301, heading(files.apres, 'Se repérer dans l’addiction'), 2),
    item('S’en sortir', 304, heading(files.apres, 'S’en sortir'), 2),
    item('Cas de l’alcool', 314, heading(files.apres, 'Cas de l’alcool'), 2),
    item('Cancer', 327, source(files.cancer)),
    item('Fonctionnement des cellules', 327, heading(files.cancer, 'Fonctionnement des cellules'), 2)
  ])
]

export const treatyTocEntryCount = treatyTocSections.reduce(
  (count, section) => count + 1 + section.entries.length,
  0
)
