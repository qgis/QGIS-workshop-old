=======================================
Tutorial -- Costruire un plugin
=======================================

Costruiamo il nostro primo plugin con 'Plugin Builder'
------------------------------------------------------

E' ora tempo di mettere le mani sul\  **Plugin Builder** \.

\  **1.** \Cliccate sull'icona\  ``Plugin Builder`` \per lanciare il plugin:

.. image:: ../_static/plugin_builder_click1.png
    :scale: 100%
    :align: center

\  **2.** \Si aprirà la finestra di dialogo del Plugin Builder: qui inseriremo tutte le informazioni necessarie al plugin per creare i file modello. Quindi, modificheremo i file modello per costruire in nostro plugin. Tutti i campi del dialogo sono richiesti: compilate i campi così come mostrato nella figura seguente. Cliccate, infine, sul pulsante\  ``Ok``\:

.. image:: ../_static/plugin_builder_main_dialog.png 
    :scale: 70%
    :align: center

\  **3.** \Nella finestra di dialogo successiva, create una cartella\  ``workspace`` \all'interno di\  ``/home/qgis/``\. Salvare il progetto di plugin in \  ``workspace``\:

.. image:: ../_static/plugin_builder_save_dir.png 
    :scale: 100%
    :align: center

\  **4.** \La finestra di dialogo successiva mostra i vai passi da eseguire per personalizzare il plugin. Li vediamo nel dettaglio di seguito.

.. image:: ../_static/plugin_builder_feedback.png 
    :scale: 100%
    :align: center

\  **5.** \Portatevi, ora, nella cartella\  ``/home/qgis/workspace/vector_selectbypoint`` \ed elencatene il contenuto::

    $ cd workspace/vector_selectbypoint/
    $ ls -lah
    total 36K
    drwxr-xr-x 2 qgis qgis 4.0K 2011-08-20 13:21 .
    drwxr-xr-x 3 qgis qgis 4.0K 2011-08-20 17:34 ..
    -rw-r--r-- 1 qgis qgis 1.1K 2011-08-20 13:21 icon.png
    -rw-r--r-- 1 qgis qgis 1.6K 2011-08-20 13:21 __init__.py
    -rw-r--r-- 1 qgis qgis 1.9K 2011-08-20 13:21 Makefile
    -rw-r--r-- 1 qgis qgis  116 2011-08-20 13:21 resources.qrc
    -rw-r--r-- 1 qgis qgis 1.5K 2011-08-20 13:21 ui_vector_selectbypoint.ui
    -rw-r--r-- 1 qgis qgis 1.5K 2011-08-20 13:21 vector_selectbypointdialog.py
    -rw-r--r-- 1 qgis qgis 2.6K 2011-08-20 13:21 vector_selectbypoint.py

Notate i due file\  ``.ui`` \e\  ``.qrc``\: compiliamoli e vediamo come si presenta il plugin in QGIS.

\  **6.** \Usiamo il file\  ``Makefile`` \per compilare entrambi i file. Lanciate il seguente comando e notate le due dichiarazioni che esso mostrerà a video::

    $ make
    pyuic4 -o ui_vector_selectbypoint.py ui_vector_selectbypoint.ui
    pyrcc4 -o resources.py  resources.qrc

Le due dichiarazioni sono i comandi che servono a compilare il file risorse e la GUI. Possiamo lanciare i due comandi singolarmente, oppure diamo il comando\  ``Makefile``\, che si occuperà di compilare i due file. Ogni volta che modificate il file\  ``resources.qrc`` \o il file\  ``ui_vector_selectbypoint.ui`` \dovete ricompilare.

\  **7.** \Ora rielencate il contenuto della vostra cartella e noterete la presenza di moduli Python aggiuntivi. Quelli importanti sono::
    
    $ ls -lah
    ... # MORE FILES WERE LISTED HERE
    -rw-r--r-- 1 qgis qgis 5.4K 2011-08-20 17:42 resources.py
    -rw-r--r-- 1 qgis qgis 1.4K 2011-08-20 17:42 ui_vector_selectbypoint.py
    ... # MORE FILES WERE LISTED HERE

\  **8.** \QGIS potrà, ora, leggere i file del vostro progetto e creare il pulsante del plugin nella propria interfaccia grafica, ma la cartella del plugin va preventivemente spostata nella cartella\  ``/home/qgis/.qgis/python/plugins``\. Piuttosto che copiare tutti i nostri file, creiamo un link simbolico dalla nostra cartella\  ``/home/qgis/workspace/vector_selectbypoing/`` \alla cartella\  ``home/qgis/.qgis/python/plugings``\. In questo modo, QGIS sarà in grado di leggere il nostro plugin::

     $ ln -s /home/qgis/workspace/vector_selectbypoint/ /home/qgis/.qgis/python/plugins/

