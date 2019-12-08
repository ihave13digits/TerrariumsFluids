#!/usr/bin/python3

from tools import *

class Cursor:

    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.color = Color(255, 0, 0)
        self.img = '█'

    def move(self, d):
        self.position = self.position + d

class Cell:

    # w = water value, t = cell type

    def __init__(self, x, y, w, t):
        self.position = Vector2(x, y)
        self.color = Color(0, 0, 0)
        self.img = ' '
        self.w = w
        self.t = t
        self.update_color()

    def update_color(self):
        if self.t == "kill":
            self.color = Color(255, 0, 0)
            self.img = "X"
        elif self.t == "wall":
            self.color = Color(55, 55, 55)
            self.img = '█'
        else:
            self.color = Color(0, 0, 255)

    def update_img(self):
        if self.t != "wall":
            self.t = ""
            self.img = ' '

        if self.w <= 0.03125:
            self.w = 0
            self.img = ' '
        elif self.w <= 0.0625:
            self.img = '_'
            self.t = "liquid"
        elif self.w <= 0.125:
            self.img = '▁'
        elif self.w <= 0.25:
            self.img = '▂'
        elif self.w <= 0.375:
            self.img = '▃'
        elif self.w <= 0.5:
            self.img = '▄'
        elif self.w <= 0.625:
            self.img = '▅'
        elif self.w <= 0.75:
            self.img = '▆'
        elif self.w <= 0.875:
            self.img = '▇'
        elif self.w <= 1.0:
            self.img = '█'
        #else:
        #    self.img = ' '

    def move(self, o):
        if self.t != "wall" and o.t != "wall":
            if self.w > o.w:
                if self.w > 1.0:
                    o.w = 1
                    self.w -= 1
                elif self.w <= 1.0:
                    o.w = self.w
                    self.w = 0
            elif self.w < o.w:
                if o.w > 1.0:
                    self.w = 1
                    o.w -= 1
                elif o.w <= 1.0:
                    self.w = o.w
                    o.w = 0

    def split(self, o):
        if self.t == "kill" or o.t == "kill":
            self.w = 0.0
            o.w = 0.0
        if self.t != "wall" and o.t != "wall":
            if self.w > o.w:
                if self.w > 1.0:
                    o.w += self.w-1.0
                    self.w = 1.0
                elif self.w <= 1.0:
                    o.w += self.w/2
                    self.w -= self.w/2
            elif self.w < o.w:
                if o.w > 1.0:
                    self.w += o.w-1.0
                    o.w = 1.0
                elif o.w <= 1.0:
                    self.w += o.w/2
                    o.w -= o.w/2

        self.update_color()
        self.update_img()
