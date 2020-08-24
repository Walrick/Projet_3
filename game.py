#!/usr/bin/python3
# -*- coding: utf8 -*-

import fonction
import pygame

class Main ():
    
    """Main class for manage the game"""
    
    lvl = {}
    item = []
    character = []
    
    size_map = []
    win = False
    loose = False  
    
    def __init__ (self) :
        
        self.graphic = Graphic()
        
        line = 0
        colum = 0        
        
        path = open("Map.txt", "r")
        data = path.readlines()
        for lines in data :                              #  Read the Map.txt and write in the dic "lvl"
            for i in lines :
                if i == " ":
                    self.lvl[(line,colum)] = ["tule_brown", "tule_brown", ""]        # lvl[(x,y)] = ["type of tule", "name tule", Tule instance]
                elif i == "X":
                    self.lvl[(line,colum)] = ["wall_grey_1", "wall_grey_1", ""]   # ancien  lvl[(x,y)] = ["type of tule", "item" (eventually) , Tule instance, "name tule"]
                elif i == "A":
                    self.lvl[(line,colum)] = ["arrival", "tule_deco_brown", ""]
                elif i == "S":
                    self.lvl[(line,colum)] = ["exit", "tule_deco_brown", ""]
                else :
                    self.lvl[(line,colum)] = ["tule_brown", "tule_brown", ""]
                line += 1
            colum  += 1
            self.size_map.append(line-1)
            line = 0
        
        for j in range(0,len(self.size_map)): # y                     Instance the tule
            for i in range(0,self.size_map[j]): # x
                
                self.lvl[(i,j)][2] = fonction.Tule(self.lvl[(i,j)][1],self.graphic.dic[self.lvl[(i,j)][1]])
        
        
        for i in self.graphic.item :                                # instance item
            x, y = fonction.random_placement_item(self.lvl)
            self.item.append(fonction.Item(i[0],i[1],x,y ))
            
        for i in self.graphic.character :                           # instance character
            self.character.append(fonction.Character(i[0],i[1]))   
            
        j = 0
        for i in self.character :                                   # Placement character
            for k, val in self.lvl.items() :
                if val[0] == "arrival" and i.name == "MacGyver" :
                    i.set_placement(k[0],k[1])
                if val[0] == "exit" and i.name == "Gardien" :
                    i.set_placement(k[0],k[1])                
            j += 1
                    
    def launch(self):
        self.loop_master()
        
    def loop_master(self):
        
        running = True
        
        while running:                                     # Event management loop     
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:        # For event type KEYDOWN
                    if event.key == pygame.K_ESCAPE:    
                        running = False
                    elif event.key == pygame.K_LEFT and (self.win == False and self.loose == False) :
                        self.character[0].move("left", fonction.collision(self.lvl, self.character[0], "left"))
                    elif event.key == pygame.K_UP and (self.win == False and self.loose == False) :
                        self.character[0].move("up" ,  fonction.collision(self.lvl, self.character[0], "up"))
                    elif event.key == pygame.K_RIGHT and (self.win == False and self.loose == False) :
                        self.character[0].move("right", fonction.collision(self.lvl, self.character[0], "right"))
                    elif event.key == pygame.K_DOWN and (self.win == False and self.loose == False) :
                        self.character[0].move("down", fonction.collision(self.lvl, self.character[0], "down") )
                        
            Main.pickup_item()
        
            Main.check_win()

            self.graphic.display()                      # Load the screen

            pygame.display.update ()                    # Update the screen 
            
    def pickup_item():
        
        mac_x, mac_y = Main.character[0].get_placement()
        for item in Main.item :
            x, y = item.get_placement()
            if mac_x == x and mac_y == y and item.bag == False:
                item.pickup_item()
                Main.character[0].pickup_item()
        
        
    def check_win():
        
        mac_x, mac_y = Main.character[0].get_placement()
        gar_x, gar_y = Main.character[1].get_placement()
        total_item = Main.character[0].bag
        
        if mac_x-1 == gar_x and mac_y == gar_y :
                if total_item == 3:
                    Main.win = True
                else : Main.loose = True
            
        if mac_x+1 == gar_x and mac_y == gar_y :
                if total_item == 3:
                    Main.win = True 
                else : Main.loose = True
      
        if mac_y+1 == gar_y and mac_x == gar_x : 
                if total_item == 3:
                    Main.win = True
                else : Main.loose = True
                    
        if mac_y-1 == gar_y and mac_x == gar_x : 
                if total_item == 3:
                    Main.win = True      
                else : Main.loose = True     
                
                
    

    
