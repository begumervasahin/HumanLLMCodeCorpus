import numpy as np
import os
import h5py
from sklearn.decomposition import IncrementalPCA
def fonk1(rows, columns):
    return np.random.rand(rows, columns)
def fonk2(b1 = 1000, b6=5000, columns=1000, save_fp="dense.h5"):
    if os.path.exists(save_fp):
        os.remove(save_fp)
    with h5py.File(save_fp, b2 = "a") as f:
        b3 = np.dtype(float)
        b4 = f.create_dataset('float', (b6, columns), dtype=b3)
        for i in range(int(b6 / b1)):
            b5 = fonk1(b1, columns)
            b4[i * b1:(i + 1) * b1] = b5
            del b5
    print("Data set created.")
def fonk3(b1 = 500, compressed_columns=200, uncompressed_fp="dense.h5", compressed_fp="compressed_dense.h5"):
    with h5py.File(uncompressed_fp, 'r') as data:
        b6 = data["float"].shape[0]
        b7 = IncrementalPCA(n_components=compressed_columns)
        for i in range(int(b6 / b1) + 1):
            b8 = data["float"][i * b1:(i + 1) * b1]
            if len(b8) == 0:
                break
            b7.partial_fit(b8)
        print("Partially fit.")
        if os.path.exists(compressed_fp):
            os.remove(compressed_fp)
        with h5py.File(compressed_fp, b2 = "a") as output:
            b3 = np.dtype(float)
            b4 = output.create_dataset('float', (b6, compressed_columns), dtype=b3)
            for i in range(int(b6 / b1) + 1):
                if i * b1 >= len(data["float"]):
                    break
                b8 = b7.transform(data["float"][i * b1:(i + 1) * b1])
                b4[i * b1:(i + 1) * b1] = b8
                del b8
    print("Batches read and transformed.")
if b9 = = "__main__":
    fonk2()
    fonk3()