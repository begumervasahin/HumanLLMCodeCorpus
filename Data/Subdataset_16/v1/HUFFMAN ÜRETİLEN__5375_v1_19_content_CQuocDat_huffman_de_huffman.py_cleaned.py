import numpy as np
import cv2
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(b13, bit_sequence, b6, index):
    if b6 = = len(bit_sequence) - 1:
        if bit_sequence[b6] == 0:
            if b13.b4 is None:
                b7 = class1()
                b7.b3 = 0
                b13.b4 = b7
                b7.b1 = index
                b7.b2 = True
                return
        if bit_sequence[b6] == 1:
            if b13.b5 is None:
                b7 = class1()
                b7.b3 = 1
                b13.b5 = b7
                b7.b1 = index
                b7.b2 = True
                return
    else:
        if bit_sequence[b6] == 0:
            if b13.b4 is None:
                b7 = class1()
                b7.b3 = 0
                b13.b4 = b7
                b7.b2 = False
                fonk2(b7, bit_sequence, b6 + 1, index)
            else:
                fonk2(b13.b4, bit_sequence, b6 + 1, index)
        if bit_sequence[b6] == 1:
            if b13.b5 is None:
                b7 = class1()
                b7.b3 = 1
                b13.b5 = b7
                b7.b2 = False
                fonk2(b7, bit_sequence, b6 + 1, index)
            else:
                fonk2(b13.b5, bit_sequence, b6 + 1, index)
def fonk3(bit_string, node, chiso):
    if node.b2:
        b16.append(node.b1)
        b17.append(chiso)
        return
    else:
        if bit_string[chiso] == '0':
            fonk3(bit_string, node.b4, chiso + 1)
        if bit_string[chiso] == '1':
            fonk3(bit_string, node.b5, chiso + 1)
def fonk4():
    with open('dictionary_meo.txt', 'r') as dict_file, open('imageinBit_meo.txt', 'r') as bit_file:
        b8 = []
        for line in dict_file:
            b9 = line.split(' ')
            b10 = list(b9[1].strip())
            b10 = [int(bit) for bit in b10]
            b8.append(b10)
        b11 = b8.pop()
        b12 = b8.pop()
        b11 = int(''.join(map(str, b11)))
        b12 = int(''.join(map(str, b12)))
        print(f"Image dimensions: {b12}x{b11}")
        b13 = class1()
        for index, b10 in enumerate(b8):
            fonk2(b13, b10, 0, index)
        b14 = []
        for line in bit_file:
            b15 = list(line.strip())
            a1 = 0
            global b16, b17
            b16 = []
            b17 = []
            while a1 < len(b15):
                fonk3(b15, b13, a1)
                a1 = b17[-1] + 1
            b14.append(b16)
        b14 = np.array(b14, dtype=np.uint8).reshape((b12, b11))
        cv2.imshow('DECOMPRESS', b14)
        cv2.imwrite('meo-decompress.png', b14)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if b18 = = "__main__":
    fonk4()