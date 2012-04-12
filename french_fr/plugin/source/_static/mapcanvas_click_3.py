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
        result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    def unload(self):
        # On enleve le plugin du menu et son icone
        self.iface.removePluginMenu("&some text that appears in the menu",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleMouseDown(self, point, button):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
        #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

    # la methode run qui effectue le travail 
    def run(self):
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

