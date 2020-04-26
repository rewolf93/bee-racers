from os import path

"""Game Configuration"""
game_folder = path.dirname(__file__)
assets_folder = path.join(game_folder, 'assets')
gardens_folder = path.join(assets_folder, 'maps')
audio_folder = path.join(assets_folder, 'audio')
sprites_folder = path.join(assets_folder, 'sprites')

bee_sprite = None
garden_filename = None
bee_filename = None
game_mode = None

screen_height = 500
screen_width = 500
map_height = 0
map_width = 0
game_title = "Bee Racers"
FPS = 60
