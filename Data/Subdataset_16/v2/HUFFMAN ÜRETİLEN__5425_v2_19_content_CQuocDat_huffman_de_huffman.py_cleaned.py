import numpy as np
import cv2
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = False
        self.b3 = None
        self.b4 = None
def fonk2(b6, b8, index):
    for b5 in b8:
        if b5 = = 0:
            if b6.b3 is None:
                b6.b3 = class1()
            b6 = b6.b3
        else:
            if b6.b4 is None:
                b6.b4 = class1()
            b6 = b6.b4
    b6.b2 = True
    b6.b1 = index
def fonk3(b12, node):
    if node.b2:
        return node.b1, 0
    if b12[0] == '0':
        return fonk3(b12[1:], node.b3)
    else:
        return fonk3(b12[1:], node.b4)
def fonk4():
    with open('dictionary_meo.txt', 'r') as dict_file, open('imageinBit_meo.txt', 'r') as bit_file:
        b7 = []
        for line in dict_file:
            b8 = list(map(int, line.split()[1].strip()))
            b7.append(b8)
        b9 = int(''.join(map(str, b7.pop())))
        b10 = int(''.join(map(str, b7.pop())))
        print(f"Image dimensions: {b9}x{b10}")
        b6 = class1()
        for index, b8 in enumerate(b7):
            fonk2(b6, b8, index)
        b11 = []
        for line in bit_file:
            b12 = line.strip()
            b13 = []
            a1 = 0
            while a1 < len(b12):
                gray_value, b14 = fonk3(b12[a1:], b6)
                b13.append(gray_value)
                a1 += b14 + 1
            b11.append(b13)
        b11 = np.array(b11, dtype=np.uint8).reshape((b9, b10))
        cv2.imshow('Decompressed Image', b11)
        cv2.imwrite('meo-decompress.png', b11)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if b15 = = "__main__":
    fonk4()