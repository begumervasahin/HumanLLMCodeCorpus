from array import array
from zlib import crc32
import multiprocessing as mp
a1 = 4
def fonk1(word, base):
    return crc32(word.encode(), base)
def fonk2(a, b3):
    def fonk3(set_a, set_b, length):
        b1 = {x: i for i, x in enumerate(set_a)}
        return any(x in b1 and a[b1[x]:b1[x] + length] == b3[i:i + length]
                   for i, x in enumerate(set_b))
    with mp.Pool(a1) as pool:
        len_a, b2 = len(a) + 1, len(b3) + 1
        if len_a > b2:
            len_a, b2 = b2, len_a
            a, b3 = b3, a
        b4 = array('L', [0] * len_a)
        b5 = array('L', [0] * b2)
        b6 = array('L', pool.starmap(hash_function, zip(a, b4[1:])))
        b7 = array('L', pool.starmap(hash_function, zip(b3, b5[1:])))
        b11, b8 = 0, 1
        while b8 < len_a and fonk3(b6, b7, b8):
            b4, b6 = b6, array('L', pool.starmap(hash_function,
                                                    zip((a[i:i + b8] for i in range(b8, len(a))), b6[:-b8])))
            b5, b7 = b7, array('L', pool.starmap(hash_function,
                                                    zip((b3[i:i + b8] for i in range(b8, len(b3))), b7[:-b8])))
            b11, b8 = b8, b8 * 2
        b8 = min(b8, len(a))
        while b11 < b8:
            b9 = (b11 + b8)
            b10 = b9 - b11
            b6 = array('L', pool.starmap(hash_function,
                                          zip((a[i:i + b10] for i in range(b10, len(a))), b4[:-b10])))
            b7 = array('L', pool.starmap(hash_function,
                                          zip((b3[i:i + b10] for i in range(b10, len(b3))), b5[:-b10])))
            if fonk3(b6, b7, b9):
                b11 = b9
                b4, b5 = b6, b7
            else:
                b8 = b9
        b12 = {x: i for i, x in enumerate(b4)}
        b13 = []
        for i, x in enumerate(b5):
            b14 = b12.get(x)
            if b14 is not None and a[b14:b14 + b11] == b3[i:i + b11]:
                b13.append(a[b14:b14 + b11])
    return b11, b13
if b15 = = "__main__":
    b16 = "abcde"
    b17 = "bcdef"
    lcs_length, b18 = fonk2(b16, b17)
    print(f"Length of LCS: {lcs_length}")
    print(f"Longest Common Substrings: {b18}")