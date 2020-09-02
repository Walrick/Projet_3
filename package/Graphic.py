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

        # size of screen
        self.size = (720, 530)
        pygame.init()
        # Display the screen(tuple)
        self.screen = pygame.display.set_mode(self.size)
        pygame.draw.rect(self.screen, (128, 128, 128),
                         (0, 0, self.size[0], self.size[1]))

        # init the tule
        tileset = pygame.image.load(
            "package/objet_graphique/floor-tiles-20x20.png")
        self.load_tule(0, 0, "tule_deco_brown", tileset)
        self.load_tule(20, 0, "tule_brown", tileset)
        self.load_tule(180, 0, "wall_grey_1", tileset)

        # init the needle
        needleset = pygame.image.load("package/objet_graphique/aiguille.png")
        self.load_item("needle", needleset)

        # init the ether
        etherset = pygame.image.load("package/objet_graphique/ether.png")
        self.load_item("ether", etherset)

        # init the plastic_tubeset
        plastic_tubeset = pygame.image.load(
            "package/objet_graphique/tube_plastique.png")
        self.load_item("plastic_tube", plastic_tubeset)

        # init the syringe
        syringueset = pygame.image.load("package/objet_graphique/seringue.jpg")
        white = (255, 255, 255)
        syringueset.set_colorkey(white)
        self.load_item("syringe", syringueset)

        # init MacGyver
        MacGyverset = pygame.image.load("package/objet_graphique/MacGyver.png")
        self.load_character("MacGyver", MacGyverset)

        # init Gardien
        Gardienset = pygame.image.load("package/objet_graphique/Gardien.png")
        self.load_character("Gardien", Gardienset)

    def load_tule(self, x, y, name, data):
        """ load the tiles and fill in the dictionary """

        # select the tule
        data = data.subsurface((x, y, 20, 20))
        # transform the size
        data = pygame.transform.scale(data, (30, 30))
        self.dic_tule[name] = data

    def load_item(self, name, data):
        """ load the items and fill in the item list """

        # transform the size
        data = pygame.transform.scale(data, (30, 30))
        self.item.append([name, data])

    def load_character(self, name, data):
        """ load the character and fill in the character list """

        # transform the size
        data = pygame.transform.scale(data, (30, 30))
        self.character.append([name, data])

    def display(self, size_map, lvl, item, character, win, loose):
        """ display the game """

        # ecrase the screen
        pygame.draw.rect(self.screen, (128, 128, 128),
                         (0, 0, self.size[0], self.size[1]))

        for j in range(0, len(size_map)):  # y
            for i in range(0, size_map[j]):  # x
                a = lvl[(i, j)].data
                self.screen.blit(a, (i * 30 + 10, j * 30 + 10))

        for i in item:

            if i.bag and i.name == "needle":
                self.screen.blit(i.data, (18 * 30 + 10, 2 * 30 + 10))

            elif i.bag and i.name == "ether":
                self.screen.blit(i.data, (19 * 30 + 10, 2 * 30 + 10))

            elif i.bag and i.name == "plastic_tube":
                self.screen.blit(i.data, (20 * 30 + 10, 2 * 30 + 10))

            elif i.bag and i.name == "syringe":
                self.screen.blit(i.data, (19 * 30 + 10, 4 * 30 + 10))

            else:
                if i.name != "syringe":
                    x, y = i.get_placement()
                    self.screen.blit(i.data, (x * 30 + 10, y * 30 + 10))

        for i in character:

            x, y = i.get_placement()
            self.screen.blit(i.data, (x * 30 + 10, y * 30 + 10))

        if win:
            font = pygame.font.Font(None, 24)
            text = font.render("GAGNÉ", 1, (255, 255, 255))
            self.screen.blit(text, (300, 300))

        if loose:
            font = pygame.font.Font(None, 24)
            text = font.render("PERDU", 1, (255, 255, 255))
            self.screen.blit(text, (300, 300))
