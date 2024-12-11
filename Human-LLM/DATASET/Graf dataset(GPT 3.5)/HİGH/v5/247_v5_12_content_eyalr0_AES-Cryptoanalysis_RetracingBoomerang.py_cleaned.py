from byte_utils import bytes_from_hex
from keys500 import key
from softAESr import AESr
from AESUtils import mix_col, SBOX, getGmulInv, Gmul
import numpy as np
import matplotlib.pyplot as plt
b1 = False
b2 = True
a1 = 6
def fonk1(a, b):
    b3 = [[] for _ in range(256)]
    for k in range(256):
        b4 = SBOX[a ^ k] ^ SBOX[b ^ k]
        b3[b4].append(k)
    return b3
def fonk2(array, b5):
    if b5 = = 0:
        return np.array([array[0], array[5], array[10], array[15]], b6 = np.uint8)
    raise ValueError("Unsupported column number")
def fonk3(state, key, col):
    b7 = fonk2(state, col)
    b8 = fonk2(key, col)
    return mix_col(b7, b8)
def fonk4(p0, ptag0, k0, diff0_index):
    b9 = SBOX[p0 ^ k0] ^ SBOX[ptag0 ^ k0]
    b10 = [(2, 3), (1, 2), (1, 1), (3, 1)]
    coef0, b11 = b10[diff0_index]
    b12 = getGmulInv(b11)
    b13 = Gmul(b12, Gmul(coef0, b9))
    return diff2k5[b13]
def fonk5(p0, ptag0, diff0_index):
    b14 = {}
    for k0 in range(256):
        b15 = fonk4(p0, ptag0, k0, diff0_index)
        if len(b15) in (2, 4):
            b14[k0] = b15
        elif len(b15) != 0:
            raise ValueError('get_key_pairs - invalid length of b15')
    return b14
def fonk6(keys, pairs, b16 = 0):
    b17 = []
    for j, key_hex in enumerate(keys):
        for i, pair in enumerate(pairs):
            b18 = bytes_from_hex(key_hex)
            b19 = fonk3(pair[0], b18, 0)
            b20 = fonk3(pair[1], b18, 0)
            b4 = b19 ^ b20
            if b4[b16] == 0:
                b17.append([j, i])
    return b17
