"""Fils d'Ariane verticaux dans les marges.

À gauche : les chapitres de la partie. À droite : les sections du chapitre en cours.
Chaque rail montre ce qui est passé (sapin), là où on est (orange, titre complet) et ce qui vient (gris),
avec le texte écrit à 90° (de haut en bas). Le segment en cours et ses deux voisins portent leur titre ; les autres, leur numéro.
"""
import os
import fitz

MM = 72 / 25.4
HERE = os.path.dirname(os.path.abspath(__file__))
SAPIN, ORANGE, GRIS = (0x12/255, 0x3A/255, 0x33/255), (0xE8/255, 0x79/255, 0x4F/255), (0xB9/255, 0xB1/255, 0xA2/255)
ROT = -90
PISTE = (0xE3/255, 0xDC/255, 0xCD/255)
HAUT, BAS = 22 * MM, 270 * MM
LARGE, BORD, ECART, GAP = 1.6 * MM, 6 * MM, 1.3 * MM, 1.2 * MM
CORPS_NUM, CORPS_TITRE = 6.5, 7.5
POLICES = {"num": "Poppins-SemiBold.ttf", "titre": "Poppins-ExtraBold.ttf"}
_fonts = {k: fitz.Font(fontfile=os.path.join(HERE, "polices", f)) for k, f in POLICES.items()}


def structure(entries, total):
    """entries : (niveau, titre, page 1-based) -> parties [(début, fin, [chapitres])], chapitre = (début, fin, titre, [sections])."""
    def fin(k, lv):
        for lv2, _, pg2 in entries[k + 1:]:
            if lv2 <= lv:
                return pg2 - 1
        return total
    parts = []
    for k, (lv, t, pg) in enumerate(entries):
        if lv == 1:
            parts.append((pg, fin(k, 1), []))
        elif lv == 2 and parts:
            secs = []
            for k3 in range(k + 1, len(entries)):
                lv3, t3, pg3 = entries[k3]
                if lv3 <= 2:
                    break
                if lv3 == 3:
                    secs.append((pg3, fin(k3, 3), t3))
            parts[-1][2].append((pg, fin(k, 2), t, secs))
    # partie sans chapitre (l'Introduction) : ses sections tiennent lieu de chapitres
    for p in parts:
        if not p[2]:
            p[2].extend((pg, fin(k, 3), t, []) for k, (lv, t, pg) in enumerate(entries)
                        if lv == 3 and p[0] <= pg <= p[1])
    return parts


def numero(titre):
    tete = titre.split(" ", 1)[0]
    return tete if any(c.isdigit() for c in tete) else ""


def coupe(texte, font, size, maxi):
    if font.text_length(texte, size) <= maxi:
        return texte
    while texte and font.text_length(texte + "…", size) > maxi:
        texte = texte[:-1]
    return texte.rstrip() + "…"


def rail(page, items, cur, x_barre, x_texte, cibles=None):
    """items : titres ; cur : index de l'élément en cours (ou None) ; cibles : page (0-based) de chaque élément, pour les liens.

    Le segment en cours et ses voisins (avant, après) sont agrandis pour porter leur titre ;
    les autres gardent au moins la place de leur numéro.
    """
    n = len(items)
    if not n:
        return
    total = BAS - HAUT - GAP * (n - 1)
    ft, fn = _fonts["titre"], _fonts["num"]
    ref = cur if cur is not None else -1  # avant le premier chapitre : le suivant est le premier
    grands = {k for k in (ref - 1, ref, ref + 1) if 0 <= k < n}
    style = {k: ((ft, CORPS_TITRE) if k == cur else (fn, CORPS_NUM)) for k in range(n)}
    besoin = {k: style[k][0].text_length(items[k], style[k][1]) + 3 * MM for k in grands}
    mini = 7 * MM
    petits = n - len(grands)
    dispo = total - petits * mini
    if sum(besoin.values()) > dispo:  # titres trop longs : on partage la place disponible
        r = dispo / sum(besoin.values())
        besoin = {k: v * r for k, v in besoin.items()}
    reste = total - sum(besoin.values())
    h_petit = reste / petits if petits else 0
    if not petits and reste > 0:
        besoin = {k: v + reste / len(besoin) for k, v in besoin.items()}
    y = HAUT
    for i, titre in enumerate(items):
        h = besoin.get(i, h_petit)
        col = ORANGE if i == cur else (SAPIN if i < ref else PISTE)
        page.draw_rect(fitz.Rect(x_barre, y, x_barre + LARGE, y + h), color=None, fill=col)
        if cibles and i != cur:  # cliquer sur un segment ouvre le chapitre ou la section
            page.insert_link({"kind": fitz.LINK_GOTO, "page": cibles[i], "to": fitz.Point(0, 0),
                              "from": fitz.Rect(x_barre - 1.5 * MM, y, x_barre + LARGE + 4 * MM, y + h)})
        font, size = style[i]
        tcol = ORANGE if i == cur else (SAPIN if col == SAPIN else GRIS)
        if i in grands:
            txt = coupe(titre, font, size, h - 1.5 * MM)
        else:
            txt = numero(titre)
            if font.text_length(txt, size) > h - 1.5 * MM:
                txt = ""
        if txt:
            # texte écrit de haut en bas, à partir du haut du segment
            p = fitz.Point(x_texte, y + 0.6 * MM)
            tw = fitz.TextWriter(page.rect)
            tw.append(p, txt, font=font, fontsize=size)
            tw.write_text(page, color=tcol, morph=(p, fitz.Matrix(ROT)))
        y += h + GAP


def dessine(doc, entries, pages_corps):
    parts = structure(entries, len(doc))
    for i in pages_corps:
        pn = i + 1
        page = doc[i]
        w = page.rect.width
        part = next((p for p in parts if p[0] <= pn <= p[1]), None)
        if not part or not part[2]:
            continue
        chaps = part[2]
        cur = next((k for k, c in enumerate(chaps) if c[0] <= pn <= c[1]), None)
        rail(page, [c[2] for c in chaps], cur, BORD, BORD + LARGE + ECART, [c[0] - 1 for c in chaps])
        if cur is None:
            continue
        secs = chaps[cur][3]
        scur = next((k for k, s in enumerate(secs) if s[0] <= pn <= s[1]), None)
        if secs:
            xb = w - BORD - LARGE
            rail(page, [s[2] for s in secs], scur, xb, xb - ECART - CORPS_TITRE * 0.75, [s[0] - 1 for s in secs])
