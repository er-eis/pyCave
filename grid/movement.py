from . import tools
from messages import strings


def prompt(selections):
    while(True):
        selection = input(strings.selectionprompt)
        if(selection in selections):
            break
        else:
            print(strings.makevalidselection +
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
        return strings.moveintostone
    if (char == ''):
        return strings.moveintoempty
    if (char == 'P'):
        return strings.moveintopit
    if (char == 'T'):
        return strings.moveintotreasure
    return strings.moveintostream

def surroundingMessage(char):
    if (char == 'S' or char == ''):
        return
    if (char == 'P'):
        return strings.surroundingpit
    if (char == 'T'):
        return strings.surroundingtreasure
    return strings.surroundingstream

def cardinalMessage(selection):
    if (selection == '1'):
        return strings.cardinalnorth
    if (selection == '2'):
        return strings.cardinaleast
    if (selection == '3'):
        return strings.cardinalsouth
    if (selection == '4'):
        return strings.cardinalwest
    return strings.cardinalstream

def printMovements(movements):
    if (len(movements) == 4):
        print(strings.makemoveselectionnormal)
    else:
        print(strings.makemoveselectionwithstream)

def printSurroundings(grid, x, y):
    messageorder = tools.randomArray(4)
    for i, _ in enumerate(messageorder):
        if (surroundingMessage(move(grid, x, y, str(messageorder[i]))) is not None):
            print(surroundingMessage(move(grid, x, y, str(messageorder[i]))))
    if(grid[y][x] != ''):
        print(strings.wateronuser)

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