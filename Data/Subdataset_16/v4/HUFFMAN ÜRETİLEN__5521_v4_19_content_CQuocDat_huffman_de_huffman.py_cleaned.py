import numpy as np
import cv2
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(b10, b13, b6, b1):
    if b6 = = len(b13) - 1:
        if b13[b6] == 0:
            if b10.b4 is None:
                b10.b4 = class1()
                b10.b4.b3 = 0
                b10.b4.b1 = b1
                b10.b4.b2 = True
        elif b13[b6] == 1:
            if b10.b5 is None:
                b10.b5 = class1()
                b10.b5.b3 = 1
                b10.b5.b1 = b1
                b10.b5.b2 = True
    else:
        if b13[b6] == 0:
            if b10.b4 is None:
                b10.b4 = class1()
                b10.b4.b3 = 0
                b10.b4.b2 = False
            fonk2(b10.b4, b13, b6 + 1, b1)
        elif b13[b6] == 1:
            if b10.b5 is None:
                b10.b5 = class1()
                b10.b5.b3 = 1
                b10.b5.b2 = False
            fonk2(b10.b5, b13, b6 + 1, b1)
def fonk3(node, b13, b6):
    if node.b2:
        return node.b1, b6
    else:
        if b13[b6] == '0':
            return fonk3(node.b4, b13, b6 + 1)
        elif b13[b6] == '1':
            return fonk3(node.b5, b13, b6 + 1)
def fonk4(dictionary_file, image_file):
    with open(dictionary_file, 'r') as dict_file:
        b7 = [line.split() for line in dict_file]
    b8 = int(''.join(b7.pop(-1)))
    b9 = int(''.join(b7.pop(-1)))
    b10 = class1()
    for b6, (_, b13) in enumerate(b7):
        b11 = [int(bit) for bit in b13.strip()]
        fonk2(b10, b11, 0, b6)
    b12 = []
    with open(image_file, 'r') as file:
        for line in file:
            b13 = list(line.strip())
            a1 = 0
            b14 = []
            while a1 < len(b13):
                b1, a1 = fonk3(b10, b13, a1)
                b14.append(b1)
            b12.append(b14)
    b15 = np.array(b12, dtype=np.uint8)
    cv2.imshow('DECOMPRESS', b15)
    cv2.imwrite('meo-decompress.png', b15)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b16 = = "__main__":
    fonk4('dictionary_meo.txt', 'imageinBit_meo.txt')