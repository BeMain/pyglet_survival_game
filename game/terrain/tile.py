import pyglet
import math
from pyglet.window import key
from game import resources, constants


class Tile(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self.key_handler]

        self.dead = False

        self.velx = 0.0
        self.vely = 0.0

    def update(self, dt):
        # Check if outside screen
        if self.x < 0 or self.x > constants.SCREEN_WIDTH or self.y < 0 or self.y > constants.SCREEN_HEIGHT:
            # Mark for removal
            self.dead = True
