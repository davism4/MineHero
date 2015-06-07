import pygame
import constants as con
import resources as res

class Spritesheet(pygame.sprite.Sprite):
    # NOTE: Column = x index, Row = y index
    
    def __init__(self, sheet, (cols, rows)=(1,1), (frameWidth, frameHeight)=con.TILE_SIZE):
        super(Spritesheet,self).__init__()
        self.sheet = sheet
        self.order = [(0,0)]
        self.index = 0
        self.w = frameWidth # frame width
        self.h = frameHeight # frame height
        self.c = 0 # current column (depends on index)
        self.r = 0 # current row (depends on index)
        (self.cols, self.rows) = (cols, rows)
        return

    # Assume that the sheet will be traversed in an order
    def setOrder(self, order):
        self.order = order
        return

    # Get the frame at x,y (c,r) on the sheet
    def setFrame(self, c, r):
        self.r = r
        self.c = c

    # Gets from the spritesheet, index by column/row numbers
    def frameAt(self, c, r):
        rect = pygame.Rect((c*self.w,r*self.h,self.w,self.h))
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image

    # Returns the current frame
    def frame(self):
        return self.frameAt(self.c, self.r)

    # Generates a Rect that starts at coords (x,y)
    def rect(self, x, y):
        return pygame.Rect(x, y, x+self.w, y+self.h)

    # When you have an ordered list of sprites, this can be used
    # to animate the sprite in a cycle
    def animateNext(self):
        self.index = (self.index + 1) % len(self.order)
        (self.c, self.r) = self.order[self.index]
        return self.frameAt(self.c, self.r)

    # Parameter is a surface
    def setSheet(self, sheet):
        self.sheet = sheet
        return
