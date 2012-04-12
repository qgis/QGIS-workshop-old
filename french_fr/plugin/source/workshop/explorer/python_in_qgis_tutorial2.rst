====================================================
Tutoriel #2 -- Exploration de la Console Python QGIS
====================================================


Mise en place
-------------

\  **1.** \Pour commencer, ouvrir une nouvelle session QGIS en cliquant sur l'icône de QGIS dans la barre de menu, ou en lançant QGIS à partir d'un terminal. Les données que nous utiliserons sont situées dans le répertoire\ ``natural_earth_50m`` \ dans votre espace personnel::

    /home/formation/natural_earth_50m

\  **2.** \Ajouter les fichiers raster et vecteur suivant à QGIS::

    /home/formation/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif
    
    # Désactiver la couche tif pour qu'elle ne ralentisse pas l'affichage

    /home/formation/natural_earth_50m/cultural/50m_cultural/50m_populated_places_simple.shp

\  **3.** \Ouvrir la Console Python en sélectionnant le menu::

    Extensions > Console Python

.. image:: ../_static/python_console.png
    :scale: 100%
    :align: center

------------------------------------------------------

Accéder aux couches
--------------------------

.. note:: Les liens qui suivent référencent tous la\  `documentation de l'API QGIS <http://doc.qgis.org>`_ \. Cliquer dessus pour voir les classes et les méthodes que nous utiliserons ci-dessous.

Il y a plusieurs manières d'accéder aux couches dans QGIS. Chaque foçon commence par une référence à la \ `classe QgisInterface <http://doc.qgis.org/head/classQgisInterface.html>`_ \qui est appelée\ **iface** \dans les bindings Python. À partir de la Console Python on peut accéder à\\ **iface** \en appelant la commande suivante::
    
    >>> qgis.utils.iface

Entrer la commande suivante dans la Console Python et vous devriez voir ce résultat::    

    >>> qgis.utils.iface
    <qgis.gui.QgisInterface object at 0x925266c>

Exécuter la commande précédente donne le nom réel de la classe QGIS avec laquelle nous travaillons -- en effet iface est en réalité l'objet QgisInterface.    

Methode 1
*********

Dans la classe iface, une fonction utile qui retourne une référence à la couche selectionnée dans la liste des couches, s'appelle\  `activeLayer() <http://doc.qgis.org/head/classQgisInterface.html#231f32fbf95004aebb067cb98f3a391c>`_ \.

\  **1.** \Exécuter la commande suivante::

    >>> aLayer = qgis.utils.iface.activeLayer()
    >>> aLayer
    <qgis.core.QgsRasterLayer object at 0x99ea6ec>

Selon quelle couche est selectionnée dans la liste de couche, vous allez voir soit un résultat en couche raster soit en couche vecteur. Ici la couche raster était selectionnée.    

\  **2.** \Quel est le nom de la couche active?::

    >>> aLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

\  **3.** \Comment peut on avoir une idée de quelles fonctions cet objet Python propose ? Il y a deux manières:

    \1) La façon la plus agréable de naviguer dans les attributs des classes est d'aller sur la\  `documentation de l'API QGIS <http://doc.qgis.org>`_ \et de chercher la classe avec laquelle vous travaillez.

    \2) La façon Python (moins visuelle) est de lancer la commande suivante sur un objet pour lequel vous voulez avoir des informations::
        
            >>> help(aLayer) 

             # Sortie tronquée pour la démo
             ...
             |  extent = <built-in function extent>
             |  
             |  getLayerID = <built-in function getLayerID>
             |  
             |  getTransparency = <built-in function getTransparency>
             ...
             # Sortie tronquée pour la démo

La pile de texte sortie sur le shell est difficile à naviguer. Ci dessus est représenté quelques un des attributs que vous pouvez voir. Il est certainement mieux d'utiliser le lien proposé auparavant.

Methode 2
**********

\  **1.** \Un autre moyen classique d'accéder à la couche sélectionnée dans la liste des couches est de la récupérer en utilisant\  `QgsMapCanvas <http://doc.qgis.org/head/classQgsMapCanvas.html>`_ \. La classe mapCanvas a de nombreuses fonctions utiles::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> cLayer = canvas.currentLayer()
    >>> cLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Methode 3
**********
\  **1.** \Avec la classe map canvas, on peut récupérer plus que juste la couche active -- en fait on peut tout récupérer::

    >>> allLayers = canvas.layers()
    >>> for i in allLayers: print i.name()
    ... 
    50m_populated_places_simple

