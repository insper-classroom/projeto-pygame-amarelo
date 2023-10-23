import pygame
import math
import random



def inicializacao():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(('Flap Bird'))

    assets = {}
    estado = {}
    return 