# On importe la bibliothèque Pygame,
# Elle contient toutes les commandes pour créer ton jeu vidéo.
import pygame
from pygame.locals import *

# On importe nos fichiers
import variables as VAR
import serpents
import terrain
import pommes

# On active Pygame.
pygame.init()

# On crée la fenêtre de ton jeu,
# On utilisera la variable "fenetre" pour dessiner dessus.
fenetre = pygame.display.set_mode((VAR.ECRAN_X, VAR.ECRAN_Y))

# On met un titre à la fenêtre de ton jeu
pygame.display.set_caption(VAR.TITRE)

# --- Création de l'objet serpent
terrain.creer()
pommes.creer(1)
serpent = serpents.objet_serpent()

# =============================================================================
# LA BOUCLE PRINCIPALE
# =============================================================================
# Elle se repette tant que la variable "boucle_active" est VRAI (True)
VAR.boucle_active = True
while VAR.boucle_active:
        
    # --- On dessine un rectangle sur toute la surface "fenetre" 
    #     de couleur noire (0,0,0), a l'emplacement (0, 0) 
    #     et de taille (800, 600).
    pygame.draw.rect(fenetre, VAR.COULEUR_FOND_ECRAN, (0, 0, VAR.ECRAN_X, VAR.ECRAN_Y))

    # --- On controle les actions du joueurs.
    for event in pygame.event.get():      
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            VAR.boucle_active = False # Indique de sortir de la boucle.
    
        if event.type == KEYDOWN:  # KEYUP existe aussi
            if event.key == K_RIGHT and not serpent.direction == "GAUCHE": serpent.direction = "DROITE"
            if event.key == K_LEFT  and not serpent.direction == "DROITE": serpent.direction = "GAUCHE"
            if event.key == K_UP    and not serpent.direction == "BAS":    serpent.direction = "HAUT"
            if event.key == K_DOWN  and not serpent.direction == "HAUT":   serpent.direction = "BAS"
    
    terrain.afficher(fenetre)
    serpent.se_deplace()
    serpent.afficher(fenetre)
    pommes.afficher(fenetre)

    # --- Actualise la fenêtre
    pygame.display.flip()

# --- Quitte le programme proprement
pygame.display.quit() 
pygame.quit() 

