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
    def fonk2(self, other):
        return self.b1 < other.b1
def fonk3(img):
    b6 = np.array([0.2989, 0.5870, 0.1140])
    b7 = np.dot(img[..., :3], b6)
    return b7.astype(int)
def fonk4(b3):
    b8 = np.argsort(b3)
    smallest_idx, b9 = b8[:2]
    smallest_val, b10 = b3[smallest_idx], b3[b9]
    return smallest_idx, smallest_val, b9, b10
def fonk5(b23):
    b11 = queue.PriorityQueue()
    for b18, probability in enumerate(b23):
        b12 = class1()
        b12.b3 = b18
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
def fonk6(b24, b25, file):
    if b24.b4 is not None:
        b25[traverse_huffman_tree.a1] = 1
        traverse_huffman_tree.a1 += 1
        fonk6(b24.b4, b25, file)
        traverse_huffman_tree.a1 -= 1
    if b24.b5 is not None:
        b25[traverse_huffman_tree.a1] = 0
        traverse_huffman_tree.a1 += 1
        fonk6(b24.b5, b25, file)
        traverse_huffman_tree.a1 -= 1
    else:
        b26[b24.b3] = traverse_huffman_tree.a1
        b17 = ''.join(str(cell) for cell in b25[1:traverse_huffman_tree.a1])
        b18 = str(b24.b3)
        b19 = b18 + ' ' + b17 + '\n'
        file.write(b19)
b20 = imread('tiger.bmp')
b20 = imresize(b20, 10)
b21 = fonk3(b20)
b22 = np.bincount(b21.ravel(), minlength=256)
b23 = b22 / np.sum(b22)
b24 = fonk5(b23)
b25 = np.ones([64], dtype=int)
b26 = np.empty(256, dtype=int)
traverse_huffman_tree.a1 = 0
with open('codes.txt', 'w') as file:
    fonk6(b24, b25, file)
b27 = b20.size * 8
b28 = (1 - np.sum(b26 * b22) / b27) * 100
print('Compression ratio:', b28, 'percent')