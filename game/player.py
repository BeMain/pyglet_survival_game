import pyglet
import math
from pyglet.window import key

from . import physics_object, resources, util, constants


class Player(physics_object.PhysicsObject):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(
            img=resources.player_image, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

        self.move_speed = 100.0
        self.rotate_speed = 200.0

    def update(self, dt):
        super(Player, self).update()

        # Handle rotation
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        # Handle movement
        if self.key_handler[key.UP]:
            rot_rad = -math.radians(self.rotation)

            dx = math.cos(rot_rad) * self.move_speed * dt
            dy = math.sin(rot_rad) * self.move_speed * dt

            self.velx = dx
            self.vely = dy
        else:
            self.velx = 0
            self.vely = 0
    

