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
- Rythme : 3 publications par semaine (bébé : lundi, mercredi, vendredi ; mariage : mardi, jeudi, samedi), chacune 1 article + 1 top.
- Si src/sujets.md a moins de 10 sujets non cochés, en ajouter 15 nouveaux (longue traîne, questions précises, pas de doublon avec les pages existantes) à la fin, dans le même format. Si src/tops.md a moins de 5 tops non cochés, en ajouter 8.
