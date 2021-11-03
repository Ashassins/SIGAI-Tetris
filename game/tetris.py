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
    
    def new_figure(self):
        self.figure = Figure(3, 0)

    