from array import array
from zlib import crc32
import multiprocessing as mp
a1 = 4
def fonk1(word, base):
    return crc32(word.encode(), base)
def fonk2(set_a, set_b, m, b10, b3):
    b1 = {x: i for i, x in enumerate(set_a)}
    return any(x in b1 and b10[b1[x]:b1[x] + m] == b3[i:i + m]
               for i, x in enumerate(set_b))
def fonk3(strings, base):
    return array('L', [0] * len(strings)), array('L', mp.starmap(hash_function, zip(strings, base[1:])))
def fonk4(prev_hashes, new_strings, prev_hashes_trimmed):
    return prev_hashes_trimmed, array('L', mp.starmap(hash_function, zip(new_strings, prev_hashes[:-len(new_strings)])))
def fonk5(b10, b3):
    len_a, b2 = len(b10) + 1, len(b3) + 1
    if len_a > b2:
        len_a, b2 = b2, len_a
        b10, b3 = b3, b10
    l, b4 = 0, 1
    L_a, b5 = fonk3(b10, b10)
    L_b, b6 = fonk3(b3, b3)
    while b4 < len_a and fonk2(b5, b6, b4, b10, b3):
        L_a, b5 = fonk4(b5, (b10[i:i + b4] for i in range(b4, len(b10))), b5[:-b4])
        L_b, b6 = fonk4(b6, (b3[i:i + b4] for i in range(b4, len(b3))), b6[:-b4])
        l, b4 = b4, b4 * 2
    return min(b4, len(b10))
def fonk6(b10, b3, b11):
    b1 = {x: i for i, x in enumerate(L_a)}
    b7 = []
    for i, x in enumerate(L_b):
        b8 = b1.get(x, None)
        if b8 is not None and b10[b8:b8 + b11] == b3[i:i + b11]:
            b7.append(b10[b8:b8 + b11])
    return b7
if b9 = = "__main__":
    b10 = "ABAB"
    b3 = "BABA"
    b11 = fonk5(b10, b3)
    b12 = fonk6(b10, b3, b11)
    print(f"Length of LCS: {b11}")
    print(f"Longest Common Substrings: {b12}")