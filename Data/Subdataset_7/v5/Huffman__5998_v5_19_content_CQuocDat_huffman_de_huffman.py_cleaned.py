import numpy as np
import cv2
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(parent_node, bit_array, b6, index):
    if b6 = = len(bit_array) - 1:
        b7 = parent_node.b4 if bit_array[b6] == 0 else parent_node.b5
        if b7 is None:
            b8 = class1()
            b8.b3 = bit_array[b6]
            b7 = parent_node.b4 if bit_array[b6] == 0 else parent_node.b5
            b7 = b8
            b8.b1 = index
            b8.b2 = True
    else:
        b7 = parent_node.b4 if bit_array[b6] == 0 else parent_node.b5
        if b7 is None:
            b8 = class1()
            b8.b3 = bit_array[b6]
            b7 = b8
            b8.b2 = False
            fonk2(b7, bit_array, b6 + 1, index)
        else:
            fonk2(b7, bit_array, b6 + 1, index)
def fonk3(code, node, index):
    if node.b2:
        b13.append(node.b1)
        b15.append(index)
    else:
        if code[index] == '0':
            fonk3(code, node.b4, index + 1)
        elif code[index] == '1':
            fonk3(code, node.b5, index + 1)
def fonk4():
    b9 = []
    for line in b18:
        b10 = [int(bit) for bit in line.split(' ')[1].rstrip()]
        b9.append(b10)
    width, b11 = b9.pop(), b9.pop()
    return b9, width, b11
def fonk5(b19, b16):
    b12 = []
    for line in b19:
        b10 = list(line.split()[0])
        a1 = 0
        b13 = []
        while a1 < len(b10) - 1:
            fonk3(b10, b16, a1)
            a1 = b15[-1]
        b12.append(b13)
    return np.array(b12, b14 = np.uint8)
def fonk6():
    global b13, b15
    b13, b15 = [], []
    b9, width, b11 = fonk4()
    b16 = class1()
    for i, b10 in enumerate(b9):
        fonk2(b16, b10, 0, i)
    b12 = fonk5(b19, b16)
    print("Image Dimensions:", b11, width)
    cv2.imshow('DECOMPRESS', b12)
    cv2.imwrite('meo-decompress.png', b12)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b17 = = "__main__":
    b18 = open('dictionary_meo.txt', 'r')
    b19 = open('imageinBit_meo.txt', 'r')
    fonk6()