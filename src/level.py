import pygame, tiling, sprites
import constants as con, resources as res
import os
import randomMap
import time

def run(grid_data = None):
    screen = res.screen
    tilesize = con.TILE_WIDTH
    player = sprites.JonesSprite()
    
    clock = pygame.time.Clock()

    # Initialize the grid
    board = tiling.Board(con.GRID_SIZE, con.GRID_SIZE)

    # TODO: Read grid data (2D-array), parse into tiles
##    for i in range(con.GRID_SIZE):
##        board.tileAt(i,0).setValue(con.TYPE_WALL)
##        board.tileAt(i,con.GRID_SIZE-1).setValue(con.TYPE_WALL)
##        board.tileAt(0,i).setValue(con.TYPE_WALL)
##        board.tileAt(con.GRID_SIZE-1,i).setValue(con.TYPE_WALL)
##    
##    board.tileAt(5, 5).setValue(con.TYPE_BOMB_ACTIVE)
##    board.tileAt(3, 3).setValue(con.TYPE_BOMB_ACTIVE)
    grid = randomMap.RandomMap()    
    pos_x = 1
    pos_y = (con.GRID_SIZE-1)

    # Finish setting up the board
    for x in range(0, con.GRID_SIZE):
        for y in range(0, con.GRID_SIZE):
            t = board.tileAt(x,y)
            t.setValue(grid[x][y])
    
    for x in range(0, con.GRID_SIZE):
        for y in range(0, con.GRID_SIZE):
            t = board.tileAt(x,y)
            if (t.getValue() != con.TYPE_WALL and not t.getIsBomb()):
                board.setTileValues(x,y)
            if (t.getValue() == con.TYPE_START):
                t.setVisible()
                pos_x = x
                pos_y = y
	        if (t.getValue() == con.TYPE_EXIT):
				t.setVisible()

    # Player variables
    health = con.MAX_HEALTH
    direction = con.STAY # used for animation

    dest_x = pos_x
    dest_y = pos_y
    draw_x = pos_x*tilesize
    draw_y = pos_y*tilesize

    hp_x = int(round(con.HEALTH_X*con.SCREEN_WIDTH))
    hp_y = int(round(con.HEALTH_Y*con.SCREEN_HEIGHT))

	#Sound initalization
    #This currently works when this file has a subdirectory called sound.

    ####################################################
    # Main Code
    ####################################################

    def can_move_to(x, y):
        if (x >= con.GRID_SIZE or x < 0):
            res.hitWall.play()
            return False
        elif (y >= con.GRID_SIZE or y < 0):
            res.hitWall.play()
            return False
        elif (board.tileAt(x,y).getValue()==con.TYPE_WALL):
            res.hitWall.play()
            return False
        else:
            return True

    gameExit = False
    pygame.display.update()
    walking = False

    # BEGIN MAIN LOOP
    while (not gameExit):
        if (health <= 0):
            res.levelEnd.play()
            screen.blit(res.Lose,(0,0))
            pygame.display.flip()
            time.sleep(5.5)
            gameExit = true
            
        # Don't ask for movement input if already walking
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
            if (not walking):
                board.tileAt(dest_x,dest_y).setVisible()
        
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

					#Major walking routine
                    if can_move_to(dest_x,dest_y):
						#You hit a bomb
                        if (board.tileAt(dest_x,dest_y).getValue() == con.TYPE_BOMB_ACTIVE):
                            res.hitBomb.play()
                            health -= 1
                            (board.tileAt(dest_x,dest_y)).setValue(con.TYPE_BOMB_INACTIVE)
						#You step on a numbered tile that hasn't been revealed.
                        elif ((board.tileAt(dest_x,dest_y).getValue() > con.TYPE_EMPTY) and (board.tileAt(dest_x,dest_y).getValue() < con.MAX_SURROUNDING) and (board.tileAt(dest_x,dest_y).getVisible() == False)):
                            res.revealNum.play()

                        elif ((board.tileAt(dest_x,dest_y).getValue() == con.TYPE_EXIT)):
                            
                            res.levelEnd.play()
                            screen.blit(res.Win,(0,0))
                            pygame.display.flip()
                            time.sleep(5.5) 
                            gameExit = True
                        pos_x = dest_x
                        pos_y = dest_y
                        walking = True
                        player.setDirection(direction)
                        #print(board.tileAt(dest_x,dest_y).getValue())

        pygame.event.clear()

        screen.fill(con.WHITE)
        
        # Tiles are mainly static
        for y in range(0, con.GRID_SIZE):
            for x in range(0, con.GRID_SIZE):
                sprite = board.tileAt(x,y).getSprite()
                if board.tileAt(x,y).getValue()==con.TYPE_WALL:
                    frame = sprite.frame()
                elif board.tileAt(x,y).getVisible():
                    frame = sprite.frameVisible()
                else:
                    frame = sprite.frameHidden()
                screen.blit(frame, sprite.rect(x*tilesize, y*tilesize))

        #pygame.draw.rect(screen, con.GREEN, (draw_x, draw_y, tilesize, tilesize))
        
        screen.blit(player.frame(), player.rect(draw_x, draw_y))
        player.animateNext()

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
    
