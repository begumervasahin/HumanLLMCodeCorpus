
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
b1 = {i: c for i, c in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
b2 = {
    1: ['alef', '\u05D0', ''], 2: ['bet', '\u05D1', 'B'], 3: ['gimel', '\u05D2', 'G'],
    4: ['dalet', '\u05D3', 'D'], 5: ['he', '\u05D4', 'H'], 6: ['vav', '\u05D5', 'V'],
    7: ['zayin', '\u05D6', 'Z'], 8: ['het', '\u05D7', 'H'], 9: ['tet', '\u05D8', 'T'],
    10: ['yud', '\u05D9', 'Y'], 20: ['kaf', '\u05DB', 'K'], 30: ['lamed', '\u05DC', 'L'],
    40: ['mem', '\u05DE', 'M'], 50: ['nun', '\u05E0', 'N'], 60: ['samekh', '\u05E1', 'S'],
    70: ['ayin', '\u05E2', ''], 80: ['pe', '\u05E4', 'P'], 90: ['tsadi', '\u05E6', 'TS'],
    100: ['kuf', '\u05E7', 'K'], 200: ['resh', '\u05E8', 'R'], 300: ['shin', '\u05E9', 'SH'], 400: ['tav', '\u05EA', 'T']
}
b3 = {
    20: ['final kaf', '\u05DA'], 40: ['final mem', '\u05DD'],
    50: ['final nun', '\u05DF'], 80: ['final pe', '\u05E3'],
    90: ['final tsadi', '\u05E5']
}
def fonk1(start, a1):
    while True:
        yield fonk2(start, a1)
        start *= 2
def fonk2(b5, a1, b4 = ''):
    if b5 = = 0:
        return b4 or '0'
    if 2 <= a1 <= 36:
        return fonk2(b5
    return fonk2(b5
def fonk3(b5, a1, b4 = 0, power=0):
    if not b5:
        return b4
    if 2 <= a1 <= 36:
        return fonk3(b5[:-1], a1, b4 + b1.index(b5[-1]) * (a1 ** power), power + 1)
    integer_part, b6 = (b5.split('.') + [''])[:2]
    return fonk3(integer_part, a1, b4 + int(b6) * (a1 ** power), power + 1)
def fonk4(b5, a1):
    b7 = fonk3(b5, a1)
    if b7 < a1:
        return b5
    if 2 <= a1 <= 36:
        return fonk4(fonk2(sum(b1.index(c) for c in b5), a1), a1)
    return fonk4(fonk2(sum(int(c) for c in b5.split('.')), a1), a1)
if b8 = = "__main__":
    a1 = 10
    a2 = 1
    b9 = fonk1(a2, a1)
    for _ in range(10):
        print(next(b9))