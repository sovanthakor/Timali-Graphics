"""
Temporary placeholder images for Timali Graphics service pages.
Replace with your REAL sample photos (same file name) when available.
Brand: Navy #272238 · Yellow #FBBA00
"""
import os, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "services")
os.makedirs(OUT, exist_ok=True)

NAVY = "#272238"
NAVY_LT = "#332C47"
YELLOW = "#FBBA00"
BG = "#F2F1F5"
LINE = "#DFDDE6"
MUTED = "#8F88A6"

TPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <rect width="800" height="600" fill="{bg}"/>
  <!-- paper / print sample silhouette -->
  <g transform="translate(400 268)">
    <rect x="-215" y="-140" width="430" height="280" rx="10" fill="#FFFFFF" stroke="{line}" stroke-width="2"/>
    <rect x="-185" y="-110" width="120" height="12" rx="6" fill="{yellow}"/>
    <rect x="-185" y="-82" width="250" height="9" rx="4.5" fill="#DFDDE6"/>
    <rect x="-185" y="-62" width="290" height="9" rx="4.5" fill="#DFDDE6"/>
    <rect x="-185" y="-42" width="200" height="9" rx="4.5" fill="#DFDDE6"/>
    <rect x="-185" y="-8" width="150" height="70" rx="6" fill="{navy}"/>
    <rect x="-15" y="-8" width="80" height="30" rx="5" fill="#EFEDF3"/>
    <rect x="-15" y="30" width="80" height="32" rx="5" fill="#EFEDF3"/>
    <rect x="-185" y="82" width="370" height="8" rx="4" fill="#DFDDE6"/>
    <rect x="-185" y="100" width="240" height="8" rx="4" fill="#DFDDE6"/>
  </g>
  <g transform="translate(400 462)">
    <rect x="-40" y="-40" width="80" height="80" rx="12" fill="{navy}"/>
    <path d="M-16 -6 h20 l12 12 v20 a4 4 0 0 1-4 4 h-28 a4 4 0 0 1-4-4 z" fill="none" stroke="{yellow}" stroke-width="3.4" stroke-linejoin="round"/>
    <path d="M4 -6 v12 h12" fill="none" stroke="{yellow}" stroke-width="3.4" stroke-linejoin="round"/>
  </g>
  <text x="400" y="530" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"
        font-size="22" font-weight="700" fill="{navy}">{title}</text>
  <text x="400" y="556" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"
        font-size="14" fill="{muted}">Temporary image — replace with your real sample</text>
</svg>
"""

items = [
    ("wedding-invitations", "Wedding Invitation"),
    ("visiting-cards",       "Visiting Card"),
    ("bill-books",           "Bill Book"),
    ("letterheads",          "Letterhead"),
    ("photo-invitations",    "Photo Invitation"),
    ("stickers-labels",      "Sticker &amp; Label"),
    ("menu-cards",           "Menu Card"),
    ("screen-printing",      "Screen Printing"),
    ("passport-photos",      "Passport Photo"),
    ("certificates",         "Certificate"),
    ("flex-banners",         "Flex Banner"),
    ("book-covers",          "Book Cover"),
    ("catalogue-design",     "Catalogue Design"),
    ("appreciation-cards",   "Appreciation Card"),
    ("custom-printing",      "Custom Printing"),
]

for slug, title in items:
    svg = textwrap.dedent(TPL).format(
        bg=BG, line=LINE, navy=NAVY, navy_lt=NAVY_LT, yellow=YELLOW, muted=MUTED, title=title
    )
    with open(os.path.join(OUT, slug + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)

print("Created", len(items), "service placeholders in", OUT)
