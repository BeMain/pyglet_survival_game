import pyglet
from pyglet.window import key
import math

from game import constants
from game.terrain import chunk


# TODO: Implement zooming in and out

class Terrain():
    def __init__(self, *args, **kwargs):
        self.chunks = {}

    def update(self, player_x, player_y, player_z):
        self.get_chunks_on_screen(player_x, player_y, player_z)
    
    def get_tile(self, world_x, world_y, z):
        chunk_x = int(world_x / constants.TILE_SIZE) // constants.CHUNK_SIZE
        chunk_y = int(world_y / constants.TILE_SIZE) // constants.CHUNK_SIZE

        tile_x = int((world_x % (constants.CHUNK_SIZE * constants.TILE_SIZE)) / constants.TILE_SIZE + 0.5) 
        tile_y = int((world_y % (constants.CHUNK_SIZE * constants.TILE_SIZE)) / constants.TILE_SIZE + 0.5)

        c = self.chunks[(chunk_x, chunk_y, z)]
        #print(tile_x, tile_y)
        tile = c.tiles[tile_x][tile_y]
        return tile

    def get_chunks_on_screen(self, player_x, player_y, player_z):
        min_x = int(player_x - constants.SCREEN_WIDTH // 2)
        min_y = int(player_y - constants.SCREEN_HEIGHT // 2)
        max_x = int(player_x + constants.SCREEN_WIDTH // 2 + constants.TILE_SIZE // 2)
        max_y = int(player_y + constants.SCREEN_HEIGHT // 2 + constants.TILE_SIZE // 2)

        chunk_min_x = int(min_x // constants.TILE_SIZE) // constants.CHUNK_SIZE
        chunk_min_y = int(min_y // constants.TILE_SIZE) // constants.CHUNK_SIZE
        chunk_max_x = int(max_x // constants.TILE_SIZE) // constants.CHUNK_SIZE + 1
        chunk_max_y = int(max_y // constants.TILE_SIZE) // constants.CHUNK_SIZE + 1

        offset_x = min_x % (constants.CHUNK_SIZE * constants.TILE_SIZE)
        offset_y = min_y % (constants.CHUNK_SIZE * constants.TILE_SIZE)

        old_keys = self.chunks.keys() if self.chunks else []
        new_keys = []

        # TODO: Tiles on layer -1 that have a block above should not render

        # Generate chunks
        for z in range(player_z-1, player_z+2):
            for x in range(chunk_min_x, chunk_max_x):
                for y in range(chunk_min_y, chunk_max_y):
                    new_keys.append((x, y, z))
                    if ((x, y, z) in old_keys):
                        c = self.chunks[(x, y, z)]
                    else:
                        c = chunk.Chunk(x, y, z)
                        self.chunks[(x, y, z)] = c

                    c.set_pos((x - chunk_min_x) * constants.CHUNK_SIZE * constants.TILE_SIZE - offset_x,
                              (y - chunk_min_y) * constants.CHUNK_SIZE * constants.TILE_SIZE - offset_y, z - player_z)

        # Remove chunks outside screen
        to_remove = set(old_keys) - set(new_keys)
        for key in to_remove:
            self.chunks[key].save()
            self.chunks[key].delete()
            del self.chunks[key]
