import pyglet

from game import resources, constants, style, event

class Tile(pyglet.sprite.Sprite):
    BATCH = None
    GROUPS = {}

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, usage="static", *args, **kwargs)

        self.event_update = event.Event()

        self.material = 0

        self.tile_x = 0
        self.tile_y = 0
    
    @staticmethod
    def init_rendering(batch, group):
        Tile.BATCH = batch
        Tile.GROUPS = {
            -1 : pyglet.graphics.OrderedGroup(0, parent=group),
            0 : pyglet.graphics.OrderedGroup(1, parent=group),
            1 : pyglet.graphics.OrderedGroup(2, parent=group),
        }


    def set_pos(self, x, y, z):
        new_x = x + self.tile_x * self.width
        new_y = y + self.tile_y * self.height

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
            self.color = style.layers[z]["color"]
            self.opacity = style.layers[z]["opacity"]

    def set_material(self, material):
        self.material = material
        if material == 0:
            self.batch = None
        else:
            self.batch = self.BATCH
        
        # Trigger update
        self.event_update(self.tile_x, self.tile_y)

    def to_data(self):
        return {
            "tile_x": self.tile_x,
            "tile_y": self.tile_y,
            "material": self.material,
        }

    @classmethod
    def from_data(cls, data):
        t = cls()

        t.tile_x = data["tile_x"]
        t.tile_y = data["tile_y"]

        color = data["material"] * 255
        t.color = (color, color, color)
        
        t.material = data["material"]

        return t
