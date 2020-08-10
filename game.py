#!/usr/bin/python3
# -*- coding: utf8 -*-

import fonction

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
    
    liste_item = fonction.Item.random_placement(lvl)                # ici on complete le dictionnaire avec les objets
    for a in liste_item :
        lvl[(a[1],a[2])][1] = a[0]
        
    # enfin ici on lis le dictionnaires lvl et on charges la map pour la premiere fois
    
    
    for i in range(0,17): # x
        for j in range(0,17): # y  
            if lvl[(i,j)][0] == "arrival":
                fonction.Tule.create(i,j,"tule_deco_brown")
                fonction.Character.create(i,j,"MacGyver")
            elif lvl[(i,j)][0] == "exit":
                fonction.Tule.create(i,j,"tule_deco_brown") 
                fonction.Character.create(i,j,"Gardien")
            elif lvl[(i,j)][0] == "tule_brown":
                fonction.Tule.create(i,j,"tule_brown")  
                if lvl[(i,j)][1] != "":
                    fonction.Item.create(i,j,lvl[(i,j)][1])
            elif lvl[(i,j)][0] == "wall_grey_1":
                fonction.Tule.create(i,j,"wall_grey_1")      
                
def update_lvl():
    
    """ update the map"""
    for i in range(0,17):    # x
        for j in range(0,17): # y  
            
            if lvl[(i,j)][0] == "arrival":
                fonction.Tule.create(i,j,"tule_deco_brown")
            elif lvl[(i,j)][0] == "exit":
                fonction.Tule.create(i,j,"tule_deco_brown") 
            elif lvl[(i,j)][0] == "tule_brown":
                fonction.Tule.create(i,j,"tule_brown")  
                if lvl[(i,j)][1] != "":
                    if fonction.Item.dic[lvl[(i,j)][1]][1] == False :
                        fonction.Item.create(i,j,lvl[(i,j)][1])
            elif lvl[(i,j)][0] == "wall_grey_1":
                fonction.Tule.create(i,j,"wall_grey_1")    
                
    fonction.total_item = 0            
    for name in fonction.Item.dic.keys():
        if fonction.Item.dic[name][1] == True and name == "needle":    
            fonction.Item.create(2,18,name)
            fonction.total_item += 1

        if fonction.Item.dic[name][1] == True and name == "ether":    
            fonction.Item.create(2,19,name)  
            fonction.total_item += 1
        
        if fonction.Item.dic[name][1] == True and name == "plastic_tube":    
            fonction.Item.create(2,20,name)
            fonction.total_item += 1
            
