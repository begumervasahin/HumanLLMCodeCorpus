import numpy as np
import struct
def fonk1(image_file, label_file):
    b1 = fonk2(image_file)
    b2 = fonk3(label_file)
    return b1, b2
def fonk2(image_file):
    with open(image_file, 'rb') as f:
        fonk4(f)
        b3 = fonk6(f)
        b4 = fonk6(f)
        b5 = fonk6(f)
        b6 = b4 * b5
        b1 = np.fromfile(f, dtype=np.uint8).reshape(b3, b6)
    return b1
def fonk3(label_file):
    with open(label_file, 'rb') as f:
        fonk5(f, 8)
        b2 = np.fromfile(f, dtype=np.uint8)
    return b2
def fonk4(file):
    fonk5(file, 4)
def fonk5(file, num_bytes):
    file.seek(num_bytes)
def fonk6(file):
    return struct.unpack('>I', file.read(4))[0]
