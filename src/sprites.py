import pygame, spritesheet, random
import constants as con
import resources as res

Spritesheet = spritesheet.Spritesheet

# Has templates for sprites for in-game objects
# Note: VALUES ARE HARDCODED! If you change the spritesheet,
# you will have to modify these values!

class TileSprite(Spritesheet):
    def __init__(self, number, randomize=True):
        super(TileSprite, self).__init__(res.stoneSheet, (4,7))
        if (randomize):
            random.seed()
            k = random.randrange(3)
            # array index is the tile contents
            # array value (x,x) refers to a location on the spritesheete
            # order = [hidden, 0, 1, 2, 3, 4, bomb]
            if (k==0):
                self.order = [(3,3),(2,3),(0,0),(1,0),(2,0),(3,0),(2,5)]
            elif (k==1):
                self.order = [(0,4),(1,3),(0,1),(1,1),(2,1),(3,1),(0,6)]
            else:
                self.order = [(1,4),(0,3),(0,1),(1,1),(2,1),(3,1),(3,5)]
        self.number = number

    # Gets the frame if the tile is hidden
    def frameHidden(self):
        (c, r) = self.order[0]
        return self.frameAt(c, r)

    # Gets the frame if the tile is visible
    def frameVisible(self):
        if (self.number == con.TYPE_BOMB_ACTIVE or self.number == con.TYPE_BOMB_INACTIVE):
            (c, r) = self.order[6]
        else:
            (c, r) = self.order[self.number + 1]
        return self.frameAt(c, r)

    # Called when player activates the tile
    def setVisible(self):
        self.r = 1
        return

    def setInvisible(self):
        self.r = 0
        return

# Used for walls. Nothing complex here.
class WallSprite(Spritesheet):
    def __init__(self, random=True):
        super(WallSprite, self).__init__(res.wall, (4,4))

# Player's sprite.
class JonesSprite(Spritesheet):
    def __init__(self):
        super(JonesSprite, self).__init__(res.jones, (4,4))
        # orders for animation frames
        self.order_walkSouth = [(0,0), (1,0), (2,0)]
        self.order_walkNorth = [(3,0), (0,1), (1,1)]
        self.order_walkWest = [(2,1), (3,1)]
        self.order_walkEast = [(0,2), (1,2)]
        self.setOrder(self.order_walkNorth)

    # Parameters from level.py, based on input
    def setDirection(self, direction):
        if (direction==con.NORTH):
            self.setOrder(self.order_walkNorth)
        elif (direction==con.EAST):
            self.setOrder(self.order_walkEast)
        elif (direction==con.SOUTH):
            self.setOrder(self.order_walkSouth)
        elif (direction==con.WEST):
            self.setOrder(self.order_walkWest)

    # override to allow alpha (transparent background)
    def frame(self):
        rect = pygame.Rect((self.c*self.w,self.r*self.h,self.w,self.h))
        image = pygame.Surface(rect.size).convert()
        image.set_colorkey((0,0,255))
        image.blit(self.sheet, (0, 0), rect)
        return image

