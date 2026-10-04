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
def fonk3(b11):
    return np.rint(b11[:, :, 0] * 0.2989 + b11[:, :, 1] * 0.5870 + b11[:, :, 2] * 0.1140).astype(int)
def fonk4(b14):
    b5 = queue.PriorityQueue()
    for pixel_value, b2 in enumerate(b14):
        if b2 > 0:
            b5.put(class1(b1 = pixel_value, b2=b2))
    while b5.qsize() > 1:
        b3 = b5.get()
        b4 = b5.get()
        b6 = class1(b2=b3.b2 + b4.b2, b1=None)
        b6.b3 = b3
        b6.b4 = b4
        b5.put(b6)
    return b5.get()
def fonk5(node, b7 = ''):
    if node is None:
        return {}
    if node.b3 is None and node.b4 is None:
        return {node.b1: b7}
    b8 = {}
    b8.update(fonk5(node.b3, b7 + '0'))
    b8.update(fonk5(node.b4, b7 + '1'))
    return b8
def fonk6(b13, b16, image_size):
    b9 = sum(len(b16[val]) * count for val, count in enumerate(b13) if count > 0)
    b10 = (1 - b9 / image_size) * 100
    return b10
def fonk7():
    b11 = imread('tiger.bmp')
    b11 = imresize(b11, 10)
    b12 = fonk3(b11)
    b13 = np.bincount(b12.ravel(), minlength=256)
    b14 = b13 / np.sum(b13)
    b15 = fonk4(b14)
    b16 = fonk5(b15)
    with open('b8.txt', 'w') as code_file:
        for pixel_value, b7 in b16.items():
            code_file.write(f'{pixel_value} {b7}\n')
    b17 = b11.shape[0] * b11.shape[1] * 8
    b10 = fonk6(b13, b16, b17)
    print(f'Compression achieved: {b10:.2f}%')
if b18 = = "__main__":
    fonk7()