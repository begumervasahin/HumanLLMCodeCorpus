import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
def load_and_resize_image(image_path, scale_percent=60):
    image = cv2.imread(image_path)
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dimensions = (width, height)
    return cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
def process_image_with_huffman(grayscale_image, height, width):
    node = Node()
    node.setFrequencePixels(grayscale_image, height, width)
    pixel_nodes = node.returnArrayNode()
    heap = Heap(pixel_nodes)
    huffman_tree = heap.returnHeapMinimum()
    huffman = Huffman(huffman_tree)
    root_node = huffman.returnHuff()
    dictionary = huffman.goThroughTree(root_node)
    compressed_data, data_length = huffman.compressOp(grayscale_image, width, height, dictionary)
    return compressed_data, data_length, root_node, huffman
def save_compressed_data(compressed_data, data_length, output_path='compressed_output.txt'):
    with open(output_path, 'w') as output_file:
        output_file.write(' '.join(str(compressed_data[i]) for i in range(data_length)))
def load_and_decompress_data(input_path, huffman, root_node):
    with open(input_path, 'r') as input_file:
        return huffman.decompressOp(input_file, root_node)
def main():
    image_path = "img1.tif"
    resized_image = load_and_resize_image(image_path)
    grayscale_image = convert_to_grayscale(resized_image)
    height, width = grayscale_image.shape
    compressed_data, data_length, root_node, huffman = process_image_with_huffman(grayscale_image, height, width)
    save_compressed_data(compressed_data, data_length)
    decompressed_data = load_and_decompress_data('compressed_output.txt', huffman, root_node)
    print("Decompressed Data:", decompressed_data)
    cv2.waitKey(0)
if __name__ == '__main__':
    main()