**Une seconde!** \Nous avons deux couches dans notre liste de couche. Pourquoi est ce qu'on ne récupère qu'un seul nom ? (en assumant que vous avez suivi les instructions et que vous avez bien désactivé l'affichage de la couche raster. Sinon vous aurez les deux noms)

Il s'avère qu'en utilisant la méthode\  ``QgsMapCanvas.layers()`` \, on ne récupère que les couches\ **visibles** \, c'est à dire celles qui sont cochées comme telles dans la liste des couches.

\  **2.** \Cocher la couche raster dans la liste des couches. Relancer les mêmes instructions dans la Console Python::

    >>> allLayers = canvas.layers()
    >>> for i in allLayers: print i.name()
    ... 
    50m_populated_places_simple
    SR_50M

Maintenant nous devrions voir les deux noms de couches affichés. 

Methode 4
**********

Il est parfois utile d'accéder aux couches dans l'ordre dans lequel ils sont listés dans la liste des couches. Les couches sont empilées de haut en bas et accédées à l'aide d'un index à base 0. Cela signifie que la première couche (celle la plus haute) commence à l'indice 0.

\  **1.** \On accède aux couches en utilisant la fonction\  `QgsMapCanvas.layer() <http://doc.qgis.org/head/classQgsMapCanvas.html#de2251f2227bc0f0efefd09810a193cd>`_ \et on lui passe l'entier désignant l'indice de la couche que nous voulons::

    >>> canvas.layer(0)
    <qgis.core.QgsVectorLayer object at 0x99eaeec>
    >>> canvas.layer(0).name()
    PyQt4.QtCore.QString(u'50m_populated_places_simple')    


Autres exercices
********************

- Régler la couche active en utilisant\  `qgis.utils.iface.setActiveLayer() <http://doc.qgis.org/head/classQgisInterface.html#c42281407013002b56ff7ed422c77336>`_

- Régler la couche courant en utilisant\  `qgis.utils.iface.mapCanvas().setCurrentLayer() <http://doc.qgis.org/head/classQgsMapCanvas.html#001c20fe97f844542895e718ee166926>`_ 

- Pouvez vous trouver la classe QgsMapLayer dans la documentation et identifier comment obtenir l'étendue d'une couche ?

.. note:: Il y a d'autres moyens d'accéder aux couches de la liste de couche QGIS. Donc gardez l'oeil ouvert pour identifier d'autres méthodes.

------------------------------------------------------

Charger des couches dans QGIS
-----------------------------

Vous avez peut-être remarqué en cherchant QgisInterface qu'il y avait quelques méthodes addLayer ? Utilisons les pour charger des couches dans QGIS.

\  **1.** \Commencez par désactiver toutes les couches actuellement dans QGIS en les décochant. Ensuite avec une carte vide, ré-ajoutez SR_50M et les données de lieux peuplés avec un nom différent::

    >>> qgis.utils.iface.addVectorLayer("/home/formation/natural_earth_50m/cultural/50m_cultural/50m_populated_places_simple.shp", "pop2", "ogr")
    <qgis.core.QgsVectorLayer object at 0xca0feac>
    >>> qgis.utils.iface.addRasterLayer("/home/formation/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif", "raster")
    <qgis.core.QgsRasterLayer object at 0xca0fe6c>

La méthode\  `addVectorLayer <http://doc.qgis.org/head/classQgisInterface.html#39be50fe9974de17177861ad89e7f36e>`_ \prend trois arguments:

    - le premier argument est le chemin vers la source de données -- le shapefile dans notre cas

    - le second argument est le nom -- le nom que la couche prend dans la liste de couche 

    - Le troisième argument est la clé de la source. La fonction veut savoir quel driver il faut utiliser pour charger la donnée. Pour nos besoins, "ogr" sera utilisé la plupart du temps avec les données vectorielles.

Remarquez que\  `addRasterLayer <http://doc.qgis.org/head/classQgisInterface.html#808a34b507a8c4204d607a5857d62748>`_ \prend seulement deux arguments -- le chemin est le nom de la couche.

Si vous regardez la définition de la fonction\ **addRasterLayer** \dans la page ci dessus vous remarquerez qu'il y a deux définitions de fonctions surchargées pour ajouter des rasters. Une des définitions prend deux arguments (celle utilisée). L'autre prend des arguments supplémentaires.

Ajouter une couche PostGIS
**************************

Vous pouvez vous demander comment ajouter des données qui sont stockées dans PostGIS. Il vous faudra disposer d'une installation de PostGIS avec quelques donnés vecteur déjà chargées pour faire cette partie.

Accéder à des données vecteur PostGIS utilise la même fonction déjà utilisée ci dessu --\  `addVectorLayer <http://doc.qgis.org/head/classQgisInterface.html#39be50fe9974de17177861ad89e7f36e>`_ \. La spécification du chemin par contre est un peu différente.

QGIS supporte le concept d'URIs (Uniform Resource Identifier) comme description de source de données pour gérer les entrées à partir de bases de données, CSVs et fichiers GPX. L'URI que l'on passe pour la base de données contient des paramètres tels que le nom de la base de donnée, le nom d'utilisateur, le mot de passe et le port sur lequel elle tourne (entre autres).

\  **1.** \Chargeons les polygones de pays à partir de PostgreSQL::

    >>> uri = QgsDataSourceURI()
    >>> uri.setConnection("localhost", "5432", "qgis_workshop", "qgis", "qgis")
    >>> uri.setDataSource("public", "countries", "the_geom")
    >>> uri.uri()
    PyQt4.QtCore.QString(u'dbname=\'qgis_workshop\' host=localhost port=5432 user=\'qgis\' password=\'qgis\' table="public"."countries" (the_geom) sql=')
    >>> qgis.utils.iface.addVectorLayer(uri.uri(), "all_these_countries", "postgres")
    <qgis.core.QgsVectorLayer object at 0xca0feac>

On devrait maintenant avoir la couche de pays chargée dans QGIS.    

.. image:: ../_static/postgres_countries_layer.png
    :scale: 43%
    :align: center

------------------------------------------------------

Accéder à la géométrie des vecteurs
-------------------------------------------------------------

Nous pouvons maintenant commencer à faire des choses amusantes -- jouer avec les géométries

La classe\  `QgsGeometry <http://doc.qgis.org/head/classQgsGeometry.html>`_ \est une des plus importantes à étudier dans l'API QGIS. Elle contient les prédicats spatiaux de base et les opérations sur les données vecteur auxquelles nous sommes tous habitués.

Par exemple, avec la référence à la géométrie d'un objet, on peut accéder à ces opérations spatiales (non exhaustif):
    - buffer
    - intersection
    - combine
    - difference 

Géométrie d'une couche vecteur
********************************************

Il y a plusieurs façons d'accéder aux features d'une couche et à la géométrie d'une feature unique. Nous n'allons\ **PAS** \les détailler toutes.

Methode 1
**********

Une des façons d'accéder aux features d'une couche se fait au moyen de la classe\  `QgsVectorDataProvider <http://doc.qgis.org/head/classQgsVectorDataProvider.html>`_ \. Vous pouvez obtenir une référence à une source de données directement à partir de la classe\  `QgsVectorLayer <http://doc.qgis.org/head/classQgsVectorLayer.html>`_ \.

\  **1.** \Premièrement, supprimez toutes les couches de QGIS


\  **2.** \Ensuite ajoutez la couche\  ``50m_admin_0_countries.shp`` \située ici::

    /home/formation/natural_earth_50m/cultural/50m_cultural/50m_admin_0_countries.shp

\  **3.** \Ouvrez la Console Python. Récupérez une référence à la couche courante::

    >>> cLayer = qgis.utils.iface.mapCanvas().currentLayer()
    >>> cLayer.name()
    PyQt4.QtCore.QString(u'50m_admin_0_countries')

\  **4.** \Récupérez une référence à la source de données (data provider)::

    >>> provider = cLayer.dataProvider()
    >>> provider.name()
    PyQt4.QtCore.QString(u'ogr')

Si il s'agissait d'une couche vecteur de postgresql alors le \ ``provider.name()`` \ "postgres" serait retourné.

\  **5.** \Un des moyen d'accéder aux features d'une couche vecteur est à travers de la fonction\  `select() <http://doc.qgis.org/head/classQgsVectorDataProvider.html#ed7343c5ccea4d4fe795159eb4268b96>`_ \du data provider::

    >>> provider.select()

La fonction\  ``select()`` \lit les attributs de la couche et la géométrie afin que l'on puisse y accéder. Si vous regardez\  `select() API <http://doc.qgis.org/head/classQgsVectorDataProvider.html#ed7343c5ccea4d4fe795159eb4268b96>`_ \vous remarquerez qu'on peut spécifier plus finement ce que l'on veut récupérer de la couche en incluant seulement certains attributs.

Lorsqu'on exécute\  ``select()`` \sans arguments on utilise les options par défaut. Les options par "défaut" signifie dans ce cas précis::

    - Attributes -- Ne récupérer aucun attribut
    - Rectangle Filter -- Ne pas utiliser de filtre spatial rectangulaire (bounding box)
    - Geometry -- Récupérer toutes les géométries des features
    - Intersection Test -- Ne pas faire de test d'intersection précis

En résumé, lorsqu'on exécute\  ``select()`` \on récupère toutes les géométries des features mais aucun attribut.

\  **6.** \Maintenant récupérons l'identifiant d'une feature et sa géométrie::

    >>> feat = QgsFeature()
    >>> # Ci dessus on a une QgsFeature vide jusqu'a ce qu'on la passe au provider
    >>> provider.nextFeature(feat)
    True
    >>> feat.id()
    0
    >>> feat.geometry()
    <qgis.core.QgsGeometry object at 0xca0fdec>
    >>> cLayer.setSelectedFeatures([0])

Le code précédent récupère la première feature depuis notre source de données -- une feature avec un featureID à 0.

On a ensuite utilisé\  `QgsFeature.geometry() <http://doc.qgis.org/head/classQgsFeature.html#b0a934a1b173ce5ad8d13363c20ef3c8>`_ \pour obtenir sa géométrie.

Finalement, on a utilisé la référence à la couche courante pour sélectionner cette feature dans QGIS.

\  **7.** \Ouvrons la table des attributs de la couche et cliquons sur l'icone 'zoomer sur l'entité selectionnée' en bas à gauche.

.. image:: ../_static/zoom_to_selected_feature.png
    :scale: 100%
    :align: center

Il semble que l'ile d'Aruba a un featureID à 0.

.. image:: ../_static/get_geometry_select_aruba.png
    :scale: 43%
    :align: center

Methode 2
**********

Bien que nous ne l'ayons pas utilisé ci dessus, nous allons utiliser souvent\  ``QgsVectorDataProvider`` \avec une instruction\  ``while`` \ pour boucler sur toutes les features d'une couche. Dans ces cas le traitement à effectuer concernera probablement toutes les features. Cependant il y a d'autres traitements pour lesquels vous avez déjà un identifiant de feature. Dans ces cas ci, vous voudrez récupérer une unique feature avec ses attributs et sa géométrie en utilisant quelque chose de similaire à la fonction\  ``select()`` \. Voici comment faire.

La fonction\  `featureAtId() function <http://doc.qgis.org/head/classQgsVectorDataProvider.html#583a432e2e1046392abf79bf1e58f404>`_ \ de la classe QgsVectorDataProvider ressemble à la fonction select avec des arguments différents::

    ## Arguments
    - featureID -- L'identifiant de la feature que vous souhaitez récupérer
    - feature -- Une QgsFeature vide que vous passez à la fonction pour l'initialiser
    - fetchGeometry -- une valeur booléenne qui spécifie si vous voulez la géométrie ou pas (True par défaut)
    - attributeList -- Une liste contenant les indexes des champs attributaires à copier (liste vide par défaut -- pas d'attributs)

\  **1.** \Si nous ne voulons pas les attributs de la feature, alors on peut ignorer les deux derniers paramètres. Lancez cette commande pour obtenir la feature Aruba de nouveau::

    >>> feat = QgsFeature()
    >>> provider.featureAtId(0, feat)
    True


Types de Geometrie
******************

\  **2.** \Avec une référence à une géométrie, on peut faire des contrôle de qualité pour être sur que l'on veut utiliser cette géométrie dans les traitements futurs::

    >>> feat.geometry().asPolygon()
    [[(-69.8991,12.452), (-69.8957,12.423), (-69.9422,12.4385), (-70.0041,12.5005), (-70.0661,12.547), (-70.0509,12.5971), (-70.0351,12.6141), (-69.9731,12.5676), (-69.9118,12.4805), (-69.8991,12.452)]]
    >>> feat.geometry().length()
    0.53411147802819525
    >>> feat.geometry().area()
    0.012862549465307641
    >>> feat.geometry().isGeosValid()
    True
    >>> feat.geometry().isGeosEmpty()
    False
    >>> feat.geometry().isMultipart()
    False

Cette géométrie est valide, non vide, et a l'air d'être un Polygon simple (par opposition à un MultiPolygon).    

\  **3.** \Pour être sur que cette géométrie est du 'type' que nous attendons on peut utiliser ces méthodes pour faire le contrôle qualité::

    >>> feat.geometry().wkbType()
    3
    >>> QGis.WKBPolygon
    3
    
Notons quelques détails. Les types de géométrie renvoient un entier (en fait un identifiant) qui détaille quelle géométrie ils représentent. Il y a deux façons de vérifier les types de géométrie:    

    \A. Ci dessus on utilise la fonction\  `QGis.WkbType() <http://doc.qgis.org/head/classQGis.html#8da456870e1caec209d8ba7502cceff7>`_ \pour comparer les types well-known-binary

    \B. Ou on peut utiliser la fonction\  `QGis.type() <http://doc.qgis.org/head/classQGis.html#09947eb19394302eeeed44d3e81dd74b>`_ \pour comparer avec les types basiques de QGIS::

        >>> feat.geometry().type()
        2
        >>> QGis.Polygon
        2

\  **4.** \Maintenant faisons une opération spatiale très simple comme un buffer::

    >>> buff_geom = feat.geometry().buffer(12, 2)
    >>> buff_geom.asPolygon()
    [[(-78.2223,4.28234), (-81.4729,8.82057), (-81.5448,16.0456), (-81.5295,16.0957), (-78.8639,20.7414), (-78.8482,20.7585), (-71.1219,24.5648), (-62.8358,22.2146), (-62.7738,22.1681), (-60.16,19.4743), (-60.0987,19.3872), (-58.9469,17.356), (-58.9342,17.3275), (-57.9838,13.875), (-57.9804,13.8461), (-59.6758,6.13379), (-65.7966,1.14483), (-73.6923,1.03945), (-73.7388,1.05495), (-77.0515,3.10271), (-77.2035,2.90002), (-77.2655,2.94651), (-77.6363,3.46418), (-78.4274,3.95324), (-78.4894,4.01522), (-78.2223,4.28234)]]
    >>> buff_geom.area()
    430.95305806853509

Nous avons fait un buffer de 12 degrés. On peut voir que cela a créé plus de point dans la liste des coordonnées du polygone. En calculant l'aire on peut aussi vérifier qu'on a bien étendu notre polygone. Pour en être surs::    

    >>> buff_geom.area() > feat.geometry().area()
    True

\  **5.** \En dernier exemple, testons la géométrie d'Aruba par rapport à un point d'intersection géométrique QgsPoint::

    >>> # Est ce qu'Aruba a une intersection avec Seattle (-122.361,47.642) -- espérons que non !
    >>> feat.geometry().intersects(QgsGeometry.fromPoint(QgsPoint(-122.361,47.642)))
    False
    >>> # Est ce qu'Aruba a une intersection avec un point situé à l'intérieur ? -- le vrai test
    >>> feat.geometry().intersects(QgsGeometry.fromPoint(QgsPoint(-69.953,12.512)))
    True

------------------------------------------------------

Accéder aux attributs des données
---------------------------------

Ici nous allons couvrir la récupération des données attributaire pour les couches raster et vecteur. Les exercices suivants vont nous aider à répondre aux questions:

    \1) Quel est le nom de la feature selectionnée ?

    \2) Quelle est la valeur de ce pixel raster ?

    \3) Combien de features correspondent à ce filtre attributaire ?
 
