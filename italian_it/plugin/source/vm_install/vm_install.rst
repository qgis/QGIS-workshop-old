==========
VirtualBox
==========
Per questo workshop potete utilizzare un'immagine disco "vdi" per VirtualBox. La macchina virtuale contiene il seguente software:

- Ubuntu 10.04 (installazione minimale)
- FireFox 
- QT e PyQT 
- QGIS compilato da SVN (Trunk del 07/01/11)

Le dimensioni dell'immagine disco sono:

- 3.1 GB non compressa
- 1.1 GB compressa

Scaricate l'immagine da:
http://www.qgisworkshop.org/dl/qgis-foss4g11-1004.vdi.zip

Per installare l'immagine:

- Installate ed avviate VirtualBox
- Create una nuova macchina utilizzando Linux - Ubuntu (32 bit) come tipo base
- NON create un nuovo disco, ma selezionate il file vdi scaricato come disco
- Terminate il setup 
- Avviate la macchina virtuale

Il sistema ha un solo utente predefinito (con sudo privs):
User: qgis
Password: qgis

Divertitevi!

================
QGIS da sorgente
================
QGIS e' stato installato dalla directory *home* dell'utente *qgis*. 
Se aprite il terminale vedrete una directory *qgis-trunk*. 
Per aggiornare QGIS potete dare i seguenti comandi::

  cd qgis-trunk
  svn up
  cd build
  make
  sudo make install


