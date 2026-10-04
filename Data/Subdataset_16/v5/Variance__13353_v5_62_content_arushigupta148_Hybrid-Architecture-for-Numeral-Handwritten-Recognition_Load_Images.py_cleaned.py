import os
import struct
from array import array as pyarray
import numpy as np
import cv2
def fonk1(b1 = "training", digits=np.arange(10), path="."):
    """
    Loads MNIST files into 3D numpy arrays.
    Parameters:
    b1 (str): "training" or "testing"
    digits (array-like): Array of digits to load
    path (str): Path to the MNIST files
    Returns:
    tuple: (b10, b11)
    """
    if b1 = = "training":
        b2 = os.path.join(path, 'train-b10.idx3-ubyte')
        b3 = os.path.join(path, 'train-b11.idx1-ubyte')
    elif b1 = = "testing":
        b2 = os.path.join(path, 't10k-b10.idx3-ubyte')
        b3 = os.path.join(path, 't10k-b11.idx1-ubyte')
    else:
        raise ValueError("b1 must be 'testing' or 'training'")
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
    for i, idx in enumerate(b8):
        b10[i] = np.array(b7[idx*rows*b6 : (idx+1)*rows*b6]).reshape((rows, b6))
        b11[i] = b5[idx]
    return b10, b11
def fonk2(b10):
    b12 = []
    for image in b10:
        _, b13 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        b12.append(b13)
    return np.array(b12)
def fonk3(b10, b11, b14 = "X_test.npy", label_filename="y_test.npy"):
    np.save(b14, b10)
    np.save(label_filename, b11)
b10, b11 = fonk1(b1="testing")
b12 = fonk2(b10)
fonk3(b12, b11)