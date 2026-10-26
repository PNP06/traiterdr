"""Version liseuse (EPUB 3) du traité, à partir du HTML produit par la chaîne du PDF.

Usage : python3 build_epub.py traite.html couverture.jpg traite-rdr.epub

traite.html est la sortie de scripts/pdf/refonte/build_html.py (même texte, mêmes corrections,
même numérotation A.1.2 que le PDF). Les images sont lues à côté de traite.html (media/).
Le livre est découpé en un fichier par chapitre ; les notes deviennent des notes cliquables
(fenêtre surgissante sur Kobo, Apple Livres, Kindle) regroupées en fin de chapitre.
"""
import datetime, html, io, os, re, sys, uuid, zipfile
from bs4 import BeautifulSoup, Tag
from lxml import etree
from PIL import Image

SRC, COVER, OUT = sys.argv[1:4]
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.abspath(SRC))
TITRE = "Traité de réduction des risques liés aux drogues – Tome 1"
AUTEUR = "Association RISKY (@risky.asso)"
UID = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "https://traiterdr.netlify.app/traite-rdr.epub"))
SVG_ATTRS = ["viewBox", "preserveAspectRatio", "markerWidth", "markerHeight", "refX", "refY", "markerUnits",
             "textLength", "lengthAdjust", "gradientUnits", "gradientTransform", "patternUnits", "stdDeviation"]

soup = BeautifulSoup(open(SRC, encoding="utf8").read(), "html.parser")
body = soup.body
for t in body.find_all(["style", "script"]):
    t.decompose()
body.find("section", class_="sommaire").decompose()

# 1. Pages d'ouverture de partie : titre, chapitres de la partie (liens ajoutés plus bas)
for op in body.find_all("section", class_="opener"):
    h1 = op.find("h1")
    sub = op.find("div", class_="sub")
    new = BeautifulSoup('<section class="partie"></section>', "html.parser").section
    if re.match(r"^[A-Z]$", op.find("div", class_="num").get_text(strip=True)):
        p = soup.new_tag("p", attrs={"class": "partie-num"})
        p.string = "Partie " + op.find("div", class_="num").get_text(strip=True)
        new.append(p)
    for sp in h1.find_all("span", class_="no"):
        sp.decompose()
    new.append(h1.extract())
    if sub:
        sub.name = "p"
        new.append(sub.extract())
    new.append(soup.new_tag("ul", attrs={"class": "partie-toc"}))
    op.replace_with(new)

# 2. Nettoyage : attributs de mise en page, décor du PDF
for t in body.find_all(True):
    for a in [a for a in t.attrs if a.startswith("data-")]:
        del t[a]
for t in body.find_all("div", class_=["koala-rond", "glow", "logo", "koala"]):
    t.decompose()
# image placée au fil d'un paragraphe dans le Word : <figure> interdit dans <p>, on garde un bloc équivalent
for fig in body.find_all("figure"):
    if fig.find_parent(["p", "span", "a", "em", "strong", "h1", "h2", "h3", "h4", "h5", "h6"]):
        fig.name, fig.attrs = "span", {"class": "figure"}
        for c in fig.find_all("figcaption"):
            c.name, c.attrs = "span", {"class": "legende"}

# 3. Découpage : un fichier par partie, chapitre ou page liminaire
fichiers = []  # [nom, titre, [éléments]]
def nouveau(nom, titre):
    fichiers.append([nom, titre, []])
nouveau("liminaire.xhtml", "Dédicace")
for el in list(body.children):
    if not isinstance(el, Tag):
        if str(el).strip() and fichiers:
            fichiers[-1][2].append(el)
        continue
    if el.name == "section" and "partie" in el.get("class", []):
        nouveau("p%02d.xhtml" % len(fichiers), el.h1.get_text(" ", strip=True))
    elif el.name == "h1" or (el.name == "h2" and "chap" in el.get("class", [])):
        nouveau("c%02d.xhtml" % len(fichiers), el.get_text(" ", strip=True))
    fichiers[-1][2].append(el)

