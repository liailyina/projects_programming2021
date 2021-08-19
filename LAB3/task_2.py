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


# Cat
ellipse(screen, ORANGE, (350, 250, 50, 90))
ellipse(screen, ORANGE, (70, 200, 310, 100))                     # BODY
ellipse(screen, BLACK, (70, 200, 310, 100), 1)
ellipse(screen, ORANGE, (90, 275, 70, 50))
ellipse(screen, BLACK, (90, 275, 70, 50), 1)
circle(screen, ORANGE, (300, 290), 50)
circle(screen, BLACK, (300, 290), 50, 1)
ellipse(screen, ORANGE, (320, 310, 30, 67))
ellipse(screen, BLACK, (320, 310, 30, 67), 1)
ellipse(screen, ORANGE, (52, 240, 42, 67))
ellipse(screen, BLACK, (52, 240, 42, 67), 1)

circle(screen, ORANGE, (70, 240), 50)                  # HEAD
circle(screen, BLACK, (70, 240), 50, 1)

polygon(screen, ORANGE, ((30, 180),(60, 190), (25, 215)))
polygon(screen, BLACK, ((30, 180),(60, 190), (25, 215)), 1)
polygon(screen, ORANGE, ((80, 190), (110, 180), (112, 218)))
polygon(screen, BLACK, ((80, 190), (110, 180), (112, 218)), 1)       # EARS
polygon(screen, LIGHT_PINK, ((32, 182), (52, 190), (28, 207)))
polygon(screen, BLACK, ((32, 182), (52, 190), (28, 207)), 1)
polygon(screen, LIGHT_PINK, ((84, 190), (106, 183), (108, 210)))
polygon(screen, BLACK, ((84, 190), (106, 183), (108, 210)), 1)

ellipse(screen, GREEN, (35, 210, 30, 35))                              #EYES
ellipse(screen, BLACK, (35, 210, 30, 35), 1)
ellipse(screen, GREEN, (80, 210, 30, 35))
ellipse(screen, BLACK, (80, 210, 30, 35), 1)
ellipse(screen, BLACK, (53, 215, 7, 25))
ellipse(screen, BLACK, (97, 215, 7, 25))
line(screen, WHITE, (46, 215), (50, 227), 4)
line(screen, WHITE, (89, 217), (95, 229), 4)

polygon(screen, LIGHT_PINK, ((70, 260), (66, 254), (74, 254)))        #NOSE
polygon(screen, BLACK, ((70, 260), (66, 254), (74, 254)), 1)
line(screen, BLACK, (70, 260), (70, 267))




arc(screen, BLACK, (60, 258, 20, 10), 3.19, 6.28, 1)
arc(screen, BLACK, (87, 254, 50, 10), 0, 3.20)
arc(screen, BLACK, (87, 258, 50, 10), 0, 3.20)                         #MOUSTACHE
arc(screen, BLACK, (87, 262, 50, 10), 0, 3.20)
arc(screen, BLACK, (5, 262, 50, 10), 0, 3.20)
arc(screen, BLACK, (5, 258, 50, 10), 0, 3.20)
arc(screen, BLACK, (5, 254, 50, 10), 0, 3.20)





pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
