import pygame
import constants as con
import tile

def run():
    screen = con.screen
    
    clock = pygame.time.Clock()

    # Initialize the grid
    board = tile.Board(con.GRID_SIZE, con.GRID_SIZE)
    board.createBoard()
    board.getTile(5, 5).setTileType(con.TYPE_BOMB_ACTIVE)
    board.getTile(3, 3).setTileType(con.TYPE_BOMB_ACTIVE)

    # Player variables
    health = con.MAX_HEALTH
    direction = con.STAY # used for animation
    pos_x = 1
    pos_y = (con.GRID_SIZE-1)
    dest_x = pos_x
    dest_y = pos_y
    draw_x = pos_x*con.TILE_WIDTH
    draw_y = pos_y*con.TILE_WIDTH

    hp_x = int(round(con.HEALTH_X*con.SCREEN_WIDTH))
    hp_y = int(round(con.HEALTH_Y*con.SCREEN_HEIGHT))
    #print(`hp_x` + ' , ' + `hp_y`)
    #print(`con.SCREEN_WIDTH` + ' , ' + `con.SCREEN_HEIGHT`)

    #myfont = pygame.font.SysFont("monospace",15)


    ####################################################
    # Main Code
    ####################################################

    def can_move(x, y):
        if (x >= con.GRID_SIZE or x <= 0):
            return False
        elif (y >= con.GRID_SIZE or y <= 0):
            return False
        elif (board.getTile(x,y).getTileType()==con.TYPE_WALL):# or grid[x][y] == con.TYPE_BOMB_ACTIVE):
            return False
        else:
            return True

    gameExit = False
    pygame.display.update()
    walking = False

    # BEGIN MAIN LOOP
    while (not gameExit):
        if (walking):
            if (direction == con.NORTH):
                if (draw_y > dest_y*con.TILE_WIDTH):
                    draw_y -= con.MOVE_SPEED
                else:
                    draw_y = dest_y*con.TILE_WIDTH
                    walking = False
            elif (direction == con.SOUTH):
                if (draw_y < dest_y*con.TILE_WIDTH):
                    draw_y += con.MOVE_SPEED
                else:
                    draw_y = dest_y*con.TILE_WIDTH
                    walking = False
            elif (direction == con.EAST):
                if (draw_x < dest_x*con.TILE_WIDTH):
                    draw_x += con.MOVE_SPEED
                else:
                    draw_x = dest_x*con.TILE_WIDTH
                    walking = False
            elif (direction == con.WEST):
                if (draw_x > dest_x*con.TILE_WIDTH):
                    draw_x -= con.MOVE_SPEED
                else:
                    draw_x = dest_x*con.TILE_WIDTH
                    walking = False
        
        # not walking --> accept input
        dest_x = pos_x
        dest_y = pos_y
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameExit = True
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    gameExit = True

                #Only register movement input when NOT animating player
                elif (not walking):
                    if (event.key == pygame.K_LEFT):
                        direction = con.WEST
                        dest_x = pos_x - 1
                    elif (event.key == pygame.K_RIGHT):
                        direction = con.EAST
                        dest_x = pos_x + 1
                    elif (event.key == pygame.K_UP):
                        direction = con.NORTH
                        dest_y = pos_y - 1
                    elif (event.key == pygame.K_DOWN):
                        direction = con.SOUTH
                        dest_y = pos_y + 1
                    #print("destination: "+`dest_x`+' , '+`dest_y`)
                    if can_move(dest_x,dest_y):
                        if (board.getTile(x,y).getTileType() == con.TYPE_BOMB_ACTIVE):
                            health -= 1
                            board.getTile(x,y).setTileType(con.TYPE_BOMB_INACTIVE)
                        else:
                            pos_x = dest_x
                            pos_y = dest_y
                            walking = True

        pygame.event.clear()

        screen.fill(con.WHITE)
        # Tiles are mainly static
        for y in range(0, con.GRID_SIZE):
            for x in range(0, con.GRID_SIZE):
                if (board.getTile(x,y).getTileType()==con.TYPE_BOMB_ACTIVE):
                    pygame.draw.rect(screen, con.RED, (x*con.TILE_WIDTH, y*con.TILE_WIDTH, con.TILE_WIDTH, con.TILE_WIDTH))
                
		elif (board.getTile(x,y).getTileType()==con.TYPE_BOMB_INACTIVE):
                    pygame.draw.rect(screen, con.GRAY, (x*con.TILE_WIDTH, y*con.TILE_WIDTH, con.TILE_WIDTH, con.TILE_WIDTH))

                elif (board.getTile(x,y).getTileType()==con.TYPE_WALL):
                    pygame.draw.rect(screen, con.BLACK, (x*con.TILE_WIDTH, y*con.TILE_WIDTH, con.TILE_WIDTH, con.TILE_WIDTH))

        pygame.draw.rect(screen, con.GREEN, (draw_x, draw_y, con.TILE_WIDTH, con.TILE_WIDTH))
                  

        for h in range(0, health):
            pygame.draw.rect(screen, con.RED, (hp_x + h*15, hp_y, 10, 10))

        
    #    healthLabel = myfont.render('health: '+`health`,1,white)
    #    screen.blit(healthLabel, (hp_x, hp_y))
        
         # clear before rendering graphics
        #pygame.event.clear()
        
        clock.tick(1/con.FRAMES_PER_SECOND)
        pygame.display.update()
        
    return
    
