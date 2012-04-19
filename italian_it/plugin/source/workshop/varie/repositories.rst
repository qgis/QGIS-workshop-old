
=====================
Repository di plugin
=====================

Repository ufficiale
--------------------

\ `QGIS Plugin repository <http://plugins.qgis.org/plugins/>`_ \ è la fonte ufficiale di plugin per QGIS. Una vecchia versione di plugin forniti da vari utenti si trova\  `qui <http://pyqgis.org/repo/contributed>`_\. Tradizionalmente gli sviluppatori di plugin dovevano mantenere il proprio repository: molti di questi ancora esistono.

Repository pubblici remoti
---------------------------

Si tratta di repository pubblici mantenuti da terze parti. Potete utilizzare tali repository da ``Recupero Plugin Python > Repository > Aggiungi repository di terze parti``: avrete a disposizione una lista di plugin. Tenete presente che questi plugin non sono gestiti e controllati dal progetto QGIS.


Il tuo repository privato
-------------------------

Se volte crearvi un vostro repository personale, basta scrivere un file XML accessibile via web per informare QGIS su dove scaricare il plugin. Segue un esempio di un tale tipo di file::

    <?xml version = '1.0' encoding = 'UTF-8'?>
    <?xml-stylesheet type='text/xsl' href='/plugins.xsl' ?>
    <plugins>
      <pyqgis_plugin name='Plugin Installer' version='1.1'>
        <description>The recent Python Plugin Installer</description>
        <version>1.1</version>
        <qgis_minimum_version>1.0</qgis_minimum_version>
        <homepage>http://www.bwj.aster.net.pl/qgis/</homepage>
        <file_name>plugin_installer.zip</file_name>
        <author_name>Borys Jurgiel</author_name>
        <download_url>http://spatialserver.net/pyqgis_1.0/plugins/plugin_installer.zip</download_url>
        <uploaded_by>borysiasty</uploaded_by>
        <create_date>2008-12-18</create_date>
        <update_date>2010-10-31</update_date>    
      </pyqgis_plugin>
    </plugins>


Pacchettizzazione
-----------------

Per creare un pacchetto zip del vostro plugin che sia compatibile con quanto richiesto da QGIS, date il seguente comando::

    zip -9vr myPlugin.zip myPlugin/*

