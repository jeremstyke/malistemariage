/* Outils gratuits : rétroplanning, budget mariage, calculateur de liste */
(function () {
  function $(s) { return document.querySelector(s); }
  var MOIS = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'];
  function fmt(d) { return d.getDate() + ' ' + MOIS[d.getMonth()] + ' ' + d.getFullYear(); }
  function parse(v) { if (!v) return null; var p = v.split('-'); return new Date(+p[0], +p[1] - 1, +p[2], 12); }
  function addM(d, m) { var x = new Date(d.getTime()); x.setMonth(x.getMonth() + m); return x; }
  function addD(d, n) { var x = new Date(d.getTime()); x.setDate(x.getDate() + n); return x; }
  function eur(n) { return Math.round(n).toLocaleString('fr-FR') + ' €'; }
  function show(h) { var o = $('#t-out'); o.innerHTML = h; o.hidden = false; o.scrollIntoView({ behavior: 'smooth', block: 'start' }); }

  /* Rétroplanning */
  var rp = $('#t-retro');
  if (rp) {
    rp.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = parse($('#t-date').value);
      if (!d) return show('<p>Indiquez la date du mariage.</p>');
      var now = new Date(); now.setHours(12, 0, 0, 0);
      var steps = [
        [-12, 'm', 'Fixer le budget, la date et le nombre d\'invités, réserver le lieu de réception'],
        [-10, 'm', 'Réserver les prestataires clés : traiteur, photographe, musique'],
        [-9, 'm', 'Choisir les témoins, envoyer les « save the date »'],
        [-8, 'm', 'Chercher les tenues, réserver l\'officiant ou la cérémonie religieuse'],
        [-6, 'm', 'Se renseigner à la mairie sur les démarches, réserver le voyage de noces'],
        [-4, 'm', 'Créer la liste de mariage et commander les faire-part'],
        [-3, 'm', 'Envoyer les faire-part avec le lien de la liste'],
        [-2, 'm', 'Déposer le dossier de mariage à la mairie (vérifiez les délais de votre commune), choisir les alliances, le menu, la décoration'],
        [-1, 'm', 'Plan de table, essais coiffure et maquillage, relancer les réponses'],
        [-7, 'd', 'Confirmer les horaires avec tous les prestataires, préparer les enveloppes'],
        [0, 'd', 'Le grand jour'],
        [30, 'd', 'Envoyer les remerciements, fermer la liste']
      ];
      var h = '<p class="res-big">Votre rétroplanning pour un mariage le <strong>' + fmt(d) + '</strong></p><ol class="res-cal">';
      var late = 0;
      steps.forEach(function (s) {
        var dt = s[1] === 'm' ? addM(d, s[0]) : addD(d, s[0]);
        var past = dt < now; if (past && s[0] < 0) late++;
        h += '<li class="' + (past ? 'past' : '') + '"><span>' + (s[0] === 0 ? 'Jour J' : 'Avant le ' + fmt(dt)) + '</span>' + s[2] + '</li>';
      });
      h += '</ol>';
      if (late) h += '<p>Certaines étapes sont déjà passées : pas de panique, faites-les dès maintenant, dans l\'ordre de la liste.</p>';
      h += '<p class="small">Calendrier indicatif. Les délais réels dépendent de votre région, de la saison et de vos prestataires.</p>';
      show(h);
    });
  }

  /* Budget mariage */
  var bg = $('#t-budget');
  if (bg) {
    var cats = [['Lieu et réception (repas, boissons)', 45], ['Tenues et beauté', 10], ['Photo et vidéo', 9], ['Musique et animation', 6],
                ['Fleurs et décoration', 7], ['Alliances', 5], ['Faire-part et papeterie', 3], ['Transport et hébergement', 5], ['Imprévus', 10]];
    var box = $('#t-cats');
    box.innerHTML = cats.map(function (c, i) {
      return '<label class="rng">' + c[0] + ' <output id="p' + i + '">' + c[1] + ' %</output><input type="range" min="0" max="70" value="' + c[1] + '" data-i="' + i + '"></label>';
    }).join('');
    box.addEventListener('input', function (e) { var i = e.target.getAttribute('data-i'); if (i !== null) $('#p' + i).textContent = e.target.value + ' %'; });
    bg.addEventListener('submit', function (e) {
      e.preventDefault();
      var guests = parseInt($('#t-guests').value, 10) || 0, total = parseFloat($('#t-total').value) || 0;
      if (!total) return show('<p>Indiquez votre budget total.</p>');
      var vals = Array.prototype.map.call(box.querySelectorAll('input'), function (x) { return +x.value; });
      var sum = vals.reduce(function (a, b) { return a + b; }, 0) || 1;
      var h = '<p class="res-big">Budget total : <strong>' + eur(total) + '</strong>' + (guests ? ', soit ' + eur(total / guests) + ' par invité' : '') + '</p>';
      if (sum !== 100) h += '<p class="small">Vos pourcentages font ' + sum + ' % : ils ont été ramenés à 100 %.</p>';
      h += '<table><thead><tr><th>Poste</th><th>Part</th><th>Montant</th></tr></thead><tbody>';
      cats.forEach(function (c, i) { var p = vals[i] / sum; h += '<tr><td>' + c[0] + '</td><td>' + Math.round(p * 100) + ' %</td><td>' + eur(total * p) + '</td></tr>'; });
      h += '</tbody></table><p class="small">Répartition indicative, à ajuster avec les vrais devis de vos prestataires.</p>';
      show(h);
    });
  }

  /* Calculateur de liste */
  var ls = $('#t-liste');
  if (ls) {
    ls.addEventListener('submit', function (e) {
      e.preventDefault();
      var g = parseInt($('#t-g').value, 10) || 0, together = $('#t-together').checked;
      if (!g) return show('<p>Indiquez le nombre d\'invités.</p>');
      var foyers = Math.ceil(g / 2), n = Math.round(foyers * (together ? 0.9 : 1.2));
      n = Math.max(15, n);
      var a = Math.round(n * 0.3), b = Math.round(n * 0.4), c = n - a - b;
      var h = '<p class="res-big">Visez environ <strong>' + n + ' articles</strong> pour ' + g + ' invités</p>' +
        '<table><thead><tr><th>Tranche de prix</th><th>Nombre d\'articles</th></tr></thead><tbody>' +
        '<tr><td>Moins de 40 €</td><td>' + a + '</td></tr><tr><td>40 à 120 €</td><td>' + b + '</td></tr><tr><td>Plus de 120 € (cadeaux de groupe)</td><td>' + c + '</td></tr></tbody></table>' +
        (together ? '<p>Vous vivez déjà ensemble : une liste plus courte suffit, complétée si besoin par une cagnotte pour le voyage.</p>' : '<p>Premier logement : prévoyez un peu plus d\'articles pour équiper toute la maison.</p>') +
        '<p>Pour remplir la liste, partez de notre <a href="../checklist/">checklist par pièce</a>.</p>';
      show(h);
    });
  }
})();
