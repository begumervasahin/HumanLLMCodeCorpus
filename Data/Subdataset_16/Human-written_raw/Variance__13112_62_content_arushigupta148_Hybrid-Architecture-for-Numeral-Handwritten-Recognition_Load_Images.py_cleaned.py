import os, struct
from array import array as pyarray
from numpy import append, array, int8, uint8, zeros
import numpy as np
from pylab import *
import pandas as pd
import cv2
def fonk1(b1 = "training", digits=np.arange(10), path="."):
    if b1 = = "training":
        b2 = os.path.join(path, 'train-b12.idx3-ubyte')
        b3 = os.path.join(path, 'train-b13.idx1-ubyte')
    elif b1 = = "testing":
        b2 = os.path.join(path, 't10k-b12.idx3-ubyte')
        b3 = os.path.join(path, 't10k-b13.idx1-ubyte')
    else:
        raise ValueError("b1 must be 'testing' or 'training'")
    b4 = open(b3, 'rb')
    magic_nr, b5 = struct.unpack(">II", b4.read(8))
    b6 = pyarray("b", b4.read())
    b4.close()
    b7 = open(b2, 'rb')
    magic_nr, b5, rows, b8 = struct.unpack(">IIII", b7.read(16))
    b9 = pyarray("B", b7.read())
    b7.close()
    b10 = [ k for k in range(b5) if b6[k] in digits ]
    b11 = len(b10)
    b12 = zeros((b11, rows, b8), dtype=uint8)
    b13 = zeros((b11, 1), dtype=int8)
    for i in range(len(b10)):
        b12[i] = array(b9[ b10[i]*rows*b8 : (b10[i]+1)*rows*b8 ]).reshape((rows, b8))
        b13[i] = b6[b10[i]]
    return b12, b13
b12, b13 = fonk1(b1="testing")
for i in range(len(b12)):
    ret3,b14 = cv2.threshold(b12[i],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    b12[i] = b14
np.save("X_test.npy", b12)
np.save("y_test.npy", b13)