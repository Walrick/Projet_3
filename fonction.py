#!/usr/bin/python3
# -*- coding: utf8 -*-

import pygame



Tules = {}

def init_graphique():
    
    global tileset, screen
    
    pygame.init()
    size = (720, 480)                         # size of screen
    screen = pygame.display.set_mode(size)    # Display the screen(tuple)
    pygame.draw.rect(screen,(128,128,128), (0,0,size[0],size[1]))    
    
    tileset = pygame.image.load("objet_graphique/floor-tiles-20x20.png")          # init the tule
    Tule(0,0,"tule_deco_brown")                                                   # select the tule
    Tule(20,0,"tule_brown")
    Tule(100,0,"wall_grey_1")
    Tule(140,0,"wall_grey_2")
    Tule(180,0,"wall_grey_3")
    
    
class Tule :
    
    """Crée et affiche les tuiles de décors"""
    
    def __init__(self,x,y,name):
        
        Tules[name] = tileset.subsurface((x,y,20,20))
        
    def create (x,y,name):
    
        screen.blit(Tules[name],(x,y))

        
        

