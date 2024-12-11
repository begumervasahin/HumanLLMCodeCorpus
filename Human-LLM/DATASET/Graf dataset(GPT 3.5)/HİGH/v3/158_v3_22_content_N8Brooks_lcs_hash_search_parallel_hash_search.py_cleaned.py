from array import array
from zlib import crc32
import multiprocessing as mp
a1 = 4
def fonk1(word, base):
    return crc32(word.encode(), base)
def fonk2(set_a, set_b, b10, b16, b4):
    b1 = {x: i for i, x in enumerate(set_a)}
    return any(x in b1 and b16[b1[x]:b1[x] + b10] == b4[i:i + b10]
               for i, x in enumerate(set_b))
def fonk3(b16, b4):
    b2 = mp.Pool(a1)
    len_a, b3 = len(b16) + 1, len(b4) + 1
    if len_a > b3:
        len_a, b3 = b3, len_a
        b16, b4 = b4, b16
    b12, b5 = 0, 1
    b6 = array('L', [0] * len_a)
    b7 = array('L', b2.starmap(hash_function, zip(b16, b6[1:])))
    b8 = array('L', [0] * b3)
    b9 = array('L', b2.starmap(hash_function, zip(b4, b8[1:])))
    while b5 < len_a and fonk2(b7, b9, b5, b16, b4):
        b6, b7 = b7, array('L', b2.starmap(hash_function, zip((b16[i:i + b5] for i in range(b5, len(b16))), b7[:-b5])))
        b8, b9 = b9, array('L', b2.starmap(hash_function, zip((b4[i:i + b5] for i in range(b5, len(b4))), b9[:-b5])))
        b12, b5 = b5, b5 * 2
    b5 = min(b5, len(b16))
    while b12 < b5:
        b10 = (b12 + b5)
        b11 = b10 - b12
        b7 = array('L', b2.starmap(hash_function, zip((b16[i:i + b11] for i in range(b11, len(b16))), b6[:-b11])))
        b9 = array('L', b2.starmap(hash_function, zip((b4[i:i + b11] for i in range(b11, len(b16))), b8[:-b11])))
        if fonk2(b7, b9, b10, b16, b4):
            b12 = b10
            b6, b8 = b7, b9
        else:
            b5 = b10
    b1 = {x: i for i, x in enumerate(b6)}
    b13 = []
    for i, x in enumerate(b8):
        b14 = b1.get(x, None)
        if b14 is not None and b16[b14:b14 + b10] == b4[i:i + b10]:
            b13.append(b16[b14:b14 + b10])
    return b12, b13
if b15 = = "__main__":
    b16 = "ABAB"
    b4 = "BABA"
    length, b17 = fonk3(b16, b4)
    print(f"Length of LCS: {length}")
    print(f"Longest Common Substrings: {b17}")