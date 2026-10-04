from math import floor, ceil
from sys import stdout as so
from bisect import bisect
def fonk1(b18, b5):
    a1 = 32
    b1 = (1 << a1) - 1
    b2 = ceil(b1 / 4)
    b3 = 2 * b2
    b4 = 3 * b2
    b5 = {symbol: prob for symbol, prob in b5.items() if prob > 0}
    b6 = [0]
    for symbol in b5:
        b6.append(b6[-1] + b5[symbol])
    b6.pop()
    b6 = {symbol: freq for symbol, freq in zip(b5, b6)}
    b7 = []
    b11, b8 = 0, b1
    a2 = 0
    for index, symbol in enumerate(b18):
        if index % b9 = = 0:
            so.write(f'Arithmetic encoded {floor(index / len(b18) * b9)}%    \r')
            so.flush()
        b10 = (b8 - b11) + 1
        b11 = ceil(b11 + b6[symbol] * b10)
        b8 = floor(b11 + b5[symbol] * b10)
        if b11 = = b8:
            raise ValueError('Zero interval encountered!')
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
def fonk2(b7, b5, sequence_length):
    a1 = 32
    b1 = (1 << a1) - 1
    b2 = ceil(b1 / 4)
    b3 = 2 * b2
    b4 = 3 * b2
    b5 = {symbol: prob for symbol, prob in b5.items() if prob > 0}
    b12 = list(b5)
    b6 = [0]
    for prob in b5.values():
        b6.append(b6[-1] + prob)
    b6.pop()
    b5 = list(b5.values())
    b7.extend([0] * a1)
    b13 = []
    b14 = int(''.join(map(str, b7[:a1])), 2)
    b15 = a1
    b11, b8 = 0, b1
    while len(b13) < sequence_length:
        if len(b13) % b9 = = 0:
            so.write(f'Arithmetic decoded {floor(len(b13) / sequence_length * b9)}%    \r')
            so.flush()
        b10 = b8 - b11 + 1
        b16 = bisect(b6, (b14 - b11) / b10) - 1
        b13.append(b12[b16])
        b11 = b11 + ceil(b6[b16] * b10)
        b8 = b11 + floor(b5[b16] * b10)
        if b11 = = b8:
            raise ValueError('Zero interval encountered!')
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
    return b13
if b17 = = "__main__":
    b5 = {'a': 0.1, 'b': 0.2, 'c': 0.3, 'd': 0.4}
    b18 = ['a', 'b', 'c', 'd', 'a', 'c', 'b', 'd']
    b7 = fonk1(b18, b5)
    print("\nEncoded b18:", b7)
    b13 = fonk2(b7, b5, len(b18))
    print("Decoded b18:", b13)