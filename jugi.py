# jugi = dict()
# for i in range(20):
#     a, b = input('>').split()
#     jugi[i+1]=(a, float(b))
# print(jugi)
# import sys
# import pygame
# from pygame.locals import *
# # import hydro


# WHITE = (255,255,255)
# GRAY = (128,128,128)
# BLACK = (0,0,0)

# pygame.init()

# size = (1080,700)
# FPS = 100
# FramePerSec = pygame.time.Clock()
# GameDisplay = pygame.display.set_mode(size)
# GameDisplay.fill(GRAY)
# pygame.display.set_caption("Bond simulation")

# if GameDisplay.get_at((10,10)) == GRAY:
#     print('yes')

import sys
import pygame
from pygame.locals import *
# import hydro


WHITE = (255,255,255)
GRAY = (128,128,128)
BLACK = (0,0,0)

pygame.init()

size = (1080,700)
FPS = 100
FramePerSec = pygame.time.Clock()
GameDisplay = pygame.display.set_mode(size)
GameDisplay.fill(GRAY)
pygame.display.set_caption("Bond simulation")

while True:
    pygame.draw.line(GameDisplay, BLACK, (10,10), (300,300))
    pygame.display.update()