# --- ---- Couleurs
COULEUR_MUR = (0,128,0)
COULEUR_FOND = (20,0,20)
COULEUR_FOND_ECRAN = (16,16,16)
COULEUR_BLANC = (255,255,255)
COULEUR_NOIR = (0,0,0)
COULEUR_ROUGE = (255,0,0)
COULEUR_BLEU = (0,0,255)
COULEUR_ORANGE = (255,128,0)


# --- Constantes du jeu
TITRE = "SerPy"

ECRAN_X = 800
ECRAN_Y = 600

HAUTEUR_ZONE_INFOS = 32
MARGE_CADRE_MIN = 32


# --- Variables
boucle_active = True

LONGUEUR_DU_SERPENT_AU_DEBUT = 2

nb_joueurs = 2
position_initial_joueur1 = (10, 10)
position_initial_joueur2 = (70, 50)
vitesse = 0.10

# --- Menu
MENU_CHOIX = {'JOUEUR' : ['1 - SOLO 1 JOUEUR', '2 - DUEL 2 JOUEURS'], 
               'DIFFICULTE' : ['1 - FACILE', '2 - NORMAL', '3 - DIFFICILE']}

menu = True
menu_select = "JOUEUR"