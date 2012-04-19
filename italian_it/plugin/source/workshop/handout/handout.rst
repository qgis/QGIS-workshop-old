
=========================================================
Cose da ricordare ed altri spunti
=========================================================

Utilizzare QgisInterface e QgsMapCanvas per accedere ai layer 
--------------------------------------------------------------

QgisInteface.activeLayer()
**************************

Restituisce un riferimento al layer selezionato in legenda::

    >>> aLayer = qgis.utils.iface.activeLayer()
    >>> aLayer
    <qgis.core.QgsRasterLayer object at 0x99ea6ec>
    >>> aLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

QgsMapCanvas.currentLayer()
***************************

Altra modalità per accedere al layer selezionato in legenda è attraverso `QgsMapCanvas <http://www.qgis.org/api/classQgsMapCanvas.html>`_::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> cLayer = canvas.currentLayer()
    >>> cLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Acquisire tutti i layer visibili con QgsMapCanvas.layers()
**********************************************************

Grazie alla classe QgsMapCanvas possiamo acquisire tutti i layer visibili, tutti quei layer della legenda che sono attivi::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> allLayers = canvas.layers()
    >>> for i in allLayers: print i.name()
    ... 
    50m_populated_places_simple

Acquisire un layer specifico tramite indice e QgsMapCanvas.layer()
******************************************************************

I layer di legenda sono ordinati dall'alto in basso in base ad un indice che parte da **0**. Il layer più in alto è individuato dall'indice **0**. Possiamo passare a\  ``QgsMapCanvas``  \un valore numerico ad indicare l'indice del layer di nostro interesse::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> canvas.layer(0)
    <qgis.core.QgsVectorLayer object at 0x99eaeec>
    >>> canvas.layer(0).name()
    PyQt4.QtCore.QString(u'50m_populated_places_simple') 

----------------------------------

Accedere agli elementi (Attributi e Geometria)
----------------------------------------------

QgsVectorDataProvider.select()
******************************

Ciclo tra gli elementi::

    # using the 50m_admin_0_countries.shp from natural earth download for this example
    cLayer = qgis.utils.iface.mapCanvas().currentLayer()
    provider = cLayer.dataProvider()
    columnList = []
    for i in ['NAME']:
        columnList.append(provider.fieldNameIndex(i))

    rect = QgsRectangle(QgsPoint(0,0),QgsPoint(20, 34))
    provider.select(selectList, rect, True, False)
    feat = QgsFeature()
    while provider.nextFeature(feat):
        att = feat.attributeMap()
        for key, value in att.items(): print str(value.toString())

QgsVectorDataProvider.featureAtId()
***********************************

Avendo a disposizione l'*id* dell'elemento di interesse, non è necessario effettuare un ciclo tra tutti gli elementi::

    # using the 50m_admin_0_countries.shp from natural earth download for this example
    cLayer = qgis.utils.iface.mapCanvas().currentLayer()
    provider = cLayer.dataProvider()
    selectList = [ 24, 32, 45, 56 ]
    if selectList:
        for id in selectList:
            nIndx = provider.fieldNameIndex('NAME')
            sFeat = QgsFeature()
            if provider.featureAtId(id, sFeat, True, [nIndx]):
                if nIndx != -1:
                    attMap = sFeat.attributeMap()
                    print str( attMap[nIndx].toString() )

------------------------------------

Segnali e Slot
----------------------------

Emettere un Segnale
*******************

Di seguito un esempio usando l'oggetto ``QgsMapCanvas``::

    self.iface.mapCanvas().emit(SIGNAL("xyCoordinates(const QgsPoint &)"), QgsPoint(-122,45))

Connettere uno Slot ad un Segnale
*********************************

Connessione della funzione *slot*\  ``listen_xyCoordinates`` \al segnale ``"xyCoordinates(const QgsPoint &)"``::

    # the connection
    QObject.connect(self.iface.mapCanvas(), SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xyCoordinates)

    # the custome slot function
    def listen_xyCoordinates(self,point):
        self.dlg.outputTextEdit.append("xyCoordinates - %d,%d" % (point.x() if point else "",point.y() if point else ""))

------------------------------------

Debug con Pdb
------------------------------

Assicuratevi di importare "pdb" prima di utilizzarlo::
    
    import pdb

Individuate il punto del codice dove intendete iniziare il debug ed aggiungete il seguente codice::

    pyqtRemoveInputHook()
    pdb.set_trace()

Lanciate QGIS da riga di comando: quando la chiamata *set_trace* viene raggiunta, avrete a disposizione un prompt "pdb" a linea di comando. Di seguito un breve elenco di comandi "pdb"; altri esempi nella\  `documentazione ufficiale pdb <http://docs.python.org/library/pdb.html>`_\:

    ``list # lista del codice sorgente con al centro la riga in esecuzione``

    ``list <numero riga> # lista del codice sorgente con <numero riga> al centro``

    ``list <da numero riga> , <a numero riga> # lista del codice sorgente tra <da numero riga> e <a numero riga>``
    
    ``break # senza argomenti restituisce tutti i punti di interruzione ed i loro ID``

    ``break <numero riga> # crea un punto di interruzione alla riga <numero riga>``

    ``next # analisi del codice una riga alla volta. Le funzioni sono eseguite direttamente per passare alla riga successiva, senza analizzarne i dettagli``
    
    ``step # analisi del codice una riga alla volta. Le funzioni sono analizzate nel dettagli``
    
    ``cl <ID punto di interruzione> # rimuove il punto di interruzione individuato da <ID punto di interruzione>``

-----------------------------

Creare un repository di plugin
------------------------------

Esempio di file XML per repository di plugin::

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


