#!/usr/bin/python
# -*- coding: utf8 -*-

from pygame import display
from random import randint

# initialise le monde
scr = display.set_mode((500,500))
# peuple le monde
p = set( (randint(200,300),randint(200,300))for foo in range(1500) )

while 1:
    q = {}
    for j,k in p:
        for x,y in ((-1,1),(0, 1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)):
            i = (j+x),(k+y)
            # q va contenir ile nb de voisins 
            # pour tous les voisins de cellules vivantes
            q[i] = q.setdefault(i,0)+1
    # Nettoyage écran
    scr.fill(0)
    # Astuce « scr.set_at(i,0xffffff) or i » pour faire en un coup le scr.set_at
    # et l'insertion du i dans le set
    p = set (scr.set_at(i,0xffffff) or i for i,j in q.items() if j == 3 or (i in p and j == 2) )
    display.flip()
