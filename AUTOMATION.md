# Article automatique tous les 2 jours (Ma liste mariage, malistedemariage.fr)

1. Prendre le premier sujet non coché dans `src/sujets.md`.
2. Écrire l'article dans `src/auto_articles.py` avec `g(...)` (même format que `src/content.py`) et ajouter son emoji dans `AUTO_META`.
3. `python3 src/build.py` (doit afficher le nouveau nombre de pages, aucun tiret long autorisé).
4. Cocher le sujet `[x]` dans `src/sujets.md`.
5. Commit + push sur `main`.

Règles d'écriture : vouvoiement (on s'adresse au couple), français simple, jamais de tiret long, 900 à 1 300 mots, un tableau, une FAQ de 2 ou 3 questions,
`{CTA}` après l'introduction, liens internes vers 2 ou 3 guides existants et vers `{R}checklist/`.
Pas de chiffre ni de fait inventé : vérifier tout fait précis (conditions Amazon, démarches, montants) par une recherche web, sinon rester général.
Ne jamais promettre de réduction sur la liste de mariage Amazon (aucune confirmée en France).
Liens Amazon : uniquement via `{AMZ:mots clés}` dans le corps (le tag est ajouté automatiquement).
Ton neutre : ne pas parler d'Amazon dans chaque paragraphe. Présenter les solutions de façon équilibrée (site marchand, liste multi-boutiques, magasin, cagnotte) ; Amazon peut être cité comme notre choix, sans plus. Lien vers la page comparatif `{R}ou-faire-sa-liste-de-mariage/` quand le sujet s'y prête.

Guides produits (« comment choisir ») : expliquer les critères de choix avec un tableau comparatif par type ou par budget, sans inventer de caractéristiques ni de prix de modèles précis. Mettre un lien `{AMZ:mots clés}` par type de produit (par exemple `{AMZ:poussette compacte}`), à l'endroit où on parle de ce type, 4 à 8 liens par article. Ne citer un modèle ou une marque que si un fait précis a été vérifié par une recherche web. Lien vers `{R}checklist/` et vers le guide liste Amazon.

