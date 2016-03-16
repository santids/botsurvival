#Hexboard

from math import sin,cos, pi
from settings import settings
import utils.vect2d as vect
import numpy as np
from copy import copy


_loctypes = {0:'walk',
             1:'obstacle'}

class HexBoard:
    

    def __init__(self,radius,size):
        self.r = radius
        self.theight = (1.0+sin(1.0/6*pi))*radius
        self.twidth = 2*radius*cos(1.0/6*pi)
        self.size = size
        try:
            self.map = np.load(settings.map_src)
            if self.size != self.map.shape:
                self.size = self.map.shape
                print 'WARNING: map size differente from expected'
        except IOError:
            print 'WARNING: no map file found'
            self.map = np.zeros(size,dtype=int)
            
        self.alllocs = [(r,c) for r in xrange(self.size[0]) for c in xrange(self.size[1])]
        self.padding = 0
    
    def centerPoint(self,(row,col)):
        """Return the surface point corresponding with the center of the given hextile"""
        x = 0
        y = 0

        if row %2 ==0:
            x = col*self.twidth+self.padding
        else:
            x = (col+0.5)*self.twidth+self.padding
        y = row*self.theight+self.padding

        return (x,y)
    def isValidLoc(self,loc):
        """True if loc is inside map bounds"""
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
        """return the type of the loc. o.w. return invalid"""
        if self.isValidLoc(loc) and self.map[loc] in _loctypes:
            return _loctypes[self.map[loc]]
        else:
            return 'invalid'
    def wdist(self,loc1,loc2,maxdepth=15,depth=0,d=None,yafui=[]):
        yafui.append(loc1)
        if d == None:
            d=dict()
        if loc1 == loc2:
            return 0
        if depth > maxdepth or not self.isValidLoc(loc1):
            return int(1e3)
        if loc1 in d:
            return d[loc1]
        around = [loc for loc in self.locs_around(loc1) if loc not in yafui]

        try:
            dists = [self.wdist(loc,loc2,maxdepth,depth+1,d,copy(yafui)) for loc in around]     
            d[loc1] = 1+min(dists)
            
            return 1+min(dists)
        
        except RuntimeError:
            return int(1e3)
        except ValueError:
            return int(1e3)


        
        
    
#test
if __name__ == '__main__':
    
    board = HexBoard(20,(15,15))
    print "walk dist",board.wdist((2,0),(3,14))
    print board.locs_around((3,3))
    
                              
        
        
