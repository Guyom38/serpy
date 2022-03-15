import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((800, 600))

# --- Boucle du jeu
recommence = True
while recommence:
    # --- Vérifie si tu appuies sur ECHAP ou la X de la fenêtre
    for event in pygame.event.get():      
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            recommence = False 


    # --- Espace de dessin (PYGAME.DRAW.)
    pygame.draw.rect(fenetre, (0,0,0), (0, 0, 800, 600))

    couleur = (255,0,0)
    liste_points = [(10,10), (20,20), (30,10)]
    pygame.draw.polygon(fenetre, couleur, liste_points)

    couleur = (255,255,0)
    diametre = 20
    positionCentre = (50, 50)
    pygame.draw.circle(fenetre, couleur, positionCentre, diametre)

    couleur = (0,0,255)
    liste_points = (100,100, 310, 240)
    pygame.draw.ellipse(fenetre, couleur, liste_points)

    # --- Affiche mon dessin
    pygame.display.flip()

# --- Fin du programme
pygame.display.quit() 
pygame.quit() 


