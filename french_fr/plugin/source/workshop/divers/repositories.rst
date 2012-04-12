
=====================
Dépôt de plugins
=====================

Dépôt officiel
-----------------------
Lorsqu'on cherche des plugins à installer ou à utiliser comme exemples, le\ `dépôt officiel de plugin QGIS <http://plugins.qgis.org/plugins/>`_ \ est le meilleur endroit où commencer. Une version plus ancienne du dépôt des contributions externes est situé\ `ici <http://pyqgis.org/repo/contributed>`_ \. Alors que la communauté de développeurs de plugin augmente, le processus de développement de plugin change également. Historiquement beaucoup de développeurs externes maintenaient leurs propres dépôts, et beaucoup existent toujours aujourd'hui. Il est cependant conseillé désormais de contribuer sur le dépôt officiel de plugins, afin de faciliter la maintenance des plugins et de simplifier la gestion des bugs et corrections.

Dépôts publics
-------------------------
Il y a aussi un certain nombre de dépôts publics qui sont maintenus par des tierces parties enregistrés dans QGIS. Dans le gestionnaire d'extensions de QGIS, l'onglet 'Dépots' permet d'ajouter ces dépôts externes. Avec cette option vous aurez une liste des dépôts publics disponibles. Mais ceux ci ne sont pas gérés ni maintenus par le projet QGIS, et sont donc à utiliser à vos propres risques.

Votre propre dépôt privé
-----------------------------
Si vous voulez créer votre propre dépôt privé, c'est aussi simple que de créer un fichier XML (qui peut être local) accessible par le web, et qui décrit à QGIS où télécharger le plugin. L'extrait XML suivant est un exemple de la structure nécessaire pour créer un dépôt::

    <?xml version = '1.0' encoding = 'UTF-8'?>
    <?xml-stylesheet type='text/xsl' href='/plugins.xsl' ?>
    <plugins>
      <pyqgis_plugin name='Plugin Installer' version='1.1'>
        <description>The recent Python Plugin Installer</description>
        <version>1.1</version>
        <qgis_minimum_version>1.0</qgis_minimum_version>
        <homepage>http://www.bwj.aster.net.pl/qgis/</homepage>
        <file_name>plugin_installer.zip</file_name>
        <author_name>Borys Jurgiel</author_name>
        <download_url>http://spatialserver.net/pyqgis_1.0/plugins/plugin_installer.zip</download_url>
        <uploaded_by>borysiasty</uploaded_by>
        <create_date>2008-12-18</create_date>
        <update_date>2010-10-31</update_date>    
      </pyqgis_plugin>
    </plugins>


Packaging
------------
Pour créer un paquet vous devez finaliser tout votre code et vos fichiers UI, et ensuite zipper le paquet pour pouvoir le distrubuer. QGIS s'attend à ce que le paquet Zip contienne une structure de répertoire qui sera hébergé dans le répertoire .qgis, donc la commande suivante sur les systèmes unix devrait vous donner le résultat souhaité::

    zip -9vr myPlugin.zip myPlugin/*

