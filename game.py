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
    for lines in data :                              # cette parties lis le fichier map et remplit le dictionnaire "lvl"
        for i in lines :
            if i == " ":
                lvl[(line,colum)] = ["tule_brown", "" ]
            elif i == "X":
                lvl[(line,colum)] = ["wall_grey_1", "" ]
            elif i == "A":
                lvl[(line,colum)] = ["arrival", "" ]
            elif i == "S":
                lvl[(line,colum)] = ["exit", "" ]
            colum += 1
        line += 1
        colum = 0
        
    liste_item = Item.random_placement(lvl)                 # ici on complete le dictionnaire avec les objets
    for a in liste_item :
        lvl[(a[1],a[2])][1] = a[0]
        
    # enfin ici on lis le dictionnaires lvl et on charges la map
    
    
    for i in range(0,17):    # x
        for j in range(0,17): # y  
            if lvl[(i,j)][0] == "arrival":
                Tule.create(i,j,"tule_deco_brown")
                Character.create(i,j,"MacGyver")
            elif lvl[(i,j)][0] == "exit":
                Tule.create(i,j,"tule_deco_brown") 
                Character.create(i,j,"Gardien")
            elif lvl[(i,j)][0] == "tule_brown":
                Tule.create(i,j,"tule_brown")  
                if lvl[(i,j)][1] != "":
                    Item.create(i,j,lvl[(i,j)][1])
            elif lvl[(i,j)][0] == "wall_grey_1":
                Tule.create(i,j,"wall_grey_1")      
                

    
    
    

    
 