# -*- coding: cp1252 -*-
from fonctions_et_constantes import *
import time

class Bombes() :
    """Objet bombes, représenté par l'image d'une bombe, contients des fonctions pour le fontionnement de ces bombes"""
    def __init__(self) :
        self.liste_bombes = [] # creation de la liste qui contiendra les informations sur chaque bombes 
        self.son_explosion = pygame.mixer.Sound("musiques\\son_explosion.mp3") # initialisation du son de l'explosion d'une bombe

    def actualiser(self,niveau) :
        """fonction actualisant l'etat des bombes, cette fontions prend l'objet niveau en parametre"""
        for bombe in self.liste_bombes : # boucle qui parcour la liste des bombes
            if time.time()-bombe[2] >= 3 and bombe[3] == 0: # condition: si la bombe a été crée il y a plus de 3 secondes et qu'elle n'est pas en etat explosé
                self.exploser(bombe[1][0],bombe[1][1],bombe[5],niveau) # on appelle la fonction exploser en passant en parametres la position de la bombe, la taille de l'explosion et l'objet niveau
                self.son_explosion.play() # on joue le son de l'explosion
            elif time.time()-bombe[2] >= 0.3 and bombe[3] == 1: # condition : si la bombe est en état d'explosion et que cet état a duré 0,3 secondes ou plus
                self.nettoyer(bombe[1][0],bombe[1][1],bombe[5],niveau) # on appelle la fonction nettoyer en passant en parametres la position de la bombe, la taille de l'explosion et l'objet niveau

    def ajouter_bombe(self,nom_joueur,case,niveau,taille_exp) :
        """fonction qui crée une bombe, cettte bombe est une liste qui contient plusieurs caracteristiques :
        le nom du joueur qui l'a posé, la position de la bombe, l'horaire a laquelle elle a été posée,
        l'état de la bombe(0=bombe pas explosé et 1=bombe explosé) et la taille de l'explosion"""
        self.liste_bombes.append([nom_joueur,case,time.time(),0,len(self.liste_bombes),taille_exp]) # ajout de la bombe dans la liste des bombes
        niveau.set_case_structure([case[1],case[0]],'b') # modification du niveau pour indiquer qu'il y a une bombe (on passe la position de la bombe et la lettre qui caracterise une bombe)

    def exploser(self,bombex,bombey,taille_exp,niveau) :
        """fonction générant l'exposion de la bombe, elle prend en parametre la position de la bombe, la taille de l'explosion et l'objet niveau"""
        for bombe in self.liste_bombes : # parcour de la liste des bombes
            if [bombex,bombey] in bombe : #recherche de la bombe passé en parametre
                self.liste_bombes[self.liste_bombes.index(bombe)][3] = 1 # actualisation de l'etat de la bombe (elle passe dans l'état explosé)
                self.liste_bombes[self.liste_bombes.index(bombe)][2] = time.time() # actualisation de l'horaire de la bombe
        structure = niveau.get_structure() # récupération de la structure du niveau
        
        niveau.set_case_structure((bombey,bombex),'e') # modification de niveau pour indiquer qu'il y a une explosion a l'emplacement de la bombe
                                                       #(on passe en parametres la position de la bombe et la lettre qui caracterise l'explosion centrale
        #création des bras de l'explosion de la bombe
        #rangee du haut (on regarde les y , on fait des soustraction pour monter dans la liste)
        for k in range(1,taille_exp): # boucle qui parcours un intervalle de cases de 1 a la taille de l'explosion de la bombe
            if structure[bombey-k][bombex] == 'm': # si la case est un mur :
                break # on sort de la boucle pour que l'explosion ne traverse pas les murs
            elif structure[bombey-k][bombex] == 'k': # si la case un un bloc cassable :
                niveau.set_case_structure((bombey-k,bombex),remplacer_block()) # on enleve la bloc cassable et on appelle la fonction remplace_block() pour generer une amelioration ou pas
                break # on sort de la boucle pour ne pas traverser le bloc ( on le casse juste et ça stop l'explosion)
            elif structure[bombey-k][bombex] == 'b': # si la case est une bombe
                for bombe in self.liste_bombes : # on cherche la bombe qui a été touché par l'explosion
                    if [bombex,bombey-k] in bombe : # si on a trouvé la bombe
                        self.exploser(bombe[1][0],bombe[1][1],bombe[5],niveau) # on fait exploser la bombe qui a été touché
                break # on sort de la boucle pour ne pas traverser la bombe
            elif structure[bombey-k][bombex] == 'e': # si la case est le centre d'une explosion de bombe on passe ( pour reperer ou on exploser les bombes)
                pass
            else : # sinon s'il n'y a aucun obstacle
                if k == taille_exp-1 : # si a la derniere case de la taille de l'explosion il n'y a pas d'obstacle 
                    niveau.set_case_structure((bombey-k,bombex),'u') # on arrondi le bras de l'explosion (on modifie la case dans la structure du niveau)
                else : # sinon 
                    niveau.set_case_structure((bombey-k,bombex),'v') # on ajoute un morceau de bras de l'explosion
            
        #rangee du bas (on regarde les y, on fait des addition pour descendre dans la liste)
        for k in range(1,taille_exp):
            if structure[bombey+k][bombex] == 'm':
                break
            elif structure[bombey+k][bombex] == 'k':
                niveau.set_case_structure((bombey+k,bombex),remplacer_block())
                break
            elif structure[bombey+k][bombex] == 'b':
                for bombe in self.liste_bombes :
                    if [bombex,bombey+k] in bombe : 
                        self.exploser(bombe[1][0],bombe[1][1],bombe[5],niveau)
                break
            elif structure[bombey+k][bombex] == 'e':
                pass
            else :
                if k == taille_exp-1 :
                    niveau.set_case_structure((bombey+k,bombex),'d')
                else :
                    niveau.set_case_structure((bombey+k,bombex),'v')
                
        #rangee de gauche (on regarde les x, on fait des soustractions pour reculer dans la liste)
        for k in range(1,taille_exp):
            if structure[bombey][bombex-k] == 'm':
                break
            elif structure[bombey][bombex-k] == 'k':
                niveau.set_case_structure((bombey,bombex-k),remplacer_block())
                break
            elif structure[bombey][bombex-k] == 'b':
                for bombe in self.liste_bombes :
                    if [bombex-k,bombey] in bombe : 
                        self.exploser(bombe[1][0],bombe[1][1],bombe[5],niveau)
                break
            elif structure[bombey][bombex-k] == 'e':
                pass
            else :
                if k == taille_exp-1 :
                    niveau.set_case_structure((bombey,bombex-k),'l')
                else :
                    niveau.set_case_structure((bombey,bombex-k),'h')
                
        #rangee de droite (on regarde les x, on fait des additions pour avancer dans la liste)
        for k in range(1,taille_exp):
            if structure[bombey][bombex+k] == 'm':
                break
            elif structure[bombey][bombex+k] == 'k':
                niveau.set_case_structure((bombey,bombex+k),remplacer_block())
                break
            elif structure[bombey][bombex+k] == 'b':
                for bombe in self.liste_bombes :
                    if [bombex+k,bombey] in bombe : 
                        self.exploser(bombe[1][0],bombe[1][1],bombe[5],niveau)
                break
            elif structure[bombey][bombex+k] == 'e':
                pass
            else :
                if k == taille_exp-1 :
                    niveau.set_case_structure((bombey,bombex+k),'r')
                else :
                    niveau.set_case_structure((bombey,bombex+k),'h')


    def nettoyer(self,bombex,bombey,taille_exp,niveau) :
        """fonction qui efface l'explosion des bombes, elle prend en parametres la position de la bombe, la taille de l'explosion et l'objet niveau"""
        structure = niveau.get_structure() #on recupere la structure du niveau
        niveau.set_case_structure((bombey,bombex),'0') # on modifie le niveau pour effacer le centre de l'explosion
        #rangee du haut
        for k in range(1,taille_exp): # boucle qui parcours un intervalle de cases de 1 a la taille de l'explosion de la bombe
            if structure[bombey-k][bombex] == 'v' or structure[bombey-k][bombex] == 'u': # si la case est une explosion verticale ou un bout arrondit d'explosion verticale
                niveau.set_case_structure((bombey-k,bombex),'0') # on modifie le niveau en effaçant les bras de l'explosion
            elif structure[bombey-k][bombex] == 'm' : # si la case est un mur 
                break # on sort de la boucle pour ne ps traverser le mur car les explosions netraversent pas les murs
                
        #rangee du bas
        for k in range(1,taille_exp):
            if structure[bombey+k][bombex] == 'v' or structure[bombey+k][bombex] == 'd':
                niveau.set_case_structure((bombey+k,bombex),'0')
            elif structure[bombey+k][bombex] == 'm':
                break

        #rangee de gauche
        for k in range(1,taille_exp):
            if structure[bombey][bombex-k] == 'h' or structure[bombey][bombex-k] == 'l':
                niveau.set_case_structure((bombey,bombex-k),'0')
            elif structure[bombey][bombex-k] == 'm':
                break

        #rangee de droite
        for k in range(1,taille_exp):
            if structure[bombey][bombex+k] == 'h' or structure[bombey][bombex+k] == 'r':
                niveau.set_case_structure((bombey,bombex+k),'0')
            elif structure[bombey][bombex+k] == 'm':
                break
        
        for liste in self.liste_bombes : # boucle qui parcour la liste des bombes
            if [bombex,bombey] in liste : # on cherche la bombe qu'on a nettoyer
                del self.liste_bombes[self.liste_bombes.index(liste)] #on supprime la bombe

    def get_bombes_joueur(self,nom_joueur) :
        """ fonction qui renvois le nombre de bombes qu'un joueur a posé, elle prend en parametre le nom du joueur"""
        liste_bj =[] # creation d'une liste vide
        for bombe in self.liste_bombes : # boucle qui parcour la liste des bombes
            if bombe[0] == nom_joueur : # si la bombe a comme caracteristique le nom du joueur mis en parametres
                liste_bj.append(bombe) # on ajoute cette bombe dans la liste crée
        return len(liste_bj) # on retourne la longeur de cette liste

    def get_liste_bombes(self) :
        """fonction qui renvois la liste des bombes"""
        return self.liste_bombes # renvois la liste des bombes

    def set_bombes_pause(self,temps_ecouler) :
        """fonction qui permet de mettre a jour le timer des bombes apres le mode pause du jeu, elle prend en parametres le temps ecoulé pendant le mode pause"""
        for bombe in self.liste_bombes : # boucle qui parcour la liste des bombes
            bombe[2] += temps_ecouler # ajout du temps ecoulé pendant le mode pause

    def reset_bombes(self) :
        """fonction qui remet a 0 la liste des bombes, elle permet de recommencer une partie sans bombes initialisés"""
        self.liste_bombes = [] # vide la liste des bombes
