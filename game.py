#Game module

import sys, traceback
import pygame as pg
from pygame.locals import *
from display import colors,drawing
from hexboard import HexBoard
from random import choice, randint, gauss
from settings import settings
from math import floor

KNUMS = [K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9]


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((settings.scr_width,settings.scr_height),settings.fullscreen)
        pg.display.set_caption('BotSurvival!')
        self.screen.fill(settings.back_color)
        pg.display.update()
        self.clock = pg.time.Clock()
        
        self.restart()

    def restart(self):
        self.turn = 1
        self.gamealive = True
        self.board = HexBoard(settings.radius,(settings.map_size,settings.map_size))
        self.board.padding = settings.padding
        self.draw_board()
        self.bots = []
        size = self.board.size[0]-1
        for i in range(150):
            x = int(floor(max(0,min(size,gauss(size/2,10)))))
            y = int(floor(max(0,min(size,gauss(size/2,10)))))
            self.bots.append((x,y))
        pg.display.update()
        while self.gamealive:
            deltaTime = self.clock.tick(settings.fps)
            pg.display.set_caption('BotSurvival! '+str(round(1.0/deltaTime*1000)))
            self.dirty_rects = []
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
                    if event.key == K_ESCAPE:
                        close()
        self.restart()
        close()
        
    def run_turn(self):
        print self.turn
        nl = []
        for loc in self.bots:
            try:
                self.draw_tile(loc,self.get_color(loc))
                loc = choice(self.board.locs_around(loc,['water','mountain']))
                nl.append(loc)
                self.draw_tile(loc,colors.cyan5,settings.radius*0.6,False)
            except IndexError:
                pass
                
        self.bots = nl

        
        if self.turn >= settings.max_turns:
            self.gamealive = False
            
    def draw_board(self):

        color = colors.gray5
        
        for loc in self.board.alllocs:
            #print self.board.map[loc]
            

            color = self.get_color(loc)
            self.draw_tile(loc,color)
            
    def draw_tile(self,loc,color,radius=settings.radius,contorno=True):
        cpoint = self.board.centerPoint(loc)
        hexa = drawing.hexagon(cpoint,radius)

        pg.draw.polygon(self.screen,color,hexa)
        if contorno:
            pg.draw.lines(self.screen,colors.black,True,hexa,1)
    def get_color(self,loc):
        loctype = self.board.loc_type(loc)
        if loctype== 'walk':
            if loc[1] % 2 == 0:
                return colors.green7
            else:
                return settings.walk_color
        elif loctype == 'obstacle':
            return settings.obst_color
        elif loctype == 'water':
            return colors.blue8
        elif loctype == 'hills':
            return  colors.brown8
        elif loctype == 'plains':
            return  colors.green4
        elif loctype == 'mountain':
            return colors.brown4
        else:
            raise ValueError('not color for that loc: '+str(loc)+loctype)


    
            
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

