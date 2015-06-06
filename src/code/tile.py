class Board(object):
#class Board(pygame.sprite.Sprite):
    def __init__(self,XWid, YWid):
        self.XWid= XWid+2
        self.YWid= YWid+2
	self.Tiles = []

    def createBoard(self):
	self.Tiles = [[Tile(y,x) for y in range(self.YWid)] for x in range(self.XWid)] 
        #This with make a board with range [x][y]
		#zones[i][j].x = j*40 + 20;
        	#zones[i][j].y = i*40 + 20;
    def __getitem__(self,key):
	return 0

    def getTile(self, x, y):
	return self.Tiles[x][y]

    def getBoard(self):
	return self.Tiles
    
    def putmine(self,x,y):
	self.Tiles[x][y].IfBomb = True


    def FindBombSurrond(self):
	zoneNumber = 0
	for x in range(0, self.XWid):
		for y in range(0, self.YWid):
			#zones[x][y].block_mc.visible = False
			if (x == 0) or (x == (self.XWid)-1) or ( y == 0) or ( y == (self.YWid) - 1):
				1+1
			else:
			    neighboursArray = self.Findsurrounds(x,y)
			    length = len(neighboursArray)
			    zoneNumber = 0			#resetting the value for each zone
			    for d in range(0, length):
				#print neighboursArray
				#print neighboursArray[d]
				#print d
				#print "\n"
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
        self.IfBomb = False
	self.BombActive = False
        self.NumBombSurround = 0
        self.IfRevealed = False
        self.Xpos = i
        self.Ypos = j
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

    
