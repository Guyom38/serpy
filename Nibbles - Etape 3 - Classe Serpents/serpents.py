import pygame
from pygame.locals import *
import time

import variables as VAR

class objet_serpent:
    
    # --- Crée notre serpent
    def __init__(self):  
        self.corps = []    
        self.vitesse = VAR.vitesse
        self.vitesse_timer = time.time()
        self.couleur = VAR.COULEUR_ROUGE
        self.direction = ""

        # --- Création du corps du serpent
        for i in range(0, 8):
            self.corps.append((15,15))
    
    # --- Affiche notre serpent
    def afficher(self, _fenetre):
        for bout_du_serpent in self.corps:
            x, y = bout_du_serpent
            pygame.draw.rect(_fenetre, self.couleur, \
                ((x * VAR.tailleCellule), (y * VAR.tailleCellule), \
                VAR.tailleCellule, VAR.tailleCellule))
        
    # --- Deplace notre serpent
    def se_deplace(self):
        # --- Temporise le deplacement
        if time.time() < self.vitesse_timer + self.vitesse:
            return
        self.vitesse_timer = time.time()

        # --- Deplace le derrière vers l'avant, jusqu'a la tête
        for i in range(len(self.corps)-1, 0, -1):   
            print(i, self.corps[i], "<=", i-1, self.corps[i-1]) 
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
        
        self.corps[0] = (xTete, yTete)




       
    