import pyglet

from game import resources, constants

class Tile(pyglet.sprite.Sprite):
    BATCH = None
    GROUPS = {}

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, usage="static", *args, **kwargs)

        self.local_x = 0.0
        self.local_y = 0.0
    
    @staticmethod
    def init_rendering(batch, group):
        print("Main group: ", group)
        Tile.BATCH = batch
        Tile.GROUPS = {
            -1 : pyglet.graphics.OrderedGroup(-3, parent=group),
            0 : pyglet.graphics.OrderedGroup(-2, parent=group),
            1 : pyglet.graphics.OrderedGroup(-1, parent=group),
        }

    def set_pos(self, x, y, z):
        new_x = x + self.local_x * self.width
        new_y = y + self.local_y * self.height
        
        # Check bounds
        if new_x < -constants.TILE_SIZE // 2 or new_x > constants.SCREEN_WIDTH + constants.TILE_SIZE // 2  or new_y < -constants.TILE_SIZE // 2 or new_y > constants.SCREEN_HEIGHT + constants.TILE_SIZE // 2:
            # Don't render if sprite is not on screen
            self.batch = None
        else:
            self.batch = self.BATCH

            self.x = new_x
            self.y = new_y
        
            # Change appearance depending on what layer we are on
            self.group = self.GROUPS[z]
            if z == -1:
                self.opacity = 255
                self.color = (50,50,50)
            elif z == 0:
                self.opacity = 255
            elif z == 1:
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
