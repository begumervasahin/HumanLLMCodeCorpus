1. Repository: vuolleko/pyTSNE
   File: data.py
   URL: https:
   Code Content:
import numpy as np
import struct
def read_MNIST(filename_images, filename_labels):
    pixels = _read_images(filename_images)
    labels = _read_labels(filename_labels)
    return [pixels, labels]
def _read_images(filename):
    with open(filename, 'rb') as fin:
        fin.seek(4)
        n_samples = struct.unpack('>i', fin.read(4))[0]
        n_rows = struct.unpack('>i', fin.read(4))[0]
        n_cols = struct.unpack('>i', fin.read(4))[0]
        n_dim = n_cols * n_rows
        pixels = np.fromfile(fin, dtype=np.ubyte)
    pixels = pixels.reshape(n_samples, n_dim)
    return pixels
def _read_labels(filename):
    with open(filename, 'rb') as fin:
        fin.seek(8)
        labels = np.fromfile(fin, dtype=np.ubyte)
    return labels
   README Content:
* Heavy usage of Numpy makes the basic version relatively efficient.
* Conversely, the Barnes-Hut accelerated version relies more on pure Python and is therefore much slower at least for moderate sample sizes.
A school project.
