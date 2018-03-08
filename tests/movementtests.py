import os, sys
sys.path.append(os.getcwd())

import numpy
from grid import movement

## TEST GRID
## 1	S	''
## P	U	''
## ''	T	1
grid = numpy.zeros((3, 3), str)
grid[0][1] = 'S'
grid[1][0] = 'P'
grid[2][1] = 'T'
grid[2][2] = '1'
grid[0][0] = '1'
x = 1
y = 1


def testMoveToStoneValidation():
    coords = movement.performMove(grid, x, y, '1')
    assert(coords.get('x')) == 1
    assert(coords.get('y')) == 1
def testMoveToOpenValidation():
    coords = movement.performMove(grid, x, y, '2')
    assert(coords.get('x')) == 2
    assert(coords.get('y')) == 1
def testMoveToTreasureValidation():
    coords = movement.performMove(grid, x, y, '3')
    assert(coords.get('x')) == -1
    assert(coords.get('y')) == -1
def testMoveToPitValidation():
    coords = movement.performMove(grid, x, y, '4')
    assert(coords.get('x')) == -1
    assert(coords.get('y')) == -1
def testMoveToStreamValidation():
    x = 2
    coords = movement.performMove(grid, x, y, '3')
    assert(coords.get('x')) == 2
    assert(coords.get('y')) == 2
def testTakeStreamPathValidation():
    x = 2
    y = 2
    coords = movement.performMove(grid, x, y, '5')
    assert(coords.get('x')) == 0
    assert(coords.get('y')) == 0
