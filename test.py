import time
import threading
from concurrent.futures import ThreadPoolExecutor

from game.terrain import data_handler, terrain, tile, chunk

import pyglet

def test():
    size = 20
    for x in range(size):
        for y in range(size):
            for z in range(size):
                data_handler.load_chunk(x,y,z)


tile.Tile.init_rendering(None, pyglet.graphics.Group())
t = terrain.Terrain()
c = chunk.Chunk(0,0,0)



start = time.time()


#test()

#for i in range(1):
    #t.update_chunks_on_screen(i*1000,i*1000,i*1000)



#tp = ThreadPoolExecutor(10)  # max 10 threads

c.load_tiles()



print(time.time() - start)
