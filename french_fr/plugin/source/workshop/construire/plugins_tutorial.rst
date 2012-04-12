=======================================
Tutoriel -- Créer un plugin simple
=======================================

Créer notre premier plugin avec 'Plugin Builder'
-----------------------------------------------------

Il est temps de nous mettre à l'ouvrage avec le\  **Plugin Builder** \.

\  **1.** \Dans la barre de menu de QGIS cliquer sur l'icone de\  ``Plugin Builder`` \pour lancer le plugin:

.. image:: ../_static/plugin_builder_click1.png
    :scale: 100%
    :align: center

\  **2.** \La boîte de dialogue principale de Plugin Builder va apparaître. C'est la où nous remlpssons les informations générales de configuration que Plugin Builder utilise pour créer les modèles de fichiers. Nous allons ensuite modifier ces modèles de fichiers pour construire notre plugin. Tous les champs de la fenêtre de dialogue sont nécessaires. Remplissez ces champs comme sur l'image, puis cliquez sur le bouton\  ``Ok`` \.:

.. image:: ../_static/plugin_builder_main_dialog.png 
    :scale: 70%
    :align: center

\  **3.** \Une boite de dialogue de choix de fichier apparaît. Créez un répertoire\  ``workspace`` \dans votre espace personnel\  ``/home/formation/`` \. Sauvez votre projet de plugin en sélectionnant le répertoire\  ``workspace`` \dans la boîte de dialogue:

.. image:: ../_static/plugin_builder_save_dir.png 
    :scale: 100%
    :align: center

\  **4.** \Si tout va bien, Plugin Builder va afficher une boîte de dialogue finale qui vous indique les étapes suivantes pour personnaliser votre projet de plugin. Nous allons suivre exactement les mêmes étapes dans la suite.

.. image:: ../_static/plugin_builder_feedback.png 
    :scale: 100%
    :align: center

\  **5.** \Ouvrez un shelle et déplacez vous vers le répertoire de travail de votre plugin\  ``/home/formation/workspace/vector_selectbypoint`` \et affichez le contenu::

    $ cd workspace/vector_selectbypoint/
    $ ls -lah
    total 36K
    drwxr-xr-x 2 formation formation 4.0K 2011-08-20 13:21 .
    drwxr-xr-x 3 formation formation 4.0K 2011-08-20 17:34 ..
    -rw-r--r-- 1 formation formation 1.1K 2011-08-20 13:21 icon.png
    -rw-r--r-- 1 formation formation 1.6K 2011-08-20 13:21 __init__.py
    -rw-r--r-- 1 formation formation 1.9K 2011-08-20 13:21 Makefile
    -rw-r--r-- 1 formation formation  116 2011-08-20 13:21 resources.qrc
    -rw-r--r-- 1 formation formation 1.5K 2011-08-20 13:21 ui_vector_selectbypoint.ui
    -rw-r--r-- 1 formation formation 1.5K 2011-08-20 13:21 vector_selectbypointdialog.py
    -rw-r--r-- 1 formation formation 2.6K 2011-08-20 13:21 vector_selectbypoint.py


Notez que nous avons un seul fichier\  ``.ui`` \et un seul fichier\  ``.qrc`` \qui n'ont pas encore été compilés en module Python. Compilons les et regardons à quoi ressemble notre plugin dans QGIS.

\  **6.** \Par chance nous avons un\  ``Makefile`` \dans ce répertoire que nous pouvons utiliser pour compiler les deux fichiers facilement. Depuis le répertoire\  ``vector_selectbypoint`` \lancer la commande suivante, qui va afficher deux lignes::

    $ make
    pyuic4 -o ui_vector_selectbypoint.py ui_vector_selectbypoint.ui
    pyrcc4 -o resources.py  resources.qrc

Ces deux lignes sont les commandes nécessaires pour compiler les ressources et les fichiers d'interface graphuqe. On peut soit lancer ces commandes individuellement ou juste lancer \ ``make`` \ pour les exécuter d'un seul coup. Chaque fois que des changements sont fait sur les fichiers\  ``resources.qrc`` \ou \  ``ui_vector_selectbypoint.ui`` \il faudra relancer la compilation.

\  **7.** \Réaffichez le contenu du répertoire et vous verrez que de nouveaux modules Python ont été créés. Les modules importants sont ceux ci::
    
    $ ls -lah
    ... # AUTRES FICHIERS LISTES 
    -rw-r--r-- 1 formation formation 5.4K 2011-08-20 17:42 resources.py
    -rw-r--r-- 1 formation formation 1.4K 2011-08-20 17:42 ui_vector_selectbypoint.py
    ... # AUTRES FICHIERS LISTES 

\  **8.** \QGIS va maintenant pouvoir lire ces fichiers dans votre projet et créer le bouton correspondant dans la barre de menu. Cependant, pour que QGIS détecte notre nouveau plugin, nous allons devoir le mettre dans le répertoire\  ``/home/formation/.qgis/python/plugins`` \. Plutôt que de coier tous nos fichiers, faisons un lien symbolique (un raccourci) à partir de notre workspace\  ``/home/formation/workspace/vector_selectbypoing/`` \vers le répertoire\  ``/home/formation/.qgis/python/plugins`` \. De cette façon QGIS va prendre en compte notre projet de plugin mais les fichiers d'origine sont toujours situés dans le répertoire de workspace où on peut les éditer::

     $ ln -s /home/formation/workspace/vector_selectbypoint/ /home/formation/.qgis/python/plugins/

