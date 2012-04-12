=====================================
Architecture de plugin
=====================================

Les extensions (plugins) Python de QGIS sont un ensemble de module Python qui décrivent l'intégralité de ce qui est nécessaire pour une fonctionnalité, des ressources du plugin, jusqu'au code qui donne la logique du plugin. Nous verrons les détails plus bas, mais voici un aperçu des fichiers qu'on y retrouve.

Pour créer des plugins Python QGIS vous allez avoir besoin d'au moins 4 types de fichier dans votre projet (la plupart des plugins en contient plus):
    - un fichier avec une extension ``.ui`` qui décrit votre interface graphique (GUI). Il doit être compilé en un module Python en utilisant l'outil en ligne de commande \ ``pyuic4``\.
    - un fichier qui donne des informations générales de configuration sur votre plugin tel que son nom et son auteur\ ``__init__.py``\.
    - un fichier avec une extension\ ``.qrc``\ décrivant les ressources que votre plugin va utiliser tels que les images. Ce fichier doit être compilé en un module Python en utilisant l'outil en ligne de commande\ ``pyrcc4``\.
    - enfin, le fichier qui effectue le réel travail. Ce fichier est juste un module Python normal avec quelques import spécifiques et des noms de méthodes standardisées. Il peut être nommée comme on le souhaite, même si le nom du fichier est généralement associé au nom du plugin.

-----------------------------

Pour avoir une meilleure idée de comment ces différents fichiers composent un projet de plugin, on peut regarder un plugin Python qui est déjà installé sur le système.

\  **1.** \Ouvrir un shell bash. Le shell bash, ou terminal, est disponible dans le menu de la distribution. On obtient une fenêtre avec un curseur clignotant.

.. image:: ../_static/terminal_window_open.png
    :scale: 70%
    :align: center

\  **2.** \Allons dans le répertoire caché\  ``.qgis`` \qui se trouve dans votre répertoire personnel. Dans ce répertoire se trouvent les plugins Python de QGIS. On peut les lister :

::
	
    $cd .qgis/python/plugins/
    $ ls -lah
    total 17K
    drwxr-xr-x 10 formation formation 4.0K 2011-07-17 20:40 .
    drwxr-xr-x  4 formation formation 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x  3 formation formation 4.0K 2011-07-07 13:41 pluginbuilder
    

Le projet\  **pluginbuilder** \situé dans\ ``/home/formation/.qgis/python/plugins`` \est un plugin avec lequel nous allons nous familiariser sous peu. Il rend la création de plugins plus simlpe en créant les modèles de fichiers automagiquement (les fichiers cités précedemment).Le\  **pluginbuilder** \ajoute aussi du code dans ces modèles, que nous allons pouvoir modifier ensuite.


\  **3.** \Changez de répertoire en entrant dans\  ``pluginbuilder`` \et affichez uniquement les fichiers d'extension\  ``(.ui, .py and .qrc)`` \comme ci-dessous. La raison pour laquelle nous ne visualisons que ces fichiers est pour exclure les modules Python compilés -- ceux avec une extension\  ``.pyc`` \ :

::
	
    $ cd pluginbuilder
    $ ls -l *.py *.ui *.qrc
    -rw-r--r-- 1 formation formation  1586 2011-07-07 13:41 __init__.py
    -rw-r--r-- 1 formation formation  1403 2011-07-07 13:41 pluginbuilder_dialog.py
    -rw-r--r-- 1 formation formation  7077 2011-07-07 13:41 pluginbuilder.py
    -rw-r--r-- 1 formation formation  2232 2011-07-07 13:41 pluginspec.py
    -rw-r--r-- 1 formation formation 22936 2011-07-07 13:41 resources.py
    -rw-r--r-- 1 formation formation   143 2011-07-07 13:41 resources.qrc
    -rw-r--r-- 1 formation formation  1373 2011-07-07 13:41 result_dialog.py
    -rw-r--r-- 1 formation formation  8718 2011-07-07 13:41 ui_pluginbuilder.py
    -rw-r--r-- 1 formation formation  7046 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r-- 1 formation formation  1734 2011-07-07 13:41 ui_results.py
    -rw-r--r-- 1 formation formation  1880 2011-07-07 13:41 ui_results.ui


Notez que nous nous intéressons uniquement aux types de fichiers ici. Comme on peut le voir, il semble y avoir 2 GUIs associés à ce plugin. On le voit car il y a deux fichirs avec une extension\  ``.ui`` \::

    -rw-r--r--  1 formation formation 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 formation formation 1.9K 2011-07-07 13:41 ui_results.ui

On peut aussi voir que chacun des fichiers\  ``.ui`` \a été compilé en un module Python avec le même nom de base. D'expérience, on sait que si le mot\  ``dialog`` \apparait dans un module Python c'est un fichier qui fonctionne avec le fichier d'interface graphique\  ``ui.py`` \. Donc l'ensemble de ces fichiers semble être lié à la GUI::

    -rw-r--r-- 1 formation formation  1373 2011-07-07 13:41 result_dialog.py
    -rw-r--r-- 1 formation formation 1.4K 2011-07-07 13:41 pluginbuilder_dialog.py
    -rw-r--r--  1 formation formation 8.6K 2011-07-07 13:41 ui_pluginbuilder.py
    -rw-r--r--  1 formation formation 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 formation formation 1.7K 2011-07-07 13:41 ui_results.py
    -rw-r--r--  1 formation formation 1.9K 2011-07-07 13:41 ui_results.ui

Remarquez le fichier\  ``__init__.py`` \. Si vous ouvrez ce fichier et que vous regardez le contenu, vous verrez la description générale du plugin comme les noms et les numéros de version::

    def name():
        return "Plugin Builder"
    def description():
        return "Creates a QGIS plugin template for use as a starting point in plugin development"
    def version():
        return "Version 0.3.2"
    def icon():
        return 'plugin_builder.png'
    def qgisMinimumVersion():
        return "1.0"
    def classFactory(iface):
        # load PluginBuilder class from file PluginBuilder
        from pluginbuilder import PluginBuilder
        return PluginBuilder(iface)

On voit aussi qu'il y a des fichiers de ressource associés avec le projet. Il faut noter que les fichiers\  ``.qrc`` \ doivent être compilés en un module Python. Ce sont les fichiers::

    -rw-r--r--  1 formation formation  23K 2011-07-07 13:41 resources.py
    -rw-r--r--  1 formation formation  143 2011-07-07 13:41 resources.qrc

Ceci fait, on peut deviner que tous les autres fichiers avec une extension\  ``.py`` \dont nous n'avons pas encore parlé est lié à la logique du plugin. Il semblo aussi y avoir des documents et des images dont nous ne nous préoccupons pas encore.


