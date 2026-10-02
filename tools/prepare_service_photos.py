"""
Take the real service photos the owner dropped into assets/img/services/,
optimise them and rename them to the service slugs the website expects.

Run:  python tools/prepare_service_photos.py
"""
import os, glob, warnings
from PIL import Image

# some phone photos are 100+ megapixel, raise Pillow's decompression-bomb guard
Image.MAX_IMAGE_PIXELS = None
warnings.simplefilter("ignore", Image.DecompressionBombWarning)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "assets", "img", "services")

# owner filename (lower-cased)  ->  service slug used in the HTML
MAP = {
    "visiting card.jpg":          "visiting-cards",
    "weding card.jpg":            "wedding-invitations",
    "bener desigen.jpg":          "flex-banners",
    "billbook.jpg":               "bill-books",
    "leterhed.jpg":               "letterheads",
    "photo invition card.jpg":    "photo-invitations",
    "sticer.jpg":                 "stickers-labels",
    "food menu card.jpg":         "menu-cards",
    "certificet.jpg":             "certificates",
    "psport photo.jpg":           "passport-photos",
    "book cover desigen.jpg":     "book-covers",
}

MAX_EDGE = 1200   # rendered at ~500px, so 2x for retina
QUALITY = 82

print(f"{'source':<26}{'original':>14}{'->':>3}{'new':>13}{'->':>3}{'webp':>10}")
print("-" * 70)

ok, missing = [], []
for name, slug in sorted(MAP.items(), key=lambda x: x[1]):
    src = os.path.join(D, name)
    dst = os.path.join(D, slug + ".webp")
    if not os.path.exists(src):
        missing.append(slug)
        print(f"{name:<26}{'MISSING':>14}")
        continue

    im = Image.open(src)
    before = os.path.getsize(src) / 1024
    orig = im.size

    im = im.convert("RGB")
    if max(im.size) > MAX_EDGE:
        r = MAX_EDGE / max(im.size)
        im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    im.save(dst, "WEBP", quality=QUALITY, method=6)
    after = os.path.getsize(dst) / 1024

    print(f"{name:<26}{orig[0]}x{orig[1]:<7}{before:>6.0f}KB -> {im.width}x{im.height:<7}{after:>5.0f}KB")

    os.remove(src)
    ok.append(slug)

# remove the placeholder svg for every service we now have a real photo for
for slug in ok:
    ph = os.path.join(D, slug + ".svg")
    if os.path.exists(ph):
        os.remove(ph)
        print(f"removed placeholder: {slug}.svg")

print()
print(f"done: {len(ok)} photos optimised")
if missing:
    print("no photo supplied yet (placeholder kept): " + ", ".join(sorted(missing)))
