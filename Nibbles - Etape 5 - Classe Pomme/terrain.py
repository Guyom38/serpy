import pygame
from pygame.locals import *
import variables as VAR

grille = []

dimensionX = 80
dimensionY = 60

# --- Dimension du carré qui représente le terrain, ainsi que les morceaux des serpents
tailleCellule = int(VAR.ECRAN_X / dimensionX)

# --- Recal
positionX = int((VAR.ECRAN_X-(dimensionX * tailleCellule))/2)
positionY = int((VAR.ECRAN_Y-(dimensionY * tailleCellule))/2)

def creer():
    global grille

    # --- Remplie chaque cellule de la grille avec une variable COULEUR composée de 3 valeurs (0, 0, 0) 
    # ---   valeur 1 => (0 ... 255) => Rouge => correspond aux traces du joueur 1
    # ---   valeur 2 => (0, 255)    => Vert  => correspond aux murs du niveau
    # ---   valeur 3 => (0 ... 255) => Bleu  => correspond aux traces du joueur 2
    grille = [ [(20,0,20) for j in range(dimensionY+1) ] for i in range(dimensionX+1) ]

def afficher_fond(_fenetre):
    
    # --- dessine un rectangle (un peu plus grand) vert sur tout l'espace du jeu    
    pygame.draw.rect(_fenetre, VAR.COULEUR_MUR, (positionX-4, positionY-4, (dimensionX * tailleCellule)+8, (dimensionY * tailleCellule)+8))

    # --- dessine un rectangle noir sur tout l'espace du jeu
    pygame.draw.rect(_fenetre, VAR.COULEUR_NOIR, (positionX, positionY, (dimensionX * tailleCellule), (dimensionY * tailleCellule)))
 
def afficher(_fenetre):
    afficher_fond(_fenetre)

    # Dessine Terrain
    for y in range(0, dimensionY):
        for x in range (0, dimensionX):
            couleurCase = grille[x][y]
            posX, posY = positionX + (x * tailleCellule), positionY + (y * tailleCellule)
            pygame.draw.rect(_fenetre, couleurCase, (posX, posY , tailleCellule, tailleCellule))

def modifier(_x, _y):
    global grille
    
    v1,v2,v3 = grille[_x][_y]

    if v1 < 256 - 15: 
        v1 = v1 + 15 
    else:
        v1 = 0

    grille[_x][_y] = (v1, v2, v3)