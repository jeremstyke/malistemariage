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
