========================
Développer au grand jour
========================

Environnement de développement de plugin
-----------------------------------------

Comme nous l'avons vu, il y a plusieurs options pour maintenir un environnement de développement de plugins:

Copier le modèle du plugin dans le répertoire de plugin QGIS et travailler à partir de cet endroit.
Travailler dans le répertoire où on a créé nos modèles et faire un lien à partir du répertoire de plugin.

Le problème avec la première option est que si on veut tester la fonction de désinstallation des plugins, cela va supprimer tout le répertoire du plugin, et on risque de perdre notre code.
Avec la seconde option on a pas ce risque, mais il faut à chaque fois que l'on veut tester la désinstallation refaire le lien à partir du répertoire de plugin.

Il y a deux autres solutions pour régler ce problème.

La première est d'utiliser un gestionnaire de versionnement de code tel que *git* et de faire des commits à partir du répertoire de travail et des *pull* dans le répertoire de plugins. Ce n'est pas beaucoup plus pratique que de copier le code dans le répertoire de plugin à chaque modification.

La seconde est la meilleure solution. Il s'agit de travailler dans un répertoire externe au répertoire des plugins, et d'utiliser la variable d'environnement QGIS_PLUGINPATH en la faisant pointer vers le répertoire de développement. Lorsque cette variable est présente, QGIS_PLUGINPATH indique à QGIS d'aller chercher les plugins dans des répertoires supplémentaires. Cela permet d'utiliser le répertoire de développement et de tester le plugin sans avoir à faire de lien ni de copie. Le plugin n'étant dans ce cas pas installé avec l'installateur de plugins, il ne peut pas être désinstallé, et donc ne peut pas être supprimé par erreur. Lorsqu'on est prêt à tester l'installation et la désinstallation du plugin, on peut alors le copier dans le répertoire de QGIS ou créer un dépôt pour cela.

Qu'est ce que c'est que Git ?
------------------------------

Git est un système de gestion de version de code source distribué. Il permet de gérer différents flux de production de développement de code source. Git est aujourd'hui un des outils de développement les plus utilisés dans le monde du développement opensource. Il est notamment utilisé pour gérer les sources du noyau Linux.

