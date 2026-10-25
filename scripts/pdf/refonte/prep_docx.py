"""Prépare le .docx du traité pour pandoc.

- paragraphes encadrés (bordure Word) -> style « Encadre » (deviennent des encadrés koala) ;
- koala ancré à côté des encadrés retiré (l'encadré l'affiche déjà) ;
- SmartArt, graphique et figure en zone de texte -> repère [[SCHEMA:id]], remplacé ensuite par un schéma redessiné ;
- tout ce qui précède les Remerciements (suivi interne, titres alternatifs, sommaire Word, dédicace)
  est retiré : le gabarit recompose la dédicace, la citation et le sommaire ;
- notes « A faire » retirées.

Usage : python3 prep_docx.py traite.docx traite-prep.docx
"""
import re, sys, zipfile
from lxml import etree

SRC, OUT = sys.argv[1:3]
KOALA = "media/image3.jpeg"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W, "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "dgm": "http://schemas.openxmlformats.org/drawingml/2006/diagram",
      "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
      "wps": "http://schemas.microsoft.com/office/word/2010/wordprocessingShape"}
q = lambda tag: "{%s}%s" % (W, tag)

zin = zipfile.ZipFile(SRC)
root = etree.fromstring(zin.read("word/document.xml"))
styles = zin.read("word/styles.xml").decode("utf8")
rels = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="([^"]+)"', zin.read("word/_rels/document.xml.rels").decode()))
koala_ids = {k for k, v in rels.items() if v == KOALA}
body = root.find(q("body"))

def text(el):
    return "".join(el.itertext()) if el is not None else ""

def pstyle(p):
    s = p.find("w:pPr/w:pStyle", NS)
    return s.get(q("val")) if s is not None else ""

def set_style(p, name):
    ppr = p.find(q("pPr"))
    if ppr is None:
        ppr = etree.SubElement(p, q("pPr")); p.remove(ppr); p.insert(0, ppr)
    s = ppr.find(q("pStyle"))
    if s is None:
        s = etree.Element(q("pStyle")); ppr.insert(0, s)
    s.set(q("val"), name)

def marker(label):
    p = etree.Element(q("p")); r = etree.SubElement(p, q("r")); t = etree.SubElement(r, q("t"))
    t.text = "[[SCHEMA:%s]]" % label
    return p

# notes de travail retirées du livre (comme dans le PDF retouché du 25/10/2026)
NOTES_DE_TRAVAIL = {"A faire :", "Pause diabolo pour la partie testing", "Addicto",
    "Préciser role intervention brève", "Pourquoi le cancer tue ?", "Pourquoi le cancer tue\u202f?",
    "En soit des cellules qui se multiplie ça ne tue pas directement", "Cancer malin/Benin",
    "Les types les classification", "Regarder le doc du CIRC qui détail les RR",
    "➔ Regarder le doc du CIRC qui détail les RR", "– Fiche des risques génériques—", "-", "–"}
EN_COURS = {"Voir EM consult IEA. Donne critère de sevrage."}
children = list(body)
front = True
stats = {"encadres": 0, "schemas": 0, "retires": 0}
for i, el in enumerate(children):
    tag = etree.QName(el).localname
    if tag == "sectPr":
        continue
    t = text(el)
    if front:
        if tag == "p" and pstyle(el) == "Titre1" and t.strip().startswith("Remerciements"):
            front = False
        else:  # la dédicace et la citation sont recomposées dans le gabarit
            body.remove(el); stats["retires"] += 1
            continue
    norm = re.sub(r"\s+", " ", t).strip()
    if norm in NOTES_DE_TRAVAIL:
        body.remove(el); stats["retires"] += 1
        continue
    if norm in EN_COURS:
        p = etree.Element(q("p")); r = etree.SubElement(p, q("r")); rpr = etree.SubElement(r, q("rPr"))
        etree.SubElement(rpr, q("i")); tt = etree.SubElement(r, q("t")); tt.text = "Chapitre en cours d'écriture."
        body.replace(el, p); stats["retires"] += 1
        continue
    # koala décoratif
    for blip in el.iterfind(".//a:blip", NS):
        if blip.get("{%s}embed" % NS["r"]) in koala_ids:
            d = blip
            while d is not None and etree.QName(d).localname not in ("drawing",):
                d = d.getparent()
            if d is not None and d.getparent() is not None:
                d.getparent().remove(d)
    # schémas non convertibles
    kind = None
    if el.find(".//dgm:relIds", NS) is not None: kind = "smartart"
    elif el.find(".//c:chart", NS) is not None: kind = "graphique"
    elif el.find(".//wps:txbx", NS) is not None and "Figure" in t: kind = "zone"
    if kind:
        body.replace(el, marker("%s-%d" % (kind, i))); stats["schemas"] += 1
        continue
    if tag == "p" and el.find("w:pPr/w:pBdr", NS) is not None and not re.match(r"(Titre\d|TM\d)$", pstyle(el)):
        set_style(el, "Encadre"); stats["encadres"] += 1

styles = styles.replace("</w:styles>",
    '<w:style w:type="paragraph" w:customStyle="1" w:styleId="Encadre"><w:name w:val="Encadre"/><w:basedOn w:val="Normal"/></w:style></w:styles>')
zout = zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED)
for item in zin.infolist():
    data = zin.read(item.filename)
    if item.filename == "word/document.xml":
        data = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
    elif item.filename == "word/styles.xml":
        data = styles.encode("utf8")
    zout.writestr(item, data)
zout.close()
print(stats)
