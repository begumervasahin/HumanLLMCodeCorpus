import numpy as np
import cv2
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = False
        self.b3 = None
        self.b4 = None
def fonk2(b6, bit_sequence, grayscale_value):
    for b5 in bit_sequence:
        if b5 = = 0:
            if b6.b3 is None:
                b6.b3 = class1()
            b6 = b6.b3
        else:
            if b6.b4 is None:
                b6.b4 = class1()
            b6 = b6.b4
    b6.b2 = True
    b6.b1 = grayscale_value
def fonk3(b12, node):
    if node.b2:
        return node.b1, 0
    b7 = node.b3 if b12[0] == '0' else node.b4
    return fonk3(b12[1:], b7)
def fonk4(b10):
    b8 = int(''.join(map(str, b10.pop())))
    b9 = int(''.join(map(str, b10.pop())))
    return b8, b9
def fonk5():
    with open('dictionary_meo.txt', 'r') as dict_file, open('imageinBit_meo.txt', 'r') as bit_file:
        b10 = [list(map(int, line.split()[1].strip())) for line in dict_file]
        b8, b9 = fonk4(b10)
        print(f"Image dimensions: {b8}x{b9}")
        b6 = class1()
        for grayscale_value, bit_sequence in enumerate(b10):
            fonk2(b6, bit_sequence, grayscale_value)
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
        b11 = np.array(b11, dtype=np.uint8).reshape((b8, b9))
        cv2.imshow('Decompressed Image', b11)
        cv2.imwrite('meo-decompress.png', b11)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if b15 = = "__main__":
    fonk5()