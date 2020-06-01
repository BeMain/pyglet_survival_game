import pyglet

from game import resources, constants

class Tile(pyglet.sprite.Sprite):
    BATCH = None
    GROUPS = {}

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, usage="static", *args, **kwargs)

        self.material = 0

        self.local_x = 0
        self.local_y = 0
    
    @staticmethod
    def init_rendering(batch, group):
        print("Main group: ", group)
        Tile.BATCH = batch
        Tile.GROUPS = {
            -1 : pyglet.graphics.OrderedGroup(0, parent=group),
            0 : pyglet.graphics.OrderedGroup(1, parent=group),
            1 : pyglet.graphics.OrderedGroup(2, parent=group),
        }

    def set_pos(self, x, y, z):
        new_x = x + self.local_x * self.width
        new_y = y + self.local_y * self.height

        # Check bounds
        if (new_x < -constants.TILE_SIZE // 2) or (new_x > constants.SCREEN_WIDTH + constants.TILE_SIZE // 2) or (new_y < -constants.TILE_SIZE // 2) or (new_y > constants.SCREEN_HEIGHT + constants.TILE_SIZE // 2):
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
                self.color = (75,75,75)
            elif z == 0:
                self.opacity = 255
                self.color = (150,150,150)
            elif z == 1:
                self.opacity = 128
                self.color = (255,255,255)

    def set_material(self, material):
        self.material = material
        if material == 0:
            self.batch = None

    def to_data(self):
        return {
            "local_x": self.local_x,
            "local_y": self.local_y,
            "material": self.material,
        }

    @classmethod
    def from_data(cls, data):
        t = cls()

        t.local_x = data["local_x"]
        t.local_y = data["local_y"]

        color = data["material"] * 255
        t.color = (color, color, color)
        
        t.material = data["material"]

        return t
