# -*- coding: utf-8 -*-
# Contenu du site Ma liste mariage

# Checklist : (categorie, emoji, [(article, recherche Amazon, priorite, conseil)])
# priorite : 1 = essentiel, 2 = utile, 3 = coup de coeur
CHECKLIST = [
  ("Cuisine", "🍳", [
    ("Batterie de casseroles", "batterie casseroles induction", 1, "Vérifiez qu'elle est compatible avec votre plaque (induction, gaz, vitrocéramique)."),
    ("Poêles antiadhésives (x2)", "poele antiadhesive lot", 1, "Une de 24 cm pour les oeufs, une de 28 cm pour le reste."),
    ("Cocotte en fonte", "cocotte fonte 24 cm", 1, "Le cadeau qui dure 30 ans : idéal pour un cadeau de groupe."),
    ("Couteaux de cuisine", "bloc couteaux cuisine", 1, "Mieux vaut 3 bons couteaux qu'un bloc de 12 médiocres."),
    ("Planches à découper", "planche a decouper bois", 1, "Une en bois pour le pain, une lavable au lave-vaisselle pour la viande."),
    ("Robot pâtissier", "robot patissier", 2, "Le grand classique des listes : parfait pour une participation à plusieurs."),
    ("Robot multifonction ou blender", "blender", 2, "Pour les soupes, smoothies et sauces."),
    ("Machine à café", "machine a cafe grain", 2, "À grain pour les amateurs, à capsules pour la simplicité."),
    ("Bouilloire", "bouilloire", 2, "Un modèle avec réglage de température si vous buvez du thé."),
    ("Grille-pain", "grille pain", 3, "Petit prix, facile à offrir pour un invité."),
    ("Ustensiles de cuisine", "ustensiles cuisine silicone set", 1, "Spatules, louche, fouet : on en manque toujours."),
    ("Moules à gâteau", "moule a gateau set", 3, "Un joli cadeau pour les cousins et les amis."),
  ]),
  ("Arts de la table", "🍽️", [
    ("Service de vaisselle (12 couverts)", "service vaisselle 12 personnes", 1, "Prévoyez 12 couverts : c'est la taille des grandes tablées de famille."),
    ("Ménagère de couverts", "menagere couverts 12 personnes", 1, "En inox 18/10, elle passe au lave-vaisselle sans s'abîmer."),
    ("Verres à eau et à vin", "verres a vin lot", 1, "Ajoutez quelques verres de plus : ils cassent plus vite que les assiettes."),
    ("Flûtes à champagne", "flutes champagne", 2, "Un clin d'oeil au jour J."),
    ("Plat de service et saladiers", "plat de service porcelaine", 2, "Pour recevoir les deux familles."),
    ("Nappe et serviettes en lin", "nappe lin", 3, "Le lin lavé ne se repasse pas."),
    ("Carafe", "carafe en verre", 3, "Petit cadeau élégant à moins de 30 €."),
  ]),
  ("Linge de maison", "🛏️", [
    ("Parure de lit", "parure de lit percale", 1, "En percale ou en lin, à la bonne taille de couette."),
    ("Couette de qualité", "couette 240x220", 1, "Une couette 4 saisons évite d'en acheter deux."),
    ("Oreillers (x2)", "oreiller", 1, "Ferme ou moelleux : chacun choisit le sien."),
    ("Draps housses (x2)", "drap housse 160x200", 1, "Vérifiez la profondeur du bonnet selon votre matelas."),
    ("Serviettes de bain", "serviettes de bain lot coton", 1, "Coton épais d'au moins 500 g/m²."),
    ("Plaid", "plaid", 3, "Pour le canapé et les soirées d'hiver."),
  ]),
  ("Salle de bain", "🛁", [
    ("Peignoirs assortis", "peignoir couple", 2, "Un cadeau qui plaît souvent aux témoins."),
    ("Tapis de bain", "tapis de bain", 2, "Antidérapant et lavable en machine."),
    ("Pèse-personne", "pese personne", 3, "Petit cadeau pratique."),
    ("Diffuseur d'huiles essentielles", "diffuseur huiles essentielles", 3, "Pour une ambiance douce à la maison."),
  ]),
  ("Maison et entretien", "🏠", [
    ("Aspirateur balai sans fil", "aspirateur balai sans fil", 1, "Le cadeau de groupe le plus utile au quotidien."),
    ("Robot aspirateur", "robot aspirateur", 2, "Pour ne plus jamais passer l'aspirateur le samedi."),
    ("Fer ou centrale vapeur", "centrale vapeur", 2, "Une défroisseuse suffit si vous repassez peu."),
    ("Boîte à outils", "boite a outils complete", 2, "Indispensable dans un premier logement."),
    ("Lampes et luminaires", "lampe a poser", 3, "Pour personnaliser le salon."),
    ("Cadre photo pour le mariage", "cadre photo mariage", 3, "Pour accrocher la plus belle photo du jour J."),
    ("Album photo de mariage", "album photo mariage", 2, "Vous l'ouvrirez encore dans 20 ans."),
  ]),
  ("Voyage de noces", "✈️", [
    ("Valises cabine (x2)", "valise cabine", 1, "Rigides, légères, aux dimensions des compagnies low cost."),
    ("Grande valise", "valise grande taille", 2, "Pour un voyage de plus d'une semaine."),
    ("Trousses de toilette", "trousse de toilette", 3, "Petit cadeau facile."),
    ("Adaptateur de voyage universel", "adaptateur prise universel", 2, "Indispensable hors d'Europe."),
    ("Batterie externe", "batterie externe", 2, "Pour ne jamais tomber à court de photos."),
    ("Appareil photo instantané", "appareil photo instantane", 3, "Les photos du voyage tout de suite en main."),
    ("Guide de voyage", "guide de voyage", 3, "Le cadeau à 15 € des invités qui veulent participer."),
  ]),
  ("Loisirs à deux", "🎲", [
    ("Barbecue ou plancha", "plancha electrique", 2, "Parfait pour les beaux jours avec les amis."),
    ("Jeux de société pour deux", "jeu de societe 2 joueurs", 3, "Petit prix, grandes soirées."),
    ("Machine à raclette ou fondue", "appareil raclette", 2, "Un classique des dîners d'hiver."),
    ("Enceinte Bluetooth", "enceinte bluetooth", 3, "Pour la musique à la maison et en voyage."),
    ("Vélo électrique ou équipement sport", "velo electrique", 3, "Un gros cadeau de groupe pour les couples sportifs."),
    ("Kit de dégustation de vin", "coffret degustation vin", 3, "Pour les amateurs."),
  ]),
]

