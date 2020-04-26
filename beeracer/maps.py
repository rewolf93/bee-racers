import pytmx
import pygame as pg


class Garden:
    def __init__(self, filename: str):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render_background(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if layer.name != "Foreground":
                if isinstance(layer, pytmx.TiledTileLayer):
                    print("Drawing " + layer.name)
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                y * self.tmxdata.tileheight))

    def render_foreground(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if layer.name == "Foreground":
                if isinstance(layer, pytmx.TiledTileLayer):
                    print("Drawing " + layer.name)
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def build_background(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render_background(temp_surface)
        return temp_surface

    def build_foreground(self):
        temp_surface = pg.Surface((self.width, self.height), pg.SRCALPHA, 32)
        self.render_foreground(temp_surface)
        return temp_surface
