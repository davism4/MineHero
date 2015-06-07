import pygame
import constants as con
import tile
import resources as res

def run(grid_data = None):
    screen = res.screen
    tilesize = con.TILE_WIDTH
    
    clock = pygame.time.Clock()

    # Initialize the grid
    board = tile.Board(con.GRID_SIZE, con.GRID_SIZE)

    # TODO: Read grid data (2D-array), parse into tiles
    for i in range(con.GRID_SIZE):
        board.getTile(i,0).setTileType(con.TYPE_WALL)
        board.getTile(i,con.GRID_SIZE-1).setTileType(con.TYPE_WALL)
        board.getTile(0,i).setTileType(con.TYPE_WALL)
        board.getTile(con.GRID_SIZE-1,i).setTileType(con.TYPE_WALL)

    for x in range(con.GRID_SIZE):
        for y in range(con.GRID_SIZE):
            t = board.getTile(x,y)
            if (t.getTileType()==con.TYPE_WALL):
                t.setImages(res.sanic)
                #screen.blit(t.getImage(),pygame.Rect(x*tilesize, y*tilesize, tilesize, tilesize))

    
    board.getTile(5, 5).setTileType(con.TYPE_BOMB_ACTIVE)
    board.getTile(3, 3).setTileType(con.TYPE_BOMB_ACTIVE)

    # Player variables
    health = con.MAX_HEALTH
    direction = con.STAY # used for animation
    pos_x = 1
    pos_y = (con.GRID_SIZE-1)
    dest_x = pos_x
    dest_y = pos_y
    draw_x = pos_x*tilesize
    draw_y = pos_y*tilesize

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
                if (draw_y > dest_y*tilesize):
                    draw_y -= con.MOVE_SPEED
                else:
                    draw_y = dest_y*tilesize
                    walking = False
            elif (direction == con.SOUTH):
                if (draw_y < dest_y*tilesize):
                    draw_y += con.MOVE_SPEED
                else:
                    draw_y = dest_y*tilesize
                    walking = False
            elif (direction == con.EAST):
                if (draw_x < dest_x*tilesize):
                    draw_x += con.MOVE_SPEED
                else:
                    draw_x = dest_x*tilesize
                    walking = False
            elif (direction == con.WEST):
                if (draw_x > dest_x*tilesize):
                    draw_x -= con.MOVE_SPEED
                else:
                    draw_x = dest_x*tilesize
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
                    print("destination: "+`dest_x`+' , '+`dest_y` + ' type: ' + `board.getTile(dest_x,dest_y).getTileType()`)
                    if can_move(dest_x,dest_y):
                        if (board.getTile(dest_x,dest_y).getTileType() == con.TYPE_BOMB_ACTIVE):
                            health -= 1
                            (board.getTile(dest_x,dest_y)).setTileType(con.TYPE_BOMB_INACTIVE)
                        else:
                            pos_x = dest_x
                            pos_y = dest_y
                            walking = True

        pygame.event.clear()

        screen.fill(con.WHITE)
        #image = pygame.Surface((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
        
        # Tiles are mainly static
        for y in range(0, con.GRID_SIZE):
            for x in range(0, con.GRID_SIZE):
                t = board.getTile(x,y)
                if (t.getTileType()==con.TYPE_BOMB_ACTIVE):
                    pygame.draw.rect(screen, con.RED, (x*tilesize, y*tilesize, tilesize, tilesize))
                elif (t.getTileType()==con.TYPE_BOMB_INACTIVE):
                    pygame.draw.rect(screen, con.GRAY, (x*tilesize, y*tilesize, tilesize, tilesize))

                elif (t.getTileType()==con.TYPE_WALL):
                    screen.blit(t.getSprite().get(), t.getSprite().rect(x*tilesize, y*tilesize))

        pygame.draw.rect(screen, con.GREEN, (draw_x, draw_y, tilesize, tilesize))
        

        for h in range(0, health):
            pygame.draw.rect(screen, con.RED, (hp_x + h*15, hp_y, 10, 10))

        #screen.blit(image, pygame.Rect(0, 0, con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    #    healthLabel = myfont.render('health: '+`health`,1,white)
    #    screen.blit(healthLabel, (hp_x, hp_y))
        
         # clear before rendering graphics
        #pygame.event.clear()
        
        clock.tick(1/con.FRAMES_PER_SECOND)
        pygame.display.update()
        
    return
    
