1. Repository: vuolleko/pyTSNE
   File: data.py
   URL: https:
   Code Content:
import numpy as np
import struct
def fonk1(filename_images, filename_labels):
    b1 = fonk2(filename_images)
    b2 = fonk3(filename_labels)
    return [b1, b2]
def fonk2(filename):
    with open(filename, 'rb') as fin:
        fin.seek(4)
        b3 = struct.unpack('>i', fin.read(4))[0]
        b4 = struct.unpack('>i', fin.read(4))[0]
        b5 = struct.unpack('>i', fin.read(4))[0]
        b6 = b5 * b4
        b1 = np.fromfile(fin, dtype=np.ubyte)
    b1 = b1.reshape(b3, b6)
    return b1
def fonk3(filename):
    with open(filename, 'rb') as fin:
        fin.seek(8)
        b2 = np.fromfile(fin, dtype=np.ubyte)
    return b2
   README Content:
* Heavy usage of Numpy makes the basic version relatively efficient.
* Conversely, the Barnes-Hut accelerated version relies more on pure Python and is therefore much slower at least for moderate sample sizes.
A school project.
