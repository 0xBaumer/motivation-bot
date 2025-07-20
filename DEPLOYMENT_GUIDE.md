# Guide de Déploiement - TopG Alpha Bot sur Railway 🚀

## Étape 1 : Créer un repository GitHub

### A. Créer le repo sur GitHub.com
1. Allez sur [github.com](https://github.com)
2. Cliquez sur le bouton **"New"** (ou le "+" en haut à droite)
3. Nom du repository : `topg-alpha-telegram-bot`
4. Description : `Bot Telegram avec citations motivationnelles de personnalités inspirantes`
5. Sélectionnez **Public** ou **Private** (au choix)
6. **NE PAS** cocher "Initialize this repository with README" (on a déjà nos fichiers)
7. Cliquez sur **"Create repository"**

### B. Connecter votre repo local à GitHub
Dans votre terminal, exécutez ces commandes (remplacez `VOTRE_USERNAME` par votre nom d'utilisateur GitHub) :

```bash
cd /Users/balintnussbaumer/Desktop/Scrapers
git remote add origin https://github.com/VOTRE_USERNAME/topg-alpha-telegram-bot.git
git branch -M main
git push -u origin main
```

## Étape 2 : Déployer sur Railway

### A. Créer un compte Railway
1. Allez sur [railway.app](https://railway.app)
2. Cliquez sur **"Login"**
3. Connectez-vous avec votre compte **GitHub**
4. Autorisez Railway à accéder à vos repositories

### B. Créer un nouveau projet
1. Dans Railway, cliquez sur **"New Project"**
2. Sélectionnez **"Deploy from GitHub repo"**
3. Choisissez votre repository `topg-alpha-telegram-bot`
4. Railway va automatiquement détecter que c'est un projet Python

### C. Configurer les variables d'environnement
1. Dans votre projet Railway, allez dans l'onglet **"Variables"**
2. Ajoutez une nouvelle variable :
   - **Nom** : `BOT_TOKEN`
   - **Valeur** : `7836750010:AAE9iW2qLXLNxivMH3Yh_K2UbrxghW9cyBc`
3. Cliquez sur **"Add"**

### D. Déployer
1. Railway va automatiquement déployer votre bot
2. Le déploiement prend environ 2-3 minutes
3. Vous verrez les logs en temps réel
4. Une fois terminé, votre bot sera **EN LIGNE 24/7** ! 🎉

## Étape 3 : Vérifier que ça marche

1. Ouvrez Telegram
2. Recherchez `@TopGAlphaBot`
3. Envoyez `/start`
4. Testez quelques commandes comme `/goggins` ou `/tate`

## Étape 4 : Surveiller votre bot

### Dans Railway :
- **Logs** : Onglet "Deployments" pour voir les logs
- **Métriques** : Onglet "Metrics" pour voir l'utilisation
- **Consommation** : Onglet "Usage" pour voir les heures utilisées

### Gratuit jusqu'à 500h/mois
- Avec Railway gratuit, votre bot peut tourner ~20 jours par mois
- Si vous dépassez, le bot s'arrêtera automatiquement
- Pour plus, upgrade vers Railway Pro ($5/mois)

## Troubleshooting

### Bot ne répond pas ?
1. Vérifiez les logs dans Railway
2. Assurez-vous que `BOT_TOKEN` est bien configuré
3. Vérifiez que le déploiement s'est bien passé

### Erreur de déploiement ?
1. Vérifiez que tous les fichiers sont bien pushés sur GitHub
2. Regardez les logs d'erreur dans Railway
3. Assurez-vous que `requirements.txt` et `Procfile` sont présents

### Bot s'arrête après quelques jours ?
- Vous avez probablement dépassé les 500h gratuites
- Upgrade vers Railway Pro ou utilisez une autre plateforme

## Alternatives si Railway ne marche pas

1. **Render.com** - Également gratuit avec 750h/mois
2. **Heroku** - Plan gratuit disponible
3. **DigitalOcean App Platform** - $5/mois mais plus fiable
4. **VPS classique** - Plus complexe mais plus de contrôle

---

**Une fois déployé, votre bot fonctionnera 24/7 même quand votre ordinateur est éteint ! 💪**

**Stay hard!** 🔥