PRIO = {1: "Essentiel", 2: "Utile", 3: "Coup de cœur"}

GUIDES = []

def g(slug, title, h1, desc, body, faq=None, short=None):
    GUIDES.append(dict(slug=slug, title=title, h1=h1, desc=desc, body=body, faq=faq or [], short=short or h1))

g("liste-de-mariage-amazon/",
  "Liste de mariage Amazon : comment ça marche ? (2026)",
  "Liste de mariage Amazon : comment ça marche ?",
  "Création, partage, livraison, cagnotte et limites : le guide complet de la liste de mariage Amazon, étape par étape, pour la créer en 10 minutes.",
  """
<p>La liste de mariage Amazon est gratuite et se crée en quelques minutes avec un compte Amazon. Vous ajoutez les articles qui vous font envie, vous partagez le lien, et vos invités achètent directement. Chaque article offert est marqué comme acheté : fini les trois grille-pain.</p>
{CTA}
<h2>Pourquoi choisir une liste Amazon ?</h2>
<p>Le premier avantage, c'est le <strong>catalogue</strong> : cuisine, linge, électroménager, bagages, high-tech, livres. Vous trouvez tout au même endroit, à tous les prix, du petit cadeau à 15 € au robot pâtissier à 500 €. Les invités n'ont pas besoin d'aller dans un magasin précis : ils commandent depuis leur canapé.</p>
<p>Le deuxième avantage, c'est la <strong>simplicité pour les invités</strong>. La plupart ont déjà un compte Amazon, connaissent le fonctionnement et peuvent faire livrer le cadeau chez vous en deux clics. Pour les proches qui habitent loin, c'est souvent la solution la plus confortable.</p>
<p>Enfin, la liste est <strong>modifiable à tout moment</strong> : vous ajoutez, retirez ou remplacez des articles quand vous voulez, même après le mariage.</p>
<h2>Créer sa liste en 5 étapes</h2>
<ol>
<li><strong>Ouvrez la page liste de mariage</strong> d'Amazon et connectez-vous avec votre compte.</li>
<li><strong>Renseignez les informations</strong> : vos deux prénoms, la date du mariage, l'adresse de livraison et éventuellement un cotitulaire pour gérer la liste à deux.</li>
<li><strong>Ajoutez les articles</strong> avec le bouton « Ajouter à la liste de mariage » sur chaque fiche produit. Notre <a href="{R}checklist/">checklist par pièce</a> vous évite d'oublier l'essentiel.</li>
<li><strong>Réglez la confidentialité</strong> : liste publique (trouvable par vos noms) ou accessible seulement avec le lien.</li>
<li><strong>Partagez le lien</strong> sur votre site de mariage, par e-mail ou par message. On vous propose des <a href="{R}message-liste-de-mariage/">textes tout prêts</a>.</li>
</ol>
<h2>Combien d'articles mettre ?</h2>
<p>Une bonne règle : prévoyez <strong>un peu plus d'articles que d'invités</strong> (ou de couples d'invités), pour que les derniers aient encore du choix. Pour 80 invités, visez 50 à 70 articles. Répartissez les prix :</p>
<ul>
<li>un tiers d'articles <strong>à moins de 40 €</strong>, pour les amis et les jeunes invités ;</li>
<li>un tiers <strong>entre 40 et 120 €</strong>, le budget le plus courant ;</li>
<li>un tiers de <strong>gros cadeaux</strong> que plusieurs personnes peuvent offrir ensemble.</li>
</ul>
<h2>La livraison des cadeaux</h2>
<p>Les invités choisissent de faire livrer chez vous ou chez eux. Si vous ne voulez pas recevoir trente colis la semaine du mariage, précisez dans votre message que la livraison peut se faire à votre adresse après la date. Vérifiez dans les réglages de la liste quelles informations d'adresse sont visibles par les invités avant de la partager.</p>
<h2>Les limites de la liste Amazon</h2>
<p>Amazon ne convient pas à tout le monde. Il n'y a pas de cagnotte libre pour financer un voyage de noces comme sur certaines plateformes dédiées, les articles de petits créateurs sont rares, et certains invités préfèrent offrir de l'argent. Beaucoup de couples combinent donc une liste Amazon pour la maison et une <a href="{R}liste-de-mariage-ou-cagnotte/">cagnotte</a> pour le voyage.</p>
<h2>Nos conseils pour une liste réussie</h2>
<ul>
<li><strong>Créez-la tôt</strong>, en même temps que l'envoi des faire-part, soit 3 à 4 mois avant le jour J.</li>
<li><strong>Choisissez des articles précis</strong> (taille, couleur, modèle) pour éviter les échanges.</li>
<li><strong>Mettez les gros cadeaux en avant</strong> et indiquez qu'ils peuvent être offerts à plusieurs.</li>
<li><strong>Revenez sur la liste chaque mois</strong> pour ajouter des articles si elle se vide vite.</li>
<li><strong>Notez qui a offert quoi</strong> au fur et à mesure pour vos <a href="{R}remerciements-mariage/">remerciements</a>.</li>
</ul>
""",
  faq=[
    ("La liste de mariage Amazon est-elle gratuite ?", "Oui. La création, la gestion et le partage sont gratuits. L'abonnement Prime n'est pas nécessaire pour créer une liste."),
    ("Comment trouver la liste de mariage Amazon de quelqu'un ?", "Le plus simple est de demander le lien aux mariés. Si la liste est publique, vous pouvez aussi la chercher par le nom des mariés sur la page liste de mariage d'Amazon."),
    ("Peut-on gérer la liste à deux ?", "Oui, vous pouvez ajouter un cotitulaire pour que les deux mariés puissent modifier la liste."),
    ("Les invités voient-ils qui a offert quoi ?", "Non, les autres invités voient seulement que l'article est acheté. Les mariés, eux, peuvent retrouver les messages des invités."),
  ],
  short="Liste de mariage Amazon : le guide")

