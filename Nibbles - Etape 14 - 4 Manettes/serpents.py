import pygame
from pygame.locals import *
import time

import variables as VAR
import terrain
import pommes



class objet_serpent:
    
    # --- Crée notre serpent
    def __init__(self, _joueur):  
        self.joueur = _joueur
        
        self.corps = []    
        self.vitesse = VAR.vitesse
        self.vitesse_timer = time.time()

        self.couleur = [(255,0,0,255), (0,0,255,255), (255,255,0,255), (0,255,255,255), (128,0,128,255), (128,128,128, 255)][self.joueur-1]
     

        self.direction = ""

        self.pommes_manges = 0
        self.score = 0
        self.croissance = 4
        self.positionInitale = (0,0)

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
        terrain.modifier(self.joueur, xTete, yTete)
        
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
        xTete, yTete = self.corps[0]
        i = 1
        while i < len(self.corps):
            x, y = self.corps[i]
            if xTete == x and yTete == y:
                return True
            i = i +1
        return False

    def estCeQuiMordUnAutreSerpent(self):
        if VAR.nb_joueurs < 2: 
            return False

        xTete, yTete = self.corps[0]

        i = 1
        for autre_serpent in VAR.liste_serpents:
            if not autre_serpent.joueur == self.joueur:
                while i < len(autre_serpent.corps):
                    x, y = autre_serpent.corps[i]
                    print((x,y, " | ", xTete, yTete))
                    if xTete == x and yTete == y:
                        return True
                    i = i +1
                return False 

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

    def perdUnePomme(self):
        # --- Retire une pomme du ventre du serpent et du compteur général
        if self.pommes_manges > 0:
            self.pommes_manges = self.pommes_manges - 1
            VAR.pommes_mangees = VAR.pommes_mangees - 1
            # --- crée une pomme
            pommes.creer(1) 

    # --- Deplace notre serpent
    def se_deplace(self):
        # --- Temporise le deplacement
        # --- Si le temps qui s'écoule de l'ordinateur <  que celui du compteur du serpent + de sa vitesse
        if time.time() < self.vitesse_timer + self.vitesse:
            # --- alors il est trop tot pour bouger, quitte la fonction
            return

        # --- réinitialise le compteur du serpent avec le temps qui s'écoule de l'ordinateur
        self.vitesse_timer = time.time()

        # --- Deplace le derrière vers l'avant, jusqu'a la tête
        for i in range(len(self.corps)-1, 0, -1):           
            self.corps[i] = self.corps[i-1]

        # --- Position de la tete après deplacement
        xTete, yTete = self.corps[0]

        # --- deplace la tete en fonction de la direction
        if self.direction == "BAS":
            yTete = yTete +1
        elif self.direction == "HAUT":
            yTete = yTete -1
        elif self.direction == "DROITE":
            xTete = xTete +1
        elif self.direction == "GAUCHE":
            xTete = xTete -1
        else:
            # --- Sors la fonction si le serpent est immobile
            return None

        # --- controle si la tete sort du terrain
        xTete, yTete = self.estCeQuiSort(xTete, yTete)
        # --- enregistre la nouvelle position de la tete
        self.corps[0] = (xTete, yTete)

        # --- controle les collisions problematiques
        if self.estCeQuiSeMord() \
            or self.estCeQuiMordUnAutreSerpent() \
            or self.estCeQuiSePrendUnMur() :

            # --- enleve une pomme au serpent
            self.perdUnePomme()
            # --- rend le serpent petit
            self.redevient_bebe()

        # --- fait la trace du serpent sur la cellule traversée
        self.frotteLesFesses()

        # --- Controle la nourriture
        questCeQuilAMange = self.estCeQuiMange()

        # --- si ce qu'il a mangé n'est pas RIEN
        if not questCeQuilAMange == None:
            # --- ajoute du score en tenant compte du niveau
            self.score = self.score + ((1+VAR.niveau) * 10)
            # --- ajoute un pomme mangée a son compteur
            self.pommes_manges = self.pommes_manges + 1
            # --- détruit ce qu'il a mangé (objet pomme)
            pommes.detruire(questCeQuilAMange)
            # --- fait grandir le serpent
            self.grandit()
            # --- crée une nouvelle pomme
            pommes.creer(1)

