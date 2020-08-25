#!/usr/bin/python3
# -*- coding: utf8 -*-

import fonction
import pygame

from tule import *
from item import *
from character import *

class Main ():
    
    """Main class for manage the game"""
    
    def __init__ (self) :
        
        self.graphic = Graphic()                
        
        self.lvl = {}
        self.item = []
        self.character = []        
        
        self.size_map = []
        self.win = False
        self.loose = False   
        
        line = 0
        colum = 0        
        
        path = open("Map.txt", "r")
        data = path.readlines()
        for lines in data :                              #  Read the Map.txt and write in the dic "lvl"
            for i in lines :
                if i == " ":
                    self.lvl[(line,colum)] = ["tule_brown", "tule_brown", ""]        # lvl[(x,y)] = ["type of tule", "name tule", Tule instance]
                elif i == "X":
                    self.lvl[(line,colum)] = ["wall_grey_1", "wall_grey_1", ""]  
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
                
                if self.lvl[(i,j)][1] == "wall_grey_1":
                    self.lvl[(i,j)][2] = Tule(self.lvl[(i,j)][1],self.graphic.dic_tule[self.lvl[(i,j)][1]], True, self.lvl[(i,j)][0])
                else : 
                    self.lvl[(i,j)][2] = Tule(self.lvl[(i,j)][1],self.graphic.dic_tule[self.lvl[(i,j)][1]], False, self.lvl[(i,j)][0])
        
        for i in self.graphic.item :                                # instance item
            x, y = fonction.random_placement_item(self.lvl)
            self.item.append(Item(i[0],i[1],x,y ))
            
        for i in self.graphic.character :                           # instance character
            self.character.append(Character(i[0],i[1]))   
            
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
                    if event.key == pygame.K_ESCAPE:    # Exit
                        running = False
                    elif event.key == pygame.K_LEFT and (self.win == False and self.loose == False) :
                        self.character[0].move("left", fonction.collision_test(self.lvl, self.character[0], "left"))
                    elif event.key == pygame.K_UP and (self.win == False and self.loose == False) :
                        self.character[0].move("up" ,  fonction.collision_test(self.lvl, self.character[0], "up"))
                    elif event.key == pygame.K_RIGHT and (self.win == False and self.loose == False) :
                        self.character[0].move("right", fonction.collision_test(self.lvl, self.character[0], "right"))
                    elif event.key == pygame.K_DOWN and (self.win == False and self.loose == False) :
                        self.character[0].move("down", fonction.collision_test(self.lvl, self.character[0], "down") )
                        
            self.check_pickup_item()
        
            self.check_win()

            self.graphic.display(self.size_map, self.lvl, self.item, self.character, self.win, self.loose)                      # Load the screen

            pygame.display.update ()                    # Update the screen 
            
    def check_pickup_item(self):
        
        mac_x, mac_y = self.character[0].get_placement()
        for item in self.item :
            x, y = item.get_placement()
            if mac_x == x and mac_y == y and item.bag == False:
                item.pickup_item()
                self.character[0].pickup_item()
        
        
    def check_win(self):
        
        mac_x, mac_y = self.character[0].get_placement()
        gar_x, gar_y = self.character[1].get_placement()
        total_item = self.character[0].bag
        
        if mac_x-1 == gar_x and mac_y == gar_y :
                if total_item == 3:
                    self.win = True
                else : self.loose = True
            
        if mac_x+1 == gar_x and mac_y == gar_y :
                if total_item == 3:
                    self.win = True 
                else : self.loose = True
      
        if mac_y+1 == gar_y and mac_x == gar_x : 
                if total_item == 3:
                    self.win = True
                else : self.loose = True
                    
        if mac_y-1 == gar_y and mac_x == gar_x : 
                if total_item == 3:
                    self.win = True      
                else : self.loose = True     
                
                
    
class Graphic :
    
    """Load dic_tule, item and character and manage the screen """
    
    
    dic_tule =  {}
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
        self.dic_tule[name] = data
        
    def load_item(self,name,data):
        data = pygame.transform.scale(data, (30, 30))       # transform the size
        self.item.append([name,data])
        
    def load_character(self,name,data):
        data = pygame.transform.scale(data, (30, 30))       # transform the size
        self.character.append([name,data])
    
            
    def display (self,size_map,lvl,item,character, win, loose):
        
        pygame.draw.rect(self.screen,(128,128,128), (0,0,self.size[0],self.size[1]))    # ecrase the screen
        
        for j in range(0,len(size_map)): # y
            for i in range(0,size_map[j]): # x
                a = lvl[(i,j)][2].data
                self.screen.blit(a,(i*30+10,j*30+10))
                
        for i in item:
            
            if i.bag == True and i.name == "needle":    
                self.screen.blit(i.data,(18*30+10,2*30+10))
        
            elif i.bag == True and i.name == "ether":    
                self.screen.blit(i.data,(19*30+10,2*30+10))
                
            elif i.bag == True and i.name == "plastic_tube":    
                self.screen.blit(i.data,(20*30+10,2*30+10))
                
            else :
                x, y = i.get_placement()
                self.screen.blit(i.data,(x*30+10,y*30+10))
                
                
        for i in character:
            
            a, x, y = i.create()
            self.screen.blit(a,(x*30+10,y*30+10))            
            
        if win == True :
            font=pygame.font.Font(None, 24)
            text = font.render("GAGNÉ",1,(255,255,255)) 
            self.screen.blit(text, (300, 300))
            
        if loose == True :
            font=pygame.font.Font(None, 24)
            text = font.render("PERDU",1,(255,255,255)) 
            self.screen.blit(text, (300, 300))          
            
            
