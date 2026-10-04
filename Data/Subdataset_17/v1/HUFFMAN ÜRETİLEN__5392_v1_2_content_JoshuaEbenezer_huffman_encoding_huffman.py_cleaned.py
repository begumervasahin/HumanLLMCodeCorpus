import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
import queue
class Node:
    def __init__(self):
        self.prob = None
        self.code = None
        self.data = None
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.prob < other.prob
    def __ge__(self, other):
        return self.prob > other.prob
def rgb2gray(img):
    gray_img = np.rint(img[:, :, 0] * 0.2989 + img[:, :, 1] * 0.5870 + img[:, :, 2] * 0.1140)
    gray_img = gray_img.astype(int)
    return gray_img
def tree(probabilities):
    prq = queue.PriorityQueue()
    for color, probability in enumerate(probabilities):
        if probability > 0:
            leaf = Node()
            leaf.data = color
            leaf.prob = probability
            prq.put(leaf)
    while prq.qsize() > 1:
        newnode = Node()
        l = prq.get()
        r = prq.get()
        newnode.left = l
        newnode.right = r
        newprob = l.prob + r.prob
        newnode.prob = newprob
        prq.put(newnode)
    return prq.get()
def huffman_traversal(root_node, tmp_array, f):
    if root_node.left is not None:
        tmp_array[huffman_traversal.count] = 1
        huffman_traversal.count += 1
        huffman_traversal(root_node.left, tmp_array, f)
        huffman_traversal.count -= 1
    if root_node.right is not None:
        tmp_array[huffman_traversal.count] = 0
        huffman_traversal.count += 1
        huffman_traversal(root_node.right, tmp_array, f)
        huffman_traversal.count -= 1
    else:
        huffman_traversal.output_bits[root_node.data] = huffman_traversal.count
        bitstream = ''.join(str(cell) for cell in tmp_array[1:huffman_traversal.count])
        color = str(root_node.data)
        wr_str = color + ' ' + bitstream + '\n'
        f.write(wr_str)
if __name__ == "__main__":
    img = imread('tiger.bmp')
    img = imresize(img, 10)
    gray_img = rgb2gray(img)
    hist = np.bincount(gray_img.ravel(), minlength=256)
    probabilities = hist / np.sum(hist)
    root_node = tree(probabilities)
    tmp_array = np.ones([64], dtype=int)
    huffman_traversal.output_bits = np.zeros(256, dtype=int)
    huffman_traversal.count = 0
    with open('codes.txt', 'w') as f:
        huffman_traversal(root_node, tmp_array, f)
    input_bits = img.shape[0] * img.shape[1] * 8
    compression = (1 - np.sum(huffman_traversal.output_bits * hist) / input_bits) * 100
    print('Compression is {:.2f} percent'.format(compression))