#!/usr/bin/python3
# -*- coding: utf8 -*-


import pygame

from graphic import *

from package.fonction import *

from package.tule import *
from package.item import *
from package.character import *


class Main ():

    """Main class for manage the game"""

    def __init__(self):
        """ init the Main class for the game """

        self.graphic = Graphic()

        self.lvl = {}
        self.item = []
        self.character = []

        self.size_map = []                      # init size_map list [nomber line for colum 1 , nomber line for colum 2, etc ...]
        self.win = False
        self.loose = False

        line = 0
        colum = 0

        path = open("Map.txt", "r")
        data = path.readlines()
        for lines in data:  # Read the Map.txt and write in the dic "lvl"
            for i in lines:
                if i == " ":
                    self.lvl[(line, colum)] = ["None", "tule_brown"]        # lvl[(x,y)] = ["type of tule", "name tule"]
                elif i == "X":
                    self.lvl[(line, colum)] = ["None", "wall_grey_1"]
                elif i == "A":
                    self.lvl[(line, colum)] = ["arrival", "tule_deco_brown"]
                elif i == "S":
                    self.lvl[(line, colum)] = ["exit", "tule_deco_brown"]
                else:
                    self.lvl[(line, colum)] = ["None", "tule_brown"]
                line += 1
            colum += 1
            self.size_map.append(line - 1)
            line = 0

        for j in range(0, len(self.size_map)):  # y                     Instance the tule
            for i in range(0, self.size_map[j]):  # x

                if self.lvl[(i, j)][1] == "wall_grey_1":
                    self.lvl[(i, j)] = Tule(self.lvl[(i, j)][1], self.graphic.dic_tule[self.lvl[(i, j)][1]], False, self.lvl[(i, j)][0])  # name, data, collision, type_tule
                else:
                    self.lvl[(i, j)] = Tule(self.lvl[(i, j)][1], self.graphic.dic_tule[self.lvl[(i, j)][1]], True, self.lvl[(i, j)][0])

        for i in self.graphic.item:                                # instance item
            x, y = random_placement_item(self.lvl)
            self.item.append(Item(i[0], i[1], x, y))

        for i in self.graphic.character:                           # instance character
            self.character.append(Character(i[0], i[1]))

        for i in self.character:                                   # Placement character
            for x in range(0, len(self.size_map)):  # y                     Instance the tule
                for y in range(0, self.size_map[j]):  # x

                    if self.lvl[x, y].type_tule == "arrival" and i.name == "MacGyver":
                        i.set_placement(x, y)
                    if self.lvl[x, y].type_tule == "exit" and i.name == "Gardien":
                        i.set_placement(x, y)

    def launch(self):
        """ launch the game """

        self.loop_master()

    def loop_master(self):
        """ loop master for the game """

        running = True

        while running:                                     # Event management loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:        # For event type KEYDOWN
                    if event.key == pygame.K_ESCAPE:    # Exit
                        running = False
                    elif event.key == pygame.K_LEFT and (self.win == False and self.loose == False):
                        self.character[0].move("left", collision_test(self.lvl, self.character[0], "left"))
                    elif event.key == pygame.K_UP and (self.win == False and self.loose == False):
                        self.character[0].move("up", collision_test(self.lvl, self.character[0], "up"))
                    elif event.key == pygame.K_RIGHT and (self.win == False and self.loose == False):
                        self.character[0].move("right", collision_test(self.lvl, self.character[0], "right"))
                    elif event.key == pygame.K_DOWN and (self.win == False and self.loose == False):
                        self.character[0].move("down", collision_test(self.lvl, self.character[0], "down"))

            self.check_pickup_item()

            self.check_win()

            self.graphic.display(self.size_map, self.lvl, self.item, self.character, self.win, self.loose)                      # Load the screen

            pygame.display.update()                    # Update the screen

    def check_pickup_item(self):
        """ check the pickup item """

        mac_x, mac_y = self.character[0].get_placement()
        for item in self.item:
            x, y = item.get_placement()
            if mac_x == x and mac_y == y and item.bag == False:
                item.pickup_item()
                self.character[0].pickup_item()

    def check_win(self):
        """ check the end game, for win or loose  """

        mac_x, mac_y = self.character[0].get_placement()
        gar_x, gar_y = self.character[1].get_placement()
        total_item = self.character[0].bag

        if mac_x - 1 == gar_x and mac_y == gar_y:
                if total_item == 3:
                    self.win = True
                else:
                    self.loose = True

        if mac_x + 1 == gar_x and mac_y == gar_y:
                if total_item == 3:
                    self.win = True
                else:
                    self.loose = True

        if mac_y + 1 == gar_y and mac_x == gar_x:
                if total_item == 3:
                    self.win = True
                else:
                    self.loose = True

        if mac_y - 1 == gar_y and mac_x == gar_x:
                if total_item == 3:
                    self.win = True
                else:
                    self.loose = True



