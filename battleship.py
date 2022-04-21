"""
1. 10 x 10 grid will have 5 ships of different length randomly place on the grid.
2. The player will have 40 rockets to take the ships down.
3. The player can choose a row and a column (like chess, A7) to indicate where to shoot.
4. For every shot that hits or misses it will show on the grid.
5. A ship can only be placed horizontally or vertically, so if a shot hits the rest of the ship is in either of the 4 directions: left, right, up, and down.
6. If all ships are hit before using up all the bullets, the player wins, else, the player loses.

Keys:
'.' = empty space/water
'0' = part of ship that wasn't hit
'x' = part of ship that was hit
'#' = water that was shot, but no ship
"""

GRID = [[]]
GRID_SIZE = 10
NUM_OF_SHIPS = 10
TOTAL_BULLETS = 40
NUM_OF_SUNKED_SHIPS = 0
ALPHABET = 'ABCDEFGHIJ'


def create_board():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(GRID, end = '')
        print()


def check_grid_to_place_ship():
    '''
    Check if the grid is available to place the given size of ship.

    Return: True or false
    '''
    pass


def main():
    create_board()

if __name__ == '__main__':
    main()