\  **9.** \Se ci spostiamo nella cartella\  ``/home/qgis/.qgis/python/plugins`` \e ne elenchiamo il contenuto, noteremo un collegamento\  ``vector_selectbypoint`` \che punta alla nostra cartella workspace::

    $ cd /home/qgis/.qgis/python/plugins
    $ ls -lah
    total 16K
    drwxr-xr-x 4 qgis qgis 4.0K 2011-08-20 17:58 .
    drwxr-xr-x 4 qgis qgis 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x 2 qgis qgis 4.0K 2011-08-20 12:26 osmpoly_export
    drwxr-xr-x 3 qgis qgis 4.0K 2011-07-07 13:41 pluginbuilder
    lrwxrwxrwx 1 qgis qgis   42 2011-08-20 17:58 vector_selectbypoint -> /home/qgis/workspace/vector_selectbypoint/

\  **10.** \Caricate il plugin in QGIS da\  ``Plugins > Gestione plugin``\. Nella finestra del *Gestore QGIS Plugin* usate la stringa\  ``Select_`` \come filtro di ricerca: il nostro plugin dovrebbe essere elencato. Spuntate la casella di controllo a sinistra del nome del plugin, quindi cliccate sul pulsante\  ``OK``\:

.. image:: ../_static/plugin_builder_adding2QGIS.png
    :scale: 100%
    :align: center

\  **11.** \Potrete notare la presenza di una nuova icona a destra dell'icona del *Plugin Builder*. Cliccateci sopra:

.. image:: ../_static/click_vector_selectbypoint_tool.png
    :scale: 100%
    :align: center

\  **12.** \Dovrebbe aprirsi una finestra di dialogo con i pulsanti\  ``OK`` \e\  ``Cancel``\.  Come vedete, il *Plugin Builder* non ci fornisce nulla di direttamente utilizzabile, ma velocizza notevolmente il processo di sviluppo dei plugin. Sta a noi, ora, personalizzare il codice:

.. image:: ../_static/vector_selectbypoint_firstview.png
    :scale: 100%
    :align: center

----------------------------

Estendere i modelli del Plugin Builder
-----------------------------------------  

L'idea dietro il plugin ed il flusso di lavoro per la sua implementazione
*************************************************************************

Il tool che andremo ad implementare dovrà fare alcune cose di base:

     1. Restituire le coordinate X,Y di un *QgsPoint* ad ogni click del mouse. 
     2. Selezionare ogni elemento vettoriale intersecato dal punto
     3. Fornire la possibilità di abilitarlo/disabilitarlo tramite una casella di controllo.

.. note:: Il tool funzionerà esattamente come il tool esistente *Select Single Feature* di QGIS. Lo scopo è quello di illustrare i passi necessari alla sua implementazione. Alla fine del tutorial saranno presentati vari esercizi pratici.

Affrontiamo l'implementazione passo passo:

    1. Modifichiamo la GUI (file\  ``.ui``  \) nel "Qt 4 Designer"
    2. Implementiamo il click del mouse sull'area mappa e l'acquisizione delle coordinate del punto
    3. Implementiamo la selezione dell'elemento al click nell'area mappa
    4. Implementiamo la possibilità di abilitare/disabilitare il tool 
    5. Rivediamo il codice per adeguare l'aspetto del tool

---------------------------------------

\1) Design della GUI
--------------------

Vediamo come dovrebbe apparire la GUI. I requisiti sono assolutamente basici:

    1. Abbiamo necessità di mostrare delle coordinate all'utente (useremo il widget *TextBrowser* a tal fine)
    2. Ci serve un modo per attivare/disattivare il tool (useremo il widget *checkbox*)

Per modificare la GUI dobbiamo editare il file con estensione\  ``.ui``\. Useremo il Qt Designer per modificare tale file.


\  **1.** \Aprite\  **Qt 4 Designer** \dal menu\  ``Applications > Programming``\:

.. image:: ../_static/qt_design1.png
    :scale: 100%
    :align: center

\  **2.** \Nella finestra di dialogo che si apre, portatevi nella cartella\  ``/home/qgis/workspace/vector_selectbypoint/``\. Dovrebbe essere elencato il solo file con estensione\  ``.ui`` \: il file ha nome\  ``ui_vector_selectbypoint.ui``\. Selezionatelo e cliccate su\  ``Open``\:

.. image:: ../_static/qt_design2.png
    :scale: 100%
    :align: center

\  **3.** \Apparirà una form Qt semplice con un paio di pulsanti:

.. image:: ../_static/qt_design3.png
    :scale: 100%
    :align: center

\  **4.** \Dobbiamo inserire un *TextBrowser* e un *CheckBox*. Cliccate e trascinate sulla form il widget *TextBrowser*: lo trovate nella colonna sinistra sotto\  ``Display Widgets``\:

