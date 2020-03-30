import numpy as np
import pygame as pg

CALC_PRECISION = 10


class Physical(pg.sprite.Sprite):

    def __init__(self, spritepath: str):
        pg.sprite.Sprite.__init__(self, self.groups)
        fle = open(spritepath, 'rb')
        image = pg.image.load(fle.read()).convert_alpha()
        fle.close()
        self._image = pg.transform.scale(image, (50, 50))
        self._originalimage = self._image
        self.rect = self.image.get_rect()
        self.old_rect = self.rect
        self.pos = (0, 0)

    @classmethod
    def rotateaxis(cls, xy, heading):
        '''
        '''
        basis = np.array([(np.cos(heading), -np.sin(heading)),
                          (np.sin(heading), np.cos(heading))])
        calc = xy*basis
        return np.around(np.sum(calc, axis=1), decimals=CALC_PRECISION)


class Moveable(Physical):

    def __init__(self, spritepath: str):
        Physical.__init__(self, spritepath)

    def update(self):
        self.old_rect.center = self.rect.center
        self.pos = self.get_loc()
        rotation = -(self.theta / np.pi) * 180
        self.image = pg.transform.rotate(self._originalimage, rotation)
        self.rect.center = self.pos


class Immoveable(Physical):

    def __init__(self, spritepath: str):
        Physical.__init__(self, spritepath)

    def update(self):
        pass