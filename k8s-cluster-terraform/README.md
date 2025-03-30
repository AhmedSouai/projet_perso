Fichiers Terraform

1. provider.tf - Configuration du Cloud Provider
Ce fichier contient la configuration de Terraform Provider qui définit quel cloud provider utiliser pour créer les ressources. Par exemple, avec AWS, il configure l'accès avec tes clés d'API AWS.

Utilité : Ce fichier déclare le fournisseur de cloud utilisé pour l'infrastructure (par exemple, AWS, Azure, GCP). Il permet à Terraform de savoir où déployer les ressources.

3. variables.tf - Déclaration des Variables
Ce fichier contient la déclaration des variables utilisées dans la configuration Terraform. Il est également là pour définir des variables sensibles, comme les clés d'accès.

Utilité : Ce fichier permet de rendre le projet plus flexible en paramétrant les valeurs via des variables. Les variables sensibles (comme les clés d'API) sont déclarées ici mais ne sont pas stockées en clair dans le code. Elles doivent être définies dans un fichier terraform.tfvars ou via des variables d'environnement pour plus de sécurité.

5. main.tf - Définition des Ressources
Le fichier main.tf définit les ressources à créer, comme les instances EC2 (sur AWS) ou autres ressources cloud, ainsi que leurs configurations (exemple, type d'instance, adresse IP privée).


Utilité : Ce fichier définit la topologie de l'infrastructure. Dans l'exemple ci-dessus, il déploie des instances EC2 pour le cluster Kubernetes, mais tu peux ajouter d'autres ressources comme des VPC, subnets, groupes de sécurité, etc.

7. outputs.tf - Définition des Outputs
Ce fichier permet de définir des outputs qui sont retournés à la fin du déploiement. Par exemple, tu peux récupérer les adresses IP des instances pour les utiliser dans une autre étape de ton déploiement ou dans une configuration supplémentaire.


Utilité : Les outputs sont utiles pour récupérer des informations importantes une fois que l’infrastructure est déployée. Cela permet de communiquer des résultats de manière structurée à d'autres scripts ou utilisateurs.

9. terraform.tfvars - Affectation des Variables
Le fichier terraform.tfvars est utilisé pour assigner les valeurs aux variables définies dans variables.tf. C’est ici que les informations sensibles, comme les clés d'API, les noms d'instance, etc., doivent être assignées.


Utilité : Ce fichier permet de définir les valeurs réelles pour les variables, en les séparant des fichiers de configuration. N’oublie pas de ne jamais versionner ce fichier dans ton dépôt pour des raisons de sécurité.

