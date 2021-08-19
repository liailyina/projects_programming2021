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

# Window
rect(screen, DOUBLE_LIGHT_BLUE, (220, 15, 160, 160))
rect(screen, VERY_LIGHT_BLUE, (220, 10, 160, 15))
rect(screen, VERY_LIGHT_BLUE, (220, 10, 15, 165))
rect(screen, VERY_LIGHT_BLUE, (220, 170, 160, 15))
rect(screen, VERY_LIGHT_BLUE, (365, 10, 15, 165))
rect(screen, VERY_LIGHT_BLUE, (295, 10, 15, 165))
rect(screen, VERY_LIGHT_BLUE, (220, 50,160, 15))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
