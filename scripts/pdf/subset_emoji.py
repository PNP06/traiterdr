# Réduit les polices Segoe UI Emoji (intégrées en entier par Word) aux seuls glyphes utilisés.
import io, sys, zlib, collections, pikepdf
from fontTools.ttLib import TTFont
from fontTools import subset

pdf = pikepdf.open(sys.argv[1])
used = collections.defaultdict(set)
done = set()

def fontfile(font):
    if font is None or font.get("/Subtype") != "/Type0":
        return None
    desc = font.DescendantFonts[0].get("/FontDescriptor")
    if desc is None or "Emoji" not in str(desc.FontName) or "/FontFile2" not in desc:
        return None
    return desc.FontFile2

def scan(stream, res, seen):
    key = stream.objgen
    if key != (0, 0) and key in seen:
        return
    seen.add(key)
    res = res or pikepdf.Dictionary()
    fonts = res.get("/Font", pikepdf.Dictionary())
    xobjs = res.get("/XObject", pikepdf.Dictionary())
    cur = None
    for operands, op in pikepdf.parse_content_stream(stream):
        op = str(op)
        if op == "Tf":
            cur = fontfile(fonts.get(str(operands[0])))
        elif cur is not None and op in ("Tj", "TJ", "'", '"'):
            for s in (operands[0] if op == "TJ" else [operands[-1]]):
                if isinstance(s, pikepdf.String):
                    b = bytes(s)
                    used[cur.objgen].update(int.from_bytes(b[i:i + 2], "big") for i in range(0, len(b) - 1, 2))
        elif op == "Do":
            xo = xobjs.get(str(operands[0]))
            if xo is not None and xo.get("/Subtype") == "/Form":
                scan(xo, xo.get("/Resources", res), seen)

seen = set()
for page in pdf.pages:
    scan(page, page.obj.get("/Resources"), seen)
    for a in page.obj.get("/Annots", []):
        ap = a.get("/AP")
        if ap is not None and isinstance(ap.get("/N"), pikepdf.Stream):
            scan(ap.N, ap.N.get("/Resources"), seen)

for obj in pdf.objects:
    if isinstance(obj, pikepdf.Dictionary) and obj.get("/Type") == "/FontDescriptor" \
            and "Emoji" in str(obj.get("/FontName")) and "/FontFile2" in obj:
        ff = obj.FontFile2
        if ff.objgen in done:
            continue
        done.add(ff.objgen)
        gids = used.get(ff.objgen)
        if not gids:
            print("police emoji sans usage repéré, laissée telle quelle", ff.objgen)
            continue
        before = len(ff.read_raw_bytes())
        font = TTFont(io.BytesIO(ff.read_bytes()))
        order = font.getGlyphOrder()
        opts = subset.Options(); opts.retain_gids = True; opts.notdef_outline = True
        opts.drop_tables += ["COLR", "CPAL", "meta"]; opts.name_IDs = ["*"]
        sub = subset.Subsetter(opts)
        sub.populate(glyphs=[order[g] for g in gids if g < len(order)] + [order[0]])
        sub.subset(font)
        out = io.BytesIO(); font.save(out)
        ff.write(zlib.compress(out.getvalue(), 9), filter=pikepdf.Name.FlateDecode)
        ff.Length1 = len(out.getvalue())
        print("police emoji", ff.objgen, len(gids), "glyphes", before // 1024, "KB ->", len(ff.read_raw_bytes()) // 1024, "KB")
pdf.save(sys.argv[2], object_stream_mode=pikepdf.ObjectStreamMode.generate, compress_streams=True, linearize=True)
