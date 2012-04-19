==============================================
Tutorial #1 -- Installare plugin in QGIS
==============================================

Vediamo come installare i plugin Python in QGIS; aggiungeremo, inoltre, il repository PyQGIS FOSS4G.

\  **1.** \Nella barra dei menu di QGIS cliccare su\  ``Plugins > Recupero Plugin Python``\:

.. image:: ../_static/plugins_menu_click_1.png
    :scale: 100%
    :align: center

\  **2.** \Si aprirà una finestra di dialogo che si connetterà a vari reporitory recuperando i plugin disponibili. Cliccate su\  ``Annulla scarico`` \in caso di blocco della finestra:

.. image:: ../_static/Abort_Fetching.png
    :scale: 100%
    :align: center 

\  **3.** \Ora dovreste vedere l'*Installatore QGIS Python Plugin* con la lista dei plugin disponibili. E' possibile aggiungere repository di terze parti cliccando sulla scheda\  ``Repository`` \e sul pulsante\  ``Aggiungi repository di terze parti``\: 

.. image:: ../_static/add_3rd_partyplugins_new.png
    :scale: 100%
    :align: center

\  **4.** \Ora aggiungeremo un nuovo repository, contenente il codice di esempio per questo workshop. Cliccate sul pulsante\  ``Add`` \nella scheda\  ``Repository`` \tab. Assegnate il nome\  ``foss4g2011`` \al repository ed usare come url::

    http://www.qgisworkshop.org/plugins/plugins.xml

.. image:: ../_static/add_repo.png
    :scale: 70%
    :align: center

.. image:: ../_static/add_repo_url.png
    :scale: 70%
    :align: center

.. note:: E' possibile controllare il repository con il\  `browser web <http://www.qgisworkshop.org/plugins/plugins.xml>`_ \

\  **5.** \Ritornate nella scheda\  ``Plugin`` \e selezionate\  ``foss4g2011`` \dal menu a cascata\  ``Repositories``\:

.. image:: ../_static/filter_foss4g.png
    :scale: 70%
    :align: center

\  **6.** \Selezionate ed installate tutti i plugin del repository cliccando sul pulsante\  ``Installa Plugin``\:

.. image:: ../_static/install_foss4g_plugin.png
    :scale: 70%
    :align: center

\  **7.** \Portatevi, con la shell o con il file manager, nella cartella\  ``/home/qgis/.qgis/python/plugins`` \; dovreste trovare il codice dei plugin::

    $ cd /home/qgis/.qgis/python/plugins/
    $ ls -lah
    total 28K
    drwxr-xr-x 7 qgis qgis 4.0K 2011-09-02 10:24 .
    drwxr-xr-x 4 qgis qgis 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x 2 qgis qgis 4.0K 2011-09-02 10:21 foss4g2011_example1_starter
    drwxr-xr-x 2 qgis qgis 4.0K 2011-09-02 10:21 foss4g2011_example1_solution
    drwxr-xr-x 2 qgis qgis 4.0K 2011-09-02 10:21 foss4g2011_example2_starter
    drwxr-xr-x 2 qgis qgis 4.0K 2011-09-02 10:21 foss4g2011_example2_solution
    drwxr-xr-x 2 qgis qgis 4.0K 2011-09-02 10:24 foss4g2011_example3_starter
    drwxr-xr-x 2 qgis qgis 4.0K 2011-09-02 10:24 foss4g2011_example3_solution
    drwxr-xr-x 2 qgis qgis 4.0K 2011-09-02 10:21 foss4g2011_tutorial1_solution
    drwxr-xr-x 3 qgis qgis 4.0K 2011-07-07 13:41 pluginbuilder

\  **8.** \E' possibile attivare/disattivare i plugin cliccando su\  ``Plugins > Gestione plugins`` \per lanciare il *Gestore QGIS Plugin*:

.. image:: ../_static/plugin_manager_console.png
    :scale: 100%
    :align: center
