"""Liserés de progression sur les bords des pages.

À gauche : la partie, découpée en un segment par chapitre (chapitres lus en sapin, chapitre en cours en orange).
À droite : le chapitre en cours, rempli en orange jusqu'à la page courante, avec un repère par section.
"""
import fitz

MM = 72 / 25.4
SAPIN, ORANGE, VIOLET, PISTE = (0x12/255, 0x3A/255, 0x33/255), (0xE8/255, 0x79/255, 0x4F/255), (0x5B/255, 0x3F/255, 0xCF/255), (0xE3/255, 0xDC/255, 0xCD/255)
HAUT, BAS, LARGE, BORD = 22 * MM, 273 * MM, 2 * MM, 6 * MM


def plages(entries, total):
    """entries : (niveau, titre, page 1-based). Renvoie parties et chapitres sous forme (début, fin, sections)."""
    parts, chaps = [], []
    for k, (lv, t, pg) in enumerate(entries):
        if lv > 2:
            continue
        fin = total
        for lv2, _, pg2 in entries[k + 1:]:
            if lv2 <= lv:
                fin = pg2 - 1
                break
        if lv == 1:
            parts.append([pg, fin, []])
        elif parts:
            secs = []
            for lv3, _, pg3 in entries[k + 1:]:
                if lv3 <= 2:
                    break
                secs.append(pg3)
            c = (pg, fin, secs)
            chaps.append(c)
            parts[-1][2].append(c)
    return parts, chaps


def barre(page, x, y0, y1, color):
    if y1 - y0 < 0.5:
        return
    r = fitz.Rect(x, y0, x + LARGE, y1)
    page.draw_rect(r, color=None, fill=color, radius=min(0.5, LARGE / max(r.height, 1) / 2) if r.height > LARGE else None)


def dessine(doc, entries, pages_corps):
    parts, chaps = plages(entries, len(doc))
    for i in pages_corps:
        pn = i + 1
        page = doc[i]
        w = page.rect.width
        part = next((p for p in parts if p[0] <= pn <= p[1]), None)
        if not part or not part[2]:
            continue
        # gauche : chapitres de la partie
        a, b = part[2][0][0], part[1]
        span = b - a + 1
        gap = 0.8 * MM
        for c in part[2]:
            y0 = HAUT + (c[0] - a) / span * (BAS - HAUT)
            y1 = HAUT + (c[1] - a + 1) / span * (BAS - HAUT) - gap
            col = ORANGE if c[0] <= pn <= c[1] else (SAPIN if c[1] < pn else PISTE)
            barre(page, BORD, y0, y1, col)
        # droite : progression dans le chapitre
        c = next((c for c in chaps if c[0] <= pn <= c[1]), None)
        if not c:
            continue
        n = c[1] - c[0] + 1
        x = w - BORD - LARGE
        barre(page, x, HAUT, BAS, PISTE)
        barre(page, x, HAUT, HAUT + (pn - c[0] + 1) / n * (BAS - HAUT), ORANGE)
        for s in c[2]:
            y = HAUT + (s - c[0]) / n * (BAS - HAUT)
            page.draw_line(fitz.Point(x - 1.2 * MM, y), fitz.Point(x, y), color=VIOLET, width=1.2)
