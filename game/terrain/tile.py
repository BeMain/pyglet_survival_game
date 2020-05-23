import pyglet

from game import resources, constants


class Tile(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, *args, **kwargs)
