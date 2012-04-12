=====
PyQT
=====

Qu'est ce que c'est
-------------------

PyQt désigne les *bindings* Python qui enrobent la bibliothèque C++ de Qt. Cela signifie que l'on peut maintenant utiliser Python pour construire des applications Qt au lieu d'apprendre le C++.

Comment l'idée de PyQGIS est arrivée
------------------------------------

Utiler les *wrappers* PyQt pour accéder aux bibliothèques QGIS était une solution pratique car QGIS était construit au dessus des bibliothèques Qt. D'après le \  `PyQGIS cookbook <http://www.qgis.org/pyqgis-cookbook/intro.html#python-console>`_ \, une autre raison pour PyQt semble être l'immense popularité de Python.

Exemples
---------

Ci dessous se trouvent deux exemples: le premier est une définition XML pour Qt et le second est un module PyQt.

Le schema XML définit la constitution de l'interfaçe graphique utilisateur (GUI). Il a été créé en utilisant Qt Designer, un programme qui aide à construre des interfaçes graphiques avec des composants à glisser-déposer. Les composants sont ensuites sauvés dans un schéma XML. Il faut noter que XML, comme HTML, est un langage qui définit une structure de données, mais n'est pas un langage fonctionnel.

Exemple d'une structure XML de QT Designer::

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

Une fois effectué le rendu, la structure XML ci-dessus décrit ce type de fenêtre GUI. Un exemple très simple:    

.. image:: ../_static/qt_designer_form_example.png
   :scale: 100 %
   :align: center 


Quand on a une structure XML qui définit notre interface graphique, on a besoin de le transformer en module Python de sorte de pouvoir l'utiliser dans des applications PyQt. Le module PyQt en exemple ci dessous a été produit en utilisant un outil très pratique sur lequel nous reviendrons.

    * pyuic4: Un script Python qui compile un fichier XML Qt Designer en module Python.

Si on compile ce fichier XML en utilisant \  **pyuic4** \ il va créer magiquement du code PyQt. Voici l'instruction de compilation depuis le shell bash::

    pyuic4 -x -o form.py form.ui

Il faut noter que l'option -x crée un fichier python de sortie qui peut être lancé directement, pour voir un exemple de rendu du widget que nous venons juste de créer.    

Voici le résultat -- un module Python::

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
            Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
    
    
    if __name__ == "__main__":
        import sys
        app = QtGui.QApplication(sys.argv)
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())

On remarque tout d'abord l'instruction d'import::        

    from PyQt4 import QtCore, QtGui

Le nombre dans PyQt4 se rapporte à la version avec laquelle on travaille. On importe ici le module noyau de la bibliothèque Qt, et le module qui permet de faire des GUIs.

Il faut noter que la classe Python ci-dessus définit notre boîte de dialogue de l'interface utilisateur. La fonction de classe suivante construit notre interface avec les boutons et les combobox qui étaient spécifiées dans le XML.

Regardons maintenant quelques commandes spécifiques de PyQGIS (nous détaillerons ensuite plus amplement le sujet). Ce qui est intéressant ici est que nous verrons que les objets PyQt fonctionnent en arrière plan (après tout, PyQGIS est basé sur les bindings PyQT). Ce code utilise la console Python pour accéder à la couche sélectionnée de la liste de couches::

    >>> layer = qgis.utils.iface.activeLayer()
    >>> layer.getLayerID()
    PyQt4.QtCore.QString(u'TM_WORLD_BORDERS_0_3_90091320110704184935426')
    >>> layer.featureCount()
    144L
    >>> layer.srs()
    <qgis.core.QgsCoordinateReferenceSystem object at 0x3d10b78>
    >>> layer.source()
    PyQt4.QtCore.QString(u'/home/qgis/DATA/SHAPES/world_borders/TM_WORLD_BORDERS-0.3_900913.shp')
    >>> layer.setTransparency(50)
    >>> layer.wkbType()
    3
    >>> # 3 == MultiPolygon type
    ... 
    >>> layer.name()
    PyQt4.QtCore.QString(u'TM_WORLD_BORDERS-0.3_900913')

 
Voyez tous ces types de données\  ``PyQt4.QtCore.QString`` \en action? On prend la couche active de la liste des couches (actif voulant dire selectionné). On affiche ensuite son layerID, le nombre de feature, le système de projection, le chemin de la source, et le type WKB (Well-Known-Binary) des données. Il s'agit d'un petit aperçu de la puissance que l'on a en accédant à nos couches de données QGIS.




