===========================
Exercice
===========================

Afficher dans un TextBrowser les attributs d'une couche vecteur
---------------------------------------------------------------

À partir du plugin\  ``foss4g2011_example1_starter`` \vous allez modifier une fonction. Dans cette fonction vous pourrez écrire la logique qui lit les attributs d'une couche de données vecteur et qui les affiche dans un TextBrowser.

Objectif
*************************

\  **1.** \Ouvrez le plugin\  ``foss4g2011_example1_starter`` \avec une couche vecteur chargée dans QGIS

.. image:: ../_static/ex1_openplugin.png
    :scale: 100%
    :align: center

\  **2.** \Cliquer quelque part sur la carte et vous verrez une sortie générique dans le TextBrowser

.. image:: ../_static/ex1_exoutput.png
    :scale: 100%
    :align: center

\  **3.** \En utilisant gedit, aller à \  ``/home/formation/.qgis/python/plugins/foss4g2011_example1_starter/`` \et ouvrir le module\  ``foss4g2011_example1_starter.py`` . Trouver la fonction\  ``updateTextBrowser()`` \. C'est le code que vous allez changer:: 

    def updateTextBrowser(self):
        # vérification pour être sur que nous avons une feature sélectionnée dans notre selectList -- il peut y en avoir plus d'une
        if self.selectList:

            # ***************EXAMPLE 1 EDITER ICI********************
            ''' Ecrire du code qui affiche dans le TextBrowser tous les attributs pour une unique feature selectionnee
                plutôt que d'utiliser la fonction dataProvider.select(), récupérer la vraie QgsFeature en utilisant dataProvider.featureAtId() '''
     
            self.dlg.setTextBrowser("Exemple de sortie texte\n dans le TextBrowser")

Essayez de développer cette fonction par vous même. Si vous n'y arrivez pas, vous pouvez utiliser les conseils ou la solution.

Conseils
***************

Dans cette partie nous avons vu des exemples utilisant \  ``dataProvider.select()`` \et\  ``dataProvider.featureAtId()`` \. Utilisez le code ci-dessous comme guide pour écrire votre fonction::

        if self.selectList:

            # ############ EXAMPLE 1 EDITER ICI ####################  
            ''' Ecrire du code qui affiche dans le TextBrowser tous les attributs pour une unique feature selectionnee
                plutôt que d'utiliser la fonction dataProvider.select(), récupérer la vraie QgsFeature en utilisant dataProvider.featureAtId() '''
            # Obtenir tous les indices des champs pour la feature
            fields = self.provider.fields()
            # Obtenir la feature en passant une feature vide
            feat = QgsFeature()
            # On prend la premiere feature car il peut y en avoir plus d'une
            if self.provider.featureAtId(self.selectList[0], feat, True, fields.keys()):
                attMap = feat.attributeMap()
                output = "FEATURE ID: %i\n" % feat.id()
                for index,qgsfield in fields.items():
                    output += "\t" + str(qgsfield.name()) + " : " + str( (attMap[index]).toString() ) + "\n" 
                self.dlg.setTextBrowser(output)


Solution
************

Il y a un plugin solution pour cet outil. Ouvrez ce plugin et utilisez le ou regardez le code source dans\  ``/home/formation/.qgis/python/plugins/foss4g2011_example1_solution/foss4g2011_example1_solution.py``\pour vous aider:

.. image:: ../_static/ex1_solutionset.png
    :scale: 100%
    :align: center


