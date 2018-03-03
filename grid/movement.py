from . import tools
from os import system


def prompt(selections):
    while(True):
        selection = input('Which will you select?\n')
        if(selection in selections):
            break
        else:
            print('Please enter a valid selection (either: ' + 
                  ', '.join(selections) + ').')
    return selection

def performMove(grid, x, y, selection):
    desiredmove = move(grid, x, y, selection)
    if (desiredmove == 'P' or desiredmove == 'T'):
        newlocation = {'x': -1,
                       'y': -1}
    elif (desiredmove != 'S'):
        newlocation = validMove(grid, x, y, selection, desiredmove)
    else:
        newlocation = {'x': x,
                       'y': y}
    message = tileMessage(desiredmove) + cardinalMessage(selection)
    print(message)
    return newlocation

def move(grid, x, y, selection): # player's current x,y coordinates
    if(selection == '1'):
        if(y == 0):
            return 'S'
        else:
            return grid[y-1][x]
    if(selection == '2'):
        if(x == len(grid) - 1):
            return 'S'
        else:
            return grid[y][x+1]
    if(selection == '3'):
        if(y == len(grid) - 1):
            return 'S'
        else:
            return grid[y+1][x]
    if(selection == '4'):
        if(x == 0):
            return 'S'
        return grid[y][x-1]
    return grid[y][x]

def validMove(grid, x, y, selection, desiredmove):
    if (selection == '5'):       
        newlocation = tools.findStreamEnd(grid, x, y, desiredmove)
    else:
        newlocation = moveOpen(x, y, selection)  
    return newlocation

def moveOpen(x, y, selection):
    if(selection == '1'):
        newlocation = {'x': x,
                       'y': y-1}
    elif(selection == '2'):
        newlocation = {'x': x+1,
                       'y': y}
    elif(selection == '3'):
        newlocation = {'x': x,
                       'y': y+1}
    else:
        newlocation = {'x': x-1,
                       'y': y}
    return newlocation

#tile types: open (''), pit ('P'), stream ('1', '2', etc), treasure ('T'), stone ('S')
def tileMessage(char):
    if (char == 'S'):
        return 'You hit a stone wall which blocks your path as you attempt to move '
    if (char == ''):
        return 'You move '
    if (char == 'P'):
        return 'You fall into a pit as you move '
    if (char == 'T'):
        return 'You find the treasure as you move '
    return 'You feel the rush of a stream as you move '

def surroundingMessage(char):
    if (char == 'S' or char == ''):
        return
    if (char == 'P'):
        return 'You hear an echo coming from the ground.'
    if (char == 'T'):
        return 'Your room is illuminated with a faint golden hue.'
    return 'You hear the sounds of rushing water.'

def cardinalMessage(selection):
    if (selection == '1'):
        return 'to the North.'
    if (selection == '2'):
        return 'to the East.'
    if (selection == '3'):
        return 'to the South.'
    if (selection == '4'):
        return 'to the West.'
    else:
        return 'into the water\'s path, following its direction.'

def printMovements(movements):
    if (len(movements) == 4):
        print('Move in a direction:\n1-North\n2-East\n3-South\n4-West')
    else:
        print('Move in a direction:\n1-North\n2-East\n3-South\n4-West\n5-Follow the stream')

def printSurroundings(grid, x, y):
    messageorder = tools.randomArray(4)
    
    for i in range(len(messageorder)):
        if (surroundingMessage(move(grid, x, y, str(messageorder[i]))) is not None):
            print(surroundingMessage(move(grid, x, y, str(messageorder[i]))))
    if(grid[y][x] != ''):
        print('You feel water rushing past you where you stand.')

def movementOptions(grid, x, y):
    if (grid[y][x] == ''):
        return ['1',
                '2',
                '3',
                '4']
    return ['1',
            '2',
            '3',
            '4',
            '5']