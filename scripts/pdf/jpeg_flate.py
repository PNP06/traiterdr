# Réencode en JPEG (qualité 85) les images non compressées en JPEG quand ça divise leur poids par 2 au moins.
import io, sys, zlib, pikepdf
from PIL import Image

pdf = pikepdf.open(sys.argv[1])
saved = n = 0
for obj in list(pdf.objects):
    if not (isinstance(obj, pikepdf.Stream) and obj.get("/Subtype") == "/Image"):
        continue
    if obj.get("/Filter") != "/FlateDecode" or obj.get("/ImageMask") or obj.get("/BitsPerComponent", 8) != 8:
        continue
    cs = obj.get("/ColorSpace")
    if isinstance(cs, pikepdf.Array) and cs[0] == "/ICCBased":
        ncomp = int(cs[1].get("/N", 3))
    elif cs in ("/DeviceRGB", "/DeviceGray"):
        ncomp = 3 if cs == "/DeviceRGB" else 1
    else:
        continue
    mode = {3: "RGB", 1: "L"}.get(ncomp)
    data = obj.read_bytes()
    if mode is None or len(data) != obj.Width * obj.Height * ncomp:
        continue
    im = Image.frombytes(mode, (int(obj.Width), int(obj.Height)), data)
    if im.mode not in ("RGB", "L") or im.width * im.height < 40000:
        continue
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=85, optimize=True)
    before = len(obj.read_raw_bytes())
    if len(buf.getvalue()) * 2 > before:
        continue
    obj.write(buf.getvalue(), filter=pikepdf.Name.DCTDecode)
    for k in ("/DecodeParms", "/Decode"):
        if k in obj:
            del obj[k]
    saved += before - len(buf.getvalue()); n += 1
print(n, "images réencodées,", saved // 1024, "KB gagnés")
pdf.save(sys.argv[2], object_stream_mode=pikepdf.ObjectStreamMode.generate, compress_streams=True, linearize=True)
