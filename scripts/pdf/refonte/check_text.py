"""Vérifie qu'aucun mot du Word n'a été perdu dans le PDF produit.

Usage : python3 check_text.py prep.html traite.pdf
Liste les suites de 4 mots ou plus présentes dans le Word et absentes du PDF
(les notes, en-têtes et numéros ajoutés par la mise en page sont ignorés).
"""
import difflib, html, re, subprocess, sys

src, pdf = sys.argv[1:3]
t = open(src, encoding="utf8").read()
t = re.sub(r"<aside.*?</aside>", "", t, flags=re.S)
t = re.sub(r'<a href="#fn\d+"[^>]*>.*?</a>', "", t, flags=re.S)
t = html.unescape(re.sub(r"<[^>]+>", " ", t))
# texte du corps seulement : les fils d'Ariane des marges (liseres.py) sont exclus (A4, 15 mm de chaque côté)
p = subprocess.run(["pdftotext", "-x", "43", "-y", "0", "-W", "510", "-H", "842", pdf, "-"], capture_output=True, text=True).stdout
p = "\n".join(l for l in p.split("\n") if not re.match(r"\s*(TRAITÉ RDR · TOME 1|RISKY : TRAITÉ DE RÉDUCTION DES RISQUES ET DES DOMMAGES)", l, re.I))
def toks(s):
    s = s.replace("­", "")
    s = re.sub(r"(\w)-\n(\w)", r"\1\2", s)
    return [w for w in re.findall(r"\w+", s.lower()) if not w.isdigit()]
a, b = toks(t), toks(p)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
manque = [" ".join(a[i1:i2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op in ("delete", "replace") and i2 - i1 >= 4]
print("mots Word", len(a), "mots PDF", len(b), "suites manquantes", len(manque))
for m in manque:
    print("-", m[:240])
