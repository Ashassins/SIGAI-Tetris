import random


class Piece:

    x = 0
    y = 0
    
    def __init__ (self, x, y):
        self.x = x
        self.y = y


class squarePiece(Piece):

    x = 0
    y = 0

    shape = [[2, 2, 0, 0], 
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


class TPiece(Piece):

    x = 0
    y = 0
    
    shape = [[[0, 1, 0, 0], 
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


class longPiece(Piece):

    x = 0
    y = 0

    shape = [[[3, 0, 0, 0],
             [3, 0, 0, 0],
             [3, 0, 0, 0],
             [3, 0, 0, 0]],
                  
            [[3, 3, 3, 3],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]]

    color = [0, 255, 0]

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[3, 0, 0, 0],
             [3, 0, 0, 0],
             [3, 0, 0, 0],
             [3, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0


class reverseSPiece(Piece):

    x = 0
    y = 0

    shape = [[[4, 4, 0, 0],
              [0, 4, 4, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]],
               
             [[0, 4, 0, 0],
              [4, 4, 0, 0],
              [4, 0, 0, 0],
              [0, 0, 0, 0]]]

    color = [0, 255, 0]

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[4, 4, 0, 0],
              [0, 4, 4, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0


class SPiece(Piece):

    x = 0
    y = 0

    shape = [[[0, 5, 5, 0],
               [5, 5, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],
               
              [[5, 0, 0, 0],
               [5, 5, 0, 0],
               [0, 5, 0, 0],
               [0, 0, 0, 0]]]

    color = [0, 255, 0]

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 5, 5, 0],
               [5, 5, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0


class reverseLPiece(Piece):

    x = 0
    y = 0

    shape = [[[0, 6, 0, 0],
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

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.shape = [[0, 6, 0, 0],
              [0, 6, 0, 0],
              [6, 6, 0, 0],
              [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0


    class lPiece(Piece):

        x = 0
        y = 0

        shape = [[[7, 0, 0, 0],
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

    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [[7, 0, 0, 0],
               [7, 0, 0, 0],
               [7, 7, 0, 0],
               [0, 0, 0, 0]]
        self.color = [0, 255, 0]
        self.rotation = 0