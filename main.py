#!/usr/bin/python3
# -*- coding: utf8 -*-


import pygame
import fonction



def init():
    
    pygame.init()
    size = (720, 480)
    screen = pygame.display.set_mode(size)    # Display the screen(tuple)
    pygame.draw.rect(screen,(128,128,128), (0,0,size[0],size[1]))
    
    
    

init()


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
    
    
    pygame.display.update()


