from array import array
from zlib import crc32
import multiprocessing as mp
PARALLEL = 4
def hash_function(word, base):
    return crc32(word.encode(), base)
def found_common_substring(hash_set_a, hash_set_b, str_a, str_b, substring_length):
    hash_dict_a = {hash_value: idx for idx, hash_value in enumerate(hash_set_a)}
    return any(
        hash_value in hash_dict_a and
        str_a[hash_dict_a[hash_value]:hash_dict_a[hash_value] + substring_length] == str_b[i:i + substring_length]
        for i, hash_value in enumerate(hash_set_b)
    )
def compute_hashes(pool, string, length, previous_hashes):
    substrings = (string[i:i + length] for i in range(length, len(string)))
    return array('L', pool.starmap(hash_function, zip(substrings, previous_hashes[:-length])))
def longest_common_substring(str_a, str_b):
    with mp.Pool(PARALLEL) as pool:
        if len(str_a) > len(str_b):
            str_a, str_b = str_b, str_a
        len_a, len_b = len(str_a) + 1, len(str_b) + 1
        hash_a = array('L', [0] * len_a)
        hash_a_next = compute_hashes(pool, str_a, 1, hash_a[1:])
        hash_b = array('L', [0] * len_b)
        hash_b_next = compute_hashes(pool, str_b, 1, hash_b[1:])
        l, r = 0, 1
        while r < len_a and found_common_substring(hash_a_next, hash_b_next, str_a, str_b, r):
            hash_a, hash_a_next = hash_a_next, compute_hashes(pool, str_a, r, hash_a_next)
            hash_b, hash_b_next = hash_b_next, compute_hashes(pool, str_b, r, hash_b_next)
            l, r = r, r * 2
        r = min(r, len(str_a))
        while l < r:
            m = (l + r)
            hash_a_next = compute_hashes(pool, str_a, m - l, hash_a)
            hash_b_next = compute_hashes(pool, str_b, m - l, hash_b)
            if found_common_substring(hash_a_next, hash_b_next, str_a, str_b, m):
                l = m
                hash_a, hash_b = hash_a_next, hash_b_next
            else:
                r = m
        hash_dict_a = {hash_value: idx for idx, hash_value in enumerate(hash_a)}
        unique_lcs = []
        for i, hash_value in enumerate(hash_b):
            loc = hash_dict_a.get(hash_value)
            if loc is not None and str_a[loc:loc + l] == str_b[i:i + l]:
                unique_lcs.append(str_a[loc:loc + l])
        return l, unique_lcs