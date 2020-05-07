import pickle as pkl
import numpy as np
from beeracer.codeParserLambda import CodeParser
from beeracer.physics import Moveable, Physical
from beeracer.settings import *
from beeracer.sprites import Pollen



class Bee(Moveable):

    def __init__(self, game, spritepath: str, dt=0.05, assemblypath=None, binary=None, pos=None):
        if assemblypath is None and binary is None:
            raise Exception("Must provide assemblypath or binary")

        Moveable.__init__(self, game, spritepath)
        self.game = game

        self.__vm = CodeParser(assemblypath)

        self._max_acceleration = 120
        self._velocity = 0
        self._location = np.array([0., 0])
        self._phi = 0
        self._dt = dt
        self._acceleration = 0
        self.pollen = 0
        if pos:
            self.start(pos)

    def start(self, startpos: (int, int)):
        start_x = float(startpos[0])
        start_y = float(startpos[1])
        self._location = np.array([start_x, start_y])
        self.pos = (start_x, start_y)

    def reset(self):
        self.image = self._originalimage
        self.rect = self.image.get_rect()
        self.old_rect = self.rect

        self.__vm = None
        self._velocity = np.array([0., 0])
        self._location = np.array([0., 0])
        self.pos = (0, 0)

    def update(self):
        self.__vm.tick()

        if self.__vm.checkMemory(1)*np.pi/180 != self.theta:
            self.theta = self.__vm.checkMemory(1) * np.pi / 180

        current_speed = self.__vm.checkMemory(2)
        desired_speed = self.__vm.checkMemory(0)
        speed_delta = round(desired_speed - current_speed)

        if speed_delta != 0:
            if abs(speed_delta) > self._max_acceleration*self._dt + current_speed:
                self.acceleration = self._max_acceleration * (speed_delta / abs(speed_delta))
            else:
                self.acceleration = speed_delta / self._dt
        else:
            self.acceleration = 0

        self.move()

        speed = self._velocity
        self.__vm.setMemory(loc=5, value=self.pos[0])
        self.__vm.setMemory(loc=6, value=self.pos[1])
        self.__vm.setMemory(loc=2, value=speed)

        closestpollen = 0
        pollenheading = 0
        for sprite in self.game.pollen:
            dist = ((sprite.rect.center[0] - self.pos[0]) ** 2 +
                    ((sprite.rect.center[1] - self.pos[1]) ** 2) ** 0.5)
            if closestpollen == 0 or dist < closestpollen:
                closestpollen = dist
                pollenheading = int(Physical.getangle(
                    self.pos[0], sprite.rect.center[0],
                    self.pos[1], sprite.rect.center[1]
                ) * 180 / np.pi)
        self.__vm.setMemory(loc='pollenhead', value=pollenheading)

        Moveable.update(self)

    def save(self, filepath: str):
        temp = self.__vm
        self.__vm = None
        with open(filepath, 'wb') as fle:
            pkl.dump(self, fle)
        self.__vm = temp

    def move(self):
        self.theta += self._phi
        arry = np.array([self.acceleration, self._velocity])
        timevector = np.array([float(self._dt**2), self._dt])
        calc = arry*timevector
        ds = np.sum(calc)
        dv = self.acceleration * self._dt
        self._velocity += dv
        #print(f'theta: {self.theta}')
        real_ds = Physical.rotateaxis(np.array([ds, 0]), self.theta)
        self._location += real_ds

    def get_loc(self):
        return tuple(self._location)

    def draw_pollen(self):
        pollen = self.__vm.checkMemory('pollencount')
        if pollen > 60:
            col = RED
        elif pollen > 30:
            col = YELLOW
        else:
            col = GREEN
        width = int(self.rect.width * pollen / PLAYER_MAX_POLLEN)
        self.pollen_bar = pg.Rect(0, 0, width, 10)
        if pollen > 0:
            pg.draw.rect(self.image, col, self.pollen_bar)

    def add_pollen(self, amount):
        pollen = self.__vm.checkMemory('pollencount')
        pollen += amount
        if pollen == PLAYER_MAX_POLLEN:
            self.game.quit()
        self.__vm.setMemory(loc='pollencount', value=pollen)

    def get_pollen(self):
        return self.__vm.checkMemory('pollencount')


class ManualBee(Moveable):

    def __init__(self, game, spritepath: str, distance: int):
        Moveable.__init__(self, game, spritepath)
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
