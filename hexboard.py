#Hexboard

from math import sin,cos, pi
import utils.vect2d as vect
import numpy as np


_loctypes = {0:'walk',
             1:'obstacle'}

class HexBoard:
    

    def __init__(self,radius,size):
        self.r = radius
        self.theight = (1.0+sin(1.0/6*pi))*radius
        self.twidth = 2*radius*cos(1.0/6*pi)
        self.size = size
        self.map = np.asarray([[1,1,1,1,1,1,1,1,1,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,1,1,1,1,1,1,1,1,1]])
        self.alllocs = [(r,c) for r in xrange(size[0]) for c in xrange(size[1])]
        self.padding = 0
    
    def centerPoint(self,(row,col)):
        x = 0
        y = 0

        if row %2 ==0:
            x = col*self.twidth+self.padding
        else:
            x = (col+0.5)*self.twidth+self.padding
        y = row*self.theight+self.padding

        return (x,y)
    def isValidLoc(self,loc):
        return vect.isInsideRect(loc,self.size)
        
    def locs_around(self,loc,filter=None):
        """nearby Locs"""
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
        if filter:
            nl = [loc for loc in nl if _loctypes[self.map[loc]]not in filter]

        return nl
    def loc_type(self,loc):
        if self.map[loc] in _loctypes:
            return _loctypes[self.map[loc]]
        else:
            return 'invalid'
        
    
#test
if __name__ == '__main__':
    
    board = HexBoard(20,(10,10))
    print board.locs_around((1,1),filter=['obstacle'])
    print board.map[(0,0)]
    
                              
        
        
