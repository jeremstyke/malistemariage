# -*- coding: utf-8 -*-
# Pages de longue traîne (requêtes précises, peu concurrentielles)
import html
from content import g, CHECKLIST, PRIO

def _printlist():
    out = '<div class="printlist">'
    for cat, emo, items in CHECKLIST:
        out += '<h3>%s %s</h3><ul>' % (emo, html.escape(cat))
        for n, q, p, t in items:
            out += '<li>☐ %s <small>(%s)</small></li>' % (html.escape(n), PRIO[p])
        out += '</ul>'
    return out + '</div><p><button class="btn ghost" type="button" onclick="window.print()">Imprimer cette liste</button></p>'

PRINTLIST = _printlist()

g("acheter-sur-une-liste-de-mariage-amazon/",
  "Offrir un cadeau sur une liste de mariage Amazon : mode d'emploi",
  "Comment offrir un cadeau sur une liste de mariage Amazon",
  "Vous êtes invité et les mariés ont une liste Amazon ? Comment trouver la liste, choisir un cadeau, le faire livrer et ajouter un message, étape par étape.",
  """
<p>Les mariés vous ont envoyé le lien de leur liste de mariage Amazon et vous n'avez jamais fait ça ? Rassurez-vous, c'est aussi simple qu'une commande classique. Voici la marche à suivre, à envoyer aussi aux grands-parents.</p>
{CTA}
<h2>Étape 1 : ouvrir la bonne liste</h2>
<p>Le plus sûr est d'utiliser le lien envoyé par les mariés (faire-part, site de mariage, message). Si vous ne l'avez pas, demandez-le : c'est plus fiable qu'une recherche par nom, car plusieurs couples peuvent porter le même nom. Voyez aussi notre guide <a href="{R}trouver-une-liste-de-mariage-amazon/">pour trouver une liste de mariage Amazon</a>.</p>
<h2>Étape 2 : choisir un cadeau</h2>
<p>La liste affiche les articles choisis par les mariés, avec leur prix et souvent la quantité souhaitée. Les articles déjà offerts sont indiqués comme achetés. Vous pouvez trier par prix pour trouver un cadeau adapté à votre budget.</p>
<h2>Étape 3 : ajouter au panier depuis la liste</h2>
<p>C'est l'étape la plus importante : cliquez sur le bouton d'ajout au panier <strong>directement dans la liste</strong>. Si vous cherchez le même produit ailleurs sur Amazon, l'achat ne sera pas rattaché à la liste, et l'article restera affiché comme disponible. Un autre invité risque alors de l'offrir aussi.</p>
<h2>Étape 4 : la livraison</h2>
<p>Au moment de payer, vous choisissez où livrer : chez les mariés, si l'option est proposée, ou chez vous pour apporter le cadeau le jour J. Selon les réglages de la liste, l'adresse des mariés n'est pas forcément affichée en entier. Si vous voulez apporter le cadeau à la fête, faites-vous livrer chez vous.</p>
<h2>Étape 5 : le message et l'emballage</h2>
<p>Pensez à ajouter un petit mot pour que les mariés sachent que le cadeau vient de vous. Sans message, ils peuvent avoir du mal à vous remercier. Si l'option cadeau est proposée, elle évite que la facture soit jointe au colis.</p>
<h2>Récapitulatif</h2>
<table><thead><tr><th>Étape</th><th>À faire</th><th>Piège à éviter</th></tr></thead><tbody>
<tr><td>1</td><td>Ouvrir le lien des mariés</td><td>Se tromper de couple</td></tr>
<tr><td>2</td><td>Choisir selon son budget</td><td>Prendre un article déjà offert</td></tr>
<tr><td>3</td><td>Ajouter au panier depuis la liste</td><td>Acheter le produit hors liste</td></tr>
<tr><td>4</td><td>Choisir l'adresse de livraison</td><td>Livrer chez soi par erreur</td></tr>
<tr><td>5</td><td>Ajouter un message</td><td>Oublier de signer</td></tr>
</tbody></table>
<h2>Offrir à plusieurs</h2>
<p>Pour un gros cadeau, une seule personne commande et les autres la remboursent. Signez le message avec tous les prénoms. Pour le montant habituel, voyez notre guide <a href="{R}combien-donner-pour-un-mariage/">combien donner pour un mariage</a>.</p>
<h2>Si l'article est en rupture</h2>
<p>Choisissez un autre article de la liste plutôt qu'un produit ressemblant hors liste. Si vous tenez à cet article, prévenez les mariés : ils pourront le remplacer par un modèle disponible.</p>
""",
  faq=[
    ("Les mariés savent-ils qui a offert le cadeau ?", "Oui si vous ajoutez un message avec votre nom. Pensez-y, sinon ils ne pourront pas vous remercier."),
    ("Faut-il un compte Amazon pour offrir un cadeau sur une liste ?", "Oui, il faut un compte Amazon pour passer commande, comme pour n'importe quel achat."),
    ("Peut-on offrir seulement une partie d'un lot ?", "Si les mariés ont indiqué une quantité (par exemple 12 verres), vous pouvez en offrir une partie. La liste se met à jour avec ce qui reste."),
  ],
  short="Offrir sur une liste Amazon")

