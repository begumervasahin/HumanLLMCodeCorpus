import numpy as np
import sys
import os
import h5py
from sklearn.decomposition import IncrementalPCA
def fonk1(rows,columns):
    return np.random.rand(rows,columns)
def fonk2(b1 = 1000,b7=5000,columns=1000,save_fp="dense.h5"):
    if os.path.exists(save_fp):
        os.remove(save_fp)
    b2 = h5py.File(save_fp,mode="a")
    b3 = np.dtype(float)
    b4 = b2.create_dataset('float',(b7,columns),dtype=b3)
    for i in range(int(b7/b1)):
        b5 = fonk1(b1,columns)
        b4[i*b1:(i+1)*b1] = b5
        del b5
    b2.close()
def fonk3(b1 = 500,compressed_columns=200,uncompressed_fp="dense.h5",compressed_fp="compressed_dense.h5"):
    b6 = h5py.File(uncompressed_fp, 'r')
    b7 = b6["float"].shape[0]
    b8 = IncrementalPCA(n_components=compressed_columns)
    for i in range(int(b7/b1)+1):
        b9 = b6["float"][i*b1:(i+1)*b1]
        if len(b9) == 0:
            break
        b8.partial_fit(b9)
    print("Partially fit.")
    if os.path.exists(compressed_fp):
        os.remove(compressed_fp)
    b10 = h5py.File(compressed_fp,mode="a")
    b3 = np.dtype(float)
    b4 = b10.create_dataset('float',(b7,compressed_columns),dtype=b3)
    for i in range(int(b7/b1)+1):
        if i*b1 >= len(b6["float"]):
            break
        b9 = b8.transform(b6["float"][i*b1:(i+1)*b1])
        b4[i*b1:(i+1)*b1] = b9
        del b9
    b6.close()
    b10.close()
if b11 = = "__main__":
    fonk2()
    print("Data set created.")
    fonk3()
    print("Batches read.")