
#!/usr/bin/python3
# -*- coding: utf8 -*-



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