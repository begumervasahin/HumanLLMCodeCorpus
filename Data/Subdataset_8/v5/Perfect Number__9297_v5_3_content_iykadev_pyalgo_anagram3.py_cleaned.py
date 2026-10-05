def is_anagram(s1, s2):
    count_s1 = [0] * 26
    count_s2 = [0] * 26
    for char in s1:
        pos = ord(char) - ord('a')
        count_s1[pos] += 1
    for char in s2:
        pos = ord(char) - ord('a')
        count_s2[pos] += 1
    for i in range(26):
        if count_s1[i] != count_s2[i]:
            return False
    return True
print(is_anagram('pide', 'epid'))