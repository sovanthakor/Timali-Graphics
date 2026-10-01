"""
Generates neutral placeholder images for the Timali Graphics portfolio grid.
Replace these files with your REAL work photos (same file name, .jpg) later.
Brand colours: Navy #272238 · Yellow #FBBA00
"""
import os, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "portfolio")
os.makedirs(OUT, exist_ok=True)

NAVY = "#272238"
NAVY_LT = "#332C47"
YELLOW = "#FBBA00"
BG = "#F2F1F5"
LINE = "#DFDDE6"
MUTED = "#8F88A6"

TPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <rect width="800" height="600" fill="{bg}"/>
  <rect x="20" y="20" width="760" height="560" rx="18" fill="none" stroke="{line}" stroke-width="2" stroke-dasharray="10 8"/>
  <g transform="translate(400 250)">
    <rect x="-70" y="-52" width="140" height="104" rx="10" fill="{navy}"/>
    <rect x="-52" y="-34" width="58" height="7" rx="3.5" fill="{yellow}"/>
    <rect x="-52" y="-16" width="104" height="6" rx="3" fill="#4B4363"/>
    <rect x="-52" y="-2"  width="78"  height="6" rx="3" fill="#4B4363"/>
    <rect x="-52" y="12"  width="92"  height="6" rx="3" fill="#4B4363"/>
    <rect x="-52" y="30"  width="44"  height="9" rx="4" fill="{yellow}" opacity=".75"/>
  </g>
  <text x="400" y="392" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"
        font-size="27" font-weight="700" fill="{navy}">{title}</text>
  <text x="400" y="424" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"
        font-size="16" fill="{muted}">{sub}</text>
  <g transform="translate(400 486)">
    <rect x="-152" y="-22" width="304" height="44" rx="10" fill="{navy}"/>
    <text x="0" y="6" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"
          font-size="14" font-weight="700" letter-spacing="2.4" fill="{yellow}">ADD YOUR REAL PHOTO HERE</text>
  </g>
  <text x="400" y="546" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"
        font-size="13" fill="{muted}">assets/img/portfolio/{fname}</text>
</svg>
"""

items = [
    ("01-visiting-card",      "Visiting Card",        "Business &amp; personal cards"),
    ("02-wedding-invitation", "Wedding Invitation",   "Flex &amp; premium invite"),
    ("03-flex-banner",        "Flex Banner",          "Events &amp; promotions"),
    ("04-sticker",            "Sticker &amp; Label",     "Product &amp; packaging"),
    ("05-menu-card",          "Menu Card",            "Restaurant &amp; cafe"),
    ("06-certificate",        "Certificate",          "School &amp; corporate"),
    ("07-bill-book",          "Bill Book",            "Shop &amp; counter"),
    ("08-letterhead",         "Letterhead",           "Business stationery"),
    ("09-book-cover",         "Book Cover",           "Notebook &amp; diary"),
    ("10-catalogue",          "Catalogue",            "Product catalogue"),
    ("11-colour-banner",      "Colour Banner",        "Advertisement"),
    ("12-passport-photo",     "Passport Photo",       "ID &amp; stamp size"),
]

for fname, title, sub in items:
    svg = textwrap.dedent(TPL).format(
        bg=BG, line=LINE, navy=NAVY, navy_lt=NAVY_LT, yellow=YELLOW,
        muted=MUTED, title=title, sub=sub, fname=fname + ".svg"
    )
    with open(os.path.join(OUT, fname + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)

print("Created", len(items), "placeholders in", OUT)
