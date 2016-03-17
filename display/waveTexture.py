import numpy as np
from math import sqrt, sin

vel = 50

def onda(x,y,mult,time):
    spread = 1.5

    ondas_array = [[0.05*mult,12*spread,-100,270],
                   [0.05*mult,5*spread,1700,-50],
                   [0.1*mult,40*spread,600,2000],
                   [0.1*mult,18*spread,360,400],
                   [0.2*mult,14*spread,360,200],
                   [0.3*mult,50*spread,1200,450],
                   [0.3*mult,25*spread,200,200],
                   ]

    result = 0
    for n in range(len(ondas_array)):
        armonic = ondas_array[n]
        k = 2*np.pi/armonic[1]
        w = k*vel
        t = time
        x0 = armonic[2]
        y0 = armonic[3]
        d = sqrt( ((x-x0)**2) + ((y-y0)**2))
        A = armonic[0]
    
        result +=A*sin(k*d-w*t)

    return result
def createWaveMap(size,maxvalue,seed):

    x = 0
    y = 0

    A = np.zeros(size)
    rows, colm= A.shape[0],A.shape[1]

    while x < rows:
        while y < colm:
            A[x][y] = int(min(round(onda(x,y,maxvalue,seed)),maxvalue))
            y+=1
        x += 1
        y = 0
    
    G = np.absolute(A)
    
    return G.astype(int)
if __name__ == '__main__':
    arr = createWaveMap((3,3),4)
    print arr

