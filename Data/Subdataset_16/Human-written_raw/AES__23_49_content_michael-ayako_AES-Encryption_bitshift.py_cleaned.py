import numpy as np
from util import logging
def fonk1(BITS):
    b1 = []
    for x in BITS:
        b2 = []
        for y in x:
            b2.append(y)
        b3 = np.asarray(b2).reshape(4,4)
        a1 = 0
        b4 = []
        b6,b7,b8,b5 = [] , [] , [] , []
        for m in b3:
            if a1 = = 0:
                b6 = [m[0],m[1],m[2],m[3]]
                b4.append(b6)
            if a1 = = 1:
                b7 = [m[1],m[2],m[3],m[0]]
                b4.append(b7)
            if a1 = = 2:
                b8 = [m[2],m[3],m[0],m[1]]
                b4.append(b8)
            if a1 = = 3:
                b5 = [m[3],m[0],m[1],m[2]]
                b4.append(b5)
            a1 += 1
        b9 = np.asarray(b4).reshape(4,4)
        b1.append(b9)
    b10 = []
    for x in b1:
        b11 = ''
        for y in x:
            for z in y:
                b11 += str(z)
        b10.append(b11)
    return b10
def fonk2(BITS):
    b1 = []
    for x in BITS:
        b2 = []
        for y in x:
            b2.append(y)
        b3 = np.asarray(b2).reshape(4,4)
        a1 = 0
        b4 = []
        b6,b7,b8,b5 = [] , [] , [] , []
        for m in b3:
            if a1 = = 0:
                b6 = [m[0],m[1],m[2],m[3]]
                b4.append(b6)
            if a1 = = 1:
                b7 = [m[3],m[0],m[1],m[2]]
                b4.append(b7)
            if a1 = = 2:
                b8 = [m[2],m[3],m[0],m[1]]
                b4.append(b8)
            if a1 = = 3:
                b5 = [m[1],m[2],m[3],m[0]]
                b4.append(b5)
            a1 += 1
        b9 = np.asarray(b4)
        b1.append(b9)
    b10 = []
    for x in b1:
        b11 = ''
        for y in x:
            for z in y:
                b11 += str(z)
        b10.append(b11)
    return b10