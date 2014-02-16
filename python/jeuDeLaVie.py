#!/usr/bin/python
# -*- coding: utf8 -*-


class Cell(object):
    """ An organic cell. Id given by (x,y) position in the worlsModélise """

    def __init__(self, x, y, act_state, ftr_state):
        """
        Defines the (x,y) cell
        Its actual state is 0:dead or 1:alive
        Its future state is 0:dead or 1:alive
        """
        self.position = Position(x, y)
        self.act_state = act_state
        self.ftr_state = ftr_state


class Position(object):
    """ Position in a toric matrix world dim_x * dim_y """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self, dim_x=10):
        """
        Return x coordinate in tore
        e.g. if dim_x=10, x=18 equiv. x=8
        >>> p = Position(18,22)
        >>> print(str(p.getX(10)))
        8
        """
        return self.x % dim_x

    def getY(self, dim_y=8):
        """
        Return y coordinate in tore
        e.g. if dim_y)=8, y=22 equiv. y=6
        >>> p = Position(18,22)
        >>> print(str(p.getY(8)))
        6
        """
        return self.y % dim_y


"Les dimensions du monde"
dim_x = 10
dim_y = 20

"Initialisation d'un monde désert"
cell = [[0 for x in xrange(dim_y)] for x in xrange(dim_x)]
for x in xrange(dim_x):
    for y in xrange(dim_y):
        cell[x][y] = Cell(x, y, 0, 0)

"Donne la vie à quelques cellules dans le monde"
cell[1][1] = Cell(1, 1, 1, 0)
cell[2][1] = Cell(2, 1, 1, 0)
cell[3][1] = Cell(3, 1, 1, 0)
cell[3][2] = Cell(3, 2, 1, 0)
cell[2][3] = Cell(2, 3, 1, 0)

"pour un affichage raisonnablement temporisé"
import curses
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

while True:
    event = screen.getch()
    """
    On parcourt le monde pour déterminer l'état futur de chaque cellule
    et l'afficher sur une grille sous forme de . et de o
    """
    for x in xrange(dim_x):
        "row va servir pour l'affichage du monde"
        row = ""
        for y in xrange(dim_y):
            """
            On définit les positions des 8 cellules qui entourent
            la cellule courante.
            """
            p1 = Position(x - 1, y - 1)
            p2 = Position(x - 1, y)
            p3 = Position(x - 1, y + 1)
            p4 = Position(x, y + 1)
            p5 = Position(x + 1, y + 1)
            p6 = Position(x + 1, y)
            p7 = Position(x + 1, y - 1)
            p8 = Position(x, y - 1)
            """
            On calcule le nombre de cellules en contact avec
            la cellule courante
            """
            c = cell[p1.getX(dim_x)][p1.getY(dim_y)].act_state
            c += cell[p2.getX(dim_x)][p2.getY(dim_y)].act_state
            c += cell[p3.getX(dim_x)][p3.getY(dim_y)].act_state
            c += cell[p4.getX(dim_x)][p4.getY(dim_y)].act_state
            c += cell[p5.getX(dim_x)][p5.getY(dim_y)].act_state
            c += cell[p6.getX(dim_x)][p6.getY(dim_y)].act_state
            c += cell[p7.getX(dim_x)][p7.getY(dim_y)].act_state
            c += cell[p8.getX(dim_x)][p8.getY(dim_y)].act_state
            if cell[x][y].act_state == 0 and c == 3:
                """ If cell is dead and has 3 neighbours, it births """
                cell[x][y].ftr_state = 1
            elif cell[x][y].act_state == 1 and (c == 2 or c == 3):
                """ If cell is alive and has 2 or 3 neighbours, it survives """
                cell[x][y].ftr_state = 1
            else:
                """ In all othe cases, it dies or stays dead """
                cell[x][y].ftr_state = 0
            """Affichage"""
            if cell[x][y].act_state == 1:
                row += "o"
            else:
                row += "."
        if x == 0:
            screen.clear()
        screen.addstr(row)
        screen.addstr("\n")
    """
    On parcourt le monde pour incrémenter le temps en
    remplaçant affectant l'état futur à l'état présent
    """
    for x in xrange(dim_x):
        for y in xrange(dim_y):
            cell[x][y].act_state = cell[x][y].ftr_state
    #time.sleep(2)
    #print

if __name__ == "__main__":
    import doctest
    doctest.testmod()
