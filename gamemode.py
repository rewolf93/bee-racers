import pygame as pg
import config
import startmenu
from maps import Map


def play_game(mode):

    #if mode == "Pollen Hunt":
    game = PollenHunt()
    # Add other game modes here

    game.show_splash_screen()
    game.new()
    game.run()


class PollenHunt:

    # Creates the game window
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((config.screen_width, config.screen_height))
        pg.display.set_caption(config.game_title + " - Pollen Hunt")
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.screen = pg.display.set_mode((self.map.width, self.map.height))

    # Load map and bee data
    def load_data(self):
        self.map = Map(config.map_filename)
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        # Instantiate bee(s) here

    # The main game loop
    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(config.FPS) / 1000
            self.events()
            self.update()
            self.draw()
            if not self.running:
                pg.quit()
                startmenu.create_start_menu()

    def update(self):
        # Update bee positions here
        self.all_sprites.update()

    def draw(self):
        self.screen.blit(self.map_img, self.map_rect)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                #elif event.key == whatever:
                    # Other key effects here

    def show_splash_screen(self):
        # Option to load a splash screen before the game. Vary by game mode? Show hints/controls?
        pass
