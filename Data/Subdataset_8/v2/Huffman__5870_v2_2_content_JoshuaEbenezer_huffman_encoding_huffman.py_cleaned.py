import numpy as np
from scipy.misc import imread, imresize
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
def convert_to_grayscale(img):
    grayscale_img = np.rint(img[:, :, 0] * 0.2989 + img[:, :, 1] * 0.5870 + img[:, :, 2] * 0.1140)
    grayscale_img = grayscale_img.astype(int)
    return grayscale_img
def get_two_smallest(data):
    smallest_index = second_smallest_index = 0
    smallest_value = second_smallest_value = 1
    for idx, element in enumerate(data):
        if element < smallest_value:
            second_smallest_value = smallest_value
            second_smallest_index = smallest_index
            smallest_value = element
            smallest_index = idx
        elif element < second_smallest_value and element != smallest_value:
            second_smallest_value = element
    return smallest_index, smallest_value, second_smallest_index, second_smallest_value
def build_huffman_tree(probabilities):
    priority_queue = queue.PriorityQueue()
    for color, probability in enumerate(probabilities):
        leaf_node = Node()
        leaf_node.data = color
        leaf_node.prob = probability
        priority_queue.put(leaf_node)
    while priority_queue.qsize() > 1:
        new_node = Node()
        left_node = priority_queue.get()
        right_node = priority_queue.get()
        new_node.left = left_node
        new_node.right = right_node
        new_probability = left_node.prob + right_node.prob
        new_node.prob = new_probability
        priority_queue.put(new_node)
    return priority_queue.get()
def traverse_huffman_tree(root_node, tmp_array, file):
    if root_node.left is not None:
        tmp_array[traverse_huffman_tree.count] = 1
        traverse_huffman_tree.count += 1
        traverse_huffman_tree(root_node.left, tmp_array, file)
        traverse_huffman_tree.count -= 1
    if root_node.right is not None:
        tmp_array[traverse_huffman_tree.count] = 0
        traverse_huffman_tree.count += 1
        traverse_huffman_tree(root_node.right, tmp_array, file)
        traverse_huffman_tree.count -= 1
    else:
        huffman_traversal.output_bits[root_node.data] = traverse_huffman_tree.count
        bitstream = ''.join(str(cell) for cell in tmp_array[1:traverse_huffman_tree.count])
        color = str(root_node.data)
        wr_str = color + ' ' + bitstream + '\n'
        file.write(wr_str)
image = imread('tiger.bmp')
image = imresize(image, 10)
grayscale_image = convert_to_grayscale(image)
histogram = np.bincount(grayscale_image.ravel(), minlength=256)
probabilities = histogram / np.sum(histogram)
root_node = build_huffman_tree(probabilities)
tmp_array = np.ones([64], dtype=int)
traverse_huffman_tree.output_bits = np.empty(256, dtype=int)
traverse_huffman_tree.count = 0
with open('codes.txt', 'w') as file:
    traverse_huffman_tree(root_node, tmp_array, file)
input_bits = image.shape[0] * image.shape[1] * 8
compression_ratio = (1 - np.sum(traverse_huffman_tree.output_bits * histogram) / input_bits) * 100
print('Compression ratio:', compression_ratio, 'percent')