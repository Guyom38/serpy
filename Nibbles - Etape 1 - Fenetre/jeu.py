import pygame
from pygame.locals import *

# --- Initialisation
pygame.init()

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SerPy")

# --- Boucle du jeu
boucle_active = True
while boucle_active:
    pygame.draw.rect(fenetre, (0,0,0), (0, 0, 800, 600))

    pygame.display.flip()
