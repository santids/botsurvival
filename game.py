#Game module

class Game:
    def __init__(self):
        self.restart()

    def restart(self):
        self.turn = 1
        self.gamealive = True

        while self.gamealive:
            self.run_turn()
            self.turn += 1
        
    def run_turn(self):
        print self.turn
        
        if self.turn >= 100:
            self.gamealive = False
