from game import resources
from game.terrain import data_handler, terrain_generation, tile


class Chunk():
    def __init__(self, chunk_x, chunk_y, batch=None, group=None):
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y

        self.batch = batch
        self.group = group

        self.tiles = []
        self.load_tiles()

    def set_pos(self, x, y):
        for row in self.tiles:
            for tile in row:
                tile.set_pos(x, y)

    def load_tiles(self):
        chunk = data_handler.read_chunk(self.chunk_x, self.chunk_y)
        # If chunk doesn't exist, generate new
        if not chunk:
            chunk = terrain_generation.generate_chunk(
                self.chunk_x, self.chunk_y)
            data_handler.write_chunk(self.chunk_x, self.chunk_y, chunk)
        self.tiles = list(map(lambda row: list(map(self.to_tile, row)), chunk))

    def to_tile(self, t_data):
        color = t_data["color"] * 255
        new_tile = tile.Tile(
            t_data["local_x"], t_data["local_y"], batch=self.batch, group=self.group)
        new_tile.color = (color, color, color)

        return new_tile

    def delete(self):
        for row in self.tiles:
            for tile in row:
                tile.delete()

    def save(self):
        data_handler.write_chunk(self.chunk_x, self.chunk_y, self.tiles)
