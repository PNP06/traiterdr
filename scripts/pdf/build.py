import re, sys, fitz
SRC, COVER, OUT = sys.argv[1:4]
FONT = "/usr/share/fonts/truetype/crosextra/Carlito-BoldItalic.ttf"
d = fitz.open(SRC)

# 1. Signets construits depuis les liens du sommaire (pages PDF 5-8)
toc = []
for pn in range(4, 8):
    for l in d[pn].get_links():
        if l.get("kind") != fitz.LINK_GOTO:
            continue
        r = l["from"]
        t = d[pn].get_textbox(r).replace("\n", " ")
        t = re.sub(r"\s*\.{3,}.*$", "", t).strip(" .")
        t = re.sub(r"\s+", " ", t).replace(" ", " ")
        if not t or t.upper() == "SUIVI":
            continue
        lvl = 1 if r.x0 < 60 else 2 if r.x0 < 70 else 3
        toc.append([lvl, t, l["page"] + 1])
# niveaux cohérents (pas de saut 1 -> 3)
for i, e in enumerate(toc):
    prev = toc[i - 1][0] if i else 1
    e[0] = min(e[0], prev + 1)

# 2. Contenus de brouillon à retirer (page PDF -> zones)
def blocks(pn, pred):
    return [fitz.Rect(b[:4]) for b in d[pn - 1].get_text("blocks") if pred(b[4], b)]
redact = {
    2: [fitz.Rect(54, 68, 512, 128)],                                   # tableau "Suivi des modifications"
    5: blocks(5, lambda t, b: t.startswith("SUIVI .")),                  # ligne SUIVI du sommaire
    9: blocks(9, lambda t, b: t.startswith("A faire")),                 # "A faire : Pause diabolo..."
    330: blocks(330, lambda t, b: any(t.startswith(s) for s in (
        "Pourquoi le cancer tue", "En soit des cellules", "Cancer malin", "Les types les classification"))),
    331: blocks(331, lambda t, b: "Regarder le doc du CIRC" in t),
}
# 3. En-têtes de page faux sur les premières pages et en début de chapitre
headers = {**{p: "" for p in (2, 3, 4)}, **{p: "Sommaire" for p in (5, 6, 7)},
           8: "Sommaire  /  Remerciements", **{p: "Introduction" for p in range(9, 17)},
           100: "La gestion des risques", 104: "Le cerveau et le corps",
           158: "Classification des substances", 183: "Risques génériques",
           186: "Risques durant la prise"}
for pn, txt in headers.items():
    redact.setdefault(pn, []).extend(blocks(pn, lambda t, b: b[1] < 45))

for pn, rects in redact.items():
    page = d[pn - 1]
    for r in rects:
        page.add_redact_annot(r + (-1, -1, 1, 1), fill=(1, 1, 1))
        for l in page.get_links():
            if fitz.Rect(l["from"]).intersects(r) and l.get("kind") == fitz.LINK_GOTO and pn == 5:
                page.delete_link(l)
    page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
for pn, txt in headers.items():
    if txt:
        page = d[pn - 1]
        page.insert_font(fontname="cbi", fontfile=FONT)
        w = fitz.get_text_length(txt, fontname="cbi", fontfile=FONT, fontsize=9) if False else fitz.Font(fontfile=FONT).text_length(txt, 9)
        page.insert_text(((page.rect.width - w) / 2, 34.2), txt, fontname="cbi", fontsize=9)

# 4. Pages de fin vides ("Fiche des risques génériques" vide + page blanche)
d.delete_pages(331, 332)

# 5. Couverture à la place de la page "SUIVI"
c = fitz.open(COVER)
d.delete_page(0)
d.insert_pdf(c, start_at=0)
toc[0:0] = [[1, "Couverture", 1], [1, "Sommaire", 5]]
d.set_toc(toc)

d.set_metadata({
    "title": "Traité de réduction des risques liés aux drogues – Tome 1",
    "author": "David Devesa Velasco (association RISKY)",
    "subject": "Bases de connaissances et risques génériques. Lire en ligne : traiterdr.netlify.app",
    "keywords": "réduction des risques, RDR, drogues, substances psychoactives, santé, RISKY",
    "creator": "Microsoft Word, retouches RISKY", "producer": "PyMuPDF",
    "creationDate": d.metadata.get("creationDate", ""), "modDate": fitz.get_pdf_now(),
})
d.set_pagemode("UseOutlines")

# 6. Compression des images (cible 150 dpi, JPEG qualité 80)
d.rewrite_images(dpi_threshold=170, dpi_target=150, quality=80)
d.subset_fonts()
d.save(OUT, garbage=4, deflate=True, clean=True, use_objstms=True)
print("pages", len(d), "signets", len(toc))