ou = {}  # id -> fichier
for nom, _, els in fichiers:
    for el in els:
        if isinstance(el, Tag):
            for t in [el] + el.find_all(id=True):
                if t.get("id"):
                    ou[t["id"]] = nom

# 4. Sommaire des parties (liens vers les chapitres)
for i, (nom, _, els) in enumerate(fichiers):
    sec = next((e for e in els if isinstance(e, Tag) and e.name == "section" and "partie" in e.get("class", [])), None)
    if sec is None:
        continue
    ul = sec.find("ul", class_="partie-toc")
    for nom2, titre2, els2 in fichiers[i + 1:]:
        if nom2.startswith("p"):
            break
        h = next(e for e in els2 if isinstance(e, Tag))
        li = soup.new_tag("li")
        a = soup.new_tag("a", href="%s#%s" % (nom2, h["id"]))
        a.string = titre2
        li.append(a)
        ul.append(li)
    if not ul.contents:
        ul.decompose()

# 5. Images : redimensionnées pour liseuse, largeur relative à celle du PDF
images = {}
def image(src):
    chemin = os.path.normpath(os.path.join(BASE, src))
    if chemin in images:
        return images[chemin][0]
    im = Image.open(chemin)
    im.load()
    transparent = im.mode in ("RGBA", "LA") or "transparency" in im.info
    if im.width > 1200:
        im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
    # on garde la plus légère : PNG en 256 couleurs (schémas) ou JPEG (photos, sauf transparence)
    essais = []
    buf = io.BytesIO()
    im.convert("RGBA" if transparent else "RGB").quantize(256, method=Image.FASTOCTREE if transparent else None) \
      .save(buf, "PNG", optimize=True)
    essais.append(("png", buf.getvalue()))
    if not transparent:
        buf = io.BytesIO()
        im.convert("RGB").save(buf, "JPEG", quality=82)
        essais.append(("jpg", buf.getvalue()))
    ext, data = min(essais, key=lambda e: len(e[1]))
    nom = "images/i%03d.%s" % (len(images) + 1, ext)
    images[chemin] = (nom, data)
    return nom

for nom, _, els in fichiers:
    for el in els:
        if not isinstance(el, Tag):
            continue
        for img in ([el] if el.name == "img" else []) + el.find_all("img"):
            m = re.search(r"width:([\d.]+)mm", img.get("style", ""))
            img["src"] = "../" + image(img["src"])
            img["alt"] = img.get("alt", "")
            if m and not img.find_parent(["td", "th"]):
                img["style"] = "width:%d%%" % min(100, round(float(m.group(1)) / 168 * 100))
            elif m:
                del img["style"]

# 6. Notes : appel numéroté, texte de la note en fin de chapitre ; liens internes réécrits
n = 0
xhtml = {}
for nom, titre, els in fichiers:
    frag = BeautifulSoup("<div></div>", "html.parser").div
    for el in els:
        frag.append(el)
    notes = []
    for fn in frag.find_all("span", class_="fn"):
        n += 1
        texte = fn.get_text(" ", strip=True)
        a = soup.new_tag("a", href="#n%d" % n, id="r%d" % n, attrs={"epub:type": "noteref", "class": "appel"})
        a.string = str(n)
        sup = soup.new_tag("sup")
        sup.append(a)
        fn.replace_with(sup)
        notes.append((n, texte))
    for a in frag.find_all("a", href=True):
        if a["href"].startswith("#") and a["href"][1:] in ou and ou[a["href"][1:]] != nom:
            a["href"] = ou[a["href"][1:]] + a["href"]
    corps = frag.decode_contents()
    if notes:
        corps += '<section class="notes" epub:type="footnotes"><h2 class="notes-titre">Notes</h2>'
        for k, t in notes:
            t = re.sub(r"https?://[^\s<]+[^\s<.,;:)»]", lambda m: '<a href="%s">%s</a>' % (m.group(0).replace('"', "%22"), m.group(0)),
                       html.escape(t, quote=False))
            corps += '<aside epub:type="footnote" id="n%d"><p><a href="#r%d">%d.</a> %s</p></aside>' % (k, k, k, t)
        corps += "</section>"
    xhtml[nom] = (titre, corps)

