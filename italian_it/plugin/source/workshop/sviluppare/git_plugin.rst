=============================
Sviluppare alla luce del sole
=============================

Ambiente di sviluppo dei plugin
-------------------------------

Come abbiamo precedentemente visto, ci sono varie opzioni per mantenere un ambiente di sviluppo dei plugin:

* Copiare il modello di plugin nella cartella dei plugin di QGIS e lavorare in quella posizione
* Lavorare nella cartella dove abbiamo creato i nostri modelli e creare un link a partire dalla cartella dei plugin

Il problema con la prima opzione è che se si vuole testare la disinstallazione dei plugin si rischia di perdere il codice. Con la seconda opzione non si ha questo rischio, ma bisogna ogni volta ricreare il link a partire dalla cartella dei plugin.

Ci sono due modi per gestire tale problema:

* 1 - La prima opzione consiste nell'utilizzare un sistem di controllo di versione come *Git* e di effettuare dei *commit* a partire dal repository di lavoro e dei *pull* nel repository dei plugin. Non è molto più pratico che copiare in seguito ad ogni modifica il codice dal repository del plugin.
* 2 - **La seconda opzione è quella da utilizzare**. Si tratta di lavorare in un repository esterno a quello dei plugin e di utilizzare la variabile d'ambiente QGIS_PLUGINPATH, facendola puntare verso il repository di sviluppo. QGIS_PLUGINPATH indica a QGIS dove cercare i plugin; in tal modo è possibile utilizzare il repository di sviluppo e testare i plugin senza dover ricreare il link o fare delle copie di codice di volta in volta. In questo scenario il plugin non è installato tramite l'installatore di plugin, per cui non può essere disinstallato e dunque non può essere cancellato per errore. Nel momento in cui si è pronti per testare installazione/disinstallazione, si può copiare il plugin nel repository di QGIS o creare un repository ad hoc.

Cos'è Git?
----------

Git è un sistema di controllo di versione di codice sorgente distribuito. Permette di gestire diversi flussi di sviluppo di codice ed è attualmente uno degli strumenti più utilizzati nel mondo dello sviluppo opensource: Git è usato per la gestione dei sorgenti del kernel Linux.

Una buona risorsa su Git è il libro liberamente disponibile sul web *Pro Git* (http://progit.org/it). Di seguito si riporta un breve estratto del libro:

.. toctree::
    :maxdepth: 2

    git

Crare un repository git
-----------------------

Lo sviluppo software necessita di una serie di strumenti per poter conservare una certa qualità; tra questi, il *bug tracker* ed il sistema di controllo versione del codice sorgente sono indispensabili. L'infrastruttura del progetto QGIS mette tali strumenti a disposizione di tutti.

E' possibile creare un *account* sullo hub di QGIS (http://hub.qgis.org) o su GitHub (http://www.github.com), in modo da beneficiare di un repository di codice sorgente *git*.

Ecco le tappe da seguire per creare un plugin con un sistema di gestione del codice sorgente con Git:

#. Installate Git
#. Installate il Plugin Builder
#. Create una cartella per i vostri plugin, es. *my_plugins*
#. Create un modello di plugin con Plugin Builder, indicando come base la cartella di cui al punto precedente
#. Portatevi nella cartella del plugin (es. my_plugins/zoomer) creato con Plugin Builder e create un repository *git* dando il comando::

    git init

#. Fate in modo che la variabile d'ambiente QGIS_PLUGINPATH punti alla cartella di sviluppo (*my_plugins*). **Specificate il percorso completo** 
#. Avviate QGIS ed utilizzate il gestore dei plugin per attivare il plugin di sviluppo. Se il plugin non è visibile, verificate che la variabile QGIS_PLUGINPATH sia ben impostata
#. Sviluppate e fate dei test. Non dimenticate di committare regolarmente i cambiamenti e di fare *push* verso il repository pubblico (su hub.qgis.org o su Github).

Sviluppare con Git
------------------

Ecco alcuni comandi di uso comune quando si sviluppa con Git:

Creare un nuovo repository git::

    git init

Aggiungere dei file::

    git add -A

Controllare lo stato dei file::

    git status

Committare le modifiche::

    git commit -a

Specificate un messagio per spiegare le modifiche effettuate.

Fare *push* delle modifiche sul repository remoto::

    git push

Ottenere una copia locale di un repository remoto::

    git clone git://github.com/schacon/grit.git

Aggiornare un repository locale rispetto ad un repository remoto::

    git fetch

Crare un repository sorgente QGIS
---------------------------------

Il progetto QGIS mette a disposizione la propria infrastruttura per ospitare dei progetti di sviluppo. E' possibile creare nuovi progetti di plugin e gestirne il codice.

Fase preparatoria: creare le chiavi SSH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per poter utilizzare Git è necessario disporre di chiavi di autenticazione SSH.

Verifichiamo se già disponiamo di chiavi SSH::

    $ cd ~/.ssh

Se la cartella esiste, salviamo le chiavi in essa presenti::

    $ ls
    config	id_rsa	id_rsa.pub	known_hosts
    $ mkdir key_backup
    $ cp id_rsa* key_backup
    $ rm id_rsa*

Creiamo una nuova chiave SSH, con impostazioni predefinite::

    $ ssh-keygen -t rsa -C "your_email@youremail.com"
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/formation/.ssh/id_rsa):

