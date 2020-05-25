import os
from game.terrain import terrain_generation, chunk, data_handler, terrain

x = 0
y = 0


data_handler.clear_chunks()

ter = terrain.Terrain()

ter.get_chunks_on_screen(0,0,0)

ch = data_handler.read_chunk(x,y,0)
for column in ch:
    col = []
    for data in column:
        col.append(data["color"])
    print(col)

print()
print()

ch = data_handler.read_chunk(x,y,-1)
for column in ch:
    col = []
    for data in column:
        col.append(data["color"])
    print(col)