import pygame

class Tetris:
    level = 0
    score = 0
    state = "start"
    field  = []
    height = 22
    width = 10
    piece = None

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
    
    # creating a new piece at 3,0
    def newPiece(self):
        self.piece = Piece(3, 0) 

    def checkIntersection(self):
        intersection = False
        for i in range(4) :
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                        j + self.figure.x > self.width - 1 or \
                        j + self.figure.x < 0 or \
                        self.field[i + self.figure.y][j + self.figure.x] > 0:
                            intersection = True
        return intersection

    def rotateClockwise(self):
        old_rotation = self.piece.shape
        self.piece.rotateClockwise()
        if self.intersects():
            self.piece.shape = old_rotation

    def rotateCounterClockwise(self):
        old_rotation = self.piece.shape
        self.piece.rotateCounterClockwise()
        if self.intersects():
            self.piece.shape = old_rotation

    def move_down(self):
        self.shape.y -= 1
        if self.checkIntersection():
            self.shape.y += 1
            self.place() 
    
    def go_side(self, dx):
        old_x = self.piece.old_x
        self.piece.x += dx
        if self.checkIntersection():
            self.piece.x = old_x

    def place(self):
        self.break_lines()
        self.new_figure()
        # timer to check place + gameover
        if self.checkIntersection():
            self.state = "gameover"

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeroes = 0 
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeroes += 1
            if zeroes == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2