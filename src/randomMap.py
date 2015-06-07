import random

GRID_SIZE = 14
MAX_BOMB = 20
       
def RandomMap():

    grid = [[0 for x in range(GRID_SIZE)] for x in range(GRID_SIZE)]

    for i in range(GRID_SIZE):  ## set edges of map to -2, representing walls
        grid[i][0] = -2
        grid[0][i] = -2
        grid[i][GRID_SIZE - 1] = -2
        grid[GRID_SIZE - 1][i] = -2
        
    start = random.randint(1, GRID_SIZE - 2)
    grid[GRID_SIZE - 1][start] = -3                      ## start is -3
    
    finish = random.randint(1, GRID_SIZE - 2)
    grid[0][finish] = -4                                 ## finish is -4


    for j in range(MAX_BOMB):
        bomb_y = random.randint(1, GRID_SIZE - 2)
        bomb_x = random.randint(1, GRID_SIZE - 2)
        if grid[bomb_y + 1][bomb_x] >= 0 and grid[bomb_y - 1][bomb_x] >= 0 and grid[bomb_y][bomb_x] != -1:  ## mines are -1
            grid[bomb_y][bomb_x] = -1

    return grid
