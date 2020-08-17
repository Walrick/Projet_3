#!/usr/bin/python3
# -*- coding: utf8 -*-

import pygame
import random
import game

placement_item = []
    
class Tule :
    
    def __init__(self,name,data):
        
        self.name = name
        self.data = data
        
    def create (self):
    
        return self.data
        
class Item : 
        
    def __init__(self,name,data):
        
        self.name = name
        self.data = data
        self.x , self.y = random_placement_item(game.Main.lvl)
        self.bag = False
        
    def create (self):
        
        return (self.data, self.x, self.y)
        
    def pickup_item (self):
        
        self.bag = True
        
    def set_placement(self, x, y):
        
        self.x = x
        self.y = y
        
    def get_placement(self):
        
        return (self.x, self.y)                
                

            
        
class Character : 
    
    """Create and display the graphic character""" 
    
    def __init__(self,name,data):
        
        self.name = name
        self.data = data
        self.bag = 0
            
    def create(self):
        
        return (self.data, self.x, self.y)
        
    def move(self,direction):
        
        x, y = self.x, self.y
         
        if direction == "up" and game.Main.lvl[(x,y-1)][0] != "wall_grey_1":
            self.y -= 1
        if direction == "down" and game.Main.lvl[(x,y+1)][0] != "wall_grey_1":
            self.y += 1
        if direction == "right" and game.Main.lvl[(x+1,y)][0] != "wall_grey_1":
            self.x += 1
        if direction == "left" and game.Main.lvl[(x-1,y)][0] != "wall_grey_1":
            self.x -= 1        
        
    def set_placement(self, x, y):
        
        self.x = x
        self.y = y
        
    def get_placement(self):
        
        return (self.x, self.y)
    
    def pickup_item(self):
        
        self.bag += 1
    
        
        
        
def random_placement_item(lvl):
    
    correct_placement = False 
    while correct_placement is False:
        item_stack = False
        x = random.randint(1,16)
        y = random.randint(1,16)
        if len(placement_item) != 0 :                                           # check the stack item
            for i in placement_item :
                if i[0] == x and i[1] == y :
                    item_stack = True
        
        if lvl[(x,y)][0] == "tule_brown" and item_stack == False :                              
            correct_placement = True 
            placement_item.append([x,y])

    return( x , y )