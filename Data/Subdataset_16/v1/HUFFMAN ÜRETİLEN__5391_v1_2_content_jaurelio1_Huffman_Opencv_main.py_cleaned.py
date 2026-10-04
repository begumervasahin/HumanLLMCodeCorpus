import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
if b1 = = '__main__':
    b2 = cv2.imread("img1.tif")
    a1 = 60
    b3 = int(b2.shape[1] * a1 / 100)
    b4 = int(b2.shape[0] * a1 / 100)
    b5 = (b3, b4)
    b6 = cv2.resize(b2, b5, interpolation=cv2.INTER_AREA)
    h_resized, w_resized, b7 = b6.shape
    b8 = cv2.cvtColor(b6.copy(), cv2.COLOR_RGB2GRAY)
    b9 = Node()
    b9.setFrequencePixels(b8, h_resized, w_resized)
    b10 = b9.returnArrayNode()
    b11 = Heap(b10)
    b12 = b11.returnHeapMinimum()
    b13 = Huffman(b12)
    b14 = b13.returnHuff()
    b15 = b13.goThroughTree(b14)
    compressed_data, b16 = b13.compressOp(b8, w_resized, h_resized, b15)
    with open('compressed_image.txt', 'w') as file:
        for i in range(b16):
            file.write(str(compressed_data[i]) + ' ')
    with open('compressed_image.txt', 'r') as file1:
        b17 = b13.decompressOp(file1, b14)
    print(b17)
    cv2.imshow("Original Image", b2)
    cv2.imshow("Resized Grayscale Image", b8)
    cv2.waitKey(0)
    cv2.destroyAllWindows()