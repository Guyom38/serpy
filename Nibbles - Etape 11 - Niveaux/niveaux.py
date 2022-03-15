import pygame
from pygame.locals import *
import time

import variables as VAR

import terrain
import serpents
import pommes
import interface

def charger_niveau():

     # --- Création de la pomme
    pommes.detruire_toutes_les_pommes()


    # --- Charge l'image du niveau
    image_niveau = pygame.image.load('00.png')

    # --- Controle si le niveau a les bonnes dimensions
    if (image_niveau.get_width() == terrain.dimensionX \
        and image_niveau.get_height() == terrain.dimensionY) :

        # --- Efface le niveau
        terrain.creer()
            
        # --- Récupére les murs de l'image et les crée dans le jeu
        for y in range(0, terrain.dimensionY):
            for x in range(0, terrain.dimensionX):
                Joueur1, Mur, Joueur2, SertARien = image_niveau.get_at((x, y))

                # --- Charge le mur
                if Mur > 128:
                    terrain.grille[x][y] = (0, 128, 0)
                    
                # --- Detect position joueur 1
                elif Joueur1 > 128:
                    VAR.position_initial_joueur1 = (x, y)

                # --- Detect position joueur 2
                elif Joueur2 > 128:
                    VAR.position_initial_joueur2 = (x, y)
            
        pommes.creer(1)

    # --- Création des joueurs
    serpents.reinitialiser()



        


