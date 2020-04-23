import config
from startmenu import *
from menu import *
from os import path
import gamemode
from bee import ManualBee
from gamewindow import *


def main():
    game_window = GameWindow()

    #Map file to test
    garden_filename = path.join(config.gardens_folder, 'example.tmx')

    #Bee sprite to test
    bee_sprite = path.join(config.sprites_folder, 'test_bee.png')

    garden = Garden(garden_filename)
    bees = []

    bee1 = ManualBee(bee_sprite, 5)
    bee1.start((50, 50))
    bees.append(bee1)

    bee2 = ManualBee(bee_sprite, 3)
    bee2.start((100, 100))
    bees.append(bee2)

    play_game(game_window.screen, game_window.clock, 'test', garden, bees)


main()
