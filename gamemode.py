import pygame as pg
import config
from gamewindow import Camera

#Will be called from the main menu
def play_game(screen, clock, mode, garden, bees):
    if mode == 'whatever':
        # game = YourGameMode(screen, clock, garden, bees)
        pass

    elif mode == 'test':
        game = ManualTestGame(screen, clock, garden, bees)

    else:
        game = Game(screen, clock, garden, bees)

    game.show_splash_screen()
    game.play()


class Game:

    def __init__(self, screen, clock, garden, bees):
        self.screen = screen
        self.clock = clock
        self.garden = garden
        self.bees = bees
        self.garden_background = self.garden.build_background()
        self.garden_foreground = self.garden.build_foreground()
        self.garden_rect = self.garden_background.get_rect()
        self.all_sprites = pg.sprite.Group()
        self.all_bees = pg.sprite.Group()
        self.playing = True
        self.dt = 0
        self.camera = Camera(self.garden.width, self.garden.height)

        for bee in self.bees:
            self.all_bees.add(bee)
            self.all_sprites.add(bee)

    # The main game loop
    def play(self):
        self.initial_draw()
        while self.playing:
            self.dt = self.clock.tick(config.FPS) / 1000
            self.events()
            self.update()
            self.redraw()

    def update(self):
        # Update bee positions from VMs here
        for bee in self.bees:
            pass

        self.all_sprites.update()

        #Updates the camera position to follow the first (player) bee
        self.camera.update(self.bees[0])

    def redraw(self):
        #This currently redraws the entire screen, can be changed to redraw only certain areas later
        #to improve performance
        self.initial_draw()

    def initial_draw(self):
        #Draws the background to the screen, offset by the camera location
        self.screen.blit(self.garden_background, self.camera.apply_rect(self.garden_rect))

        #Draws all sprites to the screen, offset by the camera location
        for sprite in self.all_sprites:
            self.screen.blit(sprite._image, self.camera.apply(sprite))

        #Draws the foreground to the screen, offset by the camera location
        self.screen.blit(self.garden_foreground, self.camera.apply_rect(self.garden_rect))
        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

            #Redefine events in each game mode as necessary
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False

    def show_splash_screen(self):
        # Option to load a splash screen before the game. Vary by game mode? Show hints/controls?
        pass


class ManualTestGame(Game):
    def __init__(self, screen, clock, garden, bees):
        Game.__init__(self, screen, clock, garden, bees)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False

                #Redefined for manual controls
                elif event.key == pg.K_RIGHT:
                    self.bees[0].moveRight()
                elif event.key == pg.K_LEFT:
                    self.bees[0].moveLeft()
                elif event.key == pg.K_UP:
                    self.bees[0].moveUp()
                elif event.key == pg.K_DOWN:
                    self.bees[0].moveDown()
