import numpy as np
import struct
def fonk1(filename_images, filename_labels):
    b1 = fonk2(filename_images)
    b2 = fonk3(filename_labels)
    return [b1, b2]
def fonk2(filename):
    with open(filename, 'rb') as file:
        file.seek(4)
        n_samples, n_rows, b3 = struct.unpack('>3i', file.read(12))
        b4 = n_rows * b3
        b1 = np.fromfile(file, dtype=np.ubyte)
    b1 = b1.reshape(n_samples, b4)
    return b1
def fonk3(filename):
    with open(filename, 'rb') as file:
        file.seek(8)
        b2 = np.fromfile(file, dtype=np.ubyte)
    return b2