g("trouver-une-liste-de-mariage-amazon/",
  "Trouver une liste de mariage Amazon : les 3 méthodes",
  "Comment trouver une liste de mariage Amazon ?",
  "Vous cherchez la liste de mariage Amazon d'un couple ? Lien direct, recherche par nom, liste privée : les 3 méthodes et quoi faire si vous ne la trouvez pas.",
  """
<p>Vous êtes invité à un mariage et vous savez que les mariés ont une liste sur Amazon, mais vous n'avez plus le lien ? Voici comment la retrouver.</p>
{CTA}
<h2>Méthode 1 : le lien des mariés</h2>
<p>C'est la méthode la plus fiable. Regardez le faire-part, le petit carton glissé dedans, le site de mariage ou les messages reçus. Un QR code sur le carton mène souvent directement à la liste.</p>
<h2>Méthode 2 : la recherche par nom</h2>
<p>Sur la page des listes de mariage d'Amazon, une recherche par nom des mariés est en général proposée. Elle ne fonctionne que si la liste est publique. Ajoutez la date du mariage si plusieurs couples portent le même nom.</p>
<h2>Méthode 3 : demander</h2>
<p>Si la liste est privée, seule la personne qui a le lien peut la voir. Demandez simplement le lien aux mariés, à un témoin ou à un proche de la famille. C'est une question très courante, personne ne s'en offusquera.</p>
<table><thead><tr><th>Situation</th><th>Solution</th></tr></thead><tbody>
<tr><td>Lien perdu</td><td>Faire-part, site de mariage, ou demander à un témoin</td></tr>
<tr><td>Liste introuvable par nom</td><td>Elle est sans doute privée : demander le lien</td></tr>
<tr><td>Plusieurs résultats</td><td>Vérifier la date et la ville du mariage</td></tr>
<tr><td>Liste vide</td><td>Tout est offert : choisir un autre cadeau ou une enveloppe</td></tr>
</tbody></table>
<h2>Vous êtes les mariés ?</h2>
<p>Facilitez la vie de vos invités : mettez le lien partout (site, carton, message) et ajoutez un QR code. Nos <a href="{R}message-liste-de-mariage/">textes tout prêts</a> vous aident à l'annoncer. Pour la créer, suivez notre guide <a href="{R}liste-de-mariage-amazon/">liste de mariage Amazon</a>.</p>
<h2>Une fois la liste trouvée</h2>
<p>Suivez notre guide pas à pas pour <a href="{R}acheter-sur-une-liste-de-mariage-amazon/">offrir un cadeau sur la liste</a> sans faire d'erreur.</p>
""",
  faq=[
    ("Pourquoi je ne trouve pas une liste de mariage Amazon par le nom ?", "La liste est sans doute privée. Dans ce cas, elle n'est visible qu'avec le lien : demandez-le aux mariés ou à un proche."),
    ("Peut-on trouver une liste de mariage avec un e-mail ?", "Le plus simple reste le lien partagé par les mariés. Si vous ne l'avez pas, demandez-le-leur directement."),
  ],
  short="Trouver une liste Amazon")

