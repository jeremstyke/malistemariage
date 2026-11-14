/* Comptes (Supabase Auth : lien de connexion par e-mail, même compte que Ma liste bébé) et sauvegarde de la checklist */
(function () {
  var SB_URL = 'https://txvrlvcxfnylnrpdrxtt.supabase.co';
  var KEY = 'sb_publishable_7aA-njoU5fU2ialO0ExwQQ_REHjAEIe';
  var LKEY = 'lmm-checklist-v1';
  var ROOT = (document.querySelector('link[rel=icon]').getAttribute('href') || '').replace('assets/favicon.svg', '');
  var sb = null, user = null;

  function $(s, r) { return (r || document).querySelector(s); }
  function local() { try { return JSON.parse(localStorage.getItem(LKEY) || '{}') || {}; } catch (e) { return {}; } }
  function setLocal(o) { try { localStorage.setItem(LKEY, JSON.stringify(o)); } catch (e) {} }

  function loadLib(cb) {
    if (window.supabase) return cb();
    var s = document.createElement('script');
    s.src = ROOT + 'assets/vendor/supabase.js';
    s.onload = cb;
    s.onerror = function () { var m = $('#acc-msg'); if (m) m.textContent = 'Connexion impossible pour le moment. Réessayez plus tard.'; };
    document.head.appendChild(s);
  }

  function navLink() {
    document.querySelectorAll('[data-guest]').forEach(function (el) { el.hidden = !!user; });
    var a = $('#nav-account-txt'); if (!a) return;
    a.textContent = user ? 'Mon compte' : 'Connexion';
    $('#nav-account').classList.toggle('on', !!user);
  }

  /* Synchronisation de la checklist */
  var saveT = null;
  function pushList() {
    if (!user) return;
    clearTimeout(saveT);
    saveT = setTimeout(function () {
      sb.from('lmm_lists').upsert({ user_id: user.id, items: local(), updated_at: new Date().toISOString() });
    }, 600);
  }
  function pullList() {
    if (!user) return Promise.resolve(null);
    return sb.from('lmm_lists').select('*').eq('user_id', user.id).maybeSingle().then(function (r) {
      var row = r.data, pend = null;
      try { pend = localStorage.getItem('lmm-news-pending'); localStorage.removeItem('lmm-news-pending'); } catch (x) {}
      var extra = {};
      if (pend === '1') { extra.newsletter = true; extra.newsletter_at = new Date().toISOString(); }
      var merged = Object.assign({}, (row && row.items) || {}, local());
      setLocal(merged);
      if (!row || pend === '1' || Object.keys(merged).length !== Object.keys(row.items || {}).length) {
        return sb.from('lmm_lists').upsert(Object.assign({ user_id: user.id, items: merged, updated_at: new Date().toISOString() }, extra))
          .select().maybeSingle().then(function (x) { return x.data || row; });
      }
      return row;
    });
  }
  document.addEventListener('ldn:change', pushList);

  /* Page compte */
  function msg(t, ok) { var m = $('#acc-msg'); if (m) { m.textContent = t; m.className = 'acc-msg' + (ok ? ' ok' : ''); } }
  function err(e) {
    var t = (e && e.message) || '';
    if (/Invalid login/i.test(t)) return 'E-mail ou mot de passe incorrect.';
    if (/already registered/i.test(t)) return 'Un compte existe déjà avec cet e-mail.';
    if (/Password should be/i.test(t)) return 'Le mot de passe doit faire au moins 8 caractères.';
    if (/Email not confirmed/i.test(t)) return 'Confirmez d\'abord votre e-mail avec le lien reçu.';
    if (/rate limit|security purposes/i.test(t)) return 'Trop de demandes. Attendez une minute avant de redemander un lien.';
    if (/invalid/i.test(t) && /email/i.test(t)) return 'Cette adresse e-mail ne semble pas valide.';
    return 'Une erreur est survenue. Réessayez.';
  }

  function renderAccount(row) {
    var box = $('#acc'); if (!box) return;
    if (!user) { $('#acc-out').hidden = false; $('#acc-in').hidden = true; return; }
    $('#acc-out').hidden = true; $('#acc-in').hidden = false;
    $('#acc-email').textContent = user.email;
    var n = Object.keys(local()).length;
    $('#acc-count').textContent = n + ' article' + (n > 1 ? 's' : '') + ' coché' + (n > 1 ? 's' : '');
    if (row) {
      $('#f-names').value = row.names || '';
      $('#f-date').value = row.wedding_date || '';
      $('#f-public').checked = !!row.is_public;
      $('#f-news').checked = !!row.newsletter;
      var base = new URL(ROOT + 'ma-liste/', location.href).href;
      $('#acc-share').value = base + '?l=' + row.slug;
      $('#acc-sharebox').hidden = !row.is_public;
    }
  }

  function bindAccount() {
    var box = $('#acc'); if (!box) return;
    $('#form-magic').addEventListener('submit', function (e) {
      e.preventDefault();
      var em = this.email.value.trim(), btn = this.querySelector('button');
      try { localStorage.setItem('lmm-news-pending', this.news.checked ? '1' : '0'); } catch (x) {}
      btn.disabled = true; msg('Envoi du lien...');
      sb.auth.signInWithOtp({ email: em, options: { emailRedirectTo: new URL(ROOT + 'compte/', location.href).href } })
        .then(function (r) {
          btn.disabled = false;
          if (r.error) return msg(err(r.error));
          msg(''); $('#form-magic').hidden = true; $('#acc-sent').hidden = false;
        });
    });
    $('#acc-again').addEventListener('click', function () { $('#acc-sent').hidden = true; $('#form-magic').hidden = false; msg(''); });
    $('#form-wed').addEventListener('submit', function (e) {
      e.preventDefault();
      var upd = { user_id: user.id, names: $('#f-names').value.trim() || null, wedding_date: $('#f-date').value || null,
        is_public: $('#f-public').checked, newsletter: $('#f-news').checked, items: local(), updated_at: new Date().toISOString() };
      if ($('#f-news').checked) upd.newsletter_at = new Date().toISOString();
      sb.from('lmm_lists').upsert(upd).select().maybeSingle().then(function (r) {
        if (r.error) return msg(err(r.error));
        renderAccount(r.data); msg('Enregistré.', true);
      });
    });
    $('#acc-copy').addEventListener('click', function () {
      var v = $('#acc-share').value, b = this;
      if (navigator.clipboard) navigator.clipboard.writeText(v).then(function () { b.textContent = 'Lien copié'; setTimeout(function () { b.textContent = 'Copier le lien'; }, 1800); });
    });
    $('#acc-logout').addEventListener('click', function () { sb.auth.signOut(); });
    $('#acc-wipe').addEventListener('click', function () {
      var b = this;
      if (!b.getAttribute('data-c')) { b.setAttribute('data-c', 1); b.textContent = 'Confirmer la suppression'; return; }
      sb.from('lmm_lists').delete().eq('user_id', user.id).then(function () {
        setLocal({}); msg('Vos données ont été supprimées. Pour supprimer aussi le compte, écrivez-nous.', true);
        b.removeAttribute('data-c'); b.textContent = 'Supprimer mes données';
      });
    });
  }

  /* Page publique d'une liste partagée */
  function publicList() {
    var box = $('#pub'); if (!box) return;
    var slug = new URLSearchParams(location.search).get('l');
    if (!slug) { box.innerHTML = '<p>Ce lien de liste est incomplet. Demandez le bon lien aux mariés.</p>'; return; }
    sb.rpc('lmm_public_list', { p_slug: slug }).then(function (r) {
      var row = r.data && r.data[0];
      if (!row) { box.innerHTML = '<p>Cette liste n\'existe pas ou n\'est plus partagée.</p>'; return; }
      var D = window.LDN_DATA || [], st = row.items || {}, h = '';
      var title = row.names ? 'La liste de mariage de ' + esc(row.names) : 'Une liste de mariage';
      $('#pub-title').textContent = title.replace(/&amp;/g, '&');
      D.forEach(function (c, ci) {
        var sel = c.i.filter(function (_, ii) { return st[ci + ':' + ii]; });
        if (!sel.length) return;
        h += '<section class="cat t-' + ['lilas','ciel','peche','menthe','miel','lilas','ciel'][ci % 7] + '"><h2><span class="cat-e" aria-hidden="true">' + c.e + '</span><span class="cat-n">' + c.c + '</span></h2>';
        sel.forEach(function (it) {
          h += '<div class="it"><div class="tx"><label>' + it.n + '</label><p>' + it.t + '</p></div><a class="go" href="' + it.u + '" target="_blank" rel="sponsored nofollow noopener">Voir</a></div>';
        });
        h += '</section>';
      });
      box.innerHTML = h || '<p>Les mariés n\'ont pas encore choisi d\'articles.</p>';
    });
  }
  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }

  loadLib(function () {
    sb = window.supabase.createClient(SB_URL, KEY);
    bindAccount();
    publicList();
    sb.auth.onAuthStateChange(function (ev, session) {
      user = session ? session.user : null;
      navLink();
      if (user) {
        pullList().then(function (row) {
          renderAccount(row);
          document.dispatchEvent(new CustomEvent('ldn:reload'));
        });
      } else { renderAccount(null); }
    });
  });
})();
