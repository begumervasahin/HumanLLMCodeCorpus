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
    height_resized, width_resized, b7 = b6.shape
    b8 = cv2.cvtColor(b6, cv2.COLOR_RGB2GRAY)
    b9 = Node()
    b9.setFrequencePixels(b8, height_resized, width_resized)
    b10 = b9.returnArrayNode()
    b11 = Heap(b10)
    b12 = b11.returnHeapMinimum()
    b13 = Huffman(b12)
    b14 = b13.returnHuff()
    b15 = b13.goThroughTree(b14)
    compressed_data, b16 = b13.compressOp(b8, width_resized, height_resized, b15)
    b17 = 'compressed_image.txt'
    with open(b17, 'w') as file:
        file.write(' '.join(map(str, compressed_data[:b16])))
    with open(b17, 'r') as file:
        b18 = b13.decompressOp(file, b14)
    cv2.imshow("Original Image", b2)
    cv2.imshow("Resized Grayscale Image", b8)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b19 = = '__main__':
    fonk1()