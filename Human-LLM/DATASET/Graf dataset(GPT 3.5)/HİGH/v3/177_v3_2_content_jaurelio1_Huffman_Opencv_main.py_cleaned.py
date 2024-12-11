import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
def fonk1(b7, scale):
    b1 = int(b7.shape[1] * scale / 100)
    b2 = int(b7.shape[0] * scale / 100)
    return cv2.resize(b7, (b1, b2), b3 = cv2.INTER_AREA)
def fonk2(b7):
    return cv2.cvtColor(b7, cv2.COLOR_RGB2GRAY)
def fonk3(b9, b1, b2, b15):
    b4 = Huffman(b15)
    T, b5 = b4.compressOp(b9, b1, b2)
    return T, b5
def fonk4(T, b5, filename):
    with open(filename, 'b1') as file:
        for i in range(b5):
            file.write(str(T[i]) + ' ')
def fonk5(filename):
    with open(filename, 'r') as file:
        return file.read()
def fonk6(compressed_data, b14):
    b4 = Huffman(b14)
    with open('test.txt', 'r') as file1:
        return b4.decompressOp(file1)
if b6 = = '__main__':
    b7 = cv2.imread("img1.tif")
    b8 = fonk1(b7, scale=60)
    b9 = fonk2(b8)
    b10 = Node()
    b10.setFrequencePixels(b9)
    b11 = b10.returnArrayNode()
    b12 = Heap(b11)
    b13 = b12.returnHeapMinimum()
    b4 = Huffman(b13)
    b14 = b4.returnHuff()
    b15 = b4.goThroughTree(b14)
    T, b5 = fonk3(b9, b1=b9.shape[1], b2=b9.shape[0], b15=b15)
    fonk4(T, b5, 'test.txt')
    b16 = fonk5('test.txt')
    print(b16)
    cv2.waitKey(0)