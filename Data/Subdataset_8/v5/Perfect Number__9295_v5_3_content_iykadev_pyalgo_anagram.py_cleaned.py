def is_anagram(s1, s2):
    s2_list = list(s2)
    for char in s1:
        if char in s2_list:
            s2_list.remove(char)
        else:
            return False
    return not s2_list
print(is_anagram('ey edip', 'pide ye'))