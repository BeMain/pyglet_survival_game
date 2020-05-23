from game import resources
from game.terrain import tile, terrain_generation


def terrain(size_x, size_y, *args, **kwargs):
    # TODO: Make terrain infinite

    p_terrain = terrain_generation.perlin_terrain(size_x, size_y, octaves=2)

    tiles = []

    for x in range(size_x):
        for y in range(size_y):
            new_tile = tile.Tile(*args, **kwargs)
            new_tile.scale = 1
            new_tile.x = new_tile.width * x
            new_tile.y = new_tile.height * y

            color = 255 * p_terrain[x][y]
            new_tile.color = (color, color, color)

            tiles.append(new_tile)

    return tiles


def terrain_new(size_x, size_y):
    p_terrain = terrain_generation.perlin_terrain(size_x, size_y, octaves=2)

    return p_terrain
