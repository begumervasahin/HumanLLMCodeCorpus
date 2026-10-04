from array import array
from zlib import crc32
import multiprocessing as mp
a1 = 4
def fonk1(word, base):
    return crc32(word.encode(), base)
def fonk2(b12, set_b, a, b3, b10):
    b1 = {x: i for i, x in enumerate(b12)}
    return any(x in b1 and a[b1[x]:b1[x]+b10] == b3[i:i+b10] for i, x in enumerate(set_b))
def fonk3(b2, s, length, prev_hashes):
    return array('L', b2.starmap(hash_function, zip((s[i:i+length] for i in range(length, len(s))), prev_hashes[:-length])))
def fonk4(a, b3):
    b2 = mp.Pool(a1)
    if len(a) > len(b3):
        a, b3 = b3, a
    len_a, b4 = len(a) + 1, len(b3) + 1
    b5 = array('L', [0] * len_a)
    b6 = fonk3(b2, a, 1, b5[1:])
    b7 = array('L', [0] * b4)
    b8 = fonk3(b2, b3, 1, b7[1:])
    b11, b9 = 0, 1
    while b9 < len_a and fonk2(b6, b8, a, b3, b9):
        b5, b6 = b6, fonk3(b2, a, b9, b6)
        b7, b8 = b8, fonk3(b2, b3, b9, b8)
        b11, b9 = b9, b9 * 2
    b9 = min(b9, len(a))
    while b11 < b9:
        b10 = (b11 + b9)
        b6 = fonk3(b2, a, b10 - b11, b5)
        b8 = fonk3(b2, b3, b10 - b11, b7)
        if fonk2(b6, b8, a, b3, b10):
            b11 = b10
            b5, b7 = b6, b8
        else:
            b9 = b10
    b12 = {x: i for i, x in enumerate(b5)}
    b13 = []
    for i, x in enumerate(b7):
        b14 = b12.get(x)
        if b14 is not None and a[b14:b14+b11] == b3[i:i+b11]:
            b13.append(a[b14:b14+b11])
    return b11, b13