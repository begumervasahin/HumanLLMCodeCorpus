import os
import struct
from array import array as pyarray
import numpy as np
import cv2
def fonk1(b1 = "training", digits=np.arange(10), path="."):
    if b1 = = "training":
        b2 = os.path.join(path, 'train-b10.idx3-ubyte')
        b3 = os.path.join(path, 'train-b11.idx1-ubyte')
    elif b1 = = "testing":
        b2 = os.path.join(path, 't10k-b10.idx3-ubyte')
        b3 = os.path.join(path, 't10k-b11.idx1-ubyte')
    else:
        raise ValueError("Dataset must be 'testing' or 'training'")
    with open(b3, 'rb') as flbl:
        magic_nr, b4 = struct.unpack(">II", flbl.read(8))
        b5 = pyarray("b", flbl.read())
    with open(b2, 'rb') as fimg:
        magic_nr, b4, rows, b6 = struct.unpack(">IIII", fimg.read(16))
        b7 = pyarray("B", fimg.read())
    b8 = [k for k in range(b4) if b5[k] in digits]
    b9 = len(b8)
    b10 = np.zeros((b9, rows, b6), dtype=np.uint8)
    b11 = np.zeros((b9, 1), dtype=np.int8)
    for i in range(b9):
        b10[i] = np.array(b7[b8[i]*rows*b6 : (b8[i]+1)*rows*b6]).reshape((rows, b6))
        b11[i] = b5[b8[i]]
    return b10, b11
def fonk2(b10):
    for i in range(len(b10)):
        _, b12 = cv2.threshold(b10[i], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        b10[i] = b12
    return b10
def fonk3(b10, b11, b13 = "X_test.npy", labels_path="y_test.npy"):
    np.save(b13, b10)
    np.save(labels_path, b11)
if b14 = = "__main__":
    b10, b11 = fonk1(b1="testing")
    b10 = fonk2(b10)
    fonk3(b10, b11)