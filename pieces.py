# stores the positional data of each shape
import pygame as pg

class Sue():
    # matrix of x and y changes between orientations
    #                x               y     room needed [x, y]
    deltas =   [[[0,  1, 0,  1], 
                 [ 1, 0, -1, -2], [1, 0]], # from orientation 1 to 2
                [[0, -1, 0, -1], 
                 [-1, 0,  1,  2], [0, 1]]] # 2 to 1
    # tracks part positions
    position = [[4, 4, 5, 5],
                [0, 1, 1, 2]]
    # which block is visible for each side at each orientation
    borders =  [[[1, 3], [0, 1, 3]], #bottom
                [[0, 2, 3], [1, 3]], #right
                [[0, 1, 3], [0, 2]]] #left
    #tracker for orientation
    orientation = 0

    def __init__(self):
        self.position = [[4, 4, 5, 5],
                         [0, 1, 1, 2]]  

class Steve():
    deltas =   [[[ 1,  2, -1, 0], 
                 [0, -1, 0, -1], [1, 0]],
                [[-1, -2,  1, 0], 
                 [0,  1, 0,  1], [0, 1]]]
    position = [[4, 4, 5, 5],
                [1, 2, 0, 1]]
    borders =  [[[1, 3], [0, 1, 2]],
                [[2, 3, 1], [3, 1]],
                [[2, 0, 1], [2, 0]]]
    orientation = 0

    def __init__(self):
        self.position = [[4, 4, 5, 5],
                         [1, 2, 0, 1]]

class Larry():
    deltas =   [[[ 0,  1,  2,  1], [ 1,  0, -1, -2], [1, 0]], 
                [[ 1,  0, -1, -2], [ 1,  0, -1,  0], [0, 1]], 
                [[ 1,  0, -1,  0], [-2,  -1,  0,  1], [-1, 0]], 
                [[-2, -1,  0,  1], [ 0,  1,  2,  1], [0, 1]]]
    position = [[4, 4, 4, 5],
                [0, 1, 2, 2]]
    borders =  [[[2, 3], [0, 1, 2], [3, 0], [3, 1, 0]],
                [[0, 1, 3], [2, 3], [0, 1, 2], [3, 0]],
                [[0, 1, 2], [0, 3], [3, 1, 0], [2, 3]]]
    orientation = 0

    def __init__(self):
        self.position = [[4, 4, 4, 5],
                         [0, 1, 2, 2]]

class Lewis():
    deltas =   [[[ 2, -1,  0,  1], [-1,  0, -1, -2], [1, 0]], 
                [[-1,  0, -1, -2], [-1,  2,  1,  0], [0, 1]],
                [[-1,  2,  1,  0], [ 0, -1,  0,  1], [-1, 0]],
                [[ 0, -1,  0,  1], [ 2, -1,  0,  1], [0, 1]]]   
    position = [[4, 5, 5, 5], 
                [2, 0, 1, 2]]
    borders =  [[[0, 3], [1, 2, 0], [1, 0], [3, 2, 1]],
                [[1, 2, 3], [3, 0], [0, 2, 1], [0, 1]],
                [[0, 1, 2], [1, 0], [3, 2, 1], [0, 3]]]
    orientation = 0

    def __init__(self):
        self.position = [[4, 5, 5, 5], 
                         [2, 0, 1, 2]]

class TJ():
    deltas =   [[[-1,  1,  0, -1], [ 1,  1,  0, -1], [0, 1]],
                [[ 1,  1,  0, -1], [ 0, -2, -1,  0], [1, 0]],
                [[ 0, -2, -1,  0], [ 0,  0,  1,  2], [0, 1]],
                [[ 0,  0,  1,  2], [-1,  1,  0, -1], [1, 0]]]
    position = [[4, 3, 4, 5],
                [0, 1, 1, 1]]
    borders =  [[[1, 2, 3], [0, 1], [3, 0, 1], [3, 0]], 
                [[0, 3], [3, 2, 1], [1, 0], [1, 0, 3]],
                [[0, 1], [0, 1, 3], [3, 0], [1, 2, 3]]]
    orientation = 0

    def __init__(self):
        self.position = [[4, 3, 4, 5],
                         [0, 1, 1, 1]]

class Igor():
    deltas =   [[[0, -1, -2, -3], [0,  1,  2,  3], [0, 3]],
                [[0,  1,  2,  3], [0, -1, -2, -3], [3, 0]]]
    position = [[3, 4, 5, 6],
                [0, 0, 0, 0]]
    borders =  [[[0, 1, 2, 3], [3]],
                [[3], [0, 1, 2, 3]],
                [[0], [0, 1, 2, 3]]]
    orientation = 0

    def __init__(self):
        self.position = [[3, 4, 5, 6],
                         [0, 0, 0, 0]]

class Bob():
    deltas =   [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0]]]
    position = [[4, 5, 4, 5],
                [0, 0, 1, 1]]
    borders =  [[[2, 3]],
                [[1, 3]],
                [[0, 2]]]
    orientation = 0

    def __init__(self):
        self.position = [[4, 5, 4, 5],
                         [0, 0, 1, 1]]
