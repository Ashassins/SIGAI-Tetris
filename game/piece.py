import random

class Piece:
    x = 0
    y = 0
    rotation = 0
    pieceType = None
    shape = [[0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]

    def image(self):
        return self.shape

    def pickPiece(self, x, y):
        a = random.randint(1,7)
        if (a == 1):
            self.piece = lPiece(x,y)
        elif (a == 2):
            self.piece = squarePiece(x,y)
        elif (a == 3):
            self.piece = tPiece(x,y)
        elif (a == 4):
            self.piece = longPiece(x,y)
        elif (a == 5):
            self.piece = reverseSPiece(x,y)
        elif (a == 6):
            self.piece = sPiece(x,y)
        elif (a == 7):
            self.piece = reverseLPiece(x,y)
        return self.piece

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        self.piece = self.pickPiece(x,y)

class squarePiece(Piece):
    shapeArray = [[2, 2, 0, 0], 
            [2, 2, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]

    color = [255, 211, 0]

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[2, 2, 0, 0], 
            [2, 2, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        self.color = [255, 211, 0]
        self.rotation = 0
        self.pieceType = 1

class tPiece(Piece):  
    shapeArray = [[[0, 1, 0, 0], 
            [1, 1, 1, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]], 
            
            [[1, 0, 0, 0], 
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]], 

            [[1, 1, 1, 0],
            [0, 1, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]], 
            
            [[0, 1, 0, 0], 
            [1, 1, 0, 0], 
            [0, 1, 0, 0],
            [0, 0, 0, 0]]]

    color = [120, 22, 139]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 1, 0, 0], 
                [1, 1, 1, 0], 
                [0, 0, 0, 0], 
                [0, 0, 0, 0]]
        self.color = (120, 22, 139) # RGB Code for purple shade
        self.rotation = 0
        self.pieceType = 2 

class longPiece(Piece):
    shapeArray = [[[3, 0, 0, 0],
            [3, 0, 0, 0],
            [3, 0, 0, 0],
            [3, 0, 0, 0]],

            [[3, 3, 3, 3],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]]

    color = [0, 255, 0]

    def image(self):
        return self.shape

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[3, 0, 0, 0],
            [3, 0, 0, 0],
            [3, 0, 0, 0],
            [3, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.pieceType = 3

class reverseSPiece(Piece):
    shapeArray = [[[4, 4, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],
            
            [[0, 4, 0, 0],
            [4, 4, 0, 0],
            [4, 0, 0, 0],
            [0, 0, 0, 0]]]

    color = [0, 255, 0]

    def image(self):
        return self.shape
        
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[4, 4, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.pieceType = 4

class sPiece(Piece):
    shapeArray = [[[0, 5, 5, 0],
            [5, 5, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],
            
            [[5, 0, 0, 0],
            [5, 5, 0, 0],
            [0, 5, 0, 0],
            [0, 0, 0, 0]]]

    color = [0, 255, 0]

    def image(self):
        return self.shape
        
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 5, 5, 0],
            [5, 5, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.pieceType = 5

class reverseLPiece(Piece):
    shapeArray = [[[0, 6, 0, 0],
            [0, 6, 0, 0],
            [6, 6, 0, 0],
            [0, 0, 0, 0]],
                
            [[6, 0, 0, 0],
            [6, 6, 6, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],
                    
            [[6, 6, 0, 0],
            [6, 0, 0, 0],
            [6, 0, 0, 0],
            [0, 0, 0, 0]],
                    
            [[6, 6, 6, 0],
            [0, 0, 6, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]]

    color = [0, 255, 0]

    def image(self):
        return self.shape
        
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 6, 0, 0],
            [0, 6, 0, 0],
            [6, 6, 0, 0],
            [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.pieceType = 6

class lPiece(Piece):
    shapeArray = [[[7, 0, 0, 0],
        [7, 0, 0, 0],
        [7, 7, 0, 0],
        [0, 0, 0, 0]],
        
        [[7, 7, 7, 0],
        [7, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],
        
        [[7, 7, 0, 0],
        [0, 7, 0, 0],
        [0, 7, 0, 0],
        [0, 7, 0, 0]],
        
        [[0, 0, 7, 0],
        [7, 7, 7, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]]

    color = [0, 255, 0] # CHANGE COLOR

    def image(self):
        return self.shape
        
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [[7, 0, 0, 0],
            [7, 0, 0, 0],
            [7, 7, 0, 0],
            [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.pieceType = 7