\  **9.** \Si on change de répertoire vers\  ``/home/formation/.qgis/python/plugins`` \et qu'on liste le contenu on devrait voir\  ``vector_selectbypoint`` \pointer vers notre répertoire de travail::

    $ cd /home/formation/.qgis/python/plugins
    $ ls -lah
    total 16K
    drwxr-xr-x 4 formation formation 4.0K 2011-08-20 17:58 .
    drwxr-xr-x 4 formation formation 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x 2 formation formation 4.0K 2011-08-20 12:26 osmpoly_export
    drwxr-xr-x 3 formation formation 4.0K 2011-07-07 13:41 pluginbuilder
    lrwxrwxrwx 1 formation formation   42 2011-08-20 17:58 vector_selectbypoint -> /home/formation/workspace/vector_selectbypoint/

\  **10.** \Revenons dans QGIS et ajoutons le plugin en utilisant l'outil de gestion d'extension de QGIS\  ``Extensions > Gestionnaire d'extensions`` \. Quand le gestionnaire d'extension s'affiche, tapez\  ``Select_`` \dans la barre de filtre en haut et notre plugin devrait apparaître. Cochez la case à gauche du plugin et valider avec le bouton\  ``OK`` \:

.. image:: ../_static/plugin_builder_adding2QGIS.png
    :scale: 100%
    :align: center

\  **11.** \Vous avez du remarquer qu'une icone a été ajoutée dans le menu à droite de l'icone du Plugin Builder. Cliquez dessus:

.. image:: ../_static/click_vector_selectbypoint_tool.png
    :scale: 100%
    :align: center

\  **12.** \Si tout va bien, vous allez voir une boite de dialogue vide avec un bouton\  ``OK`` \et un bouton\  ``Annuler`` \. Comme vous pouvez le constater, le Plugin Builder ne donne pas grand chose d'intéressant à première vue. Nous devons personnaliser le plugin. Mais au moins il fonctionne:

.. image:: ../_static/vector_selectbypoint_firstview.png
    :scale: 100%
    :align: center

----------------------------

Étendre les modèles de Plugin Builder
-----------------------------------------  

Le concept de plugin et le processus d'implémentation
******************************************************

L'outil que nous allons construire va faire quelques opérations basiques:

     1. L'outil va renvoyer les coordonnées X,Y d'un QgsPoint pour chaque clic sur la carte
     2. L'outil va sélectionner toutes les features vecteur qui intersectent ce point
     3. L'outil va avoir une option qui lui permet d'être actif ou inactif en utilisant une case à cocher

.. note:: Cet outil va fonctionner exactement de la même façon que l'outil actuel de selection unique de feature. Le but est d'illustrer les étapes pour créer un plugin. Des exercices à la fin de ce tutoriel vous permettront de vous entraîner.

Nous pouvons séparer les tâches d'implémentation et les résoudre une par une:

    1. Concevoir l'interface dans Qt 4 Designer en éditant le fichier \ ``.ui`` \.
    2. Implémenter le clic sur la carte et la récupération des coordonnées du point
    3. Implémenter la sélection de feature lors du clic quand il y a intersection
    4. Implémenter la fonction d'activation/désactivation avec une case à cocher
    5. Améliorer tout cela pour rendre notre outil plus ergonomique

---------------------------------------

\1) Concevoir l'interface
-------------------------

Discutons de l'apparence de l'interface graphique. Les spécifications pour cet outil sont très simples:

    1. Nous avons besoin d'un moyen d'afficher les coordonnées du point pour l'utilisateur (on utilisera un widget TextBrowser)
    2. Nous avons besoin d'un moyen pour activer et désactiver l'outil (on utilisera un widget checkbox -- case à cocher)

Pour faire des changements sur le GUI, nous allons devoir éditer le fichier \ ``.ui`` \associé à ce projet. Qt Designer est l'éditeur que nous allons utiliser pour faire ce genre d'édition.    


\  **1.** \Ouvrir\  **Qt 4 Designer** \à partir du menu\  ``Applications > Programmation`` \en haut à gauche:

.. image:: ../_static/qt_design1.png
    :scale: 100%
    :align: center

\  **2.** \Une boîte de dialogue s'ouvre. Naviguez vers l'espace de travail de notre plugin à\  ``/home/formation/workspace/vector_selectbypoint/`` \. Seul le fichier\  ``.ui`` \associé à ce projet devrait apparaitre dans la boite de choix de fichier. Il est nommé\  ``ui_vector_selectbypoint.ui`` \. Sélectionnez le et clickez sur\  ``Ouvrir`` \:

.. image:: ../_static/qt_design2.png
    :scale: 100%
    :align: center

