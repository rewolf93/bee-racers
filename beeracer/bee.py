import pygame as pg
import pickle as pkl
import numpy as np
from beeracer.codeParserLambda import *
from beeracer.physics import Moveable, Physical


class Bee(Moveable):

    def __init__(self, spritepath: str, assemblypath=None, binary=None):
        if assemblypath is None and binary is None:
            raise Exception("Must provide assemblypath or binary")

        Moveable.__init__(self, spritepath)

        if binary is None:
            binary = CodeParser(assemblypath)
        self._binary = binary
        self.__vm = None

        self._max_acceleration = 120
        self._velocity = np.array([0., 0])
        self._location = np.array([0., 0])
        self._phi = 0

    def start(self, startpos: (int, int)):
        start_x = float(startpos[0])
        start_y = float(startpos[1])
        self._location = np.array([start_x, start_y])
        self.pos = (start_x, start_y)

    def reset(self):
        self._image = self._originalimage
        self.rect = self.image.get_rect()
        self.old_rect = self.rect

        self.__vm = None
        self._velocity = np.array([0., 0])
        self._location = np.array([0., 0])
        self.pos = (0, 0)

    def tick(self):
        return
        self.__vm.tick()
        if self.__vm.checkflag():
            pass

    def save(self, filepath: str):
        temp = self.__vm
        self.__vm = None
        with open(filepath, 'wb') as fle:
            pkl.dump(self, fle)
        self.__vm = temp

    def move(self, dt=0.05):
        self._theta += self._phi
        arry = np.array([self._acceleration, self._velocity])
        timevector = np.array([float(dt**2), dt])
        calc = arry*timevector
        ds = np.sum(calc)
        dv = self.acceleration * dt
        self._velocity += dv
        real_ds = Physical.rotateaxis(np.array([ds, 0]), self.theta)
        self._location += real_ds
        self.update()

    def get_loc(self):
        return tuple(self._location)

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
