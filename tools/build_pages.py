"""
Builds the remaining Timali Graphics pages so that header, footer, lightbox and
sticky mobile CTA stay identical across every page.

Run:  python tools/build_pages.py
"""
import os
from urllib.parse import quote as urlquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- shared parts
# ---------------------------------------------------------------- shared parts
SITE = "https://timali-graphics.web.app"


def head(title, desc, slug=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="graphic design services in Idar, printing services in Idar, Timali Graphics, printing shop in Idar, visiting card printing Idar, wedding card Idar, banner printing Idar">
<meta name="author" content="Timali Graphics">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#272238">
<link rel="canonical" href="{SITE}/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Timali Graphics">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/logo.svg">
<meta property="og:url" content="{SITE}/{slug}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="assets/img/logo.svg">
<link rel="apple-touch-icon" href="assets/img/logo.svg">
<script>document.documentElement.className += ' js';</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
"""

HEADER = """
<header class="header">
  <div class="wrap header__in">
    <a class="brand" href="index.html">
      <img src="assets/img/logo.svg" alt="Timali Graphics logo" width="52" height="52">
      <span class="brand__txt">
        <b>Timali Graphics</b>
        <small>Graphic Design &amp; Printing</small>
      </span>
    </a>
    <nav class="nav" id="nav" aria-label="Main navigation">
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="services.html">Services</a>
      <a href="solutions.html">Printing Solutions</a>
      <a href="portfolio.html">Portfolio</a>
      <a href="contact.html">Contact</a>
      <a class="btn btn--primary btn--sm header__cta" href="quote.html">Get a Quote</a>
    </nav>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
"""

PHEAD = """
<section class="phead">
  <div class="wrap">
    <ol class="crumbs">
      <li><a href="index.html">Home</a></li>
      <li>{crumb}</li>
    </ol>
    <h1>{h1}</h1>
    <p>{lead}</p>
  </div>
</section>
"""

FOOTER = """
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <div class="footer__brand">
          <img src="assets/img/logo.svg" alt="" width="50" height="50">
          <span><b>Timali Graphics</b><small>Graphic Design &amp; Printing</small></span>
        </div>
        <p>Creative designs, quality printing and reliable solutions for businesses, events and everyday printing needs in Idar, Gujarat.</p>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul class="footer__links">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="solutions.html">Printing Solutions</a></li>
          <li><a href="portfolio.html">Portfolio</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="quote.html">Get a Quote</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul class="footer__contact">
          <li><svg viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.25 1z"/></svg><a href="tel:+919687130009">9687130009</a></li>
          <li><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3 7l9 6 9-6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg><a href="mailto:timaligraphics2015@gmail.com">timaligraphics2015@gmail.com</a></li>
          <li><svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 14.5 9 2.5 2.5 0 0 1 12 11.5z"/></svg><span>150, Tiranga Circle, Nagar Palika Market,<br>Opp. Nagrik Bank, Idar, Gujarat, India</span></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p>© <span data-year>2026</span> Timali Graphics. All Rights Reserved.</p>
      <ul>
        <li><a href="#" data-wa>WhatsApp</a></li>
        <li><a href="mailto:timaligraphics2015@gmail.com">Email</a></li>
        <li><a href="quote.html">Get a Quote</a></li>
      </ul>
    </div>
  </div>
</footer>
"""

TAIL = """
<div class="sticky-cta">
  <div class="sticky-cta__in">
    <a class="btn btn--dark" href="tel:+919687130009">
      <svg class="i" viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.25 1z"/></svg>
      Call Now
    </a>
    <a class="btn btn--wa" href="#" data-wa>
      <svg class="i" viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.5 14c-.2.6-1.2 1.2-1.7 1.2-.5.1-1 .2-3.2-.7-2.7-1.1-4.4-3.9-4.5-4.1-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .6l-.4.5-.3.3c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.1 1 2 1.3 2.3 1.4.3.1.5.1.7-.1l.9-1.1c.2-.2.4-.2.6-.1l2 1c.2.1.4.2.4.3.1.2.1.7-.1 1.3z"/></svg>
      WhatsApp
    </a>
  </div>
</div>

<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Portfolio image preview" aria-hidden="true">
  <button class="lb__close" type="button" aria-label="Close preview"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
  <button class="lb__nav lb__nav--prev" type="button" aria-label="Previous image"><svg viewBox="0 0 24 24"><path d="m14 6-6 6 6 6"/></svg></button>
  <button class="lb__nav lb__nav--next" type="button" aria-label="Next image"><svg viewBox="0 0 24 24"><path d="m10 6 6 6-6 6"/></svg></button>
  <div class="lb__box">
    <img alt="">
    <div class="lb__cap"><span><b data-lb-title></b><small data-lb-cat></small></span></div>
  </div>
</div>

<script src="assets/js/main.js"></script>
</body>
</html>
"""

CTA_BAND = """
<section class="sec sec--tight cta">
  <div class="wrap cta__in">
    <h2 class="reveal">Have a Printing Requirement?</h2>
    <p class="reveal">Share your requirement with us and let us help you with the right design and printing solution.</p>
    <div class="cta__actions reveal">
      <a class="btn btn--dark btn--lg" href="quote.html">Get a Quote</a>
      <a class="btn btn--outline btn--lg" href="#" data-wa>WhatsApp Us</a>
    </div>
  </div>
</section>
"""

CONTACT_MAP = """
<section class="sec bg-light" id="contact">
  <div class="wrap">
    <header class="sec__head reveal">
      <p class="eyebrow">Contact</p>
      <h2>Find Us in Idar</h2>
      <p>Visit the shop or call — we are open Monday to Saturday.</p>
    </header>
    <div class="contact__in">
      <div class="reveal">
        <div class="info-list">
          <div class="info-row">
            <span class="info-row__ic"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M4 21c0-4 3.6-6.6 8-6.6s8 2.6 8 6.6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>
            <span><small>Owner</small><b>Sovan Thakor (Golvadawala)</b></span>
          </div>
          <a class="info-row" href="tel:+919687130009">
            <span class="info-row__ic"><svg viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.25 1z"/></svg></span>
            <span><small>Phone</small><b>9687130009</b></span>
          </a>
          <a class="info-row" href="mailto:timaligraphics2015@gmail.com">
            <span class="info-row__ic"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3 7l9 6 9-6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></span>
            <span><small>Email</small><b>timaligraphics2015@gmail.com</b></span>
          </a>
          <a class="info-row" href="https://www.google.com/maps/search/?api=1&amp;query=Tiranga%20Circle%2C%20Nagar%20Palika%20Market%2C%20Idar%2C%20Gujarat" target="_blank" rel="noopener">
            <span class="info-row__ic"><svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 14.5 9 2.5 2.5 0 0 1 12 11.5z"/></svg></span>
            <span><small>Location</small><b>150, Tiranga Circle, Nagar Palika Market,<br>Opp. Nagrik Bank, Idar, Gujarat</b><em>Open in Google Maps →</em></span>
          </a>
        </div>
        <div class="contact__actions">
          <a class="btn btn--primary" href="tel:+919687130009">Call Now</a>
          <a class="btn btn--wa" href="#" data-wa>WhatsApp</a>
          <a class="btn btn--outline" href="mailto:timaligraphics2015@gmail.com">Send Email</a>
        </div>
      </div>
      <div class="map-card reveal">
        <iframe title="Timali Graphics location on Google Maps"
          src="https://www.google.com/maps?q=Tiranga%20Circle%2C%20Nagar%20Palika%20Market%2C%20Idar%2C%20Gujarat&amp;output=embed"
          loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        <div class="map-card__bar">
          <span><b>Find Us in Idar</b><small>Tiranga Circle, Nagar Palika Market</small></span>
          <a class="btn btn--dark btn--sm" target="_blank" rel="noopener"
             href="https://www.google.com/maps/dir/?api=1&amp;destination=Tiranga%20Circle%2C%20Nagar%20Palika%20Market%2C%20Idar%2C%20Gujarat">Get Directions</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- service data
SERVICES = [
    dict(slug="wedding-invitations", opt="Wedding Invitation", name="Wedding Invitations", img="wedding-invitations",
         short="Creative and elegant invitation designs for weddings and special occasions.",
         long="Wedding invitations are the first impression of your function. We design and print invitation cards in different sizes and finishes so the card matches the theme of your wedding.",
         points=["Premium, semi-premium and budget card options",
                 "Babri size and short tunkhoni size available",
                 "Photo invitations and theme-based designs",
                 "Bulk rates for large guest lists"],
         wa="Hello Timali Graphics, I am interested in Wedding Invitation printing."),
    dict(slug="visiting-cards", opt="Visiting Card", name="Visiting Cards", img="visiting-cards",
         short="Professional business and personal visiting card design and printing.",
         long="A visiting card is often the first print a customer sees. We design clean layouts with correct spacing, readable contact details and print them on quality card stock.",
         points=["Business and personal card designs",
                 "Multi-colour and premium card printing",
                 "Round corner and die-cut shapes available",
                 "Bulk discount for company requirements"],
         wa="Hello Timali Graphics, I am interested in Visiting Card printing."),
    dict(slug="bill-books", opt="Bill Book", name="Bill Books", img="bill-books",
         short="Custom printed bill books for businesses, shops and service counters.",
         long="Bill books keep your billing counter neat and professional. We print continuous, loose leaf and single-piece bill books with your shop name, address and GST details.",
         points=["Continuous and loose-leaf bill books",
                 "Duplicate, triplicate and triplicate-plus copies",
                 "Custom numbering and perforation",
                 "Printed to match your visiting card design"],
         wa="Hello Timali Graphics, I am interested in Bill Book printing."),
    dict(slug="letterheads", opt="Letterhead", name="Letterheads", img="letterheads",
         short="Professional branded letterhead printing for businesses and organizations.",
         long="A letterhead carries your company identity on official correspondence. We design it to match your logo, colours and services, and print it on smooth writing paper.",
         points=["A4 and legal size options",
                 "Matching compliment slips and envelopes",
                 "Logo placement and brand colour matching",
                 "Good paper quality for writing and printing"],
         wa="Hello Timali Graphics, I am interested in Letterhead printing."),
    dict(slug="photo-invitations", opt="Photo Invitation", name="Photo Invitations", img="photo-invitations",
         short="Customized invitations featuring photographs and creative layouts.",
         long="Photo invitations make your invite personal. Send us your photographs and we will retouch, arrange and print them into a finished invitation card.",
         points=["Photo retouching and correction",
                 "Custom layouts with your photographs",
                 "Print on card, flex or glossy paper",
                 "Matching thank-you and visiting cards"],
         wa="Hello Timali Graphics, I am interested in Photo Invitation printing."),
    dict(slug="stickers-labels", opt="Sticker", name="Stickers &amp; Labels", img="stickers-labels",
         short="Custom stickers and labels for products, promotions and events.",
         long="Labels and stickers are used on almost every product. We cut stickers in any shape and size, with strong adhesive and clean edges.",
         points=["Any shape and size available",
                 "Product labels, jar labels and bottle labels",
                 "Transparent, glossy and matte finishes",
                 "Bulk packing for packaging requirements"],
         wa="Hello Timali Graphics, I am interested in Sticker and Label printing."),
    dict(slug="menu-cards", opt="Menu Card", name="Menu Cards", img="menu-cards",
         short="Professional menu card design and printing for restaurants, cafés and hotels.",
         long="A well designed menu card makes a restaurant look organised. We handle the full layout, typography and printing for dine-in menus, takeaway menus and table tents.",
         points=["Dine-in, takeaway and table tent sizes",
                 "Food item photos included on request",
                 "Lamination and finishing options",
                 "Reprint when you add new dishes"],
         wa="Hello Timali Graphics, I am interested in Menu Card printing."),
    dict(slug="screen-printing", opt="Screen Printing", name="Screen Printing", img="screen-printing",
         short="Custom screen printing solutions for different business and promotional needs.",
         long="Screen printing is a cost-effective way to print on fabric and hard surfaces in larger runs. We help you pick the right product, colour and quantity.",
         points=["T-shirt, bag and cloth printing",
                 "Multi-colour screen printing",
                 "Bulk promotional and event requirements",
                 "Design support if you have no artwork"],
         wa="Hello Timali Graphics, I am interested in Screen Printing."),
    dict(slug="passport-photos", opt="Passport Photo", name="Passport Photos", img="passport-photos",
         short="Professional passport-size and ID photo printing with skin minting.",
         long="We print passport and ID size photos to the exact size required for the application, with clean background and skin minting so the print looks natural.",
         points=["All standard passport and ID sizes",
                 "Set of multiple prints as required",
                 "Skin minting for a natural finish",
                 "Same-day printing available"],
         wa="Hello Timali Graphics, I am interested in Passport Size photo printing."),
    dict(slug="certificates", opt="Certificate", name="Certificates", img="certificates",
         short="Clean and professional certificate design and printing.",
         long="Certificates and appreciation letters are printed for schools, colleges, offices and events. Send us the format and we will prepare the design and print it.",
         points=["School, college and government formats",
                 "Appreciation and participation certificates",
                 "Custom border, logo and signature layout",
                 "Good quality paper and printing"],
         wa="Hello Timali Graphics, I am interested in Certificate printing."),
    dict(slug="flex-banners", opt="Flex Banner", name="Flex Banners", img="flex-banners",
         short="High-impact banners for advertisements, events and promotions.",
         long="Flex banners are the most visible form of local advertising. We print high-quality flex for shops, events, painters, political and promotional work.",
         points=["Babri (large) and tunkhoni (short) sizes",
                 "Full-colour printing with sharp text",
                 "Eye-poles and mounting support available",
                 "Same-day printing for urgent requirements"],
         wa="Hello Timali Graphics, I am interested in Flex Banner printing."),
    dict(slug="book-covers", opt="Book Cover", name="Book Covers", img="book-covers",
         short="Creative book cover design and professional printing.",
         long="We design and print covers and pages for notebooks, diaries, registers and practice books used by schools and coaching classes.",
         points=["Notebook, diary and register covers",
                 "Soft cover and hard cover options",
                 "School and coaching class bulk orders",
                 "Complete book printing available"],
         wa="Hello Timali Graphics, I am interested in Book Cover printing."),
    dict(slug="catalogue-design", opt="Catalogue", name="Catalogue Design", img="catalogue-design",
         short="Organized and attractive catalogues for products and businesses.",
         long="A catalogue helps customers understand your product range. We design page layouts, place your product photographs and print the final catalogue.",
         points=["Product and price list catalogues",
                 "Page layout and typography design",
                 "Multi-page saddle-stitched or spiral binding",
                 "Reprint when your product range changes"],
         wa="Hello Timali Graphics, I am interested in Catalogue design."),
    dict(slug="appreciation-cards", opt="Appreciation Card", name="Appreciation Cards", img="appreciation-cards",
         short="Thank-you and appreciation cards for events and celebrations.",
         long="Appreciation cards are a simple way to say thank you to guests, customers or your team. Available in matching invitation themes.",
         points=["Matching invitation designs available",
                 "Short and tunkhoni sizes",
                 "Thank-you, gift and visit cards",
                 "Bulk rates for large functions"],
         wa="Hello Timali Graphics, I am interested in Appreciation Card printing."),
    dict(slug="custom-printing", opt="Custom Printing", name="Custom Printing", img="custom-printing",
         short="Any other printing requirement — stamps, envelopes, ID cards and more.",
         long="If your requirement is not listed here, send it to us anyway. We regularly handle customized printing that is not part of our standard service list.",
         points=["Rubber stamps and self-inking stamps",
                 "Envelopes, thank-you slips and ID cards",
                 "Custom shapes and sizes on request",
                 "Bulk printing for shops and offices"],
         wa="Hello Timali Graphics, I have a custom printing requirement."),
]

FILTERS = [("all", "All"), ("cards", "Business Cards"), ("invitation", "Wedding Invitations"),
           ("banner", "Banners"), ("stationery", "Business Printing"), ("sticker", "Stickers"),
           ("certificate", "Certificates"), ("other", "Other")]


def build_portfolio_items():
    rows = [
        ("01-visiting-card", "cards", "Business Cards", "Business Visiting Card", "Multi-colour card"),
        ("02-wedding-invitation", "invitation", "Wedding Invitations", "Wedding Invitation", "Premium flex invite"),
        ("03-flex-banner", "banner", "Banners", "Flex Banner", "Event &amp; promotion"),
        ("04-sticker", "sticker", "Stickers", "Sticker &amp; Label", "Product &amp; packaging"),
        ("05-menu-card", "stationery", "Business Printing", "Menu Card", "Restaurant &amp; café"),
        ("06-certificate", "certificate", "Certificates", "Certificate", "School &amp; corporate"),
        ("07-bill-book", "stationery", "Business Printing", "Bill Book", "Shop &amp; counter"),
        ("08-letterhead", "stationery", "Business Printing", "Letterhead", "Business stationery"),
        ("09-book-cover", "other", "Other", "Book Cover", "Notebook &amp; diary"),
        ("10-catalogue", "other", "Other", "Product Catalogue", "Multi-page design"),
        ("11-colour-banner", "banner", "Banners", "Colour Banner", "Advertisement"),
        ("12-passport-photo", "other", "Other", "Passport Size Photo", "ID &amp; stamp size"),
    ]
    zoom = '<span class="pf-item__zoom"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5M11 8v6M8 11h6"/></svg></span>'
    out = []
    for i, (f, cat, catlabel, title, sub) in enumerate(rows):
        path = f"assets/img/portfolio/{f}.webp"
        out.append(f"""      <button class="pf-item reveal" data-cat="{cat}" data-cat-label="{catlabel}"
              data-title="{title}" data-full="{path}">
        {zoom}
        <img src="{path}" alt="{title} designed and printed by Timali Graphics, Idar" loading="lazy" width="800" height="600">
        <span class="pf-item__body"><b>{title}</b><small>{sub}</small></span>
      </button>""")
    return "\n".join(out)


def filter_buttons():
    return "\n".join(
        f'      <button class="filter{" active" if k == "all" else ""}" data-filter="{k}" '
        f'aria-pressed="{"true" if k == "all" else "false"}">{label}</button>'
        for k, label in FILTERS)


def service_blocks():
    out = []
    for s in SERVICES:
        points = "\n".join(f"          <li>{p}</li>" for p in s["points"])
        out.append(f"""    <article class="detail reveal" id="{s['slug']}">
      <div class="detail__body">
        <h2>{s['name']}</h2>
        <p>{s['long']}</p>
        <ul class="detail__list">
{points}
        </ul>
        <div style="display:flex;flex-wrap:wrap;gap:12px">
          <a class="btn btn--primary" href="quote.html?service={urlquote(s['opt'])}">Get a Quote</a>
          <a class="btn btn--wa" href="#" data-wa="{s['wa']}">WhatsApp</a>
        </div>
      </div>
      <div class="detail__fig">
        <img src="assets/img/services/{s['img']}.svg" alt="{s['name']} by Timali Graphics" loading="lazy" width="800" height="600">
      </div>
    </article>""")
    return "\n".join(out)


# ---------------------------------------------------------------- pages
def page_about():
    b = head("About Timali Graphics | Printing &amp; Design Studio in Idar",
             "Learn about Timali Graphics, a graphic design and printing service in Idar, Gujarat offering business stationery, invitations, banners, stickers and certificates.", "about")
    b += HEADER
    b += PHEAD.format(crumb="About", h1="About Timali Graphics",
                      lead="A graphic design and printing service in Idar, Gujarat — design, printing and customized requirements handled in one place.")
    b += """
<section class="sec">
  <div class="wrap about__in">
    <div class="about__copy reveal">
      <p class="eyebrow">Who we are</p>
      <h2>Professional design and printing, close to home</h2>
      <p>
        <strong>Timali Graphics</strong> is a graphic design and printing service based in Idar, Gujarat.
        We provide creative design and printing solutions for individuals, businesses, events and organizations.
        From visiting cards and business stationery to invitations, banners, stickers, certificates and customized
        printing requirements, we focus on delivering professional designs and quality print results.
      </p>
      <p>
        Our shop is located at <strong>150, Tiranga Circle, Nagar Palika Market, opposite Nagrik Bank, Idar.</strong>
        Many of our customers come from Idar and the nearby towns of Kankrej, Dehgam, Dholakuva, Rampura and beyond,
        and many of our orders are simply shared over the phone or on WhatsApp.
      </p>
      <p>
        You do not need to know printing terms. Tell us the purpose of the work — a wedding invitation, a shop
        banner, passport photos, a bill book — and we will suggest the right size, material and quantity, then
        give you the rate before starting.
      </p>
      <ul class="ticks">
        <li>Design and printing handled at the same place</li>
        <li>Transparent rate shared before the job starts</li>
        <li>Design approved by you before printing</li>
        <li>Bulk quantity discount on larger orders</li>
      </ul>
      <a class="link-arrow" href="quote.html">Request a quote
        <svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
    </div>

    <div class="figure reveal">
      <span class="figure__note">Shop &amp; Workspace</span>
      <img src="assets/img/shop.webp" alt="Timali Graphics shop at 150, Tiranga Circle, Nagar Palika Market, Idar" loading="lazy" width="1200" height="900">
      <div class="figure__cap">
        <b>Timali Graphics, Idar</b>
        <small>150, Tiranga Circle, Nagar Palika Market</small>
      </div>
    </div>
  </div>
</section>

<section class="sec bg-navy">
  <div class="wrap">
    <header class="sec__head reveal">
      <p class="eyebrow">How we work</p>
      <h2>Our Approach</h2>
      <p>Simple, clear and based on what you actually need printed.</p>
    </header>
    <div class="why__grid">
      <div class="why__item reveal"><span class="why__n">01</span><div><h3>Listen first</h3><p>We start by understanding the purpose, quantity and budget of your requirement.</p></div></div>
      <div class="why__item reveal"><span class="why__n">02</span><div><h3>Suggest the right option</h3><p>We recommend size, material and finishing that works for your purpose and budget.</p></div></div>
      <div class="why__item reveal"><span class="why__n">03</span><div><h3>Design for approval</h3><p>The design is shared with you and printed only after you confirm it.</p></div></div>
      <div class="why__item reveal"><span class="why__n">04</span><div><h3>Print and deliver</h3><p>The job is printed, checked and handed over at the shop or delivered as agreed.</p></div></div>
    </div>
  </div>
</section>
"""
    b += CTA_BAND + CONTACT_MAP + FOOTER + TAIL
    return b


def page_services():
    b = head("Services | Timali Graphics — Printing &amp; Design in Idar",
             "Wedding invitations, visiting cards, bill books, letterheads, stickers, menu cards, screen printing, passport photos, certificates, flex banners, book covers and catalogue design in Idar, Gujarat.", "services")
    b += HEADER
    b += PHEAD.format(crumb="Services", h1="Our Services",
                      lead="Complete graphic design and printing solutions for personal, business and event requirements.")
    b += """
<section class="sec--tight" style="background:var(--bg)">
  <div class="wrap">
    <div class="filters reveal" style="margin-bottom:0" role="group" aria-label="Jump to service">
      <a class="filter" href="#wedding-invitations">Wedding Invitations</a>
      <a class="filter" href="#visiting-cards">Visiting Cards</a>
      <a class="filter" href="#bill-books">Bill Books</a>
      <a class="filter" href="#letterheads">Letterheads</a>
      <a class="filter" href="#stickers-labels">Stickers &amp; Labels</a>
      <a class="filter" href="#menu-cards">Menu Cards</a>
      <a class="filter" href="#passport-photos">Passport Photos</a>
      <a class="filter" href="#certificates">Certificates</a>
      <a class="filter" href="#flex-banners">Flex Banners</a>
      <a class="filter" href="#catalogue-design">Catalogue Design</a>
      <a class="filter" href="#custom-printing">Custom Printing</a>
    </div>
  </div>
</section>

<section class="sec--tight">
  <div class="wrap">
"""
    b += service_blocks() + "\n  </div>\n</section>\n"
    b += CTA_BAND + FOOTER + TAIL
    return b


def page_solutions():
    groups = [
        ("For Events &amp; Weddings", "wedding-invitations", "Events &amp; Weddings",
         "Invitation cards, flex invitations, photo invitations, welcome boards, thank-you cards, standees and banners. Share the theme, the number of guests and the date — we will suggest the card size and quantity."),
        ("For Shops &amp; Businesses", "visiting-cards", "Shops &amp; Businesses",
         "Visiting cards, letterheads, bill books, envelopes, compliment slips, ID cards, stamps, menu cards, catalogues, carry bags and flex banners. Send your logo or business card and we will match the design."),
        ("For Photos &amp; Documents", "passport-photos", "Photos &amp; Documents",
         "Passport size photos, stamp size photos, Mo Mohan style photos, school and college certificates, appreciation letters and ID photo printing with skin minting."),
        ("For Bulk &amp; Promotional", "flex-banners", "Bulk &amp; Promotional",
         "Flex banners, colour banners, screen printed cloth and bags, stickers, labels, packaging inserts and bulk promotional printing. Higher quantity requirements get a better rate."),
        ("For Products &amp; Packaging", "stickers-labels", "Products &amp; Packaging",
         "Product stickers, jar and bottle labels, thank-you cards, catalogue design, book covers, notebooks, registers and complete custom printing requirements."),
    ]
    blocks = []
    for i, (title, anchor, tag, body) in enumerate(groups):
        blocks.append(f"""    <article class="detail reveal" id="{anchor}">
      <div class="detail__body">
        <p class="eyebrow">{tag}</p>
        <h2>{title}</h2>
        <p>{body}</p>
        <div style="display:flex;flex-wrap:wrap;gap:12px">
          <a class="btn btn--primary" href="quote.html">Get a Quote</a>
          <a class="btn btn--outline" href="services.html">See all services</a>
        </div>
      </div>
      <div class="detail__fig">
        <img src="assets/img/services/{anchor}.svg" alt="{title} printing by Timali Graphics" loading="lazy" width="800" height="600">
      </div>
    </article>""")

    b = head("Printing Solutions | Timali Graphics — Idar",
             "Printing solutions by requirement — events and weddings, shops and businesses, photos and documents, bulk and promotional, products and packaging. Graphic design and printing in Idar, Gujarat.", "solutions")
    b += HEADER
    b += PHEAD.format(crumb="Printing Solutions", h1="Printing Solutions",
                      lead="Different requirements need different printing. Pick the category closest to your need and we will guide you on size, material and quantity.")
    b += """
<section class="sec--tight">
  <div class="wrap">
"""
    b += "\n".join(blocks) + "\n  </div>\n</section>\n"

    b += """
<section class="sec bg-light">
  <div class="wrap">
    <header class="sec__head reveal">
      <p class="eyebrow">Need help choosing?</p>
      <h2>Just tell us the purpose</h2>
      <p>You do not need to know the printing terms. Share what the work is for, how many copies you need and when you need it — we will suggest the right option and rate.</p>
    </header>
    <div class="services__grid">
      <article class="svc reveal">
        <span class="svc__ic"><svg viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.25 1z"/></svg></span>
        <h3>Call the shop</h3>
        <p>Speak to us directly on 9687130009 and explain your requirement in your own words.</p>
        <a class="svc__more" href="tel:+919687130009">Call Now <svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
      </article>
      <article class="svc reveal">
        <span class="svc__ic"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.5 14c-.2.6-1.2 1.2-1.7 1.2-.5.1-1 .2-3.2-.7-2.7-1.1-4.4-3.9-4.5-4.1-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .6l-.4.5-.3.3c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.1 1 2 1.3 2.3 1.4.3.1.5.1.7-.1l.9-1.1c.2-.2.4-.2.6-.1l2 1c.2.1.4.2.4.3.1.2.1.7-.1 1.3z"/></svg></span>
        <h3>Send on WhatsApp</h3>
        <p>Share a photo of your reference or requirement — it is the fastest way to get an answer.</p>
        <a class="svc__more" href="#" data-wa>WhatsApp Us <svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
      </article>
      <article class="svc reveal">
        <span class="svc__ic"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M9 13h6M9 17h4" fill="none" stroke="#FBBA00" stroke-width="2" stroke-linecap="round"/></svg></span>
        <h3>Request a quote</h3>
        <p>Fill the quote form with your details and we will reply with a rate for your requirement.</p>
        <a class="svc__more" href="quote.html">Get a Quote <svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
      </article>
    </div>
  </div>
</section>
"""
    b += CTA_BAND + CONTACT_MAP + FOOTER + TAIL
    return b


def page_portfolio():
    b = head("Portfolio | Timali Graphics — Our Recent Work in Idar",
             "A selection of graphic design and printing work by Timali Graphics, Idar — visiting cards, wedding invitations, banners, stickers, certificates, catalogues and more.", "portfolio")
    b += HEADER
    b += PHEAD.format(crumb="Portfolio", h1="Our Recent Work",
                      lead="A selection of our creative design and printing work — click any image to view it larger.")
    b += """
<section class="sec--tight">
  <div class="wrap">
    <div class="filters reveal" data-filters role="group" aria-label="Filter portfolio by category">
"""
    b += filter_buttons() + """
    </div>

    <div class="pf-grid">
"""
    b += build_portfolio_items() + """
    </div>
    <p class="pf-empty" data-pf-empty>No work in this category yet.</p>
  </div>
</section>

"""
    b += CTA_BAND + CONTACT_MAP + FOOTER + TAIL
    return b


def page_quote():
    b = head("Request a Quote | Timali Graphics — Idar",
             "Request a printing quote from Timali Graphics, Idar. Share your service, quantity and required date and we will reply with a rate for visiting cards, invitations, banners, stickers and more.", "quote")
    b += HEADER
    b += PHEAD.format(crumb="Get a Quote", h1="Request a Quote",
                      lead="Fill in your requirement and we will get back to you with a rate. The faster option is to call or WhatsApp us directly.")
    b += """
<section class="sec">
  <div class="wrap" style="max-width:900px">
    <div class="form-card reveal">
      <h2>Tell us what you need printed</h2>
      <p class="form-card__lead">Fields marked with <span style="color:#D14343">*</span> are required. If you have a reference image or design file, attach it here and also send it on WhatsApp for a faster reply.</p>

      <form id="quoteForm" novalidate>
        <div class="form-grid">
          <div class="field">
            <label for="q-name">Full Name <span class="req">*</span></label>
            <input id="q-name" type="text" name="name" autocomplete="name" placeholder="Enter your name" required>
            <p class="err-msg">Please enter your name.</p>
          </div>

          <div class="field">
            <label for="q-phone">Phone Number <span class="req">*</span></label>
            <input id="q-phone" type="tel" name="phone" inputmode="numeric" autocomplete="tel" placeholder="10-digit mobile number" required>
            <p class="err-msg">Please enter a 10-digit mobile number.</p>
          </div>

          <div class="field">
            <label for="q-email">Email Address</label>
            <input id="q-email" type="email" name="email" autocomplete="email" placeholder="you@example.com">
            <p class="err-msg">Please enter a valid email address.</p>
          </div>

          <div class="field">
            <label for="q-service">Service Required <span class="req">*</span></label>
            <select id="q-service" name="service" required>
              <option value="">— Select a service —</option>
              <option>Visiting Card</option>
              <option>Wedding Invitation</option>
              <option>Bill Book</option>
              <option>Letterhead</option>
              <option>Photo Invitation</option>
              <option>Sticker</option>
              <option>Menu Card</option>
              <option>Certificate</option>
              <option>Book Cover</option>
              <option>Catalogue</option>
              <option>Screen Printing</option>
              <option>Flex Banner</option>
              <option>Passport Photo</option>
              <option>Appreciation Card</option>
              <option>Custom Printing</option>
            </select>
            <p class="err-msg">Please select a service.</p>
          </div>

          <div class="field">
            <label for="q-qty">Quantity</label>
            <input id="q-qty" type="text" name="qty" inputmode="numeric" placeholder="e.g. 200 copies / 2 pieces">
            <p class="field__hint">Approximate quantity is fine.</p>
          </div>

          <div class="field">
            <label for="q-date">Required Date</label>
            <input id="q-date" type="date" name="date">
            <p class="field__hint">Tell us if it is urgent.</p>
          </div>

          <div class="field field--full">
            <label for="q-details">Describe Your Requirement</label>
            <textarea id="q-details" name="details" rows="5" placeholder="e.g. Need 200 wedding invitation cards, 4x6 size, maroon and gold theme, needed by next Saturday. Please share the rate for 100 and 200 pieces."></textarea>
          </div>

          <div class="field field--full">
            <label for="q-file">Upload Reference / Design</label>
            <input id="q-file" type="file" name="file" accept="image/*,.pdf,.ai,.cdr,.psd">
            <p class="field__hint">Optional. Also send the file on WhatsApp so we receive it properly.</p>
          </div>
        </div>

        <div class="form__foot">
          <button class="btn btn--primary btn--lg" type="submit">
            <svg class="i" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M9 13h6M9 17h4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            Request a Quote
          </button>
          <p class="form__note">Prefer to talk? Call <a href="tel:+919687130009" style="color:var(--yellow-600);font-weight:600">9687130009</a> or message us on WhatsApp.</p>
        </div>

        <p class="form__msg" id="formMsg" role="status"></p>
      </form>

      <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px;padding-top:22px;border-top:1px solid var(--line)">
        <a class="btn btn--wa" id="formWhatsApp" href="#" data-wa hidden>Send this enquiry on WhatsApp instead</a>
        <a class="btn btn--outline" href="tel:+919687130009">Call Now</a>
      </div>
    </div>
  </div>
</section>
"""
    b += CONTACT_MAP + FOOTER + TAIL
    return b


def page_contact():
    b = head("Contact | Timali Graphics — Printing Studio in Idar, Gujarat",
             "Contact Timali Graphics — call 9687130009, WhatsApp, email timaligraphics2015@gmail.com or visit 150, Tiranga Circle, Nagar Palika Market, Opp. Nagrik Bank, Idar, Gujarat.", "contact")
    b += HEADER
    b += PHEAD.format(crumb="Contact", h1="Let's Work Together",
                      lead="Call us, send a WhatsApp message, email us, or visit the shop at Tiranga Circle in Idar.")
    b += CONTACT_MAP
    b += """
<section class="sec--tight">
  <div class="wrap">
    <header class="sec__head reveal">
      <p class="eyebrow">Good to know</p>
      <h2>Before you send the requirement</h2>
      <p>A few details help us quote accurately and finish the work faster.</p>
    </header>
    <div class="services__grid">
      <article class="svc reveal">
        <span class="svc__ic"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M3 7l9 6 9-6" fill="none" stroke="currentColor" stroke-width="1.7"/></svg></span>
        <h3>Size</h3>
        <p>Visiting card, A4, 4×6 invitation, 2×3 or 3×2 flex — or just tell us where it will be used.</p>
      </article>
      <article class="svc reveal">
        <span class="svc__ic"><svg viewBox="0 0 24 24"><path d="M6 3h12v18H6z" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M9 7h6M9 11h6M9 15h4" stroke="#FBBA00" stroke-width="1.8" stroke-linecap="round"/></svg></span>
        <h3>Quantity</h3>
        <p>How many copies you need. Larger quantity usually gets a better per-piece rate.</p>
      </article>
      <article class="svc reveal">
        <span class="svc__ic"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M12 7v5l3.5 2" fill="none" stroke="#FBBA00" stroke-width="1.9" stroke-linecap="round"/></svg></span>
        <h3>Required date</h3>
        <p>When you need the work. Urgent requirements are possible but need early confirmation.</p>
      </article>
      <article class="svc reveal">
        <span class="svc__ic"><svg viewBox="0 0 24 24"><path d="M3 16.5V7a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v9.5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M3 12h18" stroke="#FBBA00" stroke-width="1.8"/><path d="M7 9h4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></span>
        <h3>Reference</h3>
        <p>A photo of something you liked, or your existing card, so we can match the style.</p>
      </article>
    </div>
  </div>
</section>
"""
    b += CTA_BAND + FOOTER + TAIL
    return b


PAGES = {
    "about.html": page_about,
    "services.html": page_services,
    "solutions.html": page_solutions,
    "portfolio.html": page_portfolio,
    "quote.html": page_quote,
    "contact.html": page_contact,
}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(fn())
        print("wrote", name)
