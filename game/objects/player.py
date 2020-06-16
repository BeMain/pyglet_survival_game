import pyglet
from pyglet.window import key

import math
import concurrent.futures

from game import resources, util, constants, event
from game.terrain import terrain, data_handler
from game.objects import physics_object


class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        self.terrain = terrain.Terrain()

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self.key_handler]

        self.event_move = event.Event()

        self.move_speed = 500.0
        self.rotate_speed = 200.0

        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 2

        self.world_x = 0.0
        self.world_y = 0.0
        self.world_z = 0

        # Load player data
        self.load_data()
    
    def load_data(self):
        data = data_handler.read_player_data()
        if data:
            self.world_x = data["world_x"]
            self.world_y = data["world_y"]
            self.world_z = data["world_z"]
    
    def to_data(self):
        return {
            "world_x": self.world_x,
            "world_y": self.world_y,
            "world_z": self.world_z,
        }
    
    def save(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(data_handler.write_player_data, self.to_data())


    def update(self, dt):
        super(Player, self).update()

        # Handle movement
        dpos = util.Vector(0,0)
        if self.key_handler[key.RIGHT]:
            dpos.x += 1
        if self.key_handler[key.LEFT]:
            dpos.x -= 1
        if self.key_handler[key.UP]:
            dpos.y += 1
        if self.key_handler[key.DOWN]:
            dpos.y -= 1
        
        if dpos != util.Vector.ZERO():
            dpos.normalize()
            # Check if tile can be moved to
            speed = self.move_speed * dt
            tile = self.terrain.get_tile(self.world_x + dpos.x * (speed + self.width / 2), self.world_y + dpos.y * (speed + self.height / 2), self.world_z)
            if tile.material == 0:
                #if self.terrain.get_tile(self.world_x + dx * self.width, self.world_y + dx * self.height, self.world_z - 1).material != 0:
                self.world_x += dpos.x * speed
                self.world_y += dpos.y * speed
            else:
                # Snap to the edge of the tile
                self.world_x += (abs(tile.x - self.x) - (tile.width / 2) - (self.width / 2)) * dpos.x
                self.world_y += (abs(tile.y - self.y) - (tile.height / 2) - (self.height / 2)) * dpos.y
            
            # Trigger move event
            self.event_move()
        

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            self.world_z += 1
            self.event_move()
        if symbol == key.S:
            self.world_z -= 1
            self.event_move()

    def on_mouse_motion(self, x, y, dx, dy):
        self.rotation = util.angle_between((self.x, self.y), (x, y))


    def collides_with(self, sprite):
        return util.distancesq((self.x, self.y), (sprite.x, sprite.y)) < ((self.width + sprite.width) / 2) ** 2