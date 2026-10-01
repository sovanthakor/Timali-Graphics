# Timali Graphics — Website

**Graphic Design & Printing Services, Idar, Gujarat**

Static multi-page website. No build step, no server, no monthly cost — koi bhi free
static host par upload kar do (Netlify, Vercel, GitHub Pages, Hostinger, cPanel).

---

## 1. Pages

| File | Purpose |
|---|---|
| `index.html` | Home — hero, trust, services, why choose us, portfolio, how it works, about, CTA, contact + map |
| `about.html` | About the business |
| `services.html` | All 15 services with detail, bullet points and sample image |
| `solutions.html` | Printing solutions grouped by **requirement** (events, shops, documents, bulk, packaging) |
| `portfolio.html` | Filterable portfolio gallery with lightbox |
| `quote.html` | Request a Quote form (opens mail + WhatsApp fallback) |
| `contact.html` | Contact details, timings, Google Map and directions |

---

## 2. Brand system

| Token | Value | Use |
|---|---|---|
| Navy | `#272238` | Dark sections, headings, buttons, icons |
| Yellow | `#FBBA00` | Primary CTA, accents, hover |
| White | `#FFFFFF` | Content sections |
| Light | `#F7F7F7` | Alternating section background |

* Heading font: **Poppins** 600/700
* Body font: **Inter** 400/500/600
* Button radius: 8–12px (not pill)

All colours are CSS variables at the top of `assets/css/style.css` — ek jagah change
karo, poora site update ho jayega.

---

## 3. Business details (kahan badalna hai)

Sabse aasan tarika: `assets/js/main.js` ke top me `TG` object badal do.

```js
var TG = {
  phone: '9687130009',
  tel: '+919687130009',
  email: 'timaligraphics2015@gmail.com',
  whatsapp: '919687130009',
  defaultMsg: 'Hello Timali Graphics, I would like to enquire about your printing services.'
};
```

Address har page ke footer/contact section me likha hai. Saare pages ek saath
update karne ke liye:

```powershell
python tools\build_pages.py
```

(`about`, `services`, `solutions`, `portfolio`, `quote`, `contact` — ye builder se
bante hain, isliye `build_pages.py` me badalna kaafi hai. `index.html` alag se
edit karna hoga.)

### Address (current)

```
150, Tiranga Circle, Nagar Palika Market,
Opposite Nagrik Bank, Idar, Gujarat
```

**Owner:** Sovan Thakor (Golvadawala) — sirf contact section me dikhta hai.

---

## 4. Real photos kaise add karein

> ✅ **Portfolio ke 12 asli photos already lagaye hue hain** (`assets/img/portfolio/*.webp`,
> 800×800). Neeche sirf nayi photo add karne ya replace karne ka tareeqa hai.

### a) Portfolio photos (12 tiles)

Folder: `assets/img/portfolio/`

```
01-visiting-card.webp      05-menu-card.webp        09-book-cover.webp
02-wedding-invitation.webp 06-certificate.webp      10-catalogue.webp
03-flex-banner.webp        07-bill-book.webp        11-colour-banner.webp
04-sticker.webp            08-letterhead.webp       12-passport-photo.webp
```

**Size: 800 × 800 px (1:1 square)** — grid ka `aspect-ratio: 1/1` isi hisaab se hai.

Nayi photo add / replace karna ho to:

