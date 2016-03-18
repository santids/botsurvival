import utils.vect2d as vect



class View:
    def __init__(self,mapsize,height=10,width=10):
        self.row = 0
        self.col = 0
        self.width = width
        self.height = height
        self.mapsize = mapsize
        print mapsize
    def getPos(self):
        return (self.row,self.col)
    def setPos(self,loc):
        if self.canMove(loc):
            self.row = loc[0]
            self.col = loc[1]
    def move(self,vel):
        self.setPos(vect.suma(self.getPos(),vel))
    def getBoardLoc(self,view_loc):
        return vect.suma(self.getPos(),view_loc)
    def getViewLoc(self,board_loc):
        return vect.resta(board_loc,self.getPos())
    def getSize(self):
        return (self.height,self.width)
    def canMove(self,pos):
        maxpos = vect.resta(self.mapsize,self.getSize())
        return vect.isInsideRect(pos,maxpos)

if __name__== '__main__':
    v = View((2,2))
    v.move((0,1))
    loc = (3,3)
    print v.getPos(),v.getBoardLoc(loc)
