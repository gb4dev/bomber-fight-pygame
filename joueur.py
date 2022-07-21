from fonctions_et_constantes import *
import time
class Joueur() :

    def __init__(self,case,nom_joueur) :
        self.casex = case[0]
        self.casey = case[1]
        self.nbombes = 1
        self.image_haut = load_png("Bombermandos.png")
        self.image_bas = load_png("Bombermanface.png")
        self.image_gauche = load_png("Bombermangauche2.png")
        self.image_droite = load_png("Bombermandroite2.png")
        self.liste_droite = [load_png("Bombermandroite.png"),load_png("Bombermandroite1.png"),load_png("Bombermandroite2.png")]
        self.liste_gauche = [load_png("Bombermangauche.png"),load_png("Bombermangauche1.png"),load_png("Bombermangauche2.png")]
        self.liste_haut = [load_png("Bombermandos.png"),load_png("Bombermandos1.png"),load_png("Bombermandos2.png")]
        self.liste_bas = [load_png("Bombermanface.png"),load_png("Bombermanface1.png"),load_png("Bombermanface2.png")]
        self.direction = self.image_bas
        self.vivant = True
        self.nom_joueur = nom_joueur
        self.taille_exp = 3
        self.font = pygame.font.Font(None, 20)
        self.surf_nom = self.font.render(self.nom_joueur, 0, (255,0,0))
        self.rect_nom = self.surf_nom.get_rect()
        self.deplacer_bombes = 0
        self.rect_image = self.image_bas.get_rect(x=self.casex*taille_sprite,y=self.casey*taille_sprite)
        self.vitesse = 3
        self.marge = 10
        self.rect_nom.centerx = self.rect_image.left+self.image_bas.get_width()/2
        self.rect_nom.centery = self.rect_image.top-self.image_bas.get_height()/2
        self.compteur_move = 0
        self.temps_animation = time.time()

    def actualiser(self,direction,niveau,bombes) :
        self.bouger(direction,niveau,bombes)
        self.rect_nom.centerx = self.rect_image.left+self.image_bas.get_width()/2
        self.rect_nom.centery = self.rect_image.top-self.image_bas.get_height()/2
        self.touche(niveau)
        

    def afficher(self,fenetre) :
        fenetre.blit(self.direction,self.rect_image)
        fenetre.blit(self.surf_nom,self.rect_nom)

    def bouger(self,direction,niveau,bombes):
        liste_murs = niveau.get_obstacles()
        liste_bombes = niveau.get_bombes()
        structure = niveau.get_structure()
        rect = self.rect_image.copy()
        
        
        if direction == 'droite' :
            if time.time()-self.temps_animation >= 0.1 :
                self.temps_animation = time.time()
                self.compteur_move += 1
                if self.compteur_move == 3 :
                    self.compteur_move = 0
            self.direction = self.liste_droite[self.compteur_move]
            
            rect.left += self.vitesse
            if rect.left > (nombre_sprite_ligne-2)*taille_sprite :
                rect.left = (nombre_sprite_ligne-2)*taille_sprite
            if rect.collidelist(liste_murs) == -1 and rect.collidelist(liste_bombes) == -1:
                self.rect_image = rect
            elif rect.collidelist(liste_bombes) != -1 and rect.collidelist(liste_murs) == -1 :
                """if rect.collidelist(liste_bombes) == self.rect_image.collidelist(liste_bombes) :
                    self.rect_image = rect"""
                if structure[rect.top/taille_sprite][rect.left/taille_sprite] == 'b' and structure[self.rect_image.top/taille_sprite][self.rect_image.left/taille_sprite] == 'b' :
                    self.rect_image = rect
                elif structure[(rect.bottom-1)/taille_sprite][(rect.right-1)/taille_sprite] == 'b' and structure[(self.rect_image.bottom-1)/taille_sprite][(self.rect_image.right-1)/taille_sprite] == 'b':
                    self.rect_image = rect
            else :
                if rect.bottom-self.marge < liste_murs[rect.collidelist(liste_murs)].top :
                    rect.bottom = liste_murs[rect.collidelist(liste_murs)].top
                    self.rect_image = rect
                elif rect.top + self.marge > liste_murs[rect.collidelist(liste_murs)].bottom :
                    rect.top = liste_murs[rect.collidelist(liste_murs)].bottom
                    self.rect_image = rect
                else :
                    rect.right = liste_murs[rect.collidelist(liste_murs)].left
                    self.rect_image = rect
                
                

        elif direction == 'gauche':
            if time.time()-self.temps_animation >= 0.1 :
                self.temps_animation = time.time()
                self.compteur_move += 1
                if self.compteur_move == 3 :
                    self.compteur_move = 0
            self.direction = self.liste_gauche[self.compteur_move]
            rect.left -= self.vitesse
            if rect.left < taille_sprite :
                rect.left = taille_sprite
            if rect.collidelist(liste_murs) == -1 and rect.collidelist(liste_bombes) == -1 :
                self.rect_image = rect
            elif rect.collidelist(liste_bombes) != -1 and rect.collidelist(liste_murs) == -1:
                """if rect.collidelist(liste_bombes) == self.rect_image.collidelist(liste_bombes) :
                    self.rect_image = rect"""
                if structure[(rect.top+1)/taille_sprite][(rect.left+1)/taille_sprite] == 'b' and structure[(self.rect_image.top+1)/taille_sprite][(self.rect_image.left+1)/taille_sprite] == 'b' :
                    self.rect_image = rect
                elif structure[(rect.bottom-1)/taille_sprite][(rect.right-1)/taille_sprite] == 'b' and structure[(self.rect_image.bottom-1)/taille_sprite][(self.rect_image.right-1)/taille_sprite] == 'b':
                    self.rect_image = rect
            else :
                if rect.bottom-self.marge < liste_murs[rect.collidelist(liste_murs)].top :
                    rect.bottom = liste_murs[rect.collidelist(liste_murs)].top
                    self.rect_image = rect
                elif rect.top + self.marge > liste_murs[rect.collidelist(liste_murs)].bottom :
                    rect.top = liste_murs[rect.collidelist(liste_murs)].bottom
                    self.rect_image = rect
                else :
                    rect.left = liste_murs[rect.collidelist(liste_murs)].right
                    self.rect_image = rect


        elif direction == 'haut':
            if time.time()-self.temps_animation >= 0.1 :
                self.temps_animation = time.time()
                self.compteur_move += 1
                if self.compteur_move == 3 :
                    self.compteur_move = 0
            self.direction = self.liste_haut[self.compteur_move]
            rect.top -= self.vitesse
            if rect.top < taille_sprite :
                rect.top = taille_sprite
            if rect.collidelist(liste_murs) == -1 and rect.collidelist(liste_bombes) == -1:
                self.rect_image = rect
            elif rect.collidelist(liste_bombes) != -1 and rect.collidelist(liste_murs) == -1:
                """if rect.collidelist(liste_bombes) == self.rect_image.collidelist(liste_bombes) :
                    self.rect_image = rect"""
                if structure[(rect.top+1)/taille_sprite][(rect.left+1)/taille_sprite] == 'b' and structure[(self.rect_image.top+1)/taille_sprite][(self.rect_image.left+1)/taille_sprite] == 'b' :
                    self.rect_image = rect
                elif structure[(rect.bottom-1)/taille_sprite][(rect.right-1)/taille_sprite] == 'b' and structure[(self.rect_image.bottom-1)/taille_sprite][(self.rect_image.right-1)/taille_sprite] == 'b':
                    self.rect_image = rect
            else :
                if rect.left+self.marge > liste_murs[rect.collidelist(liste_murs)].right :
                    rect.left = liste_murs[rect.collidelist(liste_murs)].right
                    self.rect_image = rect
                elif rect.right-self.marge < liste_murs[rect.collidelist(liste_murs)].left :
                    rect.right = liste_murs[rect.collidelist(liste_murs)].left
                    self.rect_image = rect
                else :
                    rect.top = liste_murs[rect.collidelist(liste_murs)].bottom
                    self.rect_image = rect
                    

        elif direction == 'bas':
            if time.time()-self.temps_animation >= 0.1 :
                self.temps_animation = time.time()
                self.compteur_move += 1
                if self.compteur_move == 3 :
                    self.compteur_move = 0
            self.direction = self.liste_bas[self.compteur_move]
            rect.top += self.vitesse
            if rect.top > (nombre_sprite_colone-2)*taille_sprite :
                rect.top = (nombre_sprite_colone-2)*taille_sprite
            if rect.collidelist(liste_murs) == -1 and rect.collidelist(liste_bombes) == -1:
                self.rect_image = rect
            elif rect.collidelist(liste_bombes) != -1 and rect.collidelist(liste_murs) == -1:
                """if rect.collidelist(liste_bombes) == self.rect_image.collidelist(liste_bombes) :
                    self.rect_image = rect"""
                if structure[(rect.top+1)/taille_sprite][(rect.left+1)/taille_sprite] == 'b' and structure[(self.rect_image.top+1)/taille_sprite][(self.rect_image.left+1)/taille_sprite] == 'b' :
                    self.rect_image = rect
                elif structure[(rect.bottom-1)/taille_sprite][(rect.right-1)/taille_sprite] == 'b' and structure[(self.rect_image.bottom-1)/taille_sprite][(self.rect_image.right-1)/taille_sprite] == 'b':
                    self.rect_image = rect
            else :
                if rect.left+self.marge > liste_murs[rect.collidelist(liste_murs)].right :
                    rect.left = liste_murs[rect.collidelist(liste_murs)].right
                    self.rect_image = rect
                elif rect.right-self.marge < liste_murs[rect.collidelist(liste_murs)].left :
                    rect.right = liste_murs[rect.collidelist(liste_murs)].left
                    self.rect_image = rect
                else :
                    rect.bottom = liste_murs[rect.collidelist(liste_murs)].top
                    self.rect_image = rect
                    
        else :
            if self.direction in self.liste_droite :
                self.direction = self.image_droite
            elif self.direction in self.liste_gauche :
                self.direction = self.image_gauche
            elif self.direction in self.liste_haut :
                self.direction = self.image_haut
            elif self.direction in self.liste_bas :
                self.direction = self.image_bas


        self.casex = (self.rect_image.left+taille_sprite/2)/taille_sprite
        self.casey = (self.rect_image.top+taille_sprite/2)/taille_sprite

            
                    

    def poser_bombe(self,niveau,bombes) :
        if bombes.get_bombes_joueur(self.nom_joueur) < self.nbombes :
            bombes.ajouter_bombe(self.nom_joueur,[self.casex,self.casey],niveau,self.taille_exp)

    def touche(self,niveau) :
        structure = niveau.get_structure()
        casex_tl = self.rect_image.left/taille_sprite
        casey_tl = self.rect_image.top/taille_sprite
        casex_br = (self.rect_image.right-1)/taille_sprite
        casey_br = (self.rect_image.bottom-1)/taille_sprite
        liste_mort = ['h','v','e','u','d','l','r']
        
        if structure[casey_tl][casex_tl] in liste_mort or structure[casey_br][casex_br] in liste_mort:
            self.vivant = False
        elif structure[casey_tl][casex_tl] == 't' :
            self.taille_exp +=1
            niveau.set_case_structure((casey_tl,casex_tl),'0')
        elif structure[casey_br][casex_br] == 't' :
            self.taille_exp +=1
            niveau.set_case_structure((casey_br,casex_br),'0')
        elif structure[casey_tl][casex_tl] == 'n' :
            self.nbombes +=1
            niveau.set_case_structure((casey_tl,casex_tl),'0')
        elif structure[casey_br][casex_br] == 'n' :
            self.nbombes +=1
            niveau.set_case_structure((casey_br,casex_br),'0')
        elif structure[casey_tl][casex_tl] == 's' :
            if self.vitesse < 7 :
                self.vitesse += 1
            niveau.set_case_structure((casey_tl,casex_tl),'0')
        elif structure[casey_br][casex_br] == 's' :
            if self.vitesse < 7 :
                self.vitesse += 1
            niveau.set_case_structure((casey_br,casex_br),'0')

    def get_nom_joueur(self) :
        return self.nom_joueur
        
    def get_vivant(self) :
        return self.vivant

        
