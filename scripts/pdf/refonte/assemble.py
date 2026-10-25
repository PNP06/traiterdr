"""Assemble le PDF final du traité.

Usage : python3 assemble.py dossier_parties/ couverture.pdf version.pdf sortie.pdf

- met bout à bout couverture, page de version et les parties rendues (00.pdf, 01.pdf…) ;
- compose le sommaire avec les vrais numéros de page et l'insère après la citation d'ouverture ;
- numérote les pages (sauf couverture, version, dédicace, citation et pages d'ouverture) ;
- ajoute les signets et les métadonnées.
"""
import glob, json, os, subprocess, sys
import fitz

DIR, COVER, VERSION, OUT = sys.argv[1:5]
HERE = os.path.dirname(os.path.abspath(__file__))
parts = sorted(glob.glob(os.path.join(DIR, "[0-9][0-9].pdf")))
infos = [json.load(open(p[:-4] + ".json", encoding="utf8")) for p in parts]

AVANT = 2          # couverture + version
DEBUT = 2          # dédicace + citation, en tête de 00.pdf


def compose(som_pages):
    """Liste (niveau, titre, page absolue) en supposant som_pages pages de sommaire."""
    out, offset = [], AVANT + som_pages
    for k, info in enumerate(infos):
        for t in info["titres"]:
            page = offset + t["page"]
            if k == 0 and t["page"] <= DEBUT:
                continue
            out.append((t["niveau"], t["titre"], page))
        offset += info["pages"]
    return out


def render_sommaire(entries, path):
    css = open(os.path.join(HERE, "gabarit.css"), encoding="utf8").read()
    tpl = open(os.path.join(HERE, "page.html"), encoding="utf8").read()
    items = "".join('<li class="t%d"><span class="lien">%s</span><b>%d</b></li>' % (lv, t, pg - AVANT) for lv, t, pg in entries)
    css += """
.sommaire li{display:flex; gap:2mm; align-items:baseline}
.sommaire li b{margin-left:auto; font-family:Poppins; font-weight:700; color:var(--sapin)}
.sommaire .t1{font-family:Poppins; font-weight:800; font-size:11pt; color:var(--sapin); margin-top:4mm}
.sommaire .t2{font-weight:700; font-size:9.6pt; padding-left:4mm; margin-top:1.2mm}
.sommaire .t3{font-size:8.8pt; color:var(--muted); padding-left:9mm}
.sommaire .t3 b{font-weight:500; color:var(--muted)}
"""
    html = tpl.replace("{{CSS}}", css).replace("{{CORPS}}", '<section class="sommaire" style="break-before:auto" data-partie="" data-fil="Sommaire"><h1>Sommaire</h1><ol>%s</ol></section>' % items)
    open(path + ".html", "w", encoding="utf8").write(html)
    subprocess.run(["node", os.path.join(HERE, "render.cjs"), path + ".html"], check=True)
    return fitz.open(path + ".pdf")


# le nombre de pages du sommaire dépend de lui-même : deux passes suffisent
som_n = 3
for _ in range(2):
    som = render_sommaire(compose(som_n), os.path.join(DIR, "sommaire"))
    if len(som) == som_n:
        break
    som_n = len(som)
entries = compose(som_n)

doc = fitz.open()
doc.insert_pdf(fitz.open(COVER))
doc.insert_pdf(fitz.open(VERSION))
first = fitz.open(parts[0])
doc.insert_pdf(first, to_page=DEBUT - 1)
doc.insert_pdf(som)
doc.insert_pdf(first, from_page=DEBUT)
for p in parts[1:]:
    doc.insert_pdf(fitz.open(p))
assert len(doc) == AVANT + som_n + sum(i["pages"] for i in infos), "pagination incohérente"

# Numéros de page : pages portant le pied de page courant uniquement
for i, page in enumerate(doc):
    if i < AVANT + DEBUT:
        continue
    if "risky · comprendre pour mieux choisir" not in page.get_text().lower() and i >= AVANT + DEBUT + som_n:
        continue
    page.insert_text((page.rect.width - 20 * 72 / 25.4 - 12, page.rect.height - 24 * 72 / 25.4 + 26),
                     str(i + 1 - AVANT), fontname="hebo", fontsize=9, color=(0x12 / 255, 0x3A / 255, 0x33 / 255))

# Signets (numéro imprimé = page PDF - 2)
toc = [[1, "Couverture", 1], [1, "Version et parties en cours", 2], [1, "Sommaire", AVANT + DEBUT + 1]]
last = 1
for lv, t, pg in entries:
    lv = min(lv, last + 1)
    toc.append([lv, t, pg])
    last = lv
doc.set_toc(toc)
doc.set_metadata({
    "title": "Traité de réduction des risques liés aux drogues – Tome 1",
    "author": "Association RISKY (@risky.asso)",
    "subject": "Bases de connaissances et risques génériques. Lire en ligne : traiterdr.netlify.app",
    "keywords": "réduction des risques, RDR, drogues, substances psychoactives, santé, RISKY",
    "creator": "Traité RISKY, mise en page paged.js", "producer": "PyMuPDF",
})
doc.set_pagemode("UseOutlines")
doc.save(OUT, garbage=4, deflate=True)
print("pages", len(doc), "sommaire", som_n, "signets", len(toc))
