import numpy as np
import struct
def read_MNIST(filename_images, filename_labels):
    pixels = _read_images(filename_images)
    labels = _read_labels(filename_labels)
    return [pixels, labels]
def _read_images(filename):
    with open(filename, 'rb') as file:
        file.seek(4)
        n_samples = struct.unpack('>i', file.read(4))[0]
        n_rows = struct.unpack('>i', file.read(4))[0]
        n_cols = struct.unpack('>i', file.read(4))[0]
        n_dim = n_rows * n_cols
        pixels = np.fromfile(file, dtype=np.ubyte)
    pixels = pixels.reshape(n_samples, n_dim)
    return pixels
def _read_labels(filename):
    with open(filename, 'rb') as file:
        file.seek(8)
        labels = np.fromfile(file, dtype=np.ubyte)
    return labels