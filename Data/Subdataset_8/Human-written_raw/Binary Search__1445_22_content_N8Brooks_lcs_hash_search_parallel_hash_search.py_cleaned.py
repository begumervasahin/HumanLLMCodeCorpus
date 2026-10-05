
from array import array
from zlib import crc32
import multiprocessing as mp
PARALLEL = 4
def hash_function(word, base):
    return crc32(word.encode(), base)
def lcs(a, b):
    p = mp.Pool(PARALLEL)
    def found_common(set_a, set_b, m):
        set_a = {x:i for i, x in enumerate(set_a)}
        return any(x in set_a and a[set_a[x]:set_a[x]+m] == \
            b[i:i+m] for i, x in enumerate(set_b))
    len_a, len_b = len(a) + 1, len(b) + 1
    if len_a > len_b:
        len_a, len_b = len_b, len_a
        a, b = b, a
    l, r = 0, 1
    L_a = array('L', [0]*len_a)
    R_a = array('L', p.starmap(hash_function, zip(a, L_a[1:])))
    L_b = array('L', [0]*len_b)
    R_b = array('L', p.starmap(hash_function, zip(b, L_b[1:])))
    while r < len_a and found_common(R_a, R_b, r):
        L_a, R_a = R_a, array('L', p.starmap(hash_function, zip((a[i:i+r] \
            for i in range(r, len(a))), R_a[:-r])))
        L_b, R_b = R_b, array('L', p.starmap(hash_function, zip((b[i:i+r] \
            for i in range(r, len(b))), R_b[:-r])))
        l, r = r, r * 2
    r = min(r, len(a))
    while l < r:
        m = (l + r)
        d = m-l
        R_a = array('L', p.starmap(hash_function, zip((a[i:i+d] \
            for i in range(d, len(a))), L_a[:-d])))
        R_b = array('L', p.starmap(hash_function, zip((b[i:i+d] \
            for i in range(d, len(a))), L_b[:-d])))
        if found_common(R_a, R_b, m):
            l = m
            L_a, L_b = R_a, R_b
        else:
            r = m
    set_a = {x:i for i, x in enumerate(L_a)}
    unique = list()
    for i, x in enumerate(L_b):
        loc = set_a.get(x, None)
        if loc is not None and a[loc:loc+m] == b[i:i+m]:
            unique.append(a[loc:loc+m])
    return l, unique