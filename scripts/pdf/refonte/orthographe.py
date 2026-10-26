"""Relevé des fautes d'orthographe et de grammaire avec LanguageTool (API publique).

Usage : python3 orthographe.py prep.html sortie.json
Envoie le texte paragraphe par paragraphe (par lots de ~15 Ko, au rythme permis par l'API)
et enregistre toutes les remarques avec leur contexte, pour tri.
"""
import json, re, sys, time, urllib.parse, urllib.request
from bs4 import BeautifulSoup

SRC, OUT = sys.argv[1:3]
soup = BeautifulSoup(open(SRC, encoding="utf8").read(), "html.parser")
for a in soup.find_all("a", class_="footnote-ref"):
    a.decompose()
blocs = []
for el in soup.find_all(["p", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6"]):
    if el.find(["p", "li"]) or el.find_parent(["aside", "section"], class_="footnotes"):
        continue
    t = re.sub(r"\s+", " ", el.get_text(" ")).strip()
    if len(t) > 3 and not re.match(r"^https?://", t):
        blocs.append(t)
print(len(blocs), "blocs", sum(map(len, blocs)), "caractères", file=sys.stderr)

lots, cur = [], []
for b in blocs:
    if sum(len(x) + 2 for x in cur) + len(b) > 15000 and cur:
        lots.append(cur); cur = []
    cur.append(b)
lots.append(cur)

res = []
for i, lot in enumerate(lots):
    texte = "\n\n".join(lot)
    data = urllib.parse.urlencode({"text": texte, "language": "fr", "level": "default"}).encode()
    for essai in range(5):
        try:
            r = json.load(urllib.request.urlopen("https://api.languagetool.org/v2/check", data, timeout=120))
            break
        except Exception as e:
            print("lot", i, "erreur", e, file=sys.stderr); time.sleep(30)
    else:
        continue
    for m in r["matches"]:
        o, l = m["offset"], m["length"]
        res.append({"lot": i, "mot": texte[o:o + l], "contexte": texte[max(0, o - 60):o + l + 60],
                    "suggestions": [x["value"] for x in m["replacements"][:3]],
                    "regle": m["rule"]["id"], "categorie": m["rule"]["category"]["id"], "message": m["message"]})
    print("lot", i + 1, "/", len(lots), len(res), "remarques", file=sys.stderr)
    json.dump(res, open(OUT, "w", encoding="utf8"), ensure_ascii=False, indent=0)
    time.sleep(13)
