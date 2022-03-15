import pygame
from pygame.locals import *

# On importe nos fichiers
import variables as VAR
import serpents
import terrain

# --- Initialisation
pygame.init()

fenetre = pygame.display.set_mode((VAR.ECRAN_X, VAR.ECRAN_Y))
pygame.display.set_caption(VAR.TITRE)

# --- Création de l'objet serpent
terrain.creer()
serpent = serpents.objet_serpent()

# --- Boucle du jeu
VAR.boucle_active = True
while VAR.boucle_active:
    pygame.draw.rect(fenetre, VAR.COULEUR_FOND_ECRAN, (0, 0, VAR.ECRAN_X, VAR.ECRAN_Y))

    # --- On controle les actions du joueurs.
    for event in pygame.event.get():      
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            VAR.boucle_active = False # Indique de sortir de la boucle.
    
        if event.type == KEYDOWN:  
            if event.key == K_RIGHT and not serpent.direction == "GAUCHE": serpent.direction = "DROITE"
            if event.key == K_LEFT  and not serpent.direction == "DROITE": serpent.direction = "GAUCHE"
            if event.key == K_UP    and not serpent.direction == "BAS":    serpent.direction = "HAUT"
            if event.key == K_DOWN  and not serpent.direction == "HAUT":   serpent.direction = "BAS"
    
    terrain.afficher(fenetre)
    serpent.se_deplace()
    serpent.afficher(fenetre)

    # --- Actualise la fenêtre
    pygame.display.flip()

# --- Fin du programme
pygame.display.quit() 
pygame.quit() 

