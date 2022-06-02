# Ragnarokkr Backup UI/API

>Le but de ce projet est de créer une micro interface basé sur une micro API en Python/FastAPI pour donner accès aux clients aux fonctions de backup et de restore

## Prerequis

l'API et l'Interface doivent être light car cette application est un plugin et ne doit pas consommer de ressource sur les nodes des clients.

La page web principale de l'interface doit être mono-page et entierement basé sur javascript avec des échanges REST/JSON a l'API Django

Pas de language interpreté (ex PHP, Node.Js), seul l'api pourra communiquer avec le node.
Pas de base de donnée

## Fonctionnalités
>(cf API)
 - Voir les backups/snapshots disponible avec leurs : Date, ID, Paths, Tags et Host, ce tableau devrat être classé par date plus récente
 - Pouvoir Choisir, dans une liste, un des snapshots pour lancer une restoration (liste des ID), dans cette liste un choix Latest (ou plus récent) sera à jouter.
 - Avoir un bouton restorer qui lancera la restoration (cf API) de l'ID choisie et affichera en fin d'opération et affichera le dossier de restoration.
   - Cette etape pouvant prendre du temps il faudra prévoir un mode asynchrone avec lancement de la restoration, check de l'état de la restoration, fin de restoration.
 - Avoir un bouton pour faire un backup manuel (par défaut le plugin permet déjà de faire des backups automatiques)
 - Avoir une fonction de recherche (cf API) qui va chercher un fichier ou dossier dans les backups


## Securité
 - L'interface devra se connecter a l'API sur le meme port
 - Un simple login / pass sera mis en place au niveau de la configuration de serveur web sur la node (configuré au moment de l'installation du plugin)

