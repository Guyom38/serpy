import pygame
from pygame.locals import *
import variables as VAR
import time

import serpents
import terrain



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

def afficher_scores(_fenetre):
    x = 0
    id = 1
    for serpent in VAR.liste_serpents:
        text = VAR.font.render("JOUEUR " + str(id)+ " : " + str(serpent.score),1,serpent.couleur)
        _fenetre.blit(text, (x, 10))
        x += 40 + text.get_width()
        id +=1

 
