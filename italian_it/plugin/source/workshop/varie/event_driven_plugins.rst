.. event driven plugins (3rd hour)

========================================================
Creare plugin event-driven
========================================================

Eventi in QGIS
--------------

La programmazione ad eventi con la libreria Qt utilizza i concetti di segnali e *slot*. Risorse utili per l'apprendimento di questi concetti sono il\  `tutorial PyQt <http://www.commandprompt.com/community/pyqt/c1267>`_ \e la\  `documentazione ufficiale di Qt <http://doc.qt.nokia.com/4.7/signalsandslots.html>`_\. Qui tratteremo i punti essenziali.

Segnali
*******

Gli oggetti Qt (discendenti di QObject) hanno l'abilità di emettere segnali rispetto all'occorrenza di un evento significativo. Ad esempio, nel caso della classe\  ``QgsMapCanvas`` \appare importante che venga trasmesso un QgsPoint quando il mouse passa sull'area mappa: questo segnale è definito da \  `xyCoordinates <http://www.qgis.org/api/classQgsMapCanvas.html#bf90fbd211ea419ded7c934fd289f0ab>`_\. La firma della funzione del segnale di\  ``xyCoordintes`` \è simile a::

    void QgsMapCanvas::xyCoordinates    (   const QgsPoint &    p    )

Usiamo questa firma per definire la connessione e l'interazione con altri oggetti (come vedremo di seguito). 

In PyQt possiamo trasmettere un segnale esistente tramite un riferimento all'oggetto che solitamente emette il segnale stesso. Nell'esempio successivo, avendo un riferimento all'oggetto "area mappa", possiamo emettere il segnale ``xyCoordinates``::

    self.iface.mapCanvas().emit(SIGNAL("xyCoordinates(const QgsPoint &)"), QgsPoint(-122,45))

Slot
****

Gli *slot* ricevono l'informazione del segnale. Possiamo connettere gli *slot* ai segnali usando la funzione\  `QObject.connect() function <http://doc.qt.nokia.com/4.7/qobject.html#connect>`_\. Gli argomenti della funzione sono::

    - Sender (Mittente) -- l'oggetto QObject che emette il segnale
    - Signal (Segnale) -- la firma della funzione del segnale passata come stringa alla macri SIGNAL()
    - Receiver (Ricevente) -- la funzione che acquisisce il segnale 
    - Type (Tipo)-- il tipo di connessione (ai nostri fini, questo argomento non viene considerato)

Avendo, ad esempio, una funzione\  ``listen_xyCoordinates`` \e volendo farle ricevere informazioni dal segnale\  ``xyCoordinates`` \quando viene emesso, possiamo creare uno connessione come di seguito::

    # usiamo solo tre argomenti (sender, signal, receiver)
    QObject.connect(self.iface.mapCanvas(), SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xyCoordinates)

La funzione *slot* che si connette al segnale deve accettare gli stessi argomenti della firma del segnale. Nel caso del segnale\  ``xyCoordinates``\, la nostra funzione deve accettare un QgsPoint. Di seguito la funzione::

    def listen_xyCoordinates(self,point):
        self.dlg.outputTextEdit.append("xyCoordinates - %d,%d" % (point.x() if point else "",point.y() if point else ""))


Creare un segnale personalizzato
********************************

E' possible creare dei segnali personalizzati. Di seguito un esempio di come creare un segnale del genere e connettere ad esso uno *slot*. L'esempio è preso dal plugin\  ``foss4g2011_example3_solution``\:

\  **1.** \Assicuratevi che la vostra classe plugin sia sottoclasse di QObject. Inoltre, la funzione deve chiamare il costruttore QObject sotto\  ``__init__``::

    class foss4g2011_example3_solution(QObject):

        def __init__(self, iface):
            QObject.__init__(self)
            # Salviamo il riferimento a QGIS interface
            self.iface = iface

\  **2.** \Create lo *slot* che riceve il segnale. Notate che accetta un parametro\  ``message`` \non definito nel segnale (interessante)::

     def listen_feedbackStatus(self, message):
            self.dlg.outputTextEdit.append("feedbackStatus - %s" % (message if message else ""))

\  **3.** \Ora connettere lo *slot* al segnale::

    QObject.connect(self, SIGNAL("feedbackStatus(PyQt_PyObject)"), self.listen_feedbackStatus) 

\  **4.** \Ora potete emettere il segnale e passare un messaggio allo *slot*. Il plugin\  ``foss4g2011_example3_solution`` \fa questa cosa in seguito ad un click del mouse::

     def btn_emitFeedbackStatus(self, checked):
           self.emit(SIGNAL("feedbackStatus(PyQt_PyObject)"), "Bruce Lee is my hero!")


Esempio 3
*********

Per il prossimo esercizio installate il plugin Example #3 Starter, da usare come base. Questo plugin fa da *tester* di segnali/*slot*; mette a disposizione un'area di testo ed una barra strumenti che vi permette di ascoltare un segnale o di emettere un segnale di test.

Abbiamo messo a disposizione alcuni esempi di widget che vi permetteranno di connettervi dinamicamente ad un segnale o di emettere dei segnali fittizi. Analizzate il codice e cercate di capirne il funzionamento (analizzate la GUI con il Designer, le funzioni *handler* e le connessioni segnali/*slot*). Dopo avere analizzato il tutto, cercate di creare connessioni ad altri segnali. Avete a disposizione degli esempi di segnale a cui connettervi sotto forma di codice commentato, oltre ad elementi GUI nel Designer disabilitati.

Aprite il Designer a cercate di capire come abilitare la casella di controllo per il segnale su cui volete mettervi in ascolto (Suggerimento: ce ne sono due disabilitate). Una volta abilitati gli elementi della GUI, salvate il file .ui e compilatelo. Aprite QGIS e verificate che il plugin abbia gli elementi GUI abilitati. Ora, ritornate al blocco di codice principale e trovate il codice commentato relativo al segnale abilitato nella GUI: decommentate opportunamente il codice. 

Per i più avventurosi, trovate un segnale di vostro interesse nella documentazione di QGIS, aggiungete un elemento alla GUI (es. una casella di controllo simile a quelle già implementate), aggiungete la connessione al segnale e una funzione *handler* per scrivere l'output nella casella di testo.

