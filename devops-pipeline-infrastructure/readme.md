# DevOps Pipeline CI/CD 🚀

Ce projet implémente un pipeline CI/CD complet avec **Jenkins** qui exécute plusieurs types de tests :

- **Tests unitaires** 🧪
- **Tests d'intégration** 🔗
- **Tests de performance** 🚀
- **Tests de sécurité** 🔐

## Technologies utilisées 🛠️

- **Jenkins** pour l'orchestration du pipeline 🔧
- **Docker** pour la containerisation de l'application 🐳
- **Flask** pour l'application web Python 🐍
- **Bandit** pour l'analyse de sécurité 🔒

## Étapes du pipeline 🔄

1. **Clonage du code depuis le dépôt Git** 💻
2. **Build Docker Image** 🐳
3. **Tests Unitaires** 🧪
4. **Tests d'Intégration** 🔗
5. **Tests de Performance** 🚀
6. **Tests de Sécurité** 🔐
7. **Push de l'image Docker vers Docker Hub** 🚀
8. **Notification Slack** 💬

## Prérequis 🔑 ##

Avant de commencer, assurez-vous d'avoir les outils suivants installés et configurés :

1. **Jenkins** installé et configuré ✅
2. **Docker** installé 🐳
3. **Bandit** pour l'analyse de sécurité 🔒
4. **Flask** pour l'application Python 🐍

## Configuration de Jenkins pour Slack 📲

Pour que les notifications Slack fonctionnent dans Jenkins, vous devez suivre les étapes suivantes :

### 1. **Installer le plugin Slack dans Jenkins** 🔌

- Ouvrez l'interface Jenkins.
- Allez dans **Manage Jenkins** > **Manage Plugins**.
- Sous l'onglet **Available**, recherchez **Slack Notification Plugin**.
- Cochez la case et cliquez sur **Install without restart** (Installer sans redémarrer).

### 2. **Créer une application Slack et obtenir un token** 🛠️

- Allez sur [Slack API](https://api.slack.com/apps) et créez une nouvelle application.
- Dans la section **OAuth & Permissions**, attribuez les permissions nécessaires comme `chat:write`.
- Générez un **OAuth Access Token**.
- Copiez ce token pour l'utiliser dans Jenkins.

### 3. **Configurer Slack dans Jenkins** ⚙️

- Allez dans **Manage Jenkins** > **Configure System**.
- Cherchez la section **Slack** et cliquez sur **Add Slack**.
- Remplissez les champs suivants :
  - **Workspace** : Entrez l'URL de votre espace Slack (ex : `https://tonworkspace.slack.com`).
  - **Token** : Collez votre **OAuth Access Token**.
  - **Channel** : Entrez le nom du canal Slack où vous souhaitez envoyer les notifications (ex : `#notifications`).

## Configuration Docker et Jenkins pour exécuter Docker 🐳

Avant de pouvoir construire et pousser des images Docker, assurez-vous que :

1. **Docker est installé et configuré** sur votre machine Jenkins. Jenkins doit pouvoir exécuter des commandes Docker comme `docker build` et `docker push`.

2. **Authentification Docker** : Utilisez les **credentials Docker** dans Jenkins pour vous authentifier sur Docker Hub, afin de pouvoir pousser l'image. Configurez un **credential Docker Hub** avec votre nom d'utilisateur et mot de passe ou un **access token**.

