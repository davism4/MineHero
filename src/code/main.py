import pygame
import constants as con
import tile
import level

pygame.init()

# Initialize the program

con.screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
pygame.display.set_caption('Jones Bond: Mine Hero')

level.run()

##while (not gameExit):
##    for event in pygame.event.get():
##        if (event.type == pygame.QUIT):
##            gameExit = True
##        elif (event.type == pygame.KEYDOWN):
##            if (event.key == pygame.K_ESCAPE):
##                gameExit = True
##    level.update()
##    gameExit = level.gameExit
    

# END MAIN LOOP

pygame.quit() #uninitializes things
quit() # necessary to quit python
