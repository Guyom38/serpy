# On importe la bibliothèque Pygame,
# Elle contient toutes les commandes pour créer ton jeu vidéo.
import pygame
from pygame.locals import *

# On importe nos fichiers
import variables as VAR

import serpents
import pommes
import menu 
import interface
import terrain
import niveaux

# On active Pygame.
pygame.init()

# On crée la fenêtre de ton jeu,
# On utilisera la variable "fenetre" pour dessiner dessus.
fenetre = pygame.display.set_mode((VAR.ECRAN_X, VAR.ECRAN_Y))
    

# On met un titre à la fenêtre de ton jeu
pygame.display.set_caption(VAR.TITRE)

clock = pygame.time.Clock()

# =============================================================================
# LA BOUCLE PRINCIPALE
# =============================================================================
# Elle se repette tant que la variable "boucle_active" est VRAI (True)
VAR.boucle_active = True
while VAR.boucle_active:
        
    interface.efface_ecran(fenetre, VAR.COULEUR_FOND_ECRAN)

    # Boucle sur tous les événements gérés par Pygame
    if VAR.menu == True:
        VAR.boucle_active = menu.gestion_clavier()
        menu.afficher(fenetre)
        
    else:
        VAR.boucle_active = serpents.gestion_clavier()
            
        # --- Gestion des objets
        terrain.afficher(fenetre)
        serpents.afficher(fenetre)
        pommes.afficher(fenetre)

        interface.afficher_informations(fenetre)
        niveaux.gestion_niveau_suivant(fenetre)
            

    # --- Actualise la fenêtre
    pygame.display.flip()
    clock.tick(60)

# --- Quitte le programme proprement
pygame.display.quit() 
pygame.quit() 

