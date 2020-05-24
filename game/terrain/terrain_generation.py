# Using Python 3.7.4
from noise import pnoise2, snoise2

from game import constants


def perlin_terrain(size_x, size_y):
    threshold = 0.5

    octaves = 1
    freq = 16.0 * octaves

    terrain = []
    for y in range(size_y):
        col = []
        for x in range(size_x):
            pixel = pnoise2(x / freq, y / freq, octaves) * 0.5 + 0.5
            col.append(1 if pixel >= threshold else 0)
            # col.append(pixel)
        terrain.append(col)

    # print(terrain)
    return terrain


def generate_chunk(chunk_x, chunk_y):
    threshold = 0.5

    octaves = 1
    freq = 16.0 * octaves

    world_x = chunk_x * constants.CHUNK_SIZE
    world_y = chunk_y * constants.CHUNK_SIZE

    chunk = []
    for x in range(constants.CHUNK_SIZE):
        col = []
        for y in range(constants.CHUNK_SIZE):
            pixel = pnoise2(x / freq + world_x, y / freq +
                            world_y, octaves) * 0.5 + 0.5
            dic = dict()
            dic["color"] = (1 if pixel >= threshold else 0)
            dic["local_x"] = x
            dic["local_y"] = y

            col.append(dic)
        chunk.append(col)

    return chunk
