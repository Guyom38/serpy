import pygame
from pygame.locals import *
import time

import variables as VAR
from variables import *

import terrain
import serpents
import pommes
import interface

def gestion_niveau_suivant(_fenetre):
    # --- Controle si toutes les pommes du niveaux ont été mangé
    if VAR.pommes_mangees == VAR.nb_pommes_niveaux_suivant:
        VAR.niveau = VAR.niveau + 1
        charger_niveau()

    # ---
    if VAR.jeu_suspendu == True:
        if VAR.jeu_suspendu_raison == "NOUVEAU NIVEAU":
            interface.afficher_message(_fenetre, "NIVEAU " + str(VAR.niveau), 400, 100)
            if time.time() > VAR.jeu_suspendu_timer + 1: VAR.jeu_suspendu = False

        elif VAR.jeu_suspendu_raison == "PARTIE TERMINEE":
            interface.afficher_message(_fenetre, "GAME OVER", 400, 100)
            if time.time() > VAR.jeu_suspendu_timer + 2: 
                VAR.menu_select = "JOUEUR"
                VAR.doit_etre_afficher = True

def charger_niveau():

    VAR.jeu_suspendu = True
    VAR.jeu_suspendu_timer = time.time()

    # --- Création de la pomme
    pommes.detruire_toutes_les_pommes()
    VAR.pommes_mangees = 0

    # --- Fabrique le nom du fichier par rapport au niveau
    nom_fichier_niveau = str(VAR.niveau)
    if VAR.niveau < 10: 
        nom_fichier_niveau = "0" + str(VAR.niveau)

    try:
        # --- Charge l'image du niveau
        image_niveau = pygame.image.load(nom_fichier_niveau + '.png')

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
                        VAR.position_initial_joueur[0] = (x, y)

                    # --- Detect position joueur 2
                    elif Joueur2 > 128:
                        VAR.position_initial_joueur[1] = (x, y)
            
            pommes.creer(1)
            VAR.jeu_suspendu_raison = "NOUVEAU NIVEAU"

    except:
        VAR.jeu_suspendu_raison = "PARTIE TERMINEE"

    # --- Création des joueurs
    serpents.reinitialiser()

def niveau_vide():

    VAR.jeu_suspendu = True
    VAR.jeu_suspendu_timer = time.time()

   
    pommes.detruire_toutes_les_pommes()
    VAR.pommes_mangees = 0

    terrain.creer()
    pommes.creer(10)
    VAR.jeu_suspendu_raison = "NOUVEAU NIVEAU"
    VAR.nb_pommes_niveaux_suivant = 100
    VAR.nb_joueurs = 5
    VAR.position_initial_joueur = [(5, 5), ( terrain.dimensionX -5, 5), (terrain.dimensionX -5, terrain.dimensionY -5), (5, terrain.dimensionY -5), (int(terrain.dimensionX/2), int(terrain.dimensionY/2))]
    
    serpents.creer()
    serpents.reinitialiser()

        


