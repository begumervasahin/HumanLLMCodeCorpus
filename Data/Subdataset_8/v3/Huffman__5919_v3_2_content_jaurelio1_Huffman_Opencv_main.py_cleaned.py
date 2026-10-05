import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
def resize_image(image, scale):
    w = int(image.shape[1] * scale / 100)
    h = int(image.shape[0] * scale / 100)
    return cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
def compress_image(image_gray, w, h, D):
    huff = Huffman(D)
    T, index = huff.compressOp(image_gray, w, h)
    return T, index
def write_compressed_data(T, index, filename):
    with open(filename, 'w') as file:
        for i in range(index):
            file.write(str(T[i]) + ' ')
def read_compressed_data(filename):
    with open(filename, 'r') as file:
        return file.read()
def decompress_data(compressed_data, R):
    huff = Huffman(R)
    with open('test.txt', 'r') as file1:
        return huff.decompressOp(file1)
if __name__ == '__main__':
    image = cv2.imread("img1.tif")
    scaled_image = resize_image(image, scale=60)
    image_gray = convert_to_grayscale(scaled_image)
    node = Node()
    node.setFrequencePixels(image_gray)
    freq_array = node.returnArrayNode()
    heap = Heap(freq_array)
    S = heap.returnHeapMinimum()
    huff = Huffman(S)
    R = huff.returnHuff()
    D = huff.goThroughTree(R)
    T, index = compress_image(image_gray, w=image_gray.shape[1], h=image_gray.shape[0], D=D)
    write_compressed_data(T, index, 'test.txt')
    decompressed_data = read_compressed_data('test.txt')
    print(decompressed_data)
    cv2.waitKey(0)