Vecteur
**********

On utilise notre couche\  ``50m_admin_0_countries.shp`` \:

\  **1.** \Obtenons le data provider pour ce shapefile::

    >>> provider = aLayer.dataProvider()
    >>> aLayer = qgis.utils.iface.activeLayer()
    >>> provider = aLayer.dataProvider()
    >>> aLayer.name()
    PyQt4.QtCore.QString(u'50m_admin_0_countries')
    >>> provider.name()
    PyQt4.QtCore.QString(u'ogr')

\  **2.** \Récupérons un dictionnaire Python des champs attributaires::

    >>> columns = provider.fields()
    >>> type(columns)
    <type 'dict'>

\  **3.** \Souvenez vous que le type de données dictionnaire de Python est un ensemble de clés et de valeurs. La fonction\  ``provider.fields()`` \ retourne l'indice positionnel (à base 0) des objets colonne de gauche à droite. Cela signifie que la colonne (le champs attributaire) le plus à gauche commence à 0. Chaque indice entier pointe vers un objet\  `QgsField object <http://doc.qgis.org/head/classQgsField.html>`_ \Par exemple::

    >>> columns[0]
    <qgis.core.QgsField object at 0xd8df66c>

Le résultat ci dessous ne nous aide pas beaucoup pour le moment. Pour avoir des informations utiles sur les colonnes il faut accéder aux attributs et aux fonctions de l'objet QgsField lui même (nous ferons cela en deux étapes).

