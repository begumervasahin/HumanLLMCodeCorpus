import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
def resize_image(image, scale):
    w = int(image.shape[1] * scale / 100)
    h = int(image.shape[0] * scale / 100)
    return cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
def compress_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    node = Node()
    node.set_frequence_pixels(gray_image)
    node_array = node.return_array_node()
    heap = Heap(node_array)
    min_heap = heap.return_heap_minimum()
    huffman = Huffman(min_heap)
    huff_code = huffman.return_huff()
    huff_dict = huffman.traverse_tree(huff_code)
    compressed_data, index = huffman.compress_op(gray_image, huff_dict)
    return compressed_data, index
def write_compressed_data(data, filename):
    with open(filename, 'w') as file:
        for i in range(len(data)):
            file.write(str(data[i]) + ' ')
def read_compressed_data(filename):
    with open(filename, 'r') as file:
        return file.read()
def decompress_image(compressed_data, huff_tree):
    huff = Huffman()
    return huff.decompress_op(compressed_data, huff_tree)
if __name__ == '__main__':
    image = cv2.imread("img1.tif")
    resized_image = resize_image(image, scale=60)
    compressed_data, index = compress_image(resized_image)
    write_compressed_data(compressed_data, 'test.txt')
    compressed_data = read_compressed_data('test.txt')
    decompressed_data = decompress_image(compressed_data, huff_tree=huff_code)
    print(decompressed_data)
    cv2.waitKey(0)