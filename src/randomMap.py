import random
import constants as con

#GRID_SIZE = 14
#MAX_BOMB = 20
       
def RandomMap():

    grid = [[0 for x in range(con.GRID_SIZE)] for x in range(con.GRID_SIZE)]

    for i in range(con.GRID_SIZE):  ## set edges of map to -2, representing walls
        grid[i][0] = con.TYPE_WALL
        grid[0][i] = con.TYPE_WALL
        grid[i][con.GRID_SIZE - 1] = con.TYPE_WALL
        grid[con.GRID_SIZE - 1][i] = con.TYPE_WALL
        
    start = random.randint(1, con.GRID_SIZE - 2)
    grid[con.GRID_SIZE - 1][start] = con.TYPE_START                   ## start is -3
    
    finish = random.randint(1, con.GRID_SIZE - 2)
    grid[0][finish] = con.TYPE_EXIT                                 ## finish is -4


    for j in range(con.MAX_BOMBS):
        bomb_y = random.randint(1, con.GRID_SIZE - 2)
        bomb_x = random.randint(1, con.GRID_SIZE - 2)
        if grid[bomb_y + 1][bomb_x] >= 0 and grid[bomb_y - 1][bomb_x] >= 0 and grid[bomb_y][bomb_x] != -1:  ## mines are -1
            grid[bomb_y][bomb_x] = con.TYPE_BOMB_ACTIVE

    return grid