.. image:: ../_static/qt_design4.png
    :scale: 100%
    :align: center

\  **5.** \Dovremmo, ora, avere un *TextBrowser* nella nostra form:

.. image:: ../_static/qt_design5.png
    :scale: 100%
    :align: center

\  **6.** \Assicuratevi di avere *TextBrowser* selezionato sulla form (vertici evidenziati in blu), individuate\  ``Property Editor`` \nella colonna in basso a destra e combiate il nome dell'oggetto *TextBrowser* in\  ``txtFeedback``\. Le modifiche appaiono nel campo\  ``objectName``\. Il valore inserito dovrà essere utilizzato nel nostro codice per riferirci al *TextBrowser*.

.. image:: ../_static/qt_design05.png
    :scale: 100%
    :align: center

\  **7.** \Ora aggiungete alla form il widget *CheckBox*: lo trovate nella colonna a destra sotto\  ``Buttons``\:

.. image:: ../_static/qt_design6.png
    :scale: 100%
    :align: center

.. image:: ../_static/qt_design7.png
    :scale: 100%
    :align: center

\  **8.** \Andate nel\  ``Property Editor`` \e cambiate il campo\  ``objectName`` \in\  ``chkActivate`` \ed il campo\  ``text`` \in\  ``Activate\n(check)`` \:

.. image:: ../_static/qt_design8.png
    :scale: 100%
    :align: center

.. image:: ../_static/qt_design9.png
    :scale: 100%
    :align: center

\  **9.** \Posizionate i widget in modo che la form appaia come nella figura successiva: 

.. image:: ../_static/qt_design10.png
    :scale: 100%
    :align: center

\  **10.** \Salvate i cambiamenti selezionando\  ``File > Save`` \nella barra dei menu.


\  **11.** \Aprite una shell e spostatevi nella cartella\  ``/home/qgis/workspace/vector_selectbypoint``\: ricompilate con il comando 'make'::

    $ cd /home/qgis/workspace/vector_selectbypoint
    $ make
    pyuic4 -o ui_vector_selectbypoint.py ui_vector_selectbypoint.ui

Notate il comportamento del *Makefile*, il quale riconosce che ci sono stati dei cambiamenti al solo file\  ``.ui`` \e non al file\  ``.qrc`` \file, per cui solo il primo viene ricompilato.

-----------------------------------------------

\2) Implementare l'azione click nell'area mappa
-----------------------------------------------

\  **1.** \Aprite gedit:

.. image:: ../_static/open_gedit.png
    :scale: 100%
    :align: center


\  **2.** \Navigate fino alla cartella di lavoro\
``/home/qgis/workspace/vector_selectbypoint`` \ed aprite il file\  ``vector_selectbypoing.py``\. Il vostro codice dovrebbe apparire come
quello in\  `questo file <../_static/mapcanvas_click_1.py>`_ 


\  **3.** \Analizziamo questo file:

* QGIS ha bisogno di alcuni metodi speciali, come\  ``initGui()``\,\  ``__init__()`` \e\  ``unload``\. Analizzando i commenti al codice possiamo intuire che le funzioni\  ``initGui()`` \e\  ``__init__()`` \vengono chiamate all'avvio del plugin e che parte del codice nella funzione\  ``initGui()`` \aggiunge il nostro plugin al menu. La funzione\  ``unload()`` \fa la cosa opposta.

* Notate, inoltre, che il riferimento alla classe\  ``QgsInterface``  \si trova in\  ``__init__()``\. Da questo attributo di classe possiamo creare un riferimento ad altre parti del sistema QGIS, come ad esempio l'area mappa.

* Altra cosa importante da notare è che il nostro dialogo viene creato sotto il metodo\  ``run()`` \con le seguenti linee di codice::

    dlg = vector_selectbypointDialog()
    # mostra il dialogo
    dlg.show()

* La classe\  ``vector_selectbypointDialog()`` \instanziata dal codice precedente è importata dal modulo Python del dialogo. Aprendo il modulo Python possiamo notare come esso fa riferimento all'altro modulo compilato dal file\  ``.ui`` \ --\  ``ui_vector_selectbypoint.py``\. In testa al file troveremo::

    from vector_selectbypointdialog import vector_selectbypointDialog

* L'esecuzione del metodo\  ``run()``\, quindi, si ferma in attesa di input: nel nostro caso l'input utente è il click del mouse. Il resto del codice del metodo\  ``run()`` \controlla quale pulsante tra\  ``Cancel == 0 e OK == 1`` \è stato cliccato. In genere la maggior parte del codice di un plugin finisce all'interno del metodo\  ``run()``\, anche se non è obbligatorio che stia proprio lì::

    result = dlg.exec_()
    # Controlla se è stato premuto OK
    if result == 1:
        # qui andrà del codice
        # al posto di pass
        pass 


