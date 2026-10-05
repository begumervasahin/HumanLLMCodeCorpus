
import numpy as np
def fonk1(b2,d):
    b1 = []
    while b2  >=  1:
        b1.append(str(b2 % d))
        b2 = int(b2/d)
    return ''.join(b1)
def fonk2(b4,b5):
    b3 = b4 % b5
    while b4 % b5 >= 1:
        b2 = b5 * int(b4/b5) + b4 % b5
        b4 = b5
        b5 = b3
    return b3
def fonk3(b2):
    b1 = []
    b6 = []
    b7 = b2
    b8 = range(b7+1)[2:len(range(b7+1))]
    b8 = b8[1::2]
    for i in range(len(b8)):
        for j in range(len(b8)):
             b6.append(b8[i] % b8[j])
    b9 = [b6[b10:b10+len(b8)] for b10 in xrange(0, len(b6), len(b8))]
    for i in range(len(b9)):
       if b9[i].count(0) == 1:
           b1.append(b8[i])
    b1.insert(0,2)
    return b1
def fonk4(b4, b5):
    if b4 = = 0:
        return (b5, 0, 1)
    else:
        g, b11, b10 = fonk4(b5 % b4, b4)
        return (g, b10 - (b5
def fonk5(b4, m):
    g, b10, b11 = fonk4(b4, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return b10 % m