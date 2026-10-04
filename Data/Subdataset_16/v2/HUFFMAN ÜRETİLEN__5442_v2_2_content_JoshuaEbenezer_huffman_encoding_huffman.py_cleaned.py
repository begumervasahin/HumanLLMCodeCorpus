import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
import queue
class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = None
        self.b4 = None
    def fonk2(self, other):
        return self.b2 < other.b2
    def fonk3(self, other):
        return self.b2 > other.b2
def fonk4(b12):
    return np.rint(b12[:, :, 0] * 0.2989 + b12[:, :, 1] * 0.5870 + b12[:, :, 2] * 0.1140).astype(int)
def fonk5(b15):
    b5 = queue.PriorityQueue()
    for color, b2 in enumerate(b15):
        if b2 > 0:
            b5.put(class1(b1 = color, b2=b2))
    while b5.qsize() > 1:
        b3 = b5.get()
        b4 = b5.get()
        b6 = class1(b2=b3.b2 + b4.b2)
        b6.b3 = b3
        b6.b4 = b4
        b5.put(b6)
    return b5.get()
def fonk6(node, b7 = ''):
    if node is None:
        return {}
    if node.b3 is None and node.b4 is None:
        return {node.b1: b7}
    b8 = {}
    b8.update(fonk6(node.b3, b7 + '0'))
    b8.update(fonk6(node.b4, b7 + '1'))
    return b8
def fonk7(b14, b17, image_size):
    b9 = sum(len(b17[val]) * count for val, count in enumerate(b14) if count > 0)
    b10 = (1 - b9 / image_size) * 100
    return b10
if b11 = = "__main__":
    b12 = imread('tiger.bmp')
    b12 = imresize(b12, 10)
    b13 = fonk4(b12)
    b14 = np.bincount(b13.ravel(), minlength=256)
    b15 = b14 / np.sum(b14)
    b16 = fonk5(b15)
    b17 = fonk6(b16)
    with open('b8.txt', 'w') as code_file:
        for pixel_value, b7 in b17.items():
            code_file.write(f'{pixel_value} {b7}\n')
    b18 = b12.shape[0] * b12.shape[1] * 8
    b10 = fonk7(b14, b17, b18)
    print(f'Compression achieved: {b10:.2f}%')