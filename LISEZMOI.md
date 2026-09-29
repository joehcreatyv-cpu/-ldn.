# Analyseur Ligue des Nations : mise en ligne (gratuit)

Le site est statique. Un robot GitHub récupère les résultats réels toutes les 6 heures via API-Football et met à jour `data/results.json`. Votre clé API reste secrète (elle n'apparaît jamais dans le site).

1. Créez un compte gratuit sur github.com, puis un dépôt **public** (ex. `ldn`).
2. Ajoutez les fichiers : *Add file > Upload files* pour `index.html`, `data/` et `scripts/`. Pour `.github/workflows/update.yml`, utilisez *Add file > Create new file* et tapez le chemin complet dans le nom (les dossiers cachés passent mal à l'envoi).
3. *Settings > Pages* : Source = branche `main`, dossier `/ (root)`. L'adresse `https://VOTRE-NOM.github.io/ldn/` apparaît après une minute. Ouvrez-la sur votre téléphone, puis « Ajouter à l'écran d'accueil ».
4. Créez un compte gratuit sur api-football.com et copiez votre clé API.
5. Dans le dépôt : *Settings > Secrets and variables > Actions > New repository secret*, nom `API_FOOTBALL_KEY`, valeur = votre clé.
6. Onglet *Actions* > « Mise à jour des résultats » > *Run workflow*.

## Points à vérifier
- Le plan gratuit d'API-Football (100 requêtes/jour) limite parfois les saisons accessibles. Si le robot affiche une erreur de saison, le site continue avec les dernières données. Vous pouvez alors modifier `data/results.json` à la main ou changer de fournisseur.
- `LEAGUE = 5` doit correspondre à la Ligue des Nations dans votre compte.

## Nom de domaine
L'adresse `github.io` est gratuite. Un domaine personnalisé (ex. monsite.com) coûte environ 10 à 15 $/an chez un registraire ; on le branche dans *Settings > Pages > Custom domain*.
