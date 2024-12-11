b1 = 'Anindita'
import string
import sys
def fonk1(b10,key):
        b2 = ''
        for b3 in b10:
            b3 = (ord(b3)+int(key))
            if b3-int(key)==32:
                b3 = 32
            elif b3>ord('z'):
                b3-=26
            elif b3<ord('a'):
                b3+=26
            b3 = chr(b3)
            b2 = b2 +b3
        print(b2)
        return(b2)
def fonk2(b8,key):
        b4 = ''
        for b3 in b8:
            b3 = (ord(b3)-int(key))
            if b3 + int(key)==32:
                b3 = 32
            elif b3 > ord('z'):
                b3-=26
            elif b3 < ord('a'):
                b3+=26
            b3 = chr(b3)
            b4 = b4+b3
        return (b4)
def fonk3(b10, key):
    b5 = len(key)
    b6 = [ord(i) for i in key]
    b7 = [ord(i) for i in b10]
    b8 = ''
    for i in range(len(b7)):
        b3 = (b7[i] + b6[i % b5]) % 26
        b8 += chr(b3 + 65)
    return (b8)
def fonk4(b8,key):
    b5 = len(key)
    b6 = [ord(i) for i in key]
    b9 = [ord(i) for i in b8]
    b10 = ''
    for i in range(len(b9)):
        b3 = (b9[i] - b6[i % b5]) % 26
        b10 += chr(b3 + 65)
    return (b10)