# --- affiche et deplace les serpents
def afficher(_fenetre):
    for serpent in VAR.liste_serpents:
        serpent.se_deplace()
        serpent.afficher(_fenetre)

# --- Créer les serpents (oeufs)
def creer():

    # --- Vide la liste des serpents
    VAR.liste_serpents = []
    
    # --- Création du premier joueur
    for id in range(VAR.nb_joueurs):
        VAR.liste_serpents.append(objet_serpent(id+1))

 
# --- Fait naitre les serpents
def reinitialiser():
 
    # --- Parcours chaque serpent dans la liste
    for serpent in VAR.liste_serpents:
        
        serpent.positionInitale = VAR.position_initial_joueur[serpent.joueur -1]

        # --- Remet le compteur des pommes croquées du serpent à 0
        serpent.pommes_manges = 0
        # --- Rend le serpent tout bébé (petit)
        serpent.redevient_bebe()

# --- Gestion des actions de l'utilisateur
def gestion_clavier():

    for event in pygame.event.get():        
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            # --- La fenêtre a été fermée ou La touche ESC a été pressée.
            return False # ---- retourne FAUX (le jeu va s'arreter)

        # --- Si une touche est pressée
        if event.type == KEYDOWN:  
            # --- Si le jeu n'est pas suspendu (a cause d'un message)
            if not VAR.jeu_suspendu:
                # --- si la touche est pressé, que le serpent ne va pas dans la direction opposée alors changer la direction

                if event.key == K_RIGHT and not VAR.liste_serpents[0].direction == "GAUCHE": VAR.liste_serpents[0].direction = "DROITE"
                if event.key == K_LEFT  and not VAR.liste_serpents[0].direction == "DROITE": VAR.liste_serpents[0].direction = "GAUCHE"
                if event.key == K_UP    and not VAR.liste_serpents[0].direction == "BAS":    VAR.liste_serpents[0].direction = "HAUT"
                if event.key == K_DOWN  and not VAR.liste_serpents[0].direction == "HAUT":   VAR.liste_serpents[0].direction = "BAS"

                if VAR.nb_joueurs > 1:
                    if event.key == K_d and not VAR.liste_serpents[1].direction == "GAUCHE": VAR.liste_serpents[1].direction = "DROITE"
                    if event.key == K_a and not VAR.liste_serpents[1].direction == "DROITE": VAR.liste_serpents[1].direction = "GAUCHE"
                    if event.key == K_w and not VAR.liste_serpents[1].direction == "BAS":    VAR.liste_serpents[1].direction = "HAUT"
                    if event.key == K_s and not VAR.liste_serpents[1].direction == "HAUT":   VAR.liste_serpents[1].direction = "BAS"
        
        elif event.type == pygame.JOYAXISMOTION:
            idJoy = event.joy+2
            if not VAR.jeu_suspendu:
                if event.axis == 0 and event.value > 0.9 and not VAR.liste_serpents[idJoy].direction == "GAUCHE":
                    VAR.liste_serpents[idJoy].direction = "DROITE"
                elif event.axis == 0 and event.value < -0.9 and not VAR.liste_serpents[idJoy].direction == "DROITE":
                    VAR.liste_serpents[idJoy].direction = "GAUCHE"
                elif event.axis == 1 and event.value < -0.9 and not VAR.liste_serpents[idJoy].direction == "BAS":
                    VAR.liste_serpents[idJoy].direction = "HAUT"
                elif event.axis == 1 and event.value > 0.9 and not VAR.liste_serpents[idJoy].direction == "HAUT":
                    VAR.liste_serpents[idJoy].direction = "BAS"
                

    # --- retourne VRAI (le jeu continue)
    return True