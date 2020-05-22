import pyglet
import math
from pyglet.window import key
from game import resources


class Tile(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.tile_image, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self.key_handler]

    def update(self, dt, player):
        super(Tile, self).update()

        # TODO: Improve movement and fix a different way to access player variables
        # Handle movement
        if player.key_handler[key.UP]:
            rot_rad = -math.radians(player.rotation)

            self.x += math.cos(rot_rad) * player.move_speed * dt
            self.y += math.sin(rot_rad) * player.move_speed * dt
