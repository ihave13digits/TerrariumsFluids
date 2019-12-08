#!/usr/bin/python3

from fluid import *

class Engine:

    def __init__(self, X, Y):
        self.display = Display(X, Y)
        self.cursor = Cursor(0, 0)
        self.size = Vector2(X, Y)
        self.cells = []
        self.running = True
        self.paused = False
        for y in range(Y):
            for x in range(X):
                if x % X == 0 or x % X == X-1:
                    c = Cell(x, y, 0.0, 'wall')
                elif y == 0 or y == Y-1:
                    c = Cell(x, y, 0.0, 'wall')
                else:
                    c = Cell(x, y, 0.0, '')
                self.cells.append(c)

    def update(self):
        for i, c in enumerate(self.cells):
            if c.w > 0.0:
                direction = -1
                if self.cells[i+self.size.x].t != "wall" and self.cells[i+self.size.x].w < 1.0:
                    direction = i+self.size.x
                elif self.cells[i+self.size.x].t == "wall" or self.cells[i+self.size.x].w >= 1.0:
                    if self.cells[i-1].t != "wall" and self.cells[i-1].w < 1.0:
                        direction = i-1
                    if self.cells[i+1].t != "wall" and self.cells[i+1].w < 1.0:
                        direction = i+1
                    elif self.cells[i-1].t == "wall" or self.cells[i-1].w >= 1.0 and self.cells[i+self.size.x].t == "wall" or self.cells[i+self.size.x].w >= 1.0:
                        if self.cells[i-self.size.x].t != "wall" and self.cells[i-self.size.x].w < 1:
                            direction = i-self.size.x
                try:
                    if direction != -1:
                        c.split(self.cells[direction])
                except IndexError:
                    pass
            self.display.draw(c.position.x, c.position.y, c.color.r, c.color.g, c.color.b, c.img)
            self.display.draw(self.cursor.position.x, self.cursor.position.y, self.cursor.color.r, self.cursor.color.g, self.cursor.color.b, self.cursor.img)

    def run(self):
        while self.running == True:
            i = Event.get_key()

            if i == "w":
                if self.cursor.position.y > 0:
                    self.cursor.move(Vector2(0, -1))
            if i == "s":
                if self.cursor.position.y < self.size.y-1:
                    self.cursor.move(Vector2(0, 1))
            if i == "a":
                if self.cursor.position.x > 0:
                    self.cursor.move(Vector2(-1, 0))
            if i == "d":
                if self.cursor.position.x < self.size.x-1:
                    self.cursor.move(Vector2(1, 0))

            if i == "o":
                c = Cell(self.cursor.position.x, self.cursor.position.y, 0.0, "wall")
                self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "i":
                c = Cell(self.cursor.position.x, self.cursor.position.y, 0.0, "")
                self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "u":
                c = Cell(self.cursor.position.x, self.cursor.position.y, 0.0, "kill")
                self.cells[c.position.y * self.size.x + c.position.x] = c

            if i == "1":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.1, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "2":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.2, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "3":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.3, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "4":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.4, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "5":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.5, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "6":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.6, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "7":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.7, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "8":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.8, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "9":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 0.9, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c
            if i == "0":
                if self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x]!= "wall":
                    c = Cell(self.cursor.position.x, self.cursor.position.y, 1.0, "liquid")
                    self.cells[c.position.y * self.size.x + c.position.x] = c

            if i == "x":
                self.running = False
            if i == "p":
                if self.paused == True:
                    self.paused = False
                elif self.paused == False:
                    self.paused = True

            self.display.new_display()
            if self.paused == True:
                self.display.draw(self.cursor.position.x, self.cursor.position.y, self.cursor.color.r, self.cursor.color.g, self.cursor.color.b, self.cursor.img)
            elif self.paused == False:
                self.update()
            self.display.render()
            print("Paused:{} \nWater Value @ Vector2({}, {}): {}".format(self.paused,
                self.cursor.position.x, self.cursor.position.y,
                self.cells[self.cursor.position.y * self.size.x + self.cursor.position.x].w))

E = Engine(32, 16)

E.run()
