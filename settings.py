from display import colors
from pygame.locals import FULLSCREEN

class Settings(dict):
    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        self.__dict__ = self

settings = Settings({
    #game play
    'max_turns':500,

    #map settings
    'map_size':200,
    'map_src':'assets/maps/default.npy',
    'map_seed':216,

    #display
    'view_width':40,
    'view_height':30,
    'scr_width':800,
    'scr_height':600,
    'fullscreen':False , #FULLSCREEN or 0
    'radius':9,
    'padding':30,
    'fps':60,

    #colors
    'back_color':colors.white,
    'walk_color':colors.green6,
    'obst_color':colors.black,
    'bot_color':colors.cyan5

    
    

    })

#test
if __name__ == '__main__':
    print settings['coca_cola']
