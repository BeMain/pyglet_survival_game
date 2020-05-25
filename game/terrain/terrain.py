from pyglet.window import key
import math

from game import constants, resources
from game.terrain import chunk


# TODO: Implement zooming in and out

class Terrain():
    def __init__(self, batch=None, group=None, *args, **kwargs):
        self.chunks = {}

        self.batch = batch
        self.group = group

    def update(self, player_x, player_y, player_z):
        self.get_chunks_on_screen(player_x, player_y, player_z)

    def get_chunks_on_screen(self, player_x, player_y, player_z):
        min_x = int(player_x - constants.SCREEN_WIDTH / 2)
        min_y = int(player_y - constants.SCREEN_HEIGHT / 2)
        max_x = int(player_x + constants.SCREEN_WIDTH / 2 +
                    resources.tile_image.width // 2)
        max_y = int(player_y + constants.SCREEN_HEIGHT / 2 +
                    resources.tile_image.height // 2)

        chunk_min_x = int(
            min_x // resources.tile_image.width) // constants.CHUNK_SIZE
        chunk_min_y = int(
            min_y // resources.tile_image.height) // constants.CHUNK_SIZE
        chunk_max_x = int(
            max_x // resources.tile_image.width) // constants.CHUNK_SIZE + 1
        chunk_max_y = int(
            max_y // resources.tile_image.height) // constants.CHUNK_SIZE + 1

        offset_x = min_x % (constants.CHUNK_SIZE * resources.tile_image.width)
        offset_y = min_y % (constants.CHUNK_SIZE * resources.tile_image.height)

        old_keys = self.chunks.keys() if self.chunks else []
        new_keys = []

        for z in range(1):
            for x in range(chunk_min_x, chunk_max_x):
                for y in range(chunk_min_y, chunk_max_y):
                    new_keys.append((x, y, z))
                    if ((x, y, z) in old_keys):
                        c = self.chunks[(x, y, z)]
                    else:
                        c = chunk.Chunk(x, y, z, batch=self.batch, group=self.group)
                        self.chunks[(x, y, z)] = c

                    c.set_pos((x - chunk_min_x) * constants.CHUNK_SIZE * resources.tile_image.width - offset_x,
                              (y - chunk_min_y) * constants.CHUNK_SIZE * resources.tile_image.height - offset_y)

        to_remove = set(old_keys) - set(new_keys)
        for key in to_remove:
            self.chunks[key].delete()
            del self.chunks[key]
