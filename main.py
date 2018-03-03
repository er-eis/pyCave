from grid import gridbuild
from grid import tools
from grid import movement
from messages import strings
from os import system

while (True):
    ## COMMENT OUT FOR DEBUG, SEE generateGrid IN gribuild.py
    system('cls')
    ## COMMENT OUT FOR DEBUG, SEE generateGrid IN gribuild.py
    print('Welcome to pyCave! Find the cursed treasure inside the cave and avoid the pits.')
    print('Make selections by typing the associated number and pressing Enter.')
    print('Enter your difficulty:\n1-Easy\n2-Medium\n3-Hard\n4-Very Hard')
    difficulty = int(movement.prompt(strings.difficulties()))
    print('Enter the cave size:\n1-Small\n2-Medium\n3-Large\n4-Huge')
    length = int(movement.prompt(strings.caveSizes())) + 4

    grid = gridbuild.generateGrid(length, difficulty)
    coords = gridbuild.findPlayerPosition(grid)
    x = coords.get('x')
    y = coords.get('y')
    grid[y][x] = ''

    ## COMMENT OUT FOR DEBUG, SEE generateGrid IN gribuild.py
    system('cls')
    ## COMMENT OUT FOR DEBUG, SEE generateGrid IN gribuild.py
    print('You awake inside a pitch-black cave, but are aware of cardinal directions...')
    dead = False
    while(not dead):
        ## FOR DEBUG PURPOSES
        ## Will show current game state
        #tools.debugShowState(grid, x, y)

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
    
    quit = False
    while(True):
        newgame = input('The game is over! Would you like to play again?\n1-Yes\n2-No\n')
        if(newgame == '1'):
            break
        if(newgame == '2'):
            quit = True
            break
        else:
            print('Please make a valid selection (either 1 or 2)')
    if (quit):
        break
