import pygame
from pygame.locals import *

# On importe nos fichiers
import variables as VAR

# --- Initialisation
pygame.init()

fenetre = pygame.display.set_mode((VAR.ECRAN_X, VAR.ECRAN_Y))
pygame.display.set_caption(VAR.TITRE)

# --- Boucle du jeu
VAR.boucle_active = True
while VAR.boucle_active:
    pygame.draw.rect(fenetre, VAR.COULEUR_FOND_ECRAN, (0, 0, VAR.ECRAN_X, VAR.ECRAN_Y))

    for event in pygame.event.get():      
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            VAR.boucle_active = False 

    pygame.display.flip()

# --- Fin du programme
pygame.display.quit() 
pygame.quit() 