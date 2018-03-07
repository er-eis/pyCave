************
Introduction
************
**pyCave** is an open-source, text-based adventure game where players must find a cursed treasure in a cave. Pits within the cave must be avoided! All code written in this repository is under the MIT License, but the licenses of imported libraries (such as Numpy) may be different.

**********
Game Rules
**********
The player occupies one tile on an ``NxN`` grid (if debug mode is turned on, the player will appear as a ``'U'`` tile). Here is a display of a game board:

.. image:: https://i.imgur.com/89fxgTL.png

The game board is not displayed visually during play, but instead described to the player by text statements. These text statements will tell the player clues about what is happening in the tiles directly above, to the right, beneath, and to the left of the player's current position. The order of these text statements are randomized each time so the player can't easily deduce where and what each tile is. The player must use logical deduction to conclude where tiles are based on these messages.

Board Tiles
------------------
The grid is composed of several tile types:

- ``''`` => Open
- ``'T'`` => Treasure
- ``'P'`` => Pit
- ``'1'``, ``'2'``, ``'3'``, etc => Stream
- ``'S'`` => Stone

The player's goal is to move onto the Treasure tile, which will cause them to win the game. There will be only one Treasure tile per map. The player will lose the game once they have moved onto a Pit tile. Stone tiles will prevent any movement onto them. Open tiles will allow movement onto them.

Stream tiles are represented by sequential numbers on the board starting at 1. For any given Stream tile, there will be an additional Stream tile with the same number. Stream tiles will act as an Open tile with the additional option of following the stream, thus transporting the player to the other Stream tile with the same number. Thus, if a user is standing at Stream tile ``'1'`` at position (0,0) and the other ``'1'`` tile is at position (2,1), they would be transported to position (2,1) if they chose to follow the stream.

Movement
------------------
The player's basic movements are up, right, down, and left on the board (represented by North, East, South, and West respectively). An additional option of following a Stream will be present when the player is standing on a Stream tile. Movements are made by typing the integer representing the desired move and pressing Enter.

******************
Launching The Game
******************
Run `main.py` within the parent folder of the project with python.

**********************
Procedural Generation
**********************
Each game board is procedurally generated using the difficulty and map size entered by the user. More non-Open tiles will be present at higher difficulties. Each game board is validated through a recursive, depth-first searching algorithm, along with other algorithms, after generation to ensure the following qualities:

- The game is winnable using valid moves
- The player does not spawn to the left, to the right, above, or beneath a Pit or Treasure tile

This process can be observed by navigating to the ``validateGrid()`` function within **gridbuild.py**.

***************
Debug Mode
***************
Debug mode can be enabled by setting the variable ``DEBUG`` to True within **config.py**.

Debug mode will display the game board at each game step and how many generations of the map failed before a valid map was created.

*******************
Running Test Cases
*******************
Test cases (assuming ``nose`` has been installed with pip) can be run by entering ``nosetests [filepath]`` where ``[filepath]`` is directed to one of the tests.py files (such as **gridbuildtests.py**).

***************
Installation
***************
`setup.py` will install `grid`, which contains functions and procedures for generating a **pyCave** game board and manipulating it (this is not the recommended way of interacting with the game).

****************************************
Bug Reports and Suggestions
****************************************
Feel free to submit all bugs and suggestions.