g("modifier-supprimer-liste-de-mariage-amazon/",
  "Modifier ou supprimer sa liste de mariage Amazon",
  "Modifier, masquer ou supprimer sa liste de mariage Amazon",
  "Changer la date, ajouter un cotitulaire, rendre la liste privée, retirer des articles ou la supprimer après le mariage : comment gérer votre liste Amazon.",
  """
<p>Une liste de mariage vit pendant plusieurs mois. Vous voudrez sans doute changer des articles, la date ou les réglages. Voici ce qu'il faut savoir.</p>
{CTA}
<h2>Modifier les articles</h2>
<p>Depuis votre liste, vous pouvez retirer un article, changer la quantité souhaitée ou ajouter une note. Remplacez les articles en rupture par un modèle équivalent : un invité qui tombe sur un produit indisponible risque d'acheter hors liste.</p>
<h2>Modifier les informations</h2>
<p>Les réglages de la liste permettent en général de changer la date du mariage, le nom affiché, l'adresse de livraison et d'ajouter un cotitulaire pour gérer la liste à deux. Vérifiez l'adresse si vous déménagez avant ou après le mariage.</p>
<h2>Rendre la liste privée ou publique</h2>
<p>Une liste publique peut être trouvée par une recherche de vos noms. Une liste privée n'est visible qu'avec son lien. La seconde option convient si vous préférez la partager seulement avec vos invités.</p>
<h2>Après le mariage : garder ou supprimer ?</h2>
<p>Gardez-la au moins un ou deux mois : des invités offrent encore après la fête, et la liste vous sert de mémo pour les <a href="{R}remerciements-mariage/">remerciements</a>. Ensuite, vous pouvez la rendre privée plutôt que la supprimer, pour garder une trace de qui a offert quoi.</p>
<table><thead><tr><th>Besoin</th><th>Action conseillée</th></tr></thead><tbody>
<tr><td>Article en rupture</td><td>Le remplacer par un équivalent</td></tr>
<tr><td>Liste qui se vide</td><td>Ajouter des petits prix</td></tr>
<tr><td>Déménagement</td><td>Mettre à jour l'adresse de livraison</td></tr>
<tr><td>Fin des cadeaux</td><td>Rendre la liste privée</td></tr>
</tbody></table>
<h2>Repartir de zéro</h2>
<p>Vous trouvez votre liste brouillonne ? Reprenez notre <a href="{R}checklist/">checklist par pièce</a>, cochez ce qui compte vraiment et ajustez la liste en une soirée.</p>
""",
  faq=[
    ("Peut-on changer la date du mariage sur la liste Amazon ?", "Oui, depuis les réglages de la liste. Pensez à le faire si la date change, pour ne pas induire vos invités en erreur."),
    ("Faut-il supprimer la liste après le mariage ?", "Ce n'est pas nécessaire. La rendre privée permet de garder une trace des cadeaux reçus."),
  ],
  short="Modifier sa liste Amazon")

g("liste-de-mariage-a-imprimer/",
  "Liste de mariage à imprimer : la checklist gratuite",
  "Liste de mariage à imprimer",
  "Imprimez notre checklist de liste de mariage, pièce par pièce, pour préparer votre liste à deux sur papier ou la donner aux invités qui préfèrent le papier.",
  """
<p>Certains couples aiment préparer leur liste sur papier, un crayon à la main. Et certains invités, souvent les plus âgés, préfèrent une liste imprimée. Voici notre checklist complète, prête à imprimer.</p>
{CTA}
<h2>La checklist à imprimer</h2>
<p>Cochez au crayon ce qui vous fait envie, puis ajoutez les articles à votre liste en ligne. Vous préférez cocher sur écran ? Utilisez notre <a href="{R}checklist/">checklist interactive</a>, qui garde vos choix.</p>
{PRINTLIST}
<h2>Comment l'utiliser à deux</h2>
<p>Imprimez deux exemplaires, cochez chacun de votre côté, puis comparez. Ce que vous avez coché tous les deux va directement dans la liste. Le reste se discute autour d'un café.</p>
<h2>Une version papier pour les invités ?</h2>
<p>Pour les grands-parents qui ne commandent pas en ligne, imprimez la liste de vos articles avec leur prix. Un proche peut ensuite passer la commande pour eux depuis la liste en ligne, pour que l'article soit bien marqué comme offert. Voyez notre guide pour <a href="{R}acheter-sur-une-liste-de-mariage-amazon/">offrir un cadeau sur une liste Amazon</a>.</p>
<table><thead><tr><th>Format</th><th>Pour qui</th><th>Avantage</th></tr></thead><tbody>
<tr><td>Papier</td><td>Préparation à deux, invités âgés</td><td>Pas d'écran, facile à annoter</td></tr>
<tr><td>Checklist en ligne</td><td>Préparation à deux</td><td>Sauvegarde, liens vers les articles</td></tr>
<tr><td>Liste Amazon</td><td>Tous les invités</td><td>Achat direct, pas de doublons</td></tr>
</tbody></table>
""",
  faq=[
    ("La liste imprimée suffit-elle pour les invités ?", "Elle aide à choisir, mais pour éviter les doublons, l'achat doit passer par votre liste en ligne. Un proche peut commander pour les invités qui ne sont pas à l'aise avec Internet."),
  ],
  short="Liste à imprimer")

