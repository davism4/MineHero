import pygame, level
import constants as con, resources as res
from pygame.locals import FULLSCREEN , DOUBLEBUF , HWSURFACE, RLEACCEL

pygame.init()

# Initialize the program

screensize = (con.SCREEN_WIDTH, con.SCREEN_HEIGHT)
options = (DOUBLEBUF | HWSURFACE)
screen = pygame.display.set_mode(screensize, options, 32)
res.screen = screen
pygame.display.set_caption('Jones Bond: Mine Hero')

level.run()


pygame.quit() #uninitializes things
quit() # necessary to quit python
