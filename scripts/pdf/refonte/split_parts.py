"""Découpe le HTML complet en un fichier par partie, rendus séparément puis assemblés.

Usage : python3 split_parts.py traite.html dossier/
Écrit 00.html (début + remerciements + introduction…), 01.html, 02.html…
Le sommaire n'est pas inclus : il est composé à la fin, une fois les numéros de page connus.
"""
import os, re, sys
src, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
html = open(src, encoding="utf8").read()
head, body = html.split("<body>", 1)
body = body.rsplit("</body>", 1)[0]
body = re.sub(r'<section class="sommaire">.*?</section>', "", body, count=1, flags=re.S)
chunks = re.split(r'(?=<section class="opener">)', body)
# l'introduction reste avec le début du livre
merged = [chunks[0]]
for c in chunks[1:]:
    if '<div class="num">00</div>' in c:
        merged[-1] += c
    else:
        merged.append(c)
for i, c in enumerate(merged):
    open(os.path.join(out, "%02d.html" % i), "w", encoding="utf8").write(head + "<body>" + c + "</body></html>")
    print("%02d" % i, len(c), re.search(r'<h1[^>]*>([^<]*)', c).group(1) if "<h1" in c else "")
