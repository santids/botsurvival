from display import colors
from pygame.locals import FULLSCREEN

class Settings(dict):
    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        self.__dict__ = self

settings = Settings({
    #game play
    'max_turns':100,
    'map_size':81,
    'map_src':'assets/maps/default.npy',

    #display
    'scr_width':1100,
    'scr_height':800,
    'fullscreen':False,  #FULLSCREEN or 0
    'radius':7,
    'padding':30,
    'fps':24,

    #colors
    'back_color':colors.white,
    'walk_color':colors.green6,
    'obst_color':colors.black,
    'bot_color':colors.cyan5

    
    

    })

#test
if __name__ == '__main__':
    print settings['coca_cola']
