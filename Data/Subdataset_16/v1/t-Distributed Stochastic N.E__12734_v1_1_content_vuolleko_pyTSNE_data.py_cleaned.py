import numpy as np
import struct
def fonk1(image_file, label_file):
    b1 = fonk2(image_file)
    b2 = fonk3(label_file)
    return b1, b2
def fonk2(image_file):
    with open(image_file, 'rb') as f:
        f.seek(4)
        b3 = struct.unpack('>I', f.read(4))[0]
        b4 = struct.unpack('>I', f.read(4))[0]
        b5 = struct.unpack('>I', f.read(4))[0]
        b6 = b4 * b5
        b1 = np.fromfile(f, dtype=np.uint8).reshape(b3, b6)
    return b1
def fonk3(label_file):
    with open(label_file, 'rb') as f:
        f.seek(8)
        b2 = np.fromfile(f, dtype=np.uint8)
    return b2
