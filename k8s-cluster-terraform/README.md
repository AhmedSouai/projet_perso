# Terraform Kubernetes Setup 🛠️

## **Définit le fournisseur Cloud (provider.tf) ☁️**

- Configure **AWS** (ou un autre cloud provider) comme fournisseur pour les ressources. 🌍
- Pour cela, tu dois avoir un **compte chez un fournisseur de cloud** (AWS, Azure, Google Cloud, etc.), ainsi qu'un **token** ou des **clés d'API** pour permettre à Terraform de créer et gérer les ressources dans ton cloud.

## **Crée les machines virtuelles (main.tf) 💻**

- Crée un **master node** et **deux worker nodes** pour **Kubernetes**. 🖥️⚙️

## **Attribution d'IP privées aux nœuds Kubernetes 🌐**

- Chaque machine virtuelle se voit attribuer une **adresse IP privée** pour assurer la communication interne dans le cluster Kubernetes. 🔒

## **Ajoute des tags pour identifier chaque machine 🏷️**

- Des **tags** sont ajoutés à chaque machine virtuelle pour faciliter l’identification et la gestion des ressources dans le cloud. 🏷️🔍

## **Sécurise les accès avec un key pair pour SSH 🔑**

- Utilisation d'une **clé SSH** pour se connecter de manière sécurisée aux machines virtuelles. 🛡️

## **Affiche les adresses IP des machines après le déploiement 🖥️**

- Les **adresses IP privées** de chaque machine sont affichées comme **outputs** pour que tu puisses facilement les retrouver. 🔍💡

---

### **Prérequis 🔑**

- Un **compte fournisseur cloud** (par exemple : AWS, Google Cloud, Azure, etc.) pour pouvoir provisionner des ressources.
- Un **token ou une clé API** pour authentifier Terraform auprès de ton fournisseur cloud. Assure-toi que ton token a les permissions nécessaires pour créer des ressources (machines virtuelles, réseaux, etc.).

---

### **Utilité du projet 🎯**

Ce projet a pour but de faciliter le déploiement d'une infrastructure Kubernetes sur un fournisseur cloud à l'aide de **Terraform**. Il permet de créer et configurer automatiquement des machines virtuelles (nodes) pour un cluster Kubernetes, avec des configurations de sécurité et de réseau. L'objectif est de simplifier la gestion des ressources cloud et d'automatiser la mise en place d'un environnement Kubernetes prêt à l'emploi.

Avec ce projet, tu pourras :
- Provisionner facilement des machines virtuelles dans le cloud.
- Déployer rapidement un cluster Kubernetes avec des nodes dédiés.
- Assurer la gestion sécurisée de l'accès aux machines avec des clés SSH.
- Afficher et récupérer les adresses IP privées des nœuds Kubernetes pour une configuration rapide.

---

Avec ces informations, le fichier Terraform pourra être exécuté en toute sécurité pour déployer et gérer ton infrastructure cloud pour Kubernetes.