g("que-mettre-dans-une-liste-de-mariage/",
  "Que mettre dans une liste de mariage ? 60 idées (2026)",
  "Que mettre dans une liste de mariage ?",
  "Cuisine, linge, maison, voyage, loisirs : 60 idées pour remplir votre liste de mariage, avec la bonne répartition des prix et les erreurs à éviter.",
  """
<p>Une liste de mariage réussie mélange trois choses : ce dont vous avez vraiment besoin, des cadeaux à tous les prix, et quelques coups de cœur qui vous ressemblent. Voici comment la remplir sans y passer vos soirées.</p>
{CTA}
<h2>Commencez par faire le tour de la maison</h2>
<p>Prenez 20 minutes, pièce par pièce, et notez ce qui est usé, dépareillé ou manquant. La poêle qui accroche, les serviettes qui datent de vos années étudiantes, la cafetière qui fuit. C'est exactement ce que vos invités seront ravis de remplacer. Notre <a href="{R}checklist/">checklist interactive</a> suit ce même ordre.</p>
<h2>La cuisine, pilier de la liste</h2>
<p>C'est la pièce où les cadeaux durent le plus longtemps. Les incontournables :</p>
<ul>
<li>une <strong>batterie de casseroles</strong> compatible avec votre plaque ;</li>
<li>une <strong>cocotte en fonte</strong>, le cadeau qu'on garde toute une vie ;</li>
<li>de <strong>bons couteaux</strong> et une planche en bois ;</li>
<li>un <strong>robot pâtissier</strong> ou un blender, parfaits pour un cadeau de groupe ;</li>
<li>une <strong>machine à café</strong> et une bouilloire.</li>
</ul>
<h2>Les arts de la table</h2>
<p>Un service de vaisselle pour <strong>12 personnes</strong>, une ménagère, des verres à eau et à vin, quelques plats de service. C'est le moment d'avoir enfin une vaisselle assortie pour recevoir les deux familles. Pensez à des pièces faciles à racheter à l'unité si une assiette casse.</p>
<h2>Le linge de maison</h2>
<p>Parure de lit, couette, oreillers, serviettes de bain épaisses : des cadeaux à prix moyens, très pratiques pour les invités qui ne savent pas quoi offrir. Indiquez bien les tailles (160x200, 140x190) dans la description.</p>
<h2>La maison et l'entretien</h2>
<p>Moins romantique mais tellement utile : un aspirateur balai sans fil, un robot aspirateur, une centrale vapeur, une boîte à outils. Ce sont souvent les cadeaux les plus appréciés au quotidien.</p>
<h2>Le voyage de noces</h2>
<p>Valises cabine, adaptateur universel, batterie externe, appareil photo instantané, guide du pays. Ces articles permettent aux invités de participer à votre voyage, même avec une liste matérielle.</p>
<h2>Les coups de cœur</h2>
<p>Ajoutez quelques cadeaux qui vous ressemblent : une plancha, une machine à raclette, des jeux de société, un vélo électrique pour les couples sportifs. Ce sont ceux dont vous parlerez encore dans dix ans.</p>
<h2>La bonne répartition des prix</h2>
<table><thead><tr><th>Tranche</th><th>Part de la liste</th><th>Exemples</th></tr></thead><tbody>
<tr><td>Moins de 40 €</td><td>30 %</td><td>Carafe, ustensiles, jeux, guide de voyage</td></tr>
<tr><td>40 à 120 €</td><td>40 %</td><td>Linge, poêles, verres, valise cabine</td></tr>
<tr><td>Plus de 120 €</td><td>30 %</td><td>Robot, cocotte, aspirateur, vaisselle</td></tr>
</tbody></table>
<h2>Les erreurs à éviter</h2>
<ul>
<li><strong>Une liste trop courte</strong> : les derniers invités n'ont plus rien à offrir.</li>
<li><strong>Uniquement des gros cadeaux</strong> : les jeunes invités se sentent mal à l'aise.</li>
<li><strong>Des articles vagues</strong> (« une poêle ») qui obligent à deviner.</li>
<li><strong>Oublier de mettre la liste à jour</strong> quand elle se vide.</li>
</ul>
""",
  faq=[
    ("Combien d'articles mettre dans une liste de mariage ?", "Un peu plus que le nombre de foyers invités. Pour 80 invités, 50 à 70 articles laissent du choix à tout le monde."),
    ("Peut-on mettre des cadeaux chers dans une liste de mariage ?", "Oui, à condition d'avoir aussi des petits prix. Les gros cadeaux sont souvent offerts à plusieurs, par les témoins ou les collègues."),
    ("Que mettre dans une liste de mariage quand on a déjà tout ?", "Misez sur le renouvellement (vaisselle assortie, linge de qualité), le voyage de noces et les expériences. On vous donne des idées dans notre guide dédié."),
  ],
  short="Que mettre dans sa liste ?")

