"""Fabrique l'index de la page Rechercher à partir du PDF du traité.

    python3 scripts/recherche/build_index.py [public/traite-rdr.pdf] [public/recherche-index.json]

Le texte vient de pdftotext (poppler), page par page, recadré sur la colonne
de texte pour écarter les onglets de navigation et les en-têtes courants.
Les parties viennent des signets du PDF (posés par refonte/assemble.py).
Les thèmes et produits sont définis dans themes.json, à côté de ce script.
À relancer à chaque nouvelle version du PDF.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

import pypdf

ICI = Path(__file__).resolve().parent
RACINE = ICI.parents[1]

# Colonne de texte en points PDF (A4 : 595 x 842) : les onglets latéraux sont
# à x < 40 et x > 555, l'en-tête courant à y < 40.
CADRE = dict(x=50, y=45, W=495, H=760)

# Couverture, version, sommaire : pas utiles dans les résultats.
PREMIERE_PAGE = 9

CODE = re.compile(r'^([A-H](?:\.\d+)*)\b')


def signets(lecteur):
    sortie = []

    def parcourir(noeuds, niveau):
        for noeud in noeuds:
            if isinstance(noeud, list):
                parcourir(noeud, niveau + 1)
                continue
            titre = re.sub(r'\s+', ' ', noeud.title).strip()
            page = lecteur.get_destination_page_number(noeud) + 1
            m = CODE.match(titre)
            code = m.group(1) if m else ''
            titre = re.sub(r'^[A-H](?:\.\d+)*\s*·?\s*', '', titre) if code else titre
            # Les signets ne sont pas toujours bien imbriqués : le niveau suit le code (A, A.1, A.1.2).
            if code:
                niveau = code.count('.')
            sortie.append({'code': code, 'titre': titre, 'page': page, 'niveau': niveau})

    parcourir(lecteur.outline, 0)
    return sortie


def fins_de_parties(parties, derniere_page):
    """Page de fin : jusqu'au signet suivant de même niveau ou plus haut."""
    for i, partie in enumerate(parties):
        fin = derniere_page
        for suivante in parties[i + 1:]:
            if suivante['niveau'] <= partie['niveau']:
                fin = max(partie['page'], suivante['page'] - 1)
                break
        partie['fin'] = fin


def texte_page(pdf, n):
    brut = subprocess.run(
        ['pdftotext', '-q', '-f', str(n), '-l', str(n),
         '-x', str(CADRE['x']), '-y', str(CADRE['y']), '-W', str(CADRE['W']), '-H', str(CADRE['H']),
         str(pdf), '-'],
        capture_output=True, text=True, check=True).stdout
    texte = brut.replace('­', '').replace('\f', ' ')
    # Appels de note collés au mot (« d'eau305 ») : on les retire du texte cherché.
    texte = re.sub(r'(?<=[a-zàâçéèêëîïôûùüÿœ»)])\d{1,3}(?=[\s,.;:)]|$)', '', texte)
    return re.sub(r'\s+', ' ', texte).strip()


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / 'public/traite-rdr.pdf'
    sortie = Path(sys.argv[2]) if len(sys.argv) > 2 else RACINE / 'public/recherche-index.json'

    lecteur = pypdf.PdfReader(str(pdf))
    nb_pages = len(lecteur.pages)
    parties = [p for p in signets(lecteur) if p['page'] >= PREMIERE_PAGE]
    fins_de_parties(parties, nb_pages)

    pages = []
    for n in range(PREMIERE_PAGE, nb_pages + 1):
        # Partie la plus fine qui couvre la page.
        couvrantes = [i for i, p in enumerate(parties) if p['page'] <= n <= p['fin']]
        partie = max(couvrantes, key=lambda i: (parties[i]['niveau'], parties[i]['page'])) if couvrantes else -1
        texte = texte_page(pdf, n)
        if texte:
            pages.append({'n': n, 'p': partie, 't': texte})

    config = json.loads((ICI / 'themes.json').read_text(encoding='utf-8'))
    codes = {p['code']: i for i, p in enumerate(parties) if p['code']}
    for theme in config['themes']:
        inconnus = [c for c in theme['sections'] if c not in codes]
        if inconnus:
            sys.exit(f"themes.json : {theme['id']} cite des parties absentes des signets : {inconnus}")
        theme['sections'] = [codes[c] for c in theme['sections']]

    index = {
        'pdf': '/traite-rdr.pdf',
        'pages_total': nb_pages,
        'parties': parties,
        'pages': pages,
        'themes': config['themes'],
        'produits': config['produits'],
    }
    sortie.write_text(json.dumps(index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print(f'{sortie} : {len(pages)} pages, {len(parties)} parties, '
          f"{len(config['themes'])} thèmes, {len(config['produits'])} produits, "
          f'{sortie.stat().st_size // 1024} Ko')


if __name__ == '__main__':
    main()
