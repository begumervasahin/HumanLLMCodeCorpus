def is_anagram(s1, s2):
    count_s1 = [0] * 26
    count_s2 = [0] * 26
    for char in s1:
        pos = ord(char) - ord('a')
        count_s1[pos] += 1
    for char in s2:
        pos = ord(char) - ord('a')
        count_s2[pos] += 1
    index = 0
    still_ok = True
    while index < 26 and still_ok:
        if count_s1[index] == count_s2[index]:
            index += 1
        else:
            still_ok = False
    return still_ok
print(is_anagram('pide', 'epid'))