import config
import pygame as pg


#Creates the window in which the game and menus run
class GameWindow:
    def __init__(self):
        self.width = config.screen_width
        self.height = config.screen_height
        pg.init()
        pg.display.set_caption(config.game_title)
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

        #How often a held key registers, only needed for manual controls
        pg.key.set_repeat(1, 1)


#Scrolling camera that enables maps to be larger than the window
class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    #Offsets where the sprite is drawn relative to the camera location
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    #Offsets where the surface is drawn relative to the camera location
    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    #Updates the camera location
    def update(self, target):
        x = -target.rect.x + int(config.screen_width / 2)
        y = -target.rect.y + int(config.screen_height / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - config.screen_width), x)  # right
        y = max(-(self.height - config.screen_height), y)  # bottom

        self.camera = pg.Rect(x, y, self.width, self.height)