#!/usr/bin/python3
# -*- coding: utf8 -*-


class Character:

    """ Class Character for character management """

    def __init__(self, name, data):
        """ init the character """

        self.name = name
        self.data = data
        self.bag = 0

    def move(self, direction, collision):
        """ move the character """

        if direction == "up" and collision:
            self.y -= 1
        if direction == "down" and collision:
            self.y += 1
        if direction == "right" and collision:
            self.x += 1
        if direction == "left" and collision:
            self.x -= 1

    def set_placement(self, x, y):
        """ set the character placement """

        self.x = x
        self.y = y

    def get_placement(self):
        """ return character placement """

        return (self.x, self.y)

    def pickup_item(self):
        """ count the items in the bag """

        self.bag += 1
