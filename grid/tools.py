import random as ran
from . import strings


def xyTuple(xmax, ymax):
    return {'x': ran.randint(0, xmax - 1),
            'y': ran.randint(0, ymax - 1)}

def findStreamEnd(grid, x, y, stream):
    length = len(grid)
    for i in range(length):
        for j in range(length):
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