\  **4.** \Ora siamo pronti per scrivere realmente del codice. Il nostro tool necessita di un riferimento all'area mappa e di un riferimento al tool *click*. Fate in modo che la vostra funzione\  ``__init__()`` \appaia come di seguito::

    def __init__(self, iface):
        # Salviamo il riferimento all'interfaccia di QGIS
        self.iface = iface
        # Riferimento all'area mamma
        self.canvas = self.iface.mapCanvas() #CHANGE
        # questo tool di QGIS emette un QgsPoint ad ogni click del mouse sull'area mappa
        self.clickTool = QgsMapToolEmitPoint(self.canvas)


\  **5.** \Generalmente quando si lavora con elementi della GUI di QGIS, è necessario importare le classi e le funzioni del modulo\  ``qgis.gui``\. La classe\  ``QgsMapToolEmitPoint`` \usata per creare il "tool punto" si trova proprio tra questi elementi. Aggiungete in testa al vostro modulo\  ``vector_selectbypoint.py`` \la seguente dichiarazione di *import*::

    from qgis.gui import *


\  **6.** \A questo punto abbiamo i riferimenti necessari ad implementare il nostro "click" ed ottenere un qualche risultato nella forma di un\  ``QgsPoint``\, ma dobbiamo ragionare su come il tutto funziona. In QGIS (e in molte altre applicazioni) esiste il concetto di **evento/azione**, rispettivamente **signal** e **slots** secondo la terminologia Qt. Quando un utente clicca con il mouse sull'area mappa, viene trasmesso un segnale che informa dell'accaduto. Altre funzioni del nostro programma possono sottoscrivere tale trasmissione, quindi reagire in tempo reale ad un click del mouse. Il concetto potrebbe sembrare poco intuitivo e non facile da programmare, per cui si consiglia di seguire con attenzione e cercare di capire al meglio l'esempio che segue: ritorneremo sull'argomento con ulteriori dettagli. Per chi fosse interessato ad approfondire il tema si rimanda alla documentazione web\  `PyQt signals and slots <http://www.commandprompt.com/community/pyqt/c1267>`_\.


\  **7.** \Per ottenere il risultato discusso finora, abbiamo bisogno ancora di due cose: 1) un modo per registrare una funzione all'evento click nell'area mappa e 2) una funzione che viene chiamata quando un tasto del mouse viene premuto all'interno dell'area mappa. Probabilmente il posto giusto dove mettere del codice di sottoscrizione ad un segnale "click-del-mouse" è nella funzione\  ``initGui()``\. Aggiungere il seguente codice nella parte finale di\  ``initGui()`` \ ::

    result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
    QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

La funzione\  ``QObject.connect()`` \è quella registra la funzione\  ``handleMouseDown`` \(che dobbiamo ancora scrivere) in seguito al segnale\  ``canvasClicked()`` \del *clickTool*. Restituisce un valore booleano ad indicare se la connessione ha avuto successo oppure no. Prendiamo la risposta e la inseriamo in una *message box*, per verificare il funzionamento del codice.


\  **8.** \Ora creiamo la funzione\  ``handleMouseDown``  \sotto\  ``initGui()`` \ ::

    def handleMouseDown(self, point, button):
            QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

Il segnale\  ``canvasClicked()`` \emette un\  ``QgsPoint``\. Nella nostra funzione\  ``handleMouseDown()`` \usiamo una *message box* per visualizzare le coordinate X,Y del punto. 


\  **9.** \Infine, dobbiamo assicurarci che il tool click impostato sotto\  ``__init__()`` \sia attivo. Aggiungete il seguente codice all'inizio della funzione\  ``run()`` \ ::

    # attiviamo il clickTool 
    self.canvas.setMapTool(self.clickTool)

\  **10.** \Il vostro file\  ``vector_selectbypoint.py`` \dovrebbe ora essere simile a\  `questo file <../_static/mapcanvas_click_2.py>`_


Testare le modifiche 
********************

\  **1.** \Ritornate in QGIS ed eliminate tutti i layer tranne::

    /home/qgis/natural_earth_50m/cultural/50m_cultural/50m_admin_0_countries.shp

\  **2.** \Aprite il gestore dei plugin. Se il vostro tool\  ``Select_VectorFeatures_By_PointClick`` \è selezionato, deselezionatelo e chiudete il gestore plugin. Riaprite il *Gestore QGIS Plugin* e riattivate il plugin. In tal modo ci assicuriamo che sia caricata l'ultima versione del plugin.

\  **3.** \Notate cosa succede non appena cliccate su 'OK' nel gestore plugin, ma subito prima che l'icona del plugin appaia nella barra dei menu -- o ricevete un messaggio di errore, oppure verrà mostrata una *message box* con scritto\  ``connect = True``\:

