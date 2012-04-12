==============================================
Tutorial #1 -- Installation de Plugins QGIS
==============================================

Observons rapidement comment on installe des plugins Python. Nous ajouterons aussi le dépôt PyQGIS FOSS4G.

\  **1.** \Sur la barre de menu QGIS cliquer sur\  ``Extensions > Installateur d'extensions Python`` \:

.. image:: ../_static/plugins_menu_click_1.png
    :scale: 100%
    :align: center

\  **2.** \Une nouvelle boite de dialogue s'ouvre et tente de récupérer les extensions Python à partir de dépôts tierces. Si il n'arrive pas à récupérer tous les plugins il peut bloquer. Cliquer sur le bouton \ ``Abandonner la recherche de dépôt`` \si cela commence à bloquer:

.. image:: ../_static/Abort_Fetching.png
    :scale: 100%
    :align: center 

\  **3.** \Maintenant vous devriez voir une liste des plugins Python disponibles pour l'installation. Si les dépôts tierces ne sont pas activés, peu de plugins sont disponibles. Pour les activer, il faut cliquer sur l'onglet\  ``Dépôts`` \. Il liste l'ensemble des dépôts où QGIS va chercher les plugins. Le bouton du bas permet d'ajouter les dépôts non officiels du projet :

.. image:: ../_static/add_3rd_partyplugins_new.png
    :scale: 100%
    :align: center

\  **4.** \Nous allons ajouter un nouveau dépôt. Ce dépôt contient le code d'exemple pour ce tutoriel. Cliquer sur le bouton \ ``Ajouter`` \ en bas à droite de l'onglet \ ``Dépôts`` \. Ensuite ajouter l'URL suivante et un nom pour ce dépôt::

    http://www.qgisworkshop.org/plugins/plugins.xml

.. image:: ../_static/add_repo.png
    :scale: 70%
    :align: center

.. image:: ../_static/add_repo_url.png
    :scale: 70%
    :align: center

.. note:: Vous pouvez aussi ouvrir l'adresse du dépôt avec un\  `navigateur web <http://www.qgisworkshop.org/plugins/plugins.xml>`_ \

\  **5.** \Si vous revenez à l'onglet\  ``Extensions`` \ vous pouvez alors filtrer avec la liste déroulante sur le dépôt ajouté, à côté de la boîte de texte de filtre:

.. image:: ../_static/filter_foss4g.png
    :scale: 70%
    :align: center

\  **6.** \Selectionnez chaque plugin de ce dépôt et cliquer sur\  ``Installer l'extension`` \en bas à droite:

.. image:: ../_static/install_foss4g_plugin.png
    :scale: 70%
    :align: center

\  **7.** \Dans le shell bash ou dans un explorateur de fichiers, déplacez vous dans \  ``/home/formation/.qgis/python/plugins`` \. Le code des plugins devrait être présent à cet endroit::

    $ cd /home/formation/.qgis/python/plugins/
    $ ls -lah
    total 28K
    drwxr-xr-x 7 formation formation 4.0K 2011-09-02 10:24 .
    drwxr-xr-x 4 formation formation 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x 2 formation formation 4.0K 2011-09-02 10:21 foss4g2011_example1_starter
    drwxr-xr-x 2 formation formation 4.0K 2011-09-02 10:21 foss4g2011_example1_solution
    drwxr-xr-x 2 formation formation 4.0K 2011-09-02 10:21 foss4g2011_example2_starter
    drwxr-xr-x 2 formation formation 4.0K 2011-09-02 10:21 foss4g2011_example2_solution
    drwxr-xr-x 2 formation formation 4.0K 2011-09-02 10:24 foss4g2011_example3_starter
    drwxr-xr-x 2 formation formation 4.0K 2011-09-02 10:24 foss4g2011_example3_solution
    drwxr-xr-x 2 formation formation 4.0K 2011-09-02 10:21 foss4g2011_tutorial1_solution
    drwxr-xr-x 3 formation formation 4.0K 2011-07-07 13:41 pluginbuilder

\  **8.** \Pour activer ou désactiver un plugin l'interface dédiée est accessible en cliquant sur\  ``Extensions > Gérer les extensions`` \. La boite de dialogue de gestion des plugins de QGIS apparait alors avec des cases à cocher à côté des plugins pour les activer ou les désactiver:

.. image:: ../_static/plugin_manager_console.png
    :scale: 100%
    :align: center
