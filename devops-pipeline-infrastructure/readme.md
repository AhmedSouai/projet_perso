# devops-pipeline-infrastructure 🚀

Ce projet implémente un pipeline **CI/CD** complet avec **Jenkins**, **Docker**, **Kubernetes**, **Terraform**, et **Vault**.

## Technologies utilisées 🛠️
- **Jenkins** pour l'orchestration du pipeline 🔧
- **Docker** pour la containerisation de l'application 🐳
- **Kubernetes** pour l'orchestration des conteneurs ☸️
- **Terraform** pour gérer l'infrastructure 💻
- **Vault** pour gérer les secrets de manière sécurisée 🔒

## Étapes du pipeline 🔄
1. **Clonage du code source** depuis le dépôt 💻
2. **Analyse statique du code** avec **SonarQube** 🧑‍💻
3. **Création et push** de l'image Docker 🐳
4. **Exécution des tests unitaires** 🧪
5. **Déploiement de l'application** sur Kubernetes ☸️
6. **Notifications** via **Slack** 💬

## Prérequis 🔑
- **Jenkins** installé et configuré ✅
- **Kubernetes** cluster configuré 🌐
- **Vault** pour la gestion des secrets 🔐
- **Terraform** pour la gestion de l'infrastructure 🛠️

---

**Comment démarrer 🏁 :**
1. Clonez le dépôt git.
2. Configurez Jenkins avec les outils nécessaires.
3. Assurez-vous que **Docker** et **Kubernetes** sont installés.
4. Configurez **Vault** pour gérer vos secrets.
5. Lancez le pipeline avec Jenkins et profitez du CI/CD automatisé ! 🚀

---
