========
Esercizi
========

Visualizzare gli attributi di un layer vettoriale in una casella di testo
--------------------------------------------------------------------------

Dovrete modificare una funzione del plugin\  ``foss4g2011_example1_starter`` \in modo da visualizzare in un casella di testo gli attributi di una layer vettoriale. 

Obiettivo
*********

\  **1.** \Aprite il plugin\  ``foss4g2011_example1_starter`` \avendo precaricato un layer vettoriale in QGIS

.. image:: ../_static/ex1_openplugin.png
    :scale: 100%
    :align: center

\  **2.** \Cliccate in un punto qualsiasi della mappa: vederete aprirsi una finestra di dialogo contenente una casella di testo

.. image:: ../_static/ex1_exoutput.png
    :scale: 100%
    :align: center

\  **3.** \Aprite con *gedit* il file \  ``/home/qgis/.qgis/python/plugins/foss4g2011_example1_starter/foss4g2011_example1_starter.py``\. Individuate la funzione\  ``updateTextBrowser()``\. Di seguito il codice che dovrete cambiare::

    def updateTextBrowser(self):
        # verificate che ci sia almeno un elemento nella selectList -- ci potrebbero essere più elementi
        if self.selectList:

            # ***************ESEMPIO 1 Modifiche di seguito********************
            ''' scrivete un codice che visualizzi gli attributi di un singolo elemento selezionato nella casella di testo TextBrowser. 
               Invece di usare dataProvider.select(), usate dataProvider.featureAtId() '''
     
            self.dlg.setTextBrowser("example text output\n to TextBrowser")


Suggerimenti
************

Abbiamo trascorso l'ultima ora facendo esempi con\  ``dataProvider.select()`` \e\  ``dataProvider.featureAtId()``\. Usate il codice che segue come guida per scrivere la vostra funzione::

        if self.selectList:

            # ############ESEMPIO 1 MOdifiche di seguito ####################  
            '''scrivete un codice che visualizzi gli attributi di un singolo elemento selezionato nella casella di testo  TextBrowser. 
               Invece di usare dataProvider.select(), usate dataProvider.featureAtId() '''
            # acquisite gli indici di campo dell'elemento
            fields = self.provider.fields()
            # acquisite l'elemento
            feat = QgsFeature()
            # lavorate sul primo elemento: potrebbe essercene più d'uno
            if self.provider.featureAtId(self.selectList[0], feat, True, fields.keys()):
                attMap = feat.attributeMap()
                output = "FEATURE ID: %i\n" % feat.id()
                for index,qgsfield in fields.items():
                    output += "\t" + str(qgsfield.name()) + " : " + str( (attMap[index]).toString() ) + "\n" 
                self.dlg.setTextBrowser(output)


Soluzione
*********

Trovate la soluzione nel file\  ``/home/qgis/.qgis/python/plugins/foss4g2011_example1_solution/foss4g2011_example1_solution.py``\:

.. image:: ../_static/ex1_solutionset.png
    :scale: 100%
    :align: center
