import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
import queue
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
    def fonk2(self, other):
        return self.b1 < other.b1
    def fonk3(self, other):
        return self.b1 > other.b1
def fonk4(b17):
    b6 = np.rint(b17[:, :, 0] * 0.2989 + b17[:, :, 1] * 0.5870 + b17[:, :, 2] * 0.1140)
    b6 = b6.astype(int)
    return b6
def fonk5(b19):
    b7 = queue.PriorityQueue()
    for b14, probability in enumerate(b19):
        if probability > 0:
            b8 = class1()
            b8.b3 = b14
            b8.b1 = probability
            b7.put(b8)
    while b7.qsize() > 1:
        b9 = class1()
        b10 = b7.get()
        b11 = b7.get()
        b9.b4 = b10
        b9.b5 = b11
        b12 = b10.b1 + b11.b1
        b9.b1 = b12
        b7.put(b9)
    return b7.get()
def fonk6(b20, b21, f):
    if b20.b4 is not None:
        b21[huffman_traversal.a1] = 1
        huffman_traversal.a1 += 1
        fonk6(b20.b4, b21, f)
        huffman_traversal.a1 -= 1
    if b20.b5 is not None:
        b21[huffman_traversal.a1] = 0
        huffman_traversal.a1 += 1
        fonk6(b20.b5, b21, f)
        huffman_traversal.a1 -= 1
    else:
        huffman_traversal.b22[b20.b3] = huffman_traversal.a1
        b13 = ''.join(str(cell) for cell in b21[1:huffman_traversal.a1])
        b14 = str(b20.b3)
        b15 = b14 + ' ' + b13 + '\n'
        f.write(b15)
if b16 = = "__main__":
    b17 = imread('tiger.bmp')
    b17 = imresize(b17, 10)
    b6 = fonk4(b17)
    b18 = np.bincount(b6.ravel(), minlength=256)
    b19 = b18 / np.sum(b18)
    b20 = fonk5(b19)
    b21 = np.ones([64], dtype=int)
    huffman_traversal.b22 = np.zeros(256, dtype=int)
    huffman_traversal.a1 = 0
    with open('codes.txt', 'w') as f:
        fonk6(b20, b21, f)
    b23 = b17.shape[0] * b17.shape[1] * 8
    b24 = (1 - np.sum(huffman_traversal.b22 * b18) / b23) * 100
    print('Compression is {:.2f} percent'.format(b24))