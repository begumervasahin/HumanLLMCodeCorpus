from byte_utils import bytes_from_hex
from keys500 import b8
from softAESr import AESr
from AESUtils import mix_col, SBOX, getGmulInv, Gmul
from collections import defaultdict
import pickle
import numpy as np
import matplotlib.pyplot as plt
b1 = False
b2 = True
a1 = 6
def fonk1(a, b):
    b3 = [[]] * 256
    for k in range(256):
        b4 = SBOX[a ^ k] ^ SBOX[b ^ k]
        b3[b4] = b3[b4] + [k]
    return b3
def fonk2(a, b5):
    if b5 = = 0:
        return np.array([a[0], a[5], a[10], a[15]], b6 = np.uint8)
    raise Exception("Unsupported col b5")
def fonk3(p, k, col):
    b7 = fonk2(p, col)
    b8 = fonk2(k, col)
    return mix_col(b7, b8)
def fonk4(p0, ptag0, k0, b10):
    global diff2k5
    b9 = SBOX[p0 ^ k0] ^ SBOX[ptag0 ^ k0]
    if b10 = = 0:
        a2 = 2
        a3 = 3
    if b10 = = 1:
        a2 = 1
        a3 = 2
    if b10 = = 2:
        a2 = 1
        a3 = 1
    if b10 = = 3:
        a2 = 3
        a3 = 1
    b11 = getGmulInv(a3)
    b12 = Gmul(b11, Gmul(a2, b9))
    return diff2k5[b12]
def fonk5(p0, ptag0, b10):
    b13 = {}
    for k0 in range(256):
        b14 = fonk4(p0, ptag0, k0, b10)
        if len(b14) == 2 or len(b14) == 4:
            b13[k0] = b14
        elif len(b14) != 0:
            print(b14)
            raise Exception('get_key_pairs - len of b14 is bad')
    return b13
def fonk6(b8, pairs, b10 = 0):
    b15 = []
    for j in range(len(b8)):
        for i in range(len(pairs)):
            b16 = bytes_from_hex(b8[j])
            b17 = fonk3(pairs[i][0], b16, 0)
            b18 = fonk3(pairs[i][1], b16, 0)
            b4 = b17 ^ b18
            if b4[b10] == 0:
                b15.append([j, i])
    return b15
