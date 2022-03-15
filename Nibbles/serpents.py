import pygame
from pygame.locals import *
import time

import variables as VAR
import pommes 
import terrain



liste_serpents = []

class objet_serpent:
    
    # --- Crée notre serpent
    def __init__(self, _joueur):  
        self.corps = []    
        self.score = 0
        self.pommes_manges = 0
        self.vitesse = VAR.vitesse
        self.vitesse_timer = time.time()
        self.croissance = VAR.croissance
        self.joueur = _joueur  
        #self.nePeutPasSeMordre_LaQueueAuDebut = True

        if self.joueur == 1:
            self.couleur = VAR.COULEUR_ROUGE
        elif self.joueur == 2:            
            self.couleur = VAR.COULEUR_BLEU
        
        self.direction = ""
        self.positionInitale = (0,0)

    # --- Affiche notre serpent
    def afficher(self, _fenetre):
        for bout_du_serpent in self.corps:
            x, y = bout_du_serpent
            pygame.draw.rect(_fenetre, self.couleur, \
                (terrain.positionX + (x * terrain.tailleCellule), terrain.positionY + (y * terrain.tailleCellule), \
                terrain.tailleCellule, terrain.tailleCellule))
        
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

    def estCeQuiMange(self):
        xTete, yTete = self.corps[0]
        i = 0
        while i < pommes.nbPommes():
            xPomme, yPomme = pommes.liste_de_pommes[i].position
            if xPomme == xTete and yPomme == yTete:
                return pommes.liste_de_pommes[i]
            i = i +1
        return None

    def estCeQuiSeMord(self):
        #if self.nePeutPasSeMordre_LaQueueAuDebut:
        #    return False

        xTete, yTete = self.corps[0]
        i = 1
        while i < len(self.corps):
            x, y = self.corps[i]
            if xTete == x and yTete == y:
                return True
            i = i +1
        return False

    def estCeQuiMordUnAutreSerpent(self):
        if not VAR.nb_joueurs == 2: 
            return False

        xTete, yTete = self.corps[0]

        i = 1
        for autre_serpent in liste_serpents:
            if not autre_serpent.joueur == self.joueur:
                while i < len(autre_serpent.corps):
                    x, y = autre_serpent.corps[i]
                    if xTete == x and yTete == y:
                        return True
                    i = i +1
                return False 
                
    def estCeQuiSePrendUnMur(self):
        xTete, yTete = self.corps[0]
        return terrain.estUnMur(xTete, yTete)

    def grandit(self):
        for i in range(0, self.croissance):
            self.corps.append(self.corps[-1])

    def redevient_bebe(self):
        self.corps = []
        for i in range(0, VAR.LONGUEUR_DU_SERPENT_AU_DEBUT):
            self.corps.append(self.positionInitale)
        self.direction = ""


    def frotteLesFesses(self):
        xTete, yTete = self.corps[0]
        # --- Accentue la couleur du terrain au passage de la tete du serpent
        terrain.modifier(self.joueur, xTete, yTete)

    # --- Deplace notre serpent
    def se_deplace(self):
        # --- Temporise le deplacement
        if time.time() < self.vitesse_timer + self.vitesse \
            or VAR.jeu_suspendu == True:
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
        
        
        # --- Controle les collisions
        xTete, yTete = self.estCeQuiSort(xTete, yTete)
        self.corps[0] = (xTete, yTete)

        if self.estCeQuiSeMord() \
            or self.estCeQuiMordUnAutreSerpent() \
                or self.estCeQuiSePrendUnMur():

            self.perdUnePomme()
            self.redevient_bebe()
            

        # --- Controle la nourriture
        questCeQuilAMange = self.estCeQuiMange()
        if not questCeQuilAMange == None:
            self.score = self.score + ((1+VAR.niveau) * 10)
            
            self.pommes_manges = self.pommes_manges + 1

            pommes.detruire(questCeQuilAMange)
            self.grandit()
            pommes.creer(1)

        # --- Ajoute la tete au corps du serpent
        self.frotteLesFesses()
        self.nePeutPasSeMordre_LaQueueAuDebut = False

    def perdUnePomme(self):
        # --- Retire une pomme du ventre du serpent et du compteur général
        if self.pommes_manges > 0:
            self.pommes_manges = self.pommes_manges - 1
            VAR.pommes_mangees = VAR.pommes_mangees - 1
            pommes.creer(1)        

def creer():
    global liste_serpents

    # --- Vide la liste des serpents
    liste_serpents = []
    
    # --- Création du premier joueur
    liste_serpents.append(objet_serpent(1))

    # --- Création du second joueur
    if VAR.nb_joueurs == 2:
        liste_serpents.append(objet_serpent(2))


def reinitialiser():
    global liste_serpents

    for serpent in liste_serpents:
        
        if serpent.joueur == 1:
            serpent.positionInitale = VAR.position_initial_joueur1
        elif serpent.joueur == 2:
            serpent.positionInitale = VAR.position_initial_joueur2

        serpent.pommes_manges = 0
        serpent.redevient_bebe()
        

def afficher(_fenetre):
    for serpent in liste_serpents:
        serpent.se_deplace()
        serpent.afficher(_fenetre)

def gestion_clavier():
    global liste_serpents

    for event in pygame.event.get():        
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            # La fenêtre a été fermée ou La touche ESC a été pressée.
            return False # Indique de sortir de la boucle.
    
        if event.type == KEYDOWN:  # KEYUP existe aussi
            if not VAR.jeu_suspendu:
                if event.key == K_RIGHT and not liste_serpents[0].direction == "GAUCHE": liste_serpents[0].direction = "DROITE"
                if event.key == K_LEFT  and not liste_serpents[0].direction == "DROITE": liste_serpents[0].direction = "GAUCHE"
                if event.key == K_UP    and not liste_serpents[0].direction == "BAS":    liste_serpents[0].direction = "HAUT"
                if event.key == K_DOWN  and not liste_serpents[0].direction == "HAUT":   liste_serpents[0].direction = "BAS"

                if VAR.nb_joueurs == 2:
                    if event.key == K_d and not liste_serpents[1].direction == "GAUCHE": liste_serpents[1].direction = "DROITE"
                    if event.key == K_a and not liste_serpents[1].direction == "DROITE": liste_serpents[1].direction = "GAUCHE"
                    if event.key == K_w and not liste_serpents[1].direction == "BAS":    liste_serpents[1].direction = "HAUT"
                    if event.key == K_s and not liste_serpents[1].direction == "HAUT":   liste_serpents[1].direction = "BAS"
            
    return True