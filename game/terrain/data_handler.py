import pickle
import os


def read_chunk(chunk_x, chunk_y):
    path = "chunks/{}.{}".format(chunk_x, chunk_y)
    if os.path.exists(path):
        return pickle.load(open(path, "rb"))
    return None


def write_chunk(chunk_x, chunk_y, chunk):
    pickle.dump(chunk, open("chunks/{}.{}".format(chunk_x, chunk_y), "wb"))
