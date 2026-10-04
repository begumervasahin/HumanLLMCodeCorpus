import math
from Crypto.Util import number
import os
def fonk1(b12,b1):
    if b12%b1 = = 0:
        return b1
    else:
        return fonk1(b1,b12%b1)
def fonk2(b12, b1):
     if b1 = = 0:
         return 1, 0, b12
     else:
         x, b3, b2 = fonk2(b1, b12 % b1)
         x, b3 = b3, (x - (b12
         return x, b3, b2
def fonk3(b14,b2):
    b4 = b14*b2
    b5 = (b14-1)*(b2-1)
    b6 = []
    for b7 in range(2,b5-1):
        if fonk1(b7,b5)==1:
            b6.append(b7)
            break
    b7 = b6[0]
    b8 = fonk2(-b5,b7)[1]
    if b8 < 0:
        b8 = b8 + b5
    else:
        b8 = b8
    b8 = (b8+b5) if (b8<0) else b8
    return b4,b5,b7,b8
def fonk4(b13,b7,b4):
    print("[*]encrypt...")
    return fonk6(b13,b7,b4)
def fonk5(b15,b8,b4):
    print("[*]decrypt.....")
    return fonk6(b15,b8,b4)
def fonk6(b1, b7, b13):
    a1 = 1
    while b7 != 0:
        if (b7&1) == 1:
            a1 = (a1 * b1) % b13
        b7 >>= 1
        b1 = (b1*b1) % b13
    return a1
def fonk7(b15):
    b9 = ''
    for item in b15:
        b10 = bin(int(ord(item)))[2:]
        while len(b10)!=8:
            b10 = '0'+str(b10)
        b9 = b9 + b10
    return int(str(b9),2)
def fonk8(num):
    b10 = bin(num)[2:]
    while len(b10)%8!=0:
        b10 = '0' + b10
    b11 = ''
    for i in range(len(b10)
        b12 = int(b10[8*i:8*(i+1)],2)
        b11 += chr(b12)
    return b11
def fonk9(b15):
    b13 = fonk7(b15)
    print('[*]this is num....', b13)
    b14 = number.getPrime(256, os.urandom)
    print("[*]getp..",b14)
    b2 = number.getPrime(256, os.urandom)
    print("[*]getq..",b2)
    print("[*]start....")
    b4,b5,b7,b8 = fonk3(b14,b2)
    b15 = fonk4(b13,b7,b4)
    a1 = fonk8(b15)
    print(a1)
if b16 = = "__main__":
    b15 = "Hi,this is RSA!"
    fonk9(b15)