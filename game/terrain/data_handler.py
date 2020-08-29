import pickle, json
import os
import shutil

from game import constants
from game.terrain import terrain_generation


# Player
def read_player_data():
    path = constants.PLAYER_DATA_PATH
    if not os.path.exists(path):
        # If file doesn't exist, return
        return
    with open(path, "r") as readfile:
        return json.load(readfile)

def write_player_data(data):
    with open(constants.PLAYER_DATA_PATH, "w") as writefile:
        json.dump(data, writefile)

def clear_player_data():
    print("Clearing player data")
    if os.path.exists(constants.PLAYER_DATA_PATH):
        os.remove(constants.PLAYER_DATA_PATH)


# Read chunk from disc
def read_chunk(chunk_x, chunk_y, chunk_z):
    path = f"{constants.CHUNKS_PATH}/{chunk_z}/{chunk_x}.{chunk_y}"
    if not os.path.exists(path):
        # If file doesn't exist, return None
        return
    with open(path, "rb") as readfile:
        return pickle.load(readfile)

# Write chunk to disc
def write_chunk(chunk_x, chunk_y, chunk_z, chunk):
    if not os.path.exists(f"{constants.CHUNKS_PATH}/{chunk_z}/"):
        os.makedirs(f"{constants.CHUNKS_PATH}/{chunk_z}/")
    
    with open(f"{constants.CHUNKS_PATH}/{chunk_z}/{chunk_x}.{chunk_y}", "wb") as writefile:
        pickle.dump(chunk, writefile)

# For loading a chunk. Reads chunk if it exists, otherwise generates a new one
def load_chunk(chunk_x, chunk_y, chunk_z):
    c = read_chunk(chunk_x, chunk_y, chunk_z)
    if not c:
        c = terrain_generation.generate_chunk(chunk_x, chunk_y, chunk_z)
    
    return c

# Remove all chunks
def clear_chunks():
    print("Clearing chunks")
    if os.path.exists(constants.CHUNKS_PATH):
        shutil.rmtree(constants.CHUNKS_PATH)
