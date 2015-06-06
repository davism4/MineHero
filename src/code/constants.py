import pygame

# Set-up constants
FRAMES_PER_SECOND = 60
TILE_WIDTH = 38
GRID_SIZE = 14

TYPE_BOMB_ACTIVE = 10
TYPE_BOMB_INACTIVE = 11
TYPE_NONE = 0
TYPE_WALL = 9

# Player variables initial values
MAX_HEALTH = 3
MOVE_SPEED = 1

# Directions
STAY = 0
NORTH = 2
EAST = 4
SOUTH = 6
WEST = 8

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Specify as percentages of the game window
# Example: Map screen goes from 0,0 to 0.5,1
HEALTH_X = 0.75
HEALTH_Y = 0.5

# Calculated constants
SCREEN_WIDTH = 2*TILE_WIDTH*GRID_SIZE
SCREEN_HEIGHT = TILE_WIDTH*GRID_SIZE
