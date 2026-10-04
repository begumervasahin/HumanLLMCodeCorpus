def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    return sorted_s1 == sorted_s2
print(is_anagram('ey edip', 'pide ye'))