Une bonne ressource sur git est le livre disponible librement *Pro Git* (http://progit.org). Une version en cours de traduction en français est disponible : http://progit.org/book/fr/

.. toctree::
    :maxdepth: 2

    git

Créer un dépot git
------------------
Le développement logiciel nécessite un certain nombre d'outils pour pouvoir conserver une certaine qualité. Parmi ceux-ci, le bug tracker et le gestionnaire de versionnement de code sont les deux outils indispensables aux développeurs. L'infrastructure du projet QGIS fournit ces outils lorsqu'on veut publier publiquement notre travail.

On peut créer un compte sur le hub QGIS (http://hub.qgis.org) ou bien également sur GitHub (http://www.github.com), afin de pouvoir bénéficier d'un dépôt de code source *git*.

Voici les étapes nécessaires pour créer un plugin avec gestion du code source avec git:

#. Installez le Plugin Builder
#. Créez un répertoire qui va contenir tous vos plugins, par exemple *my_plugins*
#. Créez un modèle de plugin en utilisant le Plugin Builder, et indiquez lui le répertoire précédemment créé comme base
#. Allez dans le répertoire du plugin (e.g. my_plugins/zoomer) créé par le Plugin Builder, et créez un dépôt git comme ceci ::

    git init

#. Réglez la variable d'environnement QGIS_PLUGINPATH pour pointer vers le répertoire contenant les plugins (my_plugins). Attention de bien spécifier le chemin entier.
#. Démarrez QGIS et utilisez le gestionnaire de plugins pour activer le plugin. Si le plugin n'est pas visible dans la liste, vérifiez la variable QGIS_PLUGINPATH.
#. Développez, testez. N'oubliez pas de commiter les changements régulièrement et de faire des *push* vers le dépôt public hub.qgis.org ou vers github.

Développer avec git
-------------------

Voici les quelques commandes git que vous allez devoir utiliser pour développer des plugins de QGIS.

Créer un nouveau dépôt git::

    git init

Ajouter des fichiers au système git::

    git add -A

Voir l'état des fichiers::

    git status

Commiter toutes les modifications::

    git commit -a

Attention de bien spécifier un message explicite sur les modifications que vous avez effectuées.

Pousser les modifications sur le serveur distant::

    git push

Récupérer un dépôt source distant en local::

    git clone git://github.com/schacon/grit.git

Mettre à jour un dépôt git local à partir du dépôt distant::

    git fetch

Créer un dépôt source QGIS
--------------------------

Le projet QGIS met à disposition une infrastructure d'hébergement de projets. On peut y créer des nouveaux projets de plugins, et gérer les sources avec git.

Phase préparatoire : créer des clefs ssh
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pour pouvoir utiliser git correctement, il faut disposer de clefs d'authentification SSH.

On vérifie tout d'abord si on dispose déjà de clefs::

    $ cd ~/.ssh

Si le répertoire existe, on sauvegarde les clefs existantes::

    $ ls
    config	id_rsa	id_rsa.pub	known_hosts
    $ mkdir key_backup
    $ cp id_rsa* key_backup
    $ rm id_rsa*

Créons une nouvelle clef SSH. On prend les réglages par défaut::

    $ ssh-keygen -t rsa -C "your_email@youremail.com"
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/formation/.ssh/id_rsa):

Il faut donner un mot de passe pour valider la clef::

    Enter passphrase (empty for no passphrase):<enter a passphrase>
    Enter same passphrase again:<enter passphrase again>

On obtient alors quelque chose comme::

    Your identification has been saved in /Users/your_user_directory/.ssh/id_rsa.
    Your public key has been saved in /Users/your_user_directory/.ssh/id_rsa.pub.
    The key fingerprint is:01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db user_name@username.com
    The key's randomart image is:
    +--[ RSA 2048]----+
    |     .+   +      |
    |       = o O .   |
    |        = * *    |
    |       o = +     |
    |      o S .      |
    |     o o =       |
    |      o . E      |
    |                 |
    |                 |
    +-----------------+

Vous avez créé votre clef, qu'on utilisera ensuite pour se connecter sur GitHub ou le Hub QGIS.

Configurer Git
^^^^^^^^^^^^^^

Il reste à configurer quelques options de Git

Configuration de git::

  git config --global user.name "VincentP"
  git config --global user.email vincent.picavet@oslandia.com

Il est également possible de configurer ces champs pour chaque dépôt en utilisant::

    $ cd my_other_repo
    $ git config user.name "Different Name"
    $ git config user.email "differentemail@email.com"

Créer un compte GitHub
^^^^^^^^^^^^^^^^^^^^^^

Il faut au préalable créer un compte GitHub sur http://www.github.com

Puis dans "Account Settings" > "SSH Public Keys" > "Add another public key"

Ouvrez le fichier id_rsa.pub avec un éditeur de texte. C'est votre clef SSH publique. Vous aurez peut être à activer l'affichage des fichiers cachés car le répertoire .ssh est un répertoire caché. Il est important de copier la clef SSH exactement telle qu'elle est dans le fichier sans ajouter de retour à la ligne ni d'espace.

On la copie dans le champ "Key" sur GitHub et on clique sur "Add key".

Pour tester on se connecte au serveur ssh de GitHub en utilisant la commande shell suivante (telle quelle)::

    $ ssh -T git@github.com

On obtient::

    The authenticity of host 'github.com (207.97.227.239)' can't be established.RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.Are you sure you want to continue connecting (yes/no)?

Ce qui est normal, il faut répondre *yes*. On obtient alors::

    Hi username! You've successfully authenticated, but GitHub does not provide shell access.

Si vous avez correctement réglé git comme ci-dessus, vous pouvez maintenant créer un dépot dans GitHub et y pousser un projet, ou forker un projet existant et y faire des modifications.

Créer un compte Hub QGIS
^^^^^^^^^^^^^^^^^^^^^^^^

Pour pouvoir interagir avec la plateforme de développement QGIS, il faut tout d'abord créer un compte OSGeo. Cela peut se faire à l'adresse suivante : https://www2.osgeo.org/cgi-bin/ldap_create_user.py

La page centrale du Hub QGIS est à http://hub.qgis.org

Il est ensuite possible de créer un nouveau projet sur le hub à l'adresse http://hub.qgis.org/projects/new

Des options permettent d'activer les diverses fonctionnalités voulues pour l'interface de gestion de projet. On y trouve :

* un bugtracker (avec gestion de bounty ou de feature en plus des bugs)
* Des champs spécifiques pour la gestion du bug
* un dépot de fichier
* un calendrier
* un Wiki

Lorsqu'on crée un projet on peut activer le dépôt de code, et choisir git comme gestionnaire de code source.

Ensuite dans la page du projet on accède à l'onglet *Repository* qui donne les instructions pour créer le dépôt *git*.

* configuration de la gestion des permissions
  * Upload de la clé publique ssh. À l'adresse http://hub.qgis.org/my/public_keys vous pouvez comme pour GitHub envoyer votre clef publique (cliquer sur New Value).
  * ajout des membres développeurs (dans l'onglet settings/members du projet, éditer l'utilisateur ou en ajouter un)

* création du dépôt et envoi vers le hub

::

  cd pyqgis-tutofr
  git init
  git add .
  git commit -m 'Initializing Tutoriel Python QGIS repository'
  git remote add origin gitosis@qgis.org:pyqgis-tutofr.git
  git push origin master

Si on a déjà un dépôt git existant et que l'on souhaite le pousser vers le projet sur le hub qgis::

  cd existing_git_repo
  git remote add origin gitosis@qgis.org:pyqgis-tutofr.git
  git push origin master

On peut alors voir que le projet est bien en ligne sur le Hub, et utiliser l'interface de gestion de projet pour collaborer.

Si votre projet est un plugin, il faut créer un sous-projet du projet global "User Plugins".

Distribuer avec le dépôt centralisé de plugins
-----------------------------------------------

Maintenant que notre projet est développé, et possède un environnement de développement correct, nous pouvons distribuer notre plugin. Le site http://plugins.qgis.org/ regroupe tous les plugins de QGIS et permet de faire de la recherche par mot-clef, d'évaluer les plugins suivant leur état de développement, leur popularité, etc.

Le site regroupe également des snippets de code Python qui peuvent être intéressant à partager.

Le login se fait avec le compte OSGeo.

Pour uploader un plugin, le bouton "Share a plugin" permet d'accéder à la page.
On peut ensuite envoyer le fichier zip contenant notre plugin vers le site pour que les utilisateurs puissent le charger. On peut vérifier qu'il apparaît bien dans la liste des plugins de l'installateur de plugins de QGIS. 
