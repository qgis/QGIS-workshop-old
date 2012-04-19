=============================
Esercizi
=============================

Obiettivo: Leggere valori raster on-the-fly
-------------------------------------------

In questo esercizio dovrete implementare un semplice plugin per visualizzare i valori di celle raster. Lo scopo è quello di abituarvi a concepire i vari step di programmazione. L'esercizio ha una componente\  **di base** \ed una\  **avanzata**\.

Esercizio di base
-----------------

Se non vi sentite a vostro agio nell'utilizzo del Plugin Builder per implementare un tool dall'inizio alla fine, potete modificare un plugin esistente.

1. Aprite QGIS e caricate il layer raster\  ``/home/qgis/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif``
2. Cliccate sul plugin chiamato ``foss4g2011_example2_solution``/``E#2SOL`` 
3. Portate il mouse sull'area mappa e notate come i valori RGB cambiano dinamicamente. Questo è il risultato finale cui dovete puntare
4. Portatevi nella cartella\  ``/home/qgis/.qgis/python/plugins/foss4g2011_example2_starter/``
5. Aprite i file\  ``foss4g2011_example2_starter.py`` \e\  ``foss4g2011_example2_starterdialog.py`` \ed individuate le porzioni di codice commentato. Potete decommentare il codice di questi due file per arrivare alla risoluzione dell'esercizio.

Esercizio avanzato
------------------

I requisiti del tool
********************

* Mostrare i valori di ogni banda raster al passaggio del mouse. Il tool deve funzionare, in effetti, sia con raster a banda singola in scala di grigi, sia con raster RGB. Non serve gestire il click del mouse, ma solo il passaggio del cursore del mouse sull'area mappa.

* L'output deve essere presentato in una GUI (a voi la scelta di come implementare tale GUI).

Suggerimenti
************

* Collegate una funzione al segnale dell'area mappa\  `xyCoordinates <http://www.qgis.org/api/classQgsMapCanvas.html#bf90fbd211ea419ded7c934fd289f0ab>`_ \

* Dovreste ottenere i valori del raster per ogni banda come di seguito::

    rLayer = self.iface.mapCanvas().currentLayer()
    success, data = rLayer.identify(QgsPoint(-122, 47))
    for band, value in data.items():
        print str(band) + " = " + str(value)

Soluzione
*********

Una possibile soluzione è data dai seguenti moduli:

    * \  `Modulo Python principale <../_static/rastervaluedisplay.py>`_

    * \  `Il dialogo <../_static/rastervaluedisplaydialog.py>`_

    * \  `Il modulo "ui" compilato <../_static/ui_rastervaluedisplay.py>`_

L'immagine seguente dà un'idea del plugin:

.. image:: ../_static/raster_value_final.png
    :scale: 100%
    :align: center

