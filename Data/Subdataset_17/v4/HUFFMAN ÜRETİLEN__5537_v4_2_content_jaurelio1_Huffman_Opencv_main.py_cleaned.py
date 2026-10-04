import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
def main():
    image_path = "img1.tif"
    image = cv2.imread(image_path)
    scale_percent = 60
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dimensions = (width, height)
    resized_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)
    node = Node()
    node.setFrequencePixels(grayscale_image, height, width)
    pixel_nodes = node.returnArrayNode()
    heap = Heap(pixel_nodes)
    huffman_tree = heap.returnHeapMinimum()
    huffman = Huffman(huffman_tree)
    root_node = huffman.returnHuff()
    dictionary = huffman.goThroughTree(root_node)
    compressed_data, data_length = huffman.compressOp(grayscale_image, width, height, dictionary)
    with open('compressed_output.txt', 'w') as output_file:
        for i in range(data_length):
            output_file.write(str(compressed_data[i]) + ' ')
    with open('compressed_output.txt', 'r') as input_file:
        decompressed_data = huffman.decompressOp(input_file, root_node)
    print("Decompressed Data:", decompressed_data)
    cv2.waitKey(0)
if __name__ == '__main__':
    main()