\  **3.** \Le formulaire Qt qui s'ouvre devrait vous paraître familier. C'est simplement un formulaire vide avec deux boutons:

.. image:: ../_static/qt_design3.png
    :scale: 100%
    :align: center

\  **4.** \Nous voulons ajouter un TextBrowser et un widget Checkbox à ce formulaire. Tout d'abord cliquez-glissez un widget TextBrowser sur le formulaire. Vous trouverez le TextBrowser dans la colonne de gauche dans la partie\  ``Display Widgets`` \:

.. image:: ../_static/qt_design4.png
    :scale: 100%
    :align: center

\  **5.** \Nous devrions maintenant avoir un objet TextBrowser sur notre formulaire ainsi:

.. image:: ../_static/qt_design5.png
    :scale: 100%
    :align: center

\  **6.** \En sélectionnant le TextBrowser sur le formulaire (affichant les points d'ancre bleus), aller sur la colonne de droite, en bas dans la partie nommée\ ``Éditeur de propriétés`` \et changez le nom de l'objet TextBrowser vers\  ``txtFeedback`` \. L'édition se fait dans le champs\  ``objectName`` \. La valeur que nous donnons ici sera utilisée dans notre code pour représenter le TextBrowser.

.. image:: ../_static/qt_design05.png
    :scale: 100%
    :align: center

\  **7.** \Dans la colonne de droite on cherche le widget Checkbox dans la partie\  ``Buttons`` \. Glissez le widget sur le formulaire. Celui ci ressemble alors à ceci :

.. image:: ../_static/qt_design6.png
    :scale: 100%
    :align: center

.. image:: ../_static/qt_design7.png
    :scale: 100%
    :align: center

\  **8.** \Après avoir sélectionné la CheckBox sur le formulaire (affichant les points d'ancre bleus), aller dans l'\  ``Éditeur de propriétés`` \et changer le champs\  ``objectName`` \à\  ``chkActivate`` \et le champs\  ``text`` \à \  ``Activate\n(check)`` \.:

.. image:: ../_static/qt_design8.png
    :scale: 100%
    :align: center

.. image:: ../_static/qt_design9.png
    :scale: 100%
    :align: center

\  **9.** \Bougez les widgets et redimensionnez les pour que votre formulaire ressemble à ceci :

.. image:: ../_static/qt_design10.png
    :scale: 100%
    :align: center

\  **10.** \Sauvez les modifications en sélectionnant dans la barre de menu :\  ``Fichier > Sauver`` \.


\  **11.** \Dans un shell bash changez de répertoire vers votre espace de travail\  ``/home/formation/workspace/vector_selectbypoint`` \et recompilez tout en utilisant la commande 'make'::

    $ cd /home/formation/workspace/vector_selectbypoint
    $ make
    pyuic4 -o ui_vector_selectbypoint.py ui_vector_selectbypoint.ui

Notez que le Makefile est intelligent. Il sait que seul le fichier\  ``.ui`` \ a été modifié et pas le ficheir\  ``.qrc`` \file. Il ne recompile donc que la partie interface graphique en module Python.

---------------------------------------

\2) Implémentation de l'action de click sur le Canvas
------------------------------------------------------

\  **1.** \L'édition de texte dans un éditeur tel que gedit n'est pas très complexe. Ouvrez gedit en cliquant sur l'entrée de menu de Ubuntu \ ``Éditeur de texte`` \:

.. image:: ../_static/open_gedit.png
    :scale: 100%
    :align: center

\  **2.** \Maintenant naviguez jusque votre répertoire de travail pour les plugins\  ``/home/formation/workspace/vector_selectbypoint`` \et ouvrez le fichier\  ``vector_selectbypoing.py`` \. Votre code devrait ressemble exactement à\  `ce fichier <../_static/mapcanvas_click_1.py>`_ 

\  **3.** \Étudions un certain nombre de choses importantes dans ce fichier.

* QGIS nécessite que certaines méthodes de classe existent dans votre classe principale Python pour que le plugin puisse fonctionner. Il s'agit de\  ``initGui()`` \,\  ``__init__()`` \et\  ``unload`` \. Si nous lisons les commentaires du code de ces fonctions, on peut deviner que\  ``initGui()`` \et\  ``__init__()`` \sont appelées au démarrage du plugin et qu'une partie du code de la fonction\  ``initGui()`` \est responsable de l'ajout de notre plugin dans le menu. La fonction\  ``unload()`` \fait l'inverse. Elle détruit tout ce que nous avons créé à l'initialisation.

* Notez également que la référence à la classe QgsInterface est faite dans\  ``__init__()`` \. À partir de cet attribut de classe on peut créer des référence vers d'autres parties du système QGIS comme le canevas de la carte.

* Une autre chose importante est de noter que la fenêtre de dialogue est créée dans la méthode\  ``run()`` \avec les lignes suivantes::

    dlg = vector_selectbypointDialog()
    # show the dialog
    dlg.show()

* La classe\  ``vector_selectbypointDialog()`` \qui est instanciée dans la dernière partie du code a été importée à partir de notre module Python de boîte de dialogue. Si on ouvre ce module Python on peut voir qu'il référence le module Python qui a été compilé à partir de notre fichier\  ``.ui`` \ --\  ``ui_vector_selectbypoint.py`` \. Au début du fichier on a::

    from vector_selectbypointdialog import vector_selectbypointDialog

* L'exécution de la méthode\  ``run()`` \est insuite stoppée. Elle attend une entrée utiliateur pour avancer. Cet entrée utilisateur (dans ce cas) est un clic sur un bouton. Le reste du code dans la méthode\  ``run()`` \détermine ensuite quel bouton a été cliqué.\  ``Cancel == 0 and OK == 1`` \. Qand nous commençons à écrire des plugins on écrit généralement du code dans la méthode\  ``run()`` \, mais nous verrons qu'il n'est pas nécessaire de le mettre à cet endroit par la suite::

    result = dlg.exec_()
    # See if OK was pressed
    if result == 1:
        # do something useful (delete the line containing pass and
        # substitute with your code
        pass 


\  **4.** \Maintenant nous allons commencer à programmer. Notre outil va avoir besoin d'une référence au canvas de la carte. Il va aussi avoir besoin d'une référence à un outil de clic. Modifiez la fonction\  ``__init__()`` \pour la faire ressembler à::

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # a reference to our map canvas 
        self.canvas = self.iface.mapCanvas() #CHANGE
        # this QGIS tool emits as QgsPoint after each click on the map canvas
        self.clickTool = QgsMapToolEmitPoint(self.canvas)

\  **5.** \Habituellement en travaillant avec des éléments du GUI QGIS, nous devrons importer les classes et les fonctions du module\  ``qgis.gui`` \. La classe\  ``QgsMapToolEmitPoint`` \que nous utilisons pour construire notre outil de pointage est dans ce module. En haut de notre module\  ``vector_selectbypoint.py`` \ajoutez cet instruction d'import sous les autres imports de qgis::

    from qgis.gui import *

\  **6.** \Nous avons toutes les références dont nous allons avoir besoin pour implémenter le clic et récupérer un retour sous la forme d'un\  ``QgsPoint`` \, mais nous devons réfléchir à comment tout cela fonctionne. Dans QGIS (comme dans les autres applications), il y a un concept d'évènement/action. Dans Qt nous appelons celà avec les termes de *signal* et *slot*. Quand un utilisateur clique sur la carte, il diffuse un signal sur ce qui vient de se passer. D'autres fonctions dans votre programme peuvent s'enregistrer à cette diffusion et réagir en temps réel à un clic. C'est un mécanisme qui n'est pas immédiatement intuitif ni facile à programmer au départ. Le meilleur conseil est de suivre pour le moment l'exemple suivant et de tenter d'en comprendre le plus possible. Nous reviendrons sur ce sujet plus tard pour l'approfondir. Pour plus de détail une très bonne référence est\  `PyQt signals and slots <http://www.commandprompt.com/community/pyqt/c1267>`_ \.


\  **7.** \Pour terminer ces dernières étapes, nous allons avoir besoin de deux choses -- 1) un moyen d'enregistrer une fonction spécifique à l'évènement de clic sur la carte et 2) une fonction spécifique qui est appelée lorsqu'un clic de souris survient sur le canvas de la carte. Le meilleur endroit pour mettre le code qui s'enregistre au signal de clic souris est dans la fonction\  ``initGui()`` \. Ajouteez cette ligne de code à la toute fin de la fonction\  ``initGui()`` \::

    result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
    QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

