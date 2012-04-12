.. plugins gérés par évènements (Partie 3)

========================================================
Créer des plugins QGIS avec les évènements
========================================================

Concepts d'évènements dans QGIS
-------------------------------

La conception orientée évènements dans la bibliothèque Qt utilise les notions de *signal* et *slot*. Comme mentionné dans la partie 2, quelques bonne ressources pour aller plus loin sur les signaux et les slots sont\  `ce tutoriel PyQt <http://www.commandprompt.com/community/pyqt/c1267>`_ \et la\  `documentation officielle de Qt <http://doc.qt.nokia.com/4.7/signalsandslots.html>`_\. Nous allons présenter ici les points principaux.

SIGNAL
********

Les objets Qt (tous ce qui hérite de QObject) a la possibilité d'émettre des signaux. L'objet émet un signal quand il veut diffuser un évènement d'importance. Par exemple, les concepteurs de la classe\  ``QgsMapCanvas`` \considèrent qu'il est important pour un objet de type canvas de carte de diffuser un QgsPoint quand la souris le survole. Le signal\  `xyCoordinates <http://doc.qgis.org/head/classQgsMapCanvas.html#bf90fbd211ea419ded7c934fd289f0ab>`_ \ définit la diffusion. La signature de la fonction de signal\  ``xyCoordintes`` \est la suivante::

    void QgsMapCanvas::xyCoordinates    (   const QgsPoint &    p    )

On utilise cette signature pour définir comment d'autres objets vont se connecter et interagir avec cet objet (comme nous verrons dans la prochaine section).

Dans PyQt on peut émettre un signal existant en utilisant une référence à l'objet qui émet normalement ce signal. Par exemple ci dessous on a une référence à l'objet mapCanvas, et on peut émettre un signal\  ``xyCoordinates`` \::

    self.iface.mapCanvas().emit(SIGNAL("xyCoordinates(const QgsPoint &)"), QgsPoint(-122,45))

SLOT
*******

Les *slots* sont les récepteurs de l'information des *signal*. On connecte les slots aux signaux en utilisant la fonction\  `QObject.connect() function <http://doc.qt.nokia.com/4.7/qobject.html#connect>`_ \. Les arguments de cette fonction sont::

    - Sender -- L'object Qobject responsable de l'émission du signal
    - Signal -- La signature de la fonction de signal passé comme une chaine à la macro SIGNAL()
    - Receiver -- La fonction qui va attraper le signal et effectuer une action avec
    - Type -- Le type de connexion (peut être ignoré dans nos cas d'utilisation)

Si j'avais une fonction nommée\  ``listen_xyCoordinates`` \et que je veux qu'elle reçoive de l'information à partir du signal\  ``xyCoordinates`` \quand il se déclenche, je peux établir une connexion ainsi::

    # notice that we are only passing the first three arguments here (sender, signal receiver)
    QObject.connect(self.iface.mapCanvas(), SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xyCoordinates)

La fonction slot qui se connecte à un signal doit accepter les mêmes arguments que la signature de la fonction du signal. Dans le cas du signal\  ``xyCoordinates`` \cela signifie que notre fonction spécifique doit accepter un QgsPoint. Voici cette fonction::

    def listen_xyCoordinates(self,point):
        self.dlg.outputTextEdit.append("xyCoordinates - %d,%d" % (point.x() if point else "",point.y() if point else ""))


Créer des signaux particuliers
********************************

Même si cela apporte un peu de confusion, les développeurs ont la possibilité de créer leurs propres signaux. Ci dessous se trouve un exemple de comment créer un signal spécifique et y connecter un slot. L'exemple est tiré du plugin\  ``foss4g2011_example3_solution`` \:


\  **1.** \Assurez vous que votre classe de plugin dérive de QObject. Elle doit aussi appeler le constructeur de QObject dans la méthode\  ``__init__`` \comme ci dessous::

    class foss4g2011_example3_solution(QObject):

        def __init__(self, iface):
            QObject.__init__(self)
            # Save reference to the QGIS interface
            self.iface = iface

\  **2.** \Créez un slot qui va recevoir ce signal. Notez qu'il accepte un paramètre\  ``message`` \qui n'était pas défini dans le signal (intéressant)::

     def listen_feedbackStatus(self, message):
            self.dlg.outputTextEdit.append("feedbackStatus - %s" % (message if message else ""))

\  **3.** \Connectez votre slot au signal quelque part dans le code::

    QObject.connect(self, SIGNAL("feedbackStatus(PyQt_PyObject)"), self.listen_feedbackStatus) 

\  **4.** \Désormais n'importe où dans votre plugin (il dérive de QObject) vous pouvez émettre ce signal si vous pensez qu'il est important et passer un message à votre slot. Le plugin\  ``foss4g2011_example3_solution`` \effectue ceci lors d'un clic sur un bouton::

     def btn_emitFeedbackStatus(self, checked):
           self.emit(SIGNAL("feedbackStatus(PyQt_PyObject)"), "Bruce Lee is my hero!")


Exemple #3
************************
Dans l'exercice suivant vous pouvez installer l'exemple #3 de plugin basique comme base. Ce plugin est prévu pour être un test de signal/slot. Il fournit une zone de texte simple pour que les fonctions y écrivent, et une boîte à outil à droite du plugin vous permettra d'écouter un signal ou d'envoyer un signal.

Nous avons fourni quelques exemples de widgets GUI (case à cocher et boutons) pour vous permettre de vous connecter dynamiquement à quelques signaux ou pour générer des signaux de test. Le but sera pour vous de regarder le code et comprendre comment cela est fait (à la fois en regardant le GUI dans le designer et les connexions signal/slot). Une fois que vous comprenez comment cela est fait, nous pouvons tenter de nous connecter à d'autres signaux. Dans l'exemple #3 basique, nous avons fourni quelques signaux d'exemple sur lesquels se connecter dans le code commenté. Nous avons aussi ajouté des éléments de GUI dans le designer qui sont désactivés.

Ouvrez Qt Desiger et trouver comment "activer" la case à cocher pour le signal que vous voulez écouter (Astuce : il y en a deux qui sont désactivés). Une fois que vous avez les éléments du GUI activés, sauvez le fichier .ui et lancez le make dans le répertoire des plugins. Cela va recompiler le fichier .ui en un fichier .py. Ouvrez QGIS et vérifiez que le plugin a maintenant ces éléments de GUI activés. Maintenant, revenez dans le code principal du plugin et trouvez le code commenté pour les signaux que vous avez activé dans l'interface... Et essayez de les activer en décommentant le code.

Pour ceux qui cherchent de l'aventure, trouvez un signal dans la documentation QGIS que vous voulez écouter, ajouter un élément d'interface au plugin (une case à cocher ou un élément similaire à ceux déjà implémentés), et finalement ajoutez la connexion du signal avec une fonction spécifique qui écrit dans la zone de texte.


