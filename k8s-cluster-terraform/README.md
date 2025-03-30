Ce fichier Terraform 🛠️ :
Définit le fournisseur Cloud (provider.tf) ☁️

Configure AWS (ou un autre cloud provider) comme fournisseur pour les ressources. 🌍

Crée les machines virtuelles (main.tf) 💻

Crée un master node et deux worker nodes pour Kubernetes. 🖥️⚙️

Attribution d'IP privées aux nœuds Kubernetes 🌐

Chaque machine virtuelle se voit attribuer une adresse IP privée pour assurer la communication interne dans le cluster Kubernetes. 🔒

Ajoute des tags pour identifier chaque machine 🏷️

Des tags sont ajoutés à chaque machine virtuelle pour faciliter l’identification et la gestion des ressources dans le cloud. 🏷️🔍

Sécurise les accès avec un key pair pour SSH 🔑

Utilisation d'une clé SSH pour se connecter de manière sécurisée aux machines virtuelles. 🛡️

Affiche les adresses IP des machines après le déploiement 🖥️

Les adresses IP privées de chaque machine sont affichées comme outputs pour que tu puisses facilement les retrouver. 🔍💡
