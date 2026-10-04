import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
def fonk1():
    b1 = "img1.tif"
    b2 = cv2.imread(b1)
    a1 = 60
    b3 = int(b2.shape[1] * a1 / 100)
    b4 = int(b2.shape[0] * a1 / 100)
    b5 = (b3, b4)
    b6 = cv2.resize(b2, b5, interpolation=cv2.INTER_AREA)
    b7 = cv2.cvtColor(b6, cv2.COLOR_RGB2GRAY)
    b8 = Node()
    b8.setFrequencePixels(b7, b4, b3)
    b9 = b8.returnArrayNode()
    b10 = Heap(b9)
    b11 = b10.returnHeapMinimum()
    b12 = Huffman(b11)
    b13 = b12.returnHuff()
    b14 = b12.goThroughTree(b13)
    compressed_data, b15 = b12.compressOp(b7, b3, b4, b14)
    with open('compressed_output.txt', 'w') as output_file:
        for i in range(b15):
            output_file.write(str(compressed_data[i]) + ' ')
    with open('compressed_output.txt', 'r') as input_file:
        b16 = b12.decompressOp(input_file, b13)
    print("Decompressed Data:", b16)
    cv2.waitKey(0)
if b17 = = '__main__':
    fonk1()