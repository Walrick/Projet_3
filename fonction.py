#!/usr/bin/python3
# -*- coding: utf8 -*-

import pygame
import random
import game

placement_item = []
    
class Tule :
    
    """ Class Tule for tule management """
    
    def __init__(self,name,data):
        
        self.name = name
        self.data = data
        
    def create (self):
    
        return self.data
    
        
class Item : 
    
    """ Class Item for item management """
        
    def __init__(self,name,data, x, y):
        
        self.name = name
        self.data = data
        self.x = x
        self.y = y
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
    
    """ Class Character for character management """
    
    def __init__(self,name,data):
        
        self.name = name
        self.data = data
        self.bag = 0
            
    def create(self):
        
        return (self.data, self.x, self.y)
        
    def move(self,direction, collision):
        
        x, y = self.x, self.y
         
        if direction == "up" and collision :
            self.y -= 1
        if direction == "down" and collision :
            self.y += 1
        if direction == "right" and collision :
            self.x += 1
        if direction == "left" and collision :
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

    return x , y

def collision(lvl, caractere, direction):
    
    shifting = False
    
    x , y = caractere.get_placement()
    if direction == "left" and lvl[(x-1,y)][0] != "wall_grey_1" :
        shifting = True
    if direction == "right" and lvl[(x+1,y)][0] != "wall_grey_1" :
        shifting = True    
    if direction == "up" and lvl[(x,y-1)][0] != "wall_grey_1" :
        shifting = True
    if direction == "down" and lvl[(x,y+1)][0] != "wall_grey_1"  :
        shifting = True          
    return shifting
    
    