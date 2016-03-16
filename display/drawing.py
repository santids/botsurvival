#draw forms
from math import sin,cos,pi


def hexagon((x0,y0),radius):
    verts = []
    alpha0 = pi/6
    alpha = pi/3
    for i in range(6):
        ang = alpha0 +alpha*i
        x = x0 + cos(ang)*radius
        y = y0 + sin(ang)*radius

        verts.append((x,y))
    return verts
