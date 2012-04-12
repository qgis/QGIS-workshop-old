# Import de PyQt et des bibliothèques QGIS 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialisation des ressources Qt depuis le fichier resources.py
import resources
# Import du code pour les boites de dialogue
from vector_selectbypointdialog import vector_selectbypointDialog

class vector_selectbypoint:

    def __init__(self, iface):
        # On garde la reference a l'interface QGIS
        self.iface = iface

    def initGui(self):
        # Creation de l'action qui va commencer la configuration du plugin
        self.action = QAction(QIcon(":/plugins/vector_selectbypoint/icon.png"), \
            "some text that appears in the menu", self.iface.mainWindow())
        # connexion de l'action a la methode run
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Ajout d'un bouton dans la barre de menu et une entree de menu
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&some text that appears in the menu", self.action)

    def unload(self):
        # On enleve le plugin du menu et son icone
        self.iface.removePluginMenu("&some text that appears in the menu",self.action)
        self.iface.removeToolBarIcon(self.action)

    # la methode run qui effectue le travail 
    def run(self):
        # creer et montrer la fenetre de dialogue
        dlg = vector_selectbypointDialog()
        dlg.show()
        result = dlg.exec_()
        # Voir si OK a ete appuye
        if result == 1:
            # faire quelque chose d'interessant (supprimer la ligne avec pass
            # et y mettre votre propre code)
            pass

