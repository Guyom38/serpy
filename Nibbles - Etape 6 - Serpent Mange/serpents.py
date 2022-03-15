import pygame
from pygame.locals import *
import time

import variables as VAR
import terrain
import pommes

class objet_serpent:
    
    # --- Crée notre serpent
    def __init__(self):  
        self.corps = []    
        self.vitesse = VAR.vitesse
        self.vitesse_timer = time.time()
        self.couleur = VAR.COULEUR_ROUGE
        self.direction = ""

        self.pommes_manges = 0
        self.score = 0
        self.croissance = 4

        # --- Création du corps du serpent
        for i in range(0, 2):
            self.corps.append((15,15))
    
    # --- Affiche notre serpent
    def afficher(self, _fenetre):
        for bout_du_serpent in self.corps:
            x, y = bout_du_serpent
            pygame.draw.rect(_fenetre, self.couleur, \
                (terrain.positionX + (x * terrain.tailleCellule), terrain.positionY + (y * terrain.tailleCellule), \
                terrain.tailleCellule, terrain.tailleCellule))

    def frotteLesFesses(self):
        xTete, yTete = self.corps[0]
        # --- Accentue la couleur du terrain au passage de la tete du serpent
        terrain.modifier(xTete, yTete)
        
    def estCeQuiMange(self):
        xTete, yTete = self.corps[0]
        i = 0
        while i < pommes.nbPommes():
            xPomme, yPomme = pommes.liste_de_pommes[i].position
            if xPomme == xTete and yPomme == yTete:
                return pommes.liste_de_pommes[i]
            i = i +1
        return None

    def estCeQuiSort(self, xTete, yTete):
        if xTete > terrain.dimensionX-1:
            xTete = 0
        elif xTete < 0:
            xTete = terrain.dimensionX-1
        elif yTete > terrain.dimensionY-1:
            yTete = 0
        elif yTete < 0:
            yTete = terrain.dimensionY-1
        return xTete, yTete

    def grandit(self):
        for i in range(0, self.croissance):
            self.corps.append(self.corps[-1])

    # --- Deplace notre serpent
    def se_deplace(self):
        # --- Temporise le deplacement
        if time.time() < self.vitesse_timer + self.vitesse:
            return
        self.vitesse_timer = time.time()

        # --- Deplace le derrière vers l'avant, jusqu'a la tête
        for i in range(len(self.corps)-1, 0, -1):           
            self.corps[i] = self.corps[i-1]

        # --- Position de la tete après deplacement
        xTete, yTete = self.corps[0]

        if self.direction == "BAS":
            yTete = yTete +1
        elif self.direction == "HAUT":
            yTete = yTete -1
        elif self.direction == "DROITE":
            xTete = xTete +1
        elif self.direction == "GAUCHE":
            xTete = xTete -1
        else:
            return None
        
        xTete, yTete = self.estCeQuiSort(xTete, yTete)
        self.corps[0] = (xTete, yTete)
        self.frotteLesFesses()

        # --- Controle la nourriture
        questCeQuilAMange = self.estCeQuiMange()
        if not questCeQuilAMange == None:
            self.score = self.score + 10
            self.pommes_manges = self.pommes_manges + 1

            pommes.detruire(questCeQuilAMange)
            self.grandit()
            pommes.creer(1)




       
    