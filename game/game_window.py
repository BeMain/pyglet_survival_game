import pyglet
from pyglet.window import key

import time
import math

from game import constants
from game.objects import player
from game.terrain import terrain


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(constants.SCREEN_WIDTH,
                                         constants.SCREEN_HEIGHT, vsync=False, *args, **kwargs)
        self.running = True
        self.last_scheduled_update = time.time()

        self.main_batch = pyglet.graphics.Batch()

        self.terrain_group = pyglet.graphics.OrderedGroup(0)
        self.objects_group = pyglet.graphics.OrderedGroup(1)

        self.player_sprite = player.Player(
            batch=self.main_batch, group=self.objects_group)
        self.terrain = terrain.Terrain(
            batch=self.main_batch, group=self.terrain_group)
        self.fps_display = pyglet.window.FPSDisplay(self)

        self.game_objects = [self.player_sprite]

        # Register event handlers
        for obj in self.game_objects:
            for handler in obj.event_handlers:
                self.push_handlers(handler)

    def render(self):
        self.clear()

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
            self.terrain.update(
                self.player_sprite.world_x, self.player_sprite.world_y, self.player_sprite.world_z)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.running = False

    def run(self):
        self.last_scheduled_update = time.time()

        # First draw
        self.terrain.update(
            self.player_sprite.world_x, self.player_sprite.world_y, self.player_sprite.world_z)

        # Main loop
        while self.running:
            if time.time() - self.last_scheduled_update > 1 / constants.FPS:
                self.update(time.time() - self.last_scheduled_update)
                self.last_scheduled_update = time.time()
            self.render()

            event = self.dispatch_events()
