#Eulenis Tarazona - Jeu de la vie 

import tkinter as tk 
from tkinter import *


#Classe chargée d'être l'intelligence du jeu
class LiveController:
    
    #Attributs de classe privés
    __flag = False        #Le jeu continue ou non 
    __refresh_delay = 50  #Vitesse de l'animation 
    
    @classmethod
    @property
    def flag(cls):
        return cls.__flag
    
    @classmethod
    def set_flag(cls, n_flag):
        cls.__flag = n_flag
	 
    @classmethod
    @property
    def refresh_delay(cls):
        return cls.__refresh_delay
    
    @classmethod
    def set_refresh_delay(cls, n_refresh_delay):
        cls.__refresh_delay = n_refresh_delay    
    
 
    def __init__(self, model, view):
        self.__model = model
        self.__view = view
        self.__couleur_cellules = 'black' #Détermine la couleur de la cellule
        self.model.valeur_default()
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, ins_model):
        self.__model = ins_model
    
    @property
    def view(self):
        return self.__view
    
    @view.setter
    def view(self, ins_view):
        self.__view = ins_view
    
    @property
    def couleur_cellules(self):
        return self.__couleur_cellules
    
    @couleur_cellules.setter
    def couleur_cellules(self, n_couleur_cellules):
        self.__couleur_cellules = n_couleur_cellules
    
    #le jeu commence   
    def gui_go(self):
        if LiveController.flag == False:
            LiveController.set_flag(True)
            self.play()
        
    #Le jeu s'arrête
    def gui_stop(self):
        LiveController.set_flag(False)
        
    #Changer la vitesse de l'animation
    def gui_change_vit(self, event):
        LiveController.set_refresh_delay(int(eval(event)))
        print(LiveController.refresh_delay)
        
    #Détermine la couleur de la cellule
    def gui_couleur_cellules(self):
        self.couleur_cellules = 'DeepPink2'

    #Fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
    def click_gauche(self, event):
        x = event.x - event.x % self.model.cellule
        y = event.y - event.y % self.model.cellule
        self.view.can1.create_rectangle(x, y, x + self.model.cellule, y + self.model.cellule, fill=self.couleur_cellules)
        self.model.dico_case[x, y] = 1


    #Fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
    def click_droit(self, event): 
        x = event.x - event.x % self.model.cellule
        y = event.y - event.y % self.model.cellule
        self.view.can1.create_rectangle(x, y, x + self.model.cellule, y + self.model.cellule, fill='white')
        self.model.dico_case[x, y] = 0
    
    
    def canon(self): #Fonction dessinant le célèbre canon à planeur de Bill Gosper
        self.model.dico_case[0*self.model.cellule,5*self.model.cellule]=1
        self.model.dico_case[0*self.model.cellule,6*self.model.cellule]=1
        self.model.dico_case[1*self.model.cellule,5*self.model.cellule]=1
        self.model.dico_case[1*self.model.cellule,6*self.model.cellule]=1
        self.model.dico_case[10*self.model.cellule,5*self.model.cellule]=1
        self.model.dico_case[10*self.model.cellule,6*self.model.cellule]=1
        self.model.dico_case[10*self.model.cellule,7*self.model.cellule]=1
        self.model.dico_case[11*self.model.cellule,4*self.model.cellule]=1
        self.model.dico_case[11*self.model.cellule,8*self.model.cellule]=1
        self.model.dico_case[12*self.model.cellule,3*self.model.cellule]=1
        self.model.dico_case[12*self.model.cellule,9*self.model.cellule]=1
        self.model.dico_case[13*self.model.cellule,3*self.model.cellule]=1
        self.model.dico_case[13*self.model.cellule,9*self.model.cellule]=1
        self.model.dico_case[14*self.model.cellule,6*self.model.cellule]=1
        self.model.dico_case[15*self.model.cellule,4*self.model.cellule]=1
        self.model.dico_case[15*self.model.cellule,8*self.model.cellule]=1
        self.model.dico_case[16*self.model.cellule,5*self.model.cellule]=1
        self.model.dico_case[16*self.model.cellule,6*self.model.cellule]=1
        self.model.dico_case[16*self.model.cellule,7*self.model.cellule]=1
        self.model.dico_case[17*self.model.cellule,6*self.model.cellule]=1
        self.model.dico_case[20*self.model.cellule,3*self.model.cellule]=1
        self.model.dico_case[20*self.model.cellule,4*self.model.cellule]=1
        self.model.dico_case[20*self.model.cellule,5*self.model.cellule]=1
        self.model.dico_case[21*self.model.cellule,3*self.model.cellule]=1
        self.model.dico_case[21*self.model.cellule,4*self.model.cellule]=1
        self.model.dico_case[21*self.model.cellule,5*self.model.cellule]=1
        self.model.dico_case[22*self.model.cellule,2*self.model.cellule]=1
        self.model.dico_case[22*self.model.cellule,6*self.model.cellule]=1
        self.model.dico_case[24*self.model.cellule,1*self.model.cellule]=1
        self.model.dico_case[24*self.model.cellule,2*self.model.cellule]=1
        self.model.dico_case[24*self.model.cellule,6*self.model.cellule]=1
        self.model.dico_case[24*self.model.cellule,7*self.model.cellule]=1
        self.model.dico_case[34*self.model.cellule,3*self.model.cellule]=1
        self.model.dico_case[34*self.model.cellule,4*self.model.cellule]=1
        self.model.dico_case[35*self.model.cellule,3*self.model.cellule]=1
        self.model.dico_case[35*self.model.cellule,4*self.model.cellule]=1    
        self.gui_go()
    
   #Fonction comptant le nombre de cellules vivantes autour de chaque cellule 
    def play(self):
        
        v=0
        while v!= self.model.canvas_width/self.model.cellule:
            w=0
            while w!= self.model.canvas_width/self.model.cellule:
                x=v*self.model.cellule
                y=w*self.model.cellule
                
                # cas spéciaux:
                # les coins
                if x==0 and y==0: #coin en haut à gauche
                    compt_viv=0
                            
                    for i in [x , x+self.model.cellule]:
                        for j in [y , y+self.model.cellule]:
                            
                            if i == x and j == y: 
                                continue
                            if self.model.dico_case[i , j]==1:
                                compt_viv+=1 
                
                    self.model.nb_neighbours[x, y]=compt_viv
                    
                elif x==0 and y==int(self.model.canvas_height-self.model.cellule): #coin en bas à gauche
                    compt_viv=0
                             
                    for i in [x , x+self.model.cellule]:
                        for j in [y-self.model.cellule , y]:
                            
                            if i == x and j == y: 
                                continue
                            if self.model.dico_case[i , j]==1:
                                compt_viv+=1 
                                              
                    self.model.nb_neighbours[x, y]=compt_viv
                                 
                elif x==int(self.model.canvas_width-self.model.cellule) and y==0: #coin en haut à droite
                    compt_viv=0        
                    
                    for i in [x-self.model.cellule , x]:
                        for j in [y, y+self.model.cellule]:
                            
                            if i == x and j == y: 
                                continue
                            if self.model.dico_case[i , j]==1:
                                compt_viv+=1 
                                  
                    self.model.nb_neighbours[x, y]=compt_viv
                          
                elif x==int(self.model.canvas_width-self.model.cellule) and y==int(self.model.canvas_height-self.model.cellule): #coin en bas à droite
                    compt_viv=0
                      
                    for i in [x-self.model.cellule , x]:
                        for j in [y-self.model.cellule, y]:
                            
                            if i == x and j == y: 
                                continue
                            if self.model.dico_case[i , j]==1:
                                compt_viv+=1 
                            
                    self.model.nb_neighbours[x, y]=compt_viv
                    
                # cas spéciaux:
                # les bords du tableau (sans les coins)    
                elif x==0 and 0<y<int(self.model.canvas_height-self.model.cellule): # bord de gauche
                    compt_viv=0
                    
                    for i in [x, x+self.model.cellule]:
                        for j in [y-self.model.cellule,y, y+self.model.cellule]:
                            if i == x and j == y: 
                                continue
                            if self.model.dico_case[i , j]==1:
                                compt_viv+=1 
                        
                    self.model.nb_neighbours[x, y]=compt_viv
                    
                elif x==int(self.model.canvas_width-self.model.cellule) and 0<y<int(self.model.canvas_height-self.model.cellule): # bord de droite
                    compt_viv=0
                    
                    for i in [x-self.model.cellule, x]:
                        for j in [y-self.model.cellule,y, y+self.model.cellule]:
                            if i == x and j == y: 
                                continue
                            if self.model.dico_case[i , j]==1:
                                compt_viv+=1 
                        
                    self.model.nb_neighbours[x, y]=compt_viv
                    
                elif 0<x<int(self.model.canvas_width-self.model.cellule) and y==0: # bord du haut
                    compt_viv=0
                    
                    for i in [x-self.model.cellule, x, x+self.model.cellule ]:
                        for j in [y, y+self.model.cellule]:
                            if i == x and j == y: 
                                continue
                            if self.model.dico_case[i , j]==1:
                                compt_viv+=1 
                        
                    self.model.nb_neighbours[x, y]=compt_viv
                    
                elif 0<x<int(self.model.canvas_width-self.model.cellule) and y==int(self.model.canvas_height-self.model.cellule): # bord du bas
                    compt_viv=0
                   
                    for i in [x-self.model.cellule, x, x+self.model.cellule ]:
                        for j in [y-self.model.cellule, y]:
                            if i == x and j == y: 
                                continue
                            if self.model.dico_case[i , j]==1:
                                compt_viv+=1 
                        
                    self.model.nb_neighbours[x, y]=compt_viv

                #cas généraux
                #les cellules qui ne sont pas dans les bords du tableau
                else:
                    compt_viv=0
                        
                    for i in [x-self.model.cellule , x, x+self.model.cellule, ]:
                            for j in [y-self.model.cellule, y, y+self.model.cellule]:
                                
                                if i == x and j == y: 
                                    continue
                                if self.model.dico_case[i , j]==1:
                                    compt_viv+=1 
                        
                    self.model.nb_neighbours[x, y]=compt_viv
                    
                w+=1
            v+=1
        self.redessiner()
        if LiveController.flag == True: 
            if self.model.grille_stable(6):  
                LiveController.set_flag(False)
                print("La grille est devenu stable. Le jeu est arrêté. Remplir de nouvelles cases et cliquer sur Go pour continuer ")              
            else:   
                self.view.fen1.after(LiveController.refresh_delay, self.play)
            
        

    #Fonction redessinant le tableau à partir de dico_etat
    def redessiner(self): 
        
        self.model.etat_precedent = dict(self.model.dico_case)
        self.model.compteur += 1
        
        self.view.can1.delete(ALL)
        self.view.ins_Canvas.damier(self.view.can1)
        
        t=0
        while t!= self.model.canvas_width/self.model.cellule:
            u=0
            while u!= self.model.canvas_height/self.model.cellule:
                x=t*self.model.cellule
                y=u*self.model.cellule
                if self.model.nb_neighbours[x,y]==3:
                    self.model.dico_case[x,y]=1
                    self.view.can1.create_rectangle(x, y, x+self.model.cellule, y+self.model.cellule, fill=self.couleur_cellules)
                elif self.model.nb_neighbours[x,y]==2:
                    if self.model.dico_case[x,y]==1:
                        self.view.can1.create_rectangle(x, y, x+self.model.cellule, y+self.model.cellule, fill=self.couleur_cellules)
                    else:
                        self.view.can1.create_rectangle(x, y, x+self.model.cellule, y+self.model.cellule, fill='white')
                elif self.model.nb_neighbours[x,y]<2 or self.model.nb_neighbours[x,y]>3:
                    self.model.dico_case[x,y]=0
                    self.view.can1.create_rectangle(x, y, x+self.model.cellule, y+self.model.cellule, fill='white')
                u+=1
            t+=1
        
        

