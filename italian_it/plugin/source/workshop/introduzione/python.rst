======
Python
======

Cos'è Python
------------

Python è un linguaggio di programmazione potente e divertente, che trova utilizzo sia nello sviluppo di applicazioni web che di software desktop. E' possibile ritrovarlo in wrap a librerie tipo GDAL/OGR, JTS e GEOS. Le caratteristiche principali sono:

    * chiarezza e leggibilità della sintassi
    * orientazione ad oggetti intuitiva
    * gestione dell'errore exception-based
    * tipi dato dinamici e di alto livello
    * implementato in diversi linguaggi (Python ha C/C++ nel suo *core*. Ci sono implementazioni in Java (Jython) e .NET (IronPython)

Perchè è così importante e popolare
-----------------------------------

* Per i nostro scopi, Python permette di accedere a svariate librerie e software; quindi, usiamo Python per codificare dei flussi di lavoro. Alcune delle librerie utilizzabili con Python sono: 

    - QGIS
    - PostGIS
    - GDAL/OGR
    - GEOS
    - JTS
    - GeoTools
    - Proj4
    - Mapserver
    - gvSIG

* Il suo nome deriva da “Monty Python’s Flying Circus”

* E' allo stesso tempo potente e facile da imparare

Esempi
------

Gli esempi che seguono sono eseguiti nell'interprete Python, cui si può accedere in due modi -- 1. attraverso QGIS e 2. attraverso la schell bash.

    1. La Console Python di QGIS può essere avviata da \ ``Plugins --> Console python`` \
    
    2. La shell bash può essere avviata da tastiera con \ ``<Cntl>-<ALT>t`` \o usando i menu del sistema operativo. Scrivendo\  ``python`` \al prompt dei comandi, si ha accesso all'interprete Python.

E' molto facile in Python ottenere informazioni su funzioni ed oggetti. Se, ad esempio, una particolare variabile vi sta creando problemi, potete utilizzare l'help di Python per visualizzarne il significato (se ne ha uno)::

    >>> help(range)
    Help on built-in function range in module __builtin__:

    range(...)
        range([start,] stop[, step]) -> list of integers
        
        Return a list containing an arithmetic progression of integers.
        range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
        When step is given, it specifies the increment (or decrement).
        For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
        These are exactly the valid indices for a list of 4 elements.


Stringhe, numeri, liste.... Le **liste** sono il tipo di dato più potente di Python ed è importante conoscerne bene il funzionamento. Le **liste** possono essere usate per memorizzare praticamente di tutto; i record di un database sono gestiti come **liste** in Python::
    
    >>> # this is me making a list
    ... a = [10, 50, 123, 1234]
    >>> # Replace some items:
    ... a[0:2] = [1, 12]
    >>> a
    [1, 12, 123, 1234]
    >>> # Remove some:
    ... a[0:2] = []
    >>> a
    [123, 1234]
    >>> # Insert some:
    ... a[1:1] = ['bletch', 'xyzzy']
    >>> a
    [123, 'bletch', 'xyzzy', 1234]
    >>> # Insert (a copy of) itself at the beginning
    >>> a[:0] = a
    >>> a
    [123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
    >>> # Clear the list: replace all items with an empty list
    >>> a[:] = []
    >>> a
    []


Un esempio si analisi di stringhe e di tra i dati utilizzando le **liste**::

    >>> # basic for loop
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
    >>> # sexier loop structure 
    >>> mess = [i for i in string.split("I love maps and I cannot lie"," ")]
    >>> mess
    ['I', 'love', 'maps', 'and', 'I', 'cannot', 'lie']
    >>> really_messy = [i for i in "I love maps and I cannot lie"]
    >>> really_messy
    ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'm', 'a', 'p', 's', ' ', 'a', 'n', 'd', ' ', 'I', ' ', 'c', 'a', 'n', 'n', 'o', 't', ' ', 'l', 'i', 'e']
 

Quello che segue è un esempio di utilizzo che potrebbe tornare utile. Creiamo i parametri di connessione ad un database da passare ad una funzione.
Il primo codice eseguito è:\  ``if __name__ == "__main__":``\. Su Linux (es. Ubuntu) possiamo eseguire lo script senza aprire l'interprete Python. Copiate il codice seguente in un file di testo e salvatelo come\  ``test.py``\, quindi, aprite una shell bash, portatevi nella directory contenente il file appena creato e scrivere al prompt dei comandi:\  ``python test.py``\. Lo script verrà eseguito e restituirà le stringhe seguenti:\  ``pwd=secret;database=master;uid=sa;server=gcorradini``\. Provate::

    def buildConnectionString(params):
        """Costruisce una stringa di connessione da un dizionario di parametri

        Restituisce la stringa"""
        return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

    if __name__ == "__main__": 
        myParams = {"server":"gcorradini", \
                        "database":"master", \
                        "uid":"sa", \
                        "pwd":"secret" \
                        }
        print buildConnectionString(myParams)

Di seguito dei link dove è possibile trovare ulteriori risorse su Python:

    `Dive into Python <http://it.diveintopython.net/toc/index.html>`_

    `Pensare da informatico. Versione Python <http://www.python.it/doc/Howtothink/Howtothink-html-it/index.htm>`_

    `Il Tutorial di Python <http://docs.python.it/html/tut/tut.html>`_ \# Il tutorial ufficiale di Python


