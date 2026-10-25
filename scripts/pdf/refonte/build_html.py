"""Transforme la sortie pandoc du traité en HTML paginable (paged.js) avec le gabarit.

Usage : python3 build_html.py prep.html traite.html [corrections.json]

- titres Word : Titre 1 = partie (page d'ouverture), Titre 2 = chapitre (nouvelle page),
  Titre 3 et suivants = sections ; les paragraphes courts entièrement en gras/italique/souligné
  (« Pourquoi », « Objectif »…) deviennent des titres de section, un niveau sous le titre courant ;
- notes Word -> notes en bas de page ;
- paragraphes encadrés -> encadrés koala ; légendes -> sous la figure ou le tableau ;
- [[SCHEMA:id]] -> schemas/<id>.svg ou .png s'il existe, sinon cadre « schéma à reprendre » ;
- corrections.json : liste de corrections d'orthographe validées {"avant": ..., "apres": ...}.
"""
import json, os, re, sys
from bs4 import BeautifulSoup, NavigableString, Tag

SRC, OUT = sys.argv[1:3]
CORR = sys.argv[3] if len(sys.argv) > 3 else None
HERE = os.path.dirname(os.path.abspath(__file__))
FRONT = {"Remerciements"}

soup = BeautifulSoup(open(SRC, encoding="utf8").read(), "html.parser")

# 1. Notes : contenu de la note à l'endroit de l'appel
notes = {}
fsec = soup.find(["section", "aside"], class_="footnotes")
if fsec:
    for li in fsec.find_all("li"):
        for back in li.find_all("a", class_="footnote-back"):
            back.decompose()
        notes[li.get("id")] = li.decode_contents().strip()
    fsec.decompose()
for a in soup.find_all("a", class_="footnote-ref"):
    # note réduite à du texte simple : paged.js boucle sur les notes contenant des blocs
    content = BeautifulSoup(notes.get(a["href"].lstrip("#"), ""), "html.parser").get_text(" ", strip=True)
    span = soup.new_tag("span", attrs={"class": "fn"})
    span.string = re.sub(r"\s+", " ", content)
    a.replace_with(span)

# 1 bis. Chapitres remplacés par une version composée à la main (remplacements/<id du titre 1>.html)
for h1 in soup.find_all("h1"):
    f = os.path.join(HERE, "remplacements", "%s.html" % h1.get("id", ""))
    if not os.path.exists(f):
        continue
    for sib in list(h1.next_siblings):
        if isinstance(sib, Tag) and sib.name == "h1":
            break
        sib.extract()
    h1.replace_with(BeautifulSoup('<div class="remplace" data-f="%s"></div>' % h1["id"], "html.parser"))

# 2. Styles Word : on garde le contenu, on retire les enveloppes
for el in soup.find_all(attrs={"data-custom-style": True}):
    style = el["data-custom-style"]
    if el.name == "div" and style == "Encadre":
        el.name = "div"; el.attrs = {"class": ["encadre-p"]}
    elif el.name == "div" and style == "caption":
        el.attrs = {"class": ["legende"]}
    else:
        el.unwrap()

# encadrés consécutifs fusionnés
def merge_encadres(parent):
    box = None
    for el in list(parent.children):
        if isinstance(el, NavigableString):
            if el.strip():
                box = None
            continue
        if el.name == "div" and "encadre-p" in el.get("class", []):
            if box is None:
                box = soup.new_tag("div", attrs={"class": "encadre"})
                el.insert_before(box)
            for c in list(el.children):
                box.append(c)
            el.decompose()
        else:
            box = None
            merge_encadres(el)
merge_encadres(soup)
for box in soup.find_all("div", class_="encadre"):
    if not box.get_text(strip=True) and not box.find("img"):
        box.decompose()
    else:
        for p in box.find_all("p"):
            if not p.get_text(strip=True) and not p.find("img"):
                p.decompose()
        if box.get_text(" ", strip=True).startswith("Ce livre est écrit dans le seul but"):
            box["class"] = ["encadre", "fin"]

# 3. Paragraphes parasites (tirets isolés, tirets collés en début de paragraphe)
for p in soup.find_all("p"):
    t = p.get_text()
    if t.strip() in ("-", "–", "") and not p.find(["img", "span"]):
        p.decompose()
        continue
    first = p.contents[0] if p.contents else None
    if isinstance(first, NavigableString) and re.match(r"^-(?=[A-ZÀ-ÖØ-Þa-z«])", first):
        first.replace_with(first[1:])

# 4. Images -> figures ; légendes rattachées
for bq in soup.find_all("blockquote"):
    if bq.find("img") and not bq.get_text(strip=True):  # image simplement en retrait dans Word
        bq.unwrap()
for img in soup.find_all("img"):
    img.attrs.pop("style", None)
    img.attrs.pop("width", None)
    img.attrs.pop("height", None)
    if img.find_parent(["td", "th"]):
        continue
    p = img.find_parent("p")
    holder = p if p is not None and p.get_text(strip=True) in ("", "-", "–") else None
    fig = soup.new_tag("figure")
    (holder or img).insert_before(fig)
    fig.append(img.extract())
    if holder is not None:
        for other in holder.find_all("img"):
            fig.append(other.extract())
        holder.decompose()
