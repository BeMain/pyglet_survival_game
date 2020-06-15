import pickle, json
import os
import shutil

from game import constants


# Player
def load_player_data():
    path = constants.PLAYER_DATA_PATH
    if not os.path.exists(path):
        # If file doesn't exist, return
        return
    with open(path, "r") as readfile:
        return json.load(readfile)

def write_player_data(player):
    data = {
        "world_x": player.world_x,
        "world_y": player.world_y,
        "world_z": player.world_z,
    }
    json.dump(data, open(constants.PLAYER_DATA_PATH, "w"))

def clear_player_data():
    print("Clearing player data")
    if os.path.exists(constants.PLAYER_DATA_PATH):
        os.remove(constants.PLAYER_DATA_PATH)


# Chunks
def read_chunk(chunk_x, chunk_y, chunk_z):
    path = f"{constants.CHUNKS_PATH}/{chunk_z}/{chunk_x}.{chunk_y}"
    if not os.path.exists(path):
        # If file doesn't exist, return None
        return None
    return pickle.load(open(path, "rb"))

def write_chunk(chunk_x, chunk_y, chunk_z, chunk):
    if not os.path.exists(f"{constants.CHUNKS_PATH}/{chunk_z}/"):
        os.makedirs(f"{constants.CHUNKS_PATH}/{chunk_z}/")
    pickle.dump(chunk, open(f"{constants.CHUNKS_PATH}/{chunk_z}/{chunk_x}.{chunk_y}", "wb"))

def clear_chunks():
    print("Clearing chunks")
    if os.path.exists(constants.CHUNKS_PATH):
        shutil.rmtree(constants.CHUNKS_PATH)
