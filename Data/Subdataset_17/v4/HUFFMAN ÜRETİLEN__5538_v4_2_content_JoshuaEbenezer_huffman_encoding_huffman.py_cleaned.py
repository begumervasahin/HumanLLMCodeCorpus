import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
from queue import PriorityQueue
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
    gray_img = np.rint(img[:,:,0] * 0.2989 + img[:,:,1] * 0.5870 + img[:,:,2] * 0.1140)
    return gray_img.astype(int)
def build_huffman_tree(probabilities):
    prq = PriorityQueue()
    for color, prob in enumerate(probabilities):
        leaf = Node()
        leaf.data = color
        leaf.prob = prob
        prq.put(leaf)
    while prq.qsize() > 1:
        left = prq.get()
        right = prq.get()
        new_node = Node()
        new_node.left = left
        new_node.right = right
        new_node.prob = left.prob + right.prob
        prq.put(new_node)
    return prq.get()
def huffman_traversal(root, tmp_array, f):
    if root.left is not None:
        tmp_array[huffman_traversal.count] = 1
        huffman_traversal.count += 1
        huffman_traversal(root.left, tmp_array, f)
        huffman_traversal.count -= 1
    if root.right is not None:
        tmp_array[huffman_traversal.count] = 0
        huffman_traversal.count += 1
        huffman_traversal(root.right, tmp_array, f)
        huffman_traversal.count -= 1
    if root.left is None and root.right is None:
        huffman_traversal.output_bits[root.data] = huffman_traversal.count
        bitstream = ''.join(str(bit) for bit in tmp_array[:huffman_traversal.count])
        f.write(f"{root.data} {bitstream}\n")
def main():
    img = imread('tiger.bmp')
    img = imresize(img, 10)
    gray_img = rgb2gray(img)
    hist = np.bincount(gray_img.ravel(), minlength=256)
    probabilities = hist / np.sum(hist)
    root_node = build_huffman_tree(probabilities)
    tmp_array = np.ones(64, dtype=int)
    huffman_traversal.output_bits = np.zeros(256, dtype=int)
    huffman_traversal.count = 0
    with open('codes.txt', 'w') as f:
        huffman_traversal(root_node, tmp_array, f)
    input_bits = img.shape[0] * img.shape[1] * 8
    compression = (1 - np.sum(huffman_traversal.output_bits * hist) / input_bits) * 100
    print(f"Compression is {compression:.2f} percent")
if __name__ == "__main__":
    main()