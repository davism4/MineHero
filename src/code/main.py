import pygame
import constants as con
pygame.init()

# Initialize the program

screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
pygame.display.set_caption('Mine Hero')
clock = pygame.time.Clock()
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
gray = (128, 128, 128)

# Initialize the grid
grid = [[0 for x in range(con.GRID_SIZE)] for x in range(con.GRID_SIZE)]
for x in range(con.GRID_SIZE):
    grid[x][0] = con.WALL_TYPE
    grid[x][con.GRID_SIZE-1] = con.WALL_TYPE
for y in range(con.GRID_SIZE):
    grid[0][y] = con.WALL_TYPE
    grid[con.GRID_SIZE-1][y] = con.WALL_TYPE
grid[5][5] = con.BOMB_ACTIVE_TYPE
grid[3][8] = con.BOMB_ACTIVE_TYPE

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
    elif (grid[x][y] == con.WALL_TYPE):# or grid[x][y] == con.BOMB_ACTIVE_TYPE):
        return False
    else:
        return True

gameExit = False
pygame.display.update()
walking = False

# BEGIN MAIN LOOP
while (not gameExit):
##    dest_x = pos_x
##    dest_y = pos_y
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
                    if (grid[dest_x][dest_y] == con.BOMB_ACTIVE_TYPE):
                        health -= 1
                        grid[dest_x][dest_y] = con.BOMB_INACTIVE_TYPE
                    else:
                        pos_x = dest_x
                        pos_y = dest_y
                        walking = True

    pygame.event.clear()

    screen.fill(white)
    # Tiles are mainly static
    for y in range(0, con.GRID_SIZE):
        for x in range(0, con.GRID_SIZE):
            if (grid[x][y] == con.BOMB_ACTIVE_TYPE):
                pygame.draw.rect(screen, red, (x*con.TILE_WIDTH, y*con.TILE_WIDTH, con.TILE_WIDTH, con.TILE_WIDTH))
            elif (grid[x][y] == con.BOMB_INACTIVE_TYPE):
                pygame.draw.rect(screen, gray, (x*con.TILE_WIDTH, y*con.TILE_WIDTH, con.TILE_WIDTH, con.TILE_WIDTH))

            elif (grid[x][y] == con.WALL_TYPE):
                pygame.draw.rect(screen, black, (x*con.TILE_WIDTH, y*con.TILE_WIDTH, con.TILE_WIDTH, con.TILE_WIDTH))

    pygame.draw.rect(screen, green, (draw_x, draw_y, con.TILE_WIDTH, con.TILE_WIDTH))
              

    for h in range(0, health):
        pygame.draw.rect(screen, red, (hp_x + h*15, hp_y, 10, 10))

    
#    healthLabel = myfont.render('health: '+`health`,1,white)
#    screen.blit(healthLabel, (hp_x, hp_y))
    
     # clear before rendering graphics
    #pygame.event.clear()
    
    clock.tick(1/con.FRAMES_PER_SECOND)
    pygame.display.update()
    

# END MAIN LOOP

pygame.quit() #uninitializes things
quit() # necessary to quit python