Forniamo una password per validare le chiavi::

    Enter passphrase (empty for no passphrase):<enter a passphrase>
    Enter same passphrase again:<enter passphrase again>

Apparirà qualcosa come::

    Your identification has been saved in /Users/your_user_directory/.ssh/id_rsa.
    Your public key has been saved in /Users/your_user_directory/.ssh/id_rsa.pub.
    The key fingerprint is:01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db user_name@username.com
    The key's randomart image is:
    +--[ RSA 2048]----+
    |     .+   +      |
    |       = o O .   |
    |        = * *    |
    |       o = +     |
    |      o S .      |
    |     o o =       |
    |      o . E      |
    |                 |
    |                 |
    +-----------------+

Significa che le chiavi sono state create. Potete usarle per connettervi a GitHub o a QGIS.

Configurare Git
^^^^^^^^^^^^^^^

Non resta che configurare Git::

  git config --global user.name "NomeUtente"
  git config --global user.email nome.utente@email.com

E' possibile configurare questi campi per ogni repository usando::

    $ cd my_other_repo
    $ git config user.name "NomeDiverso"
    $ git config user.email "email.diversa@email.com"

Crare un conto su GitHub
^^^^^^^^^^^^^^^^^^^^^^^^

Createvi un account su http://www.github.com. Andate in "Account Settings" > "SSH Public Keys" > "Add another public key" ed inserite nel campo "Key" la vostra chiave SSH pubblica: la trovate nel file "id_rsa.pub" (se non trovate la cartella .ssh dovete attivare la visualizzazione dei file nascosti); copiatela
esattamente come è nel file, senza spazi nè accapo. Cliccate su "Add key".

Potete testare la connessione al server SSH di GitHub utilizzando il seguente comando::

    $ ssh -T git@github.com

Dovreste ottenere::

    The authenticity of host 'github.com (207.97.227.239)' can't be established.RSA key fingerprint is 
    16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.Are you sure you want to continue connecting (yes/no)?

Rispondete "yes" e riceverete::

    Hi username! You've successfully authenticated, but GitHub does not provide shell access.

A questo punto potete creare un vostro progetto su GitHub oppure potete fare un *fork* di un progetto esistente cui volete contribuire.

Creare un conto sullo hub di QGIS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per poter interagire con la piattaforma di sviluppo di QGIS, bisogna disporre di un account **OSGeo**, che potete ottentere all'indirizzo web: https://www2.osgeo.org/cgi-bin/ldap_create_user.py

Lo hub di QGIS si trova all'indirizzo web: http://hub.qgis.org. Per creare un nuovo progetto andate all'indirizzo http://hub.qgis.org/projects/new.

Ci sono diverse opzioni per selezionare le funzionalità volute per l'interfaccia di gestione del vostro progetto:

* bugtracker
* campi specifici per la gestione di un bug
* repository di file
* calendario
* wiki

Creato un nuovo progetto, potete attivare il repository del codice e scegliere Git come gestore del codice sorgente, nel qual caso la scheda
*Repository* fornirà le istruzione per creare il repository *git*.

* configurazione della gestione dei permessi

  * Upload della chiave SSH pubblica. All'indirizzo http://hub.qgis.org/my/public_keys potete, come per GitHub, inviare la vostra chiave pubblica (cliccate su New Value).
  * aggiunta di membri sviluppatori (scheda settings/members potete modificare un utente o aggiungerne degli altri)

* creazione del repository ed invio allo hub

::

  cd pyqgis
  git init
  git add .
  git commit -m 'Initialisation of the Python QGIS Workshop repository'
  git remote add origin gitosis@qgis.org:pyqgis.git
  git push origin master

Se già si ha un repository *git* e lo si vuole inviare sullo hub di QGIS::

  cd existing_git_repo
  git remote add origin gitosis@qgis.org:pyqgis.git
  git push origin master

Se il vostro progetto riguarda un plugin, dovete creare un sottoprogetto del progetto globale "User Plugins".

Distribuire tramite il repository centrale dei plugin
-----------------------------------------------------

Ora che il nostro progetto è sviluppato e possiede un ambiente di sviluppo corretto, possiamo pensare alla sua distribuzione. 
Il sito http://plugins.qgis.org/ raggruppa tutti i plugin di QGIS e permette di ricercarli, valutarne lo stato di sviluppo, la loro popolarità, etc.

Il sito raggruppa anche frammenti di codice Python che possono essere interessanti da studiare e/o condividere.

Il login si fa con l'account *OSGeo*.

Il pulsante "Share a plugin" permette di accedere alla pagina di upload dei plugin. Possiamo, quindi, inviare un file zip contenente il nostro plugin.