g("liste-de-mariage-quand-on-vit-deja-ensemble/",
  "Liste de mariage quand on vit déjà ensemble : 40 idées",
  "Liste de mariage quand on vit déjà ensemble",
  "Vous avez déjà la vaisselle et l'aspirateur ? Idées de liste de mariage pour les couples installés : remplacer, monter en gamme, voyager et partager.",
  """
<p>Aujourd'hui, la plupart des couples vivent ensemble depuis des années quand ils se marient. Le grille-pain est là, le canapé aussi. Faut-il pour autant renoncer à la liste ? Non : il suffit de changer d'angle.</p>
{CTA}
<h2>Remplacer ce qui est usé</h2>
<p>Votre vaisselle dépareillée, vos poêles rayées, vos draps délavés : la liste est l'occasion de passer à du durable. Une vaisselle assortie pour 12, une batterie de casseroles en inox, du linge en lin. Vos invités offrent quelque chose de concret et vous profitez d'une maison renouvelée.</p>
<h2>Monter en gamme</h2>
<p>Vous avez une cafetière à filtre ? Proposez une machine à grain. Un vieil aspirateur traîneau ? Un aspirateur balai sans fil. Ce sont les achats que vous repoussez depuis des années parce qu'ils coûtent cher : parfaits pour un cadeau de groupe.</p>
<h2>Penser au voyage de noces</h2>
<p>Valises, adaptateurs, appareil photo, guide du pays, sac de voyage. Et si vous préférez de l'argent pour le voyage lui-même, complétez avec une <a href="{R}liste-de-mariage-ou-cagnotte/">cagnotte</a>.</p>
<h2>Les projets à venir</h2>
<p>Un futur jardin (outils, plancha, salon de jardin), un futur bébé, un déménagement prévu : la liste peut préparer la suite. Certains couples ajoutent des articles pour leur prochaine maison.</p>
<h2>Les loisirs à deux</h2>
<ul>
<li>jeux de société pour deux ;</li>
<li>équipement de randonnée ou de vélo ;</li>
<li>coffret de dégustation de vin ou de bières ;</li>
<li>livres de cuisine du monde ;</li>
<li>enceinte et platine vinyle.</li>
</ul>
<h2>Comment l'annoncer aux invités ?</h2>
<p>Soyez honnêtes, avec humour : « On a déjà un grille-pain, promis. Si vous voulez nous faire plaisir, on a préparé une petite liste pour renouveler ce qui a vécu et préparer notre voyage. » Retrouvez d'autres formulations dans nos <a href="{R}message-liste-de-mariage/">messages tout prêts</a>.</p>
""",
  faq=[
    ("Est-ce mal vu de faire une liste quand on vit déjà ensemble ?", "Non, c'est devenu la norme. La liste aide surtout vos invités, qui cherchent quoi offrir et préfèrent un cadeau utile."),
    ("Que mettre dans sa liste quand on a déjà tout ?", "Le renouvellement de l'existant en mieux, le voyage de noces, les loisirs à deux et les projets à venir."),
  ],
  short="Quand on vit déjà ensemble")

