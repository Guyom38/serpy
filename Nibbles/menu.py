import pygame
from pygame.locals import *

import variables as VAR

import niveaux
import serpents
import terrain

def afficher_titre(_fenetre):
    # --- affiche le titre 3D
    # --- --- affiche le titre blanc
    font = pygame.font.Font(None, 130)
    text = font.render(VAR.TITRE, 1,VAR.COULEUR_BLANC)
    posCentreX = int((VAR.ECRAN_X - text.get_width()) / 2)
    posY = 150

    _fenetre.blit(text, (posCentreX, posY))
    # --- --- affiche le titre gris foncé dessus
    text = font.render(VAR.TITRE, 1, VAR.COULEUR_MUR)
    _fenetre.blit(text, (posCentreX+2, posY+2))

def afficher(_fenetre):
    nombre_de_choix = len(VAR.MENU_CHOIX[VAR.menu_select])

    # --- dessine le fond gris foncé
    terrain.afficher_fond(_fenetre)
    afficher_titre(_fenetre)
        
    # --- affiche les choix du menu
    font = pygame.font.Font(None, 60)
 
    posY = VAR.ECRAN_Y - (nombre_de_choix * 70) - 30
    for choix in VAR.MENU_CHOIX[VAR.menu_select]:

        pygame.draw.rect(_fenetre, VAR.COULEUR_MUR, (0, posY, VAR.ECRAN_X, 50))
        text = font.render(choix, 1, VAR.COULEUR_BLANC)
        posCentreX = int((VAR.ECRAN_X - text.get_width()) / 2)
        _fenetre.blit(text, (posCentreX, posY+6))
        posY = posY + 70

def gestion_clavier():
    
    for event in pygame.event.get():        
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            # La fenêtre a été fermée ou La touche ESC a été pressée.
            return False # Indique de sortir de la boucle.
    
        if event.type == KEYDOWN:  # KEYUP existe aussi
            if VAR.menu_select == "JOUEUR":
                if event.key == K_1:
                    VAR.nb_joueurs = 1
                    VAR.menu_select = "DIFFICULTE"
                elif event.key == K_2:
                    VAR.nb_joueurs = 2
                    VAR.menu_select = "DIFFICULTE"

            elif VAR.menu_select == "DIFFICULTE":
                if event.key == K_1:
                    VAR.vitesse = 0.07
                    VAR.croissance = 40
                    lancer_la_partie()
                if event.key == K_2:
                    VAR.vitesse = 0.04
                    VAR.croissance = 20
                    lancer_la_partie()
                if event.key == K_3:
                    VAR.vitesse = 0.02
                    VAR.croissance = 8
                    lancer_la_partie()
    return True


def lancer_la_partie():

    VAR.menu = False
    VAR.menu_select = "JOUEUR"

    serpents.creer()
    VAR.niveau = 0
    niveaux.charger_niveau()
    

    

