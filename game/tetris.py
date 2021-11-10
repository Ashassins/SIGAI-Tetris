import pygame

class Tetris:
    level = 0
    score = 0
    state = "start"
    field  = []
    height = 0 
    width = 0
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
    
    def newFigure(self):
        self.figure = Figure(3, 0)

    def checkIntersection(self):
        intersection = False
        for i in range(4) :
            for j in range(r):
                if i * r + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                        j + self.figure.x > self.width - 1 or \
                        j + self.figure.x < 0 or \
                        self.field[i + self.figure.y][j + self.figure.x] > 0:
                            intersection = True
        return intersection

    def rotateClockwise(self):
        
    def rotateCounterClockwise(self):
        