g("liste-de-mariage-originale/",
  "Liste de mariage originale : 30 idées qui sortent du lot",
  "Liste de mariage originale : 30 idées",
  "Des idées de liste de mariage originale et utiles : expériences, voyage, loisirs, cuisine du monde, déco et cadeaux qui vous ressemblent.",
  """
<p>Une liste originale n'est pas une liste remplie de gadgets. C'est une liste qui raconte qui vous êtes : vos passions, vos projets, votre façon de recevoir.</p>
{CTA}
<h2>Pour les couples gourmands</h2>
<ul>
<li>un four à pizza d'extérieur ;</li>
<li>une machine à pâtes ;</li>
<li>un fumoir ou un barbecue kamado ;</li>
<li>un set à sushi et des livres de cuisine japonaise ;</li>
<li>une yaourtière et une machine à pain.</li>
</ul>
<h2>Pour les voyageurs</h2>
<ul>
<li>des valises assorties ;</li>
<li>une carte du monde à gratter ;</li>
<li>un appareil photo instantané et ses recharges ;</li>
<li>une tente et des sacs de couchage pour les escapades.</li>
</ul>
<h2>Pour les couples casaniers</h2>
<ul>
<li>un vidéoprojecteur et un écran ;</li>
<li>une collection de jeux de société ;</li>
<li>une platine vinyle ;</li>
<li>un grand plaid et des coussins de sol.</li>
</ul>
<h2>Pour les sportifs</h2>
<p>Vélos électriques, kayak gonflable, paddle, matériel de randonnée : de gros cadeaux de groupe que vos amis adoreront offrir ensemble.</p>
<h2>Pour la maison</h2>
<p>Une belle horloge, une lampe design, un cadre pour la photo du mariage, un album à remplir. Des objets qui restent visibles et rappellent le jour J.</p>
<h2>Gardez quelques classiques</h2>
<p>Même une liste originale doit garder des cadeaux simples à offrir. Les grands-parents seront plus à l'aise avec une parure de lit qu'avec un kayak. Mélangez les deux grâce à notre <a href="{R}checklist/">checklist</a>.</p>
""",
  faq=[
    ("Une liste originale plaît-elle aux invités ?", "Oui si elle reste variée. Gardez des classiques pour les invités plus traditionnels."),
  ],
  short="Liste de mariage originale")

g("liste-de-mariage-petit-budget/",
  "Liste de mariage petits prix : 40 idées à moins de 50 €",
  "Liste de mariage : 40 idées à moins de 50 €",
  "Des idées de cadeaux à moins de 30 € et moins de 50 € pour votre liste de mariage, pour que tous vos invités puissent participer sans se ruiner.",
  """
<p>Tous vos invités n'ont pas le même budget. Les étudiants, les jeunes cousins ou les amis qui enchaînent les mariages cet été apprécient les petits prix. Une bonne liste en propose au moins un tiers.</p>
{CTA}
<h2>Moins de 30 €</h2>
<ul>
<li>une carafe en verre ;</li>
<li>un set d'ustensiles en silicone ;</li>
<li>des moules à gâteau ;</li>
<li>un jeu de société pour deux ;</li>
<li>un guide de voyage ;</li>
<li>une trousse de toilette ;</li>
<li>un adaptateur de voyage universel ;</li>
<li>des torchons en lin ;</li>
<li>un cadre photo pour le mariage.</li>
</ul>
<h2>De 30 à 50 €</h2>
<ul>
<li>une poêle de qualité ;</li>
<li>des verres à vin ;</li>
<li>une bouilloire ;</li>
<li>un grille-pain ;</li>
<li>des serviettes de bain épaisses ;</li>
<li>une batterie externe ;</li>
<li>un tapis de bain ;</li>
<li>un plaid.</li>
</ul>
<h2>Proposer la participation</h2>
<p>Pour les gros cadeaux, indiquez dans votre message que les invités peuvent s'associer. Un robot pâtissier à 400 € devient accessible à 8 amis qui mettent 50 € chacun.</p>
<h2>Et si votre propre budget est serré ?</h2>
<p>Une liste ne coûte rien à créer. Elle vous permet même d'équiper la maison sans dépenser après un mariage qui a déjà coûté cher. Concentrez-vous sur l'essentiel de notre <a href="{R}checklist/">checklist</a>, filtre « Essentiel ».</p>
""",
  faq=[
    ("Combien de petits prix mettre dans une liste de mariage ?", "Environ un tiers de la liste, pour que chaque invité trouve un cadeau à son budget."),
  ],
  short="Liste à petits prix")

g("liste-de-mariage-ou-cagnotte/",
  "Liste de mariage ou cagnotte : que choisir ?",
  "Liste de mariage ou cagnotte : que choisir ?",
  "Liste de cadeaux, cagnotte en ligne ou urne le jour J ? Avantages, inconvénients, frais et conseils pour choisir la bonne formule pour votre mariage.",
  """
<p>La question revient dans presque tous les mariages : faut-il une liste de cadeaux ou une cagnotte ? La réponse dépend de vos besoins et de vos invités.</p>
{CTA}
<h2>La liste de cadeaux</h2>
<p><strong>Points forts</strong> : les invités savent exactement quoi offrir, le cadeau est concret et durable, pas de frais. Les invités plus âgés y sont souvent plus à l'aise qu'avec un virement.</p>
<p><strong>Limites</strong> : moins adaptée si vous avez déjà tout, et les articles restent fixés à l'avance.</p>
<h2>La cagnotte en ligne</h2>
<p><strong>Points forts</strong> : flexible, idéale pour financer un voyage de noces ou un projet (travaux, achat immobilier).</p>
<p><strong>Limites</strong> : certaines plateformes prennent des frais, et une partie des invités trouve que donner de l'argent manque de personnalité.</p>
<h2>L'urne le jour J</h2>
<p>Encore très répandue en France. Simple, mais attention à la sécurité : confiez-la à un témoin et ne la laissez jamais sans surveillance.</p>
<h2>La solution préférée des couples : les deux</h2>
<p>Beaucoup de couples combinent une <a href="{R}liste-de-mariage-amazon/">liste de cadeaux</a> pour la maison et une cagnotte pour le voyage. Chaque invité choisit ce qui lui convient. Présentez les deux dans le même message pour ne pas multiplier les liens.</p>
<h2>Notre conseil</h2>
<table><thead><tr><th>Votre situation</th><th>Notre conseil</th></tr></thead><tbody>
<tr><td>Premier logement à équiper</td><td>Liste de cadeaux</td></tr>
<tr><td>Vous avez déjà tout</td><td>Cagnotte et petite liste</td></tr>
<tr><td>Grand voyage de noces</td><td>Cagnotte et liste voyage</td></tr>
<tr><td>Invités de tous âges</td><td>Les deux</td></tr>
</tbody></table>
""",
  faq=[
    ("Est-ce impoli de demander de l'argent pour son mariage ?", "Non, c'est devenu courant. Expliquez simplement le projet financé, par exemple le voyage de noces."),
    ("Peut-on avoir une liste et une cagnotte ?", "Oui, c'est même la formule la plus répandue. Chaque invité choisit ce qu'il préfère."),
  ],
  short="Liste ou cagnotte ?")

