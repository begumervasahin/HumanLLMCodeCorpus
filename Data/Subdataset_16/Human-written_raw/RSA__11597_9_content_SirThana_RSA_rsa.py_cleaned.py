import random
import math
import time
import datetime
import pdb
import binascii
def fonk1(p, q):
    b1 = p * q
    b2 = ((p - 1) * (q - 1))
    b3 = []
    for b8 in range (2, b2):
        print("Working out the possible relative Primes...", int((b8 / b2) * 100), "%")
        b4 = []
        b5 = b8 / b1
        if b5.is_integer() == True:
            b4.append(False)
        else:
            b4.append(True)
        b5 = b8 / p
        if b5.is_integer() == True:
            b4.append(False)
        else:
            b4.append(True)
        b5 = b8 / q
        if b5.is_integer() == True:
            b4.append(False)
        else:
            b4.append(True)
        b5 = b2 / b8
        if b5.is_integer() == True:
            b4.append(False)
        else:
            b4.append(True)
        if all(b4):
            b3.append(b8)
    b3.sort()
    b6 = False
    while b6 = = False:
        b7 = int(random.random() * len(b3))
        b6 = fonk2(b3[b7], b2, b3[-1])
        if b6 != False:
            return b3, b2, b1, b6, int(b3[b7])
def fonk2(b8, b2, condition):
    b6 = 1
    while b6 < condition:
        if((b6 * b8) % b2 = = 1):
            return b6
        b6 += 1
    return False
def fonk3(b8, b1, a1):
    return((a1**b8)%b1)
def fonk4(b6, b1, a1):
    return((a1**b6)%b1)
def fonk5():
    b3, b2, b1, b6, b8 = fonk1(1733,1301)
    print(b3," << these are Relative Primes!\noN: ", b2,"b1: ", b1,"b6: ", b6,"b8: ", b8,"\b1")
    a1 = 2999
    print("Starting value" ,a1)
    a1 = fonk3(b8, b1, a1)
    print("Encrypted: ",a1)
    a1 = fonk4(b6, b1, a1)
    print("Decrypted",a1)
fonk5()