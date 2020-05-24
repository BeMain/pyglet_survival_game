import pyglet

from game import resources, constants


class Tile(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, *args, **kwargs)

        self.local_x = 0.0
        self.local_y = 0.0

    def set_pos(self, x, y):
        self.x = x + self.local_x * self.width
        self.y = y + self.local_y * self.height

    def to_data(self):
        return {
            "local_x": self.local_x,
            "local_Y": self.local_y,
            "color": self.color[0] / 255,
        }

    @classmethod
    def from_data(cls, data, *args, **kwargs):
        t = cls(*args, **kwargs)

        t.local_x = data["local_x"]
        t.local_y = data["local_y"]

        color = data["color"] * 255
        t.color = (color, color, color)

        return t
