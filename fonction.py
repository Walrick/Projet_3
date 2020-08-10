#!/usr/bin/python3
# -*- coding: utf8 -*-

import pygame
import random
import game

Tules = {}


def init_graphique():
    
    global tileset, screen, size
    
    pygame.init()
    size = (720, 530)                         # size of screen
    screen = pygame.display.set_mode(size)    # Display the screen(tuple)
    pygame.draw.rect(screen,(128,128,128), (0,0,size[0],size[1]))    
    
    tileset = pygame.image.load("objet_graphique/floor-tiles-20x20.png")          # init the tule
    Tule(0,0,"tule_deco_brown")                                                   
    Tule(20,0,"tule_brown")
    Tule(180,0,"wall_grey_1")
    
    needleset = pygame.image.load("objet_graphique/aiguille.png")        # init the needle
    Item("needle",needleset)
    
    etherset = pygame.image.load("objet_graphique/ether.png")         # init the ether
    Item("ether",etherset)
    
    plastic_tubeset = pygame.image.load("objet_graphique/tube_plastique.png")         # init the plastic_tubeset
    Item("plastic_tube",plastic_tubeset)
    
    MacGyverset = pygame.image.load("objet_graphique/MacGyver.png")         # init MacGyver
    Character("MacGyver", MacGyverset)
    
    Gardienset = pygame.image.load("objet_graphique/Gardien.png")         # init Gardien
    Character("Gardien", Gardienset)    
    
class Tule :
    
    """Crée et affiche les tuiles de décors"""
    
    def __init__(self,x,y,name):
        
        Tules[name] = tileset.subsurface((x,y,20,20))                    # select the tule
        Tules[name] = pygame.transform.scale(Tules[name], (30, 30))      # transform the size 
        
    def create (x,y,name):
    
        screen.blit(Tules[name],(y*30+10,x*30+10))                       # Display on the screen
        
class Item :
    
    """Crée et affiche les items du jeu"""
    
    dic =  {}

    def __init__(self,name,item):
        
        self.dic[name] = [pygame.transform.scale(item, (30, 30)),False,0,0]            # transform the size and create the list[data, carry on oneself, x, y]

    def create (x,y,name):
        
        screen.blit(Item.dic[name][0],(y*30+10,x*30+10))                               # Display on the screen et on transforme le placement x, y en pixel
        
    def random_placement(lvl):
        
        placement_item = []
        for name in Item.dic.keys():
            correct_placement = False 
            while correct_placement is False:
                item_stack = False
                x = random.randint(1,16)
                y = random.randint(1,16)
                if len(placement_item) != 0 :                                           # check the stack item
                    for i in placement_item :
                        if i[1] == x and i[2] == y :
                            item_stack = True
                
                if lvl[(x,y)][0] == "tule_brown" and item_stack == False :                              
                    correct_placement = True  
                    Item.dic[name][2] = x
                    Item.dic[name][3] = y
                    placement_item.append([name,x,y])
        return([placement_item[0],placement_item[1],placement_item[2]])
    
    def pickup_item (x, y, name):
        
        if game.lvl[(x,y)][1] != "":
            if x == Item.dic[game.lvl[(x,y)][1]][2] and y == Item.dic[game.lvl[(x,y)][1]][3]:
                Item.dic[game.lvl[(x,y)][1]][1] = True
            
        
class Character :
    
    """Crée et affiche les personnages du jeu"""
    
    dic = {}
    
    def __init__(self,name,item):
        
        self.dic[name] = [pygame.transform.scale(item, (30, 30)),0,0]             # transform the size and create the list[data, x, y]
    
    def create(x,y,name):
        
        screen.blit(Character.dic[name][0],(y*30+10,x*30+10))
        Character.dic[name][1] = x
        Character.dic[name][2] = y
        
    def move(direction,name):
        
        x = Character.dic[name][1]
        y = Character.dic[name][2]
        if direction == "up" and game.lvl[(x-1,y)][0] != "wall_grey_1":
            x -= 1
        if direction == "down" and game.lvl[(x+1,y)][0] != "wall_grey_1":
            x += 1
        if direction == "right" and game.lvl[(x,y+1)][0] != "wall_grey_1":
            y += 1
        if direction == "left" and game.lvl[(x,y-1)][0] != "wall_grey_1":
            y -= 1        
        Character.create(x,y,name)
        Item.pickup_item(x,y,name)
        
class Main ():
    
    win = False
    loose = False
    
    def __init__(self):
        
        init_graphique()
        game.game_desing()        
        
    def update():
        
        pygame.draw.rect(screen,(128,128,128), (0,0,size[0],size[1]))    # ecrase the screen
        game.update_lvl()
        Main.check_win()
        if Main.win  or Main.loose :
            Main.end()
        else :
            Character.move("","MacGyver")
            Character.move("","Gardien")
        pygame.display.update()                     # Update the screen   
        
        
    def end():
        
        if Main.win == True :
            font=pygame.font.Font(None, 24)
            text = font.render("GAGNÉ",1,(255,255,255)) 
            screen.blit(text, (300, 300))
            
        if Main.loose == True :
            font=pygame.font.Font(None, 24)
            text = font.render("PERDU",1,(255,255,255)) 
            screen.blit(text, (300, 300))       
            
    def check_win():
        
        mac_x = Character.dic["MacGyver"][1]
        mac_y = Character.dic["MacGyver"][2]
        gar_x = Character.dic["Gardien"][1]
        gar_y = Character.dic["Gardien"][2]
        
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
    
        
        
