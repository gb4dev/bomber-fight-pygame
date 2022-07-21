# -*- coding: utf-8 -*-
"""Variables et fonctions du jeu Bomberman"""
import os # impoortation du module os
import pygame # importation du module pygame
from random import choice # importation de la fonction choice du module random
import pickle # importation du module pickle
import time # importation du module time
import operator # importation du module operator

def afficher_items(fenetre,niveau,liste_joueurs,timer,extra = 0) :
    """fonction permettant d'afficher les éléments du jeu dans la fenetre,
    elle prend en parametres la fenetre dans laquelle afficher les images,
    l'objet niveau, la liste des jouers, le timer de la partie (une liste avec la surface et le rect),
    et une derniere image facultative (utilisé pour la pause du jeu et le compte a rebours)"""
    niveau.afficher_carte(fenetre) # affichache de la carte grae a la methode afficher de la classe niveau
    for joueur in liste_joueurs : # boucle qui parcour la liste des joueurs
        joueur.afficher(fenetre) # affichage des joueurs grace a leur methode afficher
    fenetre.blit(timer[0],timer[1]) # affichage du timer
    if extra != 0 : # si on a passé un 6e élément
        fenetre.blit(extra[0],extra[1]) # on affiche cet élément
    pygame.display.flip() #rafraichissement de la fenetre

def anim(fenetre,images,fond,x,y,xfin):
    """fonction qui fait une animation d'un personnage se déplacant de gauche a droite,
    elle prend en parametres la fenetre sur laquelle afficher les elements,
    la liste des images de l'animation,l'image de fond,la positionx et y de départ du personnage,
    et la position x jusqu'ou doit se deplacer le personnage"""
    compt_image = 0 # initialisation de la variable d'indice des images (pour choisir l'image dans la liste)
    animation = 1 # variable pour la boucle dd'animation, si a 1 il y a animation , si 0 l'animation est fini
    debut = time.time() # recupération du temps actuel et affectation de ce temps dans une variable
    fenetre.blit(fond, (0,0)) # affichage du fond
    fenetre.blit(images[0],(x,y)) # affiche de la premiere image
    pygame.display.flip() # raffraichissement de la fenetre
    while animation : # boucle d'animation
        for event in pygame.event.get(): # evenements...
            if event.type == pygame.QUIT: # pour quitter...
                pygame.quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN : # si l'utilisateur appui sur une touche ou clique pendant l'animation
                animation = 0 # variable animation mise a 0 pour passer l'animation (skip)
        if time.time()-debut >= 0.05: # si 0.05 secondes se sont ecoulés apres le changement d'image
            debut = time.time() # reaffectation temps actuel dans la variable
            compt_image += 1 # incrementation du compteur d'images
            if compt_image >= len(images) : # si la valeur compteur d'image est plus grande que la taille de la liste
                compt_image = 0 # on remet la variable a 0
        if x < xfin : # si la position du personnage est inférieure a la position finale voulu
            x += 5 # on incrémente de 5 la position actuelle
        else : # sinon si il a atteint la position finale voulu
            animation = 0 # on met la variable a 0 pour quitter la boucle
        
        fenetre.blit(fond, (0,0)) #affichage du fond
        fenetre.blit(images[compt_image],(x,y)) # affichage de l'image du perso
        pygame.display.flip() # raffraichissement 
        pygame.time.wait(50) # pause de 50ms entre chaque tour de boucle

def load_png(name):
    """Charge une image et retourne un objet image, elle prend en parametres le nom de l'image a charger"""
    fullname = os.path.join('images', name) # chemin complet de l'image
    try: #bloc de test pour eviter les erreurs
            image = pygame.image.load(fullname) # chargement de l'image
            if image.get_alpha() is None: # si l'image ne contient pas contient de transparence
                    image = image.convert() # on convertie simplement l'image
            else: # sinon si l'image a du transparent
                    image = image.convert_alpha() # on convertie l'image en enlevent la transparence (on decoupe l'image)
    except pygame.error, message: #si il y a une erreur
            print "Impossible de charger l'image : ", fullname
            print message
            raise SystemExit, message
    return image # on retourne l'image chargé

