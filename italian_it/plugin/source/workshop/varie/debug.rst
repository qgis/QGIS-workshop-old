
===================
Debug dei plugin
===================

La console Python
-----------------

E' possibile fare *debug* dei plugin tramite la console Python di QGIS.

Utilizzare il debugger Python
-----------------------------

Il modo migliore per fare *debug* dei plugin è usare il *debugger* Python\  `pdb <http://docs.python.org/library/pdb.html>`_\. Se intendete usare "pdb" dovete aggiungere le seguenti dichiarazioni al vostro codice::

    from PyQt4.QtCore import *
    import pdb

Individuate il punto del codice dove intendete iniziare il debug ed aggiungete il seguente codice::

    pyqtRemoveInputHook()
    pdb.set_trace()

Lanciate QGIS da riga di comando: quando la chiamata *set_trace* viene raggiunta, avrete a disposizione un prompt "pdb" a linea di comando. A questo punto vi troverete in un ambiente simile a\  `GDB <http://www.gnu.org/software/gdb/>`_\, dove potete vedere e settare le variabili ed analizzare il codice::

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
    

Comandi pdb e trucchi
---------------------

"pdb", come altri strumenti simili, ha opzioni da linea di comando che migliorano l'attività di *debug*. Analizziamo di seguito alcuni dei comandi più utilizzati; per una lista completa riferitevi alla\  `documentazione ufficiale <http://docs.python.org/library/pdb.html>`_\.


\  **1.** \Per vedere, a sessione di "pdb" avviata, in che punto del vostro codice vi trovate potete usare il comando ``list``::

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


Il comando, dato senza argomenti, restituisce undici righe di codice: la freccia\  ``->`` \indica la riga di codice in esecuzione.


\  **2.** \Con il comando\  ``list`` \possiamo elencare qualsiasi porzione di codice usando due valori numerici (ad indicare righe di codice) come argomenti::

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


Un argomento singolo visualizza la riga di nostro interesse (numero dell'argomento stesso), con cinque righe prima e dopo. I due argomenti visualizzano l'intervallo di righe da essi individuato.


\  **3.** \Possiamo, inoltre, impostare dei punti di interruzione con il comando\  ``break``\, o solo\  ``b``\, seguito dal numero di riga in cui vogliamo avvenga l'interruzione::

    (Pdb) b 64
    Breakpoint 1 at /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py:64

\  **4.** \Per conoscere il numero di punti di interruzione esistenti, lanciamo il comando\  ``break`` \senza argomenti. Notate il valore 'Num' nella chiave di identificazione del punto di interruzione; possiamo usare questo valore per passare il punto di interruzione ad un altro comando::

    (Pdb) b
    Num Type         Disp Enb   Where
    1   breakpoint   keep yes   at /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py:64

\  **5.** \Una volta impostato un punto di interruzione, lanciate il comando\  ``c`` \o\  ``continue`` \per continuare l'esecuzione del codice (fino al raggiungimento del punto di interruzione stesso)::

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

\  ``B->`` \rappresenta un punto di interruzione.


\  **6.** \Possiamo analizzare il codice linea per linea con i comandi\  ``step`` \e\  ``next`` \. Notate che\  ``step`` \analizza ogni funzione nel dettaglio, mentre\  ``next`` \le esegue e passa alla riga successiva. Rispetto al codice precedente,\  ``next`` \dovrebbe portare alla riga 65::

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


Ed infatti è così!


\  **7.** \Infine, possiamo rimuovere i punti di interruzione con il comando\  ``clear`` \o\  ``cl`` \e il valore numerico del punto che intendiamo eliminare::

    (Pdb) cl 1
    Deleted breakpoint 1



