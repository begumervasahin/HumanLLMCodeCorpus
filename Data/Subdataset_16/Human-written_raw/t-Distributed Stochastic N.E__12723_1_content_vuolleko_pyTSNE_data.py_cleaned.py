
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
