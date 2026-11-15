# -*- coding: utf-8 -*-
# Outils gratuits de Ma liste mariage

TOOLS = []

def t(**k):
    TOOLS.append(k)

t(slug='retroplanning-mariage/',
  title="Rétroplanning mariage : votre calendrier mois par mois",
  h1="Rétroplanning de mariage",
  short="Rétroplanning mariage",
  desc="Entrez la date de votre mariage et obtenez votre rétroplanning personnalisé : lieu, prestataires, faire-part, liste de mariage, mairie et remerciements.",
  emoji='🗓️', tint='lilas',
  tool="""<form id="t-retro" class="accf tool-form">
<label>Date du mariage<input type="date" id="t-date" required></label>
<button class="btn" type="submit">Voir mon rétroplanning</button>
</form>
<div id="t-out" class="tool-res" hidden aria-live="polite"></div>""",
  body="""
<h2>Pourquoi un rétroplanning ?</h2>
<p>Organiser un mariage, c'est des dizaines de tâches qui dépendent les unes des autres : on ne commande pas les faire-part avant d'avoir le lieu, ni le plan de table avant les réponses des invités. Le rétroplanning part de la date du mariage et remonte le temps pour vous dire quoi faire, et quand.</p>
<h2>Les grandes étapes</h2>
<table><thead><tr><th>Quand</th><th>Priorités</th></tr></thead><tbody>
<tr><td>12 à 10 mois avant</td><td>Budget, date, lieu, prestataires clés</td></tr>
<tr><td>9 à 6 mois avant</td><td>Témoins, tenues, voyage de noces, démarches</td></tr>
<tr><td>4 à 3 mois avant</td><td>Liste de mariage, faire-part</td></tr>
<tr><td>2 à 1 mois avant</td><td>Dossier à la mairie, alliances, menu, plan de table</td></tr>
<tr><td>Après le mariage</td><td>Remerciements, fermeture de la liste</td></tr>
</tbody></table>
<h2>Les délais de la mairie</h2>
<p>Pour un mariage civil, un dossier doit être déposé à la mairie avant la cérémonie, puis les bans sont publiés. Les pièces demandées et les délais varient selon les communes : renseignez-vous tôt auprès de la vôtre, surtout si vous visez une date très demandée au printemps ou en été.</p>
<h2>Et la liste de mariage ?</h2>
<p>Le bon moment, c'est trois à quatre mois avant, pour l'envoyer avec les faire-part. Préparez-la avec notre <a href="{R}checklist/">checklist par pièce</a>, estimez le nombre d'articles avec notre <a href="{R}calculateur-liste-de-mariage/">calculateur</a>, et annoncez-la avec nos <a href="{R}message-liste-de-mariage/">textes tout prêts</a>. Plus de détails dans <a href="{R}quand-faire-sa-liste-de-mariage/">quand faire sa liste de mariage</a>.</p>
<h2>Moins d'un an pour tout organiser ?</h2>
<p>C'est tout à fait faisable. Entrez votre date : les étapes déjà dépassées apparaissent en grisé. Faites-les dès maintenant, dans l'ordre, en commençant par le lieu et le traiteur, qui sont les plus difficiles à trouver au dernier moment.</p>
""",
  faq=[("Combien de temps avant faut-il organiser son mariage ?", "Beaucoup de couples commencent 12 à 18 mois avant, surtout pour réserver le lieu. Un mariage plus simple peut s'organiser en quelques mois."),
       ("Quand envoyer les faire-part de mariage ?", "En général trois mois avant le mariage, avec le lien de la liste. Un « save the date » peut partir bien plus tôt.")])

