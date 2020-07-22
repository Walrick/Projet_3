#!/usr/bin/python3
# -*- coding: utf8 -*-


import pygame
import fonction


fonction.init_graphique()


fonction.Tule.create(10,10,"tule_deco_brown")
fonction.Tule.create(30,30,"tule_deco_brown")
fonction.Tule.create(50,30,"wall_grey_1")
fonction.Tule.create(70,30,"wall_grey_3")
fonction.Tule.create(90,30,"wall_grey_3")
fonction.Tule.create(110,30,"wall_grey_3")



running = True

while running:                                     # Event loop launch    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:        # For event type KEYDOWN
            if event.key == pygame.K_ESCAPE:    
                running = False
            elif event.key == pygame.K_LEFT:
                print("gauche")
            elif event.key == pygame.K_UP:
                print("haut")
            elif event.key == pygame.K_RIGHT:
                print("droite")
            elif event.key == pygame.K_DOWN:
                print("bas") 
    
    
    pygame.display.update()                     # Update the screen


