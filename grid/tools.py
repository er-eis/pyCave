import os, sys
sys.path.append(os.getcwd())

import random as ran
from messages import strings


def xyTuple(xmax, ymax):
    return {'x': ran.randint(0, xmax - 1),
            'y': ran.randint(0, ymax - 1)}

def findStreamEnd(grid, x, y, stream):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == stream and not (y == i and x == j)):
                return {'x': j,
                        'y': i}
    print('findStreamEnd failed')

def randomArray(size):
    array = []
    while (len(array) < size):
        randomint = ran.randint(1, size)
        if (randomint not in array):
            array.append(randomint)
    return array

def debugShowState(grid, x, y):
    originaltile = grid[y][x]
    grid[y][x] = 'U'
    print(strings.debugmessage)
    print(grid)
    grid[y][x] = originaltile