Une note rapide. La fonction\  ``QObject.connect()`` \fait le travail d'enregistrer notre fonction spécifique\  ``handleMouseDown`` \(Qui n'a pas encore été écrite) au signal de clickTool nommé\  ``canvasClicked()`` \. Cette fonction retourne une valeur booléenne informant si la connexion a fonctionné ou pas. Nous récupérons la réponse et l'affichons dans une boîte de message pour être sur que le code que nous écrivons fonctionne correctement.


\  **8.** \Écrivons ensuite notre fonction spécifique qui sera appellée lorsqu'un évènement de clic souris survient sur le canvas de la carte. Créez cette fonction n'importe où en dessous de\  ``initGui()`` \.::

    def handleMouseDown(self, point, button):
            QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

Nous savons que le signal\  ``canvasClicked()`` \émet un QgsPoint. Dans notre fonction\  ``handleMouseDown()`` \nous utilisons une boîte de message pour visualiser les composants X,Y de ce point.


\  **9.** \Finalement, nous devons nous assurer que l'outil de clic que nous initialisons dans\  ``__init__()`` \est activé quand notre outil tourne. Ajoutez ce code au tout début de la fonction\  ``run()`` \::

    # make our clickTool the tool that we'll use for now 
    self.canvas.setMapTool(self.clickTool)

\  **10.** \Votre module entier\  ``vector_selectbypoint.py`` \devrait être maintenant\  `similaire à ce module <../_static/mapcanvas_click_2.py>`_


Tester le plugin modifié
************************

\  **1.** \Retournez dans QGIS et assurez vous que toutes les couches sont supprimées sauf la couche des contours administratifs de pays::

    /home/formation/natural_earth_50m/cultural/50m_cultural/50m_admin_0_countries.shp

