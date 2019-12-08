#!/usr/bin/python3

import os, sys

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, i):
        return Vector2((self.x + i.x),(self.y + i.y))

    def __sub__(self, i):
        return Vector2((self.x - i.x),(self.y - i.y))

    def __mul__(self, i):
        return Vector2((self.x * i.x),(self.y * i.y))

    def __div__(self, i):
        return Vector2((self.x / i.x),(self.y / i.y))

    def coords(self):
        return Vector2(self.x, self.y)


class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @property
    def color(self):
        return (self.r, self.g, self.b)

    def __add__(self, c):
        return Color(self.clamp(self.r + c.r, 0, 255), self.clamp(self.r + c.g, 0, 255), self.clamp(self.r + c.b, 0, 255))

    def __sub__(self, c):
        return Color(self.clamp(self.r - c.r, 0, 255), self.clamp(self.r - c.g, 0, 255), self.clamp(self.r - c.b, 0, 255))

    @staticmethod
    def clamp(n, minv, maxv):
        return max(min(maxv, n), minv)

    @staticmethod
    def overflow(c):
        R, G, B = c.r, c.g, c.b
        if c.r > 255:
            val = round((c.r-255+.1)/2)
            R, G, B = c.r, G+val, B+val
        elif c.r < 0:
            val = int((c.r + c.r*2)/2)
            R, G, B = c.r, G+val, B+val
        if c.g > 255:
            val = round((c.g-255+.1)/2)
            R, G, B = R+val, c.g, B+val
        elif c.g < 0:
            val = int((c.g + c.g*2)/2)
            R, G, B = R+val, c.g, B+val
        if c.b > 255:
            val = round((c.b-255+.1)/2)
            R, G, B = R+val, G+val, c.b
        elif c.b < 0:
            val = int((c.b + c.b*2)/2)
            R, G, B = R+val, G+val, c.b
        return Color(Color.clamp(R, 0, 255), Color.clamp(G, 0, 255), Color.clamp(B, 0, 255))

    def add(self, r=0, g=0, b=0):
        self.r += r
        self.g += g
        self.b += b

    def sub(self, r=0, g=0, b=0):
        self.r -= r
        self.g -= g
        self.b -= b


class Pixel:

    def __init__(self, x, y, r, g, b, c):
        self.position = Vector2(x, y)
        self.color = Color(r, g, b)
        self.char = c

    def get_pos(self):
        return Vector2(self.x, self.y)

    def get_col(self):
        return Color(self.color.r, self.color.g, self.color.b)

    def get_char(self):
        return self.char


class Event:

    def get_key():
        os.system("stty raw -echo")
        c = sys.stdin.read(1)
        os.system("stty -raw echo")
        return c


class Display:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = []
        self.clear_cmd = ""

        if sys.platform.startswith('win32'):
            self.clear_cmd = 'cls'
        else:
            self.clear_cmd = 'clear'

        self.new_display()

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def get_size(self):
        size = (self.width, self.height)
        return size

    def clear(self):
        os.system(self.clear_cmd)

    def new_display(self):
        if len(self.matrix) > 0:
            self.matrix.clear()

        for y in range(self.height):
            for x in range(self.width):
                P = Pixel(x, y, 0, 0, 0, "  ")
                self.matrix.append(P)

    def draw(self, x, y, r, g, b, char):
        P = Pixel(x, y, r, g, b, char)
        try:
            self.matrix[(y * self.width) + x] = P
        except IndexError:
            pass#print(y*self.width+x)

    def render(self):
        self.clear()
        for i, pxl in enumerate(self.matrix):
                if i % self.width == 0:
                    print("")
                sys.stdout.write("\x1b[{};2;{};{};{}m".format(38, pxl.color.r, pxl.color.g, pxl.color.b) + pxl.char + '\x1b[0m')
        print("")