# 7. Page « à propos de cette version », tirée de la page de version du PDF
ver = BeautifulSoup(open(os.path.join(HERE, "..", "pdf", "version.html"), encoding="utf8").read(), "html.parser")
apropos = ['<section class="version"><p class="ver">%s</p><h1>%s</h1><p>%s</p>'
           % (ver.find(class_="ver").get_text(), ver.h1.get_text(), ver.find("p", class_="lead").get_text())]
for h2 in ver.find_all("h2"):
    apropos.append("<h2>%s</h2><ul>" % h2.get_text().capitalize())
    for li in h2.find_next("ul").find_all("li"):
        tag, txt = li.find_all("span", recursive=False)
        apropos.append("<li><b>%s</b> · %s</li>" % (tag.get_text(), txt.decode_contents()))
    apropos.append("</ul>")
box = ver.find(class_="box")
apropos.append('<div class="encadre">%s</div>' % box.decode_contents()
               .replace("La version la plus récente se lit", "Le PDF illustré, la recherche par thème et la version la plus récente sont")
               .replace(" et se cherche par thème sur", " sur"))
apropos.append('<p class="liseuse">Version liseuse générée le %s à partir du fichier Word du traité, '
               'avec le même texte que le PDF. Les grands tableaux et schémas se lisent mieux sur le PDF.</p></section>'
               % datetime.date.today().strftime("%d/%m/%Y"))
xhtml = {"version.xhtml": ("À propos de cette version", "".join(apropos)), **xhtml}
ordre = ["couverture.xhtml", "version.xhtml"] + [f[0] for f in fichiers]


def page(titre, corps):
    doc = ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
           '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="fr" xml:lang="fr">'
           '<head><meta charset="utf-8"/><title>%s</title><link rel="stylesheet" href="../style.css"/></head>'
           '<body>%s</body></html>' % (html.escape(titre), corps))
    doc = re.sub(r"<svg(?![^>]*xmlns=)", '<svg xmlns="http://www.w3.org/2000/svg"', doc)
    for a in SVG_ATTRS:
        doc = re.sub(r'(<[^>]*\s)%s=' % a.lower(), r"\1%s=" % a, doc)
    doc = doc.replace("&nbsp;", " ")
    etree.fromstring(doc.encode("utf8"))  # vérifie que le XHTML est bien formé
    return doc

xhtml["couverture.xhtml"] = ("Couverture", '<div class="couverture"><img src="../images/couverture.jpg" alt="%s"/></div>'
                             % html.escape(TITRE))

# 8. Table des matières (nav EPUB 3 + toc.ncx pour les anciennes liseuses)
arbre = []  # (niveau, titre, cible)
arbre.append((1, "À propos de cette version", "version.xhtml"))
for nom, _, els in fichiers[1:]:
    for el in els:
        if not isinstance(el, Tag):
            continue
        for h in ([el] if re.match(r"h[123]$", el.name) else []) + el.find_all(["h1", "h2", "h3"]):
            if "notes-titre" in h.get("class", []):
                continue
            lv = int(h.name[1])
            arbre.append((lv, re.sub(r"\s+", " ", h.get_text(" ", strip=True)), "%s#%s" % (nom, h["id"])))
# une partie (h1) contient ses chapitres (h2) ; les pages liminaires (Remerciements) restent au niveau 1
def emboite(items):
    racine, pile = [], [(0, [])]
    pile[0] = (0, racine)
    for lv, t, c in items:
        noeud = (t, c, [])
        while pile[-1][0] >= lv:
            pile.pop()
        pile[-1][1].append(noeud)
        pile.append((lv, noeud[2]))
    return racine
toc = emboite(arbre)

def nav_ol(nodes):
    return "<ol>%s</ol>" % "".join('<li><a href="%s">%s</a>%s</li>' % (c, html.escape(t), nav_ol(k) if k else "")
                                    for t, c, k in nodes)
