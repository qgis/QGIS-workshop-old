# Import de PyQt et des bibliothèques QGIS 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialisation des ressources Qt depuis le fichier resources.py
import resources
# Import du code pour les boites de dialogue
from vector_selectbypointdialog import vector_selectbypointDialog

class vector_selectbypoint:

    def __init__(self, iface):
        # On garde la reference a l'interface QGIS
        self.iface = iface
        # Reference au canvas de la carte
        self.canvas = self.iface.mapCanvas()
        # Notre click tool va emettre un QgsPoint a chaque clic
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # creation de notre fenetre GUI
        self.dlg = vector_selectbypointDialog()
        # creation d'une liste pour contenir nos ids des features selectionnees
        self.selectList = []
        # reference a la couche courante (assigne dans handleLayerChange)
        self.cLayer = None
        # reference au dataProvider de la couche courante (assigne dans handleLayerChange)
        self.provider = None

    def initGui(self):
        # Creation de l'action qui va commencer la configuration du plugin
        self.action = QAction(QIcon(":/plugins/vector_selectbypoint/icon.png"), \
            "some text that appears in the menu", self.iface.mainWindow())
        # connexion de l'action a la methode run
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Ajout d'un bouton dans la barre de menu et une entree de menu
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&some text that appears in the menu", self.action)

        # connexion de notre fonction specifique a un signal clickTool quand le canvas a ete clique
        #result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

        # connexion de notre fonction select au signal canvasClicked
        #result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )
        
        # connexion de la fonction de gestion checkbox au signal de changement d etat 
        QObject.connect(self.dlg.ui.chkActivate,SIGNAL("stateChanged(int)"),self.changeActive)

        # connexion de la fonction de gestion de changement le couche au signal de changement dans la liste de couches
        result = QObject.connect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer *)"), self.handleLayerChange)

    def handleLayerChange(self, layer):
            self.cLayer = self.canvas.currentLayer()
            if self.cLayer:
                self.provider = self.cLayer.dataProvider()

    def changeActive(self,state):
         if (state==Qt.Checked):
                 # connexion au signal de clic
                 QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
                 # connexion de la fonction de select au signal canvasClicked
                 QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
         else:
                 # deconnexion du signal de clic 
                 QObject.disconnect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
                 # deconnexion de la fonction de select au signal canvasClicked
                 QObject.disconnect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)

    def unload(self):
        # On enleve le plugin du menu et son icone
        self.iface.removePluginMenu("&some text that appears in the menu",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleMouseDown(self, point, button):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
        #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

    def selectFeature(self, point, button): 
        # reinitialisation de la liste de selection a chaque nouvelle selection
        self.selectList = []
        #QMessageBox.information( self.iface.mainWindow(),"Info", "in selectFeature function" )
        # parametrage de la fonction select du provider pour filtrer les restultats sur un rectangle
        pntGeom = QgsGeometry.fromPoint(point)  
        # Buffer dependant de l echelle de 2 pixels en unite de la carte
        pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0) 
        rect = pntBuff.boundingBox()
        if self.cLayer:
            feat = QgsFeature()
            # creation de l appel select
            # les arguments signifient qu'aucun attribut n'est renvoyé, et on fait un filtre sur notre rectangle pour limiter le nombre de feature
            self.provider.select([],rect) 
            while self.provider.nextFeature(feat):
                # si la geometrie de la feature obtenue par la selection a une intersection avec le point
                # on la met dans une liste
                if feat.geometry().intersects(pntGeom):
                    self.selectList.append(feat.id())

            if self.selectList:
                # faire la selection reelle 
                self.cLayer.setSelectedFeatures(self.selectList)
                # mise a jour du Text Browser
                self.updateTextBrowser()
        else:
                QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )

    def updateTextBrowser(self):
        # si on a au moins une feature dans la liste 
        if self.selectList:
            # trouve l'index de la colonne 'NAME' et agit en fonction de s'il y en a une ou pas
            nIndx = self.provider.fieldNameIndex('NAME')
            # obtient la feature selectionnee du provider, mais il faut passer
            # une feature vide et l'indice de la colonne voulue
            sFeat = QgsFeature()
            if self.provider.featureAtId(self.selectList[0], sFeat, True, [nIndx]):
                # seulement si on a une colonne 'NAME'
                if nIndx != -1:
                    # obtient l'attributeMap de la feature
                    attMap = sFeat.attributeMap()
                    # nettoyer l'ancienne valeur du TextBrowser
                    self.dlg.clearTextBrowser()
                    # met a jour le TextBrowser avec attributeMap[nameColumnIndex]
                    # Lorsqu'on reçoit au depart la valeur de 'NAME' c'est un QSTring et il faut le transformer en Python string
                    self.dlg.setTextBrowser( str( attMap[nIndx].toString() ))


    # la methode run qui effectue le travail 
    def run(self):
        # assigne la couche courante tout de suite si elle existe, sinon elle sera assignee a la selection de l'utilisateur
        self.cLayer = self.iface.mapCanvas().currentLayer()
        if self.cLayer: self.provider = self.cLayer.dataProvider()

        # activer le clickTool
        self.canvas.setMapTool(self.clickTool)

        # Montrer la fenetre de dialogue
        self.dlg.show()
        result = self.dlg.exec_()
        # Voir si OK a ete appuye
        if result == 1:
            # faire quelque chose d'interessant (supprimer la ligne avec pass
            # et y mettre votre propre code)
            pass

