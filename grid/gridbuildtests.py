import numpy
from . import gridbuild
import nose.tools


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

def testGenerateGridEveryOptionSuccessValidation():
    for i in range(4):
        for j in range(4):
            assert(type(gridbuild.generateGrid(i + 5, j))) == type(numpy.zeros((1,1), str))