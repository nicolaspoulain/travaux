
Drupal et commerce_atos
=====================

Le module [Commerce Atos][commerce_atos] permet le paiement par carte bleue sur un site e-commerce.

  [commerce_atos]: https://drupal.org/project/commerce_atos

Documentation [Gandi][wikigandi]

  [wikigandi]: http://wiki.gandi.net/fr/simple/faq#comment_installer_et_utiliser_les_paiements_atos


> Comment installer et utiliser les paiements Atos ?
> 
> L'exécution de binaires n'est pas autorisée sur les instances Simple Hosting, cependant, nous avons installé et mis à disposition les binaires du modules de paiement SIPS d'ATOS.
> 
> Localisation des fichiers de configuration :
> 
> Vous pouvez placer les fichiers ATOS dans un sous répertoire du dossier /tmp ou bien un sous répertoire du vhost.
> 
> Il vous faudra spécifier ces chemins dans le fichier pathfile, de la manière suivante :
> 
>     /tmp/votre_dossier
> 
> ou bien
> 
>     /srv/data/web/vhosts/www.mondomaine.tld/votre_dossier
> 
> De même, la spécification du chemin du fichier pathfile dans le code de la requête ou de la réponse devra être de la même forme absolue :
> 
>     $parm="$parm pathfile=/srv/data/web/vhosts/www.mondomaine.tld/votre_dossier/pathfile";
> 
> Localisation des binaires request et response :
> 
> Dans vos pages de code dédiées à effectuer la requête au système SIPS, ainsi que dans la page chargée de traiter la reponse, vous aurez à préciser les chemins des binaires via la variable $path_bin, de cette façon :
 
>     $path_bin = "/usr/local/bin/atos/request"; $path_bin = "/usr/local/bin/atos/response";


