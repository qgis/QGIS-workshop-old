==============================================
Création de formulaires spécialisés
==============================================

Une possibilité intéressante de personnaliser QGIS est de créer des formulaires personnalisés pour les données. QGIS intègre un mécanisme qui rend la création de tels formulaires relativement simples.

Nous pouvons aller un peu plus loin avec ce mécanisme en y ajoutant des actions de validation de données par exemple.

Création du formulaire spécialisé
---------------------------------

Nous allons utiliser ici Qt Designer. On lance donc cet outil et on sélectionne "Dialog with Buttons Bottom". On crée la boîte de dialogue.

Nous prendrons comme exemple le fichier *50m_admin_0_countries* qui a notamment les champs suivants:

- ADM0_A3
- NAME
- SOVISO
- TYPE
- PEOPLE
- GDP_USDM
- COMMENT

Nous allons créer un formulaire qui prenne en compte tout d'abord l'identifiant unique **ADM0_A3** et le champ **NAME** pour les présenter et permettre de les éditer plus simplement.

Ajoutons quelques labels et éditeurs de lignes correspondant à la donnée. Réglons maintenant notre formulaire pour utiliser un arrangement en grille (clic droit sur un espace vide -> Layout -> Layout in Grid).

L'astuce pour fabriquer un formulaire spécialisé pour QGIS est de donner aux objets du formulaire le même nom que les champs de la couche de données.

On clique droit sur chaque widget d'édition de texte et on change le **objectName**, en leur donnant le nom du champ correspondant de la couche concernée.

On enregistre le formulaire ( *.ui* ) dans notre espace de travail.
Dans QGIS, on ouvre la boîte de dialogue des propriétés de la couche. Dans l'onglet général on sélectionne pour "Éditer l'interface" notre fichier .ui précedemment sauvé.

On peut maintenant passer en mode édition et sélectionner un objet avec l'outil d'identification de feature.
Notre formulaire apparaît ! Nous sommes en mode édition donc tous les changement que l'on effectue dans le formulaire vont être répercutés dans le fichier. Si nous ne sommes pas en mode édition alors le formulaire apparait avec les widgets désactivés et juste un bouton "Annuler".

Validation et logique
---------------------

Création du module
^^^^^^^^^^^^^^^^^^

Créer un formulaire spécialisé est une première étape intéressante mais ajouter du code pour pouvoir faire de la validation serait encore plus intéressant.
Nous voulons ici ajouter une validation au champ NAME pour que l'utilisateur ne puisse pas ajouter de pays sans nom (avec un nom NULL).

On commence par sauver le projet QGIS. Le module Python que nous allons développer sera recherché dans le répertoire du projet. Ouvrons un éditeur de texte et entrons le code suivant::

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

    nameField = None
    myDialog = None

    def formOpen(dialog,layerid,featureid):
        global myDialog
        myDialog = dialog
        global nameField
        nameField = dialog.findChild(QLineEdit,"NAME")
        buttonBox = dialog.findChild(QDialogButtonBox,"buttonBox")

        # Deconnexion du signal que QGIS a automatiquement associe a la zone de boutons
        buttonBox.accepted.disconnect(myDialog.accept)

        # Branchement de nos propres signaux
        buttonBox.accepted.connect(validate)
        buttonBox.rejected.connect(myDialog.reject)

    def validate():
      # Assurons nous que le nom n'est pas vide
        if not nameField.text().length() > 0:
            msgBox = QMessageBox()
            msgBox.setText("Le champ NAME ne peut pas etre vide.")
            msgBox.exec_()
        else:
            # Retournons la boîte de dialogue a QGIS comme acceptee
            myDialog.accept()

Reprenons le code en détaillant les différentes étapes


Détail du module
^^^^^^^^^^^^^^^^

Tout d'abord nous importons les modules de Qt et réglons quelques variables globales qui vont contenir le nom du champ courant et la boîte de dialogue::

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

    nameField = None
    myDialog = None

Nous créons ensuite une méthode que QGIS va appeler quand il charge le formulaire. Cette méthode prend en argument une instance de notre formulaire personnalisé, l'identifiant de la couche, et l'identifiant de la feature::

    def formOpen(dialog,layerid,featureid):

Ensuite en utilisant la méthode *findChild* nous récupérons la référence au champ NAME et aux boutons (la buttonBox). Nous appelons aussi **buttonBox.accepted.disconnect()** pour déconnecter les slots que QGIS a automatiquement attaché à nos boutons, de façons à pouvoir y mettre notre propre logique de validation.

