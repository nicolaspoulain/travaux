# Download Sublime Text 2 from http://www.sublimetext.com/2
# If you aren't root, sudo su
tar -xvjf Sublime\ Text\ 2*.tar.bz2
mv Sublime\ Text\ 2/ /opt/sublime-text-2/
ln -s /opt/sublime-text-2 /usr/local/sublime-text-2
ln -s /usr/local/sublime-text-2/sublime_text /usr/local/bin/sublime_text
rm Sublime\ Text\ 2*.tar.bz2


http://blog.goetter.fr/post/24671859680/sublime-text-2-raccourcis-et-plugins

N’oublie pas le shift + clic droit pour la sélection verticale, F9 pour trier par ordre alphabétique ou ctrl + D pour sélectionner plusieurs occurrences d'une sélection 

Raccourcis clavier utiles :
 - Clic molette : sélection verticale
 - Ctrl + Shift + P : Commandes
 - Ctrl + P : Accès rapide aux fichiers
 - Ctrl + G : Accès au numéro de ligne
 - Ctrl + R : Accès direct par terme (par ex liste des sélecteurs en CSS)
 - Ctrl + Shift + D : Dupliquer une ligne
 - Ctrl + Shift + F : Recherche dans les fichiers du projet
 - Ctrl + H : Remplacer
 - Ctrl + X : Supprimer la ligne
 - Ctrl + / : Mettre en commentaires (PHP, HTML, …)
 - Ctrl + D : Sélectionner l’occurrence identique suivante
 - Alt + F3 : Sélectionner toutes les occurrences (génial !)
 - Ctrl + Shift + M : Sélectionner tout entre les parenthèses/accolades
 - Ctrl + PageUp/PageDown : Se déplacer dans les onglets
 - Ctrl + Shift + T : Réouvrir le dernier onglet fermé
 - Alt + Shift + 1/2/3/4/5 : Vues splittées
 - Ctrl + F2 : Placer un signet
 - F2 : Aller au signet suivant
 - Ctrl + KU : Met le texte sélectionné en uppercase
 - Ctrl + KL : Met le texte sélectionné en lowercase
 - F9 : tri par ordre alphabétique



Un exemple de workflow avec Sublime Text 2 (et quelques plugins sympas
aussi !)
: [http://tarantsov.com/blog/2012...](http://tarantsov.com/blog/2012/02/sublime-text-workflow-that-beats-coda-and-espresso/) \
Pour résumer, les choses à côté desquelles il ne faut pas passer selon
moi :\
- la multi-selection de texte,\
- la possibilité de configurer n'importe quel plugin et Sublime Text 2
lui-même (raccourcis clavier/souris, menus, snippets, et autres...
exemple [https://github.com/kellyreddin...](https://github.com/kellyredding/sublime-text-2-user-settings) et [https://github.com/Grafikart/S...](https://github.com/Grafikart/Sublime-Text-2-Preferences)),\
- la possibilité d'utiliser l'ensemble des bundle de TextMate (rien que
ça !),\
- [https://github.com/weslly/Nett...](https://github.com/weslly/Nettuts-Fetch)\
- [https://github.com/Kronuz/Subl...](https://github.com/Kronuz/SublimeCodeIntel)

#### Plugins en tout genre

##### Indispensable pour commencer :

-   Installer [Package Control
    Plugin](http://wbond.net/sublime_packages/package_control/installation)
    via la Console
-   puis *Ctrl + Shift + P* : sélectionner Install Package et choisir
    dans la liste suivante…

##### Plugins intéressants pour intégrateur, par ordre de préférence personnelle :

**[CSSlisible :](https://github.com/thierrylemoulec/Sublime-Csslisible)**
pour réordonner proprement votre code CSS (ordre des déclarations,
indentation), ou tout simplement pour dé-minifier du CSS (Ctrl + Alt +
L)

[**Minifier :**](https://github.com/bistory/Sublime-Minifier) pour
minifier le HTML, CSS et JavaScript avec Ctrl+Alt+M.

[**Hayaku :**](http://hayakubundle.com/)raccourcis pour propriétés CSS
avec la touche Tab (genre de Emmet / Zencoding en mieux !)

**[Prefixr](http://wbond.net/sublime_packages/prefixr) :** pour préfixes
constructeurs CSS (Ctrl + Alt + X)

**[Caniuse](https://github.com/Azd325/sublime-text-caniuse) :** pour
chercher directement la propriété sur Caniuse (Ctrl+Alt+F)

**[CSSLint](https://github.com/austinhappel/sublime-csslint) :** pour
CSSLint (affichage des erreurs de conception) (Ctrl+Alt+C)

**[ColorHighlighter](https://github.com/Monnoroch/ColorHighlighter)**pour
afficher les couleurs CSS dans la source en highlight quand on les
focus.

[**Emmet**](http://emmet.io/) (ex-ZenCoding) avec la touche Tab

Tags pour des tas d’outils sur les balises HTML

[**StringEncode :**](https://github.com/colinta/SublimeStringEncode)
pour (entre-autre) convertir des caractères en entités HTML, par exemple
les chevrons de balises, les &, etc.

[ColorPicker](http://weslly.github.com/ColorPicker/) pour afficher la
palette couleur système et obtenir le code \#hexa avec Ctrl+Shift+C.

[SublimeLinter](https://github.com/kronuz/SublimeLinter/) pour JSLint
avec Ctrl+Shift+J (+Alt)

[ClosureLinter](https://github.com/fbzhong/sublime-closure-linter) pour
JavaScript Lint avec Ctrl+Shift+J.

[CodeIntel](https://github.com/Kronuz/SublimeCodeIntel) pour
auto-complétion magique PHP, JavaScript, Smarty, Node.js, HTML, HTML5,
Ruby, Python etc.

[GotoCSSDeclaration](https://github.com/rmaksim/Sublime-Text-2-Goto-CSS-Declaration)
aller directement à la déclaration CSS depuis HTML (ne fonctionne pas ?)

[Open-Include](https://github.com/SublimeText/Open-Include) pour ouvrir
les fichiers mentionnés dans le source avec Alt+D.

[jQuery](https://github.com/mrmartineau/Jquery) pour auto-complétion
jQuery

[Placeholders](https://github.com/mrmartineau/Placeholders) pour du
Lorem Ipsum

[LESS Sublime](https://github.com/danro/LESS-sublime) pour coloration
syntaxique LESS

[Less-ish](https://github.com/kizza/CSS-Less-ish) Pour écriture à la
LESS (variables, mixins)

[HTMLTidy](https://github.com/welovewordpress/SublimeHtmlTidy)

[FTPsync](https://github.com/NoxArt/SublimeText2-FTPSync) client FTP
direct

[SVN](http://wbond.net/sublime_packages/svn)

[Git](https://github.com/kemayo/sublime-text-2-git)
