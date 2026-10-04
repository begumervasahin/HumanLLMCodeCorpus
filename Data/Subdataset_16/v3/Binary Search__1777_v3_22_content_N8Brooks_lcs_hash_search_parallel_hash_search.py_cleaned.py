from array import array
from zlib import crc32
import multiprocessing as mp
a1 = 4
def fonk1(word, base):
    return crc32(word.encode(), base)
def fonk2(word_list, base_list):
    with mp.Pool(a1) as pool:
        return array('L', pool.starmap(hash_function, zip(word_list, base_list)))
def fonk3(set_a, set_b, length, a, b3):
    b1 = {x: i for i, x in enumerate(set_a)}
    return any(x in b1 and a[b1[x]:b1[x] + length] == b3[i:i + length]
               for i, x in enumerate(set_b))
def fonk4(a, b3):
    len_a, b2 = len(a) + 1, len(b3) + 1
    if len_a > b2:
        len_a, b2 = b2, len_a
        a, b3 = b3, a
    b4 = array('L', [0] * len_a)
    b5 = array('L', [0] * b2)
    b6 = fonk2([a[i:i+1] for i in range(len_a)], b4[1:])
    b7 = fonk2([b3[i:i+1] for i in range(b2)], b5[1:])
    b11, b8 = 0, 1
    while b8 < len_a and fonk3(b6, b7, b8, a, b3):
        b4, b6 = b6, fonk2([a[i:i+b8] for i in range(b8, len(a))], b4[:-b8])
        b5, b7 = b7, fonk2([b3[i:i+b8] for i in range(b8, len(b3))], b5[:-b8])
        b11, b8 = b8, b8 * 2
    b8 = min(b8, len(a))
    while b11 < b8:
        b9 = (b11 + b8)
        b10 = b9 - b11
        b6 = fonk2([a[i:i+b10] for i in range(b10, len(a))], b4[:-b10])
        b7 = fonk2([b3[i:i+b10] for i in range(b10, len(b3))], b5[:-b10])
        if fonk3(b6, b7, b9, a, b3):
            b11 = b9
            b4, b5 = b6, b7
        else:
            b8 = b9
    b12 = {x: i for i, x in enumerate(b4)}
    b13 = [a[loc:loc + b11] for i, x in enumerate(b5)
                         if (loc := b12.get(x)) is not None and a[loc:loc + b11] == b3[i:i + b11]]
    return b11, b13
if b14 = = "__main__":
    b15 = "abcde"
    b16 = "bcdef"
    lcs_length, b17 = fonk4(b15, b16)
    print(f"Length of LCS: {lcs_length}")
    print(f"Longest Common Substrings: {b17}")