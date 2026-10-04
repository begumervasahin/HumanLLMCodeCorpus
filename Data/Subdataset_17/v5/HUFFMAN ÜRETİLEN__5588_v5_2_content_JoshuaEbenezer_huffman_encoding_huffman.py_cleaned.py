import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imresize
from queue import PriorityQueue
class Node:
    def __init__(self, prob=None, data=None):
        self.prob = prob
        self.data = data
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.prob < other.prob
def rgb_to_gray(img):
    return np.rint(img[:, :, 0] * 0.2989 + img[:, :, 1] * 0.5870 + img[:, :, 2] * 0.1140).astype(int)
def build_huffman_tree(probabilities):
    priority_queue = PriorityQueue()
    for value, prob in enumerate(probabilities):
        if prob > 0:
            priority_queue.put(Node(prob=prob, data=value))
    while priority_queue.qsize() > 1:
        left = priority_queue.get()
        right = priority_queue.get()
        merged_node = Node(prob=left.prob + right.prob, data=None)
        merged_node.left = left
        merged_node.right = right
        priority_queue.put(merged_node)
    return priority_queue.get()
def traverse_huffman_tree(node, path, codebook):
    if node is not None:
        if node.data is not None:
            codebook[node.data] = path
        traverse_huffman_tree(node.left, path + '0', codebook)
        traverse_huffman_tree(node.right, path + '1', codebook)
def save_huffman_codes(codebook, filename='codes.txt'):
    with open(filename, 'w') as file:
        for value, code in codebook.items():
            file.write(f"{value} {code}\n")
def calculate_compression(hist, codebook, original_bits):
    compressed_bits = sum(len(codebook[value]) * freq for value, freq in enumerate(hist) if value in codebook)
    compression_ratio = (1 - compressed_bits / original_bits) * 100
    return compression_ratio
def main():
    img = imread('tiger.bmp')
    img = imresize(img, 10)
    gray_img = rgb_to_gray(img)
    hist = np.bincount(gray_img.ravel(), minlength=256)
    probabilities = hist / hist.sum()
    root_node = build_huffman_tree(probabilities)
    codebook = {}
    traverse_huffman_tree(root_node, '', codebook)
    save_huffman_codes(codebook)
    original_bits = img.size * 8
    compression = calculate_compression(hist, codebook, original_bits)
    print(f"Compression is {compression:.2f}%")
if __name__ == "__main__":
    main()