class LiveView:
    
    
    def __init__(self, f):
        
        self.__ins_Canvas = LiveCanvas()
    
        self.__bar = LiveCommandBar.factory(f)
    
        self.__fen1 = f 

        #Le canvas est créé
        self.__can1 = Canvas(self.fen1 , width = self.ins_Canvas.model_width, height = self.ins_Canvas.model_height, bg ='white')  
        self.can1.grid(row=0, column=0, rowspan=8, columnspan=8)

        #Connexion de la souris avec une autre méthode
        self.can1.bind("<Button-1>", self.envoyer_click_gauche)
        self.can1.bind("<Button-3>", self.envoyer_click_droit)

        #Appel de la grille
        self.ins_Canvas.damier(self.can1)
     
     
    @property
    def can1 (self):
        return self.__can1
    
    @can1.setter
    def can1 (self, c):
        self.__can1 = c 
     
    @property
    def fen1 (self):
        return self.__fen1
    
    @fen1.setter
    def fen1 (self, f):
        self.__fen1 = f
     
    @property
    def bar (self):
        return self.__bar
    
    @bar.setter
    def bar (self, b):
        self.__bar = b
            
    @property
    def ins_Canvas (self):
        return self.__ins_Canvas
    
    @ins_Canvas.setter
    def ins_Canvas (self, canvas):
        self.__ins_Canvas = canvas
        
    #click gauche
    def envoyer_click_gauche(self, event):
          
        if self.controller:
            self.controller.click_gauche(event)
    
    #click droite
    def envoyer_click_droit(self, event):
    
        if self.controller:  
            self.controller.click_droit(event)  
            
     #Connexion avec le Controller   
    def set_controller(self, controller):
       
        self.controller = controller
        self.bar.set_controller(controller)
    
   
   
   
