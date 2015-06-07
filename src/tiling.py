import constants as con, resources as res
import spritesheet, sprites

# One instance for level; contains a 2D array of Tiles
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
    # Note: Code is substituted elsewhere
    def setTileValues(self, x, y):
        tile = self.Tiles[x][y]
        if (tile.value != con.TYPE_WALL):
            neighbors = []
            count = 0
            # Only check in cardinal directions
            for (i,j) in [[0, 1],[1, 0],[0,-1],[-1,0]]:
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
        self.sprite = None
        self.neighbors = []

    # Bomb sprites are used for counting neighboring bombs
    def getIsBomb(self):
        return (self.value==con.TYPE_BOMB_ACTIVE or self.value==con.TYPE_BOMB_INACTIVE)

    # Get the sprite at this tile
    def getSprite(self):
        return self.sprite

    # Wall, bomb, inactive bomb, or # of neighbors (see constants)
    def getValue(self):
        return self.value

    # Is the tile content revealed yet?
    def getVisible(self):
        return self.visible

    #  Wall, bomb, inactive bomb, or # of neighbors (see constants)
    def setValue(self, value):
        self.value = value
        if (self.value == con.TYPE_WALL):
            self.sprite = sprites.WallSprite()
        else:
            self.sprite = sprites.TileSprite(value)
        return

    # from invisible (hidden value) to visible (visible value)
    def setVisible(self):
        if (self.value != con.TYPE_WALL and not self.visible):
            self.sprite.setVisible()
            self.visible = True
        
    
