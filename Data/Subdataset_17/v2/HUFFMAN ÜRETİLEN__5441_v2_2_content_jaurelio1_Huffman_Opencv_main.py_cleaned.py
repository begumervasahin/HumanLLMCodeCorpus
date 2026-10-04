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
    height_resized, width_resized, _ = resized_image.shape
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)
    node = Node()
    node.setFrequencePixels(grayscale_image, height_resized, width_resized)
    node_array = node.returnArrayNode()
    heap = Heap(node_array)
    smallest_node = heap.returnHeapMinimum()
    huffman = Huffman(smallest_node)
    huffman_tree_root = huffman.returnHuff()
    huffman_dict = huffman.goThroughTree(huffman_tree_root)
    compressed_data, data_length = huffman.compressOp(grayscale_image, width_resized, height_resized, huffman_dict)
    compressed_file_path = 'compressed_image.txt'
    with open(compressed_file_path, 'w') as file:
        file.write(' '.join(map(str, compressed_data[:data_length])))
    with open(compressed_file_path, 'r') as file:
        decompressed_data = huffman.decompressOp(file, huffman_tree_root)
    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Grayscale Image", grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()