% Vim Memo
% NPO
% Janvier 2014

#Vim Memo

 |                             | SPLIT ET RESIZE                                              |
 | :-------------------------  | :----------------------------------------------------------  |
 | `:res 60`                   | Définit la hauteur de la fenêtre                             |
 | `:vertical resize 80`       | Définit la largeur de la fenêtre                             |
 | `:res {+,-}10`              | Augmente/réduit la hauteur de la fenêtre                     |
 | `10 Ctrl-w {+,-}`           | "" idem                                                      |
 | `:vertical resize {+,-}10`  | Augmente/réduit la largeur de la fenêtre                     |
 | `10 Ctrl-w {>,<}`           | " " idem                                                     |
 | `Ctrl-w =`                  | Égalise la taille des fenêtres                               |
 | `Ctrl-w _`                  | Augment au maximum la taille de la fenêtre                   |
 | `Ctrl-w s`                  | Partge la fenêtre courante en deux                           |
 | `Ctrl-w H`  `Ctrl-w L`      | Place la fenêtre courante à gauche / à droite                |
 | `Ctrl-w J`  `Ctrl-w K`      | Place la fenêtre courante en haut / en bas [^3]              |

 |                             | BUFFERS                                                      |
 | :-------------------------  | :----------------------------------------------------------  |
 | `:e newFile`                | ouvre un nouveau buffer avec newFile                         |
 | `:ls`                       | pareil que :buffers, mais en plus court                      |
 | `:bw`                       | ferme le buffer courant                                      |
 | `:sb x`                     | place le buffer x dans une fenêtre splitée                   |
 | `:bnext`       maped to F2  | Opens next buffer                                            |
 | `:bprevious`   maped to F3  | Opens previous buffer                                        |

 |                             | RECHERCHE, REMPLACEMENT ET SUPPRESSIONS                      |
 | :-------------------------  | :----------------------------------------------------------  |
 | `*`                         | Recherche pour le mot exact sous le curseur                  |
 | `g*`                        | Recherche pour le mot partiel sous le curseur                |
 | `[I`                        | Affiche les lignes contenant le mot sous le curseur          |
 | `:g/foo`                    | Affiche les lignes contenant foo                             |
 | `:g/foo/d`                  | supprime les lignes contenant la chaîne de caractères foo    |
 | `:v/foo/d`                  | supprime les lignes ne contenant pas la chaîne foo           |
 | `:g/^[\.]*$/d`              | supprime les lignes vides                                    |

 |                             | RECHERCHE, REMPLACEMENT ET SUPPRESSIONS                      |
 | :-------------------------  | :----------------------------------------------------------  |
 | `:s/foo/bar/`               | remplace le 1er foo de la ligne courante par bar             |
 | `:s/foo/bar/g`              | remplace tous les foo de la ligne courante par bar           |
 | `:%s/foo/bar/`              | remplace TOUS le 1er foo de chaque ligne du fichier par bar  |
 | `:%s/foo/bar/g`             | remplace TOUS les foo du fichier par bar                     |
 | `:%s/foo/bar/gc`            | " " idem avec demande de confirmation                        |
 | `:%s/.*\zsfoo/bar/`         | replace the last occurrence of "foo" with "bar".             |
 | `:%s/\<foo\>//g`            | Supprime le mot "foo".                                       |
 | `:%s/.*\<foo\>//`           | Supprime le mot "foo" et tout ce qui le précède.             |
 | `:%s/\<foo\>.*//`           | Supprime le mot "foo" et tout ce qui le suit.                |
 | `:%s/.*\ze\<foo\>//`        | Supprime tout ce qui précède le mot "foo"                    |
 | `:%s/\<foo\>\zs.*//`        | Supprime tout ce qui suit le mot "foo"                       |
 | `:%s/.*\(\<foo\>\).*/\1/`   | Supprime tout ce qui entoure le mot "foo"                    |
 | `:%s/\<foo\>.\{5}//`        | Supprime le mot "foo" et les 5 catactères qui suivent        |
 | `:%s/\s\+$//`               | Supprime les espaces de fin de ligne[^5]                     |
 | `:s/.*/\U&/`                | passe la ligne courante en majuscule                         |
 | `:%s/^foo//`                | Supprime TOUS les foo placés en début de ligne               |

                  |        | SINGLE-CHARACTER                   |
                  | ` .`   | any character                      |
                  | `[ ]`  | any characters listet              |
                  | `[^ ]` | any characters except those listet |

                  |        | ANCHORS                   |
                  | ^      | start of line             |
                  | $      | end of line               |
                  | \<     | beginning of a word       |
                  | \>     | end of a word             |
                  | `\| `  | alternation (logical OR)  |

                  |                        | METACARACTÈRES                |
                  | `.`                    | any character except new line |
                  | `\s`                   | whitespace character          |
                  | `\d`                   | digit                         |
                  | `\h`                   | head of word character        |
                  | `\p`                   | printable character           |
                  | `\w`                   | word character                |
                  | `\a`                   | alphabetic character          |
                  | `\l`                   | lowercase character           |
                  | `\u`                   | uppercase character           |
                  | Greedy    : ^Greedy    | Quantifier                    |
                  | `* `      : `\{-} `    | 0 ou plus                     |
                  | `\+ `     : `\{-1} `   | 1 ou plus                     |
                  | `\= `     : `\{-0,1} ` | 0 ou 1 fois                   |
                  | `\{n} `   :            | n fois exactement             |
                  | `\{n,} `  : `\{-n,} `  | n fois au moins               |
                  | `\{,m} `  : `\{-,m} `  | m fois au plus                |
                  | `\{n,m} ` : `\{-n,m} ` | entre n et m fois             |

                  |            | REPLACEMENT                                             |
                  | `& `       | the whole matched pattern                               |
                  | `\0`       | the whole matched pattern                               |
                  | `\1 \2...` | matches text in 1st, 2nd ... pair of `\(\)`             |
                  | `~ `       | the previous substitute string                          |
                  | `\L` `\U`  | the following characters are made lowercase / uppercase |
                  | `\l` `\u`  | next character made lowercase / uppercase               |
                  | `\E`       | end of \U and \L                                        |
                  | `\r`       | split line in two at this point                         |

 |                             | SELECTION DE BLOC TEXTE                                      |
 | :-------------------------  | :----------------------------------------------------------  |
 | `v       lljj`              | selection de texte                                           |
 | `Shift-v jj`                | selection de lignes entières                                 |
 | `Ctrl-v  lljj`              | selection de colonnes                                        |
 | `gv`                        | Resélectionne le bloc                                        |
 | `h j k l'i , `D`            | En mode visuel : déplace le bloc, duplique (vim-dragvisuals) |

 |                             | INSERTION SUR PLUSIEURS LIGNES                               |
 | :-------------------------  | :----------------------------------------------------------  |
 | `Ctrl-v jj I foo Esc`       | Insertion dans une colonne d'un bloc                         |
 | `Ctrl-v jj $ A STR Esc`     | Insertion à la fin des lignes d'un bloc                      |
 | `Ctrl-v jj Shift-i # Esc`   | Commente les lignes d'un bloc                                |
 | `Shift-v s/^/#`             | Commente les lignes d'un bloc (autre méthode)                |

 |                             | INDENTATION, AUTOINDENTATION ET TABULARIZE                   |
 | :-------------------------  | :----------------------------------------------------------  |
 | `>>` `<<`                   | Indente ou desindente la ligne courante
 | `gg=G`                      | Si cela ne fonctionne pas, set `ft=html` puis `set si`[^6]   |
 | `Shift-v =`                 | Indente un bloc                                              |
 | `==`                        | indente la ligne courante                                    |
 | `:Tabularize /:`            | aligns statements on :                                       |
 | `:Tabularize /&&`           | aligns statements on &&                                      |

 |                             | REGISTRES                                                    |
 | :-------------------------  | :----------------------------------------------------------  |
 | `"5yy"` `"hyy`              | Copie la ligne dans le registre 5 (ou h)                     |
 | `:reg`                      | Liste les registres                                          |
 | `"5p`  `"hp`                | Colle le contenu du regsitre 5 (ou h)                        |

 |                             | FOLDING COMMANDS [^1]                                        |
 | :-------------------------  | :----------------------------------------------------------  |
 | `za`                        | Toggle the state of one fold (`zA` recursively) [^2]         |
 | `zR`                        | Opens ALL folds (`zr` decreases foldlevel by one)            |
 | `zM`                        | Closes ALL folds (`zM` increases foldlevel by one)           |
 | `zf%`                       | creates a fold from from a delimitor to its brother .        |
 | `Vjjjjzf`                   | creates a fold from visual block.                            |
 | `zf#j`                      | creates a fold from the cursor down # lines.                 |
 | `zf/string`                 | creates a fold from the cursor to string .                   |
 | `zj`                        | moves the cursor to the next fold.                           |
 | `zk`                        | moves the cursor to the previous fold.                       |
 | `zd`                        | deletes the fold at the cursor.                              |
 | `zE`                        | deletes ALL folds.                                           |
 | `[z`                        | move to start of open fold.                                  |
 | `]z`                        | move to end of open fold.                                    |

 |                             | TABS                                                         |
 | :-------------------------  | :----------------------------------------------------------  |
 | `:sp file <CR> CTRL-w T`    | crée un nouvel onglet avec le fichier file                   |
 | `Ctrl-PgDn` & `Ctrl-PgUp`   | go to next tab & previous tab                                |
 | `gt` (`5gt`)                | to switch to next tab (to tab 5)                             |


