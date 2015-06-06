class Board(object):
#class Board(pygame.sprite.Sprite):
    def __init__(self,XWid, YWid):
        self.XWid= XWid+2 #Two because border
        self.YWid= YWid+2 #Two because border
	self.Tiles = []

    def createBoard(self):
	self.Tiles = [[Tile(y,x) for y in range(self.YWid)] for x in range(self.XWid)] 
        #This with make a board with range [x][y]

    def __getitem__(self,key):
	return 0

    def getTile(self, x, y):
	return self.Tiles[x][y]

    def getBoard(self):
	return self.Tiles
    
    def putmine(self,x,y):
	self.Tiles[x][y].IfBomb = True

	#When called, this will change each tile's BombSurround.
    def FindBombSurrond(self):
	zoneNumber = 0
	for x in range(0, self.XWid):
		for y in range(0, self.YWid):
			

			#This is a check for if the tile is on the border
			if (x == 0) or (x == (self.XWid)-1) or ( y == 0) or ( y == (self.YWid) - 1):
				a = 1
			else:
			    neighboursArray = self.Findsurrounds(x,y)
			    length = len(neighboursArray)
			    zoneNumber = 0			#resetting the value for each zone
			    for d in range(0, length):
			    	if(self.Tiles[neighboursArray[d][1]][neighboursArray[d][0]].IfBomb):
				    zoneNumber+=1 
			#zones[x][y].num_txt.text = String(zoneNumber)
			self.Tiles[x][y].NumBombSurround= zoneNumber

    def Findsurrounds(self,x,y):
        neighboursArray= []
	print x
	print y
	print "\n"
	if y == 1:
		neighboursArray.append([y + 1,x])		#bottom center
		if x == 1:	#three surrounding zones
			neighboursArray.append([y,x + 1])		#middle right
			neighboursArray.append([y + 1,x + 1])	#bottom right
		elif x == (self.XWid - 2):	#three surrounding zones
			neighboursArray.append([y,x - 1])		#middle left
			neighboursArray.append([y + 1,x - 1])	#bottom left
		else:		#five surrounding zones
			neighboursArray.append([y,x - 1])		#middle left
			neighboursArray.append([y,x + 1])		#middle right
			neighboursArray.append([y + 1,x - 1])	#bottom left
			neighboursArray.append([y + 1,x + 1])	#bottom right
		
	elif (y == (self.YWid - 2)):
	 	neighboursArray.append([y - 1,x])		#top center
		if(x == 1):	#three surrounding zones
			neighboursArray.append([y - 1,x + 1])	#top right
			neighboursArray.append([y,x + 1])		#middle right
		elif (x == (self.XWid - 2)):	#three surrounding zones
			neighboursArray.append([y - 1,x - 1])	#top left
			neighboursArray.append([y,x - 1])		#middle left
		else:	#five surrounding zones
			neighboursArray.append([y - 1,x - 1])	#top left
			neighboursArray.append([y - 1,x + 1])	#top right
			neighboursArray.append([y,x - 1])		#middle left
			neighboursArray.append([y,x + 1])		#middle right
		
	else:
		neighboursArray.append([y - 1,x])		#top center
		neighboursArray.append([y + 1,x])		#bottom center
		if(x == 1):						#five surrounding zones
			neighboursArray.append([y - 1,x + 1])	#top right
			neighboursArray.append([y,x + 1])		#middle right
			neighboursArray.append([y + 1,x + 1])	#bottom right
		elif (x == (self.XWid - 2)):	#five surrounding zones
			neighboursArray.append([y - 1,x - 1])	#top left
			neighboursArray.append([y,x - 1])		#middle left
			neighboursArray.append([y + 1,x - 1])	#bottom left
		else:								#eight surrounding zones
			neighboursArray.append([y - 1,x - 1])	#top left
			neighboursArray.append([y - 1,x + 1])	#top right
			neighboursArray.append([y,x - 1])		#middle left
			neighboursArray.append([y,x + 1])		#middle right
			neighboursArray.append([y + 1,x - 1])	#bottom left
			neighboursArray.append([y + 1,x + 1])	#bottom right
		
	return neighboursArray

class Tile(Board):
#class Board(pygame.sprite.Sprite):
    #def __init__(self, Ifbomb, BombSurround, IfRevealed, IfWall):
    def __init__(self, j, i):
        self.IfBomb = False #If there's a bomb there
	    self.BombActive = False #If it's on/off
        self.NumBombSurround = 0 #How much stuff surrounds it
        self.IfRevealed = False #If it's been stepped on
        self.Xpos = i #X Coord
        self.Ypos = j #Y Coord
	self.IfWall = False
   
    def getIfBomb(self):
        return self.IfBomb

    def getIfRevealed(self):
        return IfRevealed

    def getNumBombSurround (self):
        return NumBombSurround 

    def getIfWall(IfWall):
	return IfWall

    def getXpos(self):
        return self.XPos

    def getYpos(self):
        return self.YPos

    def setIfBomb(Z):
        self.IfBomb = Z

    def setIfRevealed(Z):
        self.IfRevealed = Z

    def setNumBombSurround (Z):
        self.NumBombSurround = Z

    def setIfWall(Z):
	self.IfWall = Z

    def setXpos(Z):
        self.Xpos = Z

    def setYpos(Z):
        self.Ypos = Z

	def __getitem__(self,key):
	return 0
    
