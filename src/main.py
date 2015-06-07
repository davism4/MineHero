import pygame, level, sprites, process_images
import constants as con, resources as res
from pygame.locals import FULLSCREEN , DOUBLEBUF , HWSURFACE, RLEACCEL

pygame.init()

# Initialize the program

screensize = (con.SCREEN_WIDTH, con.SCREEN_HEIGHT)
options = (DOUBLEBUF | HWSURFACE)
screen = pygame.display.set_mode(screensize, options, 32)
res.screen = screen

# setup
pygame.display.set_caption('Jones Bond: Mine Hero')

process_images.process()


level.run()
##
##sprite = sprites.TileSprite(1)
##
##while(True):
##    pygame.display.update()
##    screen.fill(con.WHITE)
##    tilesize = con.TILE_WIDTH
##    screen.blit(sprite.frame(), (10, 20, tilesize*5, tilesize*5))
##    pygame.display.update()
##
##

pygame.quit() #uninitializes things
quit() # necessary to quit python
