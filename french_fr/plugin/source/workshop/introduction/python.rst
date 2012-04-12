======
Python
======

Python ?
--------

Python est un langage de programmation fun et puissant utilisé dans les applications web et les logiciels bureautiques. Il peut aussi être utilisé au travers des interfaces aux bibliothèques de l'OSGeo telles que GDAL/OGR, JTS et GEOS. Ses principales caractéristiques sont :

    * une syntaxe très claire et lisible
    * une approche objet intuitive
    * une gestion des erreurs basée sur les exceptions
    * des types de données dynamiques de très haut niveau
    * une implémentation dans de multiples langages (le cœur de Python est en C/C++ mais il existe aussi des implémentations Java (Jython), .Net (IronPython))

Importance et popularité
------------------------

* Pour nos besoins, Python peut être utilisé pour accéder à \  **des tonnes** \ de bibliothèques et logiciels de l'OSGeo. On utilise alors Python pour écrire des flux de programmations. Quelques un des logiciels de l'OSGeo incluent (non exhaustif):
    - QGIS (ou vous ne liriez pas ceci)
    - PostGIS
    - GDAL/OGR
    - GEOS
    - JTS
    - GeoTools
    - Proj4
    - Mapserver
    - gvSIG

* Python est nommé d'après “Monty Python’s Flying Circus”

* Python est simple à apprendre et est très puissant  

Exemples
-----------
Tous les exemples suivants sont executés dans l'interpréteur Python. Sur l'installation Virtual Box vous pouvez accéder à l'interpréteur Python de deux façons -- 1. Par QGIS et 2. Par le shell bash.

    1. La console Python de QGIS peut être démarrée en allant dans le menu fichier de QGIS et en cliquant sur\  ``Extensions --> Console Python`` \ 
    
    2. Le shell bash peut être démarré en appuyant sur les touches \  ``<Cntl>-<ALT>`` \ et en pressant \  ``t`` \ en même temps. Une fois qu'un nouveau shell bash est ouvert vous avez juste à taper \  ``python`` \ sur la ligne de commande et le shell devient magiquement un interpréteur Python.

Avec Python il est facile d'avoir de l'aide sur les fonctions et objets. Si une commande particulière vous pose problème, vous pouvez utiliser la commande help pour avoir sa signification (si elle en a une)::

    >>> help(range)
    Help on built-in function range in module __builtin__:

    range(...)
        range([start,] stop[, step]) -> list of integers
        
        Return a list containing an arithmetic progression of integers.
        range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
        When step is given, it specifies the increment (or decrement).
        For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
        These are exactly the valid indices for a list of 4 elements.


Strings, numbers, lists... beaucoup de mots clefs ! Le type Liste est le plus beau des types de données Python que vous devriez connaître. On peut utiliser des List pour stocker à peu près tout. Souvent les enregistrements d'une base de données sont représentés comme des List en Python:: 
    
    >>> # creer une liste
    ... a = [10, 50, 123, 1234]
    >>> # remplacer des elements:
    ... a[0:2] = [1, 12]
    >>> a
    [1, 12, 123, 1234]
    >>> # en enlever:
    ... a[0:2] = []
    >>> a
    [123, 1234]
    >>> # en ajouter:
    ... a[1:1] = ['bletch', 'xyzzy']
    >>> a
    [123, 'bletch', 'xyzzy', 1234]
    >>> # inserer une copie de la liste elle meme en debut
    >>> a[:0] = a
    >>> a
    [123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
    >>> # vider la liste : la remplacer par une liste vide
    >>> a[:] = []
    >>> a
    []


Un exemple d'utilisation de liste pour boucler sur les données et interpréter des chaines::

    >>> # Boucle for classique
    >>> for i in range(1,10): print i
    ... 
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> 
    >>> import string
    >>> # structure de boucle plus interessante
    >>> mess = [i for i in string.split("I love maps and I cannot lie"," ")]
    >>> mess
    ['I', 'love', 'maps', 'and', 'I', 'cannot', 'lie']
    >>> really_messy = [i for i in "I love maps and I cannot lie"]
    >>> really_messy
    ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'm', 'a', 'p', 's', ' ', 'a', 'n', 'd', ' ', 'I', ' ', 'c', 'a', 'n', 'n', 'o', 't', ' ', 'l', 'i', 'e']
 

Voici un exemple d'utilisation réelle. Construisons les paramètres d'une base de données, qu'on veut passer à une fonction. Dans cet exemple le premier code qui s'exécute est \  ``if __name__ == "__main__":`` \. Sur les systèmes Linux (e.g. Ubuntu) on peut exécuter ce script sans ouvrir l'interpréteur Python (Yeah!). Copier le code ci-dessous dans un fichier texte et le sauver sous \  ``test.py`` \dans un répertoire. Ensuite ouvrir un shell bash et ``cd`` dans ce répertoire. Taper sur la ligne de commande : ``python test.py`` . Votre script va s'exécuter et retourner la chaine suivante : ``pwd=secret;database=qgis;uid=sa;server=localhost``. Allez y::

    def buildConnectionString(params):
        """Build a connection string from a dictionary of parameters.

        Returns string."""
        return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

    if __name__ == "__main__": 
        myParams = {"server":"localhost", \
                        "database":"qgis", \
                        "uid":"sa", \
                        "pwd":"secret" \
                        }
        print buildConnectionString(myParams)


Quelques ressources supplémentaires pour se lancer sur la piste des Ninjas du Python:        

    `Dive into Python <http://diveintopython.org/toc/index.html>`_

    `How to Think Like a Computer Scientist <http://greenteapress.com/thinkpython/html/index.html>`_

    `The Python Tutorial <http://docs.python.org/tutorial/>`_ \-- le tutoriel officiel


    

