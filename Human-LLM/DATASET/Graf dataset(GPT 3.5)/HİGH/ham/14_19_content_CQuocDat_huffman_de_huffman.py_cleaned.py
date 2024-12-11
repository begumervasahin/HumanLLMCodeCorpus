import numpy as np
import cv2
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(nut,b20,b6,index):
    if b6 = =len(b20)-1:
        if b20[b6]==0:
            if nut.b4 = =None:
                b7 = class1()
                b7.b3 = 0
                nut.b4 = b7
                b7.b1 = index
                b7.b2 = True
                return
        if b20[b6]==1:
            if nut.b5 = =None:
                b7 = class1()
                b7.b3 = 1
                nut.b5 = b7
                b7.b1 = index
                b7.b2 = True
                return
    else:
        if b20[b6]==0:
            if nut.b4 = =None:
                b7 = class1()
                b7.b3 = 0
                nut.b4 = b7
                b7.b2 = False
                fonk2(b7,b20,b6+1,index)
            else:
                fonk2(nut.b4,b20,b6+1,index)
        if b20[b6]==1:
            if nut.b5 = =None:
                b7 = class1()
                b7.b3 = 1
                nut.b5 = b7
                b7.b2 = False
                fonk2(b7,b20,b6+1,index)
            else:
                fonk2(nut.b5,b20,b6+1,index)
def fonk3(b19):
    if b19 is None:
        return []
    if (b19.b4 = = None and b19.b5 == None):
        return [str(b19.b3)]
    b8 = fonk3(b19.b4)
    b9 = fonk3(b19.b5)
    b10 = b8 + b9
    b11 = []
    for leaf in b10:
        b11.append(str(b19.b3) + '-'+ leaf)
    return b11
def fonk4(mang,nod,chiso):
    if nod.b2 = =True:
        b23.append(nod.b1)
        b24.append(chiso)
        return
    else:
        if mang[chiso]=='0':
            fonk4(mang,nod.b4,chiso+1)
        if mang[chiso]=='1':
            fonk4(mang,nod.b5,chiso+1)
b12 = open('dictionary_meo.txt','r')
b13 = open('imageinBit_meo.txt','r')
b14 = []
a1 = 0
for b6 in b12:
    b15 = b6.split(' ')
    b16 = list(b15[1])
    b16.pop()
    for b6 in range(0,len(b16)):
        b16[b6]=int(b16[b6])
    b14.append(b16)
    a1+=1
b17 = b14.pop()
b18 = b14.pop()
b17 = int(''.join(str(b23)for b23 in b17))
b18 = int(''.join(str(b23)for b23 in b18))
print(b18,b17)
b19 = class1()
for index in range(0,len(b14)):
    b6 = 0
    fonk2(b19,b14[index],b6,index)
b20 = []
b21 = []
for line in b13:
    b20.append(line.split())
for b6 in b20:
    b22 = b6[0]
    b22 = list(b22)
    a2 = 0
    b23 = []
    b24 = []
    while(a2<len(b22)-1):
        fonk4(b22,b19,a2)
        a2 = b24[len(b24)-1]
    b21.append(b23)
b21 = np.b20(b21,dtype=np.uint8)
cv2.imshow('DECOMPRESS',b21)
cv2.imwrite('meo-decompress.png',b21)
cv2.waitKey(0)
cv2.destroyAllWindows()