class Graphic :
    
    """Load dic, item and character and manage the screen """
    
    
    dic =  {}
    item = []
    character = []
    
    def __init__ (self):
        
         
        
        self.size = (720, 530)                   # size of screen
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)    # Display the screen(tuple)
        pygame.draw.rect(self.screen,(128,128,128), (0,0,self.size[0],self.size[1]))    
        
        tileset = pygame.image.load("objet_graphique/floor-tiles-20x20.png")          # init the tule
        self.load_tule(0,0,"tule_deco_brown",tileset)                                                   
        self.load_tule(20,0,"tule_brown",tileset)
        self.load_tule(180,0,"wall_grey_1",tileset)
                
        needleset = pygame.image.load("objet_graphique/aiguille.png")        # init the needle
        self.load_item("needle",needleset)
        
        etherset = pygame.image.load("objet_graphique/ether.png")         # init the ether
        self.load_item("ether",etherset)
        
        plastic_tubeset = pygame.image.load("objet_graphique/tube_plastique.png")         # init the plastic_tubeset
        self.load_item("plastic_tube",plastic_tubeset)
        
        MacGyverset = pygame.image.load("objet_graphique/MacGyver.png")         # init MacGyver
        self.load_character("MacGyver", MacGyverset)
        
        Gardienset = pygame.image.load("objet_graphique/Gardien.png")         # init Gardien
        self.load_character("Gardien", Gardienset)     
        
            
    def load_tule(self,x,y,name,data):
        data = data.subsurface((x,y,20,20))                    # select the tule
        data = pygame.transform.scale(data, (30, 30))       # transform the size  
        self.dic[name] = data
        
    def load_item(self,name,data):
        data = pygame.transform.scale(data, (30, 30))       # transform the size
        self.item.append([name,data])
        
    def load_character(self,name,data):
        data = pygame.transform.scale(data, (30, 30))       # transform the size
        self.character.append([name,data])
    
            
    def display (self):
        
        pygame.draw.rect(self.screen,(128,128,128), (0,0,self.size[0],self.size[1]))    # ecrase the screen
        
        for j in range(0,len(Main.size_map)): # y
            for i in range(0,Main.size_map[j]): # x
                a = Main.lvl[(i,j)][2].create()
                self.screen.blit(a,(i*30+10,j*30+10))
                
        for i in Main.item:
            
            a, x, y = i.create()
            
            if i.bag == True and i.name == "needle":    
                self.screen.blit(a,(18*30+10,2*30+10))
        
            elif i.bag == True and i.name == "ether":    
                self.screen.blit(a,(19*30+10,2*30+10))
                
            elif i.bag == True and i.name == "plastic_tube":    
                self.screen.blit(a,(20*30+10,2*30+10))
                
            else :
                self.screen.blit(a,(x*30+10,y*30+10))
                
                
        for i in Main.character:
            
            a, x, y = i.create()
            self.screen.blit(a,(x*30+10,y*30+10))            
            
        if Main.win == True :
            font=pygame.font.Font(None, 24)
            text = font.render("GAGNÉ",1,(255,255,255)) 
            self.screen.blit(text, (300, 300))
            
        if Main.loose == True :
            font=pygame.font.Font(None, 24)
            text = font.render("PERDU",1,(255,255,255)) 
            self.screen.blit(text, (300, 300))          
            
            
