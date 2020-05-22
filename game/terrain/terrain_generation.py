# Using Python 3.7.4
from noise import pnoise2, snoise2


def perlin_terrain(size_x, size_y, octaves=1, threshold=0.5):
    freq = 16.0 * octaves

    terrain = []
    for y in range(size_y):
        col = []
        for x in range(size_x):
            pixel = pnoise2(x / freq, y / freq, octaves) * 0.5 + 0.5
            col.append(1 if pixel >= threshold else 0)
            # col.append(pixel)
        terrain.append(col)

    return terrain
