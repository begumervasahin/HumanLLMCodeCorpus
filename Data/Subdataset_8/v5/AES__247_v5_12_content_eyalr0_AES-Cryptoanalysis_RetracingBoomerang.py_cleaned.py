from byte_utils import bytes_from_hex
from keys500 import key
from softAESr import AESr
from AESUtils import mix_col, SBOX, getGmulInv, Gmul
import numpy as np
import matplotlib.pyplot as plt
verbose = False
struct_pairs = True
num_cipher_for_check = 6
def calc_key_from_diff(a, b):
    key_diff = [[] for _ in range(256)]
    for k in range(256):
        diff = SBOX[a ^ k] ^ SBOX[b ^ k]
        key_diff[diff].append(k)
    return key_diff
def get_col(array, num):
    if num == 0:
        return np.array([array[0], array[5], array[10], array[15]], dtype=np.uint8)
    raise ValueError("Unsupported column number")
def mixcol_first_round(state, key, col):
    plain = get_col(state, col)
    key_col = get_col(key, col)
    return mix_col(plain, key_col)
def get_k5(p0, ptag0, k0, diff0_index):
    diff0 = SBOX[p0 ^ k0] ^ SBOX[ptag0 ^ k0]
    coef_pairs = [(2, 3), (1, 2), (1, 1), (3, 1)]
    coef0, coef1 = coef_pairs[diff0_index]
    coef_inv5 = getGmulInv(coef1)
    diff5 = Gmul(coef_inv5, Gmul(coef0, diff0))
    return diff2k5[diff5]
def get_key_pairs(p0, ptag0, diff0_index):
    key_pairs = {}
    for k0 in range(256):
        k5 = get_k5(p0, ptag0, k0, diff0_index)
        if len(k5) in (2, 4):
            key_pairs[k0] = k5
        elif len(k5) != 0:
            raise ValueError('get_key_pairs - invalid length of k5')
    return key_pairs
def find_0diff_byte(keys, pairs, diff_index=0):
    all_0diff = []
    for j, key_hex in enumerate(keys):
        for i, pair in enumerate(pairs):
            key_arr = bytes_from_hex(key_hex)
            mixcol0 = mixcol_first_round(pair[0], key_arr, 0)
            mixcol1 = mixcol_first_round(pair[1], key_arr, 0)
            diff = mixcol0 ^ mixcol1
            if diff[diff_index] == 0:
                all_0diff.append([j, i])
    return all_0diff
