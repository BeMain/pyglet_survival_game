import pyglet
import math
from pyglet.window import key

from game import resources, util, constants
from game.objects import physics_object


class Player(physics_object.PhysicsObject):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(
            img=resources.player_image, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self.key_handler]

        self.move_speed = 500.0
        self.rotate_speed = 200.0

        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 2

        self.world_x = 0.0
        self.world_y = 0.0
        self.world_z = 0

    def update(self, dt):
        super(Player, self).update()

        redraw_needed = False

        # Handle rotation
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        # Handle movement
        speed = self.move_speed * dt
        if self.key_handler[key.RIGHT]:
            self.world_x += speed
            redraw_needed = True
        if self.key_handler[key.LEFT]:
            self.world_x -= speed
            redraw_needed = True
        if self.key_handler[key.UP]:
            self.world_y += speed
            redraw_needed = True
        if self.key_handler[key.DOWN]:
            self.world_y -= speed
            redraw_needed = True

        return redraw_needed
