import numpy as np
import cv2
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(node, array, b6):
    if b6 = = len(array) - 1:
        if array[b6] == 0:
            fonk3(node, 0, b6)
        if array[b6] == 1:
            fonk3(node, 1, b6)
    else:
        if array[b6] == 0:
            fonk4(node, 0, array, b6 + 1)
        if array[b6] == 1:
            fonk4(node, 1, array, b6 + 1)
def fonk3(node, b8, b6):
    b7 = class1()
    b7.b3 = b8
    node.b4 if b8 = = 0 else node.b5 = b7
    b7.b1 = b6
    b7.b2 = True
def fonk4(node, b8, array, b6):
    if getattr(node, 'b4' if b8 = = 0 else 'b5') is None:
        b7 = class1()
        b7.b3 = b8
        setattr(node, 'b4' if b8 = = 0 else 'b5', b7)
        b7.b2 = False
        fonk2(b7, array, b6)
    else:
        fonk2(getattr(node, 'b4' if b8 = = 0 else 'b5'), array, b6)
def fonk5(b19):
    if b19 is None:
        return []
    if b19.b4 is None and b19.b5 is None:
        return [str(b19.b3)]
    b9 = fonk5(b19.b4)
    b10 = fonk5(b19.b5)
    b11 = b9 + b10
    b12 = [str(b19.b3) + '-' + leaf for leaf in b11]
    return b12
def fonk6(b21, node, b6):
    if node.b2:
        e.append(node.b1)
        b22.append(b6)
        return
    else:
        b13 = node.b4 if b21[b6] == '0' else node.b5
        fonk6(b21, b13, b6 + 1)
b14 = open('dictionary_meo.txt', 'r')
b15 = open('imageinBit_meo.txt', 'r')
b16 = []
for line in b14:
    b17 = line.split(' ')
    b16.append([int(bit) for bit in b17[1].strip()])
width, b18 = map(int, b16.pop())
print("Image dimensions:", b18, "x", width)
b19 = class1()
for b6, tree_bits in enumerate(b16):
    fonk2(b19, tree_bits, b6)
b20 = []
for code_line in b15:
    b21 = list(code_line[0])
    e, b22 = [], []
    fonk6(b21, b19, 0)
    b20.append(e)
b20 = np.array(b20, dtype=np.uint8)
cv2.imshow('DECOMPRESS', b20)
cv2.imwrite('meo-decompress.png', b20)
cv2.waitKey(0)
cv2.destroyAllWindows()
b14.close()
b15.close()