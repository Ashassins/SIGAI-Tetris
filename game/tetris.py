import pygame
import piece 
from piece import Piece
class Tetris:
    level = 2
    score = 0
    state = "start"
    field  = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    piece = None

    def __init__(self, _height, _width):
        self.height = _height
        self.width = _width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(_height):
            new_line = []
            for j in range(_width):
                new_line.append(0)
            self.field.append(new_line)
    
    # creating a new piece at 3,0
    def newPiece(self):
        self.piece = Piece(3, 0) 

    # def intersectingPiece(self):
    #     intersection = False
    #     for i in range(4) :
    #         for j in range(4):
    #             if self.piece.image()[i][j]:
    #             # if i * 4 + j in self.piece.image():
    #             #     if i + self.piece.y > self.height - 1 or \
    #             #         j + self.piece.x > self.width - 1 or \
    #             #         j + self.piece.x < 0 or \
    #             #         self.field[i + self.piece.y][j + self.piece.x] > 0:
    #             #             intersection = True
    #     return intersection
    
    def notInBounds(self):
        intersection = False
        for i in range(4) :
            for j in range(4):
                if self.piece.image()[i][j]:
                    if self.piece.y > 16:
                        print("there was intersection")
                        intersection = True
                    elif self.piece.image()[i][j] and self.field[self.piece.y + i][self.piece.x + j]:
                        print("there was intersection")
                        intersection = True
                else:
                    print("no intersection")
                # if self.piece.y > 16:
                #     intersection = True
                # if i * 4 + j in self.piece.image():
                #     if i + self.piece.y > self.height - 1 or \
                #         j + self.piece.x > self.width - 1 or \
                #         j + self.piece.x < 0 or \
                #         self.field[i + self.piece.y][j + self.piece.x] > 0:
                #             print("intersection occurred")
                #             intersection = True
        return intersection

    def rotateClockwise(self):
        old_rotation = self.piece.shape
        self.piece.rotateClockwise()
        if self.notInBounds(): #self.checkIntersection():
            self.piece.shape = old_rotation

    def rotateCounterClockwise(self):
        old_rotation = self.piece.shape
        self.piece.rotateCounterClockwise()
        if self.notInBounds(): #self.checkIntersection():
            self.piece.shape = old_rotation

    def move_down(self):
        self.piece.y += 1
        if self.notInBounds(): #self.checkIntersection():
            print("move down, not in Bounds")
            self.piece.y -= 1
            self.place() 
    
    def move_sideways(self, dx):
        old_x = self.piece.x
        self.piece.x += dx
        if self.notInBounds(): #self.checkIntersection():
            self.piece.x = old_x

    def place(self):
        for i in range(4):
            for j in range(4):
                if self.piece.image()[i][j]:
                    self.field[i + self.piece.y][j + self.piece.x] &= self.piece.image()[i][j]
                    
        #self.break_lines()
        self.newPiece()
        # timer to check place + gameover
        if self.notInBounds(): #self.checkIntersection():
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