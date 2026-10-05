def is_anagram(s1, s2):
    s2_list = list(s2)
    index_s1 = 0
    is_still_ok = True
    while index_s1 < len(s1) and is_still_ok:
        index_s2 = 0
        found = False
        while index_s2 < len(s2_list) and not found:
            if s1[index_s1] == s2_list[index_s2]:
                found = True
            else:
                index_s2 += 1
        if found:
            s2_list[index_s2] = None
        else:
            is_still_ok = False
        index_s1 += 1
    return is_still_ok
print(is_anagram('ey edip', 'pide ye'))