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
    image_gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
    node = Node()
    node.setFrequencePixels(image_gray, h_resized, w_resized)
    freq_array = node.returnArrayNode()
    heap = Heap(freq_array)
    S = heap.returnHeapMinimum()
    huff = Huffman(S)
    R = huff.returnHuff()
    D = huff.goThroughTree(R)
    T, index = huff.compressOp(image_gray, w_resized, h_resized, D)
    with open('test.txt', 'w') as file:
        for i in range(index):
            file.write(str(T[i]) + ' ')
    with open('test.txt', 'r') as file1:
        decompressed_data = huff.decompressOp(file1, R)
        print(decompressed_data)
    cv2.waitKey(0)