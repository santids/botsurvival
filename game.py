#Game module

import sys, traceback
import pygame as pg
from pygame.locals import *
from display import colors,drawing
from hexboard import HexBoard
from random import choice

WIDTH = HEIGHT = 650
FPS = 24
KNUMS = [K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9]
RADIUS = 25
PAD = 30
MAXTURNS = 100

class Game:
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
        self.myloc = (3,3)
        self.draw_tile(self.myloc,colors.cyan5)
        pg.display.update()
        while self.gamealive:
            deltaTime = self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == QUIT:
                    close()
                elif event.type == MOUSEBUTTONDOWN: 
                    self.run_turn()
                    self.turn += 1
                    pg.display.update()
                elif event.type == KEYDOWN:
                    if event.key == K_r:
                        self.restart()
                        self.gamealive = False
                    if event.key == K_ESC:
                        close()
        close()
        
    def run_turn(self):
        print self.turn

        self.myloc = choice(self.board.locs_around(self.myloc,filter=['obstacle']))
        self.draw_board()
        self.draw_tile(self.myloc,colors.cyan5)
        
        
        if self.turn >= MAXTURNS:
            self.gamealive = False
            
    def draw_board(self):

        color = colors.gray5
        
        for loc in self.board.alllocs:
            if self.board.loc_type(loc) == 'walk':
                color = colors.gray6
            elif self.board.loc_type(loc) == 'obstacle':
                color = colors.black

            self.draw_tile(loc,color)
            
    def draw_tile(self,loc,color):
        cpoint = self.board.centerPoint(loc)
        hexa = drawing.hexagon(cpoint,RADIUS)
        pg.draw.polygon(self.screen,color,hexa)
        pg.draw.lines(self.screen,colors.black,True,hexa,1)
    
            
def close():
    print "Exit Game"
    pg.quit()
    sys.exit()
            
        

if __name__ == '__main__':
    try:
        game = Game()
    except Exception as ex:
        print type(ex), ex
        traceback.print_exc()
        close()
