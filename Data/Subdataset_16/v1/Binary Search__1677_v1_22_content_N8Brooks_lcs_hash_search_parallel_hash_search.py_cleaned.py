from array import array
from zlib import crc32
import multiprocessing as mp
a1 = 4
def fonk1(word, base):
    return crc32(word.encode(), base)
def fonk2(a, b4):
    def fonk3(b13, set_b, b10):
        b1 = {x: i for i, x in enumerate(b13)}
        return any(x in b1 and a[b1[x]:b1[x] + b10] == b4[i:i + b10] for i, x in enumerate(set_b))
    b2 = mp.Pool(a1)
    len_a, b3 = len(a) + 1, len(b4) + 1
    if len_a > b3:
        len_a, b3 = b3, len_a
        a, b4 = b4, a
    b5 = array('L', [0] * len_a)
    b6 = array('L', b2.starmap(hash_function, zip(a, b5[1:])))
    b7 = array('L', [0] * b3)
    b8 = array('L', b2.starmap(hash_function, zip(b4, b7[1:])))
    b12, b9 = 0, 1
    while b9 < len_a and fonk3(b6, b8, b9):
        b5, b6 = b6, array('L', b2.starmap(hash_function, zip((a[i:i + b9] for i in range(b9, len(a))), b6[:-b9])))
        b7, b8 = b8, array('L', b2.starmap(hash_function, zip((b4[i:i + b9] for i in range(b9, len(b4))), b8[:-b9])))
        b12, b9 = b9, b9 * 2
    b9 = min(b9, len(a))
    while b12 < b9:
        b10 = (b12 + b9)
        b11 = b10 - b12
        b6 = array('L', b2.starmap(hash_function, zip((a[i:i + b11] for i in range(b11, len(a))), b5[:-b11])))
        b8 = array('L', b2.starmap(hash_function, zip((b4[i:i + b11] for i in range(b11, len(b4))), b7[:-b11])))
        if fonk3(b6, b8, b10):
            b12 = b10
            b5, b7 = b6, b8
        else:
            b9 = b10
    b13 = {x: i for i, x in enumerate(b5)}
    b14 = []
    for i, x in enumerate(b7):
        b15 = b13.get(x, None)
        if b15 is not None and a[b15:b15 + b12] == b4[i:i + b12]:
            b14.append(a[b15:b15 + b12])
    return b12, b14
if b16 = = "__main__":
    b17 = "abcde"
    b18 = "bcdef"
    lcs_length, b19 = fonk2(b17, b18)
    print(f"Length of LCS: {lcs_length}")
    print(f"Longest Common Substrings: {b19}")