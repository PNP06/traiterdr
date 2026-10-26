"""Fils d'Ariane verticaux dans les marges.

À gauche : les chapitres de la partie. À droite : les sections du chapitre en cours.
Chaque rail montre ce qui est passé (sapin), là où on est (orange) et ce qui vient (gris), texte à 90° (de haut en bas) :
les titres complets autour de la position (autant que la hauteur le permet), et un résumé « B.1 à B.5 » pour le reste.
"""
import os
import fitz

MM = 72 / 25.4
HERE = os.path.dirname(os.path.abspath(__file__))
SAPIN, ORANGE, GRIS = (0x12/255, 0x3A/255, 0x33/255), (0xE8/255, 0x79/255, 0x4F/255), (0x7A/255, 0x72/255, 0x64/255)
ROT = -90
PISTE = (0xD9/255, 0xD0/255, 0xBE/255)
HAUT, BAS = 22 * MM, 270 * MM
LARGE, BORD, ECART, GAP = 2 * MM, 6 * MM, 1.5 * MM, 1.5 * MM
CORPS_NUM, CORPS_TITRE = 7.5, 8.5
FENETRE = 2  # titres complets affichés avant et après l'élément en cours
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


def plage(items, a, b):
    """Libellé résumé d'un groupe d'éléments masqués, ex. « B.1 à B.5 » ou « 3 sections »."""
    na, nb = numero(items[a]), numero(items[b])
    if a == b:
        return items[a]
    return "%s à %s" % (na, nb) if na and nb else "%d sections" % (b - a + 1)


def rail(page, items, cur, x_barre, x_texte, cibles=None):
    """Rail vertical : fenêtre de titres complets autour de l'élément en cours (deux avant, deux après),
    et un segment résumé pour ce qui est plus loin (« B.1 à B.5 » au-dessus, « B.10 à B.15 » en dessous).
    items : titres ; cur : index en cours (ou None) ; cibles : page (0-based) de chaque élément, pour les liens.
    """
    n = len(items)
    if not n:
        return
    ref = cur if cur is not None else -1
    style = {"cours": (_fonts["titre"], CORPS_TITRE, ORANGE, ORANGE),
             "passe": (_fonts["num"], CORPS_NUM, SAPIN, SAPIN),
             "avenir": (_fonts["num"], CORPS_NUM, PISTE, GRIS)}

    def decoupe(a, b):
        segs = []  # (texte, état, index de la cible)
        if a > 0:
            segs.append((plage(items, 0, a - 1), "passe", 0))
        for k in range(a, b + 1):
            segs.append((items[k], "cours" if k == cur else ("passe" if k < ref else "avenir"), k))
        if b < n - 1:
            segs.append((plage(items, b + 1, n - 1), "avenir", b + 1))
        besoin = [style[e][0].text_length(s, style[e][1]) + 3 * MM for s, e, _ in segs]
        return segs, besoin, sum(besoin) + GAP * (len(segs) - 1)

    # fenêtre de deux titres avant et après, élargie tant que tout tient en entier
    a, b = max(0, ref - FENETRE), min(n - 1, max(ref, 0) + FENETRE)
    segs, besoin, h = decoupe(a, b)
    while a > 0 or b < n - 1:
        essais = [x for x in ((a, b + 1), (a - 1, b)) if x[0] >= 0 and x[1] <= n - 1]
        ok = [(x, decoupe(*x)) for x in essais if decoupe(*x)[2] <= BAS - HAUT]
        if not ok:
            break
        (a, b), (segs, besoin, h) = ok[0]
    total = BAS - HAUT - GAP * (len(segs) - 1)
    if sum(besoin) > total:  # trop long : on raccourcit d'abord les titres les plus longs
        plafond = max(besoin)
        while sum(min(x, plafond) for x in besoin) > total:
            plafond -= 1
        besoin = [min(x, plafond) for x in besoin]
    else:  # place en trop : elle va au segment en cours (ou se répartit)
        k_cur = next((i for i, s in enumerate(segs) if s[1] == "cours"), None)
        surplus = total - sum(besoin)
        if k_cur is not None:
            besoin[k_cur] += surplus
        else:
            besoin = [x + surplus / len(besoin) for x in besoin]
    y = HAUT
    for (texte, etat, k), h in zip(segs, besoin):
        font, size, cbar, ctxt = style[etat]
        page.draw_rect(fitz.Rect(x_barre, y, x_barre + LARGE, y + h), color=None, fill=cbar)
        if cibles and etat != "cours":  # cliquer sur un segment ouvre le chapitre ou la section
            page.insert_link({"kind": fitz.LINK_GOTO, "page": cibles[k], "to": fitz.Point(0, 0),
                              "from": fitz.Rect(x_barre - 1.5 * MM, y, x_barre + LARGE + 4 * MM, y + h)})
        txt = coupe(texte, font, size, h - 2 * MM)
        if txt and txt != "…":
            # texte écrit de haut en bas, à partir du haut du segment
            p = fitz.Point(x_texte, y + 0.8 * MM)
            tw = fitz.TextWriter(page.rect)
            tw.append(p, txt, font=font, fontsize=size)
            tw.write_text(page, color=ctxt, morph=(p, fitz.Matrix(ROT)))
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
            rail(page, [s[2] for s in secs], scur, xb, xb - ECART - CORPS_TITRE * 0.8, [s[0] - 1 for s in secs])