class LiveCommandBar: 
    
    def __init__(self, fen1):
        self.__fen1 = fen1
        self.__controller = None
        self.__v_h_r_button = StringVar(value="Horizontal")
            
        self.create_widgets()
        self.horizontal()
   
    @property
    def  v_h_r_button (self):
        return self.__v_h_r_button
    
    @v_h_r_button.setter
    def v_h_r_button (self, v_h):
        self.__v_h_r_button = v_h
   
    @property
    def fen1 (self):
        return self.__fen1
    
    @fen1.setter
    def fen1 (self, f):
        self.__fen1 = f
 
    @property
    def controller (self):
        return self.__controller
    
    @controller.setter
    def controller (self, contr):
        self.__controller = contr
        
    #Connexion avec le Controller   
    def set_controller(self, controller):
       
        self.controller = controller

    #Toutes les méthodes suivantes sont des méthodes qui font le lien entre les boutons et leurs méthodes dans la classe du Controller.
    def envoyer_gui_go(self):
    
        if self.controller:
            self.controller.gui_go()
            
    def envoyer_gui_stop(self):
    
        if self.controller:
            self.controller.gui_stop()
            
    def envoyer_gui_canon(self):
    
        if self.controller:
            self.controller.canon()
                  
        
    def envoyer_gui_change_vit(self, event):
    
        if self.controller:
            self.controller.gui_change_vit(event)
    
    
    def envoyer_couleur(self):

        if self.controller:
            self.controller.gui_couleur_cellules()
    
    
    #Méthode qui crée les boutons
    def create_widgets(self):
    
        self.b1 = Button(self.fen1, text='Go!', bg="LightPink1", command=self.envoyer_gui_go) 
        
        self.b2 = Button(self.fen1, text='Stop', bg="LightPink1", command=self.envoyer_gui_stop)
      
        self.b3 = Button(self.fen1, text ='Canon', bg="LightPink1", command =self.envoyer_gui_canon)
        
        self.b4 = Button(self.fen1, text ='Cel PINK', bg="VioletRed1", command = self.envoyer_couleur)
        
        self.b5 = Radiobutton(self.fen1, text ='Vertical', variable= self.v_h_r_button, value="Vertical", command = self.gui_v_h)
       
        self.b6 = Radiobutton(self.fen1, text ='Horizontal', variable= self.v_h_r_button, value="Horizontal", command = self.gui_v_h)
        
        self.chai = Label(self.fen1)
        self.chai.configure(text="Délai (ms) :")
      
        self.ent = Entry(self.fen1)
        self.ent.bind("<Return>", lambda event: self.envoyer_gui_change_vit(self.ent.get()))
       
    #Méthode qui positionne les boutons horizontalement   
    def horizontal(self):
        self.b1.grid(row=9, column=0, pady=4, padx=4, sticky="ew")
        self.b2.grid(row=9, column=1, pady=4,  padx=4, sticky="ew")
        self.b3.grid(row=9, column=2, pady=4,  padx=4, sticky="ew")
        self.b4.grid(row=9, column=3, pady=4,  padx=4, sticky="ew")
        self.b5.grid(row=10, column=0, pady=4,  padx=4, sticky="ew")
        self.b6.grid(row=10, column=1, pady=4,  padx=4, sticky="ew")
        self.chai.grid(row=9, column=4, pady=4, sticky="ew")
        self.ent.grid(row=9, column=5, columnspan=6, pady=5, padx=4, sticky="ew")    
        
        
    #Supprime les boutons, reçoit la valeur "horizontale" ou "verticale" et envoie cette donnée à Factory
    def  gui_v_h(self):
    
            for button in [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.ent, self.chai]:
                button.grid_remove()
            
            h_v = self.v_h_r_button.get()

            bar = LiveCommandBar.factory(self.fen1 , h_v)
            bar.set_controller(self.controller)   
    
        
    #Design pattern: Factory 
    @classmethod        
    def  factory(cls, fen1, widgets_v_h="Horizontal"):  
        
        if widgets_v_h == "Horizontal":
            return Horizontal(fen1)
        else:
            return Vertical(fen1)

            