g("quand-faire-sa-liste-de-mariage/",
  "Quand faire sa liste de mariage ? Le bon calendrier",
  "Quand faire sa liste de mariage ?",
  "Combien de temps avant le mariage créer sa liste, quand l'envoyer aux invités et jusqu'à quand la garder ouverte : le calendrier complet.",
  """
<p>Trop tôt, vos invités oublient. Trop tard, ils ont déjà acheté autre chose. Voici le bon calendrier.</p>
{CTA}
<h2>6 mois avant : commencez à réfléchir</h2>
<p>Faites le tour de la maison, discutez de vos envies et de vos projets (voyage, travaux). Commencez à cocher notre <a href="{R}checklist/">checklist</a>.</p>
<h2>4 mois avant : créez la liste</h2>
<p>Créez la liste en même temps que vous préparez les faire-part. Elle doit être prête quand les premiers invités vous demandent quoi offrir, souvent dès la réception du faire-part.</p>
<h2>3 mois avant : partagez-la</h2>
<p>Ajoutez le lien sur votre site de mariage ou sur un petit carton glissé dans le faire-part. Évitez de l'imprimer en gros sur le faire-part lui-même. Voir nos <a href="{R}message-liste-de-mariage/">formulations</a>.</p>
<h2>1 mois avant : vérifiez</h2>
<p>Regardez ce qui reste. Si la liste se vide, ajoutez des articles à petits prix pour les invités tardifs.</p>
<h2>Après le mariage</h2>
<p>Gardez la liste ouverte 1 à 2 mois : beaucoup d'invités offrent leur cadeau après la fête. Puis rédigez vos <a href="{R}remerciements-mariage/">remerciements</a>.</p>
""",
  faq=[
    ("Combien de temps avant le mariage faire sa liste ?", "Idéalement 3 à 4 mois avant, en même temps que l'envoi des faire-part."),
    ("Jusqu'à quand garder la liste ouverte ?", "1 à 2 mois après le mariage, car beaucoup d'invités offrent leur cadeau après la fête."),
  ],
  short="Quand faire sa liste ?")

g("message-liste-de-mariage/",
  "Texte liste de mariage : 12 formulations pour le faire-part",
  "Comment annoncer sa liste de mariage : 12 textes",
  "Formulations élégantes ou drôles pour annoncer votre liste de mariage dans le faire-part, sur le site ou par message, prêtes à copier.",
  """
<p>Parler de cadeaux peut sembler gênant. Pourtant vos invités attendent l'information. L'astuce : un ton simple, chaleureux, et jamais insistant.</p>
<h2>Où mettre le lien ?</h2>
<ul>
<li><strong>Sur votre site de mariage</strong>, dans une rubrique dédiée : la solution la plus discrète.</li>
<li><strong>Sur un petit carton</strong> glissé avec le faire-part, avec un QR code.</li>
<li><strong>Par message</strong>, aux invités qui vous demandent quoi offrir.</li>
</ul>
<h2>Nos messages tout prêts</h2>
<p>Remplacez {LIEN} par le lien de votre liste, puis copiez.</p>
{MSGS}
{CTA}
<h2>Les maladresses à éviter</h2>
<ul>
<li>imposer un montant ;</li>
<li>écrire la liste en gros sur le faire-part ;</li>
<li>relancer les invités qui n'ont rien offert.</li>
</ul>
""",
  faq=[
    ("Faut-il mettre la liste de mariage sur le faire-part ?", "Plutôt sur un carton à part ou sur votre site de mariage. C'est plus élégant qu'une mention en gros sur le faire-part."),
  ],
  short="Messages et textes")

