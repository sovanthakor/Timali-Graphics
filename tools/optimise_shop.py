"""
Optimise the shop photo for the web:
- resize to a sensible width (about section shows it at ~500px, 2x for retina = 1000px)
- save as .webp (much smaller than .jpeg for photos)
Run: python tools/optimise_shop.py
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "img", "shop.jpeg")
DST = os.path.join(ROOT, "assets", "img", "shop.webp")
MAX_W = 1200

im = Image.open(SRC)
print("source   :", im.size, im.mode, f"{os.path.getsize(SRC)/1024:.0f} KB")

im = im.convert("RGB")

if im.width > MAX_W:
    ratio = MAX_W / im.width
    im = im.resize((MAX_W, round(im.height * ratio)), Image.LANCZOS)
print("resized  :", im.size)

im.save(DST, "WEBP", quality=82, method=6)
print("webp     :", f"{os.path.getsize(DST)/1024:.0f} KB  -> {DST}")

# keep a jpg fallback? no - every modern browser supports webp
if os.path.exists(SRC):
    os.remove(SRC)
    print("removed original jpeg (webp is the published format)")
