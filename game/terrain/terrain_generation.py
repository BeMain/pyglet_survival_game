# Using Python 3.7.4
from noise import pnoise2, snoise2

from game import constants


# TODO: Fix problem with terrain not generating continuesly. There are "holes" in the terrain

def generate_chunk(chunk_x, chunk_y):
    threshold = 0.5

    octaves = 1
    freq = 16.0 * octaves

    world_x = chunk_x * constants.CHUNK_SIZE
    world_y = chunk_y * constants.CHUNK_SIZE

    #print(chunk_x, world_x)

    chunk = []
    for x in range(constants.CHUNK_SIZE):
        col = []
        for y in range(constants.CHUNK_SIZE):
            pixel = pnoise2((world_x + x) / freq,
                            (world_y + y) / freq, octaves) * 0.5 + 0.5
            t_data = {}

            t_data["color"] = (1 if pixel >= threshold else 0)
            #dic["color"] = pixel
            t_data["local_x"] = x
            t_data["local_y"] = y

            col.append(t_data)
        chunk.append(col)

    return chunk
