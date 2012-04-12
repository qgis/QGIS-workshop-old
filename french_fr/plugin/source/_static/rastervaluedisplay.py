"""
/***************************************************************************
 rastervaluedisplay
                                 A QGIS plugin
 a tool that displays raster values on-the-fly
                              -------------------
        begin                : 2011-08-25
        copyright            : (C) 2011 by CUGOS
        email                : none@cugos.org
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
# Initialisation des ressources Qt depuis le fichier resources.py
import resources
# Import du code pour les boites de dialogue
from rastervaluedisplaydialog import rastervaluedisplayDialog

class rastervaluedisplay:

    def __init__(self, iface):
        # On garde la reference a l'interface QGIS
        self.iface = iface
        # Reference au canvas de la carte
        self.canvas = self.iface.mapCanvas()
        # creation de notre fenetre GUI
        self.dlg = rastervaluedisplayDialog()

    def initGui(self):
        # Creation de l'action qui va commencer la configuration du plugin
        self.action = QAction(QIcon(":/plugins/rastervaluedisplay/icon.png"), \
            "a tool that displays raster values on-the-fly", self.iface.mainWindow())
        # connexion de l'action a la methode run
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Ajout d'un bouton dans la barre de menu et une entree de menu
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&a tool that displays raster values on-the-fly", self.action)
        
        # Ajout d'une connexion au signal xycoord du map canvas
        result = QObject.connect(self.canvas, SIGNAL("xyCoordinates (const QgsPoint &)"), self.handleXY)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    def unload(self):
        # On enleve le plugin du menu et son icone
        self.iface.removePluginMenu("&a tool that displays raster values on-the-fly",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleXY(self, point):
        #QMessageBox.information( self.iface.mainWindow(), "Info", str(point.x()) + "," + str(point.y()) )
        self.dlg.clearTextBrowser()
        self.cLayer = self.canvas.currentLayer()
        if self.cLayer:
            if self.cLayer.type() == 1:
                success, data = self.cLayer.identify(point)
                final = "" 
                for key,value in data.items():
                    final += str(key) + " > " + str(value) + "\n"
                self.dlg.setTextBrowser(final) 

    # la methode run qui effectue le travail 
    def run(self):

        # Montrer la fenetre de dialogue
        self.dlg.show()
        result = self.dlg.exec_()
        # Voir si OK a ete appuye
        if result == 1:
            # faire quelque chose d'interessant (supprimer la ligne avec pass
            # et y mettre votre propre code)
            pass


