import pygame
from pygame.locals import *
import variables as VAR
import time

import serpents
import niveaux
import terrain
import menu



def efface_ecran(_fenetre, _couleur):
    pygame.draw.rect(_fenetre, _couleur, (0, 0, VAR.ECRAN_X, VAR.ECRAN_Y))

def afficher_message(_fenetre, _texte, _dimension_cadre_X, _dimension_cadre_Y):
    posCadreCentreX = int((VAR.ECRAN_X - _dimension_cadre_X) / 2)
    posCadreCentreY = int((VAR.ECRAN_Y - _dimension_cadre_Y) / 2)
    epaisseurCadre = 4
    
    pygame.draw.rect(_fenetre, VAR.COULEUR_MUR, \
        (posCadreCentreX, posCadreCentreY, _dimension_cadre_X, _dimension_cadre_Y))
    pygame.draw.rect(_fenetre, VAR.COULEUR_FOND, \
        (posCadreCentreX+epaisseurCadre, posCadreCentreY+epaisseurCadre, \
        _dimension_cadre_X-(epaisseurCadre*2), _dimension_cadre_Y-(epaisseurCadre*2)))
    
    font = pygame.font.Font(None, 60)
    texte = font.render(_texte,1,VAR.COULEUR_BLANC)
    posTexteCentreX = posCadreCentreX + int((_dimension_cadre_X - texte.get_width()) / 2)
    posTexteCentreY = posCadreCentreY + int((_dimension_cadre_Y - texte.get_height()) / 2)
    _fenetre.blit(texte, (posTexteCentreX, posTexteCentreY))
   


def afficher_informations(_fenetre):
    afficher_scores(_fenetre)
    afficher_niveau(_fenetre)
    afficher_pommes_croquees(_fenetre)

def afficher_scores(_fenetre):
    joueur1 = serpents.liste_serpents[0]
    
    # --- afficher un cadre de couleur pour les informations
    largeurCadre = int(VAR.ECRAN_X / 3)
    font = pygame.font.Font(None, 24)
    
    # --- Info Serpent 1
    pygame.draw.rect(_fenetre, VAR.COULEUR_BLANC, (0,8, largeurCadre, 20))
    pygame.draw.rect(_fenetre, joueur1.couleur, (0,0, 150, 8))
    text = font.render("SCORE : " + str(joueur1.score),1,VAR.COULEUR_NOIR)
    _fenetre.blit(text, (16, 10))

    # --- Info Serpent 2
    if VAR.nb_joueurs == 2:
        joueur2 = serpents.liste_serpents[1]
        pygame.draw.rect(_fenetre, VAR.COULEUR_BLANC, (VAR.ECRAN_X-largeurCadre,8, largeurCadre, 20))
        pygame.draw.rect(_fenetre, joueur2.couleur, (VAR.ECRAN_X-150,0, 150, 8))
        text = font.render("SCORE : " + str(joueur2.score),1,VAR.COULEUR_NOIR)
        _fenetre.blit(text, (VAR.ECRAN_X-largeurCadre+16, 10))

def afficher_pommes_croquees(_fenetre):
    tailleImgPomme = VAR.MARGE_CADRE_MIN

    joueur1 = serpents.liste_serpents[0]
    for i in range(0, joueur1.pommes_manges):
        pygame.draw.rect(_fenetre, joueur1.couleur, (0, terrain.positionY + ((tailleImgPomme + 4) * i), \
            tailleImgPomme, tailleImgPomme))

    # --- Info Serpent 2
    if VAR.nb_joueurs == 2:
        joueur2 = serpents.liste_serpents[1]
        for i in range(0, joueur2.pommes_manges):
            pygame.draw.rect(_fenetre, joueur2.couleur, \
                (VAR.ECRAN_X-tailleImgPomme, terrain.positionY + ((tailleImgPomme + 4) * i), \
                tailleImgPomme, tailleImgPomme))

def afficher_niveau(_fenetre):
    font = pygame.font.Font(None, 40)
    text = font.render("LEVEL : " + str(VAR.niveau),1,VAR.COULEUR_BLANC)
    _fenetre.blit(text, ((VAR.ECRAN_X-text.get_width()) / 2, 10))