#!/usr/bin/python3
# -*- coding: utf8 -*-



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