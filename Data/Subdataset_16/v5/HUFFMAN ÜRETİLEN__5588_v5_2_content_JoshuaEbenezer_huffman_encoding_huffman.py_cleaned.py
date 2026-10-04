import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imresize
from queue import PriorityQueue
class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
    def fonk2(self, other):
        return self.b1 < other.b1
def fonk3(b10):
    return np.rint(b10[:, :, 0] * 0.2989 + b10[:, :, 1] * 0.5870 + b10[:, :, 2] * 0.1140).astype(int)
def fonk4(b13):
    b5 = PriorityQueue()
    for value, b1 in enumerate(b13):
        if b1 > 0:
            b5.put(class1(b1 = b1, b2=value))
    while b5.qsize() > 1:
        b3 = b5.get()
        b4 = b5.get()
        b6 = class1(b1=b3.b1 + b4.b1, b2=None)
        b6.b3 = b3
        b6.b4 = b4
        b5.put(b6)
    return b5.get()
def fonk5(node, path, b15):
    if node is not None:
        if node.b2 is not None:
            b15[node.b2] = path
        fonk5(node.b3, path + '0', b15)
        fonk5(node.b4, path + '1', b15)
def fonk6(b15, b7 = 'codes.txt'):
    with open(b7, 'w') as file:
        for value, code in b15.items():
            file.write(f"{value} {code}\n")
def fonk7(b12, b15, b16):
    b8 = sum(len(b15[value]) * freq for value, freq in enumerate(b12) if value in b15)
    b9 = (1 - b8 / b16) * 100
    return b9
def fonk8():
    b10 = imread('tiger.bmp')
    b10 = imresize(b10, 10)
    b11 = fonk3(b10)
    b12 = np.bincount(b11.ravel(), minlength=256)
    b13 = b12 / b12.sum()
    b14 = fonk4(b13)
    b15 = {}
    fonk5(b14, '', b15)
    fonk6(b15)
    b16 = b10.size * 8
    b17 = fonk7(b12, b15, b16)
    print(f"Compression is {b17:.2f}%")
if b18 = = "__main__":
    fonk8()