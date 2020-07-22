#!/usr/bin/python3
# -*- coding: utf8 -*-

from fonction import *

lvl = {}

def game_desing():
    
    """Affiche le niveau du jeux"""
    
    line = 0
    colum = 0
    
    path = open("Map.txt", "r")
    data = path.readlines()
    for lines in data :
        for i in lines :
            if i == " ":
                lvl[(line,colum)] = "tule_brown"
            elif i == "X":
                lvl[(line,colum)] = "wall_grey_1" 
            elif i == "A":
                lvl[(line,colum)] = "arrival" 
            elif i == "S":
                lvl[(line,colum)] = "exit"    
            colum += 1
        line += 1
        colum = 0
        
    print(lvl)
        
    for i in range(0,17): # x
        for j in range(0,17): # y  
            if lvl[(i,j)] == "arrival":
                Tule.create(i,j,"tule_deco_brown")
            elif lvl[(i,j)] == "exit":
                Tule.create(i,j,"tule_deco_brown")    
            elif lvl[(i,j)] == "tule_brown":
                Tule.create(i,j,"tule_brown")    
            elif lvl[(i,j)] == "wall_grey_1":
                Tule.create(i,j,"wall_grey_1")                    
    

    

    
 