\  **2.** \Ouvrez le gestionnaire d'extensions de QGIS. Si notre plugin\  ``Select_VectorFeatures_By_PointClick`` \est déjà sélectionner, alors désélectionnez le, et fermez le gestionnaire d'extension. Maintenant réouvrez le gestionnaire d'extension et réactivez notre plugin en le cochant pour l'ajouter à QGIS. Ce processus assure que la dernière version du plugin soit bien chargée.

\  **3.** \Vous devriez remarquer que dès que vous sélectionnez 'OK' dans le gestionnaire d'extensions, mais avant que le plugin n'apparaisse dans la barre de menu, des choses se passent : vous avez soit une erreur, soit un message d'information\  ``connect = True`` \:

.. image:: ../_static/connect_equals_true.png
    :scale: 100%
    :align: center

Si vous avez une erreur, faites de votre mieux pour la localiser, éditez la, et réajouter le plugin pour le tester. Si vous ne trouvez pas l'erreur posez des questions.

\  **4.** \Cliquez maintenant sur le bouton de plugin dans la barre de menu:

.. image:: ../_static/click_vector_selectbypoint_tool.png
    :scale: 100%
    :align: center


\  **5.** \Vous devriez remarquer deux choses ici. Notre formulaire apparait avec le nouveau look. On remarque aussi que lorsque la souris survole le canvas de la carte, le pointeur change. Cliquez quelque part sur la carte et vous devriez avoir une seconde boîte de message avec les coordonnées X,Y:

.. image:: ../_static/point_feedback.png
    :scale: 70%
    :align: center

Si vous avez une erreur, faites de votre mieux pour la localiser, éditez la, et réajouter le plugin pour le tester. Si vous ne trouvez pas l'erreur posez des questions.


Relier la sortie de QgsPoint au GUI
-**********************************

\  **1.** \Ouvrez le fichier\  ``vector_selectbypointdialog.py`` \.::

    from PyQt4 import QtCore, QtGui
    from ui_vector_selectbypoint import Ui_vector_selectbypoint
    # create the dialog for zoom to point
    class vector_selectbypointDialog(QtGui.QDialog):

        def __init__(self):
            QtGui.QDialog.__init__(self)
            # Set up the user interface from Designer.
            self.ui = Ui_vector_selectbypoint()
            self.ui.setupUi(self)

Quelques remarques à propos de ce fichier:            

    * Ce module Python dérive une classe QtGui.QDialog et inclus le fichier compilé\  ``ui_vector_selectbypoint.py`` \ à partir de notre\ ``.ui`` \. Notez qu'on importe ce module au début avec la ligne\  ``from ui_vector_selectbypoint import Ui_vector_selectbypoint`` \.

    * L'intérêt de cette classe est d'abstraire l'initialisation de l'interface de telle sorte qu'on ait pas à la gérer dans le module Python principal. Maintenant lorsque nous voulons créer notre fenêtre il suffit de créer une instance de la classe\  ``vector_selectbypointDialog`` \et cela prend en charge tout le paramétrage de l'interface.

    * Cette classe est un bon endroit pour ajouter des propriétés spécifiques à la fenêtre, comme des accesseurs pour les entrées/sorties et des choses qui vont interagir avec les boutons.

\  **2.** \Ajoutez des propriétés pour fixer l'entrée du TextBrowser. Cela va remplacer notre QMessageBox générique pour la sortie de notre QgsPoint. Créez les fonctions nécessaires pour que\  ``ui_vector_selectbypoint.py`` \ressemble à ce qui suit. Souvenez vous que \  ``txtFeedback`` \était le\  ``objectName`` \que l'on a donné à l'objet TextBrowser dans Qt Designer::

    from PyQt4 import QtCore, QtGui
    from ui_vector_selectbypoint import Ui_vector_selectbypoint
    # create the dialog for zoom to point
    class vector_selectbypointDialog(QtGui.QDialog):

        def __init__(self):
            QtGui.QDialog.__init__(self)
            # Set up the user interface from Designer.
            self.ui = Ui_vector_selectbypoint()
            self.ui.setupUi(self)

        def setTextBrowser(self, output):
            self.ui.txtFeedback.setText(output)
         
        def clearTextBrowser(self):
            self.ui.txtFeedback.clear()


\  **3.** \Ouvrez maintenant et commentez la création de la boîte de message\  ``vector_selectbypoint.py`` \::

    #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

\  **4.** \Dans\  ``vector_selectbypoint.py`` \également nous voulons bouger la création de notre objet dialog pour l'enlever de\  ``run()`` \et le mettre dans la fonction\  ``__init__`` \pour qu'il soit accessible de l'ensemble des fonctions de la classe::

    # create our GUI dialog
    self.dlg = vector_selectbypointDialog()

\  **5.** \Maintenant que la variable\  ``dlg`` \est une variable d'instance de classe en Python nous devons vérifier que toutes les références qui y sont faites doivent inclure\  ``self.`` \. Changez donc toutes les références à\  ``dlg`` \dans la fonction\  ``run()`` \::

    # show the dialog
    self.dlg.show()
    result = self.dlg.exec_()

