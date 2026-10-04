import numpy as np
import cv2
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = False
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(b8, b14, b1, b6 = 0):
    if b6 = = len(b14):
        b8.b1 = b1
        b8.b2 = True
        return
    b7 = b14[b6]
    if b7 = = 0:
        if b8.b4 is None:
            b8.b4 = class1()
        fonk2(b8.b4, b14, b1, b6 + 1)
    elif b7 = = 1:
        if b8.b5 is None:
            b8.b5 = class1()
        fonk2(b8.b5, b14, b1, b6 + 1)
def fonk3(node, b14, b6):
    if node.b2:
        return node.b1, b6
    b7 = b14[b6]
    if b7 = = '0':
        return fonk3(node.b4, b14, b6 + 1)
    elif b7 = = '1':
        return fonk3(node.b5, b14, b6 + 1)
def fonk4(dictionary_file, image_file):
    b8 = class1()
    with open(dictionary_file, 'r') as dict_file:
        b9 = [line.split() for line in dict_file]
    b10 = int(b9.pop(-1)[0])
    b11 = int(b9.pop(-1)[0])
    for b1, b14 in enumerate(b9):
        b12 = [int(b7) for b7 in b14[0]]
        fonk2(b8, b12, b1)
    b13 = []
    with open(image_file, 'r') as file:
        for line in file:
            b14 = list(line.strip())
            a1 = 0
            b15 = []
            while a1 < len(b14):
                b1, a1 = fonk3(b8, b14, a1)
                b15.append(b1)
            b13.append(b15)
    b16 = np.array(b13, dtype=np.uint8)
    cv2.imshow('Decompressed Image', b16)
    cv2.imwrite('decompressed_image.png', b16)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b17 = = "__main__":
    fonk4('dictionary_meo.txt', 'imageinBit_meo.txt')