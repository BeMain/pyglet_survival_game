import pyglet
import math
from pyglet.window import key

from game import resources, util, constants
from game.terrain import terrain
from game.objects import physics_object


class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        self.terrain = terrain.Terrain()

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

        # Handle movement
        dx = 0
        dy = 0
        if self.key_handler[key.RIGHT]:
            dx += 1
        if self.key_handler[key.LEFT]:
            dx -= 1
        if self.key_handler[key.UP]:
            dy += 1
        if self.key_handler[key.DOWN]:
            dy -= 1
        
        # Check if tile can be moved to
        speed = self.move_speed * dt
        tile = self.terrain.get_tile(self.world_x + dx * (speed + self.width / 2), self.world_y + dy * (speed + self.height / 2), self.world_z)
        if tile.material == 0:
            #if self.terrain.get_tile(self.world_x + dx * self.width, self.world_y + dx * self.height, self.world_z - 1).material != 0:
            self.world_x += dx * speed
            self.world_y += dy * speed
            redraw_needed = True
        else:
            # Snap to the edge of the tile
            self.world_x += (abs(tile.x - self.x) - (tile.width / 2) - (self.width / 2)) * dx
            self.world_y += (abs(tile.y - self.y) - (tile.height / 2) - (self.height / 2)) * dy
            redraw_needed = True
        

        return redraw_needed

    def on_key_press(self, symbol, modifiers):
        redraw_needed = False

        if symbol == key.W:
            self.world_z += 1
            redraw_needed = True
        if symbol == key.S:
            self.world_z -= 1
            redraw_needed = True
        
        return redraw_needed

    def on_mouse_motion(self, x, y, dx, dy):
        self.rotation = util.angle_between((self.x, self.y), (x, y))

    def collides_with(self, sprite):
        return util.distancesq((self.x, self.y), (sprite.x, sprite.y)) < ((self.width + sprite.width) / 2) ** 2