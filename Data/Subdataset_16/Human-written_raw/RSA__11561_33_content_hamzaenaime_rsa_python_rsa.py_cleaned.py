import math
import random
import sys
def fonk1(a, b1):
    while b1:
        a, b1 = b1, a % b1
    return a
def fonk2(b2):
    if b2 > 1:
        if b2 = = 0:
            return True
        else:
            for b3 in range(2, b2):
                if b2 % b3 = = 0:
                    return False
            return True
    else:
        print("nombre invalide")
def fonk3():
    b4 = list()
    for b3 in range(2, 50):
        if fonk2(b3):
            b4.append(b3)
    return b4
def fonk4():
    b5 = random.randint(0, len(fonk3()))
    return fonk3()[b5]
def fonk5():
    b6 = fonk4()
    b7 = fonk4()
    while(b6 = = b7):
        b6 = fonk4()
        b7 = fonk4()
    b2 = b6*b7
    b8 = (b6-1)*(b7-1)
    return [b8, b2]
def fonk6(b9,  b8):
    b9 = b9 % b8
    for b20 in range(1, b8):
        if (b9*b20) % b8 = = 1:
            return b20
def fonk7(b8):
    if (b8 > 2):
        b9 = random.randint(1, b8)
        b10 = fonk1(b8, b9)
        while b10 != 1:
            b9 = random.randint(1, b8)
            b10 = fonk1(b8, b9)
        return b9
def fonk8(b13):
    b11 = list()
    for b3 in range(0, len(b13)):
        b11.append(ord(b13[b3]))
    return b11
def fonk9(code_ascii, b2, b9):
    b12 = list()
    b13 = str()
    for b3 in range(0, len(code_ascii)):
        b14 = int((code_ascii[b3] ** b9) % b2)
        b12.append(b14)
        b13 += str(b14)
    print("b12 b13 : " + b13)
    return b12
def fonk10(b21, b2, b20):
    b15 = list()
    b16 = str()
    for b3 in range(0, len(b21)):
        b17 = int((b21[b3] ** b20) % b2)
        b16 += chr(b17)
    print("uncrypted b13 : " + b16)
b18 = fonk5()
b19 = b18[0]
b2 = b18[1]
b9 = fonk7(b19)
b20 = fonk6(b9, b19)
b13 = input("Enter Your Message : ")
b21 = fonk9(fonk8(b13), b2, b9)
fonk10(b21,  b2, b20)