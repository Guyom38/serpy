import pygame
from pygame.locals import *
import variables as VAR

# --- terrain
grille = []

# --- dimension du terrain
dimensionX = 96
dimensionY = 54

# --- Calcul de la taille d'une cellule par rapport a la resolution d'ecran et des marges
tailleCellule = int((VAR.ECRAN_X - (VAR.MARGE_CADRE_MIN * 2))/ dimensionX)

# --- Calcule la position du terrain, en tenant compte des marges et de la hauteur des informations joueurs.
positionX = int((VAR.ECRAN_X-(dimensionX * tailleCellule))/2)
positionY = VAR.HAUTEUR_ZONE_INFOS + int(((VAR.ECRAN_Y-(dimensionY * tailleCellule))-VAR.HAUTEUR_ZONE_INFOS)/2)

# --- Cree une matrice, tableau, contenant aucun mur
# --- la valeur 20, permet de voir la trace d'un serpent des le premier passage.
def creer():
    global grille

    # --- Remplie chaque cellule de la grille avec une variable COULEUR composée de 3 valeurs (0, 0, 0) 
    # ---   valeur 1 => (0 ... 255) => Rouge => correspond aux traces du joueur 1
    # ---   valeur 2 => (0, 255)    => Vert  => correspond aux murs du niveau
    # ---   valeur 3 => (0 ... 255) => Bleu  => correspond aux traces du joueur 2
    grille = [ [(20,0,20) for j in range(dimensionY+1) ] for i in range(dimensionX+1) ]

# --- fonctionne qui retourne VRAI (True), si un mur est présent.
def estUnMur(_x, _y):
    global grille
    j1, mur, j2 = grille[_x][_y]
    return mur > 0

# --- dessine un cadre, en plus du fond
def afficher_fond(_fenetre):
    
    # --- dessine un rectangle (un peu plus grand) vert sur tout l'espace du jeu    
    pygame.draw.rect(_fenetre, VAR.COULEUR_MUR, (positionX-4, positionY-4, (dimensionX * tailleCellule)+8, (dimensionY * tailleCellule)+8))

    # --- dessine un rectangle noir sur tout l'espace du jeu
    pygame.draw.rect(_fenetre, VAR.COULEUR_NOIR, (positionX, positionY, (dimensionX * tailleCellule), (dimensionY * tailleCellule)))

# --- Affiche tout le terrain
def afficher(_fenetre):
    # --- dessine un cadre, en plus du fond
    afficher_fond(_fenetre)

    # --- parcours en commencant par la premiere ligne, puis chacune des colonnes, et ainsi de suite ...
    for y in range(0, dimensionY):
        for x in range (0, dimensionX):
            # --- recupere la couleur de la cellule
            couleurCase = grille[x][y]
            # --- determine la position de la cellule sur l'écran
            posX, posY = positionX + (x * tailleCellule), positionY + (y * tailleCellule)
            # --- dessine la cellule
            pygame.draw.rect(_fenetre, couleurCase, (posX, posY , tailleCellule, tailleCellule))

# --- Colorie un peu plus la cellule au passage du joueur
def modifier(_joueur, _x, _y):
    global grille
    
    v1,v2,v3 = grille[_x][_y]

    if _joueur == 1:
        if v1 < 256 - 15: 
            v1 = v1 + 15 
        else:
            v1 = 0
        
    elif _joueur == 2:
        if v3 < 256 - 15: 
            v3 = v3 + 15 
        else: 
            v3 = 0

    grille[_x][_y] = (v1, v2, v3)