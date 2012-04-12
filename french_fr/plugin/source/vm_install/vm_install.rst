==========
VirtualBox
==========
On utilise une image disque vdi VirtualBox pour ce tutoriel. Notre VM a les 
logiciels suivants :

- Ubuntu 10.04 (minimal install)
- FireFox pour le web
- QT et PyQT, paquets de developpement
- QGIS SVN (Trunk du 07/01/11)

La taille de la vdi est 

- 3.1 GB non compresse
- 1.1 GB compresse

La vdi peut etre telechargee a partir de:
http://www.qgisworkshop.org/dl/qgis-foss4g11-1004.vdi.zip

Pour installer l'image:

- Installer et démarrer VirtualBox sur l'hote
- Creer une nouvelle machine avec Linux - Ubuntu (32 bits) comme système de base
- NE PAS créer de nouveau disque, mais donner comme disque celui téléchargé
- finir la configuration
- booter

Le système a un utilisateur par défaut (avec les droits sudo):
User: qgis
Password: qgis


================
QGIS SVN 
================
QGIS a été installé à partir du répertoire personnel de l'utilisateur QGIS. Si vous ouvrez un terminal vous allez voir un répertoire qgis-trunk. Pour mettre à jour vous pouvez effectuer les commandes suivantes::

  cd qgis-trunk
  svn up
  cd build
  make
  sudo make install


