import pygame
import constants as con
import resources as res

class Sprite(pygame.sprite.Sprite):
    def __init__(self, images, (width, height)=con.TILE_SIZE):
        super(Sprite, self).__init__()
        self.images = []
        (self.w, self.h) = (width, height)
        self.index = 0
        self.addImages(images)
        if (images == None or images == []):
            self.activeFrame = None
        else:
            self.activeFrame = self.images[self.index]

    def get(self):
        return self.activeFrame
    
    def rect(self, x, y):
        return pygame.Rect(x, y, x+self.w, y+self.h)
    
    def advanceFrame(self):
        if len(self.images) > 0:
            self.index = (self.index + 1) % len(self.images)
            self.activeFrame = self.images[self.index]

    def addImages(self, images):
        for i in images:
            i = i.convert()
            temp = pygame.Surface((self.w, self.h))
            pygame.transform.scale(i, (self.w, self.h), temp)
            i = temp
            self.images.append(i)

    def setImages(self, images):
        self.addImages(images)
        self.index = 0
        self.activeFrame = self.images[0]

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def setDims(self, w, h):
        self.w = w
        self.h = h

class MultiSprite(Sprite):
    def __init__(self, images, (width, height)=con.TILE_SIZE):
        super(MultiSPrite, self, (width, height)).__init__()
        self.speed = 1.0

    def setSpeed(self, speed):
        self.speed = speed

    def animate(self):
        if (speed > 0):
            self.advanceFrame()
            self.activeFrame = self.images[self.index]
        return self.activeFrame

class SheetSprite(Sprite):
    def __init__(self, sheet, (width, height), (rows, cols)):
        super(SheetSprite, self, size).__init__()
        self.speed = 1.0
        self.r = 0 # current row
        self.c = 0 # current column
        (self.rows, self.cols) = (rows, cols)
        self.sheet = sheet

    def frameAt(self, r, c):
        rect = pygame.Rect((r*frameWidth,c*frameHeight,(r+1)*frameWidth,(c+1)*frameHeight))
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image

    def setSpeed(self, speed):
        self.speed = speed

    def animateXY(self):
        if (speed > 0):
            self.c += 1
            if (self.c >= self.cols):
                self.c = 0
                self.r += 1
                if (self.r >= self.rows):
                    self.r = 0
            self.activeFrame = self.frameAt(self.r, self.c)
        return self.activeFrame

    def animateYX(self):
        if (speed > 0):
            self.r += 1
            if (self.r >= self.rows):
                self.r = 0
                self.c += 1
                if (self.c >= self.cols):
                    self.c = 0
            self.activeFrame = self.frameAt(self.r, self.c)
        return self.activeFrame
