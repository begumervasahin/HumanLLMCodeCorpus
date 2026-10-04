import numpy as np
import os
import h5py
from sklearn.decomposition import IncrementalPCA
def fonk1(rows, columns):
    return np.random.rand(rows, columns)
def fonk2(b1 = 1000, b5=5000, columns=1000, save_fp="dense.h5"):
    if os.path.exists(save_fp):
        os.remove(save_fp)
    with h5py.File(save_fp, b2 = "a") as f:
        b3 = f.create_dataset('float', (b5, columns), dtype=np.float64)
        for i in range(b5
            b4 = fonk1(b1, columns)
            b3[i * b1:(i + 1) * b1] = b4
    print(f"Dataset created and saved to {save_fp}")
def fonk3(b1 = 500, compressed_columns=200, uncompressed_fp="dense.h5", compressed_fp="compressed_dense.h5"):
    with h5py.File(uncompressed_fp, 'r') as data:
        b5 = data["float"].shape[0]
        b6 = IncrementalPCA(n_components=compressed_columns)
        for i in range(b5
            b4 = data["float"][i * b1:(i + 1) * b1]
            if b4.b7 = = 0:
                break
            b6.partial_fit(b4)
        print("Incremental PCA model fitted.")
        if os.path.exists(compressed_fp):
            os.remove(compressed_fp)
        with h5py.File(compressed_fp, b2 = "a") as output:
            b3 = output.create_dataset('float', (b5, compressed_columns), dtype=np.float64)
            for i in range(b5
                if i * b1 >= b5:
                    break
                b8 = b6.transform(data["float"][i * b1:(i + 1) * b1])
                b3[i * b1:(i + 1) * b1] = b8
    print(f"Compressed dataset created and saved to {compressed_fp}")
if b9 = = "__main__":
    fonk2()
    fonk3()