## SEO et liens entre sites (17 nov 2026)
- Auteur : guides signés Jérémy Dacier-Jury (byline, schema Person, publisher Organization avec logo), page /a-propos/. Ne pas retirer.
- Pied de page : liens vers les 3 autres sites (Vieillir chez soi, Les oiseaux du jardin, l'autre liste). Dans le texte : au maximum 1 lien vers un site frère par page, seulement quand c'est vraiment utile.
- Chaque nouvelle page : meta description unique de 140 à 160 caractères, FAQ de 3 à 5 vraies questions, au moins 2 liens internes. Pas de faux tests ni de prix inventés.
- Priorité aux requêtes longue traîne peu concurrencées : situations précises (jumeaux, prématuré, petit appartement, budget serré, 2e mariage, mariage à l'étranger...), questions concrètes (combien, quand, faut-il), plutôt que les grosses requêtes génériques tenues par les gros sites.

## Rythme et réapprovisionnement (17 nov 2026)
- Rythme : 2 publications par jour, tous les jours (11h43 et 20h23, chacune 1 article + 1 top). Ces deux passages sont voulus, ce ne sont pas des doublons. Minimum absolu demandé par Jeremy : au moins 1 article par jour sur chaque site.
- Si src/sujets.md a moins de 10 sujets non cochés, en ajouter 15 nouveaux (longue traîne, questions précises, pas de doublon avec les pages existantes) à la fin, dans le même format. Si src/tops.md a moins de 5 tops non cochés, en ajouter 8.

## Qui publie (17 nov 2026)
- Toutes les publications de ce site sont faites UNIQUEMENT par les tâches programmées créées depuis la conversation de Jeremy dédiée aux 4 sites affiliés (Vieillir chez soi, Les oiseaux du jardin, Ma liste bébé, Ma liste mariage). Toute autre session ou conversation ne doit ni publier de page, ni créer, modifier ou dupliquer une tâche de publication pour ce site : elle signale le besoin à Jeremy et s'arrête.

## Exploiter les failles des concurrents (règle du 18 nov 2026, obligatoire pour chaque nouvelle page)
Avant d'écrire une page, cherche sa requête principale sur le web et ouvre les 3 premiers résultats (hors Amazon et marchands). Note ce qui leur manque, puis fais-le mieux :
- page datée (ancienne année dans le titre, produits plus vendus) : produits actuels et année en cours ;
- page mince ou trop courte : réponds à toutes les vraies questions du lecteur (FAQ, cas particuliers, erreurs fréquentes) ;
- pas de tableau comparatif : mets-en un dès le haut de la page ;
- peu de produits ou un seul budget : couvre petit budget, milieu de gamme et haut de gamme ;
- critères vagues : critères de choix concrets et vérifiés (dimensions, matériaux, entretien, sécurité) ;
- liens d'achat tardifs : premier lien utile dès l'introduction, après {CTA} ;
- angle oublié (situation précise, saison, petit logement, aide financière, entretien) : traite-le dans une section dédiée.
Ne copie jamais leurs phrases ni leur structure. N'invente rien pour paraître plus complet : chaque ajout reste vérifié comme le reste de la page.

## Mots clés longue traîne (règle du 18 nov 2026, obligatoire pour chaque nouvelle page)
Le site est jeune : il gagne d'abord sur des requêtes précises de 4 mots et plus, peu disputées par les gros sites.
- Choisis pour chaque page une requête principale longue traîne (ex. « siège de douche pliable petite douche » plutôt que « siège de douche »), mets-la dans le title, le h1, le premier paragraphe et le slug d'une nouvelle page.
- Repère 5 à 10 variantes et questions voisines (suggestions de recherche, « Autres questions posées », forums) et traite-les dans les intertitres et la FAQ, formulées comme les gens les tapent.
- Une page par intention : n'écris pas deux pages qui visent la même requête ; complète plutôt la page existante.
- Quand une liste de sujets ou de tops se réapprovisionne, privilégie les requêtes longue traîne à intention d'achat (meilleur, pour qui, pour quel usage, comparatif, avis, petit budget).

## Angle du site dans chaque top (règle du 19 nov 2026, obligatoire pour chaque top)
- Un top de Ma liste mariage ne vise jamais la requête générique seule (« meilleur X ») face aux grands comparateurs : il vise la requête liée au sujet du site, un cadeau de mariage ou de liste de mariage. Exemples : « meilleure plancha pour une liste de mariage », « quelle plancha mettre sur sa liste de mariage ».
- Le title, le h1, la description et la première phrase annoncent cet angle.
- Juste après l'encadré « Comment nous avons fait cette sélection », une section <h2> du type « Pourquoi une plancha est un bon cadeau de mariage ? » explique pourquoi ce produit fait un bon cadeau de mariage (durée, usage à deux, recevoir, prix qui se partage entre invités). 2 paragraphes concrets, un avis clair (« Notre conseil : ... »), aucun fait inventé.
- La FAQ contient une question sur cet angle, par exemple « Pourquoi offrir une plancha pour un mariage ? ».
- Chaque fiche produit dit aussi, en une phrase, pour quel couple ce produit est le bon choix.
- Avant de prendre une ligne de tops.md : si sa requête est générique, réécris-la avec l'angle du site (slug compris si la page n'existe pas encore) ; si le produit n'a vraiment aucun lien avec le sujet du site, coche-la « abandonné, hors sujet » et prends la suivante.

## Bouton prix et lignes réservées (22 nov 2026)
- Dans les tops, garder pour chaque produit le lien de fin de fiche au format exact `<p><a href="{AMZ:Marque Modèle}" rel="sponsored nofollow noopener" target="_blank">Voir sur Amazon</a></p>` : build.py le transforme en bouton « Voir le prix sur Amazon ».
- Une ligne « - [~] » de sujets.md ou tops.md est réservée à une publication programmée : les tâches quotidiennes ne la prennent pas.