g("combien-donner-pour-un-mariage/",
  "Combien donner pour un mariage en 2026 ?",
  "Combien donner pour un mariage ?",
  "Ami, collègue, famille proche, témoin : combien offrir pour un mariage en 2026, en cadeau ou en argent, selon votre lien avec les mariés.",
  """
<p>Il n'y a pas de règle officielle, mais quelques repères courants en France vous aident à ne pas être à côté.</p>
<h2>Les montants habituels</h2>
<table><thead><tr><th>Votre lien</th><th>Montant courant par personne</th></tr></thead><tbody>
<tr><td>Collègue, connaissance</td><td>30 à 50 €</td></tr>
<tr><td>Ami</td><td>50 à 100 €</td></tr>
<tr><td>Ami proche</td><td>100 à 150 €</td></tr>
<tr><td>Famille proche</td><td>100 à 300 €</td></tr>
<tr><td>Témoin</td><td>150 € et plus</td></tr>
</tbody></table>
<p>Ce sont des ordres de grandeur. Votre budget compte avant tout : les mariés préfèrent votre présence à un cadeau qui vous met en difficulté.</p>
<h2>Les critères qui comptent</h2>
<ul>
<li><strong>Votre proximité</strong> avec les mariés ;</li>
<li><strong>la formule</strong> : vin d'honneur seul ou repas et soirée ;</li>
<li><strong>vos frais</strong> : un long voyage ou un hébergement coûtent déjà cher ;</li>
<li><strong>venir en couple</strong> : on compte souvent un cadeau commun un peu plus élevé.</li>
</ul>
<h2>Cadeau ou argent ?</h2>
<p>Si les mariés ont une liste, privilégiez-la : c'est ce qu'ils ont choisi. Sinon, une enveloppe accompagnée d'un mot reste très appréciée. Vous pouvez aussi participer à plusieurs à un gros cadeau.</p>
<h2>Et si on ne peut pas venir ?</h2>
<p>Un petit cadeau ou une carte reste une belle attention, même si ce n'est pas obligatoire. Voir aussi nos <a href="{R}idees-cadeau-de-mariage/">idées de cadeaux</a>.</p>
""",
  faq=[
    ("Combien donner pour un mariage quand on est ami ?", "En général entre 50 et 100 € par personne, selon votre proximité et votre budget."),
    ("Combien donne un témoin ?", "Souvent 150 € ou plus, mais les frais d'enterrement de vie de garçon ou de jeune fille comptent aussi."),
  ],
  short="Combien donner ?")

g("idees-cadeau-de-mariage/",
  "Idées cadeau de mariage : 35 idées pour les invités",
  "Idées cadeau de mariage pour les invités",
  "Pas de liste ou envie d'un cadeau personnel ? 35 idées cadeau de mariage à tous les prix, utiles, originales ou personnalisées.",
  """
<p>Les mariés n'ont pas fait de liste, ou vous voulez ajouter une attention personnelle ? Voici des idées qui font mouche.</p>
<h2>Si les mariés ont une liste</h2>
<p>Commencez par là : c'est ce qui leur fait le plus plaisir. Demandez-leur simplement le lien.</p>
{CTA}
<h2>Les cadeaux utiles</h2>
<ul>
<li>une <a href="{AMZ:cocotte fonte}" rel="sponsored nofollow noopener" target="_blank">cocotte en fonte</a> ;</li>
<li>une belle parure de lit ;</li>
<li>un service à fondue ou à raclette ;</li>
<li>des <a href="{AMZ:valise cabine}" rel="sponsored nofollow noopener" target="_blank">valises cabine</a> pour le voyage de noces.</li>
</ul>
<h2>Les cadeaux personnalisés</h2>
<ul>
<li>un cadre gravé avec la date du mariage ;</li>
<li>un album photo à remplir ;</li>
<li>une planche à découper gravée à leurs prénoms ;</li>
<li>un livre d'or original.</li>
</ul>
<h2>Les expériences</h2>
<p>Un cours de cuisine à deux, un dîner dans un restaurant, une nuit dans un lieu insolite, un vol en montgolfière.</p>
<h2>Les petits budgets</h2>
<p>Un bon vin à ouvrir pour leur premier anniversaire, un jeu de société pour deux, une carte avec un mot sincère. Plus d'idées dans notre <a href="{R}liste-de-mariage-petit-budget/">guide petits prix</a>.</p>
""",
  faq=[
    ("Quel cadeau offrir à un mariage sans liste ?", "Un objet utile et durable (cocotte, linge de qualité), une expérience à deux ou de l'argent avec un mot personnel."),
  ],
  short="Idées cadeau de mariage")

g("remerciements-mariage/",
  "Remerciements mariage : textes pour les cadeaux",
  "Remerciements de mariage : textes pour les cadeaux",
  "Comment remercier vos invités pour leurs cadeaux de mariage : délai, carte ou message, et modèles de textes à personnaliser.",
  """
<p>Les remerciements comptent autant que la liste. Un mot personnel montre à vos invités que leur cadeau vous a touchés.</p>
<h2>Quand envoyer les remerciements ?</h2>
<p>Idéalement dans les <strong>2 mois</strong> qui suivent le mariage, avec une photo du jour J. Pour ne rien oublier, notez qui a offert quoi au fur et à mesure.</p>
<h2>Carte ou message ?</h2>
<p>Une carte imprimée avec une photo reste la formule la plus appréciée, surtout pour la famille. Un message personnel suffit pour les amis proches.</p>
<h2>Modèles de textes</h2>
<ul>
<li>« Merci du fond du cœur pour votre présence et pour la magnifique cocotte. Elle a déjà servi pour notre premier dîner de jeunes mariés ! »</li>
<li>« Votre cadeau nous accompagnera pendant notre voyage de noces. Merci d'avoir partagé ce jour avec nous. »</li>
<li>« Merci pour votre généreuse participation. Grâce à vous, notre voyage va devenir réalité. »</li>
<li>« Même de loin, vous étiez avec nous. Merci pour votre jolie attention. »</li>
</ul>
<h2>Le petit plus</h2>
<p>Citez le cadeau et dites comment vous l'utilisez : c'est ce qui rend le message personnel.</p>
{CTA}
""",
  faq=[
    ("Combien de temps pour envoyer ses remerciements de mariage ?", "Idéalement dans les 2 mois qui suivent le mariage."),
  ],
  short="Remerciements")

