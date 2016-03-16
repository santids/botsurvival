#Game module

import sys, traceback
import pygame as pg
from pygame.locals import *
from display import colors,drawing
from hexboard import HexBoard
import utils.vect2d as vect
import numpy as np

WIDTH = HEIGHT = 650
FPS = 24
KNUMS = [K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9]
RADIUS = 25
PAD = 30

class MapEditor:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption('BotSurvival!')
        self.screen.fill(colors.white)
        pg.display.update()
        self.clock = pg.time.Clock()
        
        self.restart()

    def restart(self):
        self.turn = 1
        self.gamealive = True
        self.board = HexBoard(RADIUS,(10,10))
        self.board.padding = PAD
        self.draw_board()
        pg.display.update()
        while self.gamealive:
            deltaTime = self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    cpoint = self.board.centerPoint((3,3))
                    print cpoint,event.pos,vect.dist(cpoint,event.pos)
                    for loc in self.board.alllocs:                        
                        if vect.dist(self.board.centerPoint(loc),event.pos) < RADIUS:
                            self.board.map[loc] = 1
                    print np.array2string(self.board.map,separator=',')
                            
            self.draw_board()
            pg.display.update()
                            
    def draw_board(self):

        color = colors.gray5
        
        for loc in self.board.alllocs:
            if self.board.loc_type(loc) == 'walk':
                color = colors.gray6
            elif self.board.loc_type(loc) == 'obstacle':
                color = colors.black

            cpoint = self.board.centerPoint(loc)
            hexa = drawing.hexagon(cpoint,RADIUS)
            pg.draw.polygon(self.screen,color,hexa)
            pg.draw.lines(self.screen,colors.black,True,hexa,1)
            
        

if __name__ == '__main__':
    try:
        game = MapEditor()
    except Exception as ex:
        print type(ex), ex
        traceback.print_exc()
        pg.quit()
        sys.exit()
