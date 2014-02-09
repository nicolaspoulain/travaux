#!/usr/bin/python
# -*- coding: utf8 -*-


class Cell(object):
    """
    Modélise une cellule
    Son identité est donnée par sa position (x,y)
    dans le monde
    """

    def __init__(self, x, y, act_state):
        """
        Définit la cellule (x,y)
        Son état actuel 0 pour morte, 1 pour vivante
        Son état futur  0 pour morte, 1 pour vivante
        """
        self.position = Position(x, y)
        self.act_state = act_state


class Position(object):
    """
    Modélise une position dans un monde
    torique et discret en deux dimensions dim_x * dim_y
    """

    def __init__(self, x, y):
        """
        Constructeur de Position
        x : Abscisse
        y : Ordonnée
        """
        self.x = x
        self.y = y

    def getX(self, dim_x=10):
        """
        Retourne l'abscisse corrigée

        >>> p = Position(18,22)
        >>> print(str(p.getX()))
        8
        """
        return self.x % dim_x

    def getY(self, dim_y=8):
        """
        Retourne l'ordonnée corrigée

        >>> p = Position(18,22)
        >>> print(str(p.getY()))
        6
        """
        return self.y % dim_y


"Les dimensions du monde"
dim_x = 10
dim_y = 8

"Initialisation d'un monde désert"
cell = [[0 for x in xrange(dim_y)] for x in xrange(dim_x)]
for x in xrange(dim_x):
    for y in xrange(dim_y):
        cell[x][y] = Cell(x, y, 0)

"Donne la vie à quelques cellules dans le monde"
cell[2][3] = Cell(2, 3, 1)
cell[2][4] = Cell(2, 4, 1)
cell[3][5] = Cell(3, 5, 1)
cell[1][5] = Cell(1, 5, 1)

import time

for cycle in range(100):
    for x in xrange(dim_x):
        row = ""
        for y in xrange(dim_y):
            p1 = Position(x - 1, y - 1)
            p2 = Position(x - 1, y)
            p3 = Position(x - 1, y + 1)
            p4 = Position(x, y + 1)
            p5 = Position(x + 1, y + 1)
            p6 = Position(x + 1, y)
            p7 = Position(x + 1, y - 1)
            p8 = Position(x, y - 1)
            c = cell[p1.getX()][p1.getY()].act_state
            c += cell[p2.getX()][p2.getY()].act_state
            c += cell[p3.getX()][p3.getY()].act_state
            c += cell[p4.getX()][p4.getY()].act_state
            c += cell[p5.getX()][p5.getY()].act_state
            c += cell[p6.getX()][p6.getY()].act_state
            c += cell[p7.getX()][p7.getY()].act_state
            c += cell[p8.getX()][p8.getY()].act_state

            if cell[x][y].act_state == 0 and c == 3:
                row += "o"
            elif cell[x][y].act_state == 1 and (c == 2 or c == 3):
                row += "o"
            else:
                row += "."
        print row
    for x in xrange(dim_x):
        row = ""
        for y in xrange(dim_y):
            pass
    time.sleep(0.2)
    print

if __name__ == "__main__":
    import doctest
    doctest.testmod()
