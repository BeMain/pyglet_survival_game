from pyglet.window import key
import math

from game import load, constants, resources
from game.terrain import tile


class Terrain():
    def __init__(self, batch=None, group=None, *args, **kwargs):
        self.terrain = load.terrain_new(200, 200)
        self.tiles = []
        self.key_handler = key.KeyStateHandler()

        self.batch = batch
        self.group = group

    def update(self, player_x, player_y, batch=None, group=None):
        # This way of loading tiles is terrible for performance
        # TODO: Implement a way to precedurally refresh tiles when they load/unload instead of loading all tiles every time

        # Clear terrain
        for t in self.tiles:
            t.delete()
        # Get the parts that are on screen
        self.tiles = self.get_tiles_on_screen(
            player_x, player_y)

    def get_tiles_on_screen(self, player_x, player_y):
        # TODO: Use a json file for storing the terrain
        min_x = player_x - constants.SCREEN_WIDTH / 2
        min_y = player_y - constants.SCREEN_HEIGHT / 2

        world_min_x = int(min_x / resources.tile_image.width)
        world_min_y = int(min_y / resources.tile_image.height)

        world_size_x = constants.SCREEN_WIDTH // resources.tile_image.width + 1
        world_size_y = constants.SCREEN_HEIGHT // resources.tile_image.height + 1

        offset_x = min_x % resources.tile_image.width
        offset_y = min_y % resources.tile_image.height

        tiles = []
        for x in range(world_size_x):
            for y in range(world_size_y):
                color = self.terrain[x + world_min_x][y + world_min_y] * 255
                new_tile = tile.Tile(batch=self.batch, group=self.group)
                new_tile.x = x * new_tile.width - offset_x + resources.tile_image.width / 2
                new_tile.y = y * new_tile.height - offset_y + resources.tile_image.height / 2
                new_tile.color = (color, color, color)

                tiles.append(new_tile)
        return tiles
