import os, sys
sys.path.append(os.getcwd())

import numpy
from grid import gridbuild


def testGridUserStoneTrappedFailValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'U'
    grid[0][1] = 'S'
    grid[1][0] = 'S'
    grid[1][1] = 'T'
    assert(gridbuild.validateGrid(grid)) == False

def testGridUserPitTrappedFailValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'U'
    grid[0][1] = 'P'
    grid[1][0] = 'P'
    grid[1][1] = 'T'
    assert(gridbuild.validateGrid(grid)) == False

def testGridTreasurePitTrappedFailValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'T'
    grid[0][1] = 'P'
    grid[1][0] = 'P'
    grid[1][1] = 'U'
    assert(gridbuild.validateGrid(grid)) == False

def testGridTreasureStoneTrappedFailValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'T'
    grid[0][1] = 'S'
    grid[1][0] = 'S'
    grid[1][1] = 'U'
    assert(gridbuild.validateGrid(grid)) == False

def testGridSuccessValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'U'
    grid[0][1] = 'S'
    grid[1][1] = 'S'
    grid[2][2] = 'T'
    assert(gridbuild.validateGrid(grid)) == True

def testGridTreasureTrappedWithoutStreamFailValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'T'
    grid[0][2] = 'S'
    grid[1][0] = 'S'
    grid[1][1] = 'S'
    grid[2][2] = 'U'
    assert(gridbuild.validateGrid(grid)) == False

def testGridTreasureTrappedWithStreamSuccessValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'T'
    grid[0][2] = 'S'
    grid[1][0] = 'S'
    grid[1][1] = 'S'
    grid[2][2] = 'U'
    grid[0][1] = '1'
    grid[2][1] = '1'
    assert(gridbuild.validateGrid(grid)) == True

def testGridUserTrappedWithoutStreamFailValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'U'
    grid[0][2] = 'S'
    grid[1][0] = 'S'
    grid[1][1] = 'S'
    grid[2][2] = 'T'
    assert(gridbuild.validateGrid(grid)) == False

def testGridUserTrappedWithStreamSuccessValidation():
    grid = numpy.zeros((3, 3), str)
    grid[0][0] = 'U'
    grid[0][2] = 'S'
    grid[1][0] = 'S'
    grid[1][1] = 'S'
    grid[2][2] = 'T'
    grid[0][1] = '1'
    grid[2][1] = '1'
    assert(gridbuild.validateGrid(grid)) == True

def testGridUserAdjacentToEndStateFailValidation():
    grid = numpy.zeros((3, 3), str)
    grid[1][1] = 'U'
    grid[0][1] = 'T'
    assert(gridbuild.validateGrid(grid)) == False
    grid[0][1] = 'P'
    assert(gridbuild.validateGrid(grid)) == False

def testGenerateGridEveryOptionSuccessValidation():
    for i in range(4):
        for j in range(4):
            assert(type(gridbuild.generateGrid(i + 5, j))) == type(numpy.zeros((1,1), str))

def testFillGridWithTilesOfEveryTypeSuccessValidation():
    for i in range(100):
        grid = numpy.zeros((4, 4), str)
        grid = gridbuild.fillGrid(grid, 1)
        grid = numpy.reshape(grid,(1, 16))[0] # flatten the array
        grid = numpy.sort(grid) # sort it so expected chars are always in same position
        assert(grid[15] == 'U') == True, '%s has an unknown char where there should be a \'U\'!' % str(grid)
        assert(grid[14] == 'T') == True, '%s has an unknown char where there should be a \'T\'!' % str(grid)
        assert(grid[13] == 'S') == True, '%s has an unknown char where there should be a \'S\'!' % str(grid)
        assert(grid[9] == 'P') == True, '%s has an unknown char where there should be a \'P\'!' % str(grid)
        assert(grid[6] == '1') == True, '%s has an unknown char where there should be a \'1\'!' % str(grid)
        assert(grid[4] == '') == True, '%s has an unknown char where there should be a \'\'!' % str(grid)

# placeTiles, validateGridHelper, findPlayerPosition to be added