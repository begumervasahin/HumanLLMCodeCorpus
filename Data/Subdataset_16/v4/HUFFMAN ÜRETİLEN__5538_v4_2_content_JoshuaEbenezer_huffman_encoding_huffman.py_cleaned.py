import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
from queue import PriorityQueue
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
def fonk4(b11):
    b6 = np.rint(b11[:,:,0] * 0.2989 + b11[:,:,1] * 0.5870 + b11[:,:,2] * 0.1140)
    return b6.astype(int)
def fonk5(b13):
    b7 = PriorityQueue()
    for color, b1 in enumerate(b13):
        b8 = class1()
        b8.b3 = color
        b8.b1 = b1
        b7.put(b8)
    while b7.qsize() > 1:
        b4 = b7.get()
        b5 = b7.get()
        b9 = class1()
        b9.b4 = b4
        b9.b5 = b5
        b9.b1 = b4.b1 + b5.b1
        b7.put(b9)
    return b7.get()
def fonk6(root, b15, f):
    if root.b4 is not None:
        b15[huffman_traversal.a1] = 1
        huffman_traversal.a1 += 1
        fonk6(root.b4, b15, f)
        huffman_traversal.a1 -= 1
    if root.b5 is not None:
        b15[huffman_traversal.a1] = 0
        huffman_traversal.a1 += 1
        fonk6(root.b5, b15, f)
        huffman_traversal.a1 -= 1
    if root.b4 is None and root.b5 is None:
        huffman_traversal.b16[root.b3] = huffman_traversal.a1
        b10 = ''.join(str(bit) for bit in b15[:huffman_traversal.a1])
        f.write(f"{root.b3} {b10}\n")
def fonk7():
    b11 = imread('tiger.bmp')
    b11 = imresize(b11, 10)
    b6 = fonk4(b11)
    b12 = np.bincount(b6.ravel(), minlength=256)
    b13 = b12 / np.sum(b12)
    b14 = fonk5(b13)
    b15 = np.ones(64, dtype=int)
    huffman_traversal.b16 = np.zeros(256, dtype=int)
    huffman_traversal.a1 = 0
    with open('codes.txt', 'w') as f:
        fonk6(b14, b15, f)
    b17 = b11.shape[0] * b11.shape[1] * 8
    b18 = (1 - np.sum(huffman_traversal.b16 * b12) / b17) * 100
    print(f"Compression is {b18:.2f} percent")
if b19 = = "__main__":
    fonk7()