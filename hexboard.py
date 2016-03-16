#Hexboard

from math import cos, pi
import utils.vect2d as vect

class HexBoard:

    def __init__(self,radius,size):
        self.r = radius
        self.theight = 2*radius
        self.twidth = 2*radius*cos(1.0/6*pi)
        self.size = size
    
    def getLocCenterPoint((row,col)):
        x = 0
        y = 0

        if row %2 ==0:
            x = col*self.twidth
        else:
            x = (col+0.5)*self.twidth
        y = row*self.theigth

        return (x,y)
    def isValidLoc(self,loc):
        return vect.isInsideRect(loc,self.size)
        
    def locs_around(self,loc):
        locs = list()
        #sides
        locs.append(vect.suma(loc,(0,1)))
        locs.append(vect.suma(loc,(0,-1)))
        #vertically
        locs.append(vect.suma(loc,(1,0)))
        locs.append(vect.suma(loc,(-1,0)))
        #diagonally
        if loc[0] % 2== 0: #si la fila es par
            locs.append(vect.suma(loc,(-1,-1)))
            locs.append(vect.suma(loc,(1,-1)))
        else:
            locs.append(vect.suma(loc,(-1,1)))
            locs.append(vect.suma(loc,(1,1)))


        nl = [loc for loc in locs if self.isValidLoc(loc)]

        return nl
    
#test
if __name__ == '__main__':
    
    board = HexBoard(20,(50,50))
    print board.locs_around((1,0))
    
                              
        
        