g("liste-de-mariage-mariage-civil/",
  "Liste de mariage pour un mariage civil ou en petit comité",
  "Liste de mariage pour un mariage civil ou en petit comité",
  "Mariage à la mairie, petit comité, sans grande fête : faut-il une liste de mariage ? Combien d'articles, quels cadeaux et comment l'annoncer simplement.",
  """
<p>Vous vous mariez à la mairie, avec un repas entre proches ? Une liste de mariage reste utile : vos invités voudront vous offrir quelque chose et préfèrent savoir quoi.</p>
{CTA}
<h2>Faut-il une liste pour un petit mariage ?</h2>
<p>Ce n'est pas obligatoire, mais c'est pratique. Même avec 15 invités, vous éviterez les doublons et les cadeaux inutiles. Une liste courte suffit.</p>
<h2>Combien d'articles ?</h2>
<table><thead><tr><th>Nombre d'invités</th><th>Articles conseillés</th></tr></thead><tbody>
<tr><td>Moins de 20</td><td>15 à 20</td></tr>
<tr><td>20 à 40</td><td>25 à 35</td></tr>
<tr><td>40 à 60</td><td>35 à 50</td></tr>
</tbody></table>
<h2>Quels cadeaux privilégier ?</h2>
<p>En petit comité, les invités sont souvent des proches, prêts à offrir des cadeaux plus importants ou à se regrouper. Mélangez quelques beaux cadeaux de groupe (cocotte, robot, aspirateur) et des articles à prix moyen. Inspirez-vous de notre <a href="{R}que-mettre-dans-une-liste-de-mariage/">liste d'idées</a>.</p>
<h2>Comment l'annoncer ?</h2>
<p>Pas besoin de carton imprimé : un message à chacun avec le lien suffit. « On se dit oui à la mairie le 14 juin, entourés des gens qu'on aime. Si vous voulez nous faire plaisir, voici notre petite liste. » D'autres textes dans nos <a href="{R}message-liste-de-mariage/">messages tout prêts</a>.</p>
<h2>Et la grande fête plus tard ?</h2>
<p>Si vous prévoyez une fête l'année suivante, vous pouvez garder la même liste et la partager à nouveau avec les nouveaux invités. Mettez-la à jour avant, en ajoutant des articles.</p>
""",
  faq=[
    ("Une liste de mariage pour un mariage à la mairie, ça se fait ?", "Oui, de plus en plus. Les invités veulent offrir un cadeau et préfèrent savoir ce qui vous fera plaisir."),
  ],
  short="Mariage civil ou petit comité")

