
=====================================
Python in QGIS
=====================================

Il termine\  **PyQGIS** \si riferisce al binding Python a QGIS, ovvero all'API Python che fa da wrap alla libreria C++ di QGIS.



.. image:: ../_static/pyqgis_tools.png
    :scale: 80%
    :align: center

Utilizzeremo la documentazione\   `C++ QGIS API <http://doc.qgis.org>`_ \per conoscere PyQGIS, in quanto non esiste documentazione specifica. Ciò potrebbe
portare ad una certa confusione, ma la maggior parte del binding Python rispecchia la libreria C++.

Acquisiremo familiarità con la documentazione citata man mano che svilupperemo dei plugin. Per ora basti sapere che ci sono svariati modi per interagire con QGIS utilizzando Python:

    1. \ **Plugin**\: creare/estendere strumenti di interazione con i dati in QGIS 

    2. \ **Console python** \: terminale a linea di comando all'interno di QGIS
 
    3. \ **Script/Applicazioni python**\: scrivere applicazioni partendo da zero ed utilizzando le librerie QGIS e Qt. Tali applicazioni processeranno dati geografici all'esterno di QGIS, ma ne utilizzeranno le funzionalità principali. Ad esempio, si potrebbe contruire un semplice visualizzatore di dati con un set minimo di tool per una specifica attività.

Durante la prima ora del workshop analizzeremo le modalità di installazione dei plugin e l'utilizzo della console Python, per poi concentrarci sullo sviluppo di plugin.

------------------------------------------------------

Plugin QGIS
-----------

QGIS permette di installare numerosi plugin provenienti da varie fonti, sia pubbliche che private.
Il tutorial #1 che segue fornirà delle informazioni introduttive su come aggiungere dei repository di plugin e su come caricare dei plugin in QGIS.

------------------------------------------------------

Console Python 
---------------

L'utilizzo della console è il modo più semplice per testare le proprie idee riguardo lo sviluppo di un plugin. La console permette di accedere ai layer già caricati in QGIS e di interagire con i lori attributi e le loro geometrie, che poi è quello che fanno la maggior parte dei plugin.

Questi argomenti saranno affrontati nel tutorial #2.
