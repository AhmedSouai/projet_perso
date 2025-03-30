 Ce que fait ce fichier Terraform : 
Définit le fournisseur Cloud (provider.tf) → AWS (ou autre cloud provider)

Crée les machines virtuelles (main.tf) → 1 master node + 2 worker nodes

Attribue des IP privées aux nœuds Kubernetes

Ajoute des tags pour identifier chaque machine

Sécurise les accès avec un key pair pour SSH

Affiche les adresses IP des machines après le déploiement (
