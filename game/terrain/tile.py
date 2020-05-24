import pyglet

from game import resources, constants


class Tile(pyglet.sprite.Sprite):
    def __init__(self, local_x, local_y, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, *args, **kwargs)

        self.local_x = local_x
        self.local_y = local_y

    def set_pos(self, x, y):
        self.x = x + self.local_x * self.width
        self.y = y + self.local_y * self.height
        print(x)
        print("Tile.set_pos()", self.x)
