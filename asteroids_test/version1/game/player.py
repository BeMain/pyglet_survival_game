import math
import pyglet
from pyglet.window import key
from . import physicalobject, resources


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)

        self.thrust = 300.0
        self.rotate_speed = 200.0

        self.key_handler = key.KeyStateHandler()

        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible=False


    def update(self, dt):
        super(Player, self).update(dt)

        # Handle rotation
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        # Handle movement
        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt

            self.velocity_x += force_x
            self.velocity_y += force_y
            
            # Move and rotate engine flame
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False
    
    
    def delete(self):
        self.engine_sprite.delete()
        super(Player, self).delete()