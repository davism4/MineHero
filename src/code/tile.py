import constants as con

class Board(object):
#class Board(pygame.sprite.Sprite):
    def __init__(self, XWid=con.GRID_SIZE, YWid=con.GRID_SIZE):
        self.XWid= XWid #+2 #Two because border
        self.YWid= YWid #+2 #Two because border
        self.Tiles = [[Tile(y,x) for y in range(self.YWid)] for x in range(self.XWid)] 
        #This with make a board with range [x][y]

    def __getitem__(self,key):
        return 0

    def getTile(self, x, y):
        return self.Tiles[x][y]

    def getBoard(self):
        return self.Tiles

    #When called, this will change each tile's BombSurround.
    def FindBombSurround(self):
        zoneNumber = 0
        for x in range(0, self.XWid):
            for y in range(0, self.YWid):
                
                #This is a check for if the tile is on the border
                if (x == 0) or (x == (self.XWid)-1) or ( y == 0) or ( y == (self.YWid) - 1):
                        a = 1
                else:
                    neighboursArray = self.Findsurrounds(x,y)
                    length = len(neighboursArray)
                    zoneNumber = 0          #resetting the value for each zone
                    for d in range(0, length):
                        if(self.Tiles[neighboursArray[d][1]][neighboursArray[d][0]].tileType == constants.TYPE_BOMB):
                            zoneNumber+=1 
                #zones[x][y].num_txt.text = String(zoneNumber)
                self.Tiles[x][y].NumBombSurround= zoneNumber

    def Findsurrounds(self,x,y):
        neighboursArray= []
        if y == 1:
            neighboursArray.append([y + 1,x])       #bottom center
            if x == 1:  #three surrounding zones
                neighboursArray.append([y,x + 1])       #middle right
                neighboursArray.append([y + 1,x + 1])   #bottom right
            elif x == (self.XWid - 2):  #three surrounding zones
                neighboursArray.append([y,x - 1])       #middle left
                neighboursArray.append([y + 1,x - 1])   #bottom left
            else:       #five surrounding zones
                neighboursArray.append([y,x - 1])       #middle left
                neighboursArray.append([y,x + 1])       #middle right
                neighboursArray.append([y + 1,x - 1])   #bottom left
                neighboursArray.append([y + 1,x + 1])   #bottom right
            
        elif (y == (self.YWid - 2)):
            neighboursArray.append([y - 1,x])       #top center
            if(x == 1): #three surrounding zones
                neighboursArray.append([y - 1,x + 1])   #top right
                neighboursArray.append([y,x + 1])       #middle right
            elif (x == (self.XWid - 2)):    #three surrounding zones
                neighboursArray.append([y - 1,x - 1])   #top left
                neighboursArray.append([y,x - 1])       #middle left
            else:   #five surrounding zones
                neighboursArray.append([y - 1,x - 1])   #top left
                neighboursArray.append([y - 1,x + 1])   #top right
                neighboursArray.append([y,x - 1])       #middle left
                neighboursArray.append([y,x + 1])       #middle right
            
        else:
            neighboursArray.append([y - 1,x])       #top center
            neighboursArray.append([y + 1,x])       #bottom center
            if(x == 1):                     #five surrounding zones
                neighboursArray.append([y - 1,x + 1])   #top right
                neighboursArray.append([y,x + 1])       #middle right
                neighboursArray.append([y + 1,x + 1])   #bottom right
            elif (x == (self.XWid - 2)):    #five surrounding zones
                neighboursArray.append([y - 1,x - 1])   #top left
                neighboursArray.append([y,x - 1])       #middle left
                neighboursArray.append([y + 1,x - 1])   #bottom left
            else:                               #eight surrounding zones
                neighboursArray.append([y - 1,x - 1])   #top left
                neighboursArray.append([y - 1,x + 1])   #top right
                neighboursArray.append([y,x - 1])       #middle left
                neighboursArray.append([y,x + 1])       #middle right
                neighboursArray.append([y + 1,x - 1])   #bottom left
                neighboursArray.append([y + 1,x + 1])   #bottom right
            
        return neighboursArray

class Tile(Board):
    def __init__(self, j, i, tt=con.TYPE_NONE):
        self.tileType = tt # refer to constants
        self.NumBombSurround = 0 #How much stuff surrounds it
        self.IfRevealed = False #If it's been stepped on
        self.Xpos = i #X Coord
        self.Ypos = j #Y Coord

    def getTileType(self):
        return self.tileType

    def getIfRevealed(self):
        return IfRevealed

    def getNumBombSurround (self):
        return NumBombSurround 

    def getXpos(self):
        return self.XPos

    def getYpos(self):
        return self.YPos

    def setTileType(self, Z):
        self.tileType = Z

    def setIfRevealed(self, Z):
        self.IfRevealed = Z

    def setNumBombSurround (self, Z):
        self.NumBombSurround = Z

    def setXpos(self, Z):
        self.Xpos = Z

    def setYpos(self, Z):
        self.Ypos = Z

    def __getitem__(self, key):
        return 0
    
