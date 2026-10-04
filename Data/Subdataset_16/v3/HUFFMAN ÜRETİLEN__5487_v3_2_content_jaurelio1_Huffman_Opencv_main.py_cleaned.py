import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
def fonk1(b12, b1 = 60):
    b2 = cv2.imread(b12)
    b3 = int(b2.shape[1] * b1 / 100)
    b4 = int(b2.shape[0] * b1 / 100)
    b5 = cv2.resize(b2, (b3, b4), interpolation=cv2.INTER_AREA)
    return b5
def fonk2(b2):
    return cv2.cvtColor(b2, cv2.COLOR_RGB2GRAY)
def fonk3(b14):
    b4, b3 = b14.shape
    b6 = Node()
    b6.setFrequencePixels(b14, b4, b3)
    return b6.returnArrayNode()
def fonk4(b15):
    b7 = Heap(b15)
    b8 = b7.returnHeapMinimum()
    b9 = Huffman(b8)
    return b9.returnHuff()
def fonk5(b14, b16):
    b4, b3 = b14.shape
    b9 = Huffman(b16)
    b10 = b9.goThroughTree(b16)
    compressed_data, b11 = b9.compressOp(b14, b3, b4, b10)
    return compressed_data, b11, b10
def fonk6(compressed_data, b11, output_file):
    with open(output_file, 'w') as file:
        file.write(' '.join(map(str, compressed_data[:b11])))
def fonk7(file_path, b16):
    b9 = Huffman(b16)
    with open(file_path, 'r') as file:
        return b9.decompressOp(file, b16)
def fonk8(original_image, b14):
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Resized Grayscale Image", b14)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def fonk9():
    b12 = "img1.tif"
    b13 = 'compressed_image.txt'
    b5 = fonk1(b12)
    b14 = fonk2(b5)
    b15 = fonk3(b14)
    b16 = fonk4(b15)
    compressed_data, b11, b17 = fonk5(b14, b16)
    fonk6(compressed_data, b11, b13)
    b18 = fonk7(b13, b16)
    fonk8(cv2.imread(b12), b14)
if b19 = = '__main__':
    fonk9()