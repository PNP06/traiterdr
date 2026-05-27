# Rapport de nettoyage HTML

## Verdict

Le HTML source est exploitable, mais ce n'est pas un format propre pour ChatGPT tel quel : il s'agit d'un export Microsoft Word en `windows-1252`, avec beaucoup de CSS/classes Word et de mise en page inline. La version Markdown nettoyee est le fichier recommande pour l'analyse.

## Fichiers

- Source HTML : `sources/traite/raw_html_export/`
- Markdown nettoye : `sources/traite/traite_rdr_version_html_clean.md`
- Manifeste : `sources/traite/manifest_html_clean.json`

## Mesures

- Taille HTML : 2200625 octets
- Taille Markdown nettoye : 921681 octets
- Titres extraits : 442
- Paragraphes extraits : 3820
- Tables extraites : 71
- Images referencees dans le HTML : 255
- Images uniques referencees : 160
- Images manquantes : 0
- Liens href : 1362

## Points d'attention

- Le HTML original garde les artefacts Word (`Mso*`, `mso-*`, styles inline).
- L'encodage declare est `windows-1252`; lire le fichier en UTF-8 produit des caracteres corrompus.
- Les images sont signalees par des references textuelles dans le Markdown nettoye.
- Pour ChatGPT, privilegier le Markdown nettoye plutot que le HTML original ou le DOCX.

## Premiers titres

- H1 SUIVI
- H1 Remerciements
- H1 Introduction
- H1 Mythes
  - H2 Création des croyances
    - H3 Heuristique
      - H4 Heuristiques problématiques : exemples
      - H4 Comment limiter l’erreur
    - H3 Biais
      - H4 Biais parfois “fonctionnels” : exemples
      - H4 Biais parfois problématiques : exemples
      - H4 Comment limiter l’erreur
    - H3 Sophisme
      - H4 Bases de la logique
        - H5 Exemple simple (raisonnement correct vs fallacieux)
        - H5 Validité et solidité : deux façons de se tromper
        - H5 Tester un argument
      - H4 Exemples de sophismes courants
        - H5 a) Appel à la nature (appeal to nature)
        - H5 b) Fausse causalité (corrélation ≠ causalité)
        - H5 c) Généralisation abusive / preuve anecdotique
        - H5 d) Faux dilemme
        - H5 e) Whataboutism / relativisation (“il y a pire”)
        - H5 f) Appel à l’autorité illégitime
        - H5 g) Attaque personnelle (ad hominem)
      - H4 Comment limiter l’erreur
    - H3 Mécanisme de protection psychologique
      - H4 Dissonance cognitive
      - H4 Raisonnement motivé
      - H4 Protection de l’identité
      - H4 Réactance psychologique
      - H4 Lever les freins psychologiques
    - H3 Approche en réduction des risques
        - H5 1) 
 BUT : clarifier la finalité (éviter le faux débat)
        - H5 2) CADRE : rendre l’échange recevable (sinon le fond ne passe pas)
        - H5 3) FOND : traiter l’affirmation comme un problème de risque (pas comme une 
opinion)
        - H5 4) SORTIE : transformer l’analyse en décision de réduction des risques
        - H5 Exemples
          - H6 Exemple dans une conversation sur le cannabis entre ami
          - H6 Exemple dans une conversation en public sur l’alcool
          - H6 Exemple dans le cadre d’une prise en charge sur un stand RDR
    - H3 Conclusion
  - H2 Comprendre la science
    - H3 Science et recherche
      - H4 Exemple de la cigarette électronique
      - H4 Exemple de la neurotoxicité de la MDMA
    - H3 La méthode Scientifique
      - H4 1) Question testable
      - H4 2) Définir les concepts
      - H4 3) Choisir un plan d’étude adapté
      - H4 4) Mesurer et quantifier
      - H4 5) Réplication et controverse organisée
      - H4 6) Biais et garde-fous
      - H4 Conclusion
  - H2 Le mois sans 
alcool/sans tabac est inutile
    - H3 Effet individuel
    - H3 Effet sur la santé publique
      - H4 Impact des consommations « modérés » sur l’incidence des cancers
      - H4 Incidence du dry january sur l’apparition de cancer
  - H2 L’alcool et le tabac sont rentables pour l’état
    - H3 Focus sur les finances publiques pour l’alcool
    - H3 Cout social total
      - H4 Valeur économique de la vie humaine
      - H4 L’effet sur le bien être des finances publiques
      - H4 Le cout social
      - H4 Résultats
    - H3 Augmentation des taxes pour l’équilibre
        - H5 Pour l'alcool
        - H5 Pour le tabac
  - H2 Effet du prix sur la consommation
  - H2 Boire un verre de vin est bon pour la santé
    - H3 Le problème 
général : prouver le lien de causalité
      - H4 Corrélation ou causalité ?
      - H4 Difficulté de la preuve
      - H4 Étudier la population
      - H4 L’origine : Le French 
Paradox
      - H4 Le doute : observation et débats
        - H5 Limite 1 : pas bon pour le reste
        - H5 Limite 2 : pas si bon pour le cœur
      - H4 La confirmation : l’apport de la génétique