[^1]:  Dans le .vimrc `:mkview    " save folds` & `:loadview  " restore folds`
[^2]: za (resp. zA) toggles between zo & zc (resp. zO & zC)
[^3]: The lower case equivalents move focus instead of moving the window.
[^5]: In a search, `\s` finds whitespace (a space or a tab), and `\+` finds one or more occurrences.
[^6]: donner le bon le filetype et enclancher le smartindent

<!--

#Copier-coller depuis navigateur

Marre d’avoir tout votre texte décalé plein de tabulations quand 
vous copier-collez à la souris dans vim : here is the solution
Une commande à taper avant de copier-coller et le tour est joué

    set paste

Prenez soin de taper

    set nopaste

ensuite car l’option paste invalide pas mal de choses. À ne pas mettre dans le vimrc, donc.

*Autre méthode*

Turn off auto-indent when pasting text
Type in:

    :set pastetoggle=<F3>

Now you can use <F3> to toggle between paste mode (and no paste mode).

When in paste-mode auto indent will be turned off. This is very useful when pasting text that's already indented.

More info in http://www.vim.org/tips/tip.php?tip_id=330


#Don't repeat yourself - record your actions

To start recording, press qa in the normal mode, this will save your recording in the a register. 
Now do your actions. After you are done, stop recording by issuing q in normal mode.

