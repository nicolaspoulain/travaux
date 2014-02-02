http://extensions.services.openoffice.org/en/project/writer2latex

Ouvrir fichier odt

Fichier Exporter LateX2e 

Convertit en md

Si on a choisi UTF8

    $ pandoc exos.tex -o exos.mdconv

Si on a choisi ISO-8859

    $ iconv -f ISO-8859-1 exos.tex | pandoc -f latex -o exos.md



    >>> execfile('process.py')
