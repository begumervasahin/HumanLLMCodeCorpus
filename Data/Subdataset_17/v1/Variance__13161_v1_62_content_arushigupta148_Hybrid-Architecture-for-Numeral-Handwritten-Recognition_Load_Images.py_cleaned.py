import os
import struct
from array import array as pyarray
import numpy as np
import cv2
def load_mnist(dataset="training", digits=np.arange(10), path="."):
    if dataset == "training":
        fname_img = os.path.join(path, 'train-images.idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels.idx1-ubyte')
    elif dataset == "testing":
        fname_img = os.path.join(path, 't10k-images.idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels.idx1-ubyte')
    else:
        raise ValueError("Dataset must be 'testing' or 'training'")
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
def apply_otsu_threshold(images):
    for i in range(len(images)):
        _, th_img = cv2.threshold(images[i], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        images[i] = th_img
    return images
def save_images_and_labels(images, labels, images_path="X_test.npy", labels_path="y_test.npy"):
    np.save(images_path, images)
    np.save(labels_path, labels)
images, labels = load_mnist(dataset="testing")
images = apply_otsu_threshold(images)
save_images_and_labels(images, labels)