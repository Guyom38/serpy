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

serpents.creer()
serpents.reinitialiser()

# =============================================================================
# LA BOUCLE PRINCIPALE
# =============================================================================
# Elle se repette tant que la variable "boucle_active" est VRAI (True)
VAR.boucle_active = True
while VAR.boucle_active:
        
    pygame.draw.rect(fenetre, VAR.COULEUR_FOND_ECRAN, (0, 0, VAR.ECRAN_X, VAR.ECRAN_Y))

    # --- On controle les actions du joueurs.
    VAR.boucle_active = VAR.boucle_active = serpents.gestion_clavier()
    
    terrain.afficher(fenetre)
    serpents.afficher(fenetre)
    pommes.afficher(fenetre)

    # --- Actualise la fenêtre
    pygame.display.flip()

# --- Quitte le programme proprement
pygame.display.quit() 
pygame.quit() 

