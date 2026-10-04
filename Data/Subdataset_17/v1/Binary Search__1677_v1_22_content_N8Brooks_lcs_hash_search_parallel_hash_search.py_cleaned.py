from array import array
from zlib import crc32
import multiprocessing as mp
PARALLEL = 4
def hash_function(word, base):
    return crc32(word.encode(), base)
def lcs(a, b):
    def found_common(set_a, set_b, m):
        set_a_dict = {x: i for i, x in enumerate(set_a)}
        return any(x in set_a_dict and a[set_a_dict[x]:set_a_dict[x] + m] == b[i:i + m] for i, x in enumerate(set_b))
    p = mp.Pool(PARALLEL)
    len_a, len_b = len(a) + 1, len(b) + 1
    if len_a > len_b:
        len_a, len_b = len_b, len_a
        a, b = b, a
    L_a = array('L', [0] * len_a)
    R_a = array('L', p.starmap(hash_function, zip(a, L_a[1:])))
    L_b = array('L', [0] * len_b)
    R_b = array('L', p.starmap(hash_function, zip(b, L_b[1:])))
    l, r = 0, 1
    while r < len_a and found_common(R_a, R_b, r):
        L_a, R_a = R_a, array('L', p.starmap(hash_function, zip((a[i:i + r] for i in range(r, len(a))), R_a[:-r])))
        L_b, R_b = R_b, array('L', p.starmap(hash_function, zip((b[i:i + r] for i in range(r, len(b))), R_b[:-r])))
        l, r = r, r * 2
    r = min(r, len(a))
    while l < r:
        m = (l + r)
        d = m - l
        R_a = array('L', p.starmap(hash_function, zip((a[i:i + d] for i in range(d, len(a))), L_a[:-d])))
        R_b = array('L', p.starmap(hash_function, zip((b[i:i + d] for i in range(d, len(b))), L_b[:-d])))
        if found_common(R_a, R_b, m):
            l = m
            L_a, L_b = R_a, R_b
        else:
            r = m
    set_a = {x: i for i, x in enumerate(L_a)}
    unique_substrings = []
    for i, x in enumerate(L_b):
        loc = set_a.get(x, None)
        if loc is not None and a[loc:loc + l] == b[i:i + l]:
            unique_substrings.append(a[loc:loc + l])
    return l, unique_substrings
if __name__ == "__main__":
    string_a = "abcde"
    string_b = "bcdef"
    lcs_length, lcs_strings = lcs(string_a, string_b)
    print(f"Length of LCS: {lcs_length}")
    print(f"Longest Common Substrings: {lcs_strings}")