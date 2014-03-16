from pygame import display
from random import randint
scr = display.set_mode((500,500))
p = frozenset((randint(200,300),randint(200,300))for foo in range(1500))

while 1:
    q = {}
    for j,k in p:
        for x,y in ((-1,1),(0, 1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)):
            i = (j+x),(k+y)
            q[i] = q.setdefault(i,0)+1
    scr.fill(0)
    p = frozenset(scr.set_at(i,0xffffff)or i for i,j in q.items() if j == 3 or (i in p and j == 2))
    display.flip()
