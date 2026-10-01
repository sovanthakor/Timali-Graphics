/* =============================================================
   TIMALI GRAPHICS — site behaviour
   ============================================================= */
(function () {
  'use strict';

  /* ---------------- Business config (edit here) ---------------- */
  var TG = {
    phone: '9687130009',
    tel: '+919687130009',
    email: 'timaligraphics2015@gmail.com',
    whatsapp: '919687130009',
    defaultMsg: 'Hello Timali Graphics, I would like to enquire about your printing services.'
  };
  window.TG = TG;

  var waLink = function (msg) {
    return 'https://wa.me/' + TG.whatsapp + '?text=' + encodeURIComponent(msg || TG.defaultMsg);
  };

  /* ---------------- 1. Sticky header state ---------------- */
  var header = document.querySelector('.header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-stuck', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------------- 2. Mobile navigation ---------------- */
  var burger = document.getElementById('burger');
  var nav = document.getElementById('nav');
  if (burger && nav) {
    var closeMenu = function () {
      nav.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
    window.addEventListener('resize', function () { if (window.innerWidth > 880) closeMenu(); });
  }

  /* ---------------- 3. Scroll reveal (subtle) ---------------- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        setTimeout(function () { el.classList.add('in'); }, parseInt(el.dataset.delay || '0', 10));
        io.unobserve(el);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    revealEls.forEach(function (el, i) { el.dataset.delay = String((i % 4) * 70); io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }
  /* safety net — content must never stay hidden */
  window.setTimeout(function () {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }, 2200);

  /* ---------------- 4. WhatsApp links (pre-filled message) ---------------- */
  document.querySelectorAll('[data-wa]').forEach(function (a) {
    a.href = waLink(a.dataset.wa || undefined);
    a.target = '_blank';
    a.rel = 'noopener';
  });

  /* ---------------- 5. Current year ---------------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------------- 6. Portfolio filter + lightbox ---------------- */
  var filterWrap = document.querySelector('[data-filters]');
  if (filterWrap) {
    var items = Array.prototype.slice.call(document.querySelectorAll('.pf-item'));
    var empty = document.querySelector('[data-pf-empty]');
    var buttons = filterWrap.querySelectorAll('.filter');

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) {
          b.classList.remove('active');
          b.setAttribute('aria-pressed', 'false');
        });
        btn.classList.add('active');
        btn.setAttribute('aria-pressed', 'true');

        var cat = btn.dataset.filter;
        var shown = 0;
        items.forEach(function (item) {
          var match = cat === 'all' || item.dataset.cat === cat;
          item.classList.toggle('is-hidden', !match);
          if (match) shown++;
        });
        if (empty) empty.style.display = shown ? 'none' : 'block';
      });
    });
  }

  var lb = document.getElementById('lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img');
    var lbTitle = lb.querySelector('[data-lb-title]');
    var lbCat = lb.querySelector('[data-lb-cat]');
    var lbIndex = 0;
    var lbItems = [];

    /* only collect items that are currently visible */
    var collect = function () {
      lbItems = Array.prototype.slice.call(document.querySelectorAll('.pf-item'))
        .filter(function (i) { return !i.classList.contains('is-hidden'); });
    };

    var show = function (i) {
      if (!lbItems.length) return;
      lbIndex = (i + lbItems.length) % lbItems.length;
      var it = lbItems[lbIndex];
      lbImg.src = it.dataset.full || it.querySelector('img').src;
      lbImg.alt = it.dataset.title || '';
      lbTitle.textContent = it.dataset.title || '';
      lbCat.textContent = it.dataset.catLabel || '';
    };

    var openLb = function (i) {
      collect();
      show(i);
      lb.classList.add('open');
      lb.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.lb__close').focus();
    };

    var closeLb = function () {
      lb.classList.remove('open');
      lb.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    };

    document.querySelectorAll('.pf-item').forEach(function (item) {
      item.addEventListener('click', function () {
        collect();
        show(lbItems.indexOf(item));
        lb.classList.add('open');
        lb.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      });
    });

    var on = function (sel, fn) {
      var el = lb.querySelector(sel);
      if (el) el.addEventListener('click', fn);
    };
    on('.lb__close', closeLb);
    on('.lb__prev, .lb__nav--prev', function () { show(lbIndex - 1); });
    on('.lb__next, .lb__nav--next', function () { show(lbIndex + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') closeLb();
      if (e.key === 'ArrowLeft') show(lbIndex - 1);
      if (e.key === 'ArrowRight') show(lbIndex + 1);
    });
  }

  /* ---------------- 7. Generic enquiry / quote form ---------------- */
  var form = document.getElementById('quoteForm') || document.getElementById('enquiryForm');
  if (form) {
    var msg = document.getElementById('formMsg');
    var get = function (n) { return form.querySelector('[name="' + n + '"]'); };
    var wrap = function (el) { return el ? el.closest('.field') || el.parentElement : null; };

    var setErr = function (el, on) {
      var w = wrap(el);
      if (w) w.classList.toggle('is-error', on);
    };

    /* clear error as soon as user types */
    form.querySelectorAll('input,select,textarea').forEach(function (el) {
      el.addEventListener('input', function () { setErr(el, false); });
      el.addEventListener('change', function () { setErr(el, false); });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var name = get('name'), phone = get('phone'), email = get('email'),
          service = get('service'), qty = get('qty'), date = get('date'),
          details = get('details'), file = get('file');

      var bad = false;
      /* clear every previous error first, then re-flag only the failing fields */
      form.querySelectorAll('.field').forEach(function (f) { f.classList.remove('is-error'); });
      if (name && name.value.trim().length < 2) { setErr(name, true); bad = true; }
      if (phone && phone.value.replace(/\D/g, '').length < 10) { setErr(phone, true); bad = true; }
      if (email && email.value.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim())) { setErr(email, true); bad = true; }
      if (service && !service.value) { setErr(service, true); bad = true; }

      if (bad) {
        if (msg) { msg.className = 'form__msg bad'; msg.textContent = 'Please complete the highlighted fields. A 10-digit mobile number is required.'; }
        var firstErr = form.querySelector('.field.is-error input, .field.is-error select, .field.is-error textarea');
        if (firstErr) firstErr.focus();
        return;
      }

      var lines = [
        'New enquiry from timaligraphics.com',
        '',
        'Name: ' + (name ? name.value.trim() : ''),
        'Phone: ' + (phone ? phone.value.trim() : '')
      ];
      if (email) lines.push('Email: ' + (email.value.trim() || '-'));
      if (service) lines.push('Service: ' + service.value);
      if (qty) lines.push('Quantity: ' + (qty.value.trim() || '-'));
      if (date) lines.push('Required by: ' + (date.value || '-'));
      if (details) lines.push('Requirement: ' + (details.value.trim() || '-'));
      if (file && file.files && file.files[0]) {
        lines.push('Reference file: ' + file.files[0].name + ' (please ask the customer to attach it on WhatsApp)');
      }
      lines.push('', 'Please reply with a quotation. Thank you.');

      if (msg) {
        msg.className = 'form__msg ok';
        msg.textContent = 'Thank you! Your enquiry is ready. If your mail app did not open, please WhatsApp us on ' + TG.phone + ' or email ' + TG.email + ' directly.';
      }

      /* No server available — open the visitor's mail app AND offer WhatsApp */
      window.location.href = 'mailto:' + TG.email +
        '?subject=' + encodeURIComponent('Quote request — ' + (service ? service.value : 'Printing')) +
        '&body=' + encodeURIComponent(lines.join('\n'));

      var waBtn = document.getElementById('formWhatsApp');
      if (waBtn) {
        waBtn.hidden = false;
        waBtn.href = waLink('Hello Timali Graphics, I would like a quote for ' +
          (service ? service.value : 'printing work') +
          '. My name is ' + (name ? name.value.trim() : '') +
          ' and my number is ' + (phone ? phone.value.trim() : '') + '.');
      }
    });
  }

  /* ---------------- 8. Pre-fill service from URL (?service=) ---------------- */
  var params = new URLSearchParams(window.location.search);
  var svc = params.get('service');
  if (svc) {
    var sel = document.querySelector('[name="service"]');
    if (sel) {
      Array.prototype.forEach.call(sel.options, function (o) {
        if (o.value.toLowerCase() === svc.toLowerCase()) sel.value = o.value;
      });
    }
  }

  /* ---------------- 9. Min date = today (quote date field) ---------------- */
  var dateField = document.querySelector('[name="date"]');
  if (dateField) dateField.min = new Date().toISOString().split('T')[0];

  /* ---------------- 10. Active nav link ---------------- */
  var here = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav a[href]').forEach(function (a) {
    var h = (a.getAttribute('href') || '').split('#')[0].split('/').pop().toLowerCase();
    if (h && h === here) a.setAttribute('aria-current', 'page');
  });
})();
