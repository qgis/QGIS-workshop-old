
====================
Débugger les plugins
====================

La console Python dans QGIS
---------------------------
Le débogage par la console Python est toujours une méthode possible.

Utiliser le hook de debug de PyQT
---------------------------------
Quand on essaie de débugger des plugins Python, une des meilleures méthodes est d'utiliser\ `pdb <http://docs.python.org/library/pdb.html>`_ \. Pour utiliser\ `pdb <http://docs.python.org/library/pdb.html>`_ \, vous aurez besoin d'ajouter les instructions suivantes::

    from PyQt4.QtCore import *
    import pdb

Choisissez ensuite un endroit dans votre code où vous voulez passer dans le débugger (vous pouvez toujours ajouter d'autres points d'arrêt dans pdb). Ajoutez ce code là où vous voulez commencer le débug::    

    pyqtRemoveInputHook()
    pdb.set_trace()

Lancez alors QGIS à partir de la ligne de commande et quand l'appel à set_trace est exécuté, vous vous retrouverez avec un prompt PDB sur la ligne de commande. À partir de là vous aurez un environnement de debug ressemblant à "GDB" où vous pourrez voir et assigner des variables, ainsi que naviguer dans le code::    

    (Pdb) print self
    <DockableMirrorMap.mirrorMap.MirrorMap object at 0xabfa5ec>
    (Pdb) print self.iface.mainWindow().windowTitle()
    Quantum GIS 1.7.0-Wroclaw
    (Pdb) aLayer = self.iface.activeLayer()
    (Pdb) aLayer
    <qgis.core.QgsVectorLayer object at 0xabfa6ac>
    (Pdb) aLayer.name()
    PyQt4.QtCore.QString(u'50m_admin_0_boundary_breakaway_disputed_areas')
    (Pdb) 
    

Astuces et commandes Pdb
---------------------------

Pdb (comme les autres outils de debug) a des options en ligne de commande qui améliorent le confort de debug. Nous allons voir certaines de ces commandes ci-dessous. Pour une liste complète voir la\  `documentation officielle <http://docs.python.org/library/pdb.html>`_ \.


\  **1.** \Une fois que\  ``set_trace()`` \a été exécuté et nous envoie dans une session Pdb, on peut voir où on en est dans l'exécution du code avec la commande\  ``list`` \.::

    (Pdb) list
     61     
     62         def handleXY(self, point):
     63             self.dlg.clearTextBrowser()
     64             pyqtRemoveInputHook()
     65             pdb.set_trace()
     66  ->         self.cLayer = self.canvas.currentLayer()
     67             if self.cLayer:
     68                 if self.cLayer.type() == 1:
     69                     success, data = self.cLayer.identify(point)
     70                     final = "" 
     71                     for key,value in data.items():


Notez la flèche\  ``->`` \. Cette commande sans argument renvoie 11 lignes, avec la ligne en cours d'exécution au milieu.


\  **2.** \La commande\  ``list`` \est assez dynamique, ce qui signifie qu'on peut lister une partie du code en donnant les numéros de ligne. Quelques variantes de la commande::

    (Pdb) list 60
     55             #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )
     56     
     57         def unload(self):
     58             # Remove the plugin menu item and icon
     59             self.iface.removePluginMenu("&Example #2 Solution for FOSS4G 2011 Workshop",self.action)
     60             self.iface.removeToolBarIcon(self.action)
     61     
     62         def handleXY(self, point):
     63             self.dlg.clearTextBrowser()
     64             pyqtRemoveInputHook()
     65             pdb.set_trace()

    (Pdb) list 60, 75
     60             self.iface.removeToolBarIcon(self.action)
     61     
     62         def handleXY(self, point):
     63             self.dlg.clearTextBrowser()
     64             pyqtRemoveInputHook()
     65             pdb.set_trace()
     66  ->         self.cLayer = self.canvas.currentLayer()
     67             if self.cLayer:
     68                 if self.cLayer.type() == 1:
     69                     success, data = self.cLayer.identify(point)
     70                     final = "" 
     71                     for key,value in data.items():
     72                         final += str(key) + " > " + str(value) + "\n"
     73                     self.dlg.setTextBrowser(final) 
     74     
     75         # run method that performs all the real work


Un seul argument numérique affiche la ligne que demandons avec 5 lignes avant, et après. Deux argumensts affichent le code entre ces deux numéros de lignes.                

\  **3.** \On peut aussi ajouter des points d'arrêt quand on est dans pdb. On peut utiliser la commande\  ``break`` \ou juste le raccourci\  ``b`` \avec un argument numérique pour désigner sur quelle ligne on veut placer un point d'arrêt::

    (Pdb) b 64
    Breakpoint 1 at /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py:64

\  **4.** \Si on veut voir combien de points d'arrêt sont définis on peut juste utiliser la commande\  ``break`` \sans argument. Notez que la valeur 'Num' est l'identifiant d'un point d'arrêt. On peut utiliser cette valeur si on veut passer ce point d'arrêt comme argument à une autre commande::

    (Pdb) b
    Num Type         Disp Enb   Where
    1   breakpoint   keep yes   at /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py:64

\  **5.** \Maintenant que j'ai défini un nouveau point d'arrêt, je veux continuer à exécuter mon code jusqu'à y parvenir. Je peux continuer avec la raccourci\  ``c`` \ou la commande\  ``continue`` \.::

    (Pdb) c
    > /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py(64)handleXY()
    -> self.dlg.clearTextBrowser()
    (Pdb) list
     59             self.iface.removePluginMenu("&a tool that displays raster values on-the-fly",self.action)
     60             self.iface.removeToolBarIcon(self.action)
     61     
     62         def handleXY(self, point):
     63             #QMessageBox.information( self.iface.mainWindow(), "Info", str(point.x()) + "," + str(point.y()) )
     64 B->         self.dlg.clearTextBrowser()
     65             self.cLayer = self.canvas.currentLayer()
     66             if self.cLayer:
     67                 if self.cLayer.type() == 1:
     68                     success, data = self.cLayer.identify(point)
     69                     final = "" 

Remarquez que lorsque je liste le code la où l'exécution s'est arrêtée, un\  ``B->`` \montre qu'il s'agit d'un point d'arrêt.

\  **6.** \On peut avancer dans le code ligne par ligne avec deux commandes :\  ``step`` \et\  ``next`` \. \  ``step`` \descend dans toutes les fonctions (mêmes les fonctions Python standard) et\  ``next`` \les exécute et avance à la ligne suivante. Soyez surs de comprendre le résultat de la commande. Si l'exécution était arrêtée sur le point d'arrêt ci-dessus,\  ``next`` \emmène à la ligne 65::

    (Pdb) n
    > /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py(65)handleXY()
    -> self.cLayer = self.canvas.currentLayer()
    (Pdb) list
     60             self.iface.removeToolBarIcon(self.action)
     61     
     62         def handleXY(self, point):
     63             #QMessageBox.information( self.iface.mainWindow(), "Info", str(point.x()) + "," + str(point.y()) )
     64 B           self.dlg.clearTextBrowser()
     65  ->         self.cLayer = self.canvas.currentLayer()
     66             if self.cLayer:
     67                 if self.cLayer.type() == 1:
     68                     success, data = self.cLayer.identify(point)
     69                     final = "" 
     70                     for key,value in data.items():


Cela fonctionne en effet.                            

\  **7.** \Enfin, on peut retirer un point d'arrêt avec la commande\  ``clear`` \ou le raccourci\  ``cl`` \. On donne un numéro de point d'arrêt comme argument::

    (Pdb) cl 1
    Deleted breakpoint 1