.. image:: ../_static/connect_equals_true.png
    :scale: 100%
    :align: center

Se avete ricevuto un errore, cercate di individuarlo e di risolverlo. 

\  **4.** \Cliccate sull'icona del vostro plugin:

.. image:: ../_static/click_vector_selectbypoint_tool.png
    :scale: 100%
    :align: center


\  **5.** \Dovreste notare due cose. La *form* ha ora un nuovo aspetto; quando passate col mouse sull'area mappa, il cursore del mouse assume la forma di un mirino. Cliccate in un punto dell'area mappa e dovreste vedere una *message box* che mostra le coordinate del punto cliccato:

.. image:: ../_static/point_feedback.png
    :scale: 70%
    :align: center

Di nuovo, se ricevete degli errori, cercate di individuarli e correggerli. Ricordate che dopo ogni modifica dovrete ricaricare il plugin in QGIS.


Collegare l'output di QgsPoint alla GUI
***************************************

\  **1.** \Aprite il file ``vector_selectbypointdialog.py``::

    from PyQt4 import QtCore, QtGui
    from ui_vector_selectbypoint import Ui_vector_selectbypoint
    # dialogo per zoom al punto
    class vector_selectbypointDialog(QtGui.QDialog):

        def __init__(self):
            QtGui.QDialog.__init__(self)
            # impostazione interfaccia utente
            self.ui = Ui_vector_selectbypoint()
            self.ui.setupUi(self)

Alcune cose da notare su questo file:

    * Questo modulo Python è una sottoclasse di QtGui.QDialog che ingloba\  ``ui_vector_selectbypoint.py``\. Notate che importiamo quest'ultimo modulo con le righe\  ``from ui_vector_selectbypoint import Ui_vector_selectbypoint``\.

    * L'obiettivo di questo codice è di astrarre l'impostazione dell'interfaccia utente, così da evitare la sua gestione nel modulo Python principale. Ora, per creare il nostro dialogo non facciamo altro che creare un'istanza di\  ``vector_selectbypointDialog``\. 

    * Questa è la classe giusta in cui posizionare proprietà specifiche del dialogo, come la gestione di input ed output e l'interazione con i pulsanti. 

\  **2.** \Aggiungiamo qualche proprietà di supporto per impostare l'input del TextBrowser. Sostituiamo il codice generico QMessageBox per l'output di QgsPoint. Modificate il codice di\  ``ui_vector_selectbypoint.py`` \in modo che risulti come di seguito. Ricordate che\  ``txtFeedback`` \è l'\  ``objectName`` \che abbiamo dato a TextBrowser in Qt Designer::

    from PyQt4 import QtCore, QtGui
    from ui_vector_selectbypoint import Ui_vector_selectbypoint
    # dialogo per zoom al punto
    class vector_selectbypointDialog(QtGui.QDialog):

        def __init__(self):
            QtGui.QDialog.__init__(self)
            # impostazione interfaccia utente
            self.ui = Ui_vector_selectbypoint()
            self.ui.setupUi(self)

        def setTextBrowser(self, output):
            self.ui.txtFeedback.setText(output)
         
        def clearTextBrowser(self):
            self.ui.txtFeedback.clear()


\  **3.** \Ora aprite\  ``vector_selectbypoint.py`` \e commentate il codice delle *message box*::

    #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

\  **4.** \Spostate la creazione del dialogo da\  ``run()`` \alla funzione\  ``__init__``\, in modo che diventi accessibile a tutte le funzioni della classe::

    # cre il nostro dialogo
    self.dlg = vector_selectbypointDialog()

\  **5.** \Da notare che la variabile\  ``dlg`` \è una variabile instanza di classe, per cui è necessario che tutti i riferimenti alla stessa includano la string\  ``self.``\. Modificate tutti i riferimenti a\  ``dlg`` \sotto la funzione ``run()``::

    # mostra il dialogo
    self.dlg.show()
    result = self.dlg.exec_()

\  **6.** \Infine, dirigiamo l'output di QgsPoint nel *TextBrowser* tramite le proprietà di supporto. Notate che prima di impostare il contenuto di *TextBrowser* cancelliamo il suo valore precedente. Riscrivete il codice di\  ``handleMouseDown`` \come di seguito::

    def handleMouseDown(self, point, button):
            self.dlg.clearTextBrowser()
            self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
            #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

\  **7.** \Il codice dovrebbe essere simile a \  `questo <../_static/mapcanvas_click_3.py>`_