def remplacer_block() :
    """fonction qui choisi au hasard une lettre dans une liste
    (les lettres représentent des elements de la carte), puis renvois cette lettre choisie"""
    liste = ['s','t','0','n','t','0','s','n','t','0','n','s','t','0','n','s','0','s'] # liste contenant les lettres pour "imiter" des probalbilités
    return choice(liste) # retourne une lettre choisi dans la liste avec la fonction choice

def demander_nom(fenetre,joueur,fond) :
    """fonction qui demande les nom d'un joueur,
    elle prend en parametres la fenetre pour entrer le nom,
    le texte pour identifier le joueur ("joueur 1" ou "joueur 2"),
    et l'image de fond"""
    nom = "" # initialisation de la variable qui contiendra le nom du joueur
    texte = "entrez le nom du joueur {} :".format(joueur) # initialisation du texte qui sera affiché
    font = pygame.font.Font(None, 35) # creation de la police de caractere pour gerer l'affichage de texte
    surf_texte = font.render(texte,0, (255,255,255)) # initialisation de la surface du texte
    rect_texte = surf_texte.get_rect(centerx=fenetre.get_width()/2,centery=50) #initialisation du rect de la position de la surface du texte
    while True : # boucle infinie ( qui peut etre quitté par un return)
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT :
                    pygame.quit()
                if evt.type == pygame.KEYDOWN: # si une touche est appuyé
                    if evt.unicode.isalpha() and len(nom)<10: # si la touche appuyé est une lettre normale et que le nom fait moins de 10 carateres
                        nom += evt.unicode # ajout de la lettre appuyé
                    elif evt.key == pygame.K_BACKSPACE: # si la touche est la touche retour/suppr
                        nom = nom[:-1] # on enleve le dernier caractere du nom
                    elif evt.key == pygame.K_RETURN: # si la touche appuyé est "entrée"
                        if nom != "" : # si le nom n'est pas vide
                                return nom # on renvois le nom
                elif evt.type == pygame.QUIT:
                    pygame.quit() # pour quitter...
            fenetre.blit(fond,(0,0)) # affichage de l'image de fond
            block = font.render(nom, 0, (255, 255, 255)) # creation de la surface qui contient le nom du joueur
            rect = block.get_rect() # creation du rect de la surface
            rect.center = fenetre.get_rect().center # on centre le rect pour afficher le nom au millieu de la fenetre
            fenetre.blit(block, rect) # affichage du nom
            fenetre.blit(surf_texte,rect_texte) # affichage de la phrase qui demande le nom
            pygame.display.flip() #rafraichissement de la fenetre
        
                
def compte_rebours(fenetre,niveau,liste_joueurs,timer):
    """"fonction qui affiche et gere un compte a rebours de 3 secondes puis affiche "GO" a la fin de ce compte a rebours.
    elle prend en parametres la fenetre sur laquelle afficher les elements, l'objet niveau, la liste des joueurs"""
    temps = 3 # initialisation d'une variable contenant la durée du timer
    font = pygame.font.Font(None, 50) # initialisation de la police de caractere pour le texte
    surf_temps = font.render(str(temps), 0, (255, 255, 255)) # creation de la surface du texte du timer
    rect_temps = surf_temps.get_rect() # creation du rect de la position de la surface du texte du timer
    rect_temps.center = fenetre.get_rect().center # mise a jour de la position du rect (le centre du rect est le mileu de la fenetre)
    timer_go = time.time()+temps # initialisation du temps actuel + temps durée du compteur pour avoir le temps final
    while timer_go-time.time() > 0  : # boucle qui s'execute si le temps final - temps actuel est supérieur a 0 (si le la durée du compteur n'est pas dépassé)
        temps = int(round(timer_go-time.time())) # # mise a jours de la durée du timer ( qui sera affiché sur la fenetre)
        if temps == 0 : # si la duree est inférieur a 0.5 ( on arrondit quand on la met a jours donc elle apparait a 0)
            surf_temps = font.render("GO !",0,(255,255,255)) # on met a jours la surface avec le texte "GO"
        else : # sinon si c'est supérieur a 0.5
            surf_temps = font.render(str(temps),0,(255,255,255)) # on met a jour la surface avec la durée restante actuelle
    
        afficher_items(fenetre,niveau,liste_joueurs,timer,(surf_temps,rect_temps)) # affichage des elements sur la fenetre
        pygame.display.flip() # rafraichissement de la fenetre

