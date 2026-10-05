import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
if __name__ == '__main__':
    image = cv2.imread("img1.tif")
    scale = 60
    w = int(image.shape[1] * scale / 100)
    h = int(image.shape[0] * scale / 100)
    d = (w, h)
    resized = cv2.resize(image, d, interpolation=cv2.INTER_AREA)
    (h_resized, w_resized, d_resized) = resized.shape
    image_copy = resized.copy()
    image_copy = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)
    node = Node()
    node.setFrequencePixels(image_copy, h_resized, w_resized)
    tmp = node.returnArrayNode()
    heap = Heap(tmp)
    S = heap.returnHeapMinimum()
    huff = Huffman(S)
    R = huff.returnHuff()
    D = huff.goThroughTree(R)
    T, index = huff.compressOp(image_copy, w_resized, h_resized, D)
    with open('test.txt', 'w') as file:
        for i in range(index):
            file.write(str(T[i]) + ' ')
    with open('test.txt', 'r') as file1:
        dc = huff.decompressOp(file1, R)
        print(dc)
    cv2.waitKey(0)