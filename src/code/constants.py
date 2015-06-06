import pygame

# Set-up constants
FRAMES_PER_SECOND = 60
TILE_WIDTH = 38
GRID_SIZE = 14
BOMB_ACTIVE_TYPE = -1
BOMB_INACTIVE_TYPE = -2
WALL_TYPE = 9

# Player variables initial values
MAX_HEALTH = 10
MOVE_SPEED = 1

# Directions
STAY = 0
NORTH = 2
EAST = 4
SOUTH = 6
WEST = 8

# Specify as percentages of the game window
# Example: Map screen goes from 0,0 to 0.5,1
HEALTH_X = 0.75
HEALTH_Y = 0.5

# Calculated constants
SCREEN_WIDTH = 2*TILE_WIDTH*GRID_SIZE
SCREEN_HEIGHT = TILE_WIDTH*GRID_SIZE
