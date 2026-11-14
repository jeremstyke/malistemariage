document.addEventListener('click', function(e){
  var b = e.target.closest('.copy'); if (!b) return;
  var el = document.getElementById(b.getAttribute('data-t'));
  var t = el.innerText.replace(/\{LIEN\}/g, '[lien de ta liste]');
  function ok(){ b.textContent = 'Copié'; setTimeout(function(){ b.textContent = 'Copier le message'; }, 1800); }
  if (navigator.clipboard) navigator.clipboard.writeText(t).then(ok, function(){});
});