def enregistrer_scores(joueur_gagnant) :
    """fonction permettant d'enregistrer le score de la partie (elle ajoute 1 au score du joeur gagnant),
    elle prend en parametres le nom du joueur gagnant"""
    #actualisation des scores
    scores = recuperer_scores() # recupération des scores
    if scores == None : # si il n'y a pas de cores
            scores = {} # on crée le disctionnaire pour acceuillir les scores et les nom
    try : 
            scores[joueur_gagnant] += 1 # on essaye d'ajouter 1 au score du joueur (si il est déja présent dans le dictionnaire)
    except :
            scores[joueur_gagnant] = 1 # si le joueur n'est pas dans le dictionnaire on l'ajoute dans le dictionnaire et on met son score a 1
#enregistrement dans fichier de sauvegarde
    save=open("scores","wb") # ouverture du fichier des scores
    mon_pickler=pickle.Pickler(save) # utilisation du module permettant d'enregistrer des objets dans un fichier
    mon_pickler.dump(scores) # enregistremen,t des scores dans le fichier
    save.close() # fermeture du fichier

#enregistrement dans fichier txt pour pouvoir le lire en louvrant
    scores_trier = trier_scores(scores) # on tri les scores
    liste_lignes = [] # creation d'une liste vide qui contiendra le texte a ercrire dans le fichier texte
    ligne = "" # initialisation d'une variable vide qui contiendra les lignes de texte une par une
    compteur = 1 # initialisation d'un compteur qui sert de classement
    for score in scores_trier : # boucle qui parcours les scores
            ligne += str(compteur) # ajout du classement dans la ligne de texte
            if compteur < 10 : # si le compteur fait moins de deux caracteres
                    ligne += " " # on ajoute un espace (pour alligner les chiffres/nombres)
            ligne += 3*" " # ajout de 3 espaces dans la ligen de texte
            ligne += score[1] # ajout du nom du joueur dans la ligne de texte
            ligne += (18-len(score[1]))*" " # ajout d'une nombre d'espaces en fonction de la longueure du nom du joueur
            if len(str(score[0])) == 1 : # si le score fait 1 caractere
                    ligne += " " # on ajoute un espace a la ligne du texte
            ligne += str(score[0]) # on ajoute le score a la ligne de texte
            ligne += 7*" " # ajout de 7 espaces a la ligne de texte
            ligne += "\n" # ajout d'un saut de ligne a lla ligne de texte
            compteur += 1 # incrementation de 1 du compteur
            liste_lignes.append(ligne) #ajout de la ligne de texte a la liste contenant les lignes de texte
            ligne = "" # on vide la ligne de texte
    txt = open("scores_txt.txt","w") # on ouvre le fichier texte des scores
    txt.write("      NOM        Parties gagnées \n") # ecriture d'une phrase dans le fichier
    txt.write("\n") # ajout d'un saut de ligne dans le fichier texte
    for ligne in liste_lignes : # boucle qui parcours la liste des lignes de texte
            txt.write(ligne) # ecriture de la ligne de texte
            txt.write("\n") # ajout d'un saut de ligne dans le fichier de texte
    txt.close() # fermeture du fichier texte
        

