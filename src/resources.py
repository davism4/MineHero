# this file will store image and sound file data
# so that they can be loaded more quickly

import pygame, os

directory = os.path.dirname(os.path.realpath(__file__))

# References
screen = None # this is referenced in multiple places

# Graphics
sanic = [pygame.image.load(os.path.join(directory,'graphics\\sanick.jpg'))]
tileBombActive = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_active.png'))]
tileBombInctive = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))]
tile1 = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))]
tile2 = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))]
tile3 = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))]
tile4 = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))]
tile5 = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))]
tile6 = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))]
tile7 = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))]
tileBlank = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\blank.png'))]
unknown = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\unknown.png'))]
wall = [pygame.image.load(os.path.join(directory,'graphics\\alpha\\wall.png'))]

# Music
