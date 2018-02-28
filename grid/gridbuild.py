from . import tools
import numpy
import math


def generateGrid(length, difficulty):
    ## FOR DEBUG PURPOSES
    numberfailed = 0

    while (True):
        grid = numpy.zeros((length, length), str)

        fillGrid(grid, difficulty)
        if (validateGrid(grid)):
            ## FOR DEBUG PURPOSES
            ## To see this statement, comment the system('cls') lines in main.py
            print('Number of failed map generations: ' + str(numberfailed))
            return grid
        else:
            numberfailed += 1

#adds tiles to the grid
#tile types: open (''), pit ('P'), stream ('1', '2', etc), treasure ('T'), stone ('S'), player ('U')
def fillGrid(grid, difficulty):
    length = len(grid)
    stones = length
    pits = math.ceil((length ** 2) / 10.0) + difficulty
    streams = difficulty * 2

    placeTiles(grid, stones, 'S')
    placeTiles(grid, pits, 'P')
    placeTiles(grid, streams, '1')
    placeTiles(grid, 1, 'T')
    placeTiles(grid, 1, 'U')
    return grid

def placeTiles(grid, number, ch):
    length = len(grid)
    
    if (ch == '1'):
        while(number):
            coords = tools.xyTuple(length, length)
            x = coords.get('x')
            y = coords.get('y')

            if (grid[y][x] == ''):
                grid[y][x] = math.ceil(number / 2.0)
                number -= 1
    else:
        while(number):
            coords = tools.xyTuple(length, length)
            x = coords.get('x')
            y = coords.get('y')

            if (grid[y][x] == ''):
                grid[y][x] = ch
                number -= 1
    return grid

def validateGrid(grid):
    coords = findPlayerPosition(grid)
    x = coords.get('x')
    y = coords.get('y')
    explored = []
    unexplored = []

    return validateGridHelper(grid, x, y, explored, unexplored)

# recursive depth-first search of treasure from starting position
def validateGridHelper(grid, x, y, explored, unexplored):
    length = len(grid)
    currenttile = grid[y][x]
    if (currenttile == 'T'):
        return True
    if (currenttile != 'S' and currenttile != 'P'):
        if (y != 0):
            north = {'y': y-1, 'x': x}
            if (north not in explored and 
                north not in unexplored):
                unexplored.append(north)
        if (x != length - 1):
            east = {'y': y, 'x': x+1}
            if (east not in explored and
                east not in unexplored):
                unexplored.append(east)
        if (y != length - 1):
            south = {'y': y+1, 'x': x}
            if (south not in explored and
                south not in unexplored):
                unexplored.append(south)
        if (x != 0):
            west = {'y': y, 'x': x-1}
            if (west not in explored and
                west not in unexplored):
                unexplored.append(west)
        if (currenttile != '' and currenttile != 'U'):
            streamend = tools.findStreamEnd(grid, x, y, currenttile)
            if (streamend not in explored and
                streamend not in unexplored):
                unexplored.append(streamend)

    explored.append({'y': y, 'x': x})
    if (len(unexplored) != 0):
        next = unexplored.pop()
        return (False or validateGridHelper(grid, next.get('x'), next.get('y'), explored, unexplored))
    return False

def findPlayerPosition(grid):
    length = len(grid)

    for i in range(length):
        for j in range(length):
            if (grid[i][j] == 'U'):
                return {'y': i, 'x': j}