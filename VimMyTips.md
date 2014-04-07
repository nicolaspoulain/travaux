// vim:ft=txt

                           | ENTERING INSERT MODE
 ------------------------- | ---------------------------------------------
 i , I                     | Insert text before cursor (I is ^i)
 a , A                     | Append text after  cursor (A is $A)
 o , O                     | insert a new line after, before current line
 R , r{char}               | Replace instead of insert (r is for one char)
 c{motion} , cw , C        | Change ie delete and start insert (C is c$)
 s                         | Substitute char on cursor (s is cl)
 
                           | MOTIONS
 ------------------------- | ---------------------------------------------
 h , j , k , l             | left, down, up, right
 0 , $ , ^                 | start, end of line , first non blank char
 w , e                     | start of next Word, End of word
 b , ge                    | start of prev Word, End of prev word
 t{char} , f{char}         | move For,To next(maj:prev) {char} (Repeat ;,)
 /{ptrn} , ?{ptrn}         | Search for next, previous {ptrn} (Repeat n)
 gg , G                    | First line of file, last line of file
 ,,w   ,   ,,b             | Start of word forward, backward *EASYMOTION*
 ,,e   ,   ,,ge            | End   of word forward, backward *EASYMOTION* 
 ------------------------- | ---------------------------------------------
 <C-f> , <C-b>             | One  page down, up
 <C-d> , <C-u>             | Half page down, up
 '.                        | Jump to last modification line

                           | SPLIT ET RESIZE
 ------------------------- | ---------------------------------------------
  <C-w> =                  | Equalize width and height of all windows
  <C-w>_   ,  <C-w>|       | Maximize height, width of the active window
 9<C-w>_   , 9<C-w>|       | Set active window height, width to 9 units
 9<C-w> +- , 9<C-w> ><     | In/Dec-rease window 9 units height, width 
  <C-w>H   , <C-w>L        | Place la fenêtre courante à gauche /à droite
  <C-w>J   , <C-w>K        | Place la fenêtre courante en haut /en bas [^3]

                           | BUFFERS (better with *BUFFERLINE*)
 ------------------------- | ---------------------------------------------
 :e. , :Vex , Sex(plore)   | File explorer in new window, in split window 
 :e myFile                 | Ouvre un nouveau buffer avec myFile
 :ls                       | Pareil que :buffers, mais en plus court
 :bw                       | Ferme le buffer courant
 :sb x , vsp | bx          | Place le buffer x dans une fenêtre (v)splitée
 :sball                    | Split all buffers
 :bn , :bp                 | Next, previous buffer (maped to F2 F3)

                           | RECHERCHE, REMPLACEMENT ET SUPPRESSIONS
 ------------------------- | ---------------------------------------------
 * , g*                    | Recherche mot exact/partiel sous le curseur
 %                         | Match brackets {}[]()
 [I                        | Affiche lignes contenant mot sous le curseur
 :g/foo                    | Affiche les lignes contenant foo
 :g/foo/d                  | Supprime les lignes contenant chaîne foo
 :v/foo/d                  | Supprime lignes ne contenant pas foo
 :%s/\s\+$//               | Supprime les espaces de fin de ligne
 :g/^[\.]*$/d              | Supprime les lignes vides
 :s/foo/bar/               | Remplace le 1er  foo de ligne courante par bar
 :s/.*\zsfoo/bar/          | Remplace dernier foo de ligne courante par bar
 :s/foo/bar/g              | Remplace tous foo de ligne courante par bar
 :%s/foo/bar/g             | Remplace TOUS foo du fichier par bar
 :%s/foo/bar/gc            | " " idem avec demande de confirmation
 :%s/\<foo\>//g            | Supprime le mot "foo".
 :%s/.*\<foo\>//           | Supprime "foo" et tout ce qui le précède.
 :%s/\<foo\>.*//           | Supprime "foo" et tout ce qui le suit.
 :%s/.*\ze\<foo\>//        | Supprime tout ce qui précède le mot "foo"
 :%s/\<foo\>\zs.*//        | Supprime tout ce qui suit le mot "foo"
 :%s/\<foo\>.\{5}//        | Supprime "foo" et les 5 catactères qui suivent
 :%s#<\_.\{-1,}>##g        | Delete html tags possibly multi-line
 :%s/<!--\_p\{-}-->//g     | Delete multiple line comments
 Vu , VU                   | Lowercase line, uppercase line 
 ggguG                     | lowercase entire file
 :& , :~                   | Repeat last substitute
 g%                        | Normal mode repeat last substitute

     |         | --- ANCHORS ----
     | ^   $   | Start/end of line
     | \<  \>  | Beginning/end of a word
     | [ ]     | Any characters listet
     | [^ ]    | Any characters except those listet

     |                   | ---- METACARACTÈRES ---
     |  .                | Any character except newline
     | \d                | Digit character [0-9]
     | \a                | Alphabetic character [A-Za-z]
     | \w                | Word character [0-9A-Za-z_]
     | \l , \u           | Lowercase, uppercase  character
     | \p                | Printable character
     | \s                | Whitespace character
     | \_\x              | Any character of class x, including newline
     | Greedy : ^Greedy  | Quantifier
     | *      : \{-}     | 0 ou plus
     | \+     : \{-1}    | 1 ou plus
     | \=     : \{-0,1}  | 0 ou 1 fois
     | \{n}   :          | n fois exactement
     | \{n,}  : \{-n,}   | n fois au moins
     | \{,m}  : \{-,m}   | m fois au plus
     | \{n,m} : \{-n,m}  | Entre n et m fois

     |          | ---- REPLACEMENT ----
     | &        | The whole matched pattern
     | \1 \2... | Matches text in 1st, 2nd ... pair of \(\)
     | \l  \u   | Next char  made lowercase / uppercase
     | \L  \U   | Next charS made lowercase / uppercase       |
     | \E       | End of \u and \l

                           | SELECTION DE BLOC TEXTE
 ------------------------- | ---------------------------------------------
 v , <C-v>                 | Selection de texte/ de colonne
 V                         | Selection de lignes entières
 gv                        | Resélectionne le bloc précédemment défini
 h j k l' , D              | *DRAGVISUAL*:    déplace bloc, duplique
 gq                        | Formate la sélection
 :%s/\%Vold/new/g          | Do a substitute on last visual area

                           | INSERTION SUR PLUSIEURS LIGNES
 ------------------------- | ---------------------------------------------
 <C-v> jj $ A foo Esc      | Insertion à la fin des lignes d'un bloc
 <C-v> jj I foo Esc        | Insertion dans une colonne d'un bloc
 <C-v> jj I # Esc          | Commente les lignes d'un bloc
 V jj s/^/#                | Commente les lignes d'un bloc (autre méthode)

                           | INDENTATION, AUTOINDENTATION
 ------------------------- | ---------------------------------------------
 >> , <<                   | Shift right, shift left
 gg=G                      | Si marche pas, set ft=html  + set si [^6]
 == , =                    | AutoIndent current line, current block
 :Tabularize /x            | Aligns statements on char x: (*TABULARIZE*)

                           | REGISTRES
 ------------------------- | ---------------------------------------------
 "5yy" , "hyy              | Copie la ligne dans le registre 5 (ou h)
 :reg                      | Liste les registres
 "5p , "hp , i<C-r>h       | Colle le contenu du regsitre 5 (ou h)
 "_dd                      | Delete to BlackHole don't affect any register

                           | FOLDING COMMANDS [^1]
 ------------------------- | ---------------------------------------------
 za                        | Toggle state of one fold ( zA  recurs [^2])
 zR                        | Opens ALL folds ( zr  decr foldlevel by 1)
 zM                        | Closes ALL folds ( zM  incr foldlevel by 1)
 zf%                       | Creates fold from a delimitor to its brother
 V jj zf                   | Creates fold from visual block
 zj , zk                   | Move to the next, previous fold
 [z , ]z                   | Move to start/ end of open fold

                           | RECORDING
 ------------------------- | ---------------------------------------------
 qa  ,..., qz              | Démarre enregistrement action (registre a...z)
 q                         | Stopppe enregistrement action [^8]
 @a  @z                    | Joue  l'enregistrement action (registre a...z)
 6@a                       | Joue 6x enregistrement action
 @@                        | Rejoue le dernier enregistrement
 6@@                       | Rejoue 6x le dernier enregistrement
 "ap  <C-R>a               | Affiche enregistrement normal/insert mode
 "add                      | Réenregistre action dans le registre a

                           | DIVERS
 ------------------------- | ---------------------------------------------
 .                         | Repeat last modification
 @:                        | Repeat last : command (then @@)
 :history                  | List of all your commands
 <C-X><C-L>                | Line complete SUPER USEFUL
 /<C-R><C-W>               | Pull <cword> onto search/command line
 ga , g8                   | Display hex value of char under cursor
 :digraphs  ga             | Display table of utf8 chars
 i<C-v>233                 | Insert é
 <C-a> , 9<C-x>            | Increment,decrement first number after cursor
 :set paste                | Avant de coller depuis le navigateur
 :set nopaste              | Après avoir collé depuis le navigateur [^7]
 :sort [n]                 | Trier sur première colonne [numéric]
 :%!sort -t';' -k3 [-n]    | Sort column 3 of coma separated [numeric]

                           | PLUGINS
 ------------------------- | ---------------------------------------------
 <leader>gs                | *FUGITIVE* :Gstatus - un/stage, cc commt msg
 :TagbarToggle             | *TAGBAR* (maped to F8)

                           | TAGS and *SURROUND*
 ------------------------- | ---------------------------------------------
!/  a< |  a"  |\ at     !  | Around (or All) the delimitor
 <p id= " xy " > ab </p>   |    example 
  \ i<   |i"|/  |it|       | Inside the delimitor (t for a pair of tags)
cst<i>                     | <p>abc</p> to <i>abc</i>  *SURROUND*
dst                        | <p>abc</p> to abc         *SURROUND*
V S"                       | abc to "abc"              *SURROUND*
cs")                       | "abc" to (abc)            *SURROUND* 
cs)<p>                     | (abc) to <p>abc</p>       *SURROUND*

[^1]:  Dans le .vimrc :mkview    " save folds  & :lowercaseadview  " restore folds
[^2]: za (resp. zA) toggles between zo & zc (resp. zO & zC)
[^3]: The lower case equivalents move focus instead of moving the window.
[^6]: donner le bon le filetype et enclancher le smartindent
[^7]: More info in http://www.vim.org/tips/tip.php?tip_id=330
           *Autre méthode* :set pastetoggle=<F3>