\  **8.** \Salvate le modifiche e chiudete i file. Ricaricate il plugin (ricordate che se il plugin è già caricato, bisogna deselezionarlo nel gestore dei plugin e chiudere quest'ultimo, riaprire il gestore dei plugin e ricaricare il vostro plugin). Ora, dopo ogni click, dovreste vedere l'output di QgsPoint nel *TextBrowser*:

.. image:: ../_static/qgspoint_to_gui.png
    :scale: 100%
    :align: center


\3) Implementare la selezione di elementi
-----------------------------------------

L'obiettivo, ora, è di selezionare l'elemento su cui clicchiamo nell'area mappa. Abbiamo solo un paio di cose da implementare:

    1. Abbiamo bisogno di un modo per connettere la funzione che gestirà l'operazione di selezione all'evento click nell'area mappa
    2. Dobbiamo scrivere la funzione per la selezione

\  **1.** \Come prima cosa scriviamo una nuova connessione al segnale\  ``canvasClicked()``\. Scriveremo il codice della funzione di selezione\  ``selectFeature()`` \nel passaggio successivo. Notate che la connessione è implementata allo stesso modo di\  ``handleMouseDown()``\. Scrivete il seguente codice alla fine di ``initGui()``::

        # connette la funzione di selezione al segnale canvasClicked
        result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
        QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )
 
Ancora una volta utilizziamo QMessageBox per controllare la correttezza dell'operazione.

\  **2.** \Ora scriviamo la funzione di selezione. Leggete attentamente i vari commenti per capire il codice seguente. Il tutto dovrebbe essere abbastanza familiare, in quanto abbiamo fatto già esempi simili::

     def selectFeature(self, point, button):
            QMessageBox.information( self.iface.mainWindow(),"Info", "in selectFeature function" )
            # risultati filtrati in base ad un rettangolo
            pntGeom = QgsGeometry.fromPoint(point)  
            # buffer di 2 unità di mappa
            pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0) 
            rect = pntBuff.boundingBox()
            # acquisisce layer corrente e fornitore
            cLayer = self.canvas.currentLayer()
            selectList = []
            if cLayer:
                    provider = cLayer.dataProvider()
                    feat = QgsFeature()
                    # crea la dichiarazione di selezione
                    provider.select([],rect) # gli argomenti significano: no attributi, filtro rettangolo per limitare il numero di elementi  
                    while provider.nextFeature(feat):
                            # se la geometria selezionata interseca il nostro punto, inseriscila in una lista
                            if feat.geometry().intersects(pntGeom):
                                    selectList.append(feat.id())

                    # effettua la selezione
                    cLayer.setSelectedFeatures(selectList)
            else:
                    QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )

\  **3.** \Il vostro modulo Python dovrebbe, ora, essere simile a \  `questo <../_static/featureselect_1.py>`_

\  **4.** \Salvate le modifiche e chiudete i file. Ricaricate il plugin e testatelo. Dovreste vedere due *message box*: una che testa la connessione, l'altra in seguito ad un click del mouse nell'area mappa. Il secondo messaggio ci dice che ci troviamo nella funzione\  ``in selectFeature``\. Il codice scritto dopo questo messaggio effettuerà una selezione o restituirà un messaggio di errore:

.. image:: ../_static/in_selectfeature.png
    :scale: 100%
    :align: center


\4) Implementare il tool Activation w/ Checkbox
------------------------------------------------------

E' tempo di collegare il tool *active/inactive* allo stato della casella di controllo in basso a sinistra nel dialogo. Abbiamo bisogno di due cose:

1.  Creare una connessione al segnale della casella di controllo che viene emesso quando si clicca la stessa. La funzione *handler* controllerà lo stato (*checked* - *unchecked*) della casella di controllo. 

2.  Creare la funzione *handler* che controlla lo stato della casella di controllo e, di conseguenza, abilita/disabilita la connessione al segnale "cliccato" dell'area mappa. 

\  **1.** \Aggiungiamo una connessione al segnale della casella di controllo\  ``stateChanged()`` \alla fine di\  ``initGui()``\. Il nome della funzione che risponderà all'evento è\  ``changeActive()``\; la scriveremo in un passaggio successivo::

    QObject.connect(self.dlg.ui.chkActivate,SIGNAL("stateChanged(int)"),self.changeActive)

\  **2.** \Già che ci troviamo nella funzione\  ``initGui()``\, commentiamo il codice per connettere la funzione\  ``handleMouseDown`` \e la funzione\  ``selectFeature``\; tale codice sarò spostato sotto la funzione *handler* della casella di controllo:: 

    # connessione della nostra funzione al segnale canvasClicked
    #result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
    #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    # connessione della funzione di selezione al segnale canvasClicked
    #result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
    #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )


\  **3.** \Abbiamo creato una funzione che si attiva ogni volta che lo stato della casella di controllo cambia da *checked* a *unchecked* e viceversa. Se la casella di controllo è attiva, allora dobbiamo connegare\  ``handleMouseDown`` \e\  ``selectFeature`` \al segnale click del mouse nell'area mappa; se la casella di controllo è disattivata, dobbiamo disconnetterci dal segnale di click::

   def changeActive(self,state):
        if (state==Qt.Checked):
                # connessione al segnale click
                QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
                # connessione della funzione di selezione al segnale canvasClicked
                QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
        else:
                # disconnessione dal segnale click
                QObject.disconnect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
                # disconnessione della funzione di selezione dal segnale canvasClicked
                QObject.disconnect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)

\  **4.** \Il vostro codice deve essere simile a \  `questo <../_static/activate_click_1.py>`_

\  **5.** \Salvate e chiudete il vostro modulo. Ricaricate il plugin.

\  **6.** \Lanciate il plugin; la casella di controllo dovrebbe essere disattivata, quindi non riceverete nessun output nel *TextBrowser*, nè tantomeno potrete selezionare degli elementi.

.. image:: ../_static/plugin_tut_notactive.png
    :scale: 100%
    :align: center

\  **8.** \Ora attivate la casella di controllo e cliccate sulla mappa. Dovreste vedere delle coordinate X,Y nel *TextBrowser* e qualche elemento selezionato.

.. image:: ../_static/plugin_tut_active.png
    :scale: 100%
    :align: center

--------------------------------

\5)  Ottimizzazione del tool
-------------------------------------

Nel modulo\  ``vector_selectbypoint.py`` \ci sono un paio di cose che potrebbero essere ottimizzate: 

    \  **1.** \Ogni volta che clicchiamo sull'are mappa viene emesso un segnale, in seguito al quale il nostro *slot* (la funzione *handler* che gestisce il segnale)\  ``selectFeature()`` \viene eseguito e fa una serie di cose prima di selezionare un elemento:

        * acquisisce il layer corrente ed imposta una variabile di funzione locale
        * acquisisce il fornitore del layer corrente ed imposta una variabile di funzione locale

    **SOLUZIONE**\: non è questo il posto adeguato per questo genere di cose. Riorganizziamo il codice per la gestione degli eventi e rendiamo il tutto un pò più semplice. Quando un layer viene selezionato in legenda, esso emette un segnale: questo è il posto opportuno dove posizionare il codice per il layer corrente e per il fornitore, in quanto gestiremo i layer uno alla volta singolarmente.

    \  **2.** \Il *TextBrowser* è sottoutilizzato, mostrando le sole coordinate dei punti cliccati nell'area mappa.

    **SOLUZIONE**\: inviamo qualcosa di più utile nel *TextBrowser*, ad esempio un attributo 'NAME' (se esiste) di un dato layer. 

------------------------------

Riorganizziamo un po' il codice:

\  **1.** \Concentriamoci sulle variabili sotto\  ``__init__()``\. Vogliamo assicurarci che in seguito ad una selezione ci sia una variabile per gestire:

    * la lista degli elementi selezionati
    * il layer corrente
    * il fornitore del layer corrente

Optare per le variabili di classe, piuttosto che per le variabili di funzione, ci permette di rendere le variabili stesse accessibili a tutte le funzioni. Allo stato attuale del codice, tutte queste variabili sono impostate nella funzione\  ``selectFeature()`` \ e solo questa funzione può utilizzarle. Dobbiamo spostare la variabile\  ``selectList`` \da\  ``selectFeature()`` \a\  ``__init__()``\: stessa cosa per le variabili\  ``cLayer`` \e\  ``provider``\. Fate in modo che la vostra\  ``__init__()``  \appaia come di seguito::

    def __init__(self, iface):
        # riferimento all'interfaccia di QGIS
        self.iface = iface
        # riferimento all'area mappa
        self.canvas = self.iface.mapCanvas() 
        # clickTool emette un QgsPoint ad ogni click del mouse
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # crea il dialogo
        self.dlg = vector_selectbypointDialog()
        # crea lista per gli ID degli elementi selezionati
        self.selectList = []
        # riferimento al layer corrente (impostato in handleLayerChange)
        self.cLayer = None
        # riferimento al fornitore del layer corrente (impostato in handleLayerChange)
        self.provider = None 

\  **2.** \Ora modificate tutti i riferimenti (molti dei quali sono sotto\  ``selectFeature()``  \), aggiundendo loro il prefisso\  ``self.``\. 


