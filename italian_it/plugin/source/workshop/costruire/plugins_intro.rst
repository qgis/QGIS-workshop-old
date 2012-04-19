=====================================
Architettura dei Plugin
=====================================

Un plugin in Python per QGIS si compone essenzialmente di un insieme di file che descrivono le risorse del plugin stesso ed il codice. Di seguito una decrizione di questi tipi di file.

Per creare un plugin Python per QGIS avete bisogno di almeno quattro tipi di file (ma ce ne possono essere di più):
    - un file con estensione\  ``.ui`` \che descrive l'interfaccia grafica (GUI). Questo file deve essere compilato in un modulo Python utilizzando l'utility da linea di comando\  ``pyuic4`` \
    - un file\  ``__init__.py`` \che descrive in termini generali il plugin (es. nome, autore)
    - un file con estensione\  ``.qrc`` \che descrive le risorse che saranno utilizzate dal plugin (es. delle immagini). Questo file deve essere compilato in un modulo Python con l'utility da linea di comando\  ``pyrcc4`` \
    - ed infine il file contenente il codice del plugin. Questo file può avere un nome qualsiasi, ma di solito gli si associa il nome del plugin.

-----------------------------

Per avere un'idea di come questi file sono organizzati in un progetto di plugin, diamo uno sguardo ad un plugin già installato nella macchina virtuale.

\  **1.** \Aprite una nuova shell. La shella bash può essere avviata con\  ``<Cntl>-<ALT>t``\. 

.. image:: ../_static/terminal_window_open.png
    :scale: 70%
    :align: center

\  **2.** \Spostatevi nella cartella nascosta\  ``.qgis`` \; al suo interno troverete le cartelle dei plugin Python::

    $cd .qgis/python/plugins/
    $ ls -lah
    total 17K
    drwxr-xr-x 10 qgis qgis 4.0K 2011-07-17 20:40 .
    drwxr-xr-x  4 qgis qgis 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x  3 qgis qgis 4.0K 2011-07-07 13:41 pluginbuilder
    

Il progetto\  **pluginbuilder** \nella cartella\  ``/home/qgis/.qgis/python/plugins`` \è un plugin con cui acquisiremo familiarità molto presto; esso facilita lo sviluppo dei plugin, creando automaticamente i quattro file di cui si è precedentemente parlato. Il\  **pluginbuilder** \inoltre, predispone del codice modello, che poi modificheremo per adattarlo alle nostre esigenze.

\  **3.** \Spostatevi nella cartella\  ``pluginbuilder`` \ed elencate i file di tipo\  ``.ui, .py and .qrc``\: disinteressiamoci, per il momento, degli altri file, i moduli python compilati (file con estensione\  ``.pyc`` \extension)::

    $ cd pluginbuilder
    $ ls -l *.py *.ui *.qrc
    -rw-r--r-- 1 qgis qgis  1586 2011-07-07 13:41 __init__.py
    -rw-r--r-- 1 qgis qgis  1403 2011-07-07 13:41 pluginbuilder_dialog.py
    -rw-r--r-- 1 qgis qgis  7077 2011-07-07 13:41 pluginbuilder.py
    -rw-r--r-- 1 qgis qgis  2232 2011-07-07 13:41 pluginspec.py
    -rw-r--r-- 1 qgis qgis 22936 2011-07-07 13:41 resources.py
    -rw-r--r-- 1 qgis qgis   143 2011-07-07 13:41 resources.qrc
    -rw-r--r-- 1 qgis qgis  1373 2011-07-07 13:41 result_dialog.py
    -rw-r--r-- 1 qgis qgis  8718 2011-07-07 13:41 ui_pluginbuilder.py
    -rw-r--r-- 1 qgis qgis  7046 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r-- 1 qgis qgis  1734 2011-07-07 13:41 ui_results.py
    -rw-r--r-- 1 qgis qgis  1880 2011-07-07 13:41 ui_results.ui


Ricordate, siamo interessati a capire lo schema dei file. Come vedete, sembra ci siano due GUI associate a questo plugin: basta contare il file con estensione ``.ui``::

    -rw-r--r--  1 qgis qgis 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 qgis qgis 1.9K 2011-07-07 13:41 ui_results.ui

Possiamo notare che ogni file GUI è stato compilato in un modulo Python. Di solito, se la parola\  ``dialog`` \appare in un modulo Python, quest'ultimo lavora insieme al file\  ``ui.py`` \. Quindi, tutti i file seguenti dovrebbero essere relativi alla GUI::

    -rw-r--r-- 1 qgis qgis  1373 2011-07-07 13:41 result_dialog.py
    -rw-r--r-- 1 qgis qgis 1.4K 2011-07-07 13:41 pluginbuilder_dialog.py
    -rw-r--r--  1 qgis qgis 8.6K 2011-07-07 13:41 ui_pluginbuilder.py
    -rw-r--r--  1 qgis qgis 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 qgis qgis 1.7K 2011-07-07 13:41 ui_results.py
    -rw-r--r--  1 qgis qgis 1.9K 2011-07-07 13:41 ui_results.ui

Nel file\  ``__init__.py`` \troverete delle descrizioni generali del plugin, come il suo nome, la versione, il nome dell'autore, etc.::

    def name():
        return "Plugin Builder"
    def description():
        return "Creates a QGIS plugin template for use as a starting point in plugin development"
    def version():
        return "Version 0.3.2"
    def icon():
        return 'plugin_builder.png'
    def qgisMinimumVersion():
        return "1.0"
    def classFactory(iface):
        # load PluginBuilder class from file PluginBuilder
        from pluginbuilder import PluginBuilder
        return PluginBuilder(iface)

Notate, inoltre, il file risorsa associato al progetto. Ricordate che il file\  ``.qrc`` \deve essere compilato in un modulo Python::

    -rw-r--r--  1 qgis qgis  23K 2011-07-07 13:41 resources.py
    -rw-r--r--  1 qgis qgis  143 2011-07-07 13:41 resources.qrc

Possiamo assumere che tutti gli altri file presenti nella cartella (quelli con estensione\  ``.py`` \) servano in qualche modo al funzionamento del plugin. Sembrano esserci altri file di documentazione ed immagini, ma non ce ne occuperemo ora.


