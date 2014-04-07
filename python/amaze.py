#!/usr/bin/python
# -*- coding: utf8 -*-

import pygame
import random
import math
import numpy

(nb_cols, nb_rows) = (20,15)
k_zoom = 20
wall_color = (255,255,255)

(width, height) = (nb_cols * k_zoom + 1 , nb_rows * k_zoom + 1)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Amaze')

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def allequal(m):
  for i in range(nb_rows):
    for j in range(nb_cols):
      if m[i][j] != m[0][0]:
        return 0
  return 1

h_wall = numpy.random.randint(1,2, size=(nb_rows,nb_cols))
for i in range(nb_cols):
    h_wall[0][i] = 1
v_wall = numpy.random.randint(1,2, size=(nb_rows,nb_cols))
for i in range(nb_rows):
    v_wall[i][0] = 1

cells =[]
for i in range(nb_rows):
    cells.append([j+1 for j in range(i*nb_cols, (i+1)*nb_cols)])

#for n in range(42):
while not(allequal(cells)):
  ## Choisit une cellue au hasard
    (i,j) = (random.randint(0, nb_rows-1), random.randint(0, nb_cols-1))
    ## Choisit une cellule adjacente au hasard
    possible = []
    if i>0 and cells[i][j] != cells[i-1][j]:
        possible.append((i-1,j))
    if i<nb_rows-1 and cells[i][j] != cells[i+1][j]:
        possible.append((i+1,j))
    if j>0 and cells[i][j] != cells[i][j-1]:
        possible.append((i,j-1))
    if j<nb_cols-1 and cells[i][j] != cells[i][j+1]:
        possible.append((i,j+1))

    if len(possible)>0 :
      (k,l) = random.choice(possible)
      ## Fusionne les cellles
      afus = cells[k][l]
      for ii in range(nb_rows):
        for jj in range(nb_cols):
          if cells[ii][jj] == afus:
            cells[ii][jj] = cells[i][j]
      ## Élimine le mur correspondant
      ## Mur horizontal
      if i-k == 0:
          v_wall[i][1+(j+l)/2] = 0
      ## Mur vertical
      else:
          h_wall[1+(i+k)/2][j] = 0
    screen.fill(0)
    # Limit to 100 frames per second
    #clock.tick(100)
    for i in range(nb_cols):
        for j in range(nb_rows):
            A = (i * k_zoom, j * k_zoom )
            B = (i * k_zoom, j * k_zoom + k_zoom)
            if (v_wall[j][i] == 1):
                pygame.draw.line(screen, (255,255,255), A, B)
            A = (i * k_zoom , j * k_zoom)
            B = (i * k_zoom + k_zoom, j * k_zoom)
            if (h_wall[j][i] == 1):
                pygame.draw.line(screen, (255,255,255), A, B)
    pygame.draw.line(screen, (255,255,255), (nb_cols*k_zoom,0), (nb_cols*k_zoom,nb_rows*k_zoom))
    pygame.draw.line(screen, (255,255,255), (0,nb_rows*k_zoom), (nb_cols*k_zoom,nb_rows*k_zoom))
    pygame.display.flip()

print v_wall
print h_wall
running = True
#running = False
while running:
    #running = False
    for i in range(nb_cols):
        for j in range(nb_rows):
            a = (i * k_zoom, j * k_zoom )
            b = (i * k_zoom, j * k_zoom + k_zoom)
            if (v_wall[j][i] == 1):
                pygame.draw.line(screen, (255,255,255), a, b)
            a = (i * k_zoom , j * k_zoom)
            b = (i * k_zoom + k_zoom, j * k_zoom)
            if (h_wall[j][i] == 1):
                pygame.draw.line(screen, (255,255,255), a, b)
    pygame.draw.line(screen, (255,255,255), (nb_cols*k_zoom,0), (nb_cols*k_zoom,nb_rows*k_zoom))
    pygame.draw.line(screen, (255,255,255), (0,nb_rows*k_zoom), (nb_cols*k_zoom,nb_rows*k_zoom))
    pygame.display.flip()



