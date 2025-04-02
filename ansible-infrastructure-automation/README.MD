# 🚀 Projet d'Automatisation de la Sécurité et du Patch Management avec Ansible

Ce projet utilise **Ansible** pour automatiser la gestion des vulnérabilités, des patchs de sécurité et des configurations SSH sur des serveurs. Il s'agit d'une solution pour appliquer des **patchs de sécurité** sur des systèmes **Debian/Ubuntu** et **CentOS/RHEL**, de **sécuriser l'accès SSH**, et de **scanner les vulnérabilités** à l'aide de **OpenSCAP**. Ce playbook est conçu pour être utilisé en **environnement de production**.

## 🎯 Objectifs du Projet

- 🔒 **Sécuriser l'accès SSH** : Créer un utilisateur sécurisé (`secadmin`), désactiver l'accès SSH pour `root`, et limiter l'accès aux utilisateurs autorisés.
- 🛡️ **Scanner les vulnérabilités** : Utiliser **OpenSCAP** pour scanner les vulnérabilités de sécurité et afficher les résultats détaillés.
- 🔄 **Appliquer des patchs de sécurité** : Mettre à jour les paquets de sécurité sur les serveurs sans interférer avec les configurations en production.
- 🔄 **Redémarrage conditionnel** : Ne redémarrer que les services nécessaires, comme `sshd`, si un redémarrage est requis après une mise à jour.

## 🛠️ Prérequis

Avant d'exécuter ce playbook, assurez-vous que les éléments suivants sont installés sur votre machine et vos serveurs :

- Ansible (version 2.9 ou supérieure)
- OpenSCAP installé sur les serveurs cibles (voir la tâche `tasks_install_openscap.yml`)
- Accès SSH avec des droits sudo pour les utilisateurs cibles
- Clé SSH publique pour l'utilisateur `secadmin` (ou une autre clé valide)

## 🔍 Structure du Projet

ansible-infrastructure-automation/ 

├── inventory.ini # Fichier d'inventaire Ansible avec les hôtes cibles

├── playbook.yml # Playbook principal exécutant toutes les tâches 

├── tasks_install_openscap.yml # Installation d'OpenSCAP 

├── tasks_security_patching.yml # Application des patchs de sécurité 

├── tasks_ssh_access.yml # Configuration de l'accès SSH sécurisé 

└── README.md # Documentation du projet


## ⚙️ Détails des Tâches

### 1. `tasks_install_openscap.yml`

Cette tâche installe **OpenSCAP** sur les serveurs cibles pour effectuer des scans de vulnérabilités. Si OpenSCAP est déjà installé, la tâche passe cette étape.

### 2. `tasks_ssh_access.yml`

- **Création de l'utilisateur sécurisé (`secadmin`)** : Cet utilisateur a des privilèges sudo et un shell Bash.
- **Désactivation de l'accès SSH pour `root`** : Empêche la connexion SSH en tant que `root`.
- **Limitation de l'accès SSH** : L'accès SSH est limité uniquement à l'utilisateur `secadmin`.
- **Copie de la clé SSH** : Copie une clé SSH publique pour l'utilisateur `secadmin` afin d'éviter l'utilisation de mots de passe.

### 3. `tasks_security_patching.yml`

- **Mise à jour des paquets de sécurité** :
  - Pour **Debian/Ubuntu**, seuls les paquets installés sont mis à jour.
  - Pour **CentOS/RHEL**, seuls les paquets de sécurité sont mis à jour.
- **Redémarrage conditionnel** : Si un redémarrage est nécessaire (par exemple après une mise à jour du noyau), le playbook vérifie s'il faut redémarrer les services (comme `sshd`), plutôt que de redémarrer complètement le serveur.

## 📝 Comment Utiliser ce Playbook

### 1. Clonez ce dépôt

Clonez ce projet sur votre machine locale :

git clone https://github.com/AhmedSouai/projet_perso/
cd ansible-infrastructure-automation


## 🛑 Attention
Environnement de production : Bien que ce playbook soit conçu pour être utilisé en production, il est recommandé de le tester d'abord sur un environnement de staging pour éviter toute interruption de service.

Redémarrage des services : Le playbook redémarre certains services comme sshd pour appliquer les mises à jour de sécurité, mais il n'effectue pas de redémarrage complet des serveurs.

## 📄 License
Ce projet est sous la licence MIT. Vous pouvez librement l'utiliser, le modifier, et le distribuer selon les termes de cette licence.


