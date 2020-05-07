import numpy as np
import pygame as pg

CALC_PRECISION = 10


class Physical(pg.sprite.Sprite):

    def __init__(self, game, spritepath: str):
        pg.sprite.Sprite.__init__(self, game.all_sprites)
        image = pg.image.load(spritepath).convert_alpha()
        self.image = pg.transform.scale(image, (50, 50))
        self._originalimage = self.image
        self.rect = self.image.get_rect()
        self.old_rect = self.rect
        self.pos = (0, 0)
        self.theta = 0

    @classmethod
    def rotateaxis(cls, xy, heading):
        '''
        '''
        basis = np.array([(np.cos(heading), -np.sin(heading)),
                          (np.sin(heading), np.cos(heading))])
        calc = xy*basis
        return np.around(np.sum(calc, axis=1), decimals=CALC_PRECISION)

    @classmethod
    def getangle(cls, x1, x2, y1, y2):
        dx = x2 - x1
        dy = y2 - y1
        if dx < 0:
            if dy < 0:
                heading = np.arctan(dy/dx) - np.pi
            else:
                heading = np.arctan(dy/dx) + np.pi
        elif dx == 0:
            if dy == 0:
                pass
            elif dy > 0:
                heading = np.pi/2
            else:
                heading = np.pi/-2
        else:
            heading = np.arctan(dy/dx)

        return heading


class Moveable(Physical):

    def __init__(self, game, spritepath: str):
        Physical.__init__(self, game, spritepath)

    def update(self):
        self.old_rect.center = self.rect.center
        self.pos = self.get_loc()
        rotation = -(self.theta / np.pi) * 180 - 90
        self.image = pg.transform.rotate(self._originalimage, rotation)
        self.rect.center = self.pos


class Immoveable(Physical):

    def __init__(self, game, spritepath: str):
        Physical.__init__(self, game, spritepath)

    def update(self):
        pass
