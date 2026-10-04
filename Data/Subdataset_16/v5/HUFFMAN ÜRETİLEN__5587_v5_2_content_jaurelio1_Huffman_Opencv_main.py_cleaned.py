import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
def fonk1(b16, b1 = 60):
    b2 = cv2.imread(b16)
    b3 = int(b2.shape[1] * b1 / 100)
    b4 = int(b2.shape[0] * b1 / 100)
    b5 = (b3, b4)
    return cv2.resize(b2, b5, b6 = cv2.INTER_AREA)
def fonk2(b2):
    return cv2.cvtColor(b2, cv2.COLOR_RGB2GRAY)
def fonk3(b18, b4, b3):
    b7 = Node()
    b7.setFrequencePixels(b18, b4, b3)
    b8 = b7.returnArrayNode()
    b9 = Heap(b8)
    b10 = b9.returnHeapMinimum()
    b11 = Huffman(b10)
    b12 = b11.returnHuff()
    b13 = b11.goThroughTree(b12)
    compressed_data, b14 = b11.compressOp(b18, b3, b4, b13)
    return compressed_data, b14, b12, b11
def fonk4(compressed_data, b14, b15 = 'compressed_output.txt'):
    with open(b15, 'w') as output_file:
        output_file.write(' '.join(str(compressed_data[i]) for i in range(b14)))
def fonk5(input_path, b11, b12):
    with open(input_path, 'r') as input_file:
        return b11.decompressOp(input_file, b12)
def fonk6():
    b16 = "img1.tif"
    b17 = fonk1(b16)
    b18 = fonk2(b17)
    b4, b3 = b18.shape
    compressed_data, b14, b12, b11 = fonk3(b18, b4, b3)
    fonk4(compressed_data, b14)
    b19 = fonk5('compressed_output.txt', b11, b12)
    print("Decompressed Data:", b19)
    cv2.waitKey(0)
if b20 = = '__main__':
    fonk6()