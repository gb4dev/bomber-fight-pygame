from fonctions_et_constantes import *
class Niveau:
    """classe qui contient une fontion qui genere la carte
et une fonction qui l'affiche"""
    def __init__(self):
        self.structure=[]
        self.image_mur = load_png("mur1.png")
        self.image_kure = load_png("kure.png")
        self.image_fond = load_png("herbe.png")
        self.image_bombe = load_png("bombe.png")
        self.image_bombe.set_colorkey((255,255,255))
        self.image_explosion = load_png("explosion.png")
        self.image_vtrait = load_png("vtrait.png")
        self.image_htrait = load_png("htrait.png")
        self.image_taille_plus = load_png("taille_plus.png")
        self.image_taille_plus.set_colorkey((255,255,255))
        self.image_bombe_plus = load_png("bombe_plus.png")
        self.image_bombe_plus.set_colorkey((255,255,255))
        self.image_bgauche = load_png("bout_explosion_gauche.png")
        self.image_bdroite = load_png("bout_explosion_droite.png")
        self.image_bhaut = load_png("bout_explosion_haut.png")
        self.image_bbas = load_png("bout_explosion_bas.png")
        self.image_vitesse_plus = load_png("vitesse_plus.png")
        self.liste_murs = []
        self.liste_bombes = []

    def generer_niveau(self,fichier):
        """Methode permettant de generer le niveau en fonction du fichier.
		On cree une liste generale, contenant une liste par ligne a afficher"""	
            #On ouvre le fichier
        with open(fichier, "r") as struct :
                structure_niveau = []
                #On parcourt les lignes du fichier
                for ligne in struct:
                        ligne_niveau = []
                        #On parcourt les sprites (lettres) contenus dans le fichier
                        for sprite in ligne:
                                #On ignore les "\n" de fin de ligne
                                if sprite != '\n':
                                        #On ajoute le sprite a la liste de la ligne
                                        ligne_niveau.append(sprite)
                        #On ajoute la ligne a la liste du niveau
                        structure_niveau.append(ligne_niveau)
                #On sauvegarde cette structure
                self.structure = structure_niveau

    def afficher_carte(self,fenetre):
            """Methode permettant d'afficher le niveau en fonction
            de la liste de structure renvoyee par generer()"""
            #On parcourt la liste du niveau
            num_ligne = 0
            fenetre.blit(self.image_fond,(0,0))
            for ligne in self.structure:
                    #On parcourt les listes de lignes
                    num_case = 0
                    for sprite in ligne:
                            #On calcule la position reelle en pixels
                            x = num_case * taille_sprite
                            y = num_ligne * taille_sprite
                            if sprite == 'm':		#m = Mur
                                fenetre.blit(self.image_mur, (x,y))
                            elif sprite == 'k':         #k = mur cassable
                                fenetre.blit(self.image_kure,(x,y))
                            elif sprite == 'b':         #b = bombe
                                fenetre.blit(self.image_bombe,(x,y))
                            elif sprite == 'e' :        #e = centre explosion
                                fenetre.blit(self.image_explosion,(x,y))
                            elif sprite == 'v' :        #v = trait d'explosion vertical
                                fenetre.blit(self.image_vtrait,(x,y))
                            elif sprite == 'h' :        #h = trait d'explosion horizontal
                                fenetre.blit(self.image_htrait,(x,y))
                            elif sprite == 't' :        #t = upgrade taille explosion
                                fenetre.blit(self.image_taille_plus,(x,y))
                            elif sprite == 'n' :        #n = upgrade nombre bombes
                                fenetre.blit(self.image_bombe_plus,(x,y))
                            elif sprite == 'u' :
                                fenetre.blit(self.image_bhaut,(x,y))
                            elif sprite == 'd' :
                                fenetre.blit(self.image_bbas,(x,y))
                            elif sprite == 'l' :
                                fenetre.blit(self.image_bgauche,(x,y))
                            elif sprite == 'r' :
                                fenetre.blit(self.image_bdroite,(x,y))
                            elif sprite == 's' :
                                fenetre.blit(self.image_vitesse_plus,(x,y))
                            num_case += 1
                    num_ligne += 1


    def set_case_structure(self,case,obj):
        self.structure[case[0]][case[1]] = obj

    def get_structure(self):
        return self.structure

    def actualiser(self) :
        self.liste_murs = []
        self.liste_bombes = []
        x,y = 0,0
        while y < len(self.structure) :
            while x < len(self.structure[y]) :
                if self.structure[y][x] == 'k' or self.structure[y][x] == 'm' :
                    self.liste_murs.append(pygame.Rect(x*taille_sprite,y*taille_sprite,taille_sprite,taille_sprite))
                elif self.structure[y][x] == 'b' :
                    self.liste_bombes.append(pygame.Rect(x*taille_sprite,y*taille_sprite,taille_sprite,taille_sprite))
                x+=1
            y+=1
            x=0

    def get_obstacles(self) :
        return self.liste_murs

    def get_bombes(self) :
        return self.liste_bombes
