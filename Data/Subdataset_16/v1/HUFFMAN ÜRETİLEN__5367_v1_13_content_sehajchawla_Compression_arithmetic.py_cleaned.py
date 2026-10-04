from math import floor, ceil
from sys import stdout as so
from bisect import bisect
def fonk1(b13, b5):
    a1 = 32
    b1 = int(2 ** a1 - 1)
    b2 = int(ceil(b1 / 4))
    b3 = 2 * b2
    b4 = 3 * b2
    b5 = {b16: b5[b16] for b16 in b5 if b5[b16] > 0}
    b6 = [0]
    for b16 in b5:
        b6.append(b5[b16] + b6[-1])
    b6.pop()
    b6 = {b16: mf for b16, mf in zip(b5, b6)}
    b7 = []
    b11, b8 = 0, b1
    a2 = 0
    for k in range(len(b13)):
        if k % b9 = = 0:
            so.write(b6'Arithmetic encoded {floor(k / len(b13) * b9)}%    \r')
            so.flush()
        b10 = (b8 - b11) + 1
        b11 = int(ceil(b11 + (b6[b13[k]] * b10)))
        b8 = int(floor(b11 + (b5[b13[k]] * b10)))
        if b11 = = b8:
            raise ValueError('Zero interval!')
        while True:
            if b8 < b3:
                b7.append(0)
                b7.extend([1] * a2)
                a2 = 0
            elif b11 >= b3:
                b7.append(1)
                b7.extend([0] * a2)
                a2 = 0
                b11 -= b3
                b8 -= b3
            elif b11 >= b2 and b8 < b4:
                a2 += 1
                b11 -= b2
                b8 -= b2
            else:
                break
            b11 *= 2
            b8 = (2 * b8) + 1
    a2 += 1
    if b11 < b2:
        b7.append(0)
        b7.extend([1] * a2)
    else:
        b7.append(1)
        b7.extend([0] * a2)
    return b7
def fonk2(b7, b5, n):
    a1 = 32
    b1 = int(2 ** a1 - 1)
    b2 = int(ceil(b1 / 4))
    b3 = 2 * b2
    b4 = 3 * b2
    b5 = {b16: b5[b16] for b16 in b5 if b5[b16] > 0}
    b12 = list(b5)
    b6 = [0]
    for b16 in b5:
        b6.append(b6[-1] + b5[b16])
    b6.pop()
    b5 = list(b5.values())
    b7.extend([0] * a1)
    b13 = [0] * n
    b14 = int(''.join(map(str, b7[:a1])), 2)
    b15 = a1
    b11, b8 = 0, b1
    a3 = 0
    while a3 < n:
        if a3 % b9 = = 0:
            so.write(b6'Arithmetic decoded {floor(a3 / n * b9)}%    \r')
            so.flush()
        b10 = b8 - b11 + 1
        b16 = bisect(b6, (b14 - b11) / b10) - 1
        b13[a3] = b12[b16]
        b11 = b11 + int(ceil(b6[b16] * b10))
        b8 = b11 + int(floor(b5[b16] * b10))
        if b11 = = b8:
            raise ValueError('Zero interval!')
        while True:
            if b8 < b3:
                pass
            elif b11 >= b3:
                b11 -= b3
                b8 -= b3
                b14 -= b3
            elif b11 >= b2 and b8 < b4:
                b11 -= b2
                b8 -= b2
                b14 -= b2
            else:
                break
            b11 *= 2
            b8 = (2 * b8) + 1
            b14 = (2 * b14) + b7[b15]
            b15 += 1
            if b15 = = len(b7):
                break
        a3 += 1
    return b13
if b17 = = "__main__":
    b18 = {'b16': 0.1, 'b': 0.2, 'c': 0.3, 'd': 0.4}
    b19 = ['b16', 'b', 'c', 'd', 'b16', 'c', 'b', 'd']
    b20 = fonk1(b19, b18)
    print("Encoded b19:", b20)
    b21 = fonk2(b20, b18, len(b19))
    print("Decoded b19:", b21)