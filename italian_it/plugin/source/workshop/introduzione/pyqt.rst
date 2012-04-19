=====
PyQt
=====

Cos'è PyQt
----------

PyQt è il binding Python alle librerie Qt C++. Ciò significa che si può usare Python per creare applicazioni Qt, invece di C++.

Da PyQT a PyQGIS
----------------

L'utilizzo dei wrapper PyQt per accedere alle librerie di QGIS si deve a ragioni pratiche, in quanto QGIS stesso è sviluppato sulla base delle librerie Qt. Un'altra ragione sta, secondo il\  `PyQGIS cookbook <http://www.qgis.org/pyqgis-cookbook/intro.html>`_\, nell'estrema popolarità di Python.

Esempi
------

Seguono due esempi, il primo relativo ad un design Qt in XML ed il secondo ad un modulo PyQt.

Lo schema XML definisce il layout dell'interfaccia grafica. E' stato creato utilizzando il Qt Designer, un programma che aiuta nella costruzione di interfacce grafiche tramite l'utilizzo di widget. I widget sono, quindi, salvati nello schema XML. XML, come HTML, è un linguaggio che definisce la struttura dei dati, ma non la funzione.

Esempio di una struttura XML di QT Designer::

    <?xml version="1.0" encoding="UTF-8"?>
    <ui version="4.0">
     <class>Dialog</class>
     <widget class="QDialog" name="Dialog">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>400</width>
        <height>300</height>
       </rect>
      </property>
      <property name="windowTitle">
       <string>Dialog</string>
      </property>
     </widget>
     <resources/>
     <connections/>
    </ui>

Una volta renderizzata, la struttura XML produce il semplice dialogo visibile nella figura seguente:

.. image:: ../_static/qt_designer_form_example.png
   :scale: 100 %
   :align: center 

Una struttura XML che definisce una GUI va preventivamente trasformata in un modulo python, prima di poter essere utilizzata in un'applicazione PyQt. Il modulo PyQt che segue è stato prodotto utilizzando un utile tool, di cui si parlerà più in dettaglio di seguito:

    * **pyuic4**: uno script Python che compila un layout XML di QT Designer XML in un modulo Python

Se si compila un file XML utilizzando\  **pyuic4** \, si otterrà automaticamente il codice PyQt. **pyuic4** funziona secondo la seguente sintassi::

    pyuic4 -x -o form.py form.ui

L'opzione **-x** crea un file python direttamente eseguibile per visualizzare il widget che si sta creando.

Di seguito il modulo Python di output::

    # -*- coding: utf-8 -*-
    
    # Form implementation generated from reading ui file 'form.ui'
    #
    # Created: Sun Sep 11 11:52:22 2011
    #      by: PyQt4 UI code generator 4.8.3
    #
    # WARNING! All changes made in this file will be lost!
    
    from PyQt4 import QtCore, QtGui
    
    try:
        _fromUtf8 = QtCore.QString.fromUtf8
    except AttributeError:
        _fromUtf8 = lambda s: s
    
    class Ui_Dialog(object):
        def setupUi(self, Dialog):
            Dialog.setObjectName(_fromUtf8("Dialog"))
            Dialog.resize(400, 300)
    
            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)
    
        def retranslateUi(self, Dialog):
            Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", N
    one, QtGui.QApplication.UnicodeUTF8))
    
    
    if __name__ == "__main__":
        import sys
        app = QtGui.QApplication(sys.argv)
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
        
Notate la dichiarazione::

    from PyQt4 import QtCore, QtGui

Il numero in PyQt4 (4) si riferisce alla versione della libreria: vengono importati anche i moduli *core* delle Qt ed i moduli che permettono di interagire con la GUI. La classe Python del codice definisce il dialogo dell'interfaccia utente. La funzione successiva costruisce l'interfaccia con i pulsanti e le *combobox* specificate nel file XML.

Facciamo un passo avanti ed utilizziamo qualche comando PyQGIS. La cosa interessante è che, utilizzando i comandi PyQGIS, vedremo lavorare in background gli oggetti PyQt, essendo PyQGIS un binding a PyQt. 
Il codice seguente, eseguito nella console, permette di accedere al layer attivo nella legenda di QGIS::

    >>> layer = qgis.utils.iface.activeLayer()
    >>> layer.getLayerID()
    PyQt4.QtCore.QString(u'TM_WORLD_BORDERS_0_3_90091320110704184935426')
    >>> layer.featureCount()
    144L
    >>> layer.srs()
    <qgis.core.QgsCoordinateReferenceSystem object at 0x3d10b78>
    >>> layer.source()
    PyQt4.QtCore.QString(u'/home/gcorradini/DATA/SHAPES/world_borders/TM_WORLD_BORDERS-0.3_900913.shp')
    >>> layer.setTransparency(50)
    >>> layer.wkbType()
    3
    >>> # 3 == MultiPolygon type
    ... 
    >>> layer.name()
    PyQt4.QtCore.QString(u'TM_WORLD_BORDERS-0.3_900913')

Vedete tutti quei tipi di dato\  ``PyQt4.QtCore.QString`` \in azione? Il codice acquisisce il layer attivo, stampa l'ID del layer, il numero di elementi, il sistema di riferimento, il path ed il tipo WKB (well-known-binary).




