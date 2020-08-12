import pyglet
from pyglet.window import key

import math
import concurrent.futures

from game import resources, util, constants, event
from game.terrain import terrain, data_handler
from game.objects import physics_object


class Player(physics_object.PhysicsObject, pyglet.event.EventDispatcher):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        self.terrain = terrain.Terrain()

        self.register_event_type("on_move")
        self.push_handlers(self.on_move)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self.key_handler, self.on_mouse_motion]


        self.move_speed = 1000.0
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

        self.handle_xy_movement(dt)
        self.handle_z_movement()

        
    def handle_xy_movement(self, dt):
        # Handle movement
        dpos = util.Vector(0,0)
        if self.key_handler[key.RIGHT] or self.key_handler[key.D]:
            dpos.x += 1
        if self.key_handler[key.LEFT] or self.key_handler[key.A]:
            dpos.x -= 1
        if self.key_handler[key.UP] or self.key_handler[key.W]:
            dpos.y += 1
        if self.key_handler[key.DOWN] or self.key_handler[key.S]:
            dpos.y -= 1

        if dpos:
            # Normalize to avoid fast diagonal movement
            dpos.normalize()
            
            speed = self.move_speed * dt

            # Check if tile can be moved to
            tilex = self.terrain.get_tile(self.world_x + dpos.x * (speed + self.width / 2), self.world_y, self.world_z)
            tilex_b = self.terrain.get_tile(self.world_x + dpos.x * (speed + self.width / 2), self.world_y, self.world_z - 1)
            tiley = self.terrain.get_tile(self.world_x, self.world_y + dpos.y * (speed + self.height / 2), self.world_z)
            tiley_b = self.terrain.get_tile(self.world_x, self.world_y + dpos.y * (speed + self.height / 2), self.world_z - 1)
            
            # Test x
            if tilex.material == 0 and tilex_b.material != 0:
                self.world_x += dpos.x * speed
            else:
                self.world_x += (abs(tilex.x - self.x) - (constants.TILE_SIZE / 2) - (self.width / 2)) * dpos.x

            # Test y
            if tiley.material == 0 and tiley_b.material != 0:
                self.world_y += dpos.y * speed
            else:
                self.world_y += (abs(tiley.y - self.y) - (constants.TILE_SIZE / 2) - (self.height / 2)) * dpos.y

            # Trigger move event
            self.dispatch_event("on_move")

    def handle_z_movement(self):
        if self.key_handler[key.Z]:
            self.world_z += 1
            self.dispatch_event("on_move")
        if self.key_handler[key.X]:
            self.world_z -= 1
            self.dispatch_event("on_move")
    
    def on_move(self):
        # TODO: This is being called twice every move, which causes the player to "jump" forward
        self.terrain.update(self.world_x, self.world_y, self.world_z)

    def on_mouse_motion(self, x, y, dx, dy):
        self.rotation = util.angle_between((self.x, self.y), (x, y))


    def collides_with(self, sprite):
        return util.distancesq((self.x, self.y), (sprite.x, sprite.y)) < ((self.width + sprite.width) / 2) ** 2