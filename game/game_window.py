import pyglet
from pyglet.window import key

import time
import math

from game import constants, player
from game.terrain import terrain


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(constants.SCREEN_WIDTH,
                                         constants.SCREEN_HEIGHT, vsync=False, *args, **kwargs)
        self.running = True
        self.last_scheduled_update = time.time()
        self.keys = dict(left=False, right=False, up=False, down=False)

        self.main_batch = pyglet.graphics.Batch()

        self.terrain_group = pyglet.graphics.OrderedGroup(0)
        self.objects_group = pyglet.graphics.OrderedGroup(1)

        self.player_sprite = player.Player(
            batch=self.main_batch, group=self.objects_group)
        self.terrain = terrain.Terrain(
            batch=self.main_batch, group=self.terrain_group)
        self.fps_display = pyglet.window.FPSDisplay(self)

        self.game_objects = [self.player_sprite]

        self.player_x = 1000.0
        self.player_y = 1000.0

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
        # Update all objects
        # for obj in game_objects:
        #   obj.update(dt)

        # TODO: Clean up this mess
        if True in self.keys.values():
            speed = dt * 400

            if self.keys["right"]:
                self.player_x -= speed
            if self.keys["left"]:
                self.player_x += speed
            if self.keys["up"]:
                self.player_y -= speed
            if self.keys["down"]:
                self.player_y += speed

            self.terrain.update_tiles(
                self.player_x, self.player_y, batch=self.main_batch, group=self.terrain_group)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys["up"] = True
        if symbol == key.DOWN:
            self.keys["down"] = True
        if symbol == key.RIGHT:
            self.keys["right"] = True
        if symbol == key.LEFT:
            self.keys["left"] = True

        if symbol == key.ESCAPE:  # [ESC]
            self.running = False

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys["up"] = False
        if symbol == key.DOWN:
            self.keys["down"] = False
        if symbol == key.RIGHT:
            self.keys["right"] = False
        if symbol == key.LEFT:
            self.keys["left"] = False

    def run(self):
        self.last_scheduled_update = time.time()

        while self.running:
            if time.time() - self.last_scheduled_update > 1 / constants.FPS:
                self.update(time.time() - self.last_scheduled_update)
                self.last_scheduled_update = time.time()
            self.render()

            event = self.dispatch_events()