g("liste-de-mariage-et-bebe-en-route/",
  "Se marier enceinte : liste de mariage ou liste de naissance ?",
  "Mariage et bébé en route : quelle liste faire ?",
  "Vous vous mariez et un bébé arrive bientôt ? Faut-il une liste de mariage, une liste de naissance ou les deux, et comment les présenter aux invités.",
  """
<p>Vous vous mariez et un bébé est en route ? Félicitations deux fois ! Une question pratique arrive vite : que demander aux invités ? Voici comment s'organiser sans gêner personne.</p>
{CTA}
<h2>Les trois options</h2>
<table><thead><tr><th>Option</th><th>Avantages</th><th>Limites</th></tr></thead><tbody>
<tr><td>Liste de mariage seule</td><td>Simple, centrée sur le jour J</td><td>Les besoins du bébé arrivent juste après</td></tr>
<tr><td>Liste de naissance seule</td><td>Très utile pour la suite</td><td>Moins dans l'esprit du mariage</td></tr>
<tr><td>Les deux, séparées</td><td>Chacun choisit</td><td>Deux liens à partager</td></tr>
</tbody></table>
<h2>Notre conseil : deux listes, deux moments</h2>
<p>Gardez la liste de mariage pour le mariage : la maison, le voyage, vos projets à deux. Partagez la liste de naissance plus tard, quelques semaines avant l'arrivée du bébé ou à l'annonce de la naissance. Vos proches seront ravis d'offrir une deuxième fois, et chaque événement garde sa place.</p>
<h2>Si le mariage est très proche de la naissance</h2>
<p>Si bébé arrive quelques semaines après le mariage, vous pouvez mentionner les deux listes dans le même message, en laissant le choix : « Pour ceux qui le souhaitent, notre liste de mariage est ici, et celle de notre futur bébé là. » Évitez de mélanger les articles dans une seule liste : c'est plus confus pour les invités.</p>
<h2>Préparer la liste de naissance</h2>
<p>Pour la liste de bébé, utilisez notre site jumeau <a href="https://malistebebe.fr/">Ma liste bébé</a> : une checklist complète pièce par pièce, avec le même compte que sur ce site.</p>
<h2>Adapter la liste de mariage</h2>
<p>Privilégiez les articles qui serviront avec un bébé : un lave-vaisselle ou un robot cuiseur, un aspirateur sans fil, une machine à café, du linge de lit. Pour le voyage de noces, pensez à des bagages pratiques.</p>
""",
  faq=[
    ("Peut-on faire une seule liste pour le mariage et le bébé ?", "C'est possible, mais deux listes séparées sont plus claires pour les invités. Partagez la liste de naissance plutôt à l'approche de l'arrivée du bébé."),
  ],
  short="Mariage et bébé en route")

g("faut-il-faire-une-liste-de-mariage/",
  "Faut-il faire une liste de mariage ? Pour et contre",
  "Faut-il faire une liste de mariage ?",
  "Liste de mariage, cagnotte, enveloppe ou rien du tout : les avantages et les inconvénients de chaque option, et comment décider selon votre situation.",
  """
<p>Certains couples hésitent : demander des cadeaux leur semble gênant, ou ils ont déjà tout. Pourtant, la liste rend surtout service aux invités. Voici les arguments pour vous aider à décider.</p>
{CTA}
<h2>Les arguments pour</h2>
<ul>
<li><strong>Les invités savent quoi offrir</strong> : beaucoup cherchent une idée et sont soulagés d'avoir une liste.</li>
<li><strong>Pas de doublons</strong> : chaque article offert disparaît de la liste.</li>
<li><strong>Des cadeaux utiles</strong> : vous recevez ce dont vous avez vraiment besoin.</li>
<li><strong>Tous les budgets</strong> : chacun participe selon ses moyens.</li>
</ul>
<h2>Les arguments contre</h2>
<ul>
<li><strong>La gêne</strong> : certains couples n'aiment pas « demander ».</li>
<li><strong>Le temps</strong> : remplir une liste prend une soirée ou deux.</li>
<li><strong>Le côté matériel</strong>, si vous avez déjà tout.</li>
</ul>
<h2>Comment décider</h2>
<table><thead><tr><th>Votre situation</th><th>Notre conseil</th></tr></thead><tbody>
<tr><td>Premier logement</td><td>Liste de cadeaux</td></tr>
<tr><td>Couple installé</td><td>Petite liste et cagnotte</td></tr>
<tr><td>Grand voyage prévu</td><td>Cagnotte et articles de voyage</td></tr>
<tr><td>Vous ne voulez rien</td><td>Le dire clairement, ou proposer un don à une association</td></tr>
</tbody></table>
<h2>Gagner du temps</h2>
<p>Avec notre <a href="{R}checklist/">checklist par pièce</a>, une liste se prépare en une soirée. Pour savoir quoi y mettre, lisez <a href="{R}que-mettre-dans-une-liste-de-mariage/">que mettre dans une liste de mariage</a>, et pour l'annoncer sans gêne, nos <a href="{R}message-liste-de-mariage/">textes tout prêts</a>.</p>
""",
  faq=[
    ("Est-ce impoli de ne pas faire de liste de mariage ?", "Non. Mais vos invités voudront souvent offrir quelque chose : précisez alors ce qui vous ferait plaisir, même simplement."),
    ("Est-ce impoli de faire une liste de mariage ?", "Non, c'est une pratique courante et appréciée des invités, à condition de l'annoncer avec tact."),
  ],
  short="Faut-il une liste ?")