t(slug='calculateur-budget-mariage/',
  title="Calculateur de budget mariage : répartition par poste",
  h1="Calculateur de budget mariage",
  short="Budget mariage",
  desc="Répartissez votre budget de mariage entre les postes : réception, tenues, photo, musique, décoration, alliances. Ajustez les pourcentages, le calcul est immédiat.",
  emoji='💶', tint='miel',
  tool="""<form id="t-budget" class="accf tool-form">
<label>Budget total (en euros)<input type="number" id="t-total" min="0" step="100" inputmode="numeric" required></label>
<label>Nombre d'invités (facultatif)<input type="number" id="t-guests" min="0" inputmode="numeric"></label>
<fieldset class="rngs"><legend>Répartition (ajustez selon vos priorités)</legend><div id="t-cats"></div></fieldset>
<button class="btn" type="submit">Calculer la répartition</button>
</form>
<div id="t-out" class="tool-res" hidden aria-live="polite"></div>""",
  body="""
<h2>Comment utiliser le calculateur</h2>
<p>Indiquez votre budget total, puis ajustez la part de chaque poste selon vos priorités. Les pourcentages proposés par défaut sont une répartition indicative, pas une règle : si la photo compte beaucoup pour vous, augmentez-la et réduisez un autre poste. Le calculateur ramène toujours le total à 100 %.</p>
<h2>Le poste le plus lourd : la réception</h2>
<p>Le lieu et le repas représentent souvent la plus grosse part du budget, car ils dépendent directement du nombre d'invités. C'est le premier levier pour faire des économies : réduire la liste d'invités de 10 personnes change davantage le budget que de choisir des fleurs moins chères.</p>
<h2>Où économiser sans regret</h2>
<table><thead><tr><th>Poste</th><th>Idée d'économie</th></tr></thead><tbody>
<tr><td>Réception</td><td>Date hors saison, brunch le lendemain plutôt qu'un deuxième repas</td></tr>
<tr><td>Décoration</td><td>Fleurs de saison, décoration réutilisée entre cérémonie et réception</td></tr>
<tr><td>Faire-part</td><td>Faire-part numérique pour une partie des invités</td></tr>
<tr><td>Tenues</td><td>Location ou seconde main</td></tr>
</tbody></table>
<h2>Gardez une part pour les imprévus</h2>
<p>Un mariage réserve presque toujours des surprises : invités en plus, options oubliées, frais de déplacement. Gardez une réserve, souvent autour de 10 %, pour ne pas dépasser.</p>
<h2>Et les cadeaux ?</h2>
<p>Votre liste de mariage peut aussi aider à équiper la maison après le mariage, sans toucher à votre budget. Voyez <a href="{R}que-mettre-dans-une-liste-de-mariage/">que mettre dans une liste de mariage</a> et notre <a href="{R}checklist/">checklist</a>.</p>
""",
  faq=[("Quel est le poste le plus cher d'un mariage ?", "En général le lieu et la réception (repas, boissons), car ils dépendent du nombre d'invités."),
       ("Comment réduire le budget d'un mariage ?", "Le levier le plus efficace est le nombre d'invités. Viennent ensuite la date (hors saison, en semaine) et les postes de décoration.")])

t(slug='calculateur-liste-de-mariage/',
  title="Combien d'articles dans une liste de mariage ? Calculateur",
  h1="Combien d'articles dans votre liste de mariage ?",
  short="Calculateur de liste",
  desc="Indiquez le nombre d'invités : le calculateur vous dit combien d'articles mettre dans votre liste de mariage et comment les répartir par tranche de prix.",
  emoji='🧮', tint='menthe',
  tool="""<form id="t-liste" class="accf tool-form">
<label>Nombre d'invités<input type="number" id="t-g" min="1" inputmode="numeric" required></label>
<label class="check"><input type="checkbox" id="t-together"> Nous vivons déjà ensemble</label>
<button class="btn" type="submit">Calculer</button>
</form>
<div id="t-out" class="tool-res" hidden aria-live="polite"></div>""",
  body="""
<h2>Comment le calcul fonctionne</h2>
<p>La plupart des invités offrent un cadeau par foyer : un couple fait souvent un cadeau commun. Le calculateur compte donc environ un foyer pour deux invités, puis ajoute une marge pour que les derniers invités aient encore du choix. Si vous vivez déjà ensemble, la liste peut être un peu plus courte.</p>
<h2>La bonne répartition des prix</h2>
<p>Le calculateur répartit les articles en trois tranches : un tiers de petits prix pour les jeunes invités et les collègues, une grosse part de cadeaux à prix moyen, et quelques gros cadeaux à offrir à plusieurs. Plus de détails dans notre guide <a href="{R}liste-de-mariage-petit-budget/">liste de mariage petits prix</a>.</p>
<h2>Remplir la liste</h2>
<p>Une fois le nombre en tête, ouvrez notre <a href="{R}checklist/">checklist par pièce</a> et cochez les articles. Pour des idées, lisez <a href="{R}que-mettre-dans-une-liste-de-mariage/">que mettre dans une liste de mariage</a>, puis créez votre <a href="{R}liste-de-mariage-amazon/">liste de mariage Amazon</a>.</p>
<table><thead><tr><th>Invités</th><th>Articles conseillés (premier logement)</th></tr></thead><tbody>
<tr><td>40</td><td>environ 24</td></tr>
<tr><td>80</td><td>environ 48</td></tr>
<tr><td>120</td><td>environ 72</td></tr>
</tbody></table>
""",
  faq=[("Combien d'articles mettre dans une liste de mariage pour 100 invités ?", "Comptez environ 60 articles pour un premier logement, un peu moins si vous vivez déjà ensemble."),
       ("Faut-il plus d'articles que d'invités ?", "Non, un cadeau est souvent offert par foyer. Prévoyez un peu plus d'articles que de foyers pour laisser du choix.")])
