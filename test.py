from game.terrain import terrain_generation, chunk, data_handler, terrain

terrain = terrain.Terrain()
terrain.get_chunks_on_screen(100, 100)


print("Before set_pos()", terrain.chunks[(0, 0)].tiles[0][0].x)

terrain.chunks[(0, 0)].tiles[0][0].set_pos(1, 0)

print("After set_pos()", terrain.chunks[(0, 0)].tiles[0][0].x)
