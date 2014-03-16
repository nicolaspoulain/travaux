import sys
import pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()
print(ballrect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # Limit to 60 frames per second
    clock.tick(60)

    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()
