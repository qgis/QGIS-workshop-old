"""
/***************************************************************************
 foss4g2011_example1
                                 A QGIS plugin
 Example #1 for FOSS4G 2011 Workshop
                              -------------------
        begin                : 2011-08-31
        copyright            : (C) 2011 by FOSS4G
        email                : info@cugos.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import de PyQt et des bibliothèques QGIS 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import pdb
# Initialisation des ressources Qt depuis le fichier resources.py
import resources
# Import du code pour les boites de dialogue
from foss4g2011_example1dialog import foss4g2011_example1Dialog

class foss4g2011_example1:

    def __init__(self, iface):
        # On garde la reference a l'interface QGIS
        self.iface = iface
        # Reference au canvas de la carte
        self.canvas = self.iface.mapCanvas() 
        # Notre click tool va emettre un QgsPoint a chaque clic
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # creation de notre fenetre GUI
        self.dlg = foss4g2011_example1Dialog()
        # creation d'une liste pour contenir nos ids des features selectionnees
        self.selectList = []
        # reference a la couche courante (assigne dans handleLayerChange)
        self.cLayer = None
        # reference au dataProvider de la couche courante (assigne dans handleLayerChange)
        self.provider = None 

    def initGui(self):
        # Creation de l'action qui va commencer la configuration du plugin
        self.action = QAction(QIcon(":/plugins/foss4g2011_example1/icon.png"), \
            "Example #1 for FOSS4G 2011 Workshop", self.iface.mainWindow())
        # connexion de l'action a la methode run
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Ajout d'un bouton dans la barre de menu et une entree de menu
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Example #1 for FOSS4G 2011 Workshop", self.action)

        # Connexion au signal currentLayerChanged de QgsInterface
        result = QObject.connect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer *)"), self.handleLayerChange)

        # connexion de la fonction selectFature a l evenement clic du canvas de carte        
        QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)


    def unload(self):
        # On enleve le plugin du menu et son icone
        self.iface.removePluginMenu("Example #1 for FOSS4G 2011 Workshop",self.action)
        self.iface.removeToolBarIcon(self.action)


    def handleMouseDown(self, point, button):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )

    def handleLayerChange(self, layer):
        self.cLayer = self.canvas.currentLayer()        
        if self.cLayer:
            self.provider = self.cLayer.dataProvider()

    def updateTextBrowser(self):
        # verification pour etre sur qu'on a une feature selectionnee dans notre selectList -- il peut y en avoir plus d une 
        if self.selectList:

            # ############ EXAMPLE 1 EDITER ICI ####################  
            ''' ecrivez du code qui va afficher tous les attributs des features selectionnees pour une seule feature dans le Text Browser'''
            ''' plutot que d utiliser la fonction dataProvider.select(), recuperer la QgsFeature en utilisant dataProvider.featureAtId() '''
            # obtenir tous les indices des champs pour la feature
            fields = self.provider.fields()
            # obtenir la feature en passand une feature vide
            feat = QgsFeature()
            # on prend la premiere feature car il peut y en avoir plus d une
            if self.provider.featureAtId(self.selectList[0], feat, True, fields.keys()):
                attMap = feat.attributeMap()
                output = "FEATURE ID: %i\n" % feat.id()
                for index,qgsfield in fields.items():
                    #pyqtRemoveInputHook()
                    #pdb.set_trace()
                    output += "\t" + str(qgsfield.name()) + " : " + str( (attMap[index]).toString() ) + "\n"
        
                self.dlg.setTextBrowser(output)
            

    def selectFeature(self, point, button):
        # Reinitialise la liste de selection a chaque nouvelle selection
        self.selectList = []
        pntGeom = QgsGeometry.fromPoint(point)  
        pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0) 
        rect = pntBuff.boundingBox()
        if self.cLayer:
            feat = QgsFeature()
            # creation de l'instruction select
            selfprovider.select([],rect) # les arguments signifient qu'aucun attribut n'est renvoye, et on fait un filtre sur notre rectangle pour limiter le nombre de feature
            while self.provider.nextFeature(feat):
                # si la geometrie de la feature obtenue par la selection a une intersection avec le point
                # on la met dans une liste
                if feat.geometry().intersects(pntBuff):
                    self.selectList.append(feat.id())

            if self.selectList:
                # faire la selection reelle 
                self.cLayer.setSelectedFeatures([self.selectList[0]])
                # mettre a jour le TextBrowser
                self.updateTextBrowser()
        else:   
                QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )


    # la methode run qui effectue le travail 
    def run(self):
        # assigner la couche courante tout de suite si elle existe, sinon elle le sera
        # lors de la selection par l'utilisateur
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

