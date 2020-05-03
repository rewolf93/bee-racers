#Much of this code have been derived from a pygame/tiled tutorial on youtube
#and been modified to our purposes
#tutorials can be found on KidsCanCode youtube channel
#https://www.youtube.com/channel/UCNaPQ5uLX5iIEHUCLmfAgKg
import pygame as pg
import sys
from os import path
from beeracer.settings import *
from beeracer.sprites import *
from beeracer.tilemap import *

#def draw_player_pollen(surf, x, y, pct):
#	if pct < 0:
#		pct = 0
#	BAR_LENGTH = 100
#	BAR_HEIGHT = 20
#	fill = pct * BAR_LENGTH
#	outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
#	fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
#	if pct > 0.6:
#		col = RED
#	elif pct > 0.3:
#		col = YELLOW
#	else:
#		col = GREEN
#	pg.draw.rect(surf, col, fill_rect)
#	pg.draw.rect(surf, WHITE, outline_rect, 2)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'assets/sprites')
        map_folder = path.join(game_folder, 'assets/maps')
        self.map = TiledMap(path.join(map_folder, '1st_Map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.pollen_images = {}
        for pollen in POLLEN_IMAGES:
        	self.pollen_images[pollen] = pg.image.load(path.join(img_folder, POLLEN_IMAGES[pollen])).convert_alpha()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.pollen = pg.sprite.Group()
        #for row, tiles in enumerate(self.map.data):
        #	for col, tile in enumerate(tiles):
        #		if tile == '1':
        #			Wall(self, col, row)
        #		if tile == 'P':
        #			self.player = Player(self, col, row)
        for tile_object in self.map.tmxdata.objects:
        	obj_center = vec(tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height / 2)
        	if tile_object.name == 'player':
        		self.player = Player(self, obj_center.x, obj_center.y)
        	if tile_object.name == 'wall':
        		Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
        	if tile_object.name == 'Flower':
        		Pollen(self, obj_center, 'pollen')
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.spritecollide(self.player, self.pollen, False)
        for hit in hits:
        	if hit.type == 'pollen' and self.player.pollen < PLAYER_MAX_POLLEN:
        		hit.kill()
        		self.player.add_pollen(POLLEN_AMOUNT)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite in self.all_sprites:
        	if isinstance(sprite, Player):
        		sprite.draw_pollen()
        	self.screen.blit(sprite.image, self.camera.apply(sprite))
        	if self.draw_debug:
        		pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect),1)
        if self.draw_debug:
        	for wall in self.walls:
        		pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect),1)
        #pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        #draw_player_pollen(self.screen, 10, 10, self.player.pollen / PLAYER_MAX_POLLEN)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                	self.draw_debug = not self.draw_debug


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
