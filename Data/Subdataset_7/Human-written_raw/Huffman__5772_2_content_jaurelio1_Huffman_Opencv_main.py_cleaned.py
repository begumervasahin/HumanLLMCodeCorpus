import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
if b1 = = '__main__':
    b2 = cv2.imread("img1.tif")
    a1 = 60
    b3 = int(b2.shape[1]*a1 / 100)
    b4 = int(b2.shape[0]*a1 / 100)
    b5 = (b3, b4)
    b6 = cv2.resize(b2, b5, interpolation=cv2.INTER_AREA)
    (h_resized, w_resized, d_resized) = b6.shape
    b7 = b6.copy()
    b7 = cv2.cvtColor(b7, cv2.COLOR_RGB2GRAY)
    b8 = Node()
    b8.setFrequencePixels(b7, h_resized, w_resized)
    b9 = b8.returnArrayNode()
    b10 = Heap(b9)
    b11 = b10.returnHeapMinimum()
    b12 = Huffman(b11)
    b13 = b12.returnHuff()
    b14 = b12.goThroughTree(b13)
    T, b15 = b12.compressOp(b7, w_resized, h_resized, b14)
    b16 = open('test.txt', 'b3')
    for i in range(b15):
        b16.write(str(T[i])+' ')
    b17 = open('test.txt', 'r')
    b18 = b12.decompressOp(b17, b13)
    print(b18)
    b16.close()
    b17.close()
    cv2.waitKey(0)