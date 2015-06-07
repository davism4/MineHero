import constants as con
import resources as res
import sprite

class Board(object):
    def __init__(self, XWid=con.GRID_SIZE, YWid=con.GRID_SIZE):
        #super(object, self).__init__()
        self.dimX = XWid
        self.dimY = YWid
        self.Tiles = [[Tile(y,x) for y in range(YWid)] for x in range(XWid)] 
        #This with make a board with range [x][y]

    def tileAt(self, x, y):
        return self.Tiles[x][y]

    # do not call on wall spaces
    def setTileValues(self, x, y):
        tile = self.Tiles[x][y]
        if (tile.value != con.TYPE_WALL):
            neighbors = []
            count = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    t = self.Tiles[x+i][y+j]
                    if (t.value != con.TYPE_WALL):
                        neighbors.append(t)
                        if (t.getIsBomb()):
                            count += 1
            tile.neighbors = neighbors
            if (tile.value >=0 and tile.value <= 8):
                self.Tiles[x][y].setValue(count)
        return

    # TODO
    # Given an empty space, reveals other empty spaces nearby
    def reveal(self, x, y):
        self.Tiles[x][y].visible = True
        return


class Tile(object):
    def __init__(self, j, i, value=con.TYPE_EMPTY):
        #super(object, self).__init__()
        self.value = value
        self.visible = False
        self.sprite = sprite.Sprite([])
        self.neighbors = []

    def getIsBomb(self):
        return (self.value==con.TYPE_BOMB_ACTIVE or self.value==con.TYPE_BOMB_INACTIVE)

    def setImages(self, images):
        self.sprite.setImages(images)

    def getSprite(self):
        return self.sprite

    def getValue(self):
        return self.value

    def getVisible(self):
        return self.visible

    def setValue(self, value):
        self.value = value
        
        if (self.value == con.TYPE_BOMB_ACTIVE):
            self.setImages([res.unknown, res.bombActive, res.bombInactive])
        elif (self.value == con.TYPE_WALL):
            self.setImages([res.wall])
        elif (self.value == 0):
            self.setImages([res.unknown, res.blank])
        elif (self.value == 1):
            self.setImages([res.unknown, res.tile1])
        elif (self.value == 2):
            self.setImages([res.unknown, res.tile2])
        elif (self.value == 3):
            self.setImages([res.unknown, res.tile3])
        elif (self.value == 4):
            self.setImages([res.unknown, res.tile4])
        elif (self.value == 5):
            self.setImages([res.unknown, res.tile5])
        elif (self.value == 6):
            self.setImages([res.unknown, res.tile6])
        elif (self.value == 7):
            self.setImages([res.unknown, res.tile7])
        elif (self.value == 8):
            self.setImages([res.unknown, res.tile8])
        return
        
    def setVisible(self):
        if (not self.visible):
            self.sprite.advanceFrame()
            self.visible = True
        
    