def recuperer_scores() :
    """fonction permettant de recupperer les scores dans un fichier"""
    try: # test
        save=open("scores","rb") #ouverture du fichier texte
        mon_depickler=pickle.Unpickler(save) # creation de l'objet permettant de recuperer un objet dans un fichier texte
        scores = mon_depickler.load() # recuperation du dictionnaire des scores
        save.close() # fermeture du fichier
    except : #si il y a eu une erreur
        scores = None # on met None sui signifie rien dans la variable scores
    return scores # on retourne les scores recupérés

def trier_scores(scores) :
    """fonction qui trie les scores, elle prend en parametres les scores a trier"""
    liste_scores = [] # initialisation d'une liste qui contiendra les scores recupérés dans le dictionnaire (car un dictionnaire ne se tri pas)
    for nom in scores : # boucle qui parcour les elements du dictionnaire des scores
            liste_scores.append((scores[nom],nom)) # ajout du score et du nom du joueur qui a le score dans un tuple dans la liste des scores
    liste_scores = sorted(liste_scores, key=operator.itemgetter(0)) # on tri la liste avec les scores
    liste_scores.reverse() # la liste a été trié du plus petit au plus grand donc un inverse la liste ( en effet plus on a de point meilleur c'est)
    return liste_scores #on retourne la liste trié

def afficher_scores(fenetre,scores_trier) :
    """fonction qui affiche les scores sur la fenetre, elle affiche seulement les 10 premiers joueurs
    elle prend en parametres la fenetre sur laquelle afficher les scores,
    et les scores triés"""
    scores_trier = scores_trier[:10] # on coupe la liste pour recuperer les 10 meilleurs scores
    posx_nom, posy_nom = 95, 40 # initialisation des position des noms
    posx_score, posy_score = 355, 40 # initialisation de la position des scores
    font = pygame.font.Font(None, 20) # initialisation de la police de caractere du texte
    for score in scores_trier : # boucle qui parcour la liste des scores
            surf_texte = font.render(score[1], 0, (0,0,0)) # creation de la surface du texte du nom du joueur
            fenetre.blit(surf_texte,(posx_nom,posy_nom)) # affichage du nom du joueur sur la fenetre
            surf_texte = font.render(str(score[0]), 0, (0,0,0)) # creation de la surface du texte du score du joueur
            fenetre.blit(surf_texte,(posx_score,posy_score)) # affichage du score du joueur sur la fenetre
            posy_nom += 24 # mise a jour de la position y du nom pour les afficher en colone
            posy_score += 24 # mise a jour de la position y du score pour les afficher en colone


def pause(bombes,timer_partie) :
    """foncion qui permet de mettre le jeu en pause,
    quand cette fonction est appelé le jeu est en pause puis quand on sort de pause on met a jour le temps des bombes et le timer de la partie,
    elle prend en parametres l'objet bombes et le timer de la partie"""
    temps_debut = time.time() # sauvegarde du temps au debut de la pause
    boucle = 1 # variable pour entrer dans la boucle de pause
    while boucle : # tant que l'utilisateur ne sort pas de la pause
        for event in pygame.event.get(): # boucle qui parcour les evenements
            if event.type == pygame.QUIT :
                pygame.quit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_p : #si la touche appué est la touche p
                    boucle = 0 # on met a 0 la variable pour sortir de la boucle de pause donc pour sortir de la pause
    temps_ecouler = time.time()-temps_debut # calcul du temps passé dans la pause
    bombes.set_bombes_pause(temps_ecouler) # mise a jour du temps des bombes ( pour ne pas quelles explosent quand on sort de la pause)
    return timer_partie+temps_ecouler # on renvois le temps de la partie pour ne pas qu'il se soit écoulé du temps pendant la pause


