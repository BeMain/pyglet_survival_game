from game.terrain import data_handler, terrain_generation, tile

# Updated for 3d-terrain
class Chunk():
    def __init__(self, chunk_x, chunk_y, chunk_z, batch=None, group=None):
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self.chunk_z = chunk_z

        self.batch = batch
        self.group = group

        self.tiles = []
        self.load_tiles()

    def set_pos(self, x, y, z):
        for row in self.tiles:
            for tile in row:
                if tile:
                    tile.set_pos(x, y, z)

    def load_tiles(self):
        chunk = data_handler.read_chunk(self.chunk_x, self.chunk_y, self.chunk_z)
        # If chunk doesn't exist, generate new
        if not chunk:
            chunk = terrain_generation.generate_chunk(self.chunk_x, self.chunk_y, self.chunk_z)
            data_handler.write_chunk(self.chunk_x, self.chunk_y, self.chunk_z, chunk)

        # Turn the 3d-list of dicts -> 3d-list of Tiles
        self.tiles = list(map(lambda col: list(map(self.load_tile, col)), chunk))

    def load_tile(self, t_data):
        return tile.Tile.from_data(t_data, batch=self.batch, group=self.group)

    def to_data(self):
        return list(map(lambda col: list(map(lambda tile: tile.to_data(), col)), self.tiles))

    def delete(self):
        for col in self.tiles:
            for tile in col:
                if tile:
                    tile.delete()

    def save(self):
        data_handler.write_chunk(self.chunk_x, self.chunk_y, self.chunk_z, self.to_data())
