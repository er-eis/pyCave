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
    if(x == 0):  # '4' was selected
        return 'S'
    return grid[y][x-1]

def validMove(grid, x, y, selection, desiredmove):
    if (desiredmove == ''):
        newlocation = moveOpen(x, y, selection)
    else:
        templocation = moveOpen(x, y, selection)
        x = templocation.get('x')
        y = templocation.get('y')
        newlocation = tools.findStreamEnd(grid, x, y, desiredmove)
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
        return 'You hit a stone wall as you attempt to move to the '
    if (char == ''):
        return 'You move to the '
    if (char == 'P'):
        return 'You fall into a pit as you move to the '
    if (char == 'T'):
        return 'You find the treasure as you move to the '
    return 'You feel the rush of a stream as you move to the '

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
        return 'North.'
    if (selection == '2'):
        return 'East.'
    if (selection == '3'):
        return 'South.'
    return 'West.'

def printMovements():
    print('Move in a direction:\n1-North\n2-East\n3-South\n4-West')

def printSurroundings(grid, x, y):
    messageorder = tools.randomArray(4)
    
    for i in range(len(messageorder)):
        if (surroundingMessage(move(grid, x, y, str(messageorder[i]))) is not None):
            print(surroundingMessage(move(grid, x, y, str(messageorder[i]))))