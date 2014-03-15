% Vim Memo
% NPO
% Janvier 2014

#Vim Memo

 |                            | MOVE TO...                                     |
 | :------------------------- | :--------------------------------------------- |
 | `h j k l`                  | Left, down, up, right                          |
 | `0 £ ^`                    | Start, end of line - first nonBlank char       |
 | `w e`                      | Start, end of word                             |
 | `gg G`                     | First, last line of file                       |
 | `Ctrl-d Ctrl-u`            | Half page down, up                             |
 | `Ctrl-b Ctrl-f`            | Page down, up                                  |

 |                            | RECHERCHE                                      |
 | :------------------------- | :--------------------------------------------- |
 | `*`                        | Recherche pour le mot exact sous le curseur    |
 | `g*`                       | Recherche pour le mot partiel sous le curseur  |
 | `[I`                       | Affiche lignes contenant mot sous le curseur   |
 | `:g/foo`                   | Affiche les lignes contenant foo               |
 | `:g/foo/d`                 | supprime les lignes contenant chaîne foo       |
 | `:v/foo/d`                 | supprime lignes ne contenant pas foo           |
 | `:g/^[\.]*$/d`             | supprime les lignes vides                      |

 |                            | SPLIT ET RESIZE                                |
 | :------------------------- | :--------------------------------------------- |
 | `:res 60`                  | Définit la hauteur de la fenêtre               |
 | `:vertical resize 80`      | Définit la largeur de la fenêtre               |
 | `:res {+,-}10`             | Augmente/réduit la hauteur de la fenêtre       |
 | `10 Ctrl-w {+,-}`          | "" idem                                        |
 | `:vertical resize {+,-}10` | Augmente/réduit la largeur de la fenêtre       |
 | `10 Ctrl-w {>,<}`          | " " idem                                       |
 | `Ctrl-w =`                 | Égalise la taille des fenêtres                 |
 | `Ctrl-w _`                 | Augment au maximum la taille de la fenêtre     |
 | `Ctrl-w s`                 | Partage la fenêtre courante en deux            |
 | `Ctrl-w H`  `Ctrl-w L`     | Place la fenêtre courante à gauche /à droite   |
 | `Ctrl-w J`  `Ctrl-w K`     | Place la fenêtre courante en haut /en bas [^3] |

 |                            | BUFFERS  (better with bufferline)              |
 | :------------------------- | :--------------------------------------------- |
 | `:e newFile`               | ouvre un nouveau buffer avec newFile           |
 | `:ls`                      | pareil que :buffers, mais en plus court        |
 | `:bw`                      | ferme le buffer courant                        |
 | `:sb x` `vsp | bx`         | place le buffer x dans une fenêtre splitée     |
 | `:bn :bp`   maped to F2 F3 | Opens next, previous buffer                    |

 |                            | REMPLACEMENT ET SUPPRESSIONS                   |
 | :------------------------- | :--------------------------------------------- |
 | `:s/foo/bar/`              | remplace le 1er foo de ligne courante par bar  |
 | `:s/foo/bar/g`             | remplace tous foo de ligne courante par bar    |
 | `:%s/foo/bar/`             | remplace TOUS foo du fichier par bar           |
 | `:%s/foo/bar/g`            | remplace TOUS foo du fichier par bar           |
 | `:%s/foo/bar/gc`           | " " idem avec demande de confirmation          |
 | `:%s/.*\zsfoo/bar/`        | remplace dernière occurence de "foo" par "bar" |
 | `:%s/\<foo\>//g`           | Supprime "foo".                                |
 | `:%s/.*\<foo\>//`          | Supprime "foo" et tout ce qui le précède.      |
 | `:%s/\<foo\>.*//`          | Supprime "foo" et tout ce qui le suit.         |
 | `:%s/.*\ze\<foo\>//`       | Supprime tout ce qui précède le mot "foo"      |
 | `:%s/\<foo\>\zs.*//`       | Supprime tout ce qui suit le mot "foo"         |
 | `:%s/.*\(\<foo\>\).*/\1/`  | Supprime tout ce qui entoure le mot "foo"      |
 | `:%s/\<foo\>.\{5}//`       | Supprime "foo" et les 5 catactères qui suivent |
 | `:%s/\s\+$//`              | Supprime les espaces de fin de ligne[^5]       |
 | `:s/.*/\U&/`               | passe la ligne courante en majuscule           |
 | `:%s/^foo//`               | Supprime TOUS les foo placés en début de ligne |

                  |        | ANCHORS                            |
                  | ^      | start of line                      |
                  | $      | end of line                        |
                  | \<     | beginning of a word                |
                  | \>     | end of a word                      |
                  | `[ ]`  | any characters listet              |
                  | `[^ ]` | any characters except those listet |

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

                  |            | REPLACEMENT                                 |
                  | `& `       | the whole matched pattern                   |
                  | `\0`       | the whole matched pattern                   |
                  | `\1 \2...` | matches text in 1st, 2nd ... pair of `\(\)` |
                  | `~ `       | the previous substitute string              |
                  | `\L` `\U`  | make lowercase / uppercase                  |
                  | `\l` `\u`  | next character made lowercase / uppercase   |
                  | `\E`       | end of \U and \L                            |
                  | `\r`       | split line in two at this point             |

 |                            | SELECTION DE BLOC TEXTE                        |
 | :------------------------- | :--------------------------------------------- |
 | `v       lljj`             | selection de texte                             |
 | `Shift-v jj`               | selection de lignes entières                   |
 | `Ctrl-v  lljj`             | selection de colonnes                          |
 | `gv`                       | Resélectionne le bloc                          |
 | `h j k l' , `D`            | *DRAGVISUAL*:    déplace bloc, duplique        |

 |                            | INSERTION SUR PLUSIEURS LIGNES                 |
 | :------------------------- | :--------------------------------------------- |
 | `Ctrl-v jj $ A foo Esc`    | Insertion à la fin des lignes d'un bloc        |
 | `Ctrl-v jj I foo Esc`      | Insertion dans une colonne d'un bloc           |
 | `Ctrl-v jj I # Esc`        | Commente les lignes d'un bloc                  |
 | `Shift-v jj s/^/#`         | Commente les lignes d'un bloc (autre méthode)  |

 |                            | INDENTATION, AUTOINDENTATION ET *TABULARIZE*   |
 | :------------------------- | :--------------------------------------------- |
 | `>>` `<<`                  | Indente ou desindente la ligne courante
 | `gg=G`                     | Si marche pas, set `ft=html` + `set si`[^6]    |
 | `Shift-v =`                | Indente un bloc                                |
 | `==`                       | indente la ligne courante                      |
 | `:Tabularize /:`           | aligns statements on :                         |
 | `:Tabularize /&&`          | aligns statements on &&                        |

 |                            | REGISTRES                                      |
 | :------------------------- | :--------------------------------------------- |
 | `"5yy"` `"hyy`             | Copie la ligne dans le registre 5 (ou h)       |
 | `:reg`                     | Liste les registres                            |
 | `"5p`  `"hp`               | Colle le contenu du regsitre 5 (ou h)          |

 |                            | FOLDING COMMANDS [^1]                          |
 | :------------------------- | :--------------------------------------------- |
 | `za`                       | Toggle state of one fold (`zA` recurs [^2])    |
 | `zR`                       | Opens ALL folds (`zr` decr foldlevel by 1)     |
 | `zM`                       | Closes ALL folds (`zM` incr foldlevel by 1)    |
 | `zf%`                      | creates fold from a delimitor to its brother   |
 | `V jj zf`                  | creates fold from visual block                 |
 | `zf#j`                     | creates fold from the cursor down # lines      |
 | `zf/string`                | creates fold from the cursor to string         |
 | `zj` `zk`                  | moves the cursor to the next, previous fold    |
 | `zd` `zE`                  | deletes the fold at the cursor, ALL folds      |
 | `[z` `]z`                  | move to start/ end of open fold                |

 |                            | DIVERS                                         |
 | :------------------------- | :--------------------------------------------- |
 | `:set paste`               | Avant de coller depuis le navigateur           |
 | `:set nopaste`             | Après avoir collé depuis le navigateur [^7]    |
 | `:sort [n]`                | Trier sur première colonne [numérique] [^10]   |
 | `:%!sort -n -k 3           |     à l'aide de gnu sort                       |
 | `qa` ... `qz`              | Démarre enregistrement action (registre a...z) |
 | `q`                        | stopppe enregistrement action [^8]             |
 | `[6]@a`                    | joue 6x enregistrement action (registre a...z) |

 |                            | PLUGINS                                        |
 | :------------------------- | :--------------------------------------------- |
 | `<leader><leader>w`        | *EASYMOTION*                                   |
 | `<leader>gs`               | *FUGITIVE* :Gstatus `-`un/stage, `cc`commt msg |

 |                            | TAGS and *SURROUND*                            |
 | :------------------------- | :--------------------------------------------- |
 | `S<h3>`                    | Add Surround to visual sélection               |
 | `{d,y,v}it`                | deletes, yanks or visual Inside Tags           |
 | `{d,y,v}at`                | deletes, yanks or visual Around Tags           |
 | `cst<h3>`                  | Change Surrounding Tag (current) to <h3>       |
 | `cs">` `cs"<h3>`           | Change Surrounding " to  <..> / <h3></h3>      |
 | `ds"`                      | Delete le surround "                           |

[^1]:  Dans le .vimrc `:mkview    " save folds` & `:lowercaseadview  " restore folds`
[^2]: za (resp. zA) toggles between zo & zc (resp. zO & zC)
[^3]: The lower case equivalents move focus instead of moving the window.
[^5]: In a search, `\s` finds whitespace (a space or a tab), and `\+` finds one or more occurrences.
[^6]: donner le bon le filetype et enclancher le smartindent
[^7]: More info in http://www.vim.org/tips/tip.php?tip_id=330 *Autre méthode* :set pastetoggle=<F3>