1. Photo ko `800 × 800 px` me save karo
2. Webp format me convert karo (agar JPG hai to —
   <https://squoosh.app> ya `cwebp` use karo)
3. Naam wahi rakho aur folder me daal do
4. HTML me `src` aur `data-full` dono update karo

```html
<!-- pehle -->
<img src="assets/img/portfolio/01-visiting-card.webp" ...>
<!-- nayi photo ke liye -->
<img src="assets/img/portfolio/01-visiting-card.webp" ...>
```

`portfolio.html` aur `index.html` dono me references hain — `build_pages.py`
chalane se `portfolio.html` apne aap update ho jayega.

### b) Shop / workspace photo

`assets/img/shop-placeholder.svg` ko apni shop ki photo se replace karo:

```
assets/img/shop.jpg
```

Phir `index.html`, `about.html` me `shop-placeholder.svg` ko `shop.jpg` se badal do.
Size: **800 × 600 px** (portrait chhootu photo bhi chalegi, `object-fit:cover` se
theek ho jayegi).

### c) Service sample photos (services + solutions page)

⚠️ **Ye abhi bhi placeholder hain** (`.svg`). Abhi sirf portfolio me asli photos hain.

Folder: `assets/img/services/` — 15 files, har service ka ek sample.

Size **800 × 600 px**. Naam wahi rakho (`visiting-cards.jpg` etc.), `build_pages.py`
me `{{s['img']}}.svg` ko `{{s['img']}}.webp` ya `.jpg` se badal do, phir builder
chala do — dono pages apne aap update ho jayenge.

---

## 5. Quote form kaise kaam karta hai

Abhi koi server/backend nahi hai, isliye form:

1. Validation karta hai (naam, 10-digit mobile, service)
2. Visitor ke mail app me pre-filled email kholta hai
3. Ek **"Send this enquiry on WhatsApp instead"** button dikhata hai jisme saara
   enquiry WhatsApp message me bhara hota hai

Free email receiving ke liye do options:

* **Formspree / Web3Forms** — free, 2 minute setup. `main.js` me
  `window.location.href = 'mailto:...'` wali line ko unke endpoint se replace karo.
* **Google Form** — enquiry Google Sheet me aati rahegi (mobile par sabse aasan).

WhatsApp par sirf enquiry aati hai — koi bhi visitor ka number save nahi hota.
Apna number chahiye to **WhatsApp Business** use karo (free, catalogue + quick replies).

---

## 6. Google Map

Har page me iframe embed hai:

```
https://www.google.com/maps?q=Tiranga%20Circle%2C%20Nagar%20Palika%20Market%2C%20Idar%2C%20Gujarat&output=embed
```

Exact shop location pin karna ho to:

1. Google Maps me apni shop ka link copy karo (share → copy link)
2. Upar wala `q=` ko us link se replace karo
3. `build_pages.py` chala do

---

## 7. SEO

Har page ka `<title>`, meta description, keywords, Open Graph tags aur canonical
already set hain. Kuch cheezein aapko khud bharni hain:

* `https://www.timaligraphics.com/` — har page ke `<link rel="canonical">` me jagah
  hai (abhi example.com hai). Apne domain se badal do.
* Google Search Console me `sitemap.xml` submit karo (niche diya hai)
* `robots.txt` me apna domain daal do

Naye service pages banane hain (jaise `/services/visiting-cards`) to `services.html`
copy karke ek naya file bana lo — structure wahi rahega.

---

## 8. Local me test kaise karein

`file://` se Chrome me kuch cheezein (map, WhatsApp deep-link) block hoti hain,
isliye local server use karo:

```powershell
cd "D:\My Website"
python -m http.server 8791
```

Phir browser me kholo: <http://127.0.0.1:8791/>

---

## 9. Files

```
D:\My Website\
├── index.html            Home
├── about.html            About
├── services.html         All services
├── solutions.html        Printing solutions by requirement
├── portfolio.html        Portfolio gallery
├── quote.html            Request a quote
├── contact.html          Contact + map
├── robots.txt
├── sitemap.xml
├── assets\
│   ├── css\style.css     Poora design system
│   ├── js\main.js        Nav, reveal, filter, lightbox, form
│   ├── img\
│   │   ├── logo.svg              TG logo (navey + yellow)
│   │   ├── shop-placeholder.svg  Shop photo ki jagah
│   │   ├── portfolio\            12 asli photos (.webp, 800x800)
│   │   └── services\             15 placeholder samples (.svg)
└── tools\
    ├── build_pages.py            Baaki pages ek saath banata hai
    ├── make_placeholders.py      Portfolio placeholders (ab zarurat nahi)
    ├── make_service_placeholders.py
    └── webp_size.py              WebP dimensions check karta hai
```

---

## 10. Checklist — launch se pehle

- [x] Asli portfolio photos `assets/img/portfolio/` me daali (12 `.webp`)
- [ ] Shop photo `assets/img/shop.jpg` ki tarah rakhi
- [ ] Service sample photos `assets/img/services/` me daali
- [ ] `build_pages.py` dobara chalaya (saare pages update)
- [ ] Apne domain se canonical URLs badle
- [ ] Phone number / email verify kiya hai
- [ ] Mobile par Call aur WhatsApp buttons test kiye
- [ ] Quote form test kiya
- [ ] Website live host par upload ki
