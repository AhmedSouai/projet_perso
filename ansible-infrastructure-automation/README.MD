# Ansible Security Automation

## Description
Ce projet automatise la sécurité des serveurs en appliquant des correctifs de sécurité, en scannant les vulnérabilités avec **OpenSCAP** et en gérant les accès SSH à l'aide d'Ansible.

## Fonctionnalités
1. **Installation d'OpenSCAP** : Installe OpenSCAP et les guides de sécurité SCAP sur les serveurs cibles.
2. **Patch de Sécurité** : Applique les mises à jour de sécurité.
3. **Gestion des Accès SSH** : Ajoute et gère les utilisateurs SSH.
4. **Scan des Vulnérabilités** : Scanne les serveurs pour les vulnérabilités en utilisant OpenSCAP, et affiche le nombre de vulnérabilités détectées pour chaque serveur.

### Arborescence du projet

ansible-infrastructure-automation/

├── inventory.ini 

├── playbook.yml 

├── tasks_security_patch.yml 

├── tasks_ssh_access.yml

├── tasks_vulnerability_scan.yml 

├── handlers.yml 

├── README.md


## Installation

### Prérequis
- **Ansible** installé sur la machine de contrôle.
- Accès SSH aux serveurs cibles avec une clé SSH.
- **OpenSCAP** sera installé automatiquement sur les serveurs pendant l'exécution du playbook.

### Installation d'Ansible
```bash
sudo apt update && sudo apt install -y ansible


---

### Résumé des fichiers :
- **`inventory.ini`** : Liste des serveurs cibles.
- **`playbook.yml`** : Playbook principal, exécutant les différentes tâches.
- **`tasks_install_openscap.yml`** : Installation d'OpenSCAP avec vérification préalable.
- **`tasks_security_patch.yml`** : Mise à jour des paquets de sécurité.
- **`tasks_ssh_access.yml`** : Gestion des accès SSH.
- **`tasks_vulnerability_scan.yml`** : Exécution du scan de vulnérabilités et comptage des vulnérabilités.
- **`handlers.yml`** : Gestion des redémarrages.
- **`README.md`** : Documentation complète sur le projet.

Ces fichiers constituent l'ensemble du projet pour automatiser la gestion de la sécurité avec Ansible, OpenSCAP et les mises à jour de sécurité. Si tu as d'autres questions ou demandes, n'hésite pas à me le faire savoir ! 😊
