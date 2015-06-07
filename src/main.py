import pygame
import constants as con
import tile
import level
import resources as res
from pygame.locals import FULLSCREEN , DOUBLEBUF , HWSURFACE, RLEACCEL

pygame.init()

# Initialize the program

screensize = (con.SCREEN_WIDTH, con.SCREEN_HEIGHT)
options = (DOUBLEBUF | HWSURFACE)
screen = pygame.display.set_mode(screensize, options, 32)
res.screen = screen
pygame.display.set_caption('Jones Bond: Mine Hero')

# Load resources

#sanic = [pygame.image.load(os.path.join(directory,'graphics\sanick.jpg')).convert()]
#sanicSurface = pygame.Surface((con.TILE_WIDTH, con.TILE_WIDTH))
#pygame.transform.scale(sanic[0], (con.TILE_WIDTH, con.TILE_WIDTH), sanicSurface)
#sanic[0] = sanicSurface
# Store loaded resources in another file
#res.sanic = sanic


level.run()


pygame.quit() #uninitializes things
quit() # necessary to quit python
