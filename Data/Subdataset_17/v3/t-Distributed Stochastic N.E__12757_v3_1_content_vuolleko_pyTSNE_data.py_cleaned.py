import numpy as np
import struct
def read_MNIST(image_file, label_file):
    images = _load_images(image_file)
    labels = _load_labels(label_file)
    return images, labels
def _load_images(image_file):
    with open(image_file, 'rb') as f:
        _skip_bytes(f, 4)
        n_samples = _read_int(f)
        n_rows = _read_int(f)
        n_cols = _read_int(f)
        n_pixels = n_rows * n_cols
        images = np.fromfile(f, dtype=np.uint8).reshape(n_samples, n_pixels)
    return images
def _load_labels(label_file):
    with open(label_file, 'rb') as f:
        _skip_bytes(f, 8)
        labels = np.fromfile(f, dtype=np.uint8)
    return labels
def _skip_bytes(file, num_bytes):
    file.seek(num_bytes)
def _read_int(file):
    return struct.unpack('>I', file.read(4))[0]
