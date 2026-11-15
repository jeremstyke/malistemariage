(function(){
  var D = window.LDN_DATA || [], P = window.LDN_PRIO || {}, KEY = 'lmm-checklist-v1';
  var st = {};
  try { st = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch(e) { st = {}; }
  function save(){ try { localStorage.setItem(KEY, JSON.stringify(st)); } catch(e){} document.dispatchEvent(new CustomEvent('ldn:change')); }
  function id(c, i){ return c + ':' + i; }
  var root = document.getElementById('ck'); if (!root) return;
  var total = 0; D.forEach(function(c){ total += c.i.length; });
  var filter = 'all';

  var h = '<div class="ckbar"><div class="prog"><i id="pg"></i></div>' +
    '<div class="ckinfo"><span id="cnt"></span><span>Gardé sur cet appareil</span></div>' +
    '<div class="filt" id="flt">' +
    '<button data-f="all" class="on">Tout</button><button data-f="1">Essentiel</button>' +
    '<button data-f="2">Utile</button><button data-f="3">Coup de cœur</button><button data-f="todo">Pas encore coché</button></div><p class="ck-tip">Astuce : cochez un article, cliquez sur « Voir » pour choisir votre modèle sur Amazon, puis collez son lien avec « Notre modèle ».</p></div>';
  D.forEach(function(c, ci){
    var tints = ['lilas','ciel','peche','menthe','miel','lilas','ciel'];
    h += '<section class="cat t-' + tints[ci % tints.length] + '" id="cat' + ci + '"><h2><span class="cat-e" aria-hidden="true">' + c.e + '</span><span class="cat-n">' + c.c + '</span><small id="cc' + ci + '"></small></h2>';
    c.i.forEach(function(it, ii){
      var k = id(ci, ii);
      h += '<div class="it" data-p="' + it.p + '" data-k="' + k + '">' +
        '<input type="checkbox" id="c' + ci + '_' + ii + '">' +
        '<div class="tx"><label for="c' + ci + '_' + ii + '">' + it.n + '<span class="pr p' + it.p + '">' + P[it.p] + '</span></label>' +
        '<p>' + it.t + (it.g ? ' <a class="howto" href="../' + it.g + '">Comment choisir ?</a>' : '') + '</p><div class="picked"></div></div>' +
        '<div class="acts"><a class="go" href="' + it.u + '" target="_blank" rel="sponsored nofollow noopener" aria-label="Voir ' + it.n + ' sur Amazon">Voir</a>' +
        '<button class="pick" type="button">Notre modèle</button></div></div>';
    });
    h += '</section>';
  });
  h += '<div class="ckact"><button class="btn" id="cp">Partager mon lien</button>' +
    '<button class="btn ghost" id="pr">Imprimer</button>' +
    '<a class="btn ghost" href="' + window.LDN_LIST + '" target="_blank" rel="sponsored nofollow noopener">Créer ma liste en ligne ↗</a>' +
    '<button class="btn ghost" id="rs">Tout décocher</button></div>';
  root.innerHTML = h;
  /* Mes produits choisis : lien Amazon collé, transformé en lien propre avec notre identifiant */
  var CKEY = KEY.replace('checklist', 'custom'), cu = [];
  try { cu = JSON.parse(localStorage.getItem(CKEY) || '[]') || []; } catch(e) { cu = []; }
  window.LDN_CUSTOM = function(){ return cu; };
  window.LDN_SET_CUSTOM = function(a){ cu = a || []; try { localStorage.setItem(CKEY, JSON.stringify(cu)); } catch(e){} renderMine(); };
  function saveCu(){ try { localStorage.setItem(CKEY, JSON.stringify(cu)); } catch(e){} document.dispatchEvent(new CustomEvent('ldn:change')); renderMine(); }
  function asinOf(u){ var m = String(u).match(/(?:\/dp\/|\/gp\/product\/|\/gp\/aw\/d\/|\/o\/ASIN\/)([A-Z0-9]{10})/i); return m ? m[1].toUpperCase() : null; }
  function nameOf(u){ try { var p = new URL(u).pathname.split('/'), i = p.indexOf('dp'); if (i > 0 && p[i-1] && p[i-1].length > 3) return decodeURIComponent(p[i-1]).replace(/-/g, ' ').slice(0, 80); } catch(e){} return ''; }
  function plink(a){ return 'https://www.amazon.fr/dp/' + a + '?tag=' + (window.LDN_TAG || ''); }
  function esc(s){ var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  var mine = document.createElement('section');
  mine.className = 'cat t-miel mine'; mine.id = 'mine';
  mine.innerHTML = '<h2><span class="cat-e" aria-hidden="true">⭐</span><span class="cat-n">Nos produits choisis</span><small id="mc"></small></h2>' +
    '<p class="mine-help">Vous avez trouvé un modèle précis sur Amazon ? Copiez son lien (bouton Partager de l\'appli ou adresse de la page) et collez-le ici : il s\'ajoute à votre liste et à votre page de partage.</p>' +
    '<form class="mine-f" id="mine-f"><input type="text" id="mine-u" placeholder="Collez le lien du produit Amazon" autocomplete="off" required>' +
    '<input type="text" id="mine-n" placeholder="Nom du produit (facultatif)" maxlength="80"><button class="btn sm" type="submit">Ajouter</button></form>' +
    '<p class="small" id="mine-msg" role="status"></p><div id="mine-l"></div>';
  root.insertBefore(mine, root.querySelector('.ckact'));
  function renderMine(){
    var l = document.getElementById('mine-l'); if (!l) return;
    l.innerHTML = cu.map(function(x, i){
      return '<div class="it done-no"><div class="tx"><label>' + esc(x.n || 'Produit Amazon') + '</label><p>Produit choisi sur Amazon</p></div>' +
        '<a class="go" href="' + plink(x.a) + '" target="_blank" rel="sponsored nofollow noopener">Voir</a>' +
        '<button class="mine-x" type="button" data-i="' + i + '" aria-label="Retirer">×</button></div>';
    }).join('');
    document.getElementById('mc').textContent = cu.length ? cu.length + '' : '';
  }
  function addAsin(a, name){
    if (cu.some(function(x){ return x.a === a; })) return mmsg('Ce produit est déjà dans votre liste.');
    cu.push({ a: a, n: name || ('Produit ' + a) }); saveCu();
    document.getElementById('mine-u').value = ''; document.getElementById('mine-n').value = '';
    mmsg('Produit ajouté.');
  }
  function mmsg(t){ document.getElementById('mine-msg').textContent = t; }
  document.getElementById('mine-f').addEventListener('submit', function(e){
    e.preventDefault();
    var raw = document.getElementById('mine-u').value.trim(), m = raw.match(/https?:\/\/\S+/), u = m ? m[0] : raw;
    var name = document.getElementById('mine-n').value.trim();
    var a = asinOf(u);
    if (a) return addAsin(a, name || nameOf(u));
    if (/^https?:\/\/(www\.)?(amzn\.eu|amzn\.to|a\.co)\//i.test(u)) {
      mmsg('Recherche du produit...');
      fetch('https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/amzn-resolve?u=' + encodeURIComponent(u))
        .then(function(r){ return r.json(); })
        .then(function(j){ if (j.asin) addAsin(j.asin, name || nameOf(j.url || '')); else mmsg('Impossible de lire ce lien court. Ouvrez le produit dans votre navigateur et copiez l\'adresse complète de la page.'); })
        .catch(function(){ mmsg('Impossible de lire ce lien court. Ouvrez le produit dans votre navigateur et copiez l\'adresse complète de la page.'); });
      return;
    }
    mmsg('Ce lien ne ressemble pas à un produit Amazon. Copiez l\'adresse de la page du produit.');
  });
  document.getElementById('mine-l').addEventListener('click', function(e){
    var b = e.target.closest('.mine-x'); if (!b) return;
    cu.splice(+b.getAttribute('data-i'), 1); saveCu();
  });
  document.addEventListener('ldn:reload', function(){ try { cu = JSON.parse(localStorage.getItem(CKEY) || '[]') || []; } catch(e){} renderMine(); });
  renderMine();

  var rows = root.querySelectorAll('.it[data-k]');
  function refresh(){
    var n = 0;
    rows.forEach(function(r){
      var on = !!st[r.getAttribute('data-k')];
      r.querySelector('input').checked = on;
      var v = st[r.getAttribute('data-k')], pk = r.querySelector('.picked'), pb = r.querySelector('.pick');
      if (pk) {
        if (v && typeof v === 'object' && v.a) {
          pk.innerHTML = '<span>⭐ Modèle choisi : <strong>' + esc(v.n || v.a) + '</strong></span> <a href="' + plink(v.a) + '" target="_blank" rel="sponsored nofollow noopener">voir</a> <button type="button" class="unpick">retirer</button>';
          pb.textContent = 'Changer';
        } else { pk.innerHTML = ''; pb.textContent = 'Notre modèle'; }
      }
      r.classList.toggle('done', on);
      if (on) n++;
      var p = r.getAttribute('data-p'), show = filter === 'all' || filter === p || (filter === 'todo' && !on);
      r.classList.toggle('hide', !show);
    });
    D.forEach(function(c, ci){
      var m = 0; c.i.forEach(function(_, ii){ if (st[id(ci, ii)]) m++; });
      document.getElementById('cc' + ci).textContent = m + '/' + c.i.length;
    });
    document.getElementById('cnt').textContent = n + ' article' + (n > 1 ? 's' : '') + ' coché' + (n > 1 ? 's' : '') + ' sur ' + total;
    document.getElementById('pg').style.width = (total ? n / total * 100 : 0) + '%';
  }
  root.addEventListener('click', function(e){
    var r = e.target.closest('.it[data-k]'); if (!r) return;
    var k = r.getAttribute('data-k');
    if (e.target.closest('.go')) { if (!st[k]) { st[k] = 1; save(); refresh(); } return; }
    if (e.target.closest('.unpick')) { st[k] = 1; save(); refresh(); return; }
    if (!e.target.closest('.pick')) return;
    var f = r.querySelector('.pickf');
    if (f) { f.remove(); return; }
    f = document.createElement('form'); f.className = 'pickf';
    f.innerHTML = '<input type="text" placeholder="Collez le lien Amazon du modèle" autocomplete="off" required><button class="btn sm" type="submit">OK</button><p class="small"></p>';
    r.appendChild(f); f.querySelector('input').focus();
    f.addEventListener('submit', function(ev){
      ev.preventDefault();
      var raw = f.querySelector('input').value.trim(), m = raw.match(/https?:\/\/\S+/), u = m ? m[0] : raw, msg = f.querySelector('p');
      function done(a, n){ st[k] = { a: a, n: (n || '').slice(0, 80) }; save(); f.remove(); refresh(); }
      var a = asinOf(u);
      if (a) return done(a, nameOf(u));
      if (/^https?:\/\/(www\.)?(amzn\.eu|amzn\.to|a\.co)\//i.test(u)) {
        msg.textContent = 'Recherche du produit...';
        fetch('https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/amzn-resolve?u=' + encodeURIComponent(u))
          .then(function(x){ return x.json(); }).then(function(j){ if (j.asin) done(j.asin, nameOf(j.url || '')); else msg.textContent = 'Lien court illisible : ouvrez le produit dans votre navigateur et copiez l\'adresse complète.'; })
          .catch(function(){ msg.textContent = 'Lien court illisible : ouvrez le produit dans votre navigateur et copiez l\'adresse complète.'; });
        return;
      }
      msg.textContent = 'Lien non reconnu : copiez l\'adresse de la page du produit Amazon.';
    });
  });
  root.addEventListener('change', function(e){
    if (e.target.type !== 'checkbox') return;
    var r = e.target.closest('.it'); if (!r) return;
    var k = r.getAttribute('data-k');
    if (e.target.checked) st[k] = 1; else delete st[k];
    save(); refresh();
  });
  document.getElementById('flt').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    filter = b.getAttribute('data-f');
    this.querySelectorAll('button').forEach(function(x){ x.classList.toggle('on', x === b); });
    refresh();
  });
  function listText(){
    var t = 'Notre liste de mariage\n';
    D.forEach(function(c, ci){
      var sel = c.i.filter(function(_, ii){ return st[id(ci, ii)]; });
      if (!sel.length) return;
      t += '\n' + c.e + ' ' + c.c + '\n';
      sel.forEach(function(it){ t += '- ' + it.n + '\n'; });
    });
    return t + '\nFaite avec Ma liste mariage';
  }
  var ROOT = ((document.querySelector('link[rel=icon]') || {}).getAttribute ? document.querySelector('link[rel=icon]').getAttribute('href') : '').replace('assets/favicon.svg', '');
  function flash(b, t){ b.textContent = t; setTimeout(function(){ b.textContent = 'Partager mon lien'; }, 2200); }
  document.getElementById('cp').addEventListener('click', function(){
    var b = this, A = window.LDN_ACC;
    if (!Object.keys(st).length && !cu.length) return flash(b, 'Cochez d\'abord des articles');
    if (!A) { location.href = ROOT + 'compte/?partage=1'; return; }
    if (!A.row || !A.row.is_public) {
      b.textContent = '...';
      A.makePublic().then(function(){ b.textContent = 'Lien activé : touchez pour partager'; });
      return;
    }
    var url = new URL(ROOT + 'ma-liste/?l=' + A.row.slug, location.href).href, t = 'Voici notre liste de mariage : ' + url;
    if (navigator.share) { navigator.share({ title: 'Notre liste de mariage', text: 'Voici notre liste de mariage : ', url: url }).catch(function(){}); return; }
    function ok(){ flash(b, 'Lien copié'); }
    function fallback(){ var a = document.createElement('textarea'); a.value = t; document.body.appendChild(a); a.select(); try { document.execCommand('copy'); ok(); } catch(e){} a.remove(); }
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(ok, fallback); else fallback();
  });
  document.getElementById('pr').addEventListener('click', function(){ filter = 'all'; refresh(); window.print(); });
  document.getElementById('rs').addEventListener('click', function(){
    var b = this;
    if (b.getAttribute('data-c')) { st = {}; save(); refresh(); b.removeAttribute('data-c'); b.textContent = 'Tout décocher'; }
    else { b.setAttribute('data-c', 1); b.textContent = 'Confirmer ?'; setTimeout(function(){ b.removeAttribute('data-c'); b.textContent = 'Tout décocher'; }, 3000); }
  });
  document.addEventListener('ldn:reload', function(){ try { st = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch(e){} refresh(); });
  refresh();
})();
