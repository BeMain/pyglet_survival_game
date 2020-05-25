import pickle
import os
import shutil

# Updated for 3d-terrain
def read_chunk(chunk_x, chunk_y, chunk_z):
    path = "chunks/{}/{}.{}".format(chunk_z, chunk_x, chunk_y)
    if not os.path.exists(path):
        # If the chunk deosn't exist, return None
        return None
    return pickle.load(open(path, "rb"))


def write_chunk(chunk_x, chunk_y, chunk_z, chunk):
    if not os.path.exists("chunks/{}/".format(chunk_z)):
        os.makedirs("chunks/{}/".format(chunk_z))
    pickle.dump(chunk, open("chunks/{}/{}.{}".format(chunk_z, chunk_x, chunk_y), "wb"))


def clear_chunks():
    shutil.rmtree("chunks")
