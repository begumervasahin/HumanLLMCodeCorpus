
import matplotlib
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
import collections
import numpy
b1 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
    17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W',
    33: 'X', 34: 'Y', 35: 'Z'
}
b2 = {
    1: ['alef', '\u05D0', ''], 2: ['bet', '\u05D1', 'B'], 3: ['gimel', '\u05D2', 'G'],
    4: ['dalet', '\u05D3', 'D'], 5: ['he', '\u05D4', 'H'], 6: ['vav', '\u05D5', 'V'],
    7: ['zayin', '\u05D6', 'Z'], 8: ['het', '\u05D7', 'H'], 9: ['tet', '\u05D8', 'T'],
    10: ['yud', '\u05D9', 'Y'], 20: ['kaf', '\u05DB', 'K'], 30: ['lamed', '\u05DC', 'L'],
    40: ['mem', '\u05DE', 'M'], 50: ['nun', '\u05E0', 'N'], 60: ['samekh', '\u05E1', 'S'],
    70: ['ayin', '\u05E2', ''], 80: ['pe', '\u05E4', 'P'],  90: ['tsadi', '\u05E6', 'TS'],
    100: ['kuf', '\u05E7', 'K'], 200: ['resh', '\u05E8', 'R'],
    300: ['shin', '\u05E9', 'SH'], 400: ['tav', '\u05EA', 'T']
}
b3 = {
    20: ['final kaf', '\u05DA'], 40: ['final mem', '\u05DD'],
    50: ['final nun', '\u05DF'], 80: ['final pe', '\u05E3'],
    90: ['final tsadi', '\u05E5']
}
def fonk1(b4, base):
    while True:
        yield fonk2(b4, base)
        b4 = b4 * 2
def fonk2(b6, base, b5 = ''):
    if b6:
        if 2 <= base <= 36:
            return fonk2(int(b6 / base), base, b1[b6 % base] + b5)
        else:
            return fonk2(int(b6 / base), base, str(b6 % base) + '.' + b5 if b5 else str(b6 % base))
    return b5
def fonk3(b6, base, b5 = 0, power=0):
    b6 = str(b6)
    if b6:
        if 2 <= base <= 36:
            return fonk3(b6[:-1], base, b5 + list(b1.values()).index(b6[-1]) * (base ** power), power + 1)
        else:
            return fonk3('.'.join(b6.split('.')[:-1]), base, b5 + int(b6.split('.')[-1]) * (base ** power), power + 1)
    return b5
def fonk4(b6, base):
    if fonk3(b6, base) >= base:
        if 2 <= base <= 36:
            return fonk4(fonk2(sum([list(b1.values()).index(elem) for elem in list(str(b6))]), base), base)
        else:
            return fonk4(fonk2(sum([int(elem) for elem in str(b6).split('.')]), base), base)
    return b6