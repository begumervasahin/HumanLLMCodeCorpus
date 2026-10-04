import os
import struct
from array import array as pyarray
import numpy as np
import cv2
def fonk1(b1 = "training", digits=np.arange(10), path="."):
    if b1 = = "training":
        b2 = os.path.join(path, 'train-b5.idx3-ubyte')
        b3 = os.path.join(path, 'train-b4.idx1-ubyte')
    elif b1 = = "testing":
        b2 = os.path.join(path, 't10k-b5.idx3-ubyte')
        b3 = os.path.join(path, 't10k-b4.idx1-ubyte')
    else:
        raise ValueError("Dataset must be 'testing' or 'training'")
    b4 = fonk2(b3)
    b5 = fonk3(b2, b4, digits)
    return b5, b4
def fonk2(label_path):
    with open(label_path, 'rb') as flbl:
        magic_nr, b6 = struct.unpack(">II", flbl.read(8))
        b4 = pyarray("b", flbl.read())
    return b4
def fonk3(image_path, b4, digits):
    with open(image_path, 'rb') as fimg:
        magic_nr, b6, rows, b7 = struct.unpack(">IIII", fimg.read(16))
        b8 = pyarray("B", fimg.read())
    b9 = [k for k in range(b6) if b4[k] in digits]
    b10 = len(b9)
    b5 = np.zeros((b10, rows, b7), dtype=np.uint8)
    for i in range(b10):
        b5[i] = np.array(b8[b9[i] * rows * b7 : (b9[i] + 1) * rows * b7]).reshape((rows, b7))
    return b5
def fonk4(b5):
    for i in range(len(b5)):
        _, b11 = cv2.threshold(b5[i], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        b5[i] = b11
    return b5
def fonk5(b5, b4, b12 = "X_test.npy", labels_path="y_test.npy"):
    np.save(b12, b5)
    np.save(labels_path, b4)
if b13 = = "__main__":
    b5, b4 = fonk1(b1="testing")
    b5 = fonk4(b5)
    fonk5(b5, b4)