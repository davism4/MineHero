# this file will store image and sound file data
# so that they can be loaded more quickly

import pygame, os

directory = os.path.dirname(os.path.realpath(__file__))

# References
screen = None # this is referenced in multiple places

# Graphics
#bombActive = pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_active.png'))
#bombInactive = pygame.image.load(os.path.join(directory,'graphics\\alpha\\bomb_inactive.png'))
#tile1 = pygame.image.load(os.path.join(directory,'graphics\\alpha\\1.png'))
#tile2 = pygame.image.load(os.path.join(directory,'graphics\\alpha\\2.png'))
#tile3 = pygame.image.load(os.path.join(directory,'graphics\\alpha\\3.png'))
#tile4 = pygame.image.load(os.path.join(directory,'graphics\\alpha\\4.png'))
#blank = pygame.image.load(os.path.join(directory,'graphics\\alpha\\blank.png'))
#unknown = pygame.image.load(os.path.join(directory,'graphics\\alpha\\unknown.png'))
#wall = pygame.image.load(os.path.join(directory,'graphics\\alpha\\wall.png'))
wall = pygame.image.load(os.path.join(directory,'graphics\\wall.png'))
stoneSheet = pygame.image.load(os.path.join(directory,'graphics\\tiles.png'))
jones = pygame.image.load(os.path.join(directory,'graphics\\Jonessheet.png'))

# Music
pygame.mixer.init()
hitBomb = pygame.mixer.Sound(os.path.join(directory, 'sound\\hitBomb.wav'))
hitWall = pygame.mixer.Sound(os.path.join(directory, 'sound\\hitWall.wav'))
levelStart = pygame.mixer.Sound(os.path.join(directory, 'sound\\levelStart.wav'))
levelEnd = pygame.mixer.Sound(os.path.join(directory, 'sound\\levelEnd.wav'))
revealNum = pygame.mixer.Sound(os.path.join(directory, 'sound\\revealNum.wav'))