nav = page("Sommaire", '<nav epub:type="toc" id="toc"><h1>Sommaire</h1>%s</nav>'
           '<nav epub:type="landmarks" hidden=""><ol><li><a epub:type="cover" href="couverture.xhtml">Couverture</a></li>'
           '<li><a epub:type="toc" href="nav.xhtml">Sommaire</a></li>'
           '<li><a epub:type="bodymatter" href="%s">Début du traité</a></li></ol></nav>'
           % (nav_ol(toc), next(f[0] for f in fichiers if f[0].startswith("p"))))

cpt = [0]
def ncx_points(nodes):
    out = ""
    for t, c, k in nodes:
        cpt[0] += 1
        out += ('<navPoint id="np%d" playOrder="%d"><navLabel><text>%s</text></navLabel><content src="text/%s"/>%s</navPoint>'
                % (cpt[0], cpt[0], html.escape(t), c, ncx_points(k)))
    return out
ncx = ('<?xml version="1.0" encoding="utf-8"?><ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
       '<head><meta name="dtb:uid" content="%s"/></head><docTitle><text>%s</text></docTitle><navMap>%s</navMap></ncx>'
       % (UID, html.escape(TITRE), ncx_points(toc)))

# 9. Paquet EPUB
pages = {nom: page(*xhtml[nom]) for nom in ordre}
manif = ['<item id="nav" href="text/nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
         '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
         '<item id="css" href="style.css" media-type="text/css"/>',
         '<item id="couv" href="images/couverture.jpg" media-type="image/jpeg" properties="cover-image"/>']
spine = []
for i, nom in enumerate(ordre):
    props = ' properties="svg"' if "<svg" in pages[nom] else ""
    manif.append('<item id="x%d" href="text/%s" media-type="application/xhtml+xml"%s/>' % (i, nom, props))
    spine.append('<itemref idref="x%d"/>' % i)
    if nom == "version.xhtml":
        spine.append('<itemref idref="nav"/>')
for i, (nom, _) in enumerate(images.values()):
    manif.append('<item id="i%d" href="%s" media-type="image/%s"/>' % (i, nom, "png" if nom.endswith("png") else "jpeg"))
maintenant = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
opf = ('<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
       'unique-identifier="uid" xml:lang="fr"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
       '<dc:identifier id="uid">%s</dc:identifier><dc:title>%s</dc:title><dc:creator>%s</dc:creator>'
       '<dc:publisher>Association RISKY</dc:publisher><dc:language>fr</dc:language><dc:date>%s</dc:date>'
       '<dc:subject>Réduction des risques</dc:subject><dc:subject>Drogues</dc:subject><dc:subject>Santé</dc:subject>'
       '<dc:description>Substances psychoactives et santé : comprendre sans bac+5. Sans jugement.</dc:description>'
       '<meta property="dcterms:modified">%s</meta><meta name="cover" content="couv"/></metadata>'
       '<manifest>%s</manifest><spine toc="ncx">%s</spine></package>'
       % (UID, html.escape(TITRE), AUTEUR, maintenant[:10], maintenant, "".join(manif), "".join(spine)))

with zipfile.ZipFile(OUT, "w") as z:
    z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
    def w(nom, data):
        z.writestr(nom, data, compress_type=zipfile.ZIP_DEFLATED)
    w("META-INF/container.xml", '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
      '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
    w("OEBPS/content.opf", opf)
    w("OEBPS/toc.ncx", ncx)
    w("OEBPS/style.css", open(os.path.join(HERE, "style.css"), encoding="utf8").read())
    w("OEBPS/text/nav.xhtml", nav)
    for nom, doc in pages.items():
        w("OEBPS/text/" + nom, doc)
    im = Image.open(COVER).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=88)
    w("OEBPS/images/couverture.jpg", buf.getvalue())
    for nom, data in images.values():
        w("OEBPS/" + nom, data)
print("fichiers", len(pages), "notes", n, "images", len(images), "entrées du sommaire", len(arbre),
      "taille %.1f Mo" % (os.path.getsize(OUT) / 1e6))
