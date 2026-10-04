from array import array
from zlib import crc32
import multiprocessing as mp
a1 = 4
def fonk1(word, base):
    return crc32(word.encode(), base)
def fonk2(hash_set_a, hash_set_b, str_a, b3, substring_length):
    b1 = {hash_value: idx for idx, hash_value in enumerate(hash_set_a)}
    return any(
        hash_value in b1 and
        str_a[b1[hash_value]:b1[hash_value] + substring_length] == b3[i:i + substring_length]
        for i, hash_value in enumerate(hash_set_b)
    )
def fonk3(pool, string, length, previous_hashes):
    b2 = (string[i:i + length] for i in range(length, len(string)))
    return array('L', pool.starmap(hash_function, zip(b2, previous_hashes[:-length])))
def fonk4(str_a, b3):
    with mp.Pool(a1) as pool:
        if len(str_a) > len(b3):
            str_a, b3 = b3, str_a
        len_a, b4 = len(str_a) + 1, len(b3) + 1
        b5 = array('L', [0] * len_a)
        b6 = fonk3(pool, str_a, 1, b5[1:])
        b7 = array('L', [0] * b4)
        b8 = fonk3(pool, b3, 1, b7[1:])
        b11, b9 = 0, 1
        while b9 < len_a and fonk2(b6, b8, str_a, b3, b9):
            b5, b6 = b6, fonk3(pool, str_a, b9, b6)
            b7, b8 = b8, fonk3(pool, b3, b9, b8)
            b11, b9 = b9, b9 * 2
        b9 = min(b9, len(str_a))
        while b11 < b9:
            b10 = (b11 + b9)
            b6 = fonk3(pool, str_a, b10 - b11, b5)
            b8 = fonk3(pool, b3, b10 - b11, b7)
            if fonk2(b6, b8, str_a, b3, b10):
                b11 = b10
                b5, b7 = b6, b8
            else:
                b9 = b10
        b1 = {hash_value: idx for idx, hash_value in enumerate(b5)}
        b12 = []
        for i, hash_value in enumerate(b7):
            b13 = b1.get(hash_value)
            if b13 is not None and str_a[b13:b13 + b11] == b3[i:i + b11]:
                b12.append(str_a[b13:b13 + b11])
        return b11, b12