To replay your recording issue @a in normal mode.

This is really useful when doing some complex repeating tasks.

More info in http://www.vim.org/tips/tip.php?tip_id=144


#Fonction d'enregistrement (record)

Pour répéter des commandes complexes...

Exemple :
vous avez un fichier avec ça :

    phil
    bob
    claudel

Et vous voulez obtenir ça :

    printf("phil");
    printf("bob");
    printf("claudel");

Le mode d'édition en colonne pourrait être rapide, mais il y a encore plus rapide... (imaginez que vous avez 100 lignes)

Donc (depuis le mode normal), vous entrez en fonction record avec qq ensuite faites votre opération sur une ligne Iprintf("<esc>A");<esc>j (ce qui veut dire en langage vim :
Inserer en debut de ligne I le mot printf(", revenir en mode normal <esc>, inserer en fin de ligne A le mot ";, revenir en mode normal <esc>, aller une ligne en dessous j.

Ensuite quittez la fonction record avec q. Et ensuite faites @q en mode normal sur toutes les autres lignes... \o/ et voilà le travail.


Maintenant imaginez que vous avez 100 lignes, un simple 100@q et c'est fait, en tout on a tapé 16 touches.

EDIT : ceci n'est qu'une courte présentation de la fonction record, vous pouvez faire beaucoup plus, comme enregistrer plusieurs suites de commandes etc :help recording

@q : dernier enregistrement (enregistré, pas exécuté)
@@ : dernier enregistrement exécuté.
....

Vous pouvez même faire un enregistrement puis l'exécuter récursivement sur tout le fichier...
ggqqIprintf("<esc>A");<esc>j@@q@@ (Okay, ça servira peut être qu'une fois, mais quand même tongue )

oui c'est pas mal, mais dans ce cas précis, y'a mieux

    :%s/\(^.*$\)/printf("\1");

Ou encore plus simplifié dans ce cas précis:

    :%s/.*/printf("&");

cela dit pour éditer de façon similaire des paragraphes entiers (remise en forme par exemple), les macros, sont pratiques


#INTERESSANTS


- http://www.8t8.us/vim/vim.html
- http://forum.ubuntu-fr.org/viewtopic.php?id=132970

ctrl+n que avec vim-multiple-cursor

#Tabularize align everything

-->
