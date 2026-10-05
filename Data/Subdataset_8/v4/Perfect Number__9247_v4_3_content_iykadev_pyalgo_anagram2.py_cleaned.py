def is_anagram(s1, s2):
    s1_list = sorted(list(s1))
    s2_list = sorted(list(s2))
    index = 0
    matches = True
    while index < len(s1) and matches:
        if s1_list[index] == s2_list[index]:
            index += 1
        else:
            matches = False
    return matches
print(is_anagram('ey edip', 'pide ye'))