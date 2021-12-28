import random

class Piece:
    x = 0
    y = 0
    rotation = 0
    pieceType = None
    numRotations = 0
    color = [255, 0, 0]
    #shape = self.shape

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

    def rotateClockwise(self):
        self.rotation = self.rotation + 1
        N = len(self.shape[0])
        for i in range (N // 2):
            for j in range (i, N - i - 1):
                temp = self.shape[i][j]
                self.shape[i][j] = self.shape[N - 1 - j][i]
                self.shape[N - 1 - j][i] = self.shape[N - 1 - i][N - 1 - j]
                self.shape[N - 1 - i][N - 1 - j] = self.shape[j][N - 1 - i]
                self.shape[j][N - 1 - i] = temp
        return self.shape

    def rotateCounterClockwise(self):
        self.rotation = self.rotation - 1
        m = self.shape
        new_matrix = [
            [m[j][i]
            for j in range(len(m))
            ]
            for i in range(len(m[0]) - 1, -1, -1)
        ]
        self.shape = new_matrix
        return self.shape

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        self.piece = self.pickPiece(x,y)
        self.shape = self.piece.shape

class squarePiece(Piece):
    shapeArray = [[[0, 0, 0, 0], 
            [0, 0, 0, 0],
            [1, 1, 0, 0], 
            [1, 1, 0, 0]
            ]]

    color = [255, 211, 0]

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 0, 0, 0], 
            [0, 0, 0, 0],
            [1, 1, 0, 0], 
            [1, 1, 0, 0]]
        self.color = [255, 211, 0]
        self.rotation = 0
        self.numRotations = 0
        self.pieceType = 1

class tPiece(Piece):  
    shapeArray = [[[0, 0, 0, 0], 
            [0, 0, 0, 0],
            [0, 2, 0, 0], 
            [2, 2, 2, 0]], 
            
            [[0, 0, 0, 0],
            [2, 0, 0, 0], 
            [2, 2, 0, 0],
            [2, 0, 0, 0]], 

            [[0, 0, 0, 0], 
            [0, 0, 0, 0],
            [2, 2, 2, 0],
            [0, 2, 0, 0]], 
            
            [[0, 0, 0, 0],
            [0, 2, 0, 0], 
            [2, 2, 0, 0], 
            [0, 2, 0, 0]]]

    color = [120, 22, 139]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 0, 0, 0], 
            [0, 0, 0, 0],
            [0, 2, 0, 0], 
            [2, 2, 2, 0]]
        self.color = (120, 22, 139) # RGB Code for purple shade
        self.rotation = 0
        self.numRotations = 4
        self.pieceType = 2 

class longPiece(Piece):
    shapeArray = [[[3, 3, 3, 3],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[3, 0, 0, 0],
            [3, 0, 0, 0],
            [3, 0, 0, 0],
            [3, 0, 0, 0]]]

    color = [0, 255, 0]

    def image(self):
        return self.shape

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[3, 3, 3, 3],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.numRotations = 2
        self.pieceType = 3

class reverseSPiece(Piece):
    shapeArray = [[
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 4, 0, 0],
            [0, 4, 4, 0]],
            
            [[0, 0, 0, 0],
            [0, 4, 0, 0],
            [4, 4, 0, 0],
            [4, 0, 0, 0]]]

    color = [0, 255, 0]

    def image(self):
        return self.shape
        
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 4, 0, 0],
            [0, 4, 4, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.numRotations = 4
        self.pieceType = 4

class sPiece(Piece):
    shapeArray = [[[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 5, 5, 0],
            [5, 5, 0, 0]],
            
            [[0, 0, 0, 0],
            [5, 0, 0, 0],
            [5, 5, 0, 0],
            [0, 5, 0, 0]]]

    color = [0, 255, 0]

    def image(self):
        return self.shape
        
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 5, 5, 0],
            [5, 5, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.numRotations = 4
        self.pieceType = 5

class reverseLPiece(Piece):
    shapeArray = [[[0, 0, 0, 0],
            [0, 0, 0, 0],
            [6, 0, 0, 0],
            [6, 6, 6, 0]],

            [[0, 0, 0, 0],
            [0, 6, 0, 0],
            [0, 6, 0, 0],
            [6, 6, 0, 0]],
                    
            [[0, 0, 0, 0],
            [6, 6, 0, 0],
            [6, 0, 0, 0],
            [6, 0, 0, 0]],
                    
            [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [6, 6, 6, 0],
            [0, 0, 6, 0]]]

    color = [0, 255, 0]

    def image(self):
        return self.shape
        
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [6, 0, 0, 0],
            [6, 6, 6, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.numRotations = 4
        self.pieceType = 6

class lPiece(Piece):
    shapeArray = [
        [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 7, 0],
        [7, 7, 7, 0]],
        
        [[0, 0, 0, 0],
        [7, 0, 0, 0],
        [7, 0, 0, 0],
        [7, 7, 0, 0]],
        
        [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [7, 7, 7, 0],
        [7, 0, 0, 0]],
        
        [[0, 0, 0, 0],
        [7, 7, 0, 0],
        [0, 7, 0, 0],
        [0, 7, 0, 0]]]

    color = [0, 255, 0] # CHANGE COLOR

    def image(self):
        return self.shape
        
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 7, 0],
        [7, 7, 7, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0
        self.numRotations = 4
        self.pieceType = 7