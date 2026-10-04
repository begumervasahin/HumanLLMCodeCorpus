from math import floor, ceil
from sys import stdout as so
from bisect import bisect
def fonk1(b14, b5):
    a1 = 32
    b1 = (1 << a1) - 1
    b2 = (b1 + 1)
    b3 = 2 * b2
    b4 = 3 * b2
    b5 = {a: b5[a] for a in b5 if b5[a] > 0}
    b6 = [0]
    for a in b5:
        b6.append(b6[-1] + b5[a])
    b6.pop()
    b6 = {a: freq for a, freq in zip(b5, b6)}
    b7 = []
    b11, b8 = 0, b1
    a2 = 0
    for k, symbol in enumerate(b14):
        if k % b9 = = 0:
            so.write(f'Arithmetic encoded {int(floor(k / len(b14) * b9))}%    \r')
            so.flush()
        b10 = b8 - b11 + 1
        b11 = int(ceil(b11 + b6[symbol] * b10))
        b8 = int(floor(b11 + b5[symbol] * b10))
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
            elif b2 <= b11 < b4 and b2 <= b8 < b4:
                a2 += 1
                b11 -= b2
                b8 -= b2
            else:
                break
            b11 *= 2
            b8 = 2 * b8 + 1
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
    b1 = (1 << a1) - 1
    b2 = (b1 + 1)
    b3 = 2 * b2
    b4 = 3 * b2
    b5 = {a: b5[a] for a in b5 if b5[a] > 0}
    b12 = list(b5)
    b6 = [0]
    for a in b5:
        b6.append(b6[-1] + b5[a])
    b6.pop()
    b13 = list(b5.values())
    b7.extend([0] * a1)
    b14 = [0] * n
    b15 = int(''.join(map(str, b7[:a1])), 2)
    b16 = a1
    b11, b8 = 0, b1
    a3 = 0
    while a3 < n:
        if a3 % b9 = = 0:
            so.write(f'Arithmetic decoded {int(floor(a3 / n * b9))}%    \r')
            so.flush()
        b10 = b8 - b11 + 1
        b17 = bisect(b6, (b15 - b11) / b10) - 1
        b14[a3] = b12[b17]
        b11 = int(ceil(b11 + b6[b17] * b10))
        b8 = int(floor(b11 + b13[b17] * b10))
        if b11 = = b8:
            raise ValueError('Zero interval!')
        while True:
            if b8 < b3:
                pass
            elif b11 >= b3:
                b11 -= b3
                b8 -= b3
                b15 -= b3
            elif b2 <= b11 < b4 and b2 <= b8 < b4:
                b11 -= b2
                b8 -= b2
                b15 -= b2
            else:
                break
            b11 *= 2
            b8 = 2 * b8 + 1
            b15 = 2 * b15 + b7[b16]
            b16 += 1
        a3 += 1
    return b14