\  **4.** \Notez que \ **TOUTES** \les clés ou les valeurs d'un dictionnaire peuvent être obtenus sous forme de liste grâce à une de ces fonctions::

    >>> columns.keys()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    >>>
    >>> columns.values()


\  **5.** \Pour itérer dans les clés et les valeurs en une seule fois on peut faire ainsi::

    >>> for key,value in columns.items(): print str(key) + " = " + str(value)
    ... 
    0 = <qgis.core.QgsField object at 0xd8df66c>
    1 = <qgis.core.QgsField object at 0xd8df6ac>
    2 = <qgis.core.QgsField object at 0xd8df62c>
    3 = <qgis.core.QgsField object at 0xd8df5ec>
    4 = <qgis.core.QgsField object at 0xd8df5ac>
    5 = <qgis.core.QgsField object at 0xd8df56c>
    6 = <qgis.core.QgsField object at 0xd8df52c>
    7 = <qgis.core.QgsField object at 0xd8df4ec>
    8 = <qgis.core.QgsField object at 0xd8df4ac>
    
    # SORTIE COUPÉE

\  **6.** \Maintenant récupérons des sorties intéressantes à partir de l'objet QgsField::
 
    >>> for key,value in columns.items(): print str(key) + " = " + str(value.name()) 
    ... 
    0 = ScaleRank
    1 = FeatureCla
    2 = SOVEREIGNT
    3 = SOVISO
    4 = SOV_A3
    5 = LEVEL
    6 = TYPE
    7 = NAME
    8 = SORTNAME
    9 = ADM0_A3
    10 = NAME_SM
    11 = NAME_LNG
    12 = TERR_
    13 = PARENTHETI
    14 = NAME_ALT
    15 = LOCAL_LNG

    # SORTIE COUPEE

