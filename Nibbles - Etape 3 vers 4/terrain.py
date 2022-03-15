import pygame
from pygame.locals import *
import variables as VAR

dimensionX = 80
dimensionY = 60

# --- Dimension du carré qui représente le terrain, ainsi que les morceaux des serpents
tailleCellule = int(VAR.ECRAN_X / dimensionX)

# --- Recal
positionX = int((VAR.ECRAN_X-(dimensionX * tailleCellule))/2)
positionY = int((VAR.ECRAN_Y-(dimensionY * tailleCellule))/2)

def afficher_fond(_fenetre):
    
    # --- dessine un rectangle (un peu plus grand) vert sur tout l'espace du jeu    
    pygame.draw.rect(_fenetre, VAR.COULEUR_MUR, \
        (positionX-4, positionY-4, (dimensionX * tailleCellule)+8, (dimensionY * tailleCellule)+8))

    # --- dessine un rectangle noir sur tout l'espace du jeu
    pygame.draw.rect(_fenetre, VAR.COULEUR_NOIR, (positionX, positionY, \
        (dimensionX * tailleCellule), (dimensionY * tailleCellule)))

def afficher_grille(_fenetre):
    for y in range(0, dimensionY):
        for x in range (0, dimensionX):
            posX, posY = positionX + (x * tailleCellule), positionY + (y * tailleCellule)
            pygame.draw.rect(_fenetre, VAR.COULEUR_FOND_ECRAN, \
                (posX, posY , tailleCellule+1, tailleCellule+1), 1)

def afficher(_fenetre):
    afficher_fond(_fenetre)
    afficher_grille(_fenetre)

