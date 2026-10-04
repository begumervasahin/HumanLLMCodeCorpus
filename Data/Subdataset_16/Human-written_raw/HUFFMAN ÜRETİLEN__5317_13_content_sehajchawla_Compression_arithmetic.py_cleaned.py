from math import floor, ceil
from sys import stdout as so
from bisect import bisect
def fonk1(b13, b5):
    a1 = 32
    b1 = int(2**a1 - 1)
    b2 = int(ceil(b1/4))
    b3 = 2*b2
    b4 = 3*b2
    b5 = dict([(b16,b5[b16]) for b16 in b5 if b5[b16]>0])
    b6 = [0]
    for b16 in b5:
        b6.append(b5[b16] + b6[-1])
    b6.pop()
    b6 = dict([(b16,mf) for b16,mf in zip(b5,b6)])
    b7 = []
    b11,b8 = 0,b1
    a2 = 0
    for k in range(len(b13)):
        if k % b9 = = 0:
            so.write('Arithmetic encoded %d%%    \r' % int(floor(k/len(b13)*b9)))
            so.flush()
        b10 = (b8 - b11) +1
        b11 = int(ceil(b11 + (b6[b13[k]]*b10)))
        b8 = int(floor(b11 + (b5[b13[k]]*b10)))
        if (b11 = = b8):
            raise NameError('Zero interval!')
        while True:
            if b8 < b3:
                b7.append(0)
                for i in range(a2):
                    b7.append(1)
                a2 = 0
            elif b11 >= b3:
                b7.append(1)
                for i in range(a2):
                    b7.append(0)
                a2 = 0
                b11 = b11 - b3
                b8 = b8-b3
            elif b11 >= b2 and b8 < b4:
                a2+=1
                b11 = b11-b2
                b8 = b8-b2
            else:
                break
            b11 *= 2
            b8 = (2*b8) + 1
    a2 += 1
    if b11 < b2:
        b7.append(0)
        for i in range(a2):
            b7.append(1)
    else:
        b7.append(1)
        for i in range(a2):
            b7.append(0)
    return(b7)
def fonk2(b7,b5,n):
    a1 = 32
    b1 = int(2**a1 - 1)
    b2 = int(ceil(b1/4))
    b3 = 2*b2
    b4 = 3*b2
    b5 = dict([(b16,b5[b16]) for b16 in b5 if b5[b16]>0])
    b12 = list(b5)
    b6 = [0]
    for b16 in b5:
        b6.append(b6[-1]+b5[b16])
    b6.pop()
    b5 = list(b5.values())
    b7.extend(a1*[0])
    b13 = n*[0]
    b14 = int(''.join(str(b16) for b16 in b7[0:a1]), 2)
    b15 = a1
    b11,b8 = 0,b1
    a3 = 0
    while 1:
        if a3 % b9 = = 0:
            so.write('Arithmetic decoded %d%%    \r' % int(floor(a3/n*b9)))
            so.flush()
        b10 = b8 - b11 + 1
        b16 = bisect(b6, (b14-b11)/b10) - 1
        b13[a3] = b12[b16]
        b11 = b11 + int(ceil(b6[b16]*b10))
        b8 = b11 + int(floor(b5[b16]*b10))
        if (b11 = = b8):
            raise NameError('Zero interval!')
        while True:
            if b8 < b3:
                pass
            elif b11 >= b3:
                b11 = b11 - b3
                b8 = b8 - b3
                b14 = b14 - b3
            elif b11 >= b2 and b8 < b4:
                b11 = b11 - b2
                b8 = b8 - b2
                b14 = b14 - b2
            else:
                break
            b11 = 2*b11
            b8 = 2*b8 + 1
            b14 = 2*b14 + b7[b15]
            b15 += 1
            if b15 = = len(b7):
                break
        a3 += 1
        if a3 = = n or b15 == len(b7):
            break
    return(b13)