import pygame
from pygame.draw import *
from colours import *
import sys

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

# Background
rect(screen, COFFEE_BROWN, (1, 1, 399, 399))
rect(screen, BROWN, (1, 1, 399, 190))






pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
