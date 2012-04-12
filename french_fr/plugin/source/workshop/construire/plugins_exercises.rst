=============================
Exercices
=============================

But : Lire les valeurs de raster à la volée
--------------------------------------------------------

Dans cet exercice vous construisez un plugin du début à la fin en utilisant le Plugin Builder. Le but est de créer un plugin simple (même rudimentaire) pour afficher les valeurs d'un raster. L'objectif est pour vous de déterminer les étapes de programmation à partir de quelques indications. Cet exercice a un mode \ **basique** \ et un mode \ **avancé** \.

Exercice basique
----------------------

Si vous ne vous sentez pas à l'aise avec le Plugin Builder pour créer un outil à partir de zéro, vous pouvez alors modifier un plugin déjà fait et tenter de le faire ressembler à la solution.

1. Ouvrez QGIS et chargez la couche de relief ombré \  ``/home/formation/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif``
2. Cliquez sur l'outil plugin appelé\  ``foss4g2011_example2_solution``\ou\  ``E#2SOL`` 
3. Balayez la carte avec le curser de la souris et regardez les valeurs RGB changer dynamiquement. C'est le résultat final qu'il faut obtenir.
4. Naviguer dans \  ``/home/formation/.qgis/python/plugins/foss4g2011_example2_starter/``
5. Ouvrir les fichiers \  ``foss4g2011_example2_starter.py`` \et\  ``foss4g2011_example2_starterdialog.py`` \et trouvez les zones avec du code commenté. Vous allez devoir décommentez le code de ces deux fichiers pour faire fonctionner l'outil comme la solution proposée.

Exercice avancé
-----------------------

The Tool Requirements
*************************

* Display every band value for a raster on mouse hover. That sounds confusing, but the idea is that your tool should work with a single grayscale raster or an RGBA raster without blowing up. There will be no mouse clicks, we'll just be responding to the normal mouse cursor movement over the map canvas

* Feedback of raster values will be output to a GUI (your choice on how to implement this on the GUI)

Conseils
***************

* Vous allez devoir connecter une fonction spécifique au signal de canvas de carte \  `xyCoordinates <http://doc.qgis.org/head/classQgsMapCanvas.html#bf90fbd211ea419ded7c934fd289f0ab>`_ \

* Vous pouvez obtenir les valeurs pour chaque bande d'un raster comme ceci::

    rLayer = self.iface.mapCanvas().currentLayer()
    success, data = rLayer.identify(QgsPoint(-122, 47))
    for band, value in data.items():
        print str(band) + " = " + str(value)

Solution
************

Si vous voulez tricher et regarder une des solutions possibles (mais une assez mauvaise) vous pouvez jeter un oeil à ces modules:

    * Le module Python principal\  `est ici <../_static/rastervaluedisplay.py>`_

    * Le module de dialogue principal \  `est là <../_static/rastervaluedisplaydialog.py>`_

    * Le module compilé de l'ui\  `par là <../_static/ui_rastervaluedisplay.py>`_

Pour avoir une idée de la simplicité de l'outil, voici une image:    

.. image:: ../_static/raster_value_final.png
    :scale: 100%
    :align: center

