
=====================================
Python dans QGIS
=====================================

Lorsqu'on utilise le terme \ **PyQGIS** \on se réfère aux *bindings* Python pour QGIS. Plus spécifiquement on se rapporte à l'API (Application Programming Interface) Python qui enrobe la bibliothèque QGIS. La \   `documentation de l'API C++ QGIS <http://qgis.org/api>`_ \est disponible en ligne.

.. image:: ../_static/pyqgis_tools.png
    :scale: 80%
    :align: center

Nous allons utiliser la documentation de l'API C++ QGIS comme un guide pour comprendre PyQGIS car il n'y a pas de documentation de l'API PyQGIS. Cela peut être perturbant parfois. Mais pour la plus grande partie les bindings Python sont un mirroir de la bibliothèque C++.

Nous allons devenir très familiers avec certaines parties de la documentation citée au fur et à mesure que nous construisons des plugins. Pour le moment il suffit de noter qu'il y a plusieurs moyen d'intéragir avec QGIS en utilisant Python:

    1. \  **Plugins** \: Créer/étendre les outils qui interagissent avec les données dans l'environnement QGIS.

    2. \  **Python Console** \: Un terminal en ligne de commande dans QGIS pour tester des idées et faire des tâches non répétitives.

    3. \  **Python Scripts/Applications** \: Écrire des applications Python à partir de zéro qui sont construites sur la base des bibliothèques QGIS et Qt. Ces applications pourraient traiter des données spatiales en dehors de l'application QGIS, mais utilisent en réalité les fonctions du cœur sous le capot. Un exemple serait de construire un visualiseur QGIS simplifié avec un ensemble d'outils très limité pour un traitement particulier.

Nous nous concentrerons par la suite sur l'installation des plugins ainsi que l'utilisation de la console Python. Tout ce que nous allons apprendre sera directement applicable au développement de plugin pour le reste du tutoriel.

------------------------------------------------------

QGIS Plugins
------------------------------

À partir de QGIS on peut installer des extensions tierces depuis de nombreuses sources, qu'elles soient publiques ou privées.

Le premier tutoriel qui suit présente la base de l'ajout de dépôt de plugins et des plugins eux-mêmes à QGIS.

------------------------------------------------------

Console Python
------------------

C'est peut être la façon la plus simple de tester vos idées de plugin.

À partir de la Console Python on peut accéder aux couches vecteur et raster qui sont déjà chargées dans QGIS. Une fois accédées, on peut commencer à interagir avec leurs attributs et la géométrie. Comme un besoin récurrent de nombreux plugins est de travailler avec les attributs d'une couche et leur géométrie, commençons par là.

Le second tutoriel qui suit détaille un certain nombre d'exemples de blocs de code.


