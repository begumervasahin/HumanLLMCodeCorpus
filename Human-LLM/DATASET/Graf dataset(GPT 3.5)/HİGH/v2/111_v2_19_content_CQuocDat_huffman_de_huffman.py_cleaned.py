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
            if node.b4 is None:
                b7 = class1()
                b7.b3 = 0
                node.b4 = b7
                b7.b1 = b6
                b7.b2 = True
                return
        if array[b6] == 1:
            if node.b5 is None:
                b7 = class1()
                b7.b3 = 1
                node.b5 = b7
                b7.b1 = b6
                b7.b2 = True
                return
    else:
        if array[b6] == 0:
            if node.b4 is None:
                b7 = class1()
                b7.b3 = 0
                node.b4 = b7
                b7.b2 = False
                fonk2(b7, array, b6 + 1)
            else:
                fonk2(node.b4, array, b6 + 1)
        if array[b6] == 1:
            if node.b5 is None:
                b7 = class1()
                b7.b3 = 1
                node.b5 = b7
                b7.b2 = False
                fonk2(b7, array, b6 + 1)
            else:
                fonk2(node.b5, array, b6 + 1)
def fonk3(b19):
    if b19 is None:
        return []
    if b19.b4 is None and b19.b5 is None:
        return [str(b19.b3)]
    b8 = fonk3(b19.b4)
    b9 = fonk3(b19.b5)
    b10 = b8 + b9
    b11 = []
    for leaf in b10:
        b11.append(str(b19.b3) + '-' + leaf)
    return b11
def fonk4(mang, node, chiso):
    if node.b2:
        b23.append(node.b1)
        b24.append(chiso)
        return
    else:
        if mang[chiso] == '0':
            fonk4(mang, node.b4, chiso + 1)
        if mang[chiso] == '1':
            fonk4(mang, node.b5, chiso + 1)
b12 = open('dictionary_meo.txt', 'r')
b13 = open('imageinBit_meo.txt', 'r')
b14 = []
for line in b12:
    b15 = line.split(' ')
    b16 = list(b15[1].strip())
    for a1 in range(len(b16)):
        b16[a1] = int(b16[a1])
    b14.append(b16)
b17 = int(''.join(str(b23) for b23 in b14.pop()))
b18 = int(''.join(str(b23) for b23 in b14.pop()))
print("Image dimensions:", b18, "x", b17)
b19 = class1()
for b6 in range(len(b14)):
    a1 = 0
    fonk2(b19, b14[b6], b6)
b20 = []
for line in b13:
    b20.append(line.split())
b21 = []
for b22 in b20:
    b22 = b22[0]
    b22 = list(b22)
    a2 = 0
    b23 = []
    b24 = []
    while a2 < len(b22) - 1:
        fonk4(b22, b19, a2)
        a2 = b24[-1]
    b21.append(b23)
b21 = np.array(b21, dtype=np.uint8)
cv2.imshow('DECOMPRESS', b21)
cv2.imwrite('meo-decompress.png', b21)
cv2.waitKey(0)
cv2.destroyAllWindows()
b12.close()
b13.close()