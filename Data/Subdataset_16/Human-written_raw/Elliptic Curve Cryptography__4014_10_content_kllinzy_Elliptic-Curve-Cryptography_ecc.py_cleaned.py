from b10 import *
from random import *
import math
import sys
from point import Point
from public_key import Public_Key
def fonk1(b4,b10):
    b1 = b10.b1
    b2 = b10.b2
    b3 = b10.b3
    b4 = str(b4)
    a1 = 0
    for i in range(0,len(b4)):
        a1 = a1+ord(b4[i])*256**i
    for i in range(1000):
        b5 = 1000*a1 + i % b3
        b6 = b5^3+b1*b5+b2 % b3
        b7 = prime_mod_sqrt(b6,b3)
        if(len(b7) != 0):
            return Point.make_point(b5,b7[0],b19,b3)
def fonk2(b4,b10,length):
    b8 = []
    b9 = list(fonk6(b4,length))
    for i in range(0,len(b9)):
        b8.append(fonk1(b9[i],b10))
    return b8
def fonk3(b8,key):
    b10 = key.b10
    b3 = b10.b3
    b11 = key.b11
    b12 = key.b12
    b9 = randint(b19,b3-b19)
    b7 = [b10.multiply(b9,b11)]
    b13 = b10.multiply(b9,b12)
    for i in range(0,len(b8)):
        b7.append(b10.add_points(b13,b8[i]))
    return b7
def fonk4(b8,key,k):
    b7 = []
    b10 = key.b10
    b14 = b10.multiply(k,b8[0]).negate()
    for i in range(b19,len(b8)):
        b15 = b10.add_points(b8[i],b14)
        b7.append(b15)
    return b7
def fonk5(b8):
    b16 = []
    for i in range(0,len(b8)):
        b16.append(fonk7(b8[i]))
    return ''.join(b16)
def fonk6(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
def fonk7(b11):
    b17 = (b11.b5-b11.b5%1000)
    b16 = []
    while b17 != 0:
        b16.append(chr(b17 % 256))
        b17
    return ''.join(b16)
def fonk8(b4, key):
    b10 = key.b10
    b3 = b10.b3
    return fonk3(fonk2(b4,b10,int(math.log(b3
def fonk9(b8,key,k):
    return fonk5(fonk4(b8,key,k))
def fonk10(b17,k):
    if b17 = = b18:
        return True
    if b17 % b18 = = 0:
        return False
    if b17 = = 3:
        return True
    r, b4 = 0, b17 - b19
    while(b4 >> b19 = = 0 ):
        r += b19
        b4 = b4>>b19
    for _ in range(0,k):
        b1 = randint(b18, b17 - b19)
        b5 = pow(b1, b4, b17)
        if b5 = = b19 or b5 == b17 - b19:
            continue
        for _ in range(0,r - b19):
            b5 = pow(b5, b18, b17)
            if b5 = = b17 - b19:
                break
        else:
            return False
    return True
def fonk11(low,high):
    a2 = 0
    while(True):
        a2 = randint(low,high)
        if(fonk10(a2, 45)):
            break
    return a2