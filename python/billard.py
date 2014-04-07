#!/usr/bin/python
# -*- coding: utf8 -*-

# http://www.petercollingridge.co.uk/pygame-physics-simulation/movement

import pygame
import random
import math

(width, height) = (300, 200)
bg_color = (255,255,255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jeu de billard')

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


class Particle:
    
    ## Donne naissance à une cellule.
    #  Sont définies : position , taille, couleur, date de mort.
    def __init__(self, world_width, world_height):
        self.size = random.randint(2,8)
        self.x = random.randint(self.size, world_width - self.size)
        self.y = random.randint(self.size, world_height - self.size)
        self.colour = (0, 0, 255)
        self.thickness = 0
        # Date Of Death
        self.dod = pygame.time.get_ticks() + 10 * random.randint(50,255)

    def display(self):
       pygame.draw.circle(screen, self.colour, \
               (self.x, self.y), self.size, self.thickness)

    def move(self):
        if self.x < self.size: minx = 0
        else: minx = -2
        if self.x > width - self.size: maxx = 0
        else: maxx = 2
        if self.y < self.size: miny = 0
        else : miny = -2
        if self.y > height - self.size: maxy = 0
        else : maxy = 2
        self.x += random.randint(minx,maxx)
        self.y += random.randint(miny,maxy)

def dist(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.hypot(dx, dy)

def collide(p1, p2):
    return dist(p1, p2) < p1.size + p2.size
        
nb_particles = 10
my_particles = []

for n in range(nb_particles):
    particle = Particle(width, height)
    my_particles.append(particle)

running = True
while running:

    # Limit to 60 frames per second
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
    screen.fill(bg_color)
    for i, p1 in enumerate(my_particles):
        p1.move()
        for p2 in my_particles[i+1:]:
            if collide(p1, p2):
                d1 = dist(p1, p2)
                d2 = p1.size + p2.size
                p1.x = p2.x + int(d2*(p1.x - p2.x)/d1)
                p1.y = p2.y + int(d2*(p1.y - p2.y)/d1)
        p1.display()
        if pygame.time.get_ticks() > p1.dod:
            my_particles.pop(i)
    pygame.display.flip()

pygame.quit()