class Horizontal(LiveCommandBar):
    def __init__(self, fen1):
        super().__init__(fen1)
        
    
        self.b1.grid(row=9, column=0, pady=4, padx=4, sticky="ew")
        self.b2.grid(row=9, column=1, pady=4,  padx=4, sticky="ew")
        self.b3.grid(row=9, column=2, pady=4,  padx=4, sticky="ew")
        self.b4.grid(row=9, column=3, pady=4,  padx=4, sticky="ew")
        self.b5.grid(row=10, column=0, pady=4,  padx=4, sticky="ew")
        self.b6.grid(row=10, column=1, pady=4,  padx=4, sticky="ew")
        self.chai.grid(row=9, column=4, pady=4, sticky="ew")
        self.ent.grid(row=9, column=5, columnspan=6, pady=5, padx=4, sticky="ew")
        
    
class Vertical(LiveCommandBar):
    def __init__(self, fen1):
        super().__init__(fen1)  
        
        
        self.b1.grid(row=0, column=9, pady=4, padx=4, sticky="ew")
        self.b2.grid(row=1, column=9, pady=4,  padx=4, sticky="ew")
        self.b3.grid(row=2, column=9, pady=4,  padx=4, sticky="ew")
        self.b4.grid(row=3, column=9, pady=4,  padx=4, sticky="ew")
        self.b5.grid(row=4, column=9, pady=4,  padx=4, sticky="ew")
        self.b6.grid(row=4, column=10, pady=4,  padx=4, sticky="ew")
        self.chai.grid(row=6, column=9, pady=4, sticky="ew")
        self.ent.grid(row=6, column=10, pady=4, padx=4, sticky="ew")           
      
        
        
