import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
import queue
class Node:
    def __init__(self, data=None, prob=None):
        self.prob = prob
        self.data = data
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.prob < other.prob
def rgb_to_gray(img):
    return np.rint(img[:, :, 0] * 0.2989 + img[:, :, 1] * 0.5870 + img[:, :, 2] * 0.1140).astype(int)
def build_huffman_tree(probabilities):
    priority_queue = queue.PriorityQueue()
    for pixel_value, prob in enumerate(probabilities):
        if prob > 0:
            priority_queue.put(Node(data=pixel_value, prob=prob))
    while priority_queue.qsize() > 1:
        left = priority_queue.get()
        right = priority_queue.get()
        merged_node = Node(prob=left.prob + right.prob, data=None)
        merged_node.left = left
        merged_node.right = right
        priority_queue.put(merged_node)
    return priority_queue.get()
def generate_huffman_codes(node, code=''):
    if node is None:
        return {}
    if node.left is None and node.right is None:
        return {node.data: code}
    codes = {}
    codes.update(generate_huffman_codes(node.left, code + '0'))
    codes.update(generate_huffman_codes(node.right, code + '1'))
    return codes
def calculate_compression_ratio(hist, huffman_codes, image_size):
    total_bits = sum(len(huffman_codes[val]) * count for val, count in enumerate(hist) if count > 0)
    compression_ratio = (1 - total_bits / image_size) * 100
    return compression_ratio
def main():
    img = imread('tiger.bmp')
    img = imresize(img, 10)
    gray_img = rgb_to_gray(img)
    hist = np.bincount(gray_img.ravel(), minlength=256)
    probabilities = hist / np.sum(hist)
    root_node = build_huffman_tree(probabilities)
    huffman_codes = generate_huffman_codes(root_node)
    with open('codes.txt', 'w') as code_file:
        for pixel_value, code in huffman_codes.items():
            code_file.write(f'{pixel_value} {code}\n')
    original_image_bits = img.shape[0] * img.shape[1] * 8
    compression_ratio = calculate_compression_ratio(hist, huffman_codes, original_image_bits)
    print(f'Compression achieved: {compression_ratio:.2f}%')
if __name__ == "__main__":
    main()