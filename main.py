import pyglet
import time
from pyglet.window import key, FPSDisplay

from game import player, constants, load, game_window
from game.terrain import terrain


if __name__ == "__main__":
    #pyglet.clock.schedule_interval(update, 1/120.0)

    window = game_window.GameWindow()
    window.run()
