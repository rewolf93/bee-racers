import config
import pygame
import os
from gamemode import *
from gamewindow import *
from maps import *
#from startmenu import *
#from menu import *
from bee import *


def main():
    game_window = GameWindow()

    #Map file to test
    garden_filename = os.path.join(config.gardens_folder, 'example.tmx')

    #Bee sprite to test
    bee_sprite = os.path.join(config.sprites_folder, 'test_bee.png')

    garden = Garden(garden_filename)
    bees = []

    bee1 = ManualBee(bee_sprite, 5)
    bee1.start((50, 50))
    bees.append(bee1)

    bee2 = Bee(bee_sprite, assemblypath=os.path.join(config.assets_folder, 'assembly', 'basicbee.txt'))
    bee2.start((100, 100))
    bees.append(bee2)

    play_game(game_window.screen, game_window.clock, 'test', garden, bees)


main()
