from grid import gridbuild
from grid import movement
from grid import tools
from grid import strings
from messages import options
from os import system
import config

while (True):
    if (config.DEBUG == False):
        system('cls')
    print(strings.gamestart)
    difficulty = int(movement.prompt(options.difficulties()))
    print(strings.cavesizes)
    length = int(movement.prompt(options.caveSizes())) + 4

    grid = gridbuild.generateGrid(length, difficulty)
    coords = gridbuild.findPlayerPosition(grid)
    x = coords.get('x')
    y = coords.get('y')
    grid[y][x] = ''

    if (config.DEBUG == False):
        system('cls')
    print(strings.caveawake)
    dead = False
    while(not dead):
        if (config.DEBUG == True):
            tools.debugShowState(grid, x, y)

        movement.printSurroundings(grid, x, y)
        movementoptions = movement.movementOptions(grid, x, y)
        movement.printMovements(movementoptions)
        selection = movement.prompt(movementoptions)
        system('cls')
        newlocation = movement.performMove(grid, x, y, selection)
        x = newlocation.get('x')
        y = newlocation.get('y')
        if (x == -1 and y == -1):
            dead = True

    wantquit = False
    while(True):
        newgame = input(strings.gameover)
        if(newgame == '1'):
            break
        if(newgame == '2'):
            wantquit = True
            break
        else:
            print(strings.gameoverselection)
    if (wantquit):
        break