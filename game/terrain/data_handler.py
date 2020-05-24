import pickle
import os
import glob


def read_chunk(chunk_x, chunk_y):
    path = "chunks/{}.{}".format(chunk_x, chunk_y)
    if os.path.exists(path):
        return pickle.load(open(path, "rb"))
    # If the chunck deosn't exist, return None
    return None


def write_chunk(chunk_x, chunk_y, chunk):
    pickle.dump(chunk, open("chunks/{}.{}".format(chunk_x, chunk_y), "wb"))


def clear_chunks():
    files = glob.glob('chunks/*')
    for f in files:
        os.remove(f)