\  **7.** \On peut ajouter un autre attribut QgsField à l'itération ci dessus::

    >>> for key,value in columns.items(): print str(key) + " = " + str(value.name()) + " | " + str(value.typeName()) + " | " + str(value.length())
    ... 
    0 = ScaleRank | Integer | 4
    1 = FeatureCla | String | 30
    2 = SOVEREIGNT | String | 32
    3 = SOVISO | String | 3
    4 = SOV_A3 | String | 3
    5 = LEVEL | Real | 4
    6 = TYPE | String | 13
    7 = NAME | String | 36
    8 = SORTNAME | String | 36

Le point important est que l'objet QgsField nous donne les noms et types de données des colonnes attributaires mais \ **PAS** \les valeurs individuelles des attributs des features. Celles ci devront être accédées à travers des features elles-mêmes.

\  **8.** \Nous avons déjà vu comment récupérer des features à l'aide de deux fonctions:

    \1) La fonction \ ``select()`` \ de QgsVectorDataProvider

    \2) La fonction \ ``featureAtId()`` \ de QgsVectorDataProvider

L'exemple ci-dessous montre comment récupérer des features et ajoute également les étapes nécessaires pour ne sélectionner que certains attributs en utilisant la fonction\  ``dataProvider.select()`` \. Cette fois cependant nous allons passer\ **TOUS** \ les arguments de la fonction ``select()``. Des commentaires sur chaque étape sont donnés dans le code suivant::

    # Récupérer la référence de la couche
    cLayer = qgis.utils.iface.activeLayer()
    provider = cLayer.dataProvider()
    # Créer une liste vide qui va contenir les indices des colonnes que nous souhaitons récupérer
    selectList = []
    # Pour chaque colonne que nous voulons récupérer, on obtient son index et on l'ajoute à la liste selectList
    for column in ['LEVEL', 'TYPE', 'NAME', 'SORTNAME']:
        selectList.append(provider.fieldNameIndex(column))

    # On crée un rectangle de bounding box que nous utiliserons comme filtre pour ne récupérer que les features qui sont en intersection
    rect = QgsRectangle(QgsPoint(0,0),QgsPoint(20, 34))
    # L'instruction select avec tous les arguments pour appeler notre couche vecteur avec tous les attributs qui nous intéressent et la géométrie, cela pour les features qui sont en intersection avec notre QgsRectangle
    provider.select(selectList, rect, True, False)
    feat = QgsFeature()
    # Boucle sur toutes les features de notre instruction select pour obtenir les attributs
    while provider.nextFeature(feat):
        # On récupère notre dictionnaire de clés et indices qui pointent vers des valeurs attributaires de cette feature
        map = feat.attributeMap()

    # Pour chaque attribut de la feature on affiche sa valeur
    for key, value in map.items():
        print value.toString()

\  **9.** \Cet exemple est un peu plus compliqué a comprendre. L'objectif est de montrer comment créer des dictionnaires. Nous allons créer une structure de données de table -- un dictionnaire Python qui représente une table dans une base de données. La table est un dictionnaire où les clés sont les featureID pour chaque feature et les valeurs sont des dictionnaires imbriqués qui ont les noms de colonne comme clé et les valeur de la colonne comme valeu. En retravaillant l'exemple précédent cela donne::

    # Récupérer la référence de la couche
    cLayer = qgis.utils.iface.activeLayer()
    provider = cLayer.dataProvider()
    provider.select(selectList, rect, True, False)
    table = {}
    while provider.nextFeature(feat):
        attributeMap = feat.attributeMap()
        table[feat.id()] = { 'LEVEL' : str(attributeMap[provider.fieldNameIndex('LEVEL')].toString()) \
                              , 'NAME' : str(attributeMap[provider.fieldNameIndex('NAME')].toString()) \
                              , 'SORTNAME' : str(attributeMap[provider.fieldNameIndex('SORTNAME')].toString()) \
                              , 'TYPE' : str(attributeMap[provider.fieldNameIndex('TYPE')].toString()) \ 
                            }

    for id, record in table.items():
        print str(id) + " --> " + str(record)


Raster
*********

Dans cet exemple nous allons interroger les valeurs des pixels d'un raster avec un QgsPoint en utilisant la fonction\  `QgsRasterLayer.identify()  <http://doc.qgis.org/head/classQgsRasterLayer.html#4bcb29bba8fc0fca1e0bed41b6a0ee9b>`_ \. Bien que l'API C++ montre que la fonction identify() prenne deux arguments, le binding Python ne nécessite en réalité qu'un QgsPoint() passé en argument.


\  **1.** \Chargez le relief suivant dans QGIS::

    /home/formation/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif

\  **2.** \La première chose dont on a besoin est de créer des points en WGS84 (EPSG:4326) que nous pouvons utiliser pour interroger cette couche raster. On a choisi ici Dar-Es-Salaam en Tanzanie et Assam en Inde comme exemples::

    >>> DarEsSalaam = QgsPoint(39.268, -6.80)
    >>> DarEsSalaam
    (39.268,-6.8)
    >>> Assam = QgsPoint(91.76,26.144)
    >>> Assam
    (91.76,26.144)

\  **3.** \On s'assure d'avoir une référence à la couche raster\  ``SR_50M.tif`` \::

    >>> rLayer = qgis.utils.iface.mapCanvas().layer(1)
    >>> rLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

\  **4.** \La fonction \  `QgsRasterLayer.identify() <http://doc.qgis.org/head/classQgsRasterLayer.html#4bcb29bba8fc0fca1e0bed41b6a0ee9b>`_ \retourne une valeur booléenne True ou False pour indiquer si elle a fonctionné ou pas. La donnée est renvoyée dans un dictionnaire avec le numéro de bande comme clé et la valeur pour cette bande comme valeur::

    >>> rLayer.identify(Assam)
    (True, {PyQt4.QtCore.QString(u'Band 1'): PyQt4.QtCore.QString(u'218')})
    >>> rLayer.identify(DarEsSalaam)
    (True, {PyQt4.QtCore.QString(u'Band 1'): PyQt4.QtCore.QString(u'202')})

\  **5.** \Pour extraire la donnée renvoyée par identify et la rendre un peu plus présentable on peut faire le traitement suivant::

    >>> success, data = rLayer.identify(DarEsSalaam)
    >>> for band, value in data.items(): print str(band) + " = " + str(value)
    ... 
    Band 1 = 202
    >>> 