g("liste-de-pacs/",
  "Liste de Pacs : faut-il en faire une ? Idées et conseils",
  "Liste de Pacs : idées et conseils",
  "Faire une liste de cadeaux pour un Pacs : est-ce que ça se fait, comment l'annoncer et quoi mettre dedans, avec une liste Amazon gratuite.",
  """
<p>De plus en plus de couples fêtent leur Pacs avec leurs proches. Et la question arrive vite : peut-on faire une liste de cadeaux ? Oui, à condition de rester simple.</p>
{CTA}
<h2>Est-ce que ça se fait ?</h2>
<p>Oui, surtout si vous organisez une vraie fête. Vos invités vous demanderont quoi offrir : une petite liste leur facilite la vie. La liste de mariage Amazon fonctionne parfaitement pour un Pacs, il suffit d'indiquer la date de la fête.</p>
<h2>Quoi mettre dans une liste de Pacs ?</h2>
<p>Une liste plus courte qu'un mariage, 15 à 30 articles, avec beaucoup de petits prix : linge de maison, ustensiles de cuisine, jeux de société, accessoires de voyage. Inspirez-vous de notre <a href="{R}checklist/">checklist</a>.</p>
<h2>Comment l'annoncer ?</h2>
<p>Dans l'invitation ou par message : « On se pacse et on fait la fête ! Votre présence suffit, mais pour ceux qui ont demandé, voici une petite liste. »</p>
""",
  faq=[
    ("Peut-on faire une liste de mariage Amazon pour un Pacs ?", "Oui, la liste fonctionne de la même façon. Indiquez simplement la date de votre fête."),
  ],
  short="Liste de Pacs")

MESSAGES = [
  ("Carton du faire-part", "Votre présence est notre plus beau cadeau. Si vous souhaitez nous gâter, notre liste de mariage vous attend ici : {LIEN}"),
  ("Élégant", "Nous serions heureux de vous compter parmi nous. Pour ceux qui le désirent, une liste de mariage est disponible : {LIEN}"),
  ("Avec humour", "On a déjà un grille-pain, promis 😄 Pour ceux qui nous ont demandé des idées, voici notre liste : {LIEN}"),
  ("Voyage de noces", "Votre présence nous comble. Si vous souhaitez participer à notre voyage de noces ou à notre nouveau chez-nous, voici notre liste : {LIEN}"),
  ("Couple déjà installé", "Après X années sous le même toit, notre vaisselle a bien vécu ! Si vous voulez nous faire plaisir, voici notre liste : {LIEN}"),
  ("Amis, par message", "Hello ! Plusieurs d'entre vous nous ont demandé des idées, voici notre liste de mariage : {LIEN}. On a hâte de faire la fête avec vous 🥂"),
  ("Grands-parents", "Bonjour Mamie, bonjour Papi, voici la liste dont on vous a parlé : {LIEN}. Vous cliquez sur un cadeau et il arrive chez nous. On vous embrasse !"),
  ("Collègues", "Bonjour à tous, merci pour vos félicitations ! Pour ceux qui ont demandé, voici notre liste de mariage : {LIEN}"),
  ("Cadeau à plusieurs", "Certains cadeaux de notre liste peuvent être offerts à plusieurs, n'hésitez pas à vous regrouper : {LIEN}"),
  ("Site de mariage", "Votre présence est le plus important. Pour ceux qui souhaitent nous faire un cadeau, nous avons préparé une liste : {LIEN}"),
  ("Pacs", "On se pacse et on fait la fête ! Votre présence suffit, mais pour ceux qui nous ont demandé, voici une petite liste : {LIEN}"),
  ("Court, par SMS", "Comme promis, notre liste de mariage : {LIEN} Merci !"),
]

FAQ_HOME = [
  ("C'est gratuit ?", "Oui, entièrement. La checklist fonctionne sans inscription : vos choix restent sur votre appareil."),
  ("Est-ce que vous vendez les produits ?", "Non. Les articles mènent vers Amazon.fr. Si vous achetez après avoir cliqué, Amazon nous verse une petite commission, sans aucun surcoût pour vous."),
  ("Où créer ma liste en ligne ?", "Plusieurs solutions existent : site marchand, liste multi-boutiques, grand magasin ou cagnotte. Notre comparatif vous aide à choisir. Le bouton « Créer notre liste en ligne » ouvre la liste de mariage Amazon, notre choix pour sa simplicité."),
  ("Combien d'articles mettre dans sa liste ?", "Un peu plus que le nombre de foyers invités, avec des cadeaux à tous les prix."),
]
