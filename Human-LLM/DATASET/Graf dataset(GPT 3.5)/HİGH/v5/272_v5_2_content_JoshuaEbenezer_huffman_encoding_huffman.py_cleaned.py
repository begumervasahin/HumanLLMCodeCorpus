import numpy as np
from scipy.misc import imread, imresize
import queue
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(b21):
    b6 = np.rint(b21[:, :, 0] * 0.2989 + b21[:, :, 1] * 0.5870 + b21[:, :, 2] * 0.1140)
    b6 = b6.astype(int)
    return b6
def fonk3(b3):
    b7 = b10 = 0
    b8 = b9 = 1
    for idx, element in enumerate(b3):
        if element < b8:
            b9 = b8
            b10 = b7
            b8 = element
            b7 = idx
        elif element < b9 and element != b8:
            b9 = element
            b10 = idx
    return b7, b8, b10, b9
def fonk4(b23):
    b11 = queue.PriorityQueue()
    for b19, probability in enumerate(b23):
        b12 = class1()
        b12.b3 = b19
        b12.b1 = probability
        b11.put(b12)
    while b11.qsize() > 1:
        b13 = class1()
        b14 = b11.get()
        b15 = b11.get()
        b13.b4 = b14
        b13.b5 = b15
        b16 = b14.b1 + b15.b1
        b13.b1 = b16
        b11.put(b13)
    return b11.get()
def fonk5(b24, b25, b26):
    if b24.b4 is not None:
        b25[traverse_huffman_tree.a1] = 1
        traverse_huffman_tree.a1 += 1
        fonk5(b24.b4, b25, b26)
        traverse_huffman_tree.a1 -= 1
    if b24.b5 is not None:
        b25[traverse_huffman_tree.a1] = 0
        traverse_huffman_tree.a1 += 1
        fonk5(b24.b5, b25, b26)
        traverse_huffman_tree.a1 -= 1
    else:
        b17 = traverse_huffman_tree.a1
        b18 = ''.join(str(bit) for bit in b25[1:b17])
        b19 = str(b24.b3)
        b20 = f"{b19} {b18}\n"
        b26.write(b20)
    return
b21 = imread('tiger.bmp')
b21 = imresize(b21, 10)
b6 = fonk2(b21)
b22 = np.bincount(b6.ravel(), minlength=256)
b23 = b22 / np.sum(b22)
b24 = fonk4(b23)
b25 = np.ones([64], dtype=int)
traverse_huffman_tree.a1 = 0
b26 = open('codes.txt', 'w')
fonk5(b24, b25, b26)
b27 = b21.shape[0] * b21.shape[1] * 8
b28 = (1 - np.sum(traverse_huffman_tree.output_bits * b22) / b27) * 100
print('Compression ratio:', b28, 'percent')
b26.close()