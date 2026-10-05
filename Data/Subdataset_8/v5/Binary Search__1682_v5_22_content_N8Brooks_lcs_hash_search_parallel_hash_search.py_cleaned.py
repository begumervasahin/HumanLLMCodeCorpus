from array import array
from zlib import crc32
import multiprocessing as mp
PARALLEL = 4
def hash_function(word, base):
    return crc32(word.encode(), base)
def found_common(set_a, set_b, m, a, b):
    set_a_indices = {x: i for i, x in enumerate(set_a)}
    return any(x in set_a_indices and a[set_a_indices[x]:set_a_indices[x] + m] == b[i:i + m]
               for i, x in enumerate(set_b))
def compute_hashes(strings, base):
    return array('L', [0] * len(strings)), array('L', mp.starmap(hash_function, zip(strings, base[1:])))
def update_hashes(prev_hashes, new_strings, prev_hashes_trimmed):
    return prev_hashes_trimmed, array('L', mp.starmap(hash_function, zip(new_strings, prev_hashes[:-len(new_strings)])))
def find_lcs_length(a, b):
    len_a, len_b = len(a) + 1, len(b) + 1
    if len_a > len_b:
        len_a, len_b = len_b, len_a
        a, b = b, a
    l, r = 0, 1
    L_a, R_a = compute_hashes(a, a)
    L_b, R_b = compute_hashes(b, b)
    while r < len_a and found_common(R_a, R_b, r, a, b):
        L_a, R_a = update_hashes(R_a, (a[i:i + r] for i in range(r, len(a))), R_a[:-r])
        L_b, R_b = update_hashes(R_b, (b[i:i + r] for i in range(r, len(b))), R_b[:-r])
        l, r = r, r * 2
    return min(r, len(a))
def find_lcs(a, b, length):
    set_a_indices = {x: i for i, x in enumerate(L_a)}
    unique = []
    for i, x in enumerate(L_b):
        loc = set_a_indices.get(x, None)
        if loc is not None and a[loc:loc + length] == b[i:i + length]:
            unique.append(a[loc:loc + length])
    return unique
if __name__ == "__main__":
    a = "ABAB"
    b = "BABA"
    length = find_lcs_length(a, b)
    lcs_list = find_lcs(a, b, length)
    print(f"Length of LCS: {length}")
    print(f"Longest Common Substrings: {lcs_list}")