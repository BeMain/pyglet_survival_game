import pyglet
from pyglet.window import key

import time
import math

from game import constants, resources, util
from game.objects import player
from game.terrain import terrain, tile


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(constants.SCREEN_WIDTH,
                                         constants.SCREEN_HEIGHT, vsync=False, *args, **kwargs)
        self.running = True
        self.last_scheduled_update = time.time()

        self.main_batch = pyglet.graphics.Batch()

        self.main_group = pyglet.graphics.Group()
        self.objects_group = pyglet.graphics.OrderedGroup(5, parent=self.main_group)

        self.terrain = terrain.Terrain()
        self.player = player.Player(self.terrain, batch=self.main_batch, group=self.objects_group)
        self.fps_display = self.init_fps_display()

        self.game_objects = [self.player]

        # Register event handlers
        for obj in self.game_objects:
            for handler in obj.event_handlers:
                self.push_handlers(handler)

        # Init tile.Tile so they can render properly
        tile.Tile.init_rendering(self.main_batch, self.main_group)

    def init_fps_display(self):
        display = pyglet.window.FPSDisplay(self)
        display.label.color = (255,255,255,255)

        return display

    def render(self):
        self.clear()

        # Draw background
        resources.background_image.blit(0,0)

        self.main_batch.draw()
        self.fps_display.draw()

        self.flip()

    def update(self, dt):
        redraw_needed = False

        # Update all objects
        for obj in self.game_objects:
            if obj.update(dt):
                redraw_needed = True

        # Only redraw terrain if needed
        if redraw_needed:
            self.terrain.update(self.player.world_x, self.player.world_y, self.player.world_z)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.running = False
            
        if self.player.on_key_press(symbol, modifiers):
            self.terrain.update(self.player.world_x, self.player.world_y, self.player.world_z)

    def on_mouse_press(self, x, y, button, modifiers):
        x = util.clamp(x, 0, constants.SCREEN_WIDTH)
        y = util.clamp(y, 0, constants.SCREEN_HEIGHT)

        world_x = self.player.world_x - constants.SCREEN_WIDTH / 2 + x
        world_y = self.player.world_y - constants.SCREEN_HEIGHT / 2 + y
        
        tile = self.terrain.get_tile(world_x, world_y, self.player.world_z)
        tile.set_material(0)
        

    def run(self):
        self.last_scheduled_update = time.time()

        # Initialization
        cursor = self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR)
        self.set_mouse_cursor(cursor)

        # First draw
        resources.background_image.blit(0,0)
        self.terrain.update(self.player.world_x, self.player.world_y, self.player.world_z)

        # Main loop
        while self.running:
            if time.time() - self.last_scheduled_update > 1 / constants.FPS:
                self.update(time.time() - self.last_scheduled_update)
                self.last_scheduled_update = time.time()
            self.render()

            event = self.dispatch_events()
            
            if event: print("Event:", event)
