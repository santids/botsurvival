#Hexboard

from math import sin,cos, pi
from settings import settings
import utils.vect2d as vect
import numpy as np
from copy import copy
import display.waveTexture as wt
from random import randint

_loctypes = {0:'water',
             1:'plains',
             2:'hills',
             3:'mountain',
             }

class HexBoard:
    
    
    def __init__(self,radius,size):
        self.r = radius
        self.theight = (1.0+sin(1.0/6*pi))*radius
        self.twidth = 2*radius*cos(1.0/6*pi)
        self.size = size
        self.alllocs = [(r,c) for r in xrange(self.size[0]) for c in xrange(self.size[1])]
        self.padding = 0
        self.map = wt.createWaveMap(size,3,randint(0,2**10))
        """
        try:
            self.map = np.load(settings.map_src)
            if self.size != self.map.shape:
                self.size = self.map.shape
                print 'WARNING: map size differente from expected'
        except IOError:
            print 'WARNING: no map file found'
            self.map = np.zeros(size,dtype=int)
        """
        
            

        
    
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

    def createNormalMap(self):
        arr = np.random.normal(1.5,1.5,vect.div(self.size,2))
        arr = np.repeat(arr,2,0)
        arr = np.repeat(arr,2,1)
        for loc in self.alllocs:
            arr[loc] = min(max(round(arr[loc]),0),4)
        return arr
    def createBinomialMap(self):
        arr = np.random.binomial(3,0.3,vect.div(self.size,3))
        print np.mean(arr)
        arr = np.repeat(arr,3,0)
        arr = np.repeat(arr,3,1)

        self.size = arr.shape
        
        return arr
    def createGeometricMap(self):
        arr = np.random.geometric(0.35,vect.div(self.size,3))
        arr = np.repeat(arr,3,0)
        arr = np.repeat(arr,3,1)
        for loc in self.alllocs:
            arr[loc] = min(5,arr[loc])
        print np.mean(arr)
        if self.size != arr.shape:
            print "WARNING: Unexpecte map size"
            self.size = arr.shape

        return arr
    def toward(self,curr,target,filter=None):
        options = self.locs_around(curr,filter)
        dist = min([vect.dist(loc,target) for loc in options])
        for loc in options:
            if vect.dist(loc,target) == dist:
                return loc
    def mapCenter(self):
        return vect.div(self.size,2)
    
#End of class definition
    
def wdist(loc1,loc2):
    #Need further testing
    dx = abs(loc2[1]-loc1[1])
    dy = abs(loc2[0]-loc1[0])
    l = [x for x in range(dy) if x%2==0]
    if dx==0:
        return dy
    return dx+dy-min(dx,len(l))
    
    
#test
if __name__ == '__main__':
    board = HexBoard(8,(51,51))
    loc = (3,3)
    print board.mapCenter()
    
                              
        
        
