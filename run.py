#Run game
#author: Santiago Dandois

from game import Game

def main():
    try:
        game = Game()
    except Exception as ex:
        print ex


if __name__ == '__main__':
    main()
