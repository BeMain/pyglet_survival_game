import pyglet

from game import resources, constants

# Updated for 3d-terrain
class Tile(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, *args, **kwargs)

        self.local_x = 0.0
        self.local_y = 0.0

    def set_pos(self, x, y, z):
        self.x = x + self.local_x * self.width
        self.y = y + self.local_y * self.height
        if z < 0:
            self.opacity = 255
            self.color = (50,50,50)
        elif z == 0:
            self.opacity = 255
        else:
            self.opacity = 128
            self.color = (150,150,200)

    def to_data(self):
        return {
            "local_x": self.local_x,
            "local_y": self.local_y,
            "color": self.color[0] / 255,
        }

    @classmethod
    def from_data(cls, data, *args, **kwargs):
        if data["color"] == 0:
            #return cls()
            return None
        else:
            t = cls(*args, **kwargs)

            t.local_x = data["local_x"]
            t.local_y = data["local_y"]

            color = data["color"] * 255
            t.color = (color, color, color)

            return t
