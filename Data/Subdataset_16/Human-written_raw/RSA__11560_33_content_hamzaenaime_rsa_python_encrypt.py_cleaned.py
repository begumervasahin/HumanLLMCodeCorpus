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
    for b18 in range(1, b8):
        if (b9*b18) % b8 = = 1:
            return b18
def fonk7(b8):
    if (b8 > 2):
        b9 = random.randint(1, b8)
        b10 = fonk1(b8, b9)
        while b10 != 1:
            b9 = random.randint(1, b8)
            b10 = fonk1(b8, b9)
        return b9
b11 = str(sys.argv[1])
def fonk8(b14):
    b12 = list()
    for b3 in range(0, len(b14)):
        b12.append(ord(b14[b3]))
    return b12
def fonk9(code_ascii, N, E):
    b2 = int(N)
    b9 = int(E)
    b13 = list()
    b14 = str()
    for b3 in range(0, len(code_ascii)):
        b15 = int((code_ascii[b3] ** b9) % b2)
        b13.append(b15)
        b14 += str(b15)
    return b13
b16 = fonk5()
b17 = b16[0]
b2 = b16[1]
b9 = fonk7(b17)
b18 = fonk6(b9, b17)
print("public key : ("+str(b2)+","+str(b9)+")")
print("private key : ("+str(b2)+","+str(b18)+")")
print(fonk9(fonk8(b11),b2,b9))
sys.stdout.flush()