\  **3.** \Creiamo la funzione\  ``updateTextBrowser()`` \a sostituzione della funzione\  ``handleMouseDown()`` \che aggiorna il *TextBrowser* con le coordinate del punto. Affidatevi ai commenti per capire i vari passaggi::

    def updateTextBrowser(self):
        # se esiste un elemento selezionato
        if self.selectList:
            # trova l'indice della colonna 'NAME'
            nIndx = self.provider.fieldNameIndex('NAME')
            # acquisisci l'elemento selezionato dal fornitore. Dobbiamo passare attraverso una lista vuota e l'indice colonna di interesse
            sFeat = QgsFeature()
            if self.provider.featureAtId(self.selectList[0], sFeat, True, [nIndx]):
                # solo se 'NAME' esiste
                if nIndx != -1:
                    # acquisisci la attributeMap dell'elemento
                    attMap = sFeat.attributeMap()
                    # elimina valori esistenti in TextBrowser  
                    self.dlg.clearTextBrowser()
                    # aggiorna TextBrowser con attributeMap[nameColumnIndex] 
                    # 'NAME' è una QString. Va trasformata in una stringa Python
                    self.dlg.setTextBrowser( str( attMap[nIndx].toString() ))


\  **4.** \Ci serve un modo per chiamare la nostra funzione\  ``updateTextBrowser()``\. Potremmo creare una connessione di segnale, ma vogliamo assicurarci un ordine sequenziale degli eventi, nel senso che vogliamo aggiornare *TextBrowser* solo in seguito all'esecuzione della funzione\  ``selectFeature()``\. A tal scopo, chiameremo la funzione\  ``updateTextBrowser()`` \alla fine della funzione ``selectFeature()``::

    if self.selectList:
            # effettua la selezione 
            self.cLayer.setSelectedFeatures(self.selectList)
            # aggiorna il TextBrowser
            self.updateTextBrowser()  

Di seguito la funzione\  ``selectFeature()`` \nella sua interezza::

    def selectFeature(self, point, button):
        # resetta la lista selezione in seguito ad ogni nuova selezione
        self.selectList = []
        #QMessageBox.information( self.iface.mainWindow(),"Info", "in selectFeature function" )
        # risultati filtrati in base ad un rettangolo 
        pntGeom = QgsGeometry.fromPoint(point)  
        # buffer di 2 unità di mappa
        pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0) 
        rect = pntBuff.boundingBox()
        if self.cLayer:
            feat = QgsFeature()
            # crea dichiarazione di selezione
            self.provider.select([],rect) # gli argomenti significano: no attributi, filtro rettangolo per limitare il numero di elementi
            while self.provider.nextFeature(feat):
                # se la geometria selezionata interseca il nostro punto, inseriscila in una lista
                if feat.geometry().intersects(pntGeom):
                    self.selectList.append(feat.id())

            if self.selectList:
                # effettua la selezione
                self.cLayer.setSelectedFeatures(self.selectList)
                # aggiorna il TextBrowser
                self.updateTextBrowser()
        else:   
                QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )
    
\  **6.** \A titolo di precauzione, scriviamo un paio di linee di codice sotto\  ``run()`` \per impostare il layer corrente ed il fornitore all'apertura del plugin per la prima volta. Molti utenti potrebbero avere già molti layer caricati prima di caricare il nostro plugin. Siccome il nostro layer corrente ed il nostro fornitore sono impostati automaticamente quando un layer diverso viene selezionato, non si avrebbe nessun valore con cui iniziare. Ora la funzione\  ``run()`` \apparirà come di seguito::

    def run(self):
        # imposta il layer corrente se esiste, altrimenti sarà impostato dalla selezione dell'utente
        self.cLayer = self.iface.mapCanvas().currentLayer()
        if self.cLayer: self.provider = cLayer.dataProvider()
        # attiva il clickTool
        self.canvas.setMapTool(self.clickTool) 

        # mostra il dialogo
        self.dlg.show()
        result = self.dlg.exec_()
        # controlla se è stato premuto OK
        if result == 1:
            # qui andrà del codice
	    # al posto di pass
            pass

\  **7.** \Dobbiamo creare una connessione al segnale trasmesso quando il layer corrente viene modificato. Alla fine di\  ``initGui()`` \scriviamo il codice di connessione ad una funzione che creeremo vicino al segnale di QgisInterface ``currentLayerchanged()``::

        # connect to the currentLayerChanged signal of QgsInterface
        result = QObject.connect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer *)"), self.handleLayerChange)
        # QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

\  **8.** \La nostra funzione per gestire la modifica del layer corrente::

    def handleLayerChange(self, layer):
            self.cLayer = self.canvas.currentLayer()        
            if self.cLayer:
                self.provider = self.cLayer.dataProvider()

\  **9.** \L'intero modulo dovrebbe, ora, essere come\  `questo <../_static/vector_selectbypoint(2nd_hour_ex_1).py>`_ \

\  **10.** \Testate i vari cambiamenti. Un buon test consiste nel caricare un paio di shapefile (possibilmente con un campo attributi 'NAME'): passate dall'uno all'altro e cliccate su diversi elementi.
 
