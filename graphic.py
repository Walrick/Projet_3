#!/usr/bin/python3
# -*- coding: utf8 -*-

import pygame


class Graphic:

    """Load dic_tule, item and character and manage the screen """



    def __init__(self):
        """ init the Graphic class """
        
        self.dic_tule = {}
        self.item = []
        self.character = []        

        self.size = (720, 530)                   # size of screen
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)    # Display the screen(tuple)
        pygame.draw.rect(self.screen, (128, 128, 128), (0, 0, self.size[0], self.size[1]))

        tileset = pygame.image.load("package/objet_graphique/floor-tiles-20x20.png")          # init the tule
        self.load_tule(0, 0, "tule_deco_brown", tileset)
        self.load_tule(20, 0, "tule_brown", tileset)
        self.load_tule(180, 0, "wall_grey_1", tileset)

        needleset = pygame.image.load("package/objet_graphique/aiguille.png")        # init the needle
        self.load_item("needle", needleset)

        etherset = pygame.image.load("package/objet_graphique/ether.png")         # init the ether
        self.load_item("ether", etherset)

        plastic_tubeset = pygame.image.load("package/objet_graphique/tube_plastique.png")         # init the plastic_tubeset
        self.load_item("plastic_tube", plastic_tubeset)

        MacGyverset = pygame.image.load("package/objet_graphique/MacGyver.png")         # init MacGyver
        self.load_character("MacGyver", MacGyverset)

        Gardienset = pygame.image.load("package/objet_graphique/Gardien.png")         # init Gardien
        self.load_character("Gardien", Gardienset)

    def load_tule(self, x, y, name, data):
        """ load the tiles and fill in the dictionary """

        data = data.subsurface((x, y, 20, 20))                    # select the tule
        data = pygame.transform.scale(data, (30, 30))       # transform the size
        self.dic_tule[name] = data

    def load_item(self, name, data):
        """ load the items and fill in the item list """

        data = pygame.transform.scale(data, (30, 30))       # transform the size
        self.item.append([name, data])

    def load_character(self, name, data):
        """ load the character and fill in the character list """

        data = pygame.transform.scale(data, (30, 30))       # transform the size
        self.character.append([name, data])

    def display(self, size_map, lvl, item, character, win, loose):
        """ display the game """

        pygame.draw.rect(self.screen, (128, 128, 128), (0, 0, self.size[0], self.size[1]))    # ecrase the screen

        for j in range(0, len(size_map)):  # y
            for i in range(0, size_map[j]):  # x
                a = lvl[(i, j)].data
                self.screen.blit(a, (i * 30 + 10, j * 30 + 10))

        for i in item:

            if i.bag == True and i.name == "needle":
                self.screen.blit(i.data, (18 * 30 + 10, 2 * 30 + 10))

            elif i.bag == True and i.name == "ether":
                self.screen.blit(i.data, (19 * 30 + 10, 2 * 30 + 10))

            elif i.bag == True and i.name == "plastic_tube":
                self.screen.blit(i.data, (20 * 30 + 10, 2 * 30 + 10))

            else:
                x, y = i.get_placement()
                self.screen.blit(i.data, (x * 30 + 10, y * 30 + 10))

        for i in character:

            x, y = i.get_placement()
            self.screen.blit(i.data, (x * 30 + 10, y * 30 + 10))

        if win == True:
            font = pygame.font.Font(None, 24)
            text = font.render("GAGNÉ", 1, (255, 255, 255))
            self.screen.blit(text, (300, 300))

        if loose == True:
            font = pygame.font.Font(None, 24)
            text = font.render("PERDU", 1, (255, 255, 255))
            self.screen.blit(text, (300, 300))


