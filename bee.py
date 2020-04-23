from physics import Moveable, Physical
import pygame as pg
import pickle as pkl
import numpy as np



class ManualBee(Moveable):

    def __init__(self, spritepath: str, distance: int):
        Moveable.__init__(self, spritepath)
        self.distance = distance

    def start(self, startpos: (int, int)):
        start_x = float(startpos[0])
        start_y = float(startpos[1])
        self._location = np.array([start_x, start_y])
        self.pos = (start_x, start_y)

    def reset(self):
        self._image = self._originalimage
        self.rect = self.image.get_rect()
        self.old_rect = self.rect

        self.pos = np.array([0., 0])

    def update(self):
        Moveable.update(self)

    def tick(self):
        pass

    def get_loc(self):
        return tuple(self._location)

    def moveUp(self):
        self._location = np.array([self.pos[0], self.pos[1]-self.distance])

    def moveDown(self):
        self._location = np.array([self.pos[0], self.pos[1]+self.distance])

    def moveLeft(self):
        self._location = np.array([self.pos[0]-self.distance, self.pos[1]])

    def moveRight(self):
        self._location = np.array([self.pos[0]+self.distance, self.pos[1]])
