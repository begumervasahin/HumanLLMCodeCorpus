import os
import struct
from array import array as pyarray
import numpy as np
import cv2
def load_mnist(dataset="training", digits=np.arange(10), path="."):
    """
    Loads MNIST files into 3D numpy arrays.
    Parameters:
    dataset (str): "training" or "testing"
    digits (array-like): array of digits to load
    path (str): path to the MNIST files
    Returns:
    tuple: images, labels
    """
    if dataset == "training":
        fname_img = os.path.join(path, 'train-images.idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels.idx1-ubyte')
    elif dataset == "testing":
        fname_img = os.path.join(path, 't10k-images.idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels.idx1-ubyte')
    else:
        raise ValueError("dataset must be 'testing' or 'training'")
    with open(fname_lbl, 'rb') as flbl:
        magic_nr, size = struct.unpack(">II", flbl.read(8))
        lbl = pyarray("b", flbl.read())
    with open(fname_img, 'rb') as fimg:
        magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = pyarray("B", fimg.read())
    ind = [k for k in range(size) if lbl[k] in digits]
    N = len(ind)
    images = np.zeros((N, rows, cols), dtype=np.uint8)
    labels = np.zeros((N, 1), dtype=np.int8)
    for i in range(N):
        images[i] = np.array(img[ind[i]*rows*cols : (ind[i]+1)*rows*cols]).reshape((rows, cols))
        labels[i] = lbl[ind[i]]
    return images, labels
images, labels = load_mnist(dataset="testing")
for i in range(len(images)):
    _, th3 = cv2.threshold(images[i], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    images[i] = th3
np.save("X_test.npy", images)
np.save("y_test.npy", labels)