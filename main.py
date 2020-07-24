#!/usr/bin/python3
# -*- coding: utf8 -*-


import pygame
import fonction
import game


fonction.init_graphique()
game.game_desing()





running = True

while running:                                     # Event loop launch    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:        # For event type KEYDOWN
            if event.key == pygame.K_ESCAPE:    
                running = False
            elif event.key == pygame.K_LEFT:
                print("gauche")
                fonction.Character.move("left","MacGyver")
            elif event.key == pygame.K_UP:
                print("haut")
                fonction.Character.move("up","MacGyver")
            elif event.key == pygame.K_RIGHT:
                print("droite")
                fonction.Character.move("right","MacGyver")
            elif event.key == pygame.K_DOWN:
                print("bas") 
                fonction.Character.move("down","MacGyver")
                


