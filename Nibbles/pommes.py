import pygame
from pygame.locals import *
from random import *

import variables as VAR
import terrain

liste_de_pommes = []

# --- objet pomme en général
class objet_pomme:
    couleur = VAR.COULEUR_ORANGE
    position = (0, 0)

    # --- initialise la pomme
    def __init__(self):
        xPosHasard = 0
        yPosHasard = 0

        zoneLibre = False
        while not zoneLibre:
            xPosHasard = randint(0, terrain.dimensionX-1)
            yPosHasard = randint(0, terrain.dimensionY-1)

            if not (terrain.estUnMur(xPosHasard, yPosHasard) \
                or ilYaUnePomme(xPosHasard, yPosHasard)):
                zoneLibre = True
        
        self.position = (xPosHasard, yPosHasard)

    # --- dessine la pomme
    def afficher(self, _fenetre):
        x, y = self.position
        taillePomme = terrain.tailleCellule
        xPos = terrain.positionX + (x * taillePomme)
        yPos = terrain.positionY + (y * taillePomme)
        
        rayon = int(taillePomme / 2)
        pygame.draw.circle(_fenetre, self.couleur, (xPos + rayon, yPos + rayon), rayon)

# --- retourne le nombre de pommes
def nbPommes():
    return len(liste_de_pommes)

# --- crée autant de pommes qu'indiqué
def creer(_nombre_de_pommes):
    global liste_de_pommes

    for i in range(0, _nombre_de_pommes):
        liste_de_pommes.append(objet_pomme())

# --- détruit toutes les pommes
def detruire_toutes_les_pommes():
    global liste_de_pommes
    liste_de_pommes = []

# --- détruit l'objet pomme indiqué
def detruire(_pomme):
    global liste_de_pommes
    liste_de_pommes.remove(_pomme)
    VAR.pommes_mangees = VAR.pommes_mangees + 1

# --- vérifie si une pomme est présente au coordonnée indiquée
def ilYaUnePomme(_x, _y):
    i = 0
    while i<nbPommes():
        _xPom, _yPom = liste_de_pommes[i].position
        if _x == _xPom and _y == _yPom:
            return True
        i = i +1
    return False

# --- affiche l'ensemble des pommes actives
def afficher(_fenetre):
    for pomme in liste_de_pommes:
        pomme.afficher(_fenetre)