#Classe chargée de l'affichage de la matrice
#Affichage de la matrice avec le design pattern "iterator"
class LiveCanvas:
    def __init__(self):
        self.__ins_model = LiveModel()
        self.model_height = self.ins_model.canvas_height
        self.model_width = self.ins_model.canvas_width
        self.__c_x_y = 0
    
    @property
    def ins_model(self):
        return self.__ins_model
    
    @ins_model.setter
    def ins_model(self, model):
        self.__ins_model = model
        
    @property
    def c_x_y(self):
        return self.__c_x_y
    
    @c_x_y.setter
    def c_x_y(self, x_y):
        self.__c_x_y = x_y
           
    
    def __iter__(self):
        return self
    
    def __next__(self, canvas1):
        if self.c_x_y >= self.ins_model.canvas_width:
            raise StopIteration
        
        canvas1.create_line(self.c_x_y,0,self.c_x_y,self.model_height,width=1,fill='black')
        canvas1.create_line(0,self.c_x_y,self.model_width,self.c_x_y,width=1,fill='black')

        self.c_x_y += self.ins_model.cellule     
    
    def damier (self, canvas1):
        while True:
            try: 
                self.__next__(canvas1)
            except StopIteration:
                break


class LiveModel:
    def __init__(self):
        
        self.canvas_height = 500   #Hauteur de la grille
        self.canvas_width = 500    #Largeur de la grille
        self.dico_case = {}        #Coordonnées de chaques cellules
        self.cellule = LiveCell().cellule   #Taille des cellules
        self.nb_neighbours = LiveCell().dico_etat #Cellules vivantes autour de chaque cellule
        self.compteur = 0   #Compteur 
        self.etat_precedent = LiveCell().etat_precedent  #Enregistre l’état qui précède de "dico_case"
        
     
    #Assigne une valeur 0(morte) a chaque coordonnées(cellules)   
    def valeur_default(self):
        i=0
        while i!= self.canvas_width/self.cellule: 
            j=0
            while j!= self.canvas_height/self.cellule:
                x=i*self.cellule
                y=j*self.cellule
                self.dico_case[x,y]=0
                j+=1
            i+=1
    
    
    #La méthode vérifie si le tableau est resté inchangé. 
    #Par suite d'autres événements arrêter le jeu quand la grille est devenu stable      
    def grille_stable(self, num):                                        
        etat_actuel = dict(self.dico_case)
        historique_etat = [dict(self.etat_precedent)]  
        for _ in range(num - 1):
            historique_etat.append(historique_etat[-1])
            resultat = all(etat_actuel == pre_etat for pre_etat in historique_etat)
        return resultat
  
        
class LiveCell:  		
				
    def __init__(self):
        self.cellule = 10 
        self.dico_etat = {} 
        self.etat_precedent = {}        
        
  
        
#La classe regroupant les classes 
class Jeu_de_la_vie_run(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Jeu de la vie - Eulenis Tarazona')

        model = LiveModel()

        view = LiveView(self)
        
        controller = LiveController(model, view)

        view.set_controller(controller)


if __name__ == '__main__':
    run = Jeu_de_la_vie_run()
    run.mainloop()           