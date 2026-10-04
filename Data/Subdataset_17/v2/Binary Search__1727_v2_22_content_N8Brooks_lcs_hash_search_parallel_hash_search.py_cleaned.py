from array import array
from zlib import crc32
import multiprocessing as mp
PARALLEL = 4
def hash_function(word, base):
    return crc32(word.encode(), base)
def lcs(a, b):
    def found_common(set_a, set_b, length):
        hash_index_map = {x: i for i, x in enumerate(set_a)}
        return any(x in hash_index_map and a[hash_index_map[x]:hash_index_map[x] + length] == b[i:i + length]
                   for i, x in enumerate(set_b))
    with mp.Pool(PARALLEL) as pool:
        len_a, len_b = len(a) + 1, len(b) + 1
        if len_a > len_b:
            len_a, len_b = len_b, len_a
            a, b = b, a
        L_a = array('L', [0] * len_a)
        L_b = array('L', [0] * len_b)
        R_a = array('L', pool.starmap(hash_function, zip(a, L_a[1:])))
        R_b = array('L', pool.starmap(hash_function, zip(b, L_b[1:])))
        l, r = 0, 1
        while r < len_a and found_common(R_a, R_b, r):
            L_a, R_a = R_a, array('L', pool.starmap(hash_function,
                                                    zip((a[i:i + r] for i in range(r, len(a))), R_a[:-r])))
            L_b, R_b = R_b, array('L', pool.starmap(hash_function,
                                                    zip((b[i:i + r] for i in range(r, len(b))), R_b[:-r])))
            l, r = r, r * 2
        r = min(r, len(a))
        while l < r:
            m = (l + r)
            offset = m - l
            R_a = array('L', pool.starmap(hash_function,
                                          zip((a[i:i + offset] for i in range(offset, len(a))), L_a[:-offset])))
            R_b = array('L', pool.starmap(hash_function,
                                          zip((b[i:i + offset] for i in range(offset, len(b))), L_b[:-offset])))
            if found_common(R_a, R_b, m):
                l = m
                L_a, L_b = R_a, R_b
            else:
                r = m
        substring_locations = {x: i for i, x in enumerate(L_a)}
        common_substrings = []
        for i, x in enumerate(L_b):
            loc = substring_locations.get(x)
            if loc is not None and a[loc:loc + l] == b[i:i + l]:
                common_substrings.append(a[loc:loc + l])
    return l, common_substrings
if __name__ == "__main__":
    string_a = "abcde"
    string_b = "bcdef"
    lcs_length, lcs_strings = lcs(string_a, string_b)
    print(f"Length of LCS: {lcs_length}")
    print(f"Longest Common Substrings: {lcs_strings}")