for leg in soup.find_all(["div", "p"], class_="legende"):
    prev = leg.find_previous_sibling()
    leg.name = "figcaption" if prev is not None and prev.name == "figure" else "p"
    leg.attrs = {"class": ["legende"]} if leg.name == "p" else {}
    if leg.name == "figcaption":
        prev.append(leg.extract())
    for p in leg.find_all("p"):
        p.unwrap()

# 5. Schémas Word non convertibles
for t in soup.find_all(string=re.compile(r"\[\[SCHEMA:[\w-]+\]\]")):
    sid = re.search(r"\[\[SCHEMA:([\w-]+)\]\]", t).group(1)
    holder = t.find_parent("p") or t
    path = None
    for ext in ("svg", "png"):
        if os.path.exists(os.path.join(HERE, "schemas", "%s.%s" % (sid, ext))):
            path = os.path.join(HERE, "schemas", "%s.%s" % (sid, ext))
    if path and path.endswith(".svg"):
        new = BeautifulSoup("<figure>%s</figure>" % open(path, encoding="utf8").read(), "html.parser")
    elif path:
        new = BeautifulSoup('<figure><img src="file://%s"></figure>' % path, "html.parser")
    else:
        new = BeautifulSoup('<div class="schema-a-faire">Schéma Word à reprendre (%s)</div>' % sid, "html.parser")
    holder.replace_with(new)

# 6. Titres : structure et pseudo-titres
PUNCT = re.compile(r"[.;,…:]\s*$")
def pseudo_title(p):
    if p.name != "p" or p.find_parent(["td", "th", "li", "blockquote", "figure"]) or "encadre" in " ".join(
            sum([x.get("class", []) for x in p.parents if isinstance(x, Tag)], [])):
        return False
    t = p.get_text(" ", strip=True)
    if not t or len(t) > 90 or PUNCT.search(t) or p.find(["img", "span"]):
        return False
    inner = [c for c in p.contents if not (isinstance(c, NavigableString) and not c.strip())]
    if len(inner) != 1 or not isinstance(inner[0], Tag) or inner[0].name not in ("strong", "em", "u"):
        return False
    return inner[0].get_text(" ", strip=True) == t and inner[0].find("strong") is not None or inner[0].name == "strong"

body = soup
level = 1
parts, chap_in_part = 0, 0
for el in list(soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p"])):
    if el.parent is None:
        continue
    if el.name[0] == "h" and el.name[1:].isdigit():
        level = int(el.name[1])
        el.attrs.pop("class", None)
        for u in el.find_all(["u", "em", "strong", "span"]):
            u.unwrap()
        first = el.contents[0] if el.contents else None
        if isinstance(first, NavigableString) and re.match(r"^\s*[-–]\s*", first):
            first.replace_with(re.sub(r"^\s*[-–]\s*", "", first))
        continue
    if pseudo_title(el):
        lv = max(level + 1, 3)
        el.name = "h%d" % min(lv, 6)
        if lv > 6:
            el["class"] = ["h7"]
        for u in el.find_all(["u", "em", "strong"]):
            u.unwrap()

# 7. Corrections d'orthographe validées
if CORR and os.path.exists(CORR):
    for c in json.load(open(CORR, encoding="utf8")):
        n = 0
        for t in soup.find_all(string=lambda s: c["avant"] in s):
            t.replace_with(t.replace(c["avant"], c["apres"]))
            n += 1
        if n == 0:
            print("correction non appliquée :", c["avant"], file=sys.stderr)

# 8. Ouvertures de parties, chapitres, sommaire
KOALA = '<div class="koala"><img src="koala.jpg" alt=""></div>'
LOGO = ('<div class="logo">risky<svg width="52" height="7" viewBox="0 0 120 14"><path d="M3 10 C 40 2, 80 2, 117 7" '
        'stroke="#E8794F" stroke-width="5" fill="none" stroke-linecap="round"/></svg></div>')
toc = []
num = 0
heads = [h for h in soup.find_all(["h1", "h2", "h3", "div"]) if h.name != "div" or "remplace" in h.get("class", [])]
remplacements = {}
for i, h in enumerate(heads):
    if h.name == "div":
        f = h["data-f"]
        rep = BeautifulSoup(open(os.path.join(HERE, "remplacements", f + ".html"), encoding="utf8").read(), "html.parser")
        for x in rep.find_all(["h1", "h3"]):
            x["id"] = x.get("id") or "%s-%d" % (f, len(toc))
            toc.append((1 if x.name == "h1" else 3, x.get_text(" ", strip=True), x["id"]))
        remplacements[f] = str(rep)
        continue
    title = h.get_text(" ", strip=True)
    hid = h.get("id") or "t%d" % i
    h["id"] = hid
    if h.name == "h1":
        if title in FRONT:
            h["class"] = ["front"]
            toc.append((1, title, hid))
            continue
        n = "00" if title == "Introduction" else "%02d" % (num + 1)
        if title != "Introduction":
            num += 1
        subs = []
        for nxt in heads[i + 1:]:
            if nxt.name == "h1":
                break
            if nxt.name == "h2":
                subs.append(nxt.get_text(" ", strip=True))
        items = "".join('<div><span>%02d</span>%s</div>' % (k + 1, s) for k, s in enumerate(subs))
        opener = BeautifulSoup('<section class="opener"><div class="glow"></div>%s<div class="part">TRAITÉ RDR · <b>TOME 1</b></div>'
                               '<div class="num">%s</div><h1 id="%s">%s</h1><div class="toc%s">%s</div>%s</section>'
                               % (LOGO, n, hid, title, " dense" if len(subs) > 10 else "", items, KOALA), "html.parser")
        h.replace_with(opener)
        toc.append((1, title, hid))
        chap_in_part = 0
    elif h.name == "h2":
        chap_in_part += 1
        h["class"] = ["chap"]
        h["data-num"] = "%s · %02d" % (toc[-1][1].upper() if toc else "", chap_in_part)
        toc.append((2, title, hid))
    else:
        toc.append((3, title, hid))

som = ['<section class="sommaire"><h1>Sommaire</h1><ol>']
for lv, t, hid in toc:
    som.append('<li class="t%d"><a href="#%s">%s</a></li>' % (lv, hid, t))
som.append("</ol></section>")

front = open(os.path.join(HERE, "debut.html"), encoding="utf8").read()
tpl = open(os.path.join(HERE, "page.html"), encoding="utf8").read()
html = tpl.replace("{{CSS}}", open(os.path.join(HERE, "gabarit.css"), encoding="utf8").read()) \
          .replace("{{CORPS}}", front + "".join(som) + str(soup))
for f, rep in remplacements.items():
    html = html.replace('<div class="remplace" data-f="%s"></div>' % f, rep)

# 9. Numérotation A, A.1, A.1.4 et fil d'Ariane des en-têtes :
#    à gauche la partie, à droite chapitre › section (data-partie, data-fil)
full = BeautifulSoup(html, "html.parser")
lettre, chap, sec, fil_chap = None, 0, 0, ""
for h in full.find_all(["h1", "h2", "h3"]):
    if h.find_parent("section", class_="sommaire"):
        continue
    def prefix(no):
        sp = full.new_tag("span", attrs={"class": "no"})
        sp.string = no
        h.insert(0, " ")
        h.insert(0, sp)
    titre = re.sub(r"\s+", " ", h.get_text(" ", strip=True))
    if h.name == "h1" and h.find_parent("section", class_="opener"):
        lettre = chr(ord("A") + (0 if lettre is None else ord(lettre) - ord("A") + 1))
        chap, sec, fil_chap = 0, 0, ""
        h.find_parent("section").find("div", class_="num").string = lettre
        for k, sp in enumerate(h.find_parent("section").select(".toc span")):
            sp.string = "%s.%d" % (lettre, k + 1)
        prefix(lettre + " ·")
        h["data-partie"] = "Partie %s – %s" % (lettre, titre)
        h["data-fil"] = ""
    elif h.name == "h1":
        h["data-partie"] = ""
        h["data-fil"] = titre
    elif lettre is None:
        continue
    elif h.name == "h2":
        chap += 1
        sec = 0
        no = "%s.%d" % (lettre, chap)
        prefix(no)
        h["data-num"] = "PARTIE %s" % lettre
        fil_chap = "%s %s" % (no, titre)
        h["data-fil"] = fil_chap
    else:
        nxt = h.find_next(["h1", "h2"])
        if not chap and nxt is not None and nxt.name == "h2":
            # introduction de partie, avant le premier chapitre : pas de numéro
            h["data-fil"] = titre
            continue
        sec += 1
        no = "%s.%d.%d" % (lettre, chap, sec) if chap else "%s.%d" % (lettre, sec)
        prefix(no)
        h["data-fil"] = ("%s  ›  %s %s" % (fil_chap, no, titre)) if fil_chap else "%s %s" % (no, titre)
# 10. Légendes : les numéros Word (champs SEQ) sont perdus à la conversion, on renumérote dans l'ordre du livre
cpt = {"Figure": 0, "Tableau": 0}
for leg in full.find_all(["figcaption", "p", "div"]):
    if leg.name != "figcaption" and "legende" not in leg.get("class", []):
        continue
    s = leg.find(string=re.compile(r"\S"))
    m = s and re.match(r"\s*(Figure|Tableau)\s*\d*\s*\.?\s*", s)
    if not m:
        continue
    cpt[m.group(1)] += 1
    s.replace_with(s[m.end():])
    b = full.new_tag("b")
    b.string = "%s %d. " % (m.group(1), cpt[m.group(1)])
    leg.insert(0, b)
print("légendes numérotées", cpt)
html = str(full)
open(OUT, "w", encoding="utf8").write(html)
print("titres", len(toc), "notes", len(notes), "encadrés", len(soup.find_all("div", class_="encadre")),
      "figures", len(soup.find_all("figure")), "tableaux", len(soup.find_all("table")))
