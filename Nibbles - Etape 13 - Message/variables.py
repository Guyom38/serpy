# -----------------------------------------------------------------------------
# --- CONSTANTES
# -----------------------------------------------------------------------------

# --- Quelques couleurs ...
COULEUR_MUR = (0,128,0)
COULEUR_FOND = (20,0,20)
COULEUR_FOND_ECRAN = (16,16,16)
COULEUR_BLANC = (255,255,255)
COULEUR_NOIR = (0,0,0)
COULEUR_ROUGE = (255,0,0)
COULEUR_BLEU = (0,0,255)
COULEUR_ORANGE = (255,128,0)


# --- Titre du jeu
TITRE = "SerPy"

# --- Taille de la fenêtre
ECRAN_X = 800
ECRAN_Y = 600

# --- Hauteur a enlever au terrain de jeu
# --- Cela permet d'afficher des informations comme le score
HAUTEUR_ZONE_INFOS = 32

# --- Petite marge tout au tour du terrain, esthétique !
MARGE_CADRE_MIN = 32

# --- boucle du jeu
# --- si FAUX (False) le jeu s'arrete
boucle_active = True

# -----------------------------------------------------------------------------
# --- MECANISME POUR LES MESSAGES
# -----------------------------------------------------------------------------

# --- indique si le message doit-être afficher avant de jouer
jeu_suspendu = True
# --- indique la raison du message (NOUVEAU NIVEAU, PARTIE TERMINEE)
jeu_suspendu_raison = "NOUVEAU NIVEAU"
# --- compteur
jeu_suspendu_timer = 0

# --- longueur du serpent au début de la partie (tete comprise)
LONGUEUR_DU_SERPENT_AU_DEBUT = 2

# --- nombre de joueurs dans la partie
nb_joueurs = 2

# --- position des joueurs au début de la partie
position_initial_joueur1 = (10, 10)
position_initial_joueur2 = (70, 50)

# --- vitesse par defaut du serpent,
# --- plus la valeur est petite, plus il va vite !
vitesse = 0.10

# --- structure du menu (DICTIONNAIRE)
MENU_CHOIX = {'JOUEUR' : ['1 - SOLO 1 JOUEUR', '2 - DUEL 2 JOUEURS'], 
               'DIFFICULTE' : ['1 - FACILE', '2 - NORMAL', '3 - DIFFICILE']}

# --- menu doit être afficher si VRAI (True)
menu = True

# --- menu a afficher
menu_select = "JOUEUR"

# --- niveau en cours
niveau = 0

# --- nombre de pommes mangées par les serpents,
# --- compteur qui permet de savoir si l'on passe au niveau suivant.
pommes_mangees = 0

# --- nombre de pommes a manger pour passer au niveau suivant.
nb_pommes_niveaux_suivant = 3