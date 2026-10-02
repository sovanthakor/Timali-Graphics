"""
Final batch: map the remaining real design images to their service slugs.

NOTE on T-shurt.jpg
-------------------
That file is a stock photo from Unsplash (filename still contains "unsplash"
and the photographer's handle). It shows a plain black t-shirt printed by a
different company reading "SEVEN ZERO FIVE / LOS ANGELES, CA".

It is not Timali Graphics work, so it is NOT published. The file is moved to
tools/_unused/ so it is kept on disk but stays off the website, and
screen-printing keeps its placeholder until a real photo is supplied.

Run:  python tools/prepare_service_photos_2.py
"""
import os, shutil
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "assets", "img", "services")
UNUSED = os.path.join(ROOT, "tools", "_unused")

MAP = {
    "Appreciation card.png":  "appreciation-cards",
    "Catalogue.png":          "catalogue-design",
    "Custom Printing.png":    "custom-printing",
}

print(f"{'source':<28}{'original':>13}{'->':>3}{'webp':>10}")
print("-" * 56)

for name, slug in MAP.items():
    src = os.path.join(D, name)
    dst = os.path.join(D, slug + ".webp")
    if not os.path.exists(src):
        print(f"{name:<28}{'MISSING':>13}")
        continue

    im = Image.open(src)
    before = os.path.getsize(src) / 1024
    w, h = im.size

    im.save(dst, "WEBP", quality=85, method=6)   # WEBP keeps the alpha channel
    after = os.path.getsize(dst) / 1024

    print(f"{name:<28}{w}x{h:<6}{before:>6.0f}KB ->{after:>6.0f}KB   {slug}")

    os.remove(src)
    ph = os.path.join(D, slug + ".svg")
    if os.path.exists(ph):
        os.remove(ph)
        print(f"   removed placeholder {slug}.svg")

# --- stock photo: keep the file, keep it off the website ---
stock = os.path.join(D, "T-shurt.jpg")
if os.path.exists(stock):
    os.makedirs(UNUSED, exist_ok=True)
    shutil.move(stock, os.path.join(UNUSED, "T-shurt_STOCK-UNSPLASH-not-our-work.jpg"))
    print()
    print("T-shurt.jpg -> moved to tools/_unused/ (stock photo, not published)")
