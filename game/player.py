import pyglet
import math
from pyglet.window import key

from . import physics_object, resources


class Player(physics_object.PhysicsObject):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(
            img=resources.player_image, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

        self.acceleration = 2.0
        self.max_speed = 10.0
        self.rotate_speed = 200.0
        self.brake_speed = 3.0

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

            dpos = min(self.acceleration,
                       self.max_speed -
                       (math.sqrt((self.velx ** 2) + (self.vely ** 2)))) * dt

            dx = math.cos(rot_rad) * dpos
            dy = math.sin(rot_rad) * dpos

            self.velx += dx
            self.vely += dy
        else:
            rot_rad = -math.radians(self.rotation)

            dpos = min(self.brake_speed, math.sqrt(
                (self.velx ** 2) + (self.vely ** 2))) * dt

            dx = math.cos(rot_rad) * dpos
            dy = math.sin(rot_rad) * dpos

            self.velx -= dx
            self.vely -= dy
