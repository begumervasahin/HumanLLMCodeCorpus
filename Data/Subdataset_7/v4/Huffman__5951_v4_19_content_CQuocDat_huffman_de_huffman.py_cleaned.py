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
        if bit_array[b6] == 0:
            if parent_node.b4 is None:
                b7 = class1()
                b7.b3 = 0
                parent_node.b4 = b7
                b7.b1 = index
                b7.b2 = True
                return
        elif bit_array[b6] == 1:
            if parent_node.b5 is None:
                b7 = class1()
                b7.b3 = 1
                parent_node.b5 = b7
                b7.b1 = index
                b7.b2 = True
                return
    else:
        if bit_array[b6] == 0:
            if parent_node.b4 is None:
                b7 = class1()
                b7.b3 = 0
                parent_node.b4 = b7
                b7.b2 = False
                fonk2(b7, bit_array, b6 + 1, index)
            else:
                fonk2(parent_node.b4, bit_array, b6 + 1, index)
        elif bit_array[b6] == 1:
            if parent_node.b5 is None:
                b7 = class1()
                b7.b3 = 1
                parent_node.b5 = b7
                b7.b2 = False
                fonk2(b7, bit_array, b6 + 1, index)
            else:
                fonk2(parent_node.b5, bit_array, b6 + 1, index)
def fonk3(b17, node, index):
    if node.b2:
        b18.append(node.b1)
        b19.append(index)
        return
    else:
        if b17[index] == '0':
            fonk3(b17, node.b4, index + 1)
        elif b17[index] == '1':
            fonk3(b17, node.b5, index + 1)
b8 = open('dictionary_meo.txt', 'r')
b9 = open('imageinBit_meo.txt', 'r')
b10 = []
for line in b8:
    b11 = line.split(' ')
    b12 = list(b11[1].rstrip())
    for i in range(len(b12)):
        b12[i] = int(b12[i])
    b10.append(b12)
b13 = int(''.join(str(e) for e in b10.pop()))
b14 = int(''.join(str(e) for e in b10.pop()))
print("Image Dimensions:", b14, b13)
b15 = class1()
for i in range(len(b10)):
    fonk2(b15, b10[i], 0, i)
b16 = []
for line in b9:
    b17 = line.split()[0]
    b12 = list(b17)
    a1 = 0
    b18 = []
    b19 = []
    while a1 < len(b12) - 1:
        fonk3(b12, b15, a1)
        a1 = b19[-1]
    b16.append(b18)
b16 = np.array(b16, dtype=np.uint8)
cv2.imshow('DECOMPRESS', b16)
cv2.imwrite('meo-decompress.png', b16)
cv2.waitKey(0)
cv2.destroyAllWindows()