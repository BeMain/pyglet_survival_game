from pyglet.window import key
import math

from game import load, constants, resources
from game.terrain import tile


class Terrain():
    def __init__(self, batch=None, *args, **kwargs):
        self.terrain = load.terrain_new(200, 200)
        self.tiles = []
        self.key_handler = key.KeyStateHandler()

        self.vel_x = 0
        self.vel_y = 0

    def update_tiles(self, player_x, player_y, batch=None, group=None):
        # This way of loading tiles is terrible for performance
        # TODO: Implement a way to precedurally refresh tiles when they load/unload instead of loading all tiles every time

        # Clear terrain
        for t in self.tiles:
            t.delete()
        # Get the parts that are on screen
        self.tiles = self.get_tiles_on_screen(
            player_x, player_y, batch=batch, group=group)

    def get_tiles_on_screen(self, player_x, player_y, batch=None, group=None):
        # TODO: Use a json file for storing the terrain
        min_x = player_x - constants.SCREEN_WIDTH / 2
        min_y = player_y - constants.SCREEN_HEIGHT / 2

        world_min_x = int(min_x / resources.tile_image.width)
        world_min_y = int(min_y / resources.tile_image.height)

        world_size_x = constants.SCREEN_WIDTH // resources.tile_image.width
        world_size_y = constants.SCREEN_HEIGHT // resources.tile_image.height

        tiles = []
        for x in range(world_size_x):
            for y in range(world_size_y):
                color = self.terrain[x + world_min_x][y + world_min_y] * 255
                new_tile = tile.Tile(batch=batch, group=None)
                new_tile.x = x * new_tile.width
                new_tile.y = y * new_tile.height
                new_tile.color = (color, color, color)

                tiles.append(new_tile)
        return tiles
