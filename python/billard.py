
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
    def __init__(self, (x,y), size, date_of_death):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 0
        self.dod = date_of_death

    def display(self):
       pygame.draw.circle(screen, self.colour, \
               (self.x, self.y), self.size, self.thickness)

    def move(self):
        if self.x < self.size:
            minx = 0
        else: minx = -2
        if self.x > width - self.size:
            maxx = 0
        else: maxx = 2
        if self.y < self.size:
            miny = 0
        else : miny = -2
        if self.y > height - self.size:
            maxy = 0
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
    size = random.randint(7,15)
    x = random.randint(size, width - size)
    y = random.randint(size, height - size)
    dod = pygame.time.get_ticks() + 10 * random.randint(50,255)
    particle = Particle((x, y), size, dod)
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

