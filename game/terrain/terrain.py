from pyglet.window import key
import math
import numpy as np

from game import load, constants, resources
from game.terrain import tile, data_handler, chunk


# TODO: Implement zooming in and out

class Terrain():
    def __init__(self, batch=None, group=None, *args, **kwargs):
        self.terrain = load.terrain_new(200, 200)
        self.tiles = []
        self.chunks = {}
        self.key_handler = key.KeyStateHandler()

        self.batch = batch
        self.group = group

    def update(self, player_x, player_y, batch=None, group=None):
        # This way of loading tiles is terrible for performance
        # TODO: Implement a better way to precedurally refresh tiles when they load/unload instead of loading all tiles every time

        self.get_chunks_on_screen(player_x, player_y)

    def get_tiles_on_screen(self, player_x, player_y):
        min_x = player_x - constants.SCREEN_WIDTH / 2
        min_y = player_y - constants.SCREEN_HEIGHT / 2

        world_min_x = int(min_x // resources.tile_image.width)
        world_min_y = int(min_y // resources.tile_image.height)

        world_size_x = int(constants.SCREEN_WIDTH //
                           resources.tile_image.width) + 2
        world_size_y = int(constants.SCREEN_HEIGHT //
                           resources.tile_image.height) + 2

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

    # Using numpy.array and slicing
    def get_tiles_on_screen2(self, player_x, player_y):
        # TODO: Replace with a chunk-based system
        min_x = player_x - constants.SCREEN_WIDTH / 2
        min_y = player_y - constants.SCREEN_HEIGHT / 2
        max_x = player_x + constants.SCREEN_WIDTH / 2
        max_y = player_y + constants.SCREEN_HEIGHT / 2

        world_min_x = int(min_x // resources.tile_image.width)
        world_min_y = int(min_y // resources.tile_image.height)
        world_max_x = int(max_x // resources.tile_image.width) + 2
        world_max_y = int(max_y // resources.tile_image.height) + 2

        offset_x = min_x % resources.tile_image.width
        offset_y = min_y % resources.tile_image.height

        arr = np.array(self.terrain)
        arr = arr[world_min_x:world_max_x, world_min_y:world_max_y]

        tiles = []
        for x in range(len(arr)):
            for y in range(len(arr[0])):
                color = arr[x][y] * 255
                new_tile = tile.Tile(batch=self.batch, group=self.group)
                new_tile.x = x * new_tile.width - offset_x + resources.tile_image.width / 2
                new_tile.y = y * new_tile.height - offset_y + resources.tile_image.height / 2
                new_tile.color = (color, color, color)

                tiles.append(new_tile)
        return tiles

    def get_chunks_on_screen(self, player_x, player_y):
        min_x = player_x - constants.SCREEN_WIDTH / 2
        min_y = player_y - constants.SCREEN_HEIGHT / 2
        max_x = player_x + constants.SCREEN_WIDTH / 2
        max_y = player_y + constants.SCREEN_HEIGHT / 2

        chunk_min_x = int(
            min_x // resources.tile_image.width) // constants.CHUNK_SIZE
        chunk_min_y = int(
            min_y // resources.tile_image.height) // constants.CHUNK_SIZE
        chunk_max_x = int(
            max_x // resources.tile_image.width) // constants.CHUNK_SIZE
        chunk_max_y = int(
            max_y // resources.tile_image.height) // constants.CHUNK_SIZE

        offset_x = min_x % resources.tile_image.width
        offset_y = min_y % resources.tile_image.height

        print("Chunk min: {}, max: {}".format(chunk_min_x, chunk_max_x))

        old_keys = self.chunks.keys() if self.chunks else []
        new_keys = []

        for x in range(chunk_min_x, chunk_max_x):
            for y in range(chunk_min_y, chunk_max_y):
                new_keys.append((x, y))
                if not ((x, y) in old_keys):
                    c = chunk.Chunk(x, y, batch=self.batch, group=self.group)
                    c.set_pos((x - chunk_min_x) * constants.CHUNK_SIZE * resources.tile_image.width,
                              (y - chunk_min_y) * constants.CHUNK_SIZE * resources.tile_image.height)
                    self.chunks[(x, y)] = c
                print(x, (x - chunk_min_x) * constants.CHUNK_SIZE *
                      resources.tile_image.width)

        to_remove = set(old_keys) - set(new_keys)
        for key in to_remove:
            self.chunks[key].delete()
            del self.chunks[key]
