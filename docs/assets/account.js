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
  var CKEY = LKEY.replace('checklist', 'custom');
  function localCu() { if (window.LDN_CUSTOM) return window.LDN_CUSTOM(); try { return JSON.parse(localStorage.getItem(CKEY) || '[]') || []; } catch (e) { return []; } }
  function setCu(a) { if (window.LDN_SET_CUSTOM) return window.LDN_SET_CUSTOM(a); try { localStorage.setItem(CKEY, JSON.stringify(a)); } catch (e) {} }
  function mergeCu(a, b) { var seen = {}, out = []; (a || []).concat(b || []).forEach(function (x) { if (x && x.a && !seen[x.a]) { seen[x.a] = 1; out.push(x); } }); return out; }

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
      sb.from('lmm_lists').upsert({ user_id: user.id, items: local(), custom: localCu(), updated_at: new Date().toISOString() });
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
      var mcu = mergeCu((row && row.custom) || [], localCu()); setCu(mcu);
      if (!row || pend === '1' || Object.keys(merged).length !== Object.keys(row.items || {}).length || mcu.length !== (row.custom || []).length) {
        return sb.from('lmm_lists').upsert(Object.assign({ user_id: user.id, items: merged, custom: mcu, updated_at: new Date().toISOString() }, extra))
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
    if (!user) { window.LDN_ACC = null; $('#acc-out').hidden = false; $('#acc-in').hidden = true; if (/partage=1/.test(location.search)) msg('Connectez-vous pour obtenir votre lien de partage : c\'est gratuit et sans mot de passe.'); return; }
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
        is_public: $('#f-public').checked, newsletter: $('#f-news').checked, items: local(), custom: localCu(), updated_at: new Date().toISOString() };
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


  /* L'autre site (même compte) */
  function otherList() {
    var box = $('#acc-other'); if (!box || !user) return;
    sb.from('ldn_lists').select('items,is_public,slug').eq('user_id', user.id).maybeSingle().then(function (r) {
      var row = r.data, n = row ? Object.keys(row.items || {}).length : 0, h;
      if (row && n) {
        h = '<span aria-hidden="true">🍼</span><div><strong>Votre liste de naissance : ' + n + ' article' + (n > 1 ? 's' : '') + ' coché' + (n > 1 ? 's' : '') + '</strong><span>' +
          (row.is_public ? 'Liste partagée avec vos proches : <a href="https://malistebebe.fr/ma-liste/?l=' + row.slug + '" target="_blank" rel="noopener">voir le lien</a>. ' : '') +
          'Même compte, connectez-vous une fois là-bas avec votre e-mail.</span></div><a class="btn sm" href="https://malistebebe.fr/compte/" target="_blank" rel="noopener">Ouvrir Ma liste bébé</a>';
      } else {
        h = '<span aria-hidden="true">🍼</span><div><strong>Un bébé en route ?</strong><span>Votre compte marche aussi sur Ma liste bébé : même e-mail, la checklist de naissance complète.</span></div><a class="btn ghost sm" href="https://malistebebe.fr/" target="_blank" rel="noopener">Découvrir Ma liste bébé</a>';
      }
      box.innerHTML = h; box.hidden = false;
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
      var D = window.LDN_DATA || [], st = row.items || {}, h = '<p class="res-help">Vous voulez offrir un article ? Cliquez sur « Je l\'offre » pour le réserver : les autres invités verront qu\'il est déjà pris, puis achetez-le avec « Voir ».</p>';
      var RES = row.reserved || {}, MKEY = 'lmm-res-' + slug, MINE = {};
      try { MINE = JSON.parse(localStorage.getItem(MKEY) || '{}') || {}; } catch (e) {}
      Object.keys(MINE).forEach(function (k) { if (!RES[k]) delete MINE[k]; });
      var title = row.names ? 'La liste de mariage de ' + esc(row.names) : 'Une liste de mariage';
      $('#pub-title').textContent = title.replace(/&amp;/g, '&');
      D.forEach(function (c, ci) {
        var sel = []; c.i.forEach(function (it, ii) { var v = st[ci + ':' + ii]; if (v) sel.push({ it: it, v: v, k: ci + ':' + ii }); });
        if (!sel.length) return;
        h += '<section class="cat t-' + ['lilas','ciel','peche','menthe','miel','lilas','ciel'][ci % 7] + '"><h2><span class="cat-e" aria-hidden="true">' + c.e + '</span><span class="cat-n">' + c.c + '</span></h2>';
        sel.forEach(function (o) {
          var it = o.it, v = o.v, k = o.k, pick = v && typeof v === 'object' && v.a, res = RES[k], me = MINE[k];
          var href = pick ? 'https://www.amazon.fr/dp/' + encodeURIComponent(v.a) + '?tag=' + (window.LDN_TAG || '') : it.u;
          var go = '<a class="go" href="' + href + '" target="_blank" rel="sponsored nofollow noopener">Voir</a>';
          var acts = res ? (me ? go + '<button class="res-undo" type="button">Annuler</button>' : '<span class="res-tag">🎁 Déjà offert' + (res.n ? ' par ' + esc(res.n) : '') + '</span>')
                         : go + '<button class="res-btn" type="button">Je l\'offre</button>';
          h += '<div class="it' + (res && !me ? ' reserved' : '') + '" data-k="' + k + '"><div class="tx"><label>' + it.n + '</label><p>' + (pick ? '⭐ ' + esc(v.n || 'Modèle choisi') : it.t) + '</p>' +
            (res && me ? '<p class="res-mine">🎁 Déjà offert' + (res.n ? ' par ' + esc(res.n) : '') + '</p>' : '') + '</div><div class="acts">' + acts + '</div></div>';
        });
        h += '</section>';
      });
      var cu = row.custom || [];
      if (cu.length) {
        h += '<section class="cat t-miel"><h2><span class="cat-e" aria-hidden="true">⭐</span><span class="cat-n">Produits choisis</span></h2>';
        cu.forEach(function (x) { h += '<div class="it"><div class="tx"><label>' + esc(x.n || 'Produit') + '</label></div><a class="go" href="https://www.amazon.fr/dp/' + encodeURIComponent(x.a) + '?tag=' + (window.LDN_TAG || '') + '" target="_blank" rel="sponsored nofollow noopener">Voir</a></div>'; });
        h += '</section>';
      }
      box.innerHTML = h || '<p>Les mariés n\'ont pas encore choisi d\'articles.</p>';
      box.onclick = function (e) {
        var r = e.target.closest('.it[data-k]'); if (!r) return;
        var k = r.getAttribute('data-k');
        if (e.target.closest('.res-undo')) {
          sb.rpc('lmm_unreserve', { p_slug: slug, p_key: k, p_tok: MINE[k] }).then(function () { delete MINE[k]; try { localStorage.setItem(MKEY, JSON.stringify(MINE)); } catch (x) {} publicList(); });
          return;
        }
        if (!e.target.closest('.res-btn')) return;
        if (r.querySelector('.resf')) return;
        var f = document.createElement('form'); f.className = 'pickf resf';
        f.innerHTML = '<input type="text" maxlength="40" placeholder="Votre prénom (facultatif)"><button class="btn sm" type="submit">Confirmer</button><p class="small"></p>';
        r.appendChild(f); f.querySelector('input').focus();
        f.addEventListener('submit', function (ev) {
          ev.preventDefault();
          sb.rpc('lmm_reserve', { p_slug: slug, p_key: k, p_name: f.querySelector('input').value }).then(function (x) {
            if (!x.data) { f.querySelector('p').textContent = 'Quelqu\'un vient de le réserver juste avant vous. Choisissez un autre article.'; setTimeout(publicList, 1500); return; }
            MINE[k] = x.data; try { localStorage.setItem(MKEY, JSON.stringify(MINE)); } catch (y) {}
            publicList();
            setTimeout(function () { var m = document.querySelector('.it[data-k="' + k + '"] .tx'); if (m) { var p = document.createElement('p'); p.className = 'res-ok'; p.textContent = 'C\'est noté, merci ! Il ne reste plus qu\'à l\'acheter avec le bouton « Voir ».'; m.appendChild(p); } }, 400);
          });
        });
      };
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
          window.LDN_ACC = { row: row, makePublic: function () {
            var self = this;
            return sb.from('lmm_lists').update({ is_public: true, updated_at: new Date().toISOString() }).eq('user_id', user.id).select().maybeSingle()
              .then(function (r) { if (r.data) self.row = r.data; return self.row; });
          } };
          document.dispatchEvent(new CustomEvent('ldn:acc'));
          renderAccount(row);
          otherList();
          document.dispatchEvent(new CustomEvent('ldn:reload'));
        });
      } else { renderAccount(null); }
    });
  });
})();