Après avoir déconnecté le signal de validation on peut brancher notre propre appel à la méthode de validation en utilisant **buttonBox.accepted.connect(validate)**\ ::

    global myDialog
    myDialog = dialog
    global nameField
    nameField = dialog.findChild(QLineEdit,"Name")
    buttonBox = dialog.findChild(QDialogButtonBox,"buttonBox")
    # Deconnexion du signal que QGIS a automatiquement associe a la zone de boutons
    buttonBox.accepted.disconnect(myDialog.accept)

    # Branchement de nos propres signaux
    buttonBox.accepted.connect(validate)
    buttonBox.rejected.connect(myDialog.reject)


Nous avons besoin d'une méthode pour valider la logique du formulaire. Celle ci sera appelée quand le signal **buttonBox.accepted()** est lancé. La logique de cette méthode de validation sera très simple. Si la boîte d'édition de texte a une longueur positive on accepte la validation, sinon on donne un message d'erreur à l'utilisateur pour qu'il corrige l'erreur::

    def validate():
      # Assurons nous que le nom n'est pas vide
        if not nameField.text().length() > 0:
            msgBox = QMessageBox()
            msgBox.setText("Name field can not be null.")
            msgBox.exec_()
        else:
            # Retournons la boîte de dialogue a QGIS comme acceptee
            myDialog.accept()


Configuration QGIS
^^^^^^^^^^^^^^^^^^

Maintenant que nous avons notre fonction de validation, il reste à dire à QGIS de l'utiliser. Sauvez le fichier dans le même répertoire que votre projet QGIS. QGIS va chercher notre module dans le répertoire du projet et dans les répertoires de Python, c'est à dire les répertoires par défaut et ceux définis dans le PYTHONPATH.

Dans l'onglet général des propriétés de la couche, on peut régler le champ de fonction d'initialisation. La syntaxe est *{nom du module}.{nom de la fonction}*. Dans notre cas le module (le fichier Python que l'on vient de créer) s'appelle **CountryForm** et la fonction est nommée **formOpen** donc on spécifie dans l'interface de QGIS **CountryForm.formOpen**.

On sauve et on utilise l'outil d'identification de feature pour en sélectionner une. Si tout est OK, vous ne devriez pas avoir d'erreur. Maintenant essayez de vider le champs NAME et appuyez sur OK. Un message d'erreur devrait apparaître.

L'édition des champs ne peut donc être validée que si le champ NAME n'est pas nul.

Aller plus loin
---------------

On peut au lieu d'afficher un message d'erreur rendre le textbox rouge si quelque chose n'est pas valide::

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

    nameField = None
    myDialog = None

    def formOpen(dialog,layerid,featureid):
      global myDialog
      myDialog = dialog
      global nameField
      nameField = dialog.findChild(QLineEdit,"NAME")
      buttonBox = dialog.findChild(QDialogButtonBox,"buttonBox")

      nameField.textChanged.connect(Name_onTextChanged)
      # Disconnect the signal that QGIS has wired up for the dialog to the button box.
      buttonBox.accepted.disconnect(myDialog.accept)
      # Wire up our own signals.
      buttonBox.accepted.connect(validate)
      buttonBox.rejected.connect(myDialog.reject)

    def validate():
      # Make sure that the name field isn't empty.
      if not nameField.text().length() > 0:
        nameField.setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        msgBox = QMessageBox()
        msgBox.setText("Name field can not be null.")
        msgBox.exec_()
      else:
      # Return the form as accpeted to QGIS.
        myDialog.accept()

    def Name_onTextChanged(text):
      if not nameField.text().length() > 0:
        nameField.setStyleSheet("background-color: rgba(255, 107, 107, 150);")
      else:
        nameField.setStyleSheet("")

Ici la partie importante est **nameField.textChanged.connect(Name_onTextChanged)** et la méthode **Name_onTextChanged(text)**.
Essayez, cela devrait fonctionner.

Exercice
--------

* Faites de même avec d'autres champs du fichier.
* Désactivez la possibilité d'éditer l'identifiant de la feature
* Prenez un champ date et validez que la date est postérieure à 1900
* Vérifiez que les champs SOVISO, SOV_A3 ont bien le bon nombre de lettres
* Faites en sorte que l'utilisateur ne puisse choisir qu'entre les 5 valeurs possibles du champ 'TYPE'
* Faites de même avec une de vos couches de données
* Créez une nouvelle couche de données avec des points référençant des noms de photos sur le disque, et affichez les dans le formulaire


