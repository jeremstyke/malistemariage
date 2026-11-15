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
    '<button data-f="2">Utile</button><button data-f="3">Coup de cœur</button><button data-f="todo">Pas encore coché</button></div></div>';
  D.forEach(function(c, ci){
    var tints = ['lilas','ciel','peche','menthe','miel','lilas','ciel'];
    h += '<section class="cat t-' + tints[ci % tints.length] + '" id="cat' + ci + '"><h2><span class="cat-e" aria-hidden="true">' + c.e + '</span><span class="cat-n">' + c.c + '</span><small id="cc' + ci + '"></small></h2>';
    c.i.forEach(function(it, ii){
      var k = id(ci, ii);
      h += '<div class="it" data-p="' + it.p + '" data-k="' + k + '">' +
        '<input type="checkbox" id="c' + ci + '_' + ii + '">' +
        '<div class="tx"><label for="c' + ci + '_' + ii + '">' + it.n + '<span class="pr p' + it.p + '">' + P[it.p] + '</span></label>' +
        '<p>' + it.t + '</p></div>' +
        '<a class="go" href="' + it.u + '" target="_blank" rel="sponsored nofollow noopener" aria-label="Voir ' + it.n + ' sur Amazon">Voir</a></div>';
    });
    h += '</section>';
  });
  h += '<div class="ckact"><button class="btn" id="cp">Copier la liste</button>' +
    '<button class="btn ghost" id="pr">Imprimer</button>' +
    '<a class="btn ghost" href="' + window.LDN_LIST + '" target="_blank" rel="sponsored nofollow noopener">Créer ma liste en ligne ↗</a>' +
    '<button class="btn ghost" id="rs">Tout décocher</button></div>';
  root.innerHTML = h;

  var rows = root.querySelectorAll('.it');
  function refresh(){
    var n = 0;
    rows.forEach(function(r){
      var on = !!st[r.getAttribute('data-k')];
      r.querySelector('input').checked = on;
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
  root.addEventListener('change', function(e){
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
  document.getElementById('cp').addEventListener('click', function(){
    var b = this, t = listText();
    if (!Object.keys(st).length) { b.textContent = 'Cochez d\'abord des articles'; setTimeout(function(){ b.textContent = 'Copier la liste'; }, 1800); return; }
    function ok(){ b.textContent = 'Copié'; setTimeout(function(){ b.textContent = 'Copier la liste'; }, 1800); }
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(ok, fallback); else fallback();
    function fallback(){ var a = document.createElement('textarea'); a.value = t; document.body.appendChild(a); a.select(); try { document.execCommand('copy'); ok(); } catch(e){} a.remove(); }
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
