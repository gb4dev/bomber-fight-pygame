# -*- coding: utf8 -*-
import pygame # importation de la librzirie pygame
pygame.init() # initialisation de pygame
pygame.mixer.init() # initialisation du module de musique
fenetre=pygame.display.set_mode((450,330)) # creation de la fenetre du jeu
from fonctions_et_constantes import * # importation des fonctions et variables d'un autre fichier
from niveau import * # importation de la classe niveau
from joueur import * # importation de la classe joueur
from bombes import * # importation de la classe bombes



pygame.display.set_caption("bomberman") # modification du nom de la fenetre du jeu
pygame.display.set_icon(image_logo) # modification de l'icone de la fenetre du jeu
pygame.mixer.music.load("musiques\\musique_menu.wav") # chargement de la musique de menu
pygame.mixer.music.play(-1) # lanement de la musique

horloge = pygame.time.Clock() # creation de l'horloge du jeu qui permet de modifier le framerate

niveau = Niveau() # creation d'un objet niveau
bombes = Bombes() # creation d'un objet bombes

while continuer : # boucle principale contenant les autres boucles du jeu
    horloge.tick(30) # mise a jour du framerate
    
    while menu :
        horloge.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #si on appuy sur la croix rouge par exemple 
                menu = 0
                continuer = 0#le programme s'arrete et la fenetre se ferme

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                menu = 0
                continuer = 0           
                
                
                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1: #si on appui sur le clic gauche de la souris

                if 410 < event.pos[0] < 448 and 10 < event.pos[1] < 48 :
                    if 0.3 >= valeur_son >= 0.1 :
                        valeur_son = 0
                    elif valeur_son <= 0.1:
                        valeur_son = 1
                    else :
                        valeur_son -= 0.2
                        
                    if 1.1 >= valeur_son >= 0.7:
                        compteur_son = 0
                    elif 0.7 >= valeur_son >= 0.3 :
                        compteur_son = 1
                    elif 0.3 >= valeur_son >= 0.1 :
                        compteur_son = 2
                    else : 
                        compteur_son = 3
                    bouton_s = liste_bouton_son[compteur_son]
                    pygame.mixer.music.set_volume(valeur_son)
                    
                if 125 < event.pos[0] < 265 and 170 < event.pos[1] < 210:
                    bouton_sc = bouton_score2
                    #print "TU VEUX VOIR TON SCORE ?" # permet de savoir dans la console si je me trouve dans la zone du bouton

            #bouton quitter
                elif 125 < event.pos[0] < 265 and 220 < event.pos[1] < 260:
                    bouton_q = bouton_quitter2
                    #print "TU VEUX QUITTER LE MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton
                    
            #bouton jeu
                elif 125 < event.pos[0] < 265 and 120 < event.pos[1] < 160:
                    #print "TU VEUX JOUER ?" # permet de savoir dans la console si je me trouve dans la zone du bouton
                    bouton_j = bouton_jouer2
                    bouton_r = bouton_retour
            #relachement du bouton gauche
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 125 < event.pos[0] < 265 and 220 < event.pos[1] < 260:
                    bouton_q = bouton_quitter
                    #print "TU VA QUITTER LE MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton
                    continuer = 0
                    menu = 0
                    break
                    
                #bouton scores
                if 125 < event.pos[0] < 265 and 170 < event.pos[1] < 210:
                    bouton_sc = bouton_score
                    #print "TU VEUX VOIR TON SCORE ?" # permet de savoir dans la console si je me trouve dans la zone du bouton
                    scores = 1
                    menu = 0
                    break
                
                elif 125 < event.pos[0] < 265 and 120 < event.pos[1] < 160:
                    #print "TU VA JOUER !" # permet de savoir dans la console si je me trouve dans la zone du bouton
                    bouton_j = bouton_jouer
                    menu =0
                    choix_niveau = 1
                    anim(fenetre,images_animation,fond,270,255,450)
                    anim(fenetre,images_animation,fond2,0,115,210)
                    animation = 1
                    
        #affichage dans la fenetre
        fenetre.blit(fond, (0,0))
        fenetre.blit(image_face,(270,255))
        fenetre.blit(bouton_j, (125,120))
        fenetre.blit(bouton_q, (125,220))
        fenetre.blit(bouton_sc, (125,170))
        fenetre.blit(bouton_s, (400,10))
        if not animation :
            pygame.display.flip() #actualise la fenetre en permanence, sans ça la fenetre ne renverra aucune donnée on ne verra donc que son aspect graphique
        
    animation = 0

    while choix_niveau :
        horloge.tick(30)  #Limitation de la vitesse de la boucle à 30 frames(images) par secondes    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #si on appuy sur la croix rouge par exemple 
                choix_niveau = 0 #le programme s'arrete et la fenetre se ferme
                continuer = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                    pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1: #si on appui sur le clic gauche de la souris
                #pour le son
                if 410 < event.pos[0] < 448 and 10 < event.pos[1] < 48 :
                    if 0.3 >= valeur_son >= 0.1 :
                        valeur_son = 0
                    elif valeur_son <= 0.1:
                        valeur_son = 1
                    else :
                        valeur_son -= 0.2
                        
                    if 1.1 >= valeur_son >= 0.7:
                        compteur_son = 0
                    elif 0.7 >= valeur_son >= 0.3 :
                        compteur_son = 1
                    elif 0.3 >= valeur_son >= 0.1 :
                        compteur_son = 2
                    else : 
                        compteur_son = 3
                    bouton_s = liste_bouton_son[compteur_son]
                    pygame.mixer.music.set_volume(valeur_son)

                    
                if 57 < event.pos[0] < 200 and 190 < event.pos[1] < 230:
                    bouton_n1 = bouton_niveau1_2
                    fichier = "map1.txt"
                    #print "TU VA CHOISIR LE NIVEAU 1"
                    
                elif 250 < event.pos[0] < 393 and 190 < event.pos[1] < 230:
                    bouton_n2 = bouton_niveau2_2
                    fichier = "map2.txt"
                    #print "TU VA CHOISIR LE NIVEAU 2"
                    
                #bouton quitter
                elif 154 < event.pos[0] < 297 and 240 < event.pos[1] < 280:
                    bouton_q = bouton_quitter2                   
                    #print "TU VEUX QUITTER LE MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton    

                #bouton retour
                elif 154 < event.pos[0] < 297 and 285 < event.pos[1] < 325:
                    bouton_r = bouton_retour2                   
                    #print "TU VEUX RETOURNER AU MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton


            elif event.type == pygame.MOUSEBUTTONUP and event.button ==1: #si on appui sur le clic gauche de la souris
                if 57 < event.pos[0] < 200 and 190 < event.pos[1] < 230:
                    bouton_n1 = bouton_niveau1
                    #print "TU VA CHOISIR LE NIVEAU 1"
                    choix_niveau = 0
                    initialisation = 1
                    break
                elif 250 < event.pos[0] < 393 and 190 < event.pos[1] < 230:
                    bouton_n2 = bouton_niveau2
                    #print "TU VA CHOISIR LE NIVEAU 2"
                    choix_niveau = 0
                    initialisation = 1
                    break
                #bouton quitter
                elif 154 < event.pos[0] < 297 and 240 < event.pos[1] < 280:
                    bouton_q = bouton_quitter                    
                    #print "TU VEUX QUITTER LE MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton
                    continuer = 0
                    choix_niveau = 0
                    break
                #bouton retour
                elif 154 < event.pos[0] < 297 and 285 < event.pos[1] < 325:
                    bouton_r = bouton_retour                   
                    #print "TU VEUX RETOURNER AU MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton                    
                    menu = 1
                    choix_niveau = 0
                    break
                    
    #affichage dans la fenetre
        fenetre.blit(fond2, (0,0))
        fenetre.blit(image_face,(210,115))
        fenetre.blit(bouton_n1, (57,190))
        fenetre.blit(bouton_n2, (250,190))
        fenetre.blit(bouton_s, (400,10))
        fenetre.blit(bouton_q, (154,240))
        fenetre.blit(bouton_r, (154,285))
        pygame.display.flip()  #actualise/rafraichi la fenetre
    
    
    while initialisation : #boucle pour initialiser le jeu
        horloge.tick(30) # mise a jour du framerate
        sauvegarder = 1 # variable mise a 1 pour indiquer qu'il faut sauvegarder
        niveau.generer_niveau(fichier) # generation de la carte du jeu
        liste_joueurs = [] # initialisation de la variable
        bombes.reset_bombes() # mise a 0 des bombes pour effacer les bombes de la partie precedente
        egaliter = 0 # variable a 0 pour indiquer qu'il n'y a plus egalité s'il y avait egalité a la partie précédente
        joueur_gagnant = "" # effacement du joueur gagnant de la partie précédente
        nom_j1 = demander_nom(fenetre,'1',fond_noms) # creation du nom du joueur 1 grace a la fonction demander nom
        nom_j2 = demander_nom(fenetre,'2',fond_noms) # creation du nom du joueur 2
        while nom_j2 == nom_j1 : # si le joueur 2 a entré le meme nom que le joueur 1
            nom_j2 = demander_nom(fenetre,'2',fond_noms) # demande du nom du joueur 2
        liste_joueurs.append(Joueur((1,1),nom_j1)) # ajout du joueur 1 dans la liste des joueurs
        liste_joueurs.append(Joueur((13,9),nom_j2)) # ajout du joueur 2 dans la liste des joueurs
        initialisation = 0 # variable initialisation mise a 0 pour ne pas initialiser 2 fois (on sort de la boucle)
        instructions = 1 # mise a 1 de la variable pour entrer dans la prochaine boucle

    while instructions : # boucle qui affiche les commandes du jeu et les ameliorations possibles a obtenir
        horloge.tick(30) # mise a jour du framerate
        for event in pygame.event.get(): # boucle for pour parcourir les evenements
            if event.type == pygame.QUIT : # si l'utilisateur a appuyé sur la croix de la fenetre
                instructions = 0 # on met la variable 0 pour sortir de la boucle instructions
                continuer = 0 # on met la variable a 0 pour sortir de la boucle principal et quitter le jeu
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN : # si l'utilisateur a cliquer ou appuyé sur une touche
                instructions = 0 # on met la variable a 0 pour sortir de la boucle instructions
                jeu = 1 # variable jeu mise a 1 pour entrer dans la boucle pour jouer
                compte_a_rebours = 1 # variable compte a rebour a 1 pour faire le compteur avant le debut de la partie
                pygame.mixer.music.stop() # arret de la musique
        fenetre.blit(fond_instructions,(0,0)) # affichage de l'image des instructions
        pygame.display.flip() # rafraichissement des images de la fenetre

    while jeu : #boucle de jeu
        horloge.tick(30) # mise a jour du framerate
        while compte_a_rebours :#boule du compte a rebours
            son_compteur.play() # joue le son du compteur
            compte_rebours(fenetre,niveau,liste_joueurs,(surf_timer_partie,rect_timer_partie)) # lance un compte a rebour avant le debut de partie
            compte_a_rebours = 0 # on met la variable du compte a rebour a 0 pour ne pas le faire plusieurs fois
            pygame.event.clear() # effacement des evenements car si un joueur a appuyé sur des touches elles seront comptés dans le jeu
            timer_partie = time.time() # initialisation du timer de la partie
            pygame.mixer.music.load("musiques\\musique_jeu.mp3") # chargement de la musique du jeu
            pygame.mixer.music.play(-1) # lancement de la musique
                
                    
        for event in pygame.event.get(): # boucle qui parcour les evenements
            if event.type == pygame.QUIT : # si le joueur veux quitter
                jeu=0 # mise a 0 de la boucle jeu pour sortir de la boucle du jeu
                continuer=0 # mise a 0 de la boucle principale pour quitter le jeu
            if event.type == pygame.KEYDOWN : # si l'evenement est une touche appuyé
                if event.key == pygame.K_p : # si la touche p est appuyé
                    font_pause = pygame.font.Font(None, 60) # on initialise la police de caractere
                    texte_pause = "PAUSE" # on cree une variable avec le texte pause 
                    surf_pause = font_pause.render(texte_pause,0,(255,255,255)) # on cree la surface du texte pause
                    rect_pause = surf_pause.get_rect(centerx=225,centery=165) # on cree le rectangle pour la position de la surface
                    afficher_items(fenetre,niveau,liste_joueurs,(surf_timer_partie,rect_timer_partie),(surf_pause,rect_pause)) # appel de la fonction afficher_items pour afficher les images du jeu
                    timer_partie = pause(bombes,timer_partie) # on met a jour le timer de la partie en appelant la fonction qui met en pause le jeu
                if liste_joueurs[0].get_vivant() == True : # si le joueur 1 est vivant
                    if event.key == pygame.K_a : # si la touche q (on met a car la librairie comprend que le qwerty) est appuyé
                        liste_directions[0] = "gauche" # on modifie la direction du joueur 1 dans la liste des directions des joueurs
                    if event.key == pygame.K_d : 
                        liste_directions[0] = "droite"
                    if event.key == pygame.K_w : 
                        liste_directions[0] = "haut"
                    if event.key == pygame.K_s :
                        liste_directions[0] = "bas"
                    if event.key == pygame.K_SPACE :
                        liste_joueurs[0].poser_bombe(niveau,bombes)
                        
                if liste_joueurs[1].get_vivant() == True:
                    if event.key == pygame.K_LEFT :
                        liste_directions[1] = "gauche"
                    if event.key == pygame.K_RIGHT :
                        liste_directions[1] = "droite"
                    if event.key == pygame.K_UP :
                        liste_directions[1] = "haut"
                    if event.key == pygame.K_DOWN :
                        liste_directions[1] = "bas"
                    if event.key == pygame.K_KP0 :
                        liste_joueurs[1].poser_bombe(niveau,bombes)

                if event.key == pygame.K_KP1 :
                    print niveau.liste_bombes,liste_joueurs[0].rect_image
                    
            elif event.type == pygame.KEYUP :
                if liste_joueurs[0].get_vivant() == True :
                    if event.key == pygame.K_w and liste_directions[0] == "haut": # si la touche z est appuyé et que la direction est la meme, on efface la direction pour ne pas quil continue a se déplacer
                        liste_directions[0] = ""
                    elif event.key == pygame.K_a and liste_directions[0] == "gauche":
                        liste_directions[0] = ""
                    elif event.key == pygame.K_s and liste_directions[0] == "bas":
                        liste_directions[0] = ""
                    elif event.key == pygame.K_d and liste_directions[0] == "droite":
                        liste_directions[0] = ""

                if liste_joueurs[1].get_vivant() == True:
                    if event.key == pygame.K_LEFT and liste_directions[1] == "gauche":
                        liste_directions[1] = ""
                    elif event.key == pygame.K_RIGHT and liste_directions[1] == "droite":
                        liste_directions[1] = ""
                    elif event.key == pygame.K_UP and liste_directions[1] == "haut":
                        liste_directions[1] = ""
                    elif event.key == pygame.K_DOWN and liste_directions[1] == "bas":
                        liste_directions[1] = ""
                    
        #actualisation des elements du jeu
        surf_timer_partie = font_timer_partie.render(str(int(temps_partie-(time.time()-timer_partie))),0,(255,255,255)) # mise a jour de la surface du timer
        niveau.actualiser() # appel de la methode actualiser de l'objet niveau
        bombes.actualiser(niveau) # appel de la methode actualiser de l'objet bombes
        for joueur in liste_joueurs : # boucle qui parcour la liste des joueurs
            joueur.actualiser(liste_directions[liste_joueurs.index(joueur)],niveau,bombes) # actualisation des joueurs
        if liste_joueurs[0].get_vivant() == 0 and liste_joueurs[1].get_vivant() == 0 : # si les deux joueurs ne sont plus vivant
            afficher_items(fenetre,niveau,liste_joueurs,(surf_timer_partie,rect_timer_partie)) # affichage des images ( pour montrer qu'ils sont dans une explosion)
            egaliter = 1 # variable mise a 1 pour iniquer qu'il y a égalité
            jeu = 0 # mise a 0 de la variable jeu pour sortir de la boucle jeu
            fin_partie = 1 # variable mise a 1 pour pouvoir entrer dans la boucle de fin de partie
            pygame.mixer.music.stop() # arret de la musique
            son_fin.play() # lance le son de la fin de partie
            pygame.time.delay(3000) # délais de 3 secondes ( le temps du son)
            
        else : # si les deux joueurs son vivant
            for joueur in liste_joueurs : # on parcour la liste des joueurs
                if joueur.get_vivant() == False : # si le joueur n'est plus vivant
                    afficher_items(fenetre,niveau,liste_joueurs,(surf_timer_partie,rect_timer_partie)) # affichage des images ( pour montrer que le joueur s'est pris l'explosion)
                    del liste_joueurs[liste_joueurs.index(joueur)] # supression du joueur dans la liste des joueurs
                    joueur_gagnant = liste_joueurs[0].get_nom_joueur() # affectation du joueur gagnant
                    fin_partie = 1 # mise a 1 de la varible pour pouvoir entrer dans la boucle de fin de partie
                    jeu = 0 # mise a 0 de la variable jeu pour sortir de la boucle jeu
                    pygame.mixer.music.stop() # arret de la musique
                    son_fin.play() # lance le son de la fin de partie
                    pygame.time.delay(3000) # delais de 3 secondes (le temps du son)
                    break # on sort de la boucle for
        if temps_partie-(time.time()-timer_partie) <= 0 : # si le temps est ecoulé
            afficher_items(fenetre,niveau,liste_joueurs,(surf_timer_partie,rect_timer_partie)) # affichage des images
            temps_ecouler = 1 # mise a 1 la variable pour indiquer que le temps est ecoulé
            fin_partie = 1 # mise a 1 de la variable pour pouvoir entrer dans la boucle de fin de partie
            jeu = 0 # mise a 0 de la varible jeu pour sortie de la boucle jeu
            pygame.mixer.music.stop() # arret de la musique
            son_fin.play() # lance le son de fin de partie
            pygame.time.delay(3000) # delais de 3 secondes
        
            
                    
            #affichage des elements du jeu
        afficher_items(fenetre,niveau,liste_joueurs,(surf_timer_partie,rect_timer_partie)) # affichage des images

    while fin_partie: # boucle de fin de partie
        horloge.tick(30)
        if sauvegarder : # si la variable sauvegarder est a 1
            son_fin.stop()
            pygame.mixer.music.load("musiques\\musique_menu.wav") # chargement de la musque du menu
            pygame.mixer.music.play(-1) # -1 pour jouer la musique en boucle ( a linfini)
            if joueur_gagnant != "" : # si il y a un joueur gagnant
                enregistrer_scores(joueur_gagnant) # appel de la fonction pour enregistrer les scores
            sauvegarder = 0 # mise a 0 de la variable sauvegarder pour ne pas sauvegarder plusieurs fois
        if egaliter : # si il y a eu égalité
            surf_texte_egaliter = font_fin_partie.render(u"égalité...",0, (255,255,255)) # creation de la surface du texte égalité
            rect_texte_egaliter = surf_texte_egaliter.get_rect(x=265,y=285) # creation du rect de la position du texte
        elif temps_ecouler == 1 : # si il y a eu temps écoulé
            surf_texte_temps_ecouler1 = font_fin_partie.render(u"temps",0, (255,255,255)) # creation de la surface du texte "temps"
            rect_texte_temps_ecouler1 = surf_texte_temps_ecouler1.get_rect(x=275,y=270) # creation du rect de la position du texte "temps"
            surf_texte_temps_ecouler2 = font_fin_partie.render(u"ecoulé...",0, (255,255,255)) # creation de la surface du texte "écoulé"
            rect_texte_temps_ecouler2 = surf_texte_temps_ecouler2.get_rect(x=270,y=290) # creation du rect de la position du texte "écoulé"
        else : # sinon si il y a un gagnant
            texte_gagnant = [u"Le joueur",joueur_gagnant,u"a gagné !"] # creation de la liste des mots a convertir
            surf_texte1 = font_fin_partie.render(texte_gagnant[0],0, (255,255,255)) # creation de la surface du texte "le joueur"
            surf_texte2 = font_fin_partie.render(texte_gagnant[1],0, (255,255,255)) # creation de la surface du texte du joueur gagnant"
            surf_texte3 = font_fin_partie.render(texte_gagnant[2],0, (255,255,255)) # creation de la surface du texte "a gagné"
            rect_texte1 = surf_texte1.get_rect(x=260,y=260) # creation du rect de la position du texte "le joueur"
            rect_texte2 = surf_texte2.get_rect(centerx=310,centery=290) # creation du rect de la position du texte du joueur gagnant
            rect_texte3 = surf_texte3.get_rect(x=270,y=300) # creation du rect de la position du texte " a gagné"
        for event in pygame.event.get(): # boucle qui parcour les evenements
            if event.type == pygame.QUIT:  #si on appuy sur la croix rouge par exemple 
                pygame.quit() #le programme s'arrete et la fenetre se ferme
            if event.type == pygame.KEYDOWN : # si une touche est appuyé
                if event.key == pygame.K_ESCAPE : # la touche echap est appuyé
                    pygame.quit() # on quitte totalement le jeu
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1: #si on appui sur le clic gauche de la souris
                if 410 < event.pos[0] < 448 and 10 < event.pos[1] < 48 :
                    if 0.3 >= valeur_son >= 0.1 :
                        valeur_son = 0
                    elif valeur_son <= 0.1:
                        valeur_son = 1
                    else :
                        valeur_son -= 0.2
                        
                    if 1.1 >= valeur_son >= 0.7:
                        compteur_son = 0
                    elif 0.7 >= valeur_son >= 0.3 :
                        compteur_son = 1
                    elif 0.3 >= valeur_son >= 0.1 :
                        compteur_son = 2
                    else : 
                        compteur_son = 3
                    bouton_s = liste_bouton_son[compteur_son]
                    pygame.mixer.music.set_volume(valeur_son)
                #bouton retour
                if 5 < event.pos[0] < 148 and 20 < event.pos[1] < 63:
                    bouton_m = bouton_menu2                   
                    #print "TU VEUX RETOURNER AU MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton                    
                #bouton quitter
                elif 1 < event.pos[0] < 144 and 73 < event.pos[1] < 116:
                    bouton_q = bouton_quitter2                    
                    #print "TU VEUX QUITTER LE MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton
                #bouton scores
                if 1 < event.pos[0] < 144 and 126 < event.pos[1] < 169:
                    bouton_sc = bouton_score2
                    #print "TU VEUX VOIR TON SCORE ?" # permet de savoir dans la console si je me trouve dans la zone du bouton
                    
            elif event.type == pygame.MOUSEBUTTONUP and event.button ==1: #si on appui sur le clic gauche de la souris
                #bouton retour
                if 5 < event.pos[0] < 148 and 20 < event.pos[1] < 63:
                    bouton_m = bouton_menu                   
                    #print "TU VEUX RETOURNER AU MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton                    
                    menu = 1
                    fin_partie = 0
                    break
                 #bouton scores
                if 1 < event.pos[0] < 144 and 126 < event.pos[1] < 169:
                    bouton_sc = bouton_score
                    scores = 1
                    fin_partie = 0
                    #print "TU VEUX VOIR TON SCORE ?" # permet de savoir dans la console si je me trouve dans la zone du bouton
                #bouton quitter
                elif 1 < event.pos[0] < 144 and 73 < event.pos[1] < 116:
                    bouton_q = bouton_quitter
                    #print "TU VA QUITTER LE MENU !" # permet de savoir dans la console si je me trouve dans la zone du bouton
                    fin_partie = 0
                    continuer = 0
        #affichage dans la fenetre
        fenetre.blit(fond3, (0,0))
        fenetre.blit(bouton_s, (400,10))
        fenetre.blit(bouton_m, (5,20))
        fenetre.blit(bouton_q, (1,73))
        fenetre.blit(bouton_sc, (1,126))
        if egaliter : # si il y a eu égalité
            fenetre.blit(surf_texte_egaliter,rect_texte_egaliter) # on afffiche le texte "égalité"
        elif temps_ecouler == 1 : # sinon si le temps etait ecoulé 
            fenetre.blit(surf_texte_temps_ecouler1,rect_texte_temps_ecouler1) # on affiche le texte "temps"
            fenetre.blit(surf_texte_temps_ecouler2,rect_texte_temps_ecouler2) # puis en dessous le texte "écoulé"
        else : # sinon si il y a eu un gagnant
            fenetre.blit(surf_texte1,rect_texte1) # on affiche le texte "le joueur"
            fenetre.blit(surf_texte2,rect_texte2) # puis en dessous le texte du nom du joueur
            fenetre.blit(surf_texte3,rect_texte3) # puis encore en dessous le texte "à gagné"
        pygame.display.flip() #rafraichissement de la fenetre


    while scores : #boucle pour afficher les scores
        scores = recuperer_scores() # on affecte les scores recupérés dans une variable grace a la fonction recuperer_scores
        bouton_m = bouton_menu # on affecte l'image du gros bouton menu a la variable qui affichera le bouton
        rect_bouton_menu = bouton_menu.get_rect(center=(450-bouton_menu.get_width()/2,330-bouton_menu.get_height()/2)) # on cree le rect de la position du bouton menu
        affichage = 1 # variable mise a 1 pour 
        
        if scores == None : # si il n'y a pas de scores (c'est a dire qu'aucune partie n'a été gagné)
            font = pygame.font.Font(None, 50) # on initialise la police de caractère (none signifie police par défaut et 50 la taille je crois)
            surf_texte = font.render(u"Pas de scores trouvés",0, (255,255,255)) # création de la surface du texte "pas de scores trouvés"
            rect_texte = surf_texte.get_rect() # récupération du rect de l'image
            rect_texte.center = fenetre.get_rect().center # positionnement du rect de l'image (on place le texte au centre de la fenetre)
        else: # sinon si il y a des scores
            scores_trier = trier_scores(scores) # on trie les scores par ordre décroissant (celui qui a le plus de point est premier etc...) grace a la fonction trier_scores
            
        while affichage : # boucle qui permet d'afficher les elements et d'utiliser les evenements pour ne pas initialiser plusieurs fois les scores, textes et polices de caracteres
            horloge.tick(30)
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT :
                    scores=0 # misse a 0 pour quitter la boucle des scores
                    affichage = 0 #mise a 0 pour quitter la boucle d'affichage des scores
                    continuer=0 # mise a 0 pour quitter totalement le jeu
                    break # on sort des conditions
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    if event.pos[0] > 450-bouton_menu.get_width() and event.pos[1] > bouton_menu.get_height() : # si on clic sur le bouton menu
                        bouton_m = bouton_menu2 # on reduit la taille du bouton en affectant une image plus petite
                        
                elif event.type == pygame.MOUSEBUTTONUP :
                    boutom_m = bouton_menu # on regrossi le bouton
                    scores = 0 # pour sortir de la boucle scores
                    affichage = 0 #pour sortir de la boucle affichage
                    menu = 1 # pour entrer dans la boucle menu (retourne au menu principal)
                    
            fenetre.blit(fond_scores,(0,0)) # affiche l'image de font
            fenetre.blit(bouton_m,rect_bouton_menu) # affiche le bouton menu
            if scores == None : # si il n'y a pas de scores
                fenetre.blit(surf_texte,rect_texte) # on affiche le texte "pas de scores trouvés"
            else : # sinon si il y a des scores
                afficher_scores(fenetre,scores_trier) # on affiche les scores grace a la fonction afficher_scores
                
            pygame.display.flip() # raffraichissement de la fenetre
            

pygame.quit() # permet de liberer la memoire (quitte pygame)
