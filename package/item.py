#!/usr/bin/python3
# -*- coding: utf8 -*-


class Item:

    """ Class Item for item management """

    def __init__(self, name, data, x, y):
        """ init the item """

        self.name = name
        self.data = data
        self.x = x
        self.y = y
        self.bag = False

    def pickup_item(self):
        """ if the item in the bag """

        self.bag = True

    def set_placement(self, x, y):
        """ set the item placement """

        self.x = x
        self.y = y

    def get_placement(self):
        """ get the item placement """

        return (self.x, self.y)
