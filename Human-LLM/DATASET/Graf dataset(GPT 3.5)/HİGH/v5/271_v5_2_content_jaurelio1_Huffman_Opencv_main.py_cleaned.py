import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile
def fonk1(b15, scale):
    b1 = int(b15.shape[1] * scale / 100)
    b2 = int(b15.shape[0] * scale / 100)
    return cv2.resize(b15, (b1, b2), b3 = cv2.INTER_AREA)
def fonk2(b15):
    b4 = cv2.cvtColor(b15, cv2.COLOR_RGB2GRAY)
    b5 = Node()
    b5.set_frequence_pixels(b4)
    b6 = b5.return_array_node()
    b7 = Heap(b6)
    b8 = b7.return_heap_minimum()
    b9 = Huffman(b8)
    b10 = b9.return_huff()
    b11 = b9.traverse_tree(b10)
    b17, b12 = b9.compress_op(b4, b11)
    return b17, b12
def fonk3(data, filename):
    with open(filename, 'b1') as file:
        for i in range(len(data)):
            file.write(str(data[i]) + ' ')
def fonk4(filename):
    with open(filename, 'r') as file:
        return file.read()
def fonk5(b17, huff_tree):
    b13 = Huffman()
    return b13.decompress_op(b17, huff_tree)
if b14 = = '__main__':
    b15 = cv2.imread("img1.tif")
    b16 = fonk1(b15, scale=60)
    b17, b12 = fonk2(b16)
    fonk3(b17, 'test.txt')
    b17 = fonk4('test.txt')
    b18 = fonk5(b17, huff_tree=b10)
    print(b18)
    cv2.waitKey(0)