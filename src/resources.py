# this file will store image and sound file data
# so that they can be loaded more quickly

import pygame, os

directory = os.path.dirname(os.path.realpath(__file__))

# References
screen = None # this is referenced in multiple places

# Graphics
sanic = [pygame.image.load(os.path.join(directory,'graphics\sanick.jpg'))]

# Music