#les images
fond = load_png("fond.png") #on importe une image que l'on "colle" sur la fenetre
fond2 = load_png("fond2.png")
fond3 = load_png("fondfin.png")
fond_scores = load_png("image_scores.png")
fond_noms = load_png("fond_noms.png")
fond_instructions = load_png("instructions_du_jeu.png")
bouton_jouer = load_png("bouton_jouer.png")
bouton_jouer2 = load_png("bouton-jouer2.png")
bouton_quitter = load_png("bouton-quitter.png")
bouton_quitter2 = load_png("bouton-quitter2.png")
bouton_retour = load_png("bouton-retour.png")
bouton_retour2 = load_png("bouton-retour2.png")
bouton_score = load_png("bouton-score.png")
bouton_score2 = load_png("bouton-score2.png")
bouton_niveau1 = load_png("bouton-niveau1.png")
bouton_niveau1_2 = load_png("bouton-niveau1_2.png")
bouton_niveau2 = load_png("bouton-niveau2.png")
bouton_niveau2_2 = load_png("bouton-niveau2_2.png")
bouton_menu = load_png("bouton-menu.png")
bouton_menu2 = load_png("bouton-menu2.png")
bouton_son = load_png("bouton-volume1.png")
bouton_son2 = load_png("bouton-volume2.png")
bouton_son3 = load_png("bouton-volume3.png")
bouton_son4 = load_png("bouton-volume4.png")
image_face = load_png("Bombermanface.png")
images_animation = [load_png("Bombermandroite.png"), load_png("Bombermandroite1.png"), load_png("Bombermandroite2.png")]
liste_bouton_son =[bouton_son,bouton_son2,bouton_son3,bouton_son4]
image_logo = load_png("bombermanlogo.png")

son_fin = pygame.mixer.Sound("musiques\\son_fin.wav")
son_clic = pygame.mixer.Sound("musiques\\son_clic.wav")
son_compteur = pygame.mixer.Sound("musiques\\son_compteur.wav")
# variable permmetant de choisir les images a affficher (grosse image ou petite image)
bouton_j = bouton_jouer
bouton_q = bouton_quitter
bouton_sc = bouton_score
bouton_n1 = bouton_niveau1
bouton_n2 = bouton_niveau2
bouton_s = liste_bouton_son[0]
bouton_r = bouton_retour
bouton_m = bouton_menu
    
#Parametres de la fenetre
nombre_sprite_ligne = 15 # nombre de cases sur une ligne
nombre_sprite_colone = 11 # nombre de cases sur une colone
taille_sprite = 30 # taile d'une case
liste_directions = ["",""] # liste des directions des joueurs
fichier = "" # variable qui contiendra le nom du fichier pour charger le niveau (la carte)
font_fin_partie = pygame.font.Font(None, 30) # initialisation de la police de caracteres du texte de la fin de partie
font_timer_partie = pygame.font.Font(None,40) # initialisation de la police de caracteres du texte du timer
timer_partie = 0 
temps_partie = 180 # durée d'une partie
surf_timer_partie = font_timer_partie.render(str(temps_partie),0,(255,255,255)) # surface du texte du temps de la partie
rect_timer_partie = surf_timer_partie.get_rect(centerx = 225) # rect de la surface du texte du timer de la partie
compteur_son = 0 # compteur pour les images du son
valeur_son = 1 # volume du son (1 = 100%) (0 = 0%)
liste_joueurs = [] # creation de la liste des joueurs
joueur_gagnant = "" # variable qui contiendra le nom du joueur gagnant
temps_ecouler = 0 # variable qui sera a 1 si pendant une partie le temps est ecoulé
initialisation = 0 # variable de boucle
animation = 0
choix_niveau = 0 # variable de boucle
compte_a_rebours = 0 # variable de boucle
menu = 1 # variable de boucle
scores = 0 # variable de boucle
jeu = 0 # variable de boucle
fin_partie = 0 # variable de boucle
continuer = 1 # variable de boucle
egaliter = 0 #variable qui sera a 1 si pendant une partie les deux joueurs perdent en meme temps
sauvegarder = 0 #variable qui sera a 1 pour enregistrer les scores
instructions = 0 # variable de boucle
