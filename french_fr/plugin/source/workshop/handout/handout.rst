
=========================================================
À retenir
=========================================================

Accéder aux couches par QgisInterface and QgsMapCanvas 
----------------------------------------------------------

Utiliser QgisInteface.activeLayer()
***************************************

Retourne une référence à la couche sélectionnée dans la liste des couches::

    >>> aLayer = qgis.utils.iface.activeLayer()
    >>> aLayer
    <qgis.core.QgsRasterLayer object at 0x99ea6ec>
    >>> aLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Utiliser QgsMapCanvas.currentLayer()
***************************************

Un autre moyen courant d'accéder à la couche sélectionnée dans la liste des couches est de la récupérer en utilisant le\  `QgsMapCanvas <http://doc.qgis.org/head/classQgsMapCanvas.html>`_ \ainsi::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> cLayer = canvas.currentLayer()
    >>> cLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Récupérer toutes les couches visibles QgsMapCanvas.layers()
***********************************************************

Avec la classe map canvas on peut récupérer plus que le layer actif -- on peut obtenir toutes les couches visibles (ceux qui sont activés dans la liste de couches)::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> allLayers = canvas.layers()
    >>> for i in allLayers: print i.name()
    ... 
    50m_populated_places_simple

Récupérer des couches par leur indice avec QgsMapCanvas.layer()
***************************************************************

Les couches sont empilées de haut en bas et accédées par un indice à base 0. Cela signifie que la première couche (en haut) commence à l'indice 0. On passe un entier désignant l'indice de la couche que l'on veut::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> canvas.layer(0)
    <qgis.core.QgsVectorLayer object at 0x99eaeec>
    >>> canvas.layer(0).name()
    PyQt4.QtCore.QString(u'50m_populated_places_simple') 

----------------------------------

Accéder aux Features (Attributs et Geometrie)
----------------------------------------------------------

Utiliser QgsVectorDataProvider.select()
****************************************

Boucler sur toutes les features::

    # using the 50m_admin_0_countries.shp from natural earth download for this example
    cLayer = qgis.utils.iface.mapCanvas().currentLayer()
    provider = cLayer.dataProvider()
    columnList = []
    for i in ['NAME']:
        columnList.append(provider.fieldNameIndex(i))

    rect = QgsRectangle(QgsPoint(0,0),QgsPoint(20, 34))
    provider.select(selectList, rect, True, False)
    feat = QgsFeature()
    while provider.nextFeature(feat):
        att = feat.attributeMap()
        for key, value in att.items(): print str(value.toString())

Utiliser QgsVectorDataProvider.featureAtId()
********************************************

Si on a l'identifiant de la feature que l'on veut, on a pas besoin de boucler::

    # using the 50m_admin_0_countries.shp from natural earth download for this example
    cLayer = qgis.utils.iface.mapCanvas().currentLayer()
    provider = cLayer.dataProvider()
    selectList = [ 24, 32, 45, 56 ]
    if selectList:
        for id in selectList:
            nIndx = provider.fieldNameIndex('NAME')
            sFeat = QgsFeature()
            if provider.featureAtId(id, sFeat, True, [nIndx]):
                if nIndx != -1:
                    attMap = sFeat.attributeMap()
                    print str( attMap[nIndx].toString() )

------------------------------------

Exemples de SIGNAL et SLOT 
----------------------------

Émettre un Signal
*****************

On utilise l'objet \  ``QgsMapCanvas`` \en exemple. Voici comment émettre un signal::

    self.iface.mapCanvas().emit(SIGNAL("xyCoordinates(const QgsPoint &)"), QgsPoint(-122,45))

Connecter un Slot à un Signal
*****************************

On connecte ici la fonction slot\  ``listen_xyCoordinates`` \au signal\  ``"xyCoordinates(const QgsPoint &)"`` \ ::

    # the connection
    QObject.connect(self.iface.mapCanvas(), SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xyCoordinates)

    # the custome slot function
    def listen_xyCoordinates(self,point):
        self.dlg.outputTextEdit.append("xyCoordinates - %d,%d" % (point.x() if point else "",point.y() if point else ""))

------------------------------------

Debugger avec Pdb
------------------------------

Le hook de debug PyQt
*********************

Assurez vous d'importer pdb avant de l'utiliser::
    
    import pdb

Il faudra ajouter l'instruction\  ``pdb.set_trace()`` \là où vous voulez commencer à mettre un point d'arrêt dans votre code::

    pyqtRemoveInputHook()
    pdb.set_trace()

Démarrer QGIS à partir de la ligne de commande et vous aurez une invite de PDB où vous pourrez lancer des commandes pdb et des instructions Python classiques. Voici une brève liste de commandes pdb. Voir la\  `documentation officielle de pdb  <http://docs.python.org/library/pdb.html>`_ \pour plus d'exemples:

    ``list # Lister le source avec la ligne en exécution au milieu``

    ``list <line number> # lister le source avec la ligne <line number> au milieu``

    ``list <line number from> , <line number to> # lister le source entre les arguments <line number>``
    
    ``break # break sans argument renvoie tous les points d'arrêt (et leurs identifiants) définis dans le code de debug``

    ``break <line number> # crée un nouveau point d'arrêt dans le code à la ligne <line number>``

    ``next # avance dans l'exécution du code ligne a ligne. next passe à la ligne suivante sans rentrer dans les fonctions``
    
    ``step # avance dans l'exécution du code ligne a ligne. next passe à la ligne suivante en entrant dans les fonctions``
    
    ``cl <breakpoint ID> # supprime un point d'arrêt identifié par son <breakpoint ID>``

-----------------------------

Créer un dépôt de plugin
-------------------------------

Si vous voulez récupérer vos plugins par QGIS vous devez créer un fichier XML accessible par le web qui indique à QGIS où télécharger le plugin::

    <?xml version = '1.0' encoding = 'UTF-8'?>
    <?xml-stylesheet type='text/xsl' href='/plugins.xsl' ?>
    <plugins>
      <pyqgis_plugin name='Plugin Installer' version='1.1'>
        <description>The recent Python Plugin Installer</description>
        <version>1.1</version>
        <qgis_minimum_version>1.0</qgis_minimum_version>
        <homepage>http://www.bwj.aster.net.pl/qgis/</homepage>
        <file_name>plugin_installer.zip</file_name>
        <author_name>Borys Jurgiel</author_name>
        <download_url>http://spatialserver.net/pyqgis_1.0/plugins/plugin_installer.zip</download_url>
        <uploaded_by>borysiasty</uploaded_by>
        <create_date>2008-12-18</create_date>
        <update_date>2010-10-31</update_date>
      </pyqgis_plugin>
    </plugins>


