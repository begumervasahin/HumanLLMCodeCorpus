import numpy as np
import struct
def read_MNIST(image_file, label_file):
    images = _load_images(image_file)
    labels = _load_labels(label_file)
    return images, labels
def _load_images(image_file):
    with open(image_file, 'rb') as f:
        f.seek(4)
        n_samples = struct.unpack('>I', f.read(4))[0]
        n_rows = struct.unpack('>I', f.read(4))[0]
        n_cols = struct.unpack('>I', f.read(4))[0]
        n_pixels = n_rows * n_cols
        images = np.fromfile(f, dtype=np.uint8).reshape(n_samples, n_pixels)
    return images
def _load_labels(label_file):
    with open(label_file, 'rb') as f:
        f.seek(8)
        labels = np.fromfile(f, dtype=np.uint8)
    return labels