\  **6.** \Enfin, redirigeons la sortie de notre QgsPoint vers le TextBrowser avec notre propriété. Avant de régler la nouvelle valeur du TextBrowser, on vide la valeur précédente. Dans la fonction\  ``handleMouseDown`` \réécrivez le code ainsi::

    def handleMouseDown(self, point, button):
            self.dlg.clearTextBrowser()
            self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
            #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

\  **7.** \Notre code devrait maintenant ressembler \  `à ceci <../_static/mapcanvas_click_3.py>`_

\  **8.** \Enregistrez les changements. Fermez les fichiers. Rechargez le plugin en utilisant le gestionnaire d'extension. Vous devriez maintenant voir le résultat du QgsPoint dans le TextBrowser à chaque clic:

.. image:: ../_static/qgspoint_to_gui.png
    :scale: 100%
    :align: center


\3) Implémentation de la sélection de Feature au clic
-----------------------------------------------------

Le but désormais va être de sélectionner la feature qu'on a cliqué sur la carte. Il y a un certain nombre de choses que nous avons besoin d'implémenter dans la section suivante:

    1. Nous avons besoin d'un moyen de connecter la fonction spécifique qui va faire la sélection à notre évènement de clic
    2. Nous avons besoin d'écrire une fonction spécifique qui fait le travail de sélection

\  **1.** \Pour commencer, écrivez une nouvelle connexion au signal\  ``canvasClicked()`` \. Nous allons créer notre propre fonction de sélection\  ``selectFeature()`` \à la prochaine étape. Au cas où vous auriez oublié, cette connexion est implémentée exactement de la même manière que pour la fonction\  ``handleMouseDown()`` \ dans la section précédente. Mettez ce code à la fin de la fonction\  ``initGui()`` \::

        # connect our select function to the canvasClicked signal
        result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
        QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )
 
Remarquez que nous mettons un QMessageBox immédiatement après la connexion pour être sur que nous avons un retour correct pendant les tests.        

\  **2.** \Maintenant écrivez la fonction spécifique pour sélectionnez les features. Pour comprendre ce que le code suivant effectue, lisez les commentaires. Tout ce qui est ans la fonction a déjà été vu dans les parties précédentes. Reprenez les explications si cela ne vous semble pas clair ou posez des questions::

     def selectFeature(self, point, button):
            QMessageBox.information( self.iface.mainWindow(),"Info", "in selectFeature function" )
            # setup the provider select to filter results based on a rectangle
            pntGeom = QgsGeometry.fromPoint(point)  
            # scale-dependent buffer of 2 pixels-worth of map units
            pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0) 
            rect = pntBuff.boundingBox()
            # get currentLayer and dataProvider
            cLayer = self.canvas.currentLayer()
            selectList = []
            if cLayer:
                    provider = cLayer.dataProvider()
                    feat = QgsFeature()
                    # create the select statement
                    provider.select([],rect) # the arguments mean no attributes returned, and do a bbox filter with our buffered rectangle to limit the amount of features  
                    while provider.nextFeature(feat):
                            # if the feat geom returned from the selection intersects our point then put it in a list
                            if feat.geometry().intersects(pntGeom):
                                    selectList.append(feat.id())

                    # make the actual selection     
                    cLayer.setSelectedFeatures(selectList)
            else:
                    QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )

\  **3.** \Le code Python complet devrait maintenant ressembler à \  `ceci <../_static/featureselect_1.py>`_

\  **4.** \Sauver vos modifications et fermez les fichiers. Rechargez le plugin et testez le. Vous devriez voir au moins deux boîtes de dialogue -- une après le chargement du plugin qui affiche le test de la connexion au signal, et un second après avoir cliqué sur le canvas de la carte. Le second message nous dit que nous sommes dans la fonction\  ``selectFeature`` \. Le code que nous avons écrit après ce message va soit s'exécuter jusqu'au bout soit échouer:

.. image:: ../_static/in_selectfeature.png
    :scale: 100%
    :align: center


\4) Implémentation de l'activation de l'outil par CheckBox
----------------------------------------------------------

Il est temps de faire en sorte que notre outil soit activable/désactivable selon l'état de notre case à cocher en bas à gauche. Il nous manque deux étapes pour cette implémentation:

1.  Nous avons besoin de faire une connexion vers un signal de la case à cocher lorsqu'elle est cliquée. La fonction appelée va vérifier l'état (coché ou non coché) de la case à cocher.

2.  Nous avons besoin de créer la fonction de gestion qui vérifie l'état de la case à cocher et qui active ou désactive en fonction une connexion au signal de clic sur le canvas de la carte. Cela veut dire que nous allons devoir modifier notre code. 

\  **1.** \Ajoutez une connexion pour le signal\  ``stateChanged()`` \de la case à cocher, à la fin de\  ``initGui()`` \. Le nom de la fonction qui va s'activer sur cet évènement est\  ``changeActive()`` \. Nous créerons la fonction par la suite::

    QObject.connect(self.dlg.ui.chkActivate,SIGNAL("stateChanged(int)"),self.changeActive)

\  **2.** \Tant que nous sommes dans la fonction\  ``initGui()`` \nous allons commenter notre code précédent pour connecter la fonction\  ``handleMouseDown`` \et la fonction\  ``selectFeature``\. Ces actions vont être déplacées dans notre fonction de gestion de la case à cocher::

    # connect our custom function to a clickTool signal that the canvas was clicked
    #result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
    #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    # connect our select function to the canvasClicked signal
    #result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
    #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )


\  **3.** \Nous créons maintenant une fonction spécifique qui s'active chaque fois que la case à cocher change d'état de coché vers décoché ou vice-versa. L'idée est que si la case est cochée (activée), on connecte\  ``handleMouseDown`` \et\  ``selectFeature`` \au signal de clic sur le canvas de la carte. Si elle est décochée alors on déconnecte du signal de clic::

   def changeActive(self,state):
        if (state==Qt.Checked):
                # connect to click signal
                QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
                # connect our select function to the canvasClicked signal
                QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
        else:
                # disconnect from click signal
                QObject.disconnect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
                # disconnect our select function to the canvasClicked signal
                QObject.disconnect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)

\  **4.** \Votre code devrait être similaire à\  `ce code <../_static/activate_click_1.py>`_

\  **5.** \Sauvez et fermez vos modules Python. Rechargez le plugin.

\  **6.** \Après avoir chargé le plugin, la case à cocher d'activation devrait être décochée. Souvenez-vous, cela signifie que vous ne devriez pas être capable de sélectionner de feature, ni d'avoir de sortie vers le TextBrowser.

.. image:: ../_static/plugin_tut_notactive.png
    :scale: 100%
    :align: center

\  **8.** \Cliquez alors sur la case à cocher et essayer de cliquer sur la carte de nouveau. Nous devrions avoir le résultat du point X,Y dans le TextBrowser et voir les features sélectionnées sur la carte.

.. image:: ../_static/plugin_tut_active.png
    :scale: 100%
    :align: center

--------------------------------

\5)  Améliorer notre plugin
-------------------------------------

Vous avez pu remarquer quelques petits détails intéressants qui se passent dans le module\  ``vector_selectbypoint.py`` \, que je trouve pénible. Examinons les changements et modifions ensuite le code dans les étapes suivantes:

    \  **1.** \Chaque fois que l'on clique sur le canvas de la carte, un signal est émis, et notre slot (ou fonction appelée)\  ``selectFeature()`` \s'exécute et fait un certain nombre de choses avant de sélectionner une feature:
        * récupérer la couche courante et régler une variable dans la fonction locale
        * Récupérer le data provider de la couche courante et régler une variable dans la fonction locale  

    **SOLUTION** \:Cela ne semble pas être l'endroit le plus intuitif pour récupérer la couche courante et son data provider. Réorganisons les choses pour faire plus simple. Lorsqu'une couche est sélectionnée, la liste des couche émet un signal. Cela semble un bon endroit pour y mettre le code d'initialisation pour la couche courante ou le data provider puisque nous ne nous servons que d'une seule couche à la fois.

    \  **2.** \Donner les coordonnées X,Y au clic n'est pas d'un très grand intérêt.

    **SOLUTION** \:Mettons quelque chose de plus intéressant dans le TextBrowser. Nous allons mettre l'attribut Name dans le TextBrowser s'il existe pour une couche donnée.

------------------------------

La plupart de ces changements sont de la réorganisation du code.

\  **1.** \Premièrement, travaillons sur nos variables de classes. Ce sont celles qui sont définies dans\  ``__init__()`` \. Nous voulons être sur que chaque fois qu'une sélection est faite nous avons une variable de classe pour contenir:

    * La liste des features sélectionnées
    * La couche courante
    * Le data provider de la couche courante

La raison pour laquelle nous voulons utiliser des variables de classe plutôt que des variables de fonction est que nous voulons que TOUTES nos fonctions puissent y accéder et prendre des décisions basées sur leurs valeurs. Présentement toutes ces variables sont réglées dans la fonction\  ``selectFeature()`` \. Cela signifie que nous allons devoir déplacer la variable\  ``selectList`` \hors de la fonction\  ``selectFeature()`` \et la mettre dans\  ``__init__()`` \ ainsi que les variables \  ``cLayer`` \et\  ``provider`` \. Faites donc en sorte que votre fonction\  ``__init__()`` \ressemble à ceci :

::
	
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # refernce to map canvas
        self.canvas = self.iface.mapCanvas() 
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # create our GUI dialog
        self.dlg = vector_selectbypointDialog()
        # create a list to hold our selected feature ids 
        self.selectList = []
        # current layer ref (set in handleLayerChange)
        self.cLayer = None
        # current layer dataProvider ref (set in handleLayerChange)
        self.provider = None 

\  **2.** \Maintenant changez toutes les références dans le module (la plupart dans la fonction\  ``selectFeature()``  \) pour être préfixées par\  ``self.`` \. 


\  **3.** \Ensuite créons une fonction nommée\  ``updateTextBrowser()`` \qui va remplacer la fonction\  ``handleMouseDown()`` \qui met à jour le TextBrowser avec les coordonnées du point. Voici à quoi cette fonction va ressembler. Lisez les commentaires qui expliquent le code::

    def updateTextBrowser(self):
        # if we have a selected feature
        if self.selectList:
            # find the index of the 'NAME' column, branch if has one or not
            nIndx = self.provider.fieldNameIndex('NAME')
            # get our selected feature from the provider, but we have to pass in an empty feature and the column index we want
            sFeat = QgsFeature()
            if self.provider.featureAtId(self.selectList[0], sFeat, True, [nIndx]):
                # only if we have a 'NAME' column
                if nIndx != -1:
                    # get the feature attributeMap
                    attMap = sFeat.attributeMap()
                    # clear old TextBrowser values 
                    self.dlg.clearTextBrowser()
                    # now update the TextBrowser with attributeMap[nameColumnIndex] 
                    # when we first retrieve the value of 'NAME' it comes as a QString so we have to cast it to a Python string
                    self.dlg.setTextBrowser( str( attMap[nIndx].toString() ))


\  **4.** \Nous avons besoin d'appeler d'une manière ou d'une autre notre fonction\  ``updateTextBrowser()`` \. Nous pourrions créer une autre connexion de signal, mais nous voulons nous assurer d'un ordre séquentiel des évènements ici -- c'est à dire que nous voulons mettre à jour le TextBrowser uniquement après que la fonction\  ``selectFeature()`` \a été exécutée. Pour faire cela nous allons appeler\  ``updateTextBrowser()`` \à la toute fin de la fonction \ ``selectFeature()`` \en changeant quelques lignes ainsi::

    if self.selectList:
            # make the actual selection 
            self.cLayer.setSelectedFeatures(self.selectList)
            # update the TextBrowser
            self.updateTextBrowser()  

Voici la fonction complète\  ``selectFeature()`` \pour voir le code ci-dessus dans le contexte::

    def selectFeature(self, point, button):
        # reset selection list on each new selection
        self.selectList = []
        #QMessageBox.information( self.iface.mainWindow(),"Info", "in selectFeature function" )
        # setup the provider select to filter results based on a rectangle
        pntGeom = QgsGeometry.fromPoint(point)  
        # scale-dependent buffer of 2 pixels-worth of map units
        pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0) 
        rect = pntBuff.boundingBox()
        if self.cLayer:
            feat = QgsFeature()
            # create the select statement
            self.provider.select([],rect) # the arguments mean no attributes returned, and do a bbox filter with our buffered rectangle to limit the amount of features 
            while self.provider.nextFeature(feat):
                # if the feat geom returned from the selection intersects our point then put it in a list
                if feat.geometry().intersects(pntGeom):
                    self.selectList.append(feat.id())

            if self.selectList:
                # make the actual selection 
                self.cLayer.setSelectedFeatures(self.selectList)
                # update the TextBrowser
                self.updateTextBrowser()
        else:   
                QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )
    
\  **6.** \Comme précaution supplémentaire, nous allons écrire deux lignes dans la fonction\  ``run()`` \qui vont régler la couche courante et le data provider lorsque le plugin est ouvert la première fois. La plupart des gens vont avoir les layers déjà chargé avant d'ouvrir le plugin. Comme notre couche courante et notre data provider sont réglés automatiqumeent quand une couche différente est sélectionnée dans la liste des couches, nous n'avons pas de valeur initiale. Désormais la fonction\  ``run()`` \ressemblera à ceci :

::
	
    # run method that performs all the real work
    def run(self):
        # set the current layer immediately if it exists, otherwise it will be set on user selection
        self.cLayer = self.iface.mapCanvas().currentLayer()
        if self.cLayer: self.provider = cLayer.dataProvider()
        # make our clickTool the tool that we'll use for now 
        self.canvas.setMapTool(self.clickTool) 

        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass

\  **7.** \Nous avons besoin de créer une connexion à un signal qui diffuse lorsque la couche change. À la fin de\  ``initGui()`` \on ajoute ce code qui connecte une fonction spécifique que nous allons créer, au signal\  ``currentLayerchanged()`` \de QgisInterface::

        # connect to the currentLayerChanged signal of QgsInterface
        result = QObject.connect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer *)"), self.handleLayerChange)
        # QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

\  **8.** \Notre fonction spécifique pour gérer le changement de couche ressemblera à ceci :

::
	
    def handleLayerChange(self, layer):
            self.cLayer = self.canvas.currentLayer()        
            if self.cLayer:
                self.provider = self.cLayer.dataProvider()

\  **9.** \L'ensemble du code devrait maintenant ressembler à\  `ce module <../_static/vector_selectbypoint(2nd_hour_ex_1).py>`_ \

\  **10.** \Tester l'ensemble de nos changements. Un bon test est de charger deux couches de shapefile (qui auront toutes deux un champs 'NAME'). Ensuite de tester de passer d'une couche à l'autre et de cliquer sur différentes featur pour vérifier que l'outil